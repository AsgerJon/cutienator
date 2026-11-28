"""
QSvgAnimatedPropertyFloat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimatedproperty_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSvgAnimatedPropertyFloat to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSvgAbstractAnimatedProperty

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSvgAnimatedPropertyFloat(QSvgAbstractAnimatedProperty):
  """
  The cute side of Qt's QSvgAnimatedPropertyFloat: a plain Python object
  standing in front of one C++ QSvgAnimatedPropertyFloat.

  It is built on the cute 'QSvgAbstractAnimatedProperty', as Qt's
  QSvgAnimatedPropertyFloat is built on Qt's QSvgAbstractAnimatedProperty,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgAnimatedPropertyFloat that has a ritual and that
  Python can call so far, 2 names in all: 'appendValue', 'interpolate'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimatedPropertyFloat::~QSvgAnimatedPropertyFloat()': the
    destructor: Python never removes a C++ QSvgAnimatedPropertyFloat.
  - Qt's 'void QSvgAnimatedPropertyFloat::setValues(const QList<qreal>
    &values)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<qreal> QSvgAnimatedPropertyFloat::values() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QSvgAnimatedPropertyFloat is created at the first use, not by
    'QSvgAnimatedPropertyFloat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAnimatedPropertyFloat.
  - Each name of Qt's QSvgAnimatedPropertyFloat that has no cute function
    yet, 'setValues', 'values', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimatedPropertyFloat'

  #  A C++ QSvgAnimatedPropertyFloat Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAnimatedPropertyFloat'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's
    'QSvgAnimatedPropertyFloat::QSvgAnimatedPropertyFloat(const QString
    &name)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertyfloat.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QSvgAnimatedPropertyFloat::QSvgAnimatedPropertyFloat(const QString
    #      &name)
    self._noteCreation(QSvgAnimatedPropertyFloat, lambda: Rituals.call(
        'ritual_ZN25QSvgAnimatedPropertyFloatC1ERK7QString', name,
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

  @overload(float)
  def appendValue(self, value: float) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyFloat::appendValue(const qreal
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertyfloat.html#appendValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QSvgAnimatedPropertyFloat::appendValue(const qreal value)
    self.uglySide.call(
        'ritual_ZN25QSvgAnimatedPropertyFloat11appendValueEd', value,
    )

  @overload(int, float)
  def interpolate(self, index: int, t: float) -> None:
    """
    Calls Qt's 'void QSvgAnimatedPropertyFloat::interpolate(uint index, qreal
    t) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimatedpropertyfloat.html#interpolate

    Parameters
    ----------

    index : int
      Passed on as it is.

    t : float
      Passed on as it is.
    """
    #  void QSvgAnimatedPropertyFloat::interpolate(uint index, qreal t) const
    ritual = 'ritual_ZNK25QSvgAnimatedPropertyFloat11interpolateEjd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QSvgAnimatedPropertyFloat11interpolateEjd'
    self.uglySide.call(ritual, index, t)

  @staticmethod
  def setValues(*__, **_) -> Never:
    """
    Qt's 'void QSvgAnimatedPropertyFloat::setValues(const QList<qreal>
    &values)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedPropertyFloat.setValues' has no cute function yet. "
        "Qt's 'void QSvgAnimatedPropertyFloat::setValues(const QList<qreal> "
        "&values)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def values(*__, **_) -> Never:
    """
    Qt's 'QList<qreal> QSvgAnimatedPropertyFloat::values() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSvgAnimatedPropertyFloat.values' has no cute function yet. Qt's "
        "'QList<qreal> QSvgAnimatedPropertyFloat::values() const': gives a "
        "type Python has no way to take yet.")
