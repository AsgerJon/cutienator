"""
QOpcUaDoubleComplexNumber binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuadoublecomplexnumber.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QOpcUaDoubleComplexNumber(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaDoubleComplexNumber: a plain Python object
  standing in front of one C++ QOpcUaDoubleComplexNumber.

  C++ hands a QOpcUaDoubleComplexNumber around as a copy, so every C++
  QOpcUaDoubleComplexNumber behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaDoubleComplexNumber that has a ritual and that
  Python can call so far, 5 names in all: '__eq__', 'real', 'setReal',
  'imaginary', 'setImaginary'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaDoubleComplexNumber
    &QOpcUaDoubleComplexNumber::operator=(const QOpcUaDoubleComplexNumber
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaDoubleComplexNumber::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaDoubleComplexNumber::~QOpcUaDoubleComplexNumber()': the
    destructor: Python removes its C++ QOpcUaDoubleComplexNumber by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaDoubleComplexNumber is created at the first use, not by
    'QOpcUaDoubleComplexNumber(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaDoubleComplexNumber back gives a copy the
    ritual made for Python, in a new cute QOpcUaDoubleComplexNumber.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaDoubleComplexNumber'

  #  Qt's '~QOpcUaDoubleComplexNumber()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaDoubleComplexNumber behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QOpcUaDoubleComplexNumberD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def real(self) -> float:
    """
    Calls Qt's 'double QOpcUaDoubleComplexNumber::real() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html#real
    """
    #  double QOpcUaDoubleComplexNumber::real() const
    return self.uglySide.call('ritual_ZNK25QOpcUaDoubleComplexNumber4realEv')

  def imaginary(self) -> float:
    """
    Calls Qt's 'double QOpcUaDoubleComplexNumber::imaginary() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html#imaginary
    """
    #  double QOpcUaDoubleComplexNumber::imaginary() const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaDoubleComplexNumber9imaginaryEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setReal(self, real: float) -> None:
    """
    Calls Qt's 'void QOpcUaDoubleComplexNumber::setReal(double real)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html#setReal

    Parameters
    ----------

    real : float
      Passed on as it is.
    """
    #  void QOpcUaDoubleComplexNumber::setReal(double real)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDoubleComplexNumber7setRealEd', real,
    )

  @overload(float)
  def setImaginary(self, imaginary: float) -> None:
    """
    Calls Qt's 'void QOpcUaDoubleComplexNumber::setImaginary(double
    imaginary)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html#setImaginary

    Parameters
    ----------

    imaginary : float
      Passed on as it is.
    """
    #  void QOpcUaDoubleComplexNumber::setImaginary(double imaginary)
    self.uglySide.call(
        'ritual_ZN25QOpcUaDoubleComplexNumber12setImaginaryEd', imaginary,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaDoubleComplexNumber) -> bool:
    """
    Calls Qt's 'bool QOpcUaDoubleComplexNumber::operator==(const
    QOpcUaDoubleComplexNumber &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html#operator==

    Parameters
    ----------

    rhs : QOpcUaDoubleComplexNumber
      Passed on as a value: Qt reads the C++ QOpcUaDoubleComplexNumber, which
      stays Python's own.
    """
    #  bool QOpcUaDoubleComplexNumber::operator==(const
    #      QOpcUaDoubleComplexNumber &rhs) const
    return self.uglySide.call(
        'ritual_ZNK25QOpcUaDoubleComplexNumbereqERKS_', self._valueOf(rhs),
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
    'QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html
    """
    #  QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber()
    self._noteCreation(QOpcUaDoubleComplexNumber, lambda: Rituals.call(
        'ritual_ZN25QOpcUaDoubleComplexNumberC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaDoubleComplexNumber) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber(const
    QOpcUaDoubleComplexNumber &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html

    Parameters
    ----------

    a0 : QOpcUaDoubleComplexNumber
      Passed on as a value: Qt reads the C++ QOpcUaDoubleComplexNumber, which
      stays Python's own.
    """
    #  QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber(const
    #      QOpcUaDoubleComplexNumber &a0)
    self._noteCreation(QOpcUaDoubleComplexNumber, lambda: Rituals.call(
        'ritual_ZN25QOpcUaDoubleComplexNumberC1ERKS_', self._valueOf(a0),
    ))

  @overload(float, float)
  def __init__(self, real: float, imaginary: float) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber(double real, double
    imaginary)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuadoublecomplexnumber.html

    Parameters
    ----------

    real : float
      Passed on as it is.

    imaginary : float
      Passed on as it is.
    """
    #  QOpcUaDoubleComplexNumber::QOpcUaDoubleComplexNumber(double real,
    #      double imaginary)
    self._noteCreation(QOpcUaDoubleComplexNumber, lambda: Rituals.call(
        'ritual_ZN25QOpcUaDoubleComplexNumberC1Edd', real, imaginary,
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
