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


class Space:
    '''Elements Space Class'''

    def __init__(self):
        '''Initialize Physics and Events'''
        self.events = []
        self.frames = 30

    def start_sync(self):
        '''Start controlling game time'''
        pass

    def stop_sync(self):
        '''Stop controlling game time'''
        pass

    def handle_collisions(self, sprite, group):
        '''Handle all sprite collisions in game'''
        pass

    def handle_event(self, type):
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("Option not already implemented.")
