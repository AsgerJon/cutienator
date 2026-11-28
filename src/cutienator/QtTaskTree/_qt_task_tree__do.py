"""
QtTaskTree::Do binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Do(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::Do: a plain Python object standing in
  front of one C++ QtTaskTree::Do.

  What exists
  -----------

  No function of Qt's QtTaskTree::Do yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::Do::Do(const GroupItems &children)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Do::Do(std::initializer_list<GroupItem> children)':
    takes a type Python has no way to hand over yet.
  - Qt's 'Do &QtTaskTree::Do::operator=(const Do &other)': assignment: Python
    binds a name and has no operator for it.
  - Qt's 'QtTaskTree::Do::Do(Do &&other)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QtTaskTree::Do::swap(Do &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  5 of the 11 functions Qt declares: 2 written with the class 'QtTaskTree; 2
  leans on 'QExplicitlySharedDataPointer<QtTaskTree; 1 Qt's library has no
  name for it, and its code in Qt's source does not compile apart from its
  file.

  What to expect
  --------------

  - The C++ QtTaskTree::Do is created at the first use, not by
    'QtTaskTree::Do(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::Do.
  - Each name of Qt's QtTaskTree::Do that has no cute function yet,
    'children', 'swap', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTaskTree::Do'

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

  @overload(THIS)
  def __init__(self, other: Do) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::Do::Do(const Do &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-do.html#Do

    Parameters
    ----------

    other : Do
      Passed on as a value: Qt reads the C++ QtTaskTree::Do, which stays
      Python's own.
    """
    #  QtTaskTree::Do::Do(const Do &other)
    self._noteCreation(Do, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree2DoC1ERKS0_', self._valueOf(other),
    ))

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

  @staticmethod
  def children(*__, **_) -> Never:
    """
    Qt's 'GroupItem QtTaskTree::Do::children() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'constT' (aka
    'QtTaskTree::DoPrivate').
    """
    raise NotImplementedError(
        "'QtTaskTree.Do.children' has no cute function yet. Qt's 'GroupItem "
        "QtTaskTree::Do::children() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'constT' (aka "
        "'QtTaskTree::DoPrivate').")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::Do::swap(Do &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.Do.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::Do::swap(Do &other)': takes a type Python has no way "
        "to hand over yet.")
