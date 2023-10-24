'''Structures classes module'''

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


class Node:
    '''Base Tree Node Class'''

    def __init__(self, obj):
        self.obj = obj
        self.father = None
        self.left = None
        self.right = None

    def to_father(self, node):
        '''Set ascendant node'''
        self.father = node

    def to_left(self, node):
        '''Set left descendant node'''
        self.left = node

    def to_right(self, node):
        '''Set right descendant node'''
        self.right = node

    def from_father(self):
        '''Get ascendant node'''
        return self.father

    def from_right(self):
        '''Get right descendant node'''
        return self.right

    def from_left(self):
        '''Get left descendant node'''
        return self.left

    def get_item(self):
        '''Get current node contents'''
        return self.obj

    def set_item(self, item):
        '''Set current node contents'''
        self.obj = item


class Tree:
    '''Base Tree Class'''

    def __init__(self, obj):
        self.cnt = 0
        self.root = Node(obj)

    def get_root(self):
        '''Binary tree root function'''
        return self.root

    def add(self, obj):
        '''Add first in the root'''
        self.add_node(obj, self.root)
        self.cnt += 1

    def add_node(self, obj, target, direction=-1):
        '''Add the next ones in the tree'''
        if target is None:
            node = Node(obj)
            node.to_father(target)
            return node
        if target.get_item().__cmp__(obj) < 0:
            self.cnt += 1
            node = self.add_node(obj, target.from_right(), direction)
            target.to_right(node)
        else:
            self.cnt += 1
            node = self.add_node(obj, target.from_left(), direction)
            target.to_left(node)
        return target

    def count(self):
        '''Return count over addition'''
        return self.cnt

    def read(self):
        '''Read base node contents'''
        return self.read_node(self.root)

    def read_node(self, node):
        '''Read next node contents'''
        lst = ""
        if node is not None:
            left = node.from_left()
            right = node.from_right()
            lst = node.get_item().get_path()+"\n"+self.read_node(left)+self.read_node(right)
        return lst

    def search(self, obj):
        '''Search base node function'''
        return self.search_node(obj, self.root)

    def search_node(self, obj, target):
        '''Search next node function'''
        if obj is None or target is None:
            return None
        comp = target.get_item().__cmp__(obj)
        if comp == 0:
            return target
        elif comp > 0:
            return self.search_node(obj, target.from_left())
        else:
            return self.search_node(obj, target.from_right())

    def contains(self, obj):
        '''Check if obj exists on tree'''
        node = self.search(obj)
        return node is not None


class AVLNode(Node):
    '''Balanced Binary Search Tree Node Class'''

    def __init__(self, obj):
        Node.__init__(self, obj)
        self.height = 0
        self.deltah = 0

    def delta_h(self, target, direction):
        '''Height delta function'''
        if not target:
            if direction:
                self.father.from_right()
            else:
                self.father.from_left()
            h = self.height+1
        else:
            h = target.height
        self.deltah = self.height-h

    def __str__(self):
        return f'Node with height {self.height} and delta height {self.deltah}'


class AVLTree(Tree):
    '''Balanced Binary Search Tree Class'''

    def __init__(self, obj):
        Tree.__init__(self, obj)
        self.root = AVLNode(obj)
        self.height = 0
        self.depth = 0
        self.path = []

    def add(self, obj):
        self.add_node(obj, self.root, -1)
        self.cnt += 1
        if self.height > self.depth:
            self.depth = self.height
        self.height = 0
        self.path = []

    def add_node(self, obj, target, direction=-1):
        self.height += 1
        depthpath = len(self.path)
        if depthpath:
            last = self.path[len(self.path)-1]
        else:
            last = self.root
        if target:
            self.path.append(target)
            if target.get_item().__cmp__(obj) < 0:
                node = self.add_node(obj, target.from_right(), 1)
                target.to_right(node)
            else:
                node = self.add_node(obj, target.from_left(), 0)
                target.to_left(node)
        else:
            node = AVLNode(obj)
            node.height = self.height
            node.to_father(last)
            if direction:
                node.delta_h(last.from_right(), 1)
            elif direction is -1:
                node.deltah = 0
            else:
                node.delta_h(last.from_left(), 0)
            return node
        return target

    def width(self):
        '''Balanced binary search tree width function'''
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("Option not already implemented.")

    def get_path(self):
        '''Balanced binary search tree path generator function'''
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("Option not already implemented.")

    def rotate_left(self):
        '''Balanced binary search tree left rotation function'''
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("Option not already implemented.")

    def rotate_right(self):
        '''Balanced binary search tree right rotation function'''
        try:
            raise NotImplementedError
        except NotImplementedError:
            print("Option not already implemented.")
