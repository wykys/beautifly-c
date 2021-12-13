#!/usr/bin/env python3
# wykys 2018

import argparse
import os

UNCRUSTIFY_CONFIG = '~/.config/uncrustify.cfg'


class Beautifly:
    def __init__(self, path):
        for p in self.find_files(path):
            self.beautifly(p)

    def check_extension(self, name):
        extensions = ('.c', '.cpp', '.c++', '.h', '.hpp', '.h++')
        for e in extensions:
            if len(name) > len(e) and name[-len(e):] == e:
                return True
        return False

    def find_files(self, path='.'):
        if not os.path.exists(path):
            print('Error: path {} not exits.'.format(path))
            exit(-1)

        if os.path.isfile(path):
            return [path]

        path += '/' if path[-1] != '/' else ''
        files = []
        for fil in os.scandir(path):
            if fil.is_dir():
                files.extend(self.find_files(path + fil.name))
            elif self.check_extension(fil.name):
                files.append(path + fil.name)
        return sorted(files)

    def beautifly(self, path):
        os.system('uncrustify -c {} --replace --no-backup {}'.format(UNCRUSTIFY_CONFIG, path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='The script runs uncrustify for the specified file, or recursively to the specified folder.'
    )
    parser.add_argument(
        '-f',
        '--file',
        dest='path',
        action='store',
        default='.',
        help='destination source or header file',
    )
    Beautifly(parser.parse_args().path)
