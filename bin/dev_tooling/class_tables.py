"""The tables the cute classes are written by: what is the same for
every class, kept apart from the generators that read it, as
'ClassGenerator' and 'EnumGenerator'."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

#  The name Python has for each operator of C++ that takes two: the one
#  asked of what stands on the left, and the one asked of what stands on
#  the right when the left has said it cannot. For a comparison the
#  second is the comparison turned round.
BINARY_OPERATORS = {
    '+': ('__add__', '__radd__'), '-': ('__sub__', '__rsub__'),
    '*': ('__mul__', '__rmul__'), '/': ('__truediv__', '__rtruediv__'),
    '%': ('__mod__', '__rmod__'), '&': ('__and__', '__rand__'),
    '|': ('__or__', '__ror__'), '^': ('__xor__', '__rxor__'),
    '<<': ('__lshift__', '__rlshift__'),
    '>>': ('__rshift__', '__rrshift__'),
    '==': ('__eq__', '__eq__'), '!=': ('__ne__', '__ne__'),
    '<': ('__lt__', '__gt__'), '<=': ('__le__', '__ge__'),
    '>': ('__gt__', '__lt__'), '>=': ('__ge__', '__le__'),
}

#  The same for an operator that takes one, and for one that changes the
#  object it is called on.
UNARY_OPERATORS = {'-': '__neg__', '+': '__pos__', '~': '__invert__'}
IN_PLACE_OPERATORS = {
    '+=': '__iadd__', '-=': '__isub__', '*=': '__imul__',
    '/=': '__itruediv__', '%=': '__imod__', '&=': '__iand__',
    '|=': '__ior__', '^=': '__ixor__', '<<=': '__ilshift__',
    '>>=': '__irshift__',
}

#  What a number type built into C++ is in Python.
PYTHON_NUMBERS = dict(
    bool='bool', float='float', double='float',
)

#  The words Python has for the names of Qt that are words of Python in
#  an enum.
PYTHON_WORDS = {'None': 'NULL', 'True': 'TRUE', 'False': 'FALSE'}

#  The sections of a class body, in order, each with its banner.
SECTION_NAMES = (
    'STATIC METHODS', 'NAMESPACE', 'GETTERS', 'SETTERS', 'NOTIFIERS',
    'Python API', 'CONSTRUCTORS', 'DOMAIN SPECIFIC', 'OPTIONAL METHODS',
    'REQUIRED METHODS', 'PARENT METHODS', 'PUBLIC METHODS',
)

#  The class of Qt whose objects Qt can watch, and tell the removal of.
#  Its cute class says so, and every class built on it inherits that.
WATCHED_NAME = 'QObject'

#  The class of Qt that everything else of Qt needs to be there first.
#  It, and every class built on it, is made at once.
APPLICATION_NAME = 'QCoreApplication'

#  The parts of Qt, each after the parts it is built on.
PART_ORDER = ('QtCore', 'QtGui', 'QtWidgets')
