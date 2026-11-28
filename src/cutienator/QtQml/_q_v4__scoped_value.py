"""
QV4::ScopedValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::ScopedValue to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class ScopedValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::ScopedValue: a plain Python object standing in
  front of one C++ QV4::ScopedValue.

  C++ hands a QV4::ScopedValue around as a copy, so every C++
  QV4::ScopedValue behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QV4::ScopedValue yet. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::ScopedValue::ScopedValue(ScopedValue &&a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QV4::ScopedValue::ScopedValue(const Scope &scope)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QV4::ScopedValue::ScopedValue(const Scope &scope, const Value &v)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ScopedValue::ScopedValue(const Scope &scope, Heap::Base *o)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ScopedValue::ScopedValue(const Scope &scope, Managed *m)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QV4::ScopedValue::ScopedValue(const Scope &scope, const
    ReturnedValue &v)': takes a type Python has no way to hand over yet.
  - Qt's 'ScopedValue &QV4::ScopedValue::operator=(const Value &v)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'ScopedValue &QV4::ScopedValue::operator=(Heap::Base *o)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'ScopedValue &QV4::ScopedValue::operator=(Managed *m)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'ScopedValue &QV4::ScopedValue::operator=(const ReturnedValue &v)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'ScopedValue &QV4::ScopedValue::operator=(const ScopedValue
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'Value *QV4::ScopedValue::operator->()': an operator Python has no
    name for.
  - Qt's 'const Value *QV4::ScopedValue::operator->() const': an operator
    Python has no name for.
  - Qt's 'Value *QV4::ScopedValue::operator QV4::Value *()': an operator
    Python has no name for.
  - Qt's 'const Value &QV4::ScopedValue::operator const QV4::Value &()
    const': an operator Python has no name for.
  - Qt's 'QV4::ScopedValue::~ScopedValue()': the destructor: Python removes
    its C++ QV4::ScopedValue by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::ScopedValue is created at the first use, not by
    'QV4::ScopedValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::ScopedValue back gives a copy the ritual made
    for Python, in a new cute QV4::ScopedValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ScopedValue'

  #  Qt's '~QV4::ScopedValue()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::ScopedValue behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV411ScopedValueD1Ev'

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

  @overload(THIS)
  def __init__(self, a0: ScopedValue) -> None:
    """
    Notes what was given, for Qt's 'QV4::ScopedValue::ScopedValue(const
    ScopedValue &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-scopedvalue.html#ScopedValue

    Parameters
    ----------

    a0 : ScopedValue
      Passed on as a value: Qt reads the C++ QV4::ScopedValue, which stays
      Python's own.
    """
    #  QV4::ScopedValue::ScopedValue(const ScopedValue &a0)
    self._noteCreation(ScopedValue, lambda: Rituals.call(
        'ritual_ZN3QV411ScopedValueC1ERKS0_', self._valueOf(a0),
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
