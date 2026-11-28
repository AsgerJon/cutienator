"""
Qt::weak_ordering binding of the Qt C++
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
from . import QtPrivate, Qt


class weak_ordering(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt::weak_ordering: a plain Python object standing in
  front of one C++ Qt::weak_ordering.

  C++ hands a Qt::weak_ordering around as a copy, so every C++
  Qt::weak_ordering behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt::weak_ordering that has a ritual and that Python
  can call so far, 6 names in all: '__eq__', '__ne__', '__lt__', '__le__',
  '__gt__', '__ge__'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'partial_ordering Qt::weak_ordering::operator partial_ordering()
    const': an operator Python has no name for.
  - Qt's 'bool operator==(QtPrivate::CompareAgainstLiteralZero a0,
    weak_ordering rhs)': takes in Python what 'bool operator==(weak_ordering
    lhs, QtPrivate::CompareAgainstLiteralZero a1)' takes.
  - Qt's 'bool operator!=(QtPrivate::CompareAgainstLiteralZero a0,
    weak_ordering rhs)': takes in Python what 'bool operator!=(weak_ordering
    lhs, QtPrivate::CompareAgainstLiteralZero a1)' takes.
  - Qt's 'bool operator<(QtPrivate::CompareAgainstLiteralZero a0,
    weak_ordering rhs)': takes in Python what 'bool operator>(weak_ordering
    lhs, QtPrivate::CompareAgainstLiteralZero a1)' takes.
  - Qt's 'bool operator<=(QtPrivate::CompareAgainstLiteralZero a0,
    weak_ordering rhs)': takes in Python what 'bool operator>=(weak_ordering
    lhs, QtPrivate::CompareAgainstLiteralZero a1)' takes.
  - Qt's 'bool operator>(QtPrivate::CompareAgainstLiteralZero a0,
    weak_ordering rhs)': takes in Python what 'bool operator<(weak_ordering
    lhs, QtPrivate::CompareAgainstLiteralZero a1)' takes.
  - Qt's 'bool operator>=(QtPrivate::CompareAgainstLiteralZero a0,
    weak_ordering rhs)': takes in Python what 'bool operator<=(weak_ordering
    lhs, QtPrivate::CompareAgainstLiteralZero a1)' takes.
  - Qt's 'bool operator==(partial_ordering lhs, weak_ordering rhs)': takes in
    Python what 'bool operator==(weak_ordering lhs, partial_ordering rhs)'
    takes.
  - Qt's 'bool operator!=(partial_ordering lhs, weak_ordering rhs)': takes in
    Python what 'bool operator!=(weak_ordering lhs, partial_ordering rhs)'
    takes.
  - Qt's 'Qt::weak_ordering::~weak_ordering()': the destructor: Python
    removes its C++ Qt::weak_ordering by it, and has no other use for it.

  What to expect
  --------------

  - The C++ Qt::weak_ordering is created at the first use, not by
    'Qt::weak_ordering(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt::weak_ordering back gives a copy the ritual made
    for Python, in a new cute Qt::weak_ordering.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt::weak_ordering'

  #  Qt's '~Qt::weak_ordering()'. Naming it makes this a value class: Python
  #  owns every C++ Qt::weak_ordering behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN2Qt13weak_orderingD1Ev'

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

  @overload(WAIT['QtPrivate.CompareAgainstLiteralZero'])
  def __eq__(self, a1: QtPrivate.CompareAgainstLiteralZero) -> bool:
    """
    Calls Qt's 'bool operator==(weak_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator==

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator==(weak_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QteqENS_13weak_orderingEN9QtPrivate25CompareAgainstLiter'
        'alZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload(THIS)
  def __eq__(self, rhs: weak_ordering) -> bool:
    """
    Calls Qt's 'bool operator==(weak_ordering lhs, weak_ordering rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator==

    Parameters
    ----------

    rhs : weak_ordering
      Passed on as a value: Qt reads the C++ Qt::weak_ordering, which stays
      Python's own.
    """
    #  bool operator==(weak_ordering lhs, weak_ordering rhs)
    return Rituals.call(
        'ritual_ZN2QteqENS_13weak_orderingES0_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(WAIT['Qt.partial_ordering'])
  def __eq__(self, rhs: Qt.partial_ordering) -> bool:
    """
    Calls Qt's 'bool operator==(weak_ordering lhs, partial_ordering rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator==

    Parameters
    ----------

    rhs : Qt.partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  bool operator==(weak_ordering lhs, partial_ordering rhs)
    return Rituals.call(
        'ritual_ZN2QteqENS_13weak_orderingENS_16partial_orderingE',
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
    Calls Qt's 'bool operator!=(weak_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator!=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator!=(weak_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtneENS_13weak_orderingEN9QtPrivate25CompareAgainstLiter'
        'alZeroE',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload(THIS)
  def __ne__(self, rhs: weak_ordering) -> bool:
    """
    Calls Qt's 'bool operator!=(weak_ordering lhs, weak_ordering rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator!=

    Parameters
    ----------

    rhs : weak_ordering
      Passed on as a value: Qt reads the C++ Qt::weak_ordering, which stays
      Python's own.
    """
    #  bool operator!=(weak_ordering lhs, weak_ordering rhs)
    return Rituals.call(
        'ritual_ZN2QtneENS_13weak_orderingES0_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(WAIT['Qt.partial_ordering'])
  def __ne__(self, rhs: Qt.partial_ordering) -> bool:
    """
    Calls Qt's 'bool operator!=(weak_ordering lhs, partial_ordering rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator!=

    Parameters
    ----------

    rhs : Qt.partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  bool operator!=(weak_ordering lhs, partial_ordering rhs)
    return Rituals.call(
        'ritual_ZN2QtneENS_13weak_orderingENS_16partial_orderingE',
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
    Calls Qt's 'bool operator<(weak_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator<

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator<(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
    #      a1)
    return Rituals.call(
        'ritual_ZN2QtltENS_13weak_orderingEN9QtPrivate25CompareAgainstLiter'
        'alZeroE',
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
    Calls Qt's 'bool operator<=(weak_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator<=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator<=(weak_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtleENS_13weak_orderingEN9QtPrivate25CompareAgainstLiter'
        'alZeroE',
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
    Calls Qt's 'bool operator>(weak_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator>

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator>(weak_ordering lhs, QtPrivate::CompareAgainstLiteralZero
    #      a1)
    return Rituals.call(
        'ritual_ZN2QtgtENS_13weak_orderingEN9QtPrivate25CompareAgainstLiter'
        'alZeroE',
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
    Calls Qt's 'bool operator>=(weak_ordering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qt-weak_ordering.html#operator>=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator>=(weak_ordering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_ZN2QtgeENS_13weak_orderingEN9QtPrivate25CompareAgainstLiter'
        'alZeroE',
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
    'Qt::weak_ordering::weak_ordering(QtPrivate::Ordering order)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt-weak_ordering.html#weak_ordering

    Parameters
    ----------

    order : QtPrivate.Ordering
      Passed on as its number.
    """
    #  Qt::weak_ordering::weak_ordering(QtPrivate::Ordering order)
    self._noteCreation(weak_ordering, lambda: Rituals.call(
        'ritual_ZN2Qt13weak_orderingC1EN9QtPrivate8OrderingE', order.value,
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
