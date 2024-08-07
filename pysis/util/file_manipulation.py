# -*- coding: utf-8 -*-

"""
Utilities to help with file manipulation.
"""

from glob import iglob
from os.path import splitext


def write_file_list(filename, file_list=[], glob=None):
    """Write a list of files to a file.

    :param filename: the name of the file to write the list to

    :param file_list: a list of filenames to write to a file

    :param glob: if glob is specified, it will ignore file_list and instead
        create a list of files based on the pattern provide by glob (ex. *.cub)
    """
    if glob:
        file_list = iglob(glob)

    with open(filename, 'w') as f:
        for line in file_list:
            f.write(line + '\n')


def file_variations(filename, extensions):
    """Create a variation of file names.

    Generate a list of variations on a filename by replacing the extension with
    a the provided list.

    :param filename: The original file name to use as a base.

    :param extensions: A list of file extensions to generate new filenames.
    """
    (label, ext) = splitext(filename)
    return [label + extension for extension in extensions]

def create_file_group(path_to_files):
    """
    Returns a list of the names of all ISIS cubes in a path. 
    Note that by default the list comes back sorted lexacographically.

    :param path_to_files: The path in which the ISIS cubes are located.
    """

    cubes = []

    for i in os.listdir():
        cubes.append(i)

    return cubes

class ImageName(str):
    def __getattr__(self, name):
        return ImageName(self + '.' + name)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self)
