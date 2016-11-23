#!/usr/bin/env python
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spellbook_proj.settings")
import django  # noqa
django.setup()

from spellbook_app.models import (  # noqa
    CastingTime, Class, Component, Duration, Level, Range, School,
    Source, SpellSource, Spell)
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


def main():
    data_path = './data/raw_data'
    data_ext = ['.md']

    file_list = get_file_list(data_path, data_ext)
    for file_path in file_list:
        with open(file_path, 'r') as f:
            content = [line.strip() for line in f if line.strip()]

            cast_time, react_text = get_or_create_casting_time(content[8])
            # _class = get_or_create_class(content)
            range_, react_text = get_or_create_range(content[9])

if __name__ == '__main__':
    main()
