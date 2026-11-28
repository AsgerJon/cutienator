"""
QOpcUaComplexNumber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuacomplexnumber.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaComplexNumber(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaComplexNumber: a plain Python object standing
  in front of one C++ QOpcUaComplexNumber.

  C++ hands a QOpcUaComplexNumber around as a copy, so every C++
  QOpcUaComplexNumber behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaComplexNumber that has a ritual and that
  Python can call so far, 5 names in all: '__eq__', 'real', 'setReal',
  'imaginary', 'setImaginary'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaComplexNumber &QOpcUaComplexNumber::operator=(const
    QOpcUaComplexNumber &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaComplexNumber::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaComplexNumber::~QOpcUaComplexNumber()': the destructor:
    Python removes its C++ QOpcUaComplexNumber by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaComplexNumber is created at the first use, not by
    'QOpcUaComplexNumber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaComplexNumber back gives a copy the ritual made
    for Python, in a new cute QOpcUaComplexNumber.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaComplexNumber'

  #  Qt's '~QOpcUaComplexNumber()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaComplexNumber behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QOpcUaComplexNumberD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def real(self) -> float:
    """
    Calls Qt's 'float QOpcUaComplexNumber::real() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuacomplexnumber.html#real
    """
    #  float QOpcUaComplexNumber::real() const
    return self.uglySide.call('ritual_ZNK19QOpcUaComplexNumber4realEv')

  def imaginary(self) -> float:
    """
    Calls Qt's 'float QOpcUaComplexNumber::imaginary() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuacomplexnumber.html#imaginary
    """
    #  float QOpcUaComplexNumber::imaginary() const
    return self.uglySide.call('ritual_ZNK19QOpcUaComplexNumber9imaginaryEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setReal(self, real: float) -> None:
    """
    Calls Qt's 'void QOpcUaComplexNumber::setReal(float real)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuacomplexnumber.html#setReal

    Parameters
    ----------

    real : float
      Passed on as it is.
    """
    #  void QOpcUaComplexNumber::setReal(float real)
    self.uglySide.call('ritual_ZN19QOpcUaComplexNumber7setRealEf', real)

  @overload(float)
  def setImaginary(self, imaginary: float) -> None:
    """
    Calls Qt's 'void QOpcUaComplexNumber::setImaginary(float imaginary)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacomplexnumber.html#setImaginary

    Parameters
    ----------

    imaginary : float
      Passed on as it is.
    """
    #  void QOpcUaComplexNumber::setImaginary(float imaginary)
    self.uglySide.call(
        'ritual_ZN19QOpcUaComplexNumber12setImaginaryEf', imaginary,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaComplexNumber) -> bool:
    """
    Calls Qt's 'bool QOpcUaComplexNumber::operator==(const
    QOpcUaComplexNumber &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacomplexnumber.html#operator==

    Parameters
    ----------

    rhs : QOpcUaComplexNumber
      Passed on as a value: Qt reads the C++ QOpcUaComplexNumber, which stays
      Python's own.
    """
    #  bool QOpcUaComplexNumber::operator==(const QOpcUaComplexNumber &rhs)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QOpcUaComplexNumbereqERKS_', self._valueOf(rhs),
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
    Notes what was given, for Qt's
    'QOpcUaComplexNumber::QOpcUaComplexNumber()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacomplexnumber.html#QOpcUaComplexNumber
    """
    #  QOpcUaComplexNumber::QOpcUaComplexNumber()
    self._noteCreation(QOpcUaComplexNumber, lambda: Rituals.call(
        'ritual_ZN19QOpcUaComplexNumberC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaComplexNumber) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaComplexNumber::QOpcUaComplexNumber(const QOpcUaComplexNumber
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacomplexnumber.html#QOpcUaComplexNumber

    Parameters
    ----------

    a0 : QOpcUaComplexNumber
      Passed on as a value: Qt reads the C++ QOpcUaComplexNumber, which stays
      Python's own.
    """
    #  QOpcUaComplexNumber::QOpcUaComplexNumber(const QOpcUaComplexNumber
    #      &a0)
    self._noteCreation(QOpcUaComplexNumber, lambda: Rituals.call(
        'ritual_ZN19QOpcUaComplexNumberC1ERKS_', self._valueOf(a0),
    ))

  @overload(float, float)
  def __init__(self, real: float, imaginary: float) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaComplexNumber::QOpcUaComplexNumber(float real, float imaginary)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuacomplexnumber.html#QOpcUaComplexNumber

    Parameters
    ----------

    real : float
      Passed on as it is.

    imaginary : float
      Passed on as it is.
    """
    #  QOpcUaComplexNumber::QOpcUaComplexNumber(float real, float imaginary)
    self._noteCreation(QOpcUaComplexNumber, lambda: Rituals.call(
        'ritual_ZN19QOpcUaComplexNumberC1Eff', real, imaginary,
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
