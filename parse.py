#!/usr/bin/env python
# import re
import os


def get_files(path):
    files = []
    bad_files = []

    for folder in os.walk(path):
        for file in folder[2]:  # folder is a list.  The 2nd index lists files
            if "markdown" in file:
                files.append(file)
            else:
                bad_files.append(file)

    return files, bad_files


def main():
    in_path = "./data"
    # out_path = "./output"

    files, bad_files = get_files(in_path)

    print("file count = {}".format(len(files)))
    print("bad files count = {}".format(len(bad_files)))
    for x in bad_files:
        print(x)

if __name__ == '__main__':
    main()
