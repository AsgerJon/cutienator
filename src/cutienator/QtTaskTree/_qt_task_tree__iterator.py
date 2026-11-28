"""
QtTaskTree::Iterator binding of the Qt C++
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


class Iterator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::Iterator: a plain Python object standing
  in front of one C++ QtTaskTree::Iterator.

  What exists
  -----------

  Every function of Qt's QtTaskTree::Iterator that has a ritual and that
  Python can call so far, 1 name in all: 'iteration'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTaskTree::Iterator::Iterator(Iterator &&other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QtTaskTree::Iterator::swap(Iterator &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Iterator::Iterator(qsizetype count, const ValueGetter
    &valueGetter)': takes a type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Iterator::Iterator(const Condition &condition)': takes
    a type Python has no way to hand over yet.
  - Qt's 'QtTaskTree::Iterator::Iterator(LazyList &&lazyList)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const void *QtTaskTree::Iterator::valuePtr() const': gives 'void',
    which has no cute class yet.

  What has no ritual
  ------------------

  3 of the 12 functions Qt declares: 2 leans on
  'QExplicitlySharedDataPointer<QtTaskTree; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QtTaskTree::Iterator is created at the first use, not by
    'QtTaskTree::Iterator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::Iterator.
  - Each name of Qt's QtTaskTree::Iterator that has no cute function yet,
    'swap', 'valuePtr', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QtTaskTree::Iterator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def iteration(self) -> int:
    """
    Calls Qt's 'qsizetype QtTaskTree::Iterator::iteration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-iterator.html#iteration
    """
    #  qsizetype QtTaskTree::Iterator::iteration() const
    return self.uglySide.call('ritual_ZNK10QtTaskTree8Iterator9iterationEv')

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
  def __init__(self, other: Iterator) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::Iterator::Iterator(const
    Iterator &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-iterator.html#Iterator

    Parameters
    ----------

    other : Iterator
      Passed on as a value: Qt reads the C++ QtTaskTree::Iterator, which
      stays Python's own.
    """
    #  QtTaskTree::Iterator::Iterator(const Iterator &other)
    self._noteCreation(Iterator, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree8IteratorC1ERKS0_', self._valueOf(other),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::Iterator::Iterator()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-iterator.html#Iterator
    """
    #  QtTaskTree::Iterator::Iterator()
    self._noteCreation(Iterator, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree8IteratorC1Ev',
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::Iterator::swap(Iterator &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.Iterator.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::Iterator::swap(Iterator &other)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def valuePtr(*__, **_) -> Never:
    """
    Qt's 'const void *QtTaskTree::Iterator::valuePtr() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.Iterator.valuePtr' has no cute function yet. Qt's "
        "'const void *QtTaskTree::Iterator::valuePtr() const': gives "
        "'void', which has no cute class yet.")
