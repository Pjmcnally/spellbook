#!/usr/bin/env python
# import re
from collections import Counter
from data_utils import get_file_list


def main():
    data_path = "./data"
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

            for line in content:
                if line.startswith("**Duration**"):
                    output = line[14:].lower().replace("concentration, ", "")
                    duration.append(output)
                elif line.startswith("**Casting Time**"):
                    casting_time.append(line[18:])
                elif line.startswith("**Range**"):
                    s_range.append(line[11:])
                elif line.startswith("**Components**"):
                    components.append(line[16:])

    """Casting Time"""
    casting_time_counter = Counter(casting_time)
    for key, value in sorted(casting_time_counter.items()):
        print("{} appeard {} times".format(key, value))

    # """Duration"""
    # duration_counter = Counter(duration)
    # for key, value in sorted(duration_counter.items()):
    #     print("{} appeard {} times".format(key, value))

    # """Components"""
    # components_counter = Counter(components)
        # for x in sorted(components_counter):
    #     print(x)

    # """Spell Range"""
    # s_range_counter = Counter(s_range)
    # for x in sorted(s_range_counter):
    #     print(x)


if __name__ == '__main__':
    main()
