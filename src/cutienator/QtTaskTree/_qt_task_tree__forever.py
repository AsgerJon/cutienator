"""
QtTaskTree::Forever binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Forever(QtTaskTree.ExecutableItem):
  """
  The cute side of Qt's QtTaskTree::Forever: a plain Python object standing
  in front of one C++ QtTaskTree::Forever.

  It is built on the cute 'QtTaskTree::ExecutableItem', as Qt's
  QtTaskTree::Forever is built on Qt's QtTaskTree::ExecutableItem, and has
  everything that class has.

  C++ hands a QtTaskTree::Forever around as a copy, so every C++
  QtTaskTree::Forever behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QtTaskTree::Forever yet. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::Forever::Forever(const GroupItems &children)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Forever::Forever(std::initializer_list<GroupItem>
    children)': takes a type Python has no way to hand over yet.
  - Qt's 'Group QtTaskTree::Forever::operator Group() const': an operator
    Python has no name for.
  - Qt's 'QtTaskTree::Forever::~Forever()': the destructor: Python removes
    its C++ QtTaskTree::Forever by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtTaskTree::Forever is created at the first use, not by
    'QtTaskTree::Forever(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtTaskTree::Forever back gives a copy the ritual made
    for Python, in a new cute QtTaskTree::Forever.
  - Each name of Qt's QtTaskTree::Forever that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::Forever'

  #  Qt's '~QtTaskTree::Forever()'. Naming it makes this a value class:
  #  Python owns every C++ QtTaskTree::Forever behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QtTaskTree7ForeverD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QtTaskTree::Forever::Forever(const GroupItems &children)': takes
      a type Python has no way to hand over yet.
    - Qt's 'QtTaskTree::Forever::Forever(std::initializer_list<GroupItem>
      children)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.Forever.__init__' has no cute function yet. Qt's "
        "'QtTaskTree::Forever::Forever(const GroupItems &children)': takes "
        "a type Python has no way to hand over yet. Qt's "
        "'QtTaskTree::Forever::Forever(std::initializer_list<GroupItem> "
        "children)': takes a type Python has no way to hand over yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
