"""
QV4::OptionalReturnedValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4value_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QV4::OptionalReturnedValue to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class OptionalReturnedValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::OptionalReturnedValue: a plain Python object
  standing in front of one C++ QV4::OptionalReturnedValue.

  C++ hands a QV4::OptionalReturnedValue around as a copy, so every C++
  QV4::OptionalReturnedValue behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QV4::OptionalReturnedValue that has a ritual and
  that Python can call so far, 1 name in all: '__bool__'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ReturnedValue QV4::OptionalReturnedValue::operator->() const': an
    operator Python has no name for.
  - Qt's 'ReturnedValue QV4::OptionalReturnedValue::operator*() const': an
    operator Python has no name for.
  - Qt's 'QV4::OptionalReturnedValue::~OptionalReturnedValue()': the
    destructor: Python removes its C++ QV4::OptionalReturnedValue by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QV4::OptionalReturnedValue is created at the first use, not by
    'QV4::OptionalReturnedValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::OptionalReturnedValue back gives a copy the
    ritual made for Python, in a new cute QV4::OptionalReturnedValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::OptionalReturnedValue'

  #  Qt's '~QV4::OptionalReturnedValue()'. Naming it makes this a value
  #  class: Python owns every C++ QV4::OptionalReturnedValue behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV421OptionalReturnedValueD1Ev'

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

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QV4::OptionalReturnedValue::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-optionalreturnedvalue.html#operator bool
    """
    #  bool QV4::OptionalReturnedValue::operator bool() const
    return self.uglySide.call('ritual_ZNK3QV421OptionalReturnedValuecvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QV4::OptionalReturnedValue::OptionalReturnedValue()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-optionalreturnedvalue.html
    """
    #  QV4::OptionalReturnedValue::OptionalReturnedValue()
    self._noteCreation(OptionalReturnedValue, lambda: Rituals.call(
        'ritual_ZN3QV421OptionalReturnedValueC1Ev',
    ))

  @overload(int)
  def __init__(self, v: int) -> None:
    """
    Notes what was given, for Qt's
    'QV4::OptionalReturnedValue::OptionalReturnedValue(ReturnedValue v)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-optionalreturnedvalue.html

    Parameters
    ----------

    v : int
      Passed on as it is.
    """
    #  QV4::OptionalReturnedValue::OptionalReturnedValue(ReturnedValue v)
    self._noteCreation(OptionalReturnedValue, lambda: Rituals.call(
        'ritual_ZN3QV421OptionalReturnedValueC1Ey', v,
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
