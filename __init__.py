'''Engine package handler'''

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

__all__ = ["physics", "ranking", "structures", "sprites", "HAS_CPP_CORE", "CppElement", "CppElements", "IntMatrix", "FloatMatrix", "Codes"]

try:
    import _elements
    HAS_CPP_CORE = True
    CppElement = _elements.Element
    CppElements = _elements.Elements
    IntMatrix = _elements.IntMatrix
    FloatMatrix = _elements.FloatMatrix
    Codes = _elements.Codes
except ImportError:
    _elements = None
    HAS_CPP_CORE = False
    CppElement = None
    CppElements = None
    IntMatrix = None
    FloatMatrix = None
    Codes = None
