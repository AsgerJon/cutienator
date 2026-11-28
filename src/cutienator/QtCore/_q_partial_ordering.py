"""
QPartialOrdering binding of the Qt C++
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


class QPartialOrdering(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPartialOrdering: a plain Python object standing in
  front of one C++ QPartialOrdering.

  C++ hands a QPartialOrdering around as a copy, so every C++
  QPartialOrdering behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPartialOrdering that has a ritual and that Python
  can call so far, 7 names in all: '__eq__', '__ne__', '__lt__', '__le__',
  '__gt__', '__ge__', 'isOrdered'. It can be made from Python, in 5 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool operator==(QtPrivate::CompareAgainstLiteralZero a0,
    QPartialOrdering rhs)': takes in Python what 'bool
    operator==(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'bool operator!=(QtPrivate::CompareAgainstLiteralZero a0,
    QPartialOrdering rhs)': takes in Python what 'bool
    operator!=(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'bool operator<(QtPrivate::CompareAgainstLiteralZero a0,
    QPartialOrdering rhs)': takes in Python what 'bool
    operator>(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero a1)'
    takes.
  - Qt's 'bool operator<=(QtPrivate::CompareAgainstLiteralZero a0,
    QPartialOrdering rhs)': takes in Python what 'bool
    operator>=(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'bool operator>(QtPrivate::CompareAgainstLiteralZero a0,
    QPartialOrdering rhs)': takes in Python what 'bool
    operator<(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero a1)'
    takes.
  - Qt's 'bool operator>=(QtPrivate::CompareAgainstLiteralZero a0,
    QPartialOrdering rhs)': takes in Python what 'bool
    operator<=(QPartialOrdering lhs, QtPrivate::CompareAgainstLiteralZero
    a1)' takes.
  - Qt's 'Qt::partial_ordering QPartialOrdering::operator partial_ordering()
    const': an operator Python has no name for.
  - Qt's 'bool operator==(Qt::partial_ordering lhs, QPartialOrdering rhs)':
    takes in Python what 'bool operator==(QPartialOrdering lhs,
    Qt::partial_ordering rhs)' takes.
  - Qt's 'bool operator!=(Qt::partial_ordering lhs, QPartialOrdering rhs)':
    takes in Python what 'bool operator!=(QPartialOrdering lhs,
    Qt::partial_ordering rhs)' takes.
  - Qt's 'QPartialOrdering::~QPartialOrdering()': the destructor: Python
    removes its C++ QPartialOrdering by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QPartialOrdering is created at the first use, not by
    'QPartialOrdering(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPartialOrdering back gives a copy the ritual made
    for Python, in a new cute QPartialOrdering.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPartialOrdering'

  #  Qt's '~QPartialOrdering()'. Naming it makes this a value class: Python
  #  owns every C++ QPartialOrdering behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QPartialOrderingD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isOrdered(self) -> bool:
    """
    Calls Qt's 'bool QPartialOrdering::isOrdered() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#isOrdered
    """
    #  bool QPartialOrdering::isOrdered() const
    return self.uglySide.call('ritual_ZNK16QPartialOrdering9isOrderedEv')

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
    Calls Qt's 'bool operator==(QPartialOrdering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator==

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator==(QPartialOrdering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_Zeq16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZero'
        'E',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload(THIS)
  def __eq__(self, rhs: QPartialOrdering) -> bool:
    """
    Calls Qt's 'bool operator==(QPartialOrdering lhs, QPartialOrdering rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator==

    Parameters
    ----------

    rhs : QPartialOrdering
      Passed on as a value: Qt reads the C++ QPartialOrdering, which stays
      Python's own.
    """
    #  bool operator==(QPartialOrdering lhs, QPartialOrdering rhs)
    return Rituals.call(
        'ritual_Zeq16QPartialOrderingS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(WAIT['Qt.partial_ordering'])
  def __eq__(self, rhs: Qt.partial_ordering) -> bool:
    """
    Calls Qt's 'bool operator==(QPartialOrdering lhs, Qt::partial_ordering
    rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator==

    Parameters
    ----------

    rhs : Qt.partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  bool operator==(QPartialOrdering lhs, Qt::partial_ordering rhs)
    return Rituals.call(
        'ritual_Zeq16QPartialOrderingN2Qt16partial_orderingE',
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
    Calls Qt's 'bool operator!=(QPartialOrdering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator!=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator!=(QPartialOrdering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_Zne16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZero'
        'E',
        CuteMixin._valueOf(self), CuteMixin._valueOf(a1),
    )

  @overload(THIS)
  def __ne__(self, rhs: QPartialOrdering) -> bool:
    """
    Calls Qt's 'bool operator!=(QPartialOrdering lhs, QPartialOrdering rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator!=

    Parameters
    ----------

    rhs : QPartialOrdering
      Passed on as a value: Qt reads the C++ QPartialOrdering, which stays
      Python's own.
    """
    #  bool operator!=(QPartialOrdering lhs, QPartialOrdering rhs)
    return Rituals.call(
        'ritual_Zne16QPartialOrderingS_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload(WAIT['Qt.partial_ordering'])
  def __ne__(self, rhs: Qt.partial_ordering) -> bool:
    """
    Calls Qt's 'bool operator!=(QPartialOrdering lhs, Qt::partial_ordering
    rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator!=

    Parameters
    ----------

    rhs : Qt.partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  bool operator!=(QPartialOrdering lhs, Qt::partial_ordering rhs)
    return Rituals.call(
        'ritual_Zne16QPartialOrderingN2Qt16partial_orderingE',
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
    Calls Qt's 'bool operator<(QPartialOrdering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator<

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator<(QPartialOrdering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_Zlt16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZero'
        'E',
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
    Calls Qt's 'bool operator<=(QPartialOrdering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator<=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator<=(QPartialOrdering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_Zle16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZero'
        'E',
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
    Calls Qt's 'bool operator>(QPartialOrdering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator>

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator>(QPartialOrdering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_Zgt16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZero'
        'E',
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
    Calls Qt's 'bool operator>=(QPartialOrdering lhs,
    QtPrivate::CompareAgainstLiteralZero a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qpartialordering.html#operator>=

    Parameters
    ----------

    a1 : QtPrivate.CompareAgainstLiteralZero
      Passed on as a value: Qt reads the C++
      QtPrivate::CompareAgainstLiteralZero, which stays Python's own.
    """
    #  bool operator>=(QPartialOrdering lhs,
    #      QtPrivate::CompareAgainstLiteralZero a1)
    return Rituals.call(
        'ritual_Zge16QPartialOrderingN9QtPrivate25CompareAgainstLiteralZero'
        'E',
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

  @overload(WAIT['Qt.partial_ordering'])
  def __init__(self, order: Qt.partial_ordering) -> None:
    """
    Notes what was given, for Qt's
    'QPartialOrdering::QPartialOrdering(Qt::partial_ordering order)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpartialordering.html#QPartialOrdering

    Parameters
    ----------

    order : Qt.partial_ordering
      Passed on as a value: Qt reads the C++ Qt::partial_ordering, which
      stays Python's own.
    """
    #  QPartialOrdering::QPartialOrdering(Qt::partial_ordering order)
    self._noteCreation(QPartialOrdering, lambda: Rituals.call(
        'ritual_ZN16QPartialOrderingC1EN2Qt16partial_orderingE',
        self._valueOf(order),
    ))

  @overload(WAIT['Qt.weak_ordering'])
  def __init__(self, stdorder: Qt.weak_ordering) -> None:
    """
    Notes what was given, for Qt's
    'QPartialOrdering::QPartialOrdering(Qt::weak_ordering stdorder)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpartialordering.html#QPartialOrdering

    Parameters
    ----------

    stdorder : Qt.weak_ordering
      Passed on as a value: Qt reads the C++ Qt::weak_ordering, which stays
      Python's own.
    """
    #  QPartialOrdering::QPartialOrdering(Qt::weak_ordering stdorder)
    self._noteCreation(QPartialOrdering, lambda: Rituals.call(
        'ritual_ZN16QPartialOrderingC1EN2Qt13weak_orderingE',
        self._valueOf(stdorder),
    ))

  @overload(WAIT['Qt.strong_ordering'])
  def __init__(self, stdorder: Qt.strong_ordering) -> None:
    """
    Notes what was given, for Qt's
    'QPartialOrdering::QPartialOrdering(Qt::strong_ordering stdorder)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpartialordering.html#QPartialOrdering

    Parameters
    ----------

    stdorder : Qt.strong_ordering
      Passed on as a value: Qt reads the C++ Qt::strong_ordering, which stays
      Python's own.
    """
    #  QPartialOrdering::QPartialOrdering(Qt::strong_ordering stdorder)
    self._noteCreation(QPartialOrdering, lambda: Rituals.call(
        'ritual_ZN16QPartialOrderingC1EN2Qt15strong_orderingE',
        self._valueOf(stdorder),
    ))

  @overload(QtPrivate.Ordering)
  def __init__(self, order: QtPrivate.Ordering) -> None:
    """
    Notes what was given, for Qt's
    'QPartialOrdering::QPartialOrdering(QtPrivate::Ordering order)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpartialordering.html#QPartialOrdering

    Parameters
    ----------

    order : QtPrivate.Ordering
      Passed on as its number.
    """
    #  QPartialOrdering::QPartialOrdering(QtPrivate::Ordering order)
    self._noteCreation(QPartialOrdering, lambda: Rituals.call(
        'ritual_ZN16QPartialOrderingC1EN9QtPrivate8OrderingE', order.value,
    ))

  @overload(QtPrivate.LegacyUncomparable)
  def __init__(self, order: QtPrivate.LegacyUncomparable) -> None:
    """
    Notes what was given, for Qt's
    'QPartialOrdering::QPartialOrdering(QtPrivate::LegacyUncomparable
    order)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpartialordering.html#QPartialOrdering

    Parameters
    ----------

    order : QtPrivate.LegacyUncomparable
      Passed on as its number.
    """
    #  QPartialOrdering::QPartialOrdering(QtPrivate::LegacyUncomparable
    #      order)
    self._noteCreation(QPartialOrdering, lambda: Rituals.call(
        'ritual_ZN16QPartialOrderingC1EN9QtPrivate18LegacyUncomparableE',
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
