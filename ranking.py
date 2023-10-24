'''Ranking module'''

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


from .physics import handle_collisions


def change_score(element, group, discount):
    '''Change score according to collisions handling'''
    if len(handle_collisions(element, group)) > 1:
        element.hurt(discount)


def best_score():
    '''Generate best score over engine logic'''
    try:
        raise NotImplementedError
    except NotImplementedError:
        print("Option not already implemented.")
