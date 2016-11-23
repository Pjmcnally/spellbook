#!/usr/bin/env python
import re
from collections import Counter
from data_utils import get_file_list


def main():
    data_path = "./data/raw_data"
    data_ext = ['.md']
    # out_path = "./output"

    file_list = get_file_list(data_path, data_ext)

    duration = []
    components = []
    casting_time = []
    s_range = []

    for path in file_list:

        with open(path, 'r') as f:
            content = [line.strip() for line in f if line.strip()]

            # range_pat = re.compile(
            #     '\*\*Range\*\*:\s+'
            #     '(?P<_range>[\d\w\s]+)'
            #     '[\s()]*'
            #     '(?P<range_text>[\d\w\s\-]+)')

            cast_time_pat = re.compile(
                '\*\*Casting Time\*\*:\s+'
                '(?P<cast_time>[\d\w\s]+)'
                '[,\s]*'
                '(?P<react_text>[\d\w\s,]*)')

            match = re.search(cast_time_pat, content[8])
            cast_time = match.group("cast_time")
            react_text = match.group("react_text")

            print(cast_time, react_text)

    #         for line in content:
    #             if line.startswith("**Duration**"):
    #                 output = line[14:].lower().replace("concentration, ", "")
    #                 duration.append(output)
    #             elif line.startswith("**Casting Time**"):
    #                 casting_time.append(line[18:])
    #             elif line.startswith("**Range**"):
    #                 s_range.append(line[11:])
    #             elif line.startswith("**Components**"):
    #                 components.append(line[16:])

    # """Casting Time"""
    # print("\nSpell Cast Times and their count\n")
    # casting_time_counter = Counter(casting_time)
    # for key, value in sorted(casting_time_counter.items()):
    #     print("{} appeard {} times".format(key, value))

    # """Duration"""
    # print("\nSpell Durations and their count\n")
    # duration_counter = Counter(duration)
    # for key, value in sorted(duration_counter.items()):
    #     print("{} appeard {} times".format(key, value))

    # """Components"""
    # print("\nSpell Components and their count\n")
    # components_counter = Counter(components)
        # for x in sorted(components_counter):
    #     print(x)

    # """Spell Range"""
    # print("\nSpell Ranges and their count\n")
    # s_range_counter = Counter(s_range)
    # print("\nSpell Ranges\n")
    # for x in sorted(s_range_counter):
    #     print(x)


if __name__ == '__main__':
    main()
