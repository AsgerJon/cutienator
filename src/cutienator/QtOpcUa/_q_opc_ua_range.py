"""
QOpcUaRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuarange.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaRange(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaRange: a plain Python object standing in front
  of one C++ QOpcUaRange.

  C++ hands a QOpcUaRange around as a copy, so every C++ QOpcUaRange behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaRange that has a ritual and that Python can
  call so far, 5 names in all: '__eq__', 'low', 'setLow', 'high', 'setHigh'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaRange &QOpcUaRange::operator=(const QOpcUaRange &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaRange::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QOpcUaRange::~QOpcUaRange()': the destructor: Python removes its
    C++ QOpcUaRange by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaRange is created at the first use, not by
    'QOpcUaRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaRange back gives a copy the ritual made for
    Python, in a new cute QOpcUaRange.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaRange'

  #  Qt's '~QOpcUaRange()'. Naming it makes this a value class: Python owns
  #  every C++ QOpcUaRange behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QOpcUaRangeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def low(self) -> float:
    """
    Calls Qt's 'double QOpcUaRange::low() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#low
    """
    #  double QOpcUaRange::low() const
    return self.uglySide.call('ritual_ZNK11QOpcUaRange3lowEv')

  def high(self) -> float:
    """
    Calls Qt's 'double QOpcUaRange::high() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#high
    """
    #  double QOpcUaRange::high() const
    return self.uglySide.call('ritual_ZNK11QOpcUaRange4highEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setLow(self, low: float) -> None:
    """
    Calls Qt's 'void QOpcUaRange::setLow(double low)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#setLow

    Parameters
    ----------

    low : float
      Passed on as it is.
    """
    #  void QOpcUaRange::setLow(double low)
    self.uglySide.call('ritual_ZN11QOpcUaRange6setLowEd', low)

  @overload(float)
  def setHigh(self, high: float) -> None:
    """
    Calls Qt's 'void QOpcUaRange::setHigh(double high)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#setHigh

    Parameters
    ----------

    high : float
      Passed on as it is.
    """
    #  void QOpcUaRange::setHigh(double high)
    self.uglySide.call('ritual_ZN11QOpcUaRange7setHighEd', high)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaRange) -> bool:
    """
    Calls Qt's 'bool QOpcUaRange::operator==(const QOpcUaRange &rhs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#operator==

    Parameters
    ----------

    rhs : QOpcUaRange
      Passed on as a value: Qt reads the C++ QOpcUaRange, which stays
      Python's own.
    """
    #  bool QOpcUaRange::operator==(const QOpcUaRange &rhs) const
    return self.uglySide.call(
        'ritual_ZNK11QOpcUaRangeeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaRange::QOpcUaRange()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#QOpcUaRange
    """
    #  QOpcUaRange::QOpcUaRange()
    self._noteCreation(QOpcUaRange, lambda: Rituals.call(
        'ritual_ZN11QOpcUaRangeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaRange) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaRange::QOpcUaRange(const
    QOpcUaRange &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#QOpcUaRange

    Parameters
    ----------

    a0 : QOpcUaRange
      Passed on as a value: Qt reads the C++ QOpcUaRange, which stays
      Python's own.
    """
    #  QOpcUaRange::QOpcUaRange(const QOpcUaRange &a0)
    self._noteCreation(QOpcUaRange, lambda: Rituals.call(
        'ritual_ZN11QOpcUaRangeC1ERKS_', self._valueOf(a0),
    ))

  @overload(float, float)
  def __init__(self, low: float, high: float) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaRange::QOpcUaRange(double low,
    double high)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuarange.html#QOpcUaRange

    Parameters
    ----------

    low : float
      Passed on as it is.

    high : float
      Passed on as it is.
    """
    #  QOpcUaRange::QOpcUaRange(double low, double high)
    self._noteCreation(QOpcUaRange, lambda: Rituals.call(
        'ritual_ZN11QOpcUaRangeC1Edd', low, high,
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
