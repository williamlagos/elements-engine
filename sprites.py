'''Sprites instances and handling module'''

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


import os


class Element:
    '''Elements Base Class'''

    def __init__(self, token, name):
        self.token = token
        self.name = name

    def __cmp__(self, other):
        t = ord(self.token[0])
        o = ord(other.token[0])
        if t > o:
            r = 1
        elif t < o:
            r = -1
        else:
            r = 0
        return r


class ElementSprite:
    '''Elements Character Class'''
    collided = False

    def __init__(self, figure, animvet, posinit, video, hitpoints=100):
        '''Initialize the variables of Character'''
        self.speed = [1, 0]
        self.count = 0
        self.tick = 15
        self.width = video[0]
        self.height = video[1]
        self.pos = posinit
        self.anim = animvet
        self.hitpoints = hitpoints
        self.element_image(figure)
        self.rect = self.rect.move(self.speed)

    def element_image(self, figure):
        '''Generates absolute path over appointed figure'''
        return os.path.abspath(os.path.join("elements", figure))

    def hurt(self, wound):
        '''Reduces character's hit points'''
        self.hitpoints -= wound

    def which_size(self, width, height):
        '''Defines size of sprite'''
        self.width = width
        self.height = height

    def which_speed(self, speed):
        '''Defines speed of sprite'''
        self.speed = speed

    def draw_anim(self):
        '''Animates the character'''
        if self.count != len(self.anim):
            if self.tick == 0:
                self.tick = 15
                self.count += 1
            else:
                self.tick -= 1
        else:
            self.count = 0

    def reverse_speed(self):
        '''Changes direction of sprite's movement '''
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]

    def update(self):
        '''Moves the sprite and animate'''
        self.draw_anim()
        if self.rect.left < 0 or self.rect.right > self.width:
            self.speed[0] = -self.speed[0]
        elif self.rect.top < 0 or self.rect.bottom > self.height:
            self.speed[1] = -self.speed[1]

    def position(self):
        '''Returns the current sprite position'''
        return self.pos

    def rectangle(self):
        '''Returns the animation base'''
        return (self.pos[0], self.pos[1],
                self.pos[0]+self.width, self.pos[1]+self.height)
