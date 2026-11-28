"""
QtTaskTree::For binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTaskTree/qtasktree.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtTaskTree

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class For(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTaskTree::For: a plain Python object standing in
  front of one C++ QtTaskTree::For.

  What exists
  -----------

  Every function of Qt's QtTaskTree::For that has a ritual and that Python
  can call so far, 1 name in all: '__rshift__'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'For &QtTaskTree::For::operator=(const For &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QtTaskTree::For::For(For &&other)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QtTaskTree::For::swap(For &other)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 2 leans on
  'QExplicitlySharedDataPointer<QtTaskTree; 1 Qt's library has no name for
  it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QtTaskTree::For is created at the first use, not by
    'QtTaskTree::For(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtTaskTree::For.
  - Each name of Qt's QtTaskTree::For that has no cute function yet,
    'iterator', 'swap', holds a function that raises 'NotImplementedError',
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
  __qt_class__ = 'QtTaskTree::For'

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

  @overload(WAIT['QtTaskTree.Do'])
  def __rshift__(self, doItem: QtTaskTree.Do) -> QtTaskTree.Group:
    """
    Calls Qt's 'Group operator>>(const For &forItem, const Do &doItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-for.html#operator>>

    Parameters
    ----------

    doItem : QtTaskTree.Do
      Passed on as a value: Qt reads the C++ QtTaskTree::Do, which stays
      Python's own.

    Returns
    -------

    QtTaskTree.Group
      A new cute QtTaskTree::Group around the copy Qt gave back. Python owns
      it.
    """
    #  Group operator>>(const For &forItem, const Do &doItem)
    address = Rituals.call(
        'ritual_ZN10QtTaskTreersERKNS_3ForERKNS_2DoE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(doItem),
    )
    return QtTaskTree.Group._cuteOwning(address)

  @overload.fallback
  def __rshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QtTaskTree.Iterator'])
  def __init__(self, loop: QtTaskTree.Iterator) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::For::For(const Iterator
    &loop)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-for.html#For

    Parameters
    ----------

    loop : QtTaskTree.Iterator
      Passed on as a value: Qt reads the C++ QtTaskTree::Iterator, which
      stays Python's own.
    """
    #  QtTaskTree::For::For(const Iterator &loop)
    self._noteCreation(For, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree3ForC1ERKNS_8IteratorE', self._valueOf(loop),
    ))

  @overload(int)
  def __init__(self, count: int) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::For::For(qsizetype count)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-for.html#For

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  QtTaskTree::For::For(qsizetype count)
    self._noteCreation(For, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree3ForC1Ex', count,
    ))

  @overload(THIS)
  def __init__(self, other: For) -> None:
    """
    Notes what was given, for Qt's 'QtTaskTree::For::For(const For &other)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qttasktree-for.html#For

    Parameters
    ----------

    other : For
      Passed on as a value: Qt reads the C++ QtTaskTree::For, which stays
      Python's own.
    """
    #  QtTaskTree::For::For(const For &other)
    self._noteCreation(For, lambda: Rituals.call(
        'ritual_ZN10QtTaskTree3ForC1ERKS0_', self._valueOf(other),
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
  def iterator(*__, **_) -> Never:
    """
    Qt's 'Iterator QtTaskTree::For::iterator() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'constT' (aka
    'QtTaskTree::ForPrivate').
    """
    raise NotImplementedError(
        "'QtTaskTree.For.iterator' has no cute function yet. Qt's 'Iterator "
        "QtTaskTree::For::iterator() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'constT' (aka "
        "'QtTaskTree::ForPrivate').")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtTaskTree::For::swap(For &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QtTaskTree.For.swap' has no cute function yet. Qt's 'void "
        "QtTaskTree::For::swap(For &other)': takes a type Python has no way "
        "to hand over yet.")
