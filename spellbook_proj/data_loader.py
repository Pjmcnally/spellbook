#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "spellbook_proj.settings")
import django  # noqa
django.setup()

from spellbook_app.models import CastingTime  # noqa
from data_utils import get_file_list  # noqa


def parse(path):
    print(path)
    return path


def main():
    data_path = './data'
    data_ext = ['.md']

    file_list = get_file_list(data_path, data_ext)
    for file in file_list:
        parse(file)

if __name__ == '__main__':
    main()
