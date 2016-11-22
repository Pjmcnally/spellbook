import os
# import re


def get_files(path):
    files = []

    for file in os.walk(path):
        if ".markdown" in file:
            files.append(file)

    return files


def main():
    in_path = "./data"
    # out_path = "./output"

    files = get_files(in_path)

    print(files)
