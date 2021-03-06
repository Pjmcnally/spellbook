#!/usr/bin/env python

"""A module to parse data and save it to a datase

This module is designed to parse the files stored in data/markdown data.
It parses these files to extract spell data from D&D 5th edition and then
loads the data in to the database for this django project.

The markdown files were originally downloaded from repo located at:
https://github.com/thebombzen/grimoire.  However, they have been substatially
modified as part of this project.

Example:
    $ python data_markdown_parse.py

To Do:
    This was built as a one off to parse the files and load the database.
    There is much that could be done to improve it however, I feel it is
    already obsolete.

    If I return to it here is a list of items to consider/implement:
        * Testing
        * Implement class w/functions as methods
        * remove variables from repetitively called functions
        * Impletment error checking

"""

# Lines 4-7 import and establis a Django environment with all local settings
# and variables so that this script can directly interact with models/database.
import os
import sys
proj_path = "/home/pjmcnally/programming/spellbook/dnd/"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dnd.settings")
sys.path.append(proj_path)
import django  # noqa
django.setup()


# Lines 12-17 are normal imports. "# noqa" disables the linter for that line.
import re # noqa
from spellbook.models import (  # noqa
    CastingTime, Clss, Component, Duration, Domain, Level, Range, School,
    Source, SpellSource, Spell, SubDomain)
from data_utils import get_file_list   # noqa
from django.utils.text import slugify  # noqa


def get_or_create_casting_time(string):
    cast_time_pat = re.compile(
        '^\*\*Casting Time\*\*:\s+'
        '(?P<cast_time>[\d\w\s]+)[,\s]*'
        '(?P<react_text>[\d\w\s,]+)*\.*$')

    match = re.search(cast_time_pat, string)

    cast_time = match.group("cast_time")
    react_text = (match.group("react_text") or "")

    obj, created = CastingTime.objects.get_or_create(
        text=cast_time,
        slug=slugify(cast_time))

    return obj, react_text


def get_or_create_range(string):
    range_pat = re.compile(
        '^\*\*Range\*\*:\s+'
        '(?P<rng>[\d\w\s]+)[\s]*'
        '(?P<range_text>[()\d\w\s\-]+)*$')

    match = re.search(range_pat, string)
    rng = match.group("rng").strip()
    range_text = (match.group("range_text") or "")

    if range_text:
        range_text = range_text.replace("(", "").replace(")", "")

    obj, created = Range.objects.get_or_create(
        text=rng,
        slug=slugify(rng))

    return obj, range_text


def parse_tags(string):
    tags_pat = re.compile(
        '^tags:[\s]+'
        '\[(?P<tags>[\w\s\d,()]+)\]$')

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
            obj, created = Clss.objects.get_or_create(
                name=tag,
                slug=slugify(tag))
            class_objs.append(obj)
    return class_objs


def get_or_create_domains(tags):
    domain_pat = re.compile(
        '(?P<domain>[\w\s]+)'
        '\((?P<sub_domain>[\w\s]+)\)')

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


def open_file(path):
    with open(path, 'r') as f:
        content = f.readlines()

    return content


def get_or_create_duration(string):
    duration_pat = re.compile(
        '^\*\*Duration\*\*:\s+'
        '(?P<concentration>Concentration,)*\s*'
        '(?P<duration>[\w\s]+)')

    match = re.search(duration_pat, string)

    concentration = bool(match.group('concentration'))
    duration = match.group('duration').lower()

    obj, created = Duration.objects.get_or_create(
        text=duration,
        slug=slugify(duration))

    return obj, concentration


def get_or_create_components(string):
    comp_objs = []
    comp_pat = re.compile(
        '^\*\*Components\*\*\:\s+'
        '(?P<components>[\s\w,]+)'
        '\(*(?P<comp_text>[^\)]+)*\)*$')

    match = re.search(comp_pat, string)
    comp_string = match.group('components')
    comp_text = (match.group('comp_text') or "")

    if "V" in comp_string:
        v_obj, created = Component.objects.get_or_create(
            full_name="verbal",
            short_name="V",
            slug="v",
            sort_val=0)
        comp_objs.append(v_obj)
    if "S" in comp_string:
        s_obj, created = Component.objects.get_or_create(
            full_name="somatic",
            short_name="S",
            slug="s",
            sort_val=1)
        comp_objs.append(s_obj)
    if "M" in comp_string:
        m_obj, created = Component.objects.get_or_create(
            full_name="material",
            short_name="M",
            slug="m",
            sort_val=2)
        comp_objs.append(m_obj)

    return comp_objs, comp_text


def get_or_create_school(string):
    school_pat = re.compile(
        '.*'
        '(?P<school>abjuration|conjuration|divination|enchantment|'
        'evocation|illusion|necromancy|transmutation)'
        '.*')

    match = re.search(school_pat, string.lower())
    school = match.group('school')

    obj, created = School.objects.get_or_create(
        name=school,
        slug=slugify(school)
        )

    return obj


def get_or_create_sources(string):
    source_dict = {
        'PHB': {
            'full_name': "Player's Handbook",
            'short_name': 'PHB',
            'slug': 'phb',
            'version': 'First Printing w/corrections (August 2014)',
            'link': 'https://dnd.wizards.com/products/tabletop-games/rpg-products/rpg_playershandbook',
            'public': False},
        'SCAG': {
            'full_name': "Sword Coast Adventurer's Guide",
            'short_name': 'SCAG',
            'slug': 'scag',
            'version': 'First Printing (November 2015)',
            'link': 'https://dnd.wizards.com/products/tabletop-games/rpg-products/sc-adventurers-guide',
            'public': False},
        'EE': {
            'full_name': "Elemental Evil Player's Companion",
            'short_name': 'EE',
            'slug': 'ee',
            'version': '(March 2015)',
            'link': 'https://dnd.wizards.com/articles/features/elementalevil_playerscompanion',
            'public': False},
        'SRD': {
            'full_name': '5E System Reference Document',
            'short_name': 'SRD',
            'slug': 'srd',
            'version': '5.1',
            'link': 'https://dnd.wizards.com/articles/features/systems-reference-document-srd',
            'public': True}
    }

    source_pat = re.compile(
        '(?P<source>[A-Z]+)'
        '\.'
        '(?P<page>[\d]+)')

    sources = []

    for item in string[8:].strip().split(", "):
        match = re.search(source_pat, item)

        source = match.group('source')
        page = match.group('page')

        source_obj, created = Source.objects.get_or_create(
            full_name=source_dict[source]['full_name'],
            short_name=source_dict[source]['short_name'],
            slug=source_dict[source]['slug'],
            link=source_dict[source]['link'],
            public=source_dict[source]['public'])

        sources.append((source_obj, page))

    return sources


def create_spell(content):

    def get_line(string):
        # This dict contains key, value pairs that represent the content and
        # corresponding line number in the .md files being parsed.
        l_dict = {
            "title": 0,
            "source": 1,
            "tags": 2,
            "level_school": 4,
            "c_time": 6,
            "range": 8,
            "comp": 10,
            "dura": 12,
            "text": 14
        }

        if string != "text":
            return content[l_dict[string]]
        else:
            return content[l_dict["text"]:]

    name = get_name(get_line("title"))
    print(name)
    tags = parse_tags(get_line("tags"))
    classes = get_or_create_classes(tags)
    sub_domains = get_or_create_domains(tags)

    level = get_or_create_level(get_line("level_school"))
    school = get_or_create_school(get_line("level_school"))
    c_time, react_text = get_or_create_casting_time(get_line("c_time"))
    rng, range_text = get_or_create_range(get_line("range"))

    comps, component_text = get_or_create_components(get_line("comp"))
    duration, concentration = get_or_create_duration(get_line("dura"))
    sources = get_or_create_sources(get_line("source"))

    spell, created = Spell.objects.get_or_create(
        name=name,
        slug=slugify(name),
        text="".join(get_line("text")),
        concentration=concentration,
        ritual="ritual" in get_line("level_school").lower(),
        cast_time_text=react_text,
        component_text=component_text,
        range_text=range_text,
        casting_time=c_time,
        duration=duration,
        level=level,
        rng=rng,
        school=school,
    )

    for item in classes:
        spell.clss.add(item)

    for item in comps:
        spell.component.add(item)

    for item in sub_domains:
        spell.sub_domain.add(item)

    for source, page in sources:
        spell_source, created = SpellSource.objects.get_or_create(
            spell=spell,
            source=source,
            page=page)

    return spell


def main():
    data_path = '../../data'
    data_ext = ['.md']

    x = 0

    file_list = get_file_list(data_path, data_ext)
    for file_path in file_list:
        x += 1
        content = open_file(file_path)
        spell = create_spell(content)
        # print(x, spell)


if __name__ == '__main__':
    main()
