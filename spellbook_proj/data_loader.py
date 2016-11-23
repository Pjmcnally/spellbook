#!/usr/bin/env python
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spellbook_proj.settings")
import django  # noqa
django.setup()

from spellbook_app.models import (  # noqa
    CastingTime, Duration, SpellRange, School, CharClass, Level,
    Source, SpellSource, Component, SpellComponent, Spell)
from data_utils import get_file_list   # noqa
from django.utils.text import slugify  # noqa


def get_or_create_casting_time(line):
    cast_time_pat = re.compile(
        '\*\*Casting Time\*\*:\s+'
        '(?P<cast_time>[\d\w\s]+)'
        '[,\s]*'
        '(?P<react_text>[\d\w\s,]*)')

    match = re.search(cast_time_pat, line)
    cast_time = match.group("cast_time")
    react_text = match.group("react_text")

    obj, created = CastingTime.objects.get_or_create(text=x)

    return obj, react_text


def main():
    data_path = './data'
    data_ext = ['.md']

    file_list = get_file_list(data_path, data_ext)
    for file_path in file_list:
        with open(file_path, 'r') as f:
            content = [line.strip() for line in f if line.strip()]

            cast_time = get_or_create_casting_time(content[8])
            range_ = get_or_create_range(content[])

if __name__ == '__main__':
    main()
