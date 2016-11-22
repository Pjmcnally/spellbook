#!/usr/bin/env python
# import re
import os
from collections import Counter


def get_files(path):
    files = {}

    # os.walk creates a generator.
    # Each item in the generator is a tuple representing a folder.
    # The 0 index is the relative path of the that folder.
    # The 1 index is a list of folders in that folder.
    # The 2 index is a list of all files in that folder.
    for folder in os.walk(path):
        for file_name in folder[2]:  # The 2nd index of folder lists files
            if ".md" in file_name:
                files[file_name] = "{}/{}".format(folder[0], file_name)

    return files


def main():
    in_path = "./data"
    # out_path = "./output"

    files = get_files(in_path)

    duration = []
    components = []
    casting_time = []
    s_range = []

    for path in files.values():

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

    # casting_time_counter = Counter(casting_time)
    # duration_counter = Counter(duration)
    # components_counter = Counter(components)
    s_range_counter = Counter(s_range)

    # for key, value in sorted(duration_counter.items()):
    #     print("{} appeard {} times".format(key, value))

    # for key, value in sorted(casting_time_counter.items()):
    #     print("{} appeard {} times".format(key, value))

    # for x in sorted(components_counter):
    #     print(x)

    for x in sorted(s_range_counter):
        print(x)


if __name__ == '__main__':
    main()
