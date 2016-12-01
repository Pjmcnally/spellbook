#!/usr/bin/env python
import os


def get_file_list(path, extensions=None):
    """Creates list of file paths

    Creates list of relative file paths for all files in a given folder
    and all subfolders.  If optional extension argument is given list will
    only indlude files with given extensions.

    Args:
        path: A string representing the path you want to search from
        extensions: a sequesnce of strings each represention one file extension

    Returns:
        An array containg strings.  Each string is one file path relative to
        the given path.
    """

    file_list = []

    # os.walk creates a generator.
    # Each item in the generator is a tuple representing a folder.
    # The 0 index is the relative path of the that folder.
    # The 1 index is a list of folders in that folder.
    # The 2 index is a list of all files in that folder.
    total_path = os.walk(path)

    if extensions:
        for folder in total_path:
            for file_name in folder[2]:
                for extension in extensions:
                    if extension in file_name:
                        file_list.append("{}/{}".format(folder[0], file_name))
    else:
        for folder in total_path:
            for file_name in folder[2]:
                file_list.append("{}/{}".format(folder[0], file_name))

    return file_list
