"""
Qt::partial_ordering binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate


class partial_ordering(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt::partial_ordering: a plain Python object standing
  in front of one C++ Qt::partial_ordering.

  C++ hands a Qt::partial_ordering around as a copy, so every C++
  Qt::partial_ordering behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt::partial_ordering that has a ritual and that
  Python can call so far, 7 names in all: '__eq__', '__ne__', '__lt__',
  '__le__', '__gt__', '__ge__', 'isOrdered'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool operator==(QtPrivate::CompareAgainstLiteralZero a0,
    partial_ordering rhs)': takes in Python what 'bool
    operator==(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'bool operator!=(QtPrivate::CompareAgainstLiteralZero a0,
    partial_ordering rhs)': takes in Python what 'bool
    operator!=(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'bool operator<(QtPrivate::CompareAgainstLiteralZero a0,
    partial_ordering rhs)': takes in Python what 'bool
    operator>(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero a1)'
    takes.
  - Qt's 'bool operator<=(QtPrivate::CompareAgainstLiteralZero a0,
    partial_ordering rhs)': takes in Python what 'bool
    operator>=(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'bool operator>(QtPrivate::CompareAgainstLiteralZero a0,
    partial_ordering rhs)': takes in Python what 'bool
    operator<(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero a1)'
    takes.
  - Qt's 'bool operator>=(QtPrivate::CompareAgainstLiteralZero a0,
    partial_ordering rhs)': takes in Python what 'bool
    operator<=(partial_ordering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'Qt::partial_ordering::~partial_ordering()': the destructor: Python
    removes its C++ Qt::partial_ordering by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt::partial_ordering is created at the first use, not by
    'Qt::partial_ordering(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt::partial_ordering back gives a copy the ritual
    made for Python, in a new cute Qt::partial_ordering.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt::partial_ordering'

  #  Qt's '~Qt::partial_ordering()'. Naming it makes this a value class:
  #  Python owns every C++ Qt::partial_ordering behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN2Qt16partial_orderingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOrdered(self) -> bool:
    """
    Calls Qt's 'bool Qt::partial_ordering::isOrdered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt-partial_ordering.html#isOrdered
    """
    #  bool Qt::partial_ordering::isOrdered() const
    return self.uglySide.call('ritual_ZNK2Qt16partial_ordering9isOrderedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __eq__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator==(partial_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#operator==

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator==(partial_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QteqENS_16partial_orderingEN9QtPrivate25CompareAgainstLi'
        'teralZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload(THIS)
  def __eq__(self, rhs: partial_ordering) -> bool:
    """
    Calls Qt's 'bool operator==(partial_ordering lhs, partial_ordering rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#operator==

    Parameters
    ----------

    rhs : partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  bool operator==(partial_ordering lhs, partial_ordering rhs)
    return Rituals.call(
        'ritual_ZN2QteqENS_16partial_orderingES0_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __ne__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator!=(partial_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#operator!=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator!=(partial_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtneENS_16partial_orderingEN9QtPrivate25CompareAgainstLi'
        'teralZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload(THIS)
  def __ne__(self, rhs: partial_ordering) -> bool:
    """
    Calls Qt's 'bool operator!=(partial_ordering lhs, partial_ordering rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#operator!=

    Parameters
    ----------

    rhs : partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  bool operator!=(partial_ordering lhs, partial_ordering rhs)
    return Rituals.call(
        'ritual_ZN2QtneENS_16partial_orderingES0_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __lt__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator<(partial_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-partial_ordering.html#operator<

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator<(partial_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtltENS_16partial_orderingEN9QtPrivate25CompareAgainstLi'
        'teralZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __le__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator<=(partial_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#operator<=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator<=(partial_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtleENS_16partial_orderingEN9QtPrivate25CompareAgainstLi'
        'teralZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __gt__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator>(partial_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-partial_ordering.html#operator>

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator>(partial_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtgtENS_16partial_orderingEN9QtPrivate25CompareAgainstLi'
        'teralZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __ge__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator>=(partial_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#operator>=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator>=(partial_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtgeENS_16partial_orderingEN9QtPrivate25CompareAgainstLi'
        'teralZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtPrivate.Ordering)
  def __init__(self, order: QtPrivate.Ordering) -> None:
    """
    Notes what was given, for Qt's
    'Qt::partial_ordering::partial_ordering(QtPrivate::Ordering order)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#partial_ordering

    Parameters
    ----------

    order : QtPrivate.Ordering
      Passed on as its number.
    """
    #  Qt::partial_ordering::partial_ordering(QtPrivate::Ordering order)
    self._noteCreation(partial_ordering, lambda: Rituals.call(
        'ritual_ZN2Qt16partial_orderingC1EN9QtPrivate8OrderingE',
        order.value,
    ))

  @overload(QtPrivate.Uncomparable)
  def __init__(self, order: QtPrivate.Uncomparable) -> None:
    """
    Notes what was given, for Qt's
    'Qt::partial_ordering::partial_ordering(QtPrivate::Uncomparable order)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-partial_ordering.html#partial_ordering

    Parameters
    ----------

    order : QtPrivate.Uncomparable
      Passed on as its number.
    """
    #  Qt::partial_ordering::partial_ordering(QtPrivate::Uncomparable order)
    self._noteCreation(partial_ordering, lambda: Rituals.call(
        'ritual_ZN2Qt16partial_orderingC1EN9QtPrivate12UncomparableE',
        order.value,
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
