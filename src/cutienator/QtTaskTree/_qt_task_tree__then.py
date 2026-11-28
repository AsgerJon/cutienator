"""
QtTaskTree::Then binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qconditional.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class Then(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::Then: a plain Python object standing in
  front of one C++ QtTaskTree::Then.

  What exists
  -----------

  No function of Qt's QtTaskTree::Then yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::Then::Then(const GroupItems &children)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Then::Then(std::initializer_list<GroupItem> children)':
    takes a type Python has no way to hand over yet.
  - Qt's 'Then &QtTaskTree::Then::operator=(const Then &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QtTaskTree::Then::Then(Then &&other)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QtTaskTree::Then::swap(Then &other)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 9 functions Qt declares: 2 leans on
  'QExplicitlySharedDataPointer<QtTaskTree; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QtTaskTree::Then is created at the first use, not by
    'QtTaskTree::Then(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::Then.
  - Each name of Qt's QtTaskTree::Then that has no cute function yet, 'body',
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QtTaskTree::Then'

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
  def __init__(self, other: Then) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::Then::Then(const Then
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-then.html#Then

    Parameters
    ----------

    other : Then
      Passed on as a value: Qt reads the C++ QtTaskTree::Then, which stays
      Python's own.
    """
    #  QtTaskTree::Then::Then(const Then &other)
    self._noteCreation(Then, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree4ThenC1ERKS0_', self._valueOf(other),
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
  def body(*__, **_) -> Never:
    """
    Qt's 'Group QtTaskTree::Then::body() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'constT' (aka
    'QtTaskTree::ThenPrivate').
    """
    raise NotImplementedError(
        "'QtTaskTree.Then.body' has no cute function yet. Qt's 'Group "
        "QtTaskTree::Then::body() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'constT' (aka "
        "'QtTaskTree::ThenPrivate').")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::Then::swap(Then &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.Then.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::Then::swap(Then &other)': takes a type Python has no "
        "way to hand over yet.")
