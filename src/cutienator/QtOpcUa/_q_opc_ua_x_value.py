"""
QOpcUaXValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaxvalue.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaXValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaXValue: a plain Python object standing in front
  of one C++ QOpcUaXValue.

  C++ hands a QOpcUaXValue around as a copy, so every C++ QOpcUaXValue behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaXValue that has a ritual and that Python can
  call so far, 5 names in all: '__eq__', 'x', 'setX', 'value', 'setValue'. It
  can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaXValue &QOpcUaXValue::operator=(const QOpcUaXValue &a0)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaXValue::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QOpcUaXValue::~QOpcUaXValue()': the destructor: Python removes its
    C++ QOpcUaXValue by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaXValue is created at the first use, not by
    'QOpcUaXValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaXValue back gives a copy the ritual made for
    Python, in a new cute QOpcUaXValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaXValue'

  #  Qt's '~QOpcUaXValue()'. Naming it makes this a value class: Python owns
  #  every C++ QOpcUaXValue behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QOpcUaXValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def x(self) -> float:
    """
    Calls Qt's 'double QOpcUaXValue::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#x
    """
    #  double QOpcUaXValue::x() const
    return self.uglySide.call('ritual_ZNK12QOpcUaXValue1xEv')

  def value(self) -> float:
    """
    Calls Qt's 'float QOpcUaXValue::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#value
    """
    #  float QOpcUaXValue::value() const
    return self.uglySide.call('ritual_ZNK12QOpcUaXValue5valueEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QOpcUaXValue::setX(double x)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QOpcUaXValue::setX(double x)
    self.uglySide.call('ritual_ZN12QOpcUaXValue4setXEd', x)

  @overload(float)
  def setValue(self, value: float) -> None:
    """
    Calls Qt's 'void QOpcUaXValue::setValue(float value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#setValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QOpcUaXValue::setValue(float value)
    self.uglySide.call('ritual_ZN12QOpcUaXValue8setValueEf', value)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaXValue) -> bool:
    """
    Calls Qt's 'bool QOpcUaXValue::operator==(const QOpcUaXValue &rhs)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#operator==

    Parameters
    ----------

    rhs : QOpcUaXValue
      Passed on as a value: Qt reads the C++ QOpcUaXValue, which stays
      Python's own.
    """
    #  bool QOpcUaXValue::operator==(const QOpcUaXValue &rhs) const
    return self.uglySide.call(
        'ritual_ZNK12QOpcUaXValueeqERKS_', self._valueOf(rhs),
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
    Notes what was given, for Qt's 'QOpcUaXValue::QOpcUaXValue()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#QOpcUaXValue
    """
    #  QOpcUaXValue::QOpcUaXValue()
    self._noteCreation(QOpcUaXValue, lambda: Rituals.call(
        'ritual_ZN12QOpcUaXValueC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaXValue) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaXValue::QOpcUaXValue(const
    QOpcUaXValue &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#QOpcUaXValue

    Parameters
    ----------

    a0 : QOpcUaXValue
      Passed on as a value: Qt reads the C++ QOpcUaXValue, which stays
      Python's own.
    """
    #  QOpcUaXValue::QOpcUaXValue(const QOpcUaXValue &a0)
    self._noteCreation(QOpcUaXValue, lambda: Rituals.call(
        'ritual_ZN12QOpcUaXValueC1ERKS_', self._valueOf(a0),
    ))

  @overload(float, float)
  def __init__(self, x: float, value: float) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaXValue::QOpcUaXValue(double x,
    float value)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaxvalue.html#QOpcUaXValue

    Parameters
    ----------

    x : float
      Passed on as it is.

    value : float
      Passed on as it is.
    """
    #  QOpcUaXValue::QOpcUaXValue(double x, float value)
    self._noteCreation(QOpcUaXValue, lambda: Rituals.call(
        'ritual_ZN12QOpcUaXValueC1Edf', x, value,
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
