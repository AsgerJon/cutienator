"""
QJSNumberCoercion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qjsnumbercoercion.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QJSNumberCoercion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QJSNumberCoercion: a plain Python object standing in
  front of one C++ QJSNumberCoercion.

  C++ hands a QJSNumberCoercion around as a copy, so every C++
  QJSNumberCoercion behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QJSNumberCoercion that has a ritual and that Python
  can call so far, 9 names in all: 'isInteger', 'isArrayIndex', 'toInteger',
  'equals', 'roundTowards0', 'sign', 'isDenormal', 'exponent', 'significant'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QJSNumberCoercion::isArrayIndex(quint64 i)': takes in Python
    what 'bool QJSNumberCoercion::isArrayIndex(qint64 i)' takes.
  - Qt's 'QJSNumberCoercion::~QJSNumberCoercion()': the destructor: Python
    removes its C++ QJSNumberCoercion by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QJSNumberCoercion is created at the first use, not by
    'QJSNumberCoercion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QJSNumberCoercion back gives a copy the ritual made
    for Python, in a new cute QJSNumberCoercion.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(float)
  def isInteger(d: float) -> bool:
    """
    Calls Qt's 'bool QJSNumberCoercion::isInteger(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#isInteger

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  bool QJSNumberCoercion::isInteger(double d)
    return Rituals.call('ritual_ZN17QJSNumberCoercion9isIntegerEd', d)

  @staticmethod
  @overload(float)
  def isArrayIndex(d: float) -> bool:
    """
    Calls Qt's 'bool QJSNumberCoercion::isArrayIndex(double d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsnumbercoercion.html#isArrayIndex

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  bool QJSNumberCoercion::isArrayIndex(double d)
    return Rituals.call('ritual_ZN17QJSNumberCoercion12isArrayIndexEd', d)

  @staticmethod
  @overload(int)
  def isArrayIndex(i: int) -> bool:
    """
    Calls Qt's 'bool QJSNumberCoercion::isArrayIndex(qint64 i)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsnumbercoercion.html#isArrayIndex

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  bool QJSNumberCoercion::isArrayIndex(qint64 i)
    return Rituals.call('ritual_ZN17QJSNumberCoercion12isArrayIndexEx', i)

  @staticmethod
  @overload(float)
  def toInteger(d: float) -> int:
    """
    Calls Qt's 'int QJSNumberCoercion::toInteger(double d)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#toInteger

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  int QJSNumberCoercion::toInteger(double d)
    return Rituals.call('ritual_ZN17QJSNumberCoercion9toIntegerEd', d)

  @overload()
  def toInteger(self) -> int:
    """
    Calls Qt's 'int QJSNumberCoercion::toInteger()'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#toInteger
    """
    #  int QJSNumberCoercion::toInteger()
    return self.uglySide.call('ritual_ZN17QJSNumberCoercion9toIntegerEv')

  @staticmethod
  @overload(float, float)
  def equals(lhs: float, rhs: float) -> bool:
    """
    Calls Qt's 'bool QJSNumberCoercion::equals(double lhs, double rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#equals

    Parameters
    ----------

    lhs : float
      Passed on as it is.

    rhs : float
      Passed on as it is.
    """
    #  bool QJSNumberCoercion::equals(double lhs, double rhs)
    return Rituals.call('ritual_ZN17QJSNumberCoercion6equalsEdd', lhs, rhs)

  @staticmethod
  @overload(float)
  def roundTowards0(d: float) -> float:
    """
    Calls Qt's 'double QJSNumberCoercion::roundTowards0(double d)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsnumbercoercion.html#roundTowards0

    Parameters
    ----------

    d : float
      Passed on as it is.
    """
    #  double QJSNumberCoercion::roundTowards0(double d)
    return Rituals.call('ritual_ZN17QJSNumberCoercion13roundTowards0Ed', d)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJSNumberCoercion'

  #  Qt's '~QJSNumberCoercion()'. Naming it makes this a value class: Python
  #  owns every C++ QJSNumberCoercion behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN17QJSNumberCoercionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sign(self) -> int:
    """
    Calls Qt's 'int QJSNumberCoercion::sign() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#sign
    """
    #  int QJSNumberCoercion::sign() const
    return self.uglySide.call('ritual_ZNK17QJSNumberCoercion4signEv')

  def isDenormal(self) -> bool:
    """
    Calls Qt's 'bool QJSNumberCoercion::isDenormal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#isDenormal
    """
    #  bool QJSNumberCoercion::isDenormal() const
    return self.uglySide.call('ritual_ZNK17QJSNumberCoercion10isDenormalEv')

  def exponent(self) -> int:
    """
    Calls Qt's 'int QJSNumberCoercion::exponent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#exponent
    """
    #  int QJSNumberCoercion::exponent() const
    return self.uglySide.call('ritual_ZNK17QJSNumberCoercion8exponentEv')

  def significant(self) -> int:
    """
    Calls Qt's 'quint64 QJSNumberCoercion::significant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjsnumbercoercion.html#significant
    """
    #  quint64 QJSNumberCoercion::significant() const
    return self.uglySide.call('ritual_ZNK17QJSNumberCoercion11significantEv')

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

  @overload(float)
  def __init__(self, dbl: float) -> None:
    """
    Notes what was given, for Qt's
    'QJSNumberCoercion::QJSNumberCoercion(double dbl)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qjsnumbercoercion.html#QJSNumberCoercion

    Parameters
    ----------

    dbl : float
      Passed on as it is.
    """
    #  QJSNumberCoercion::QJSNumberCoercion(double dbl)
    self._noteCreation(QJSNumberCoercion, lambda: Rituals.call(
        'ritual_ZN17QJSNumberCoercionC1Ed', dbl,
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
