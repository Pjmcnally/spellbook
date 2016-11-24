#!/usr/bin/env python
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spellbook_proj.settings")
import django  # noqa
django.setup()

from spellbook_app.models import (  # noqa
    CastingTime, Class, Component, Duration, Domain, Level, Range, School,
    Source, SpellSource, Spell, SubDomain)
from data_utils import get_file_list   # noqa
from django.utils.text import slugify  # noqa


def get_or_create_casting_time(string):
    cast_time_pat = re.compile(
        '\*\*Casting Time\*\*:\s+'
        '(?P<cast_time>[\d\w\s]+)'
        '[,\s]*'
        '(?P<react_text>[\d\w\s,]*)')

    match = re.search(cast_time_pat, string)
    cast_time = match.group("cast_time")
    react_text = match.group("react_text")

    obj, created = CastingTime.objects.get_or_create(
        text=cast_time,
        slug=slugify(cast_time))

    return obj, react_text


def get_or_create_range(string):
    range_pat = re.compile(
        '^\*\*Range\*\*:\s+'
        '(?P<_range>[\d\w\s]+)'
        '[\s]*'
        '(?P<range_text>[()\d\w\s\-]+)*$')

    match = re.search(range_pat, string)
    _range = match.group("_range").strip()
    range_text = match.group("range_text")

    if range_text:
        range_text = range_text.replace("(", "").replace(")", "")

    obj, created = Range.objects.get_or_create(
        text=_range,
        slug=slugify(_range))

    return obj, range_text


def parse_tags(string):
    tags_pat = re.compile(
        '^tags:[\s]+'
        '\['
        '(?P<tags>[\w\s\d,()]+)'
        '\]$')

    match = re.search(tags_pat, string)

    tags = match.group('tags').split(", ")

    return tags


def get_or_create_classes(tags):
    classes = [
        'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk',
        'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']

    class_objs = []
    for tag in tags:
        if tag in classes:
            obj, created = Class.objects.get_or_create(
                name=tag,
                slug=slugify(tag))
            class_objs.append(obj)
    return class_objs


def get_or_create_domains(tags):
    domain_pat = re.compile(
        '(?P<domain>[\w\s]+)'
        '\('
        '(?P<sub_domain>[\w\s]+)')

    sub_domains = []

    for tag in tags:
        if "(" in tag:
            match = re.search(domain_pat, tag)
            domain = match.group("domain")
            sub_domain = match.group("sub_domain")

            d_obj, created = Domain.objects.get_or_create(
                name=domain,
                slug=slugify(domain))

            sd_obj, created = SubDomain.objects.get_or_create(
                name=sub_domain,
                slug=slugify(sub_domain),
                domain=d_obj)
            sub_domains.append(sd_obj)

    return sub_domains


def get_or_create_level(string):
    if "cantrip" in string:
        text = 'cantrip'
        ord_text = 'cantrip'
        slug = 'cantrip'
        num = 0
    else:
        level_pat = re.compile(
            '^\*\*'
            '(?P<num>\d)'
            '(?P<ord_text>[\w-]+)'
            '[/s.]*')
        match = re.search(level_pat, string)

        num = match.group('num')
        text = 'level ' + num
        ord_text = num + match.group('ord_text')
        slug = slugify(ord_text)

    obj, created = Level.objects.get_or_create(
            text=text,
            ord_text=ord_text,
            slug=slug,
            num=int(num))
    return obj


def get_name(string):
    name_pat = re.compile(
        'title:[\s]+\"'
        '(?P<name>[^\"]+)'
        '\"')

    match = re.search(name_pat, string)
    return match.group('name')


def get_text(strings):
    output = ""

    for string in strings:
        if output:
            output += "\n\n" + string
        else:
            output = string

    return output


def main():
    data_path = './data/raw_data'
    data_ext = ['.md']

    file_list = get_file_list(data_path, data_ext)
    for file_path in file_list:
        with open(file_path, 'r') as f:
            content = [line.strip() for line in f if line.strip()]
            tags = parse_tags(content[5])

            level = get_or_create_level(content[7])
            # school = get_or_create_school(content[7])

            cast_time, react_text = get_or_create_casting_time(content[8])
            range_, react_text = get_or_create_range(content[9])

            classes = get_or_create_classes(tags)
            sub_domains = get_or_create_domains(tags)

            name = get_name(content[2])
            text = get_text(content[12:])
            print(text)
            print(repr(text))
            a = input()

            # spell = Spell.objects.get_or_create(
            #     name=name,
            #     slug=slugify(name),
            #     text=text,


if __name__ == '__main__':
    main()
