'''CLI module for testing without a server'''

#
# This file is part of elements project.
#
# Copyright (C) 2009-2023 William Oliveira de Lagos <william.lagos@icloud.com>
#
# Elements is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Elements is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with elements.  If not, see <http://www.gnu.org/licenses/>.
#


import sys
import pickle

from subprocess import Popen
from argparse import ArgumentParser
from configparser import ConfigParser, NoSectionError


def main(*argv):
    '''Execute the tools for Elements Core.'''

    parser = ArgumentParser(
        prog='Elements CLI',
        description='CLI for testing elements headless engine')
    parser.add_argument('-p', '--program', dest='program',
                        help='Execute the selected program', metavar='FILE')
    parser.add_argument('-a', '--core-activate', dest='cactive',
                        action='store_true', help='Activate one or more micro-modules')
    parser.add_argument('-d', '--core-deactivate', dest='cdeactive',
                        action='store_true', help='Deactivate one or more micro-modules')
    parser.add_argument('-i', '--information', dest='info',
                        action='store_true', help='Show information about the engine.')
    options = parser.parse_args(argv[1:])

    z = Core(True)
    if options.cactive:
        z.configure_core(1)
    elif options.cdeactive:
        z.configure_core()
    elif options.info:
        z.test_libs()
    elif options.program:
        cmd = f'python {options.program}'
        exct = Popen(cmd.split())
        exct.wait()
    else:
        print('Unrecognized option. Digit -h for help.')


class Version():
    '''Version Manager Class'''

    def __init__(self, v, m, y):
        self.vers = v
        self.year = y
        self.month = m


class Core():
    '''Elements Core Class'''

    def __init__(self, boolean=False):
        '''Initialize the Core switch'''
        self.zkready = boolean

    def create_info(self, v, m, y):
        '''Create version binary data'''
        verfile = open('ver.dat', 'w', encoding='utf-8')
        versnow = Version(v, m, y)
        pickle.dump(versnow, verfile)
        verfile.close()

    def show_info(self):
        '''Show information about the platform'''
        verfile = open('ver.dat', 'r', encoding='utf-8')
        versnow = pickle.load(verfile)
        version = versnow.vers
        month = versnow.month
        year = versnow.year
        print(f'elements Platform Alpha {version}')
        print(f'Updated in {month}/{year}.')
        verfile.close()

    def configure_core(self, option=0):
        '''Configure the Elements Core with ZConf'''
        cfg = Config()
        if option == 0:
            cfg.change_conf()
        else:
            cfg.change_conf('activate')

    def test_libs(self, times=0):
        '''Do some tests with embedded libs on elements'''
        while times < 3:
            print('What do you want to do?\n'
                  '1. Verify if Pygame is installed.\n'
                  '2. Test animation with Elements.\n'
                  '3. Draw a cube with PyOpenGL.\n')
            choice = input('Select one of the options:')
            choice = '1'
            if choice == '1':
                try:
                    # print('Pygame : '+pygame.version.ver)
                    print('Pygame is now installed.')
                except ImportError:
                    print('Pygame isn\'t installed.')
                break
            elif choice == '2':
                # import game
                # game.Game([640,480])
                break
            elif choice == '3':
                # import depth
                # depth.cube_demo()
                break
            else:
                print('Invalid option. Try again.')
                times = times + 1


class Config():
    '''Elements Configuration Class'''

    def __init__(self):
        '''Prepare the configuration of Elements'''
        conf = ConfigParser()
        try:
            conf.read('euph.cfg')
        except NoSectionError:
            print('Problems with ZConf. Check the euph.cfg file.')

    def change_conf(self, option='deactivate'):
        '''Turn off or on the switches on Elements'''
        conf = ConfigParser()

        try:
            conf.read('euph.cfg')
            file = open('euph.cfg', 'w', encoding='utf-8')
            items = conf.items('Core')
        except NoSectionError:
            print('Problems with ZConf. Check the euph.cfg file.')

        if option == 'deactivate':
            for i in items:
                if i[1] == 'True':
                    print(i[0]+': '+i[1])
            choice = input('Select the sector to deactivate:')
            conf.set('Core', choice, False)
            conf.write(file)
        elif option == 'activate':
            for i in items:
                if i[1] == 'False':
                    print(i[0]+': '+i[1])
            choice = input('Select the sector to activate:')
            conf.set('Core', choice, True)
            conf.write(file)


if __name__ == '__main__':
    sys.exit(main(*sys.argv))
