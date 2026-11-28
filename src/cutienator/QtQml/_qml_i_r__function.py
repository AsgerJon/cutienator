"""
QmlIR::Function binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QmlIR::Function to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute, WAIT
from . import QmlIR

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class Function(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QmlIR::Function: a plain Python object standing in
  front of one C++ QmlIR::Function.

  C++ hands a QmlIR::Function around as a copy, so every C++ QmlIR::Function
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QmlIR::Function that has a ritual and that Python
  can call so far, 2 names in all: 'formalsBegin', 'formalsEnd'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QmlIR::Function::~Function()': the destructor: Python removes its
    C++ QmlIR::Function by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QmlIR::Function is created at the first use, not by
    'QmlIR::Function(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QmlIR::Function back gives a copy the ritual made for
    Python, in a new cute QmlIR::Function.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QmlIR::Function'

  #  Qt's '~QmlIR::Function()'. Naming it makes this a value class: Python
  #  owns every C++ QmlIR::Function behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN5QmlIR8FunctionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def formalsBegin(self) -> Optional[QmlIR.Parameter]:
    """
    Calls Qt's 'const Parameter *QmlIR::Function::formalsBegin() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-function.html#formalsBegin

    Returns
    -------

    Optional[QmlIR.Parameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Parameter *QmlIR::Function::formalsBegin() const
    address = self.uglySide.call('ritual_ZNK5QmlIR8Function12formalsBeginEv')
    return QmlIR.Parameter._cuteAt(address)

  def formalsEnd(self) -> Optional[QmlIR.Parameter]:
    """
    Calls Qt's 'const Parameter *QmlIR::Function::formalsEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmlir-function.html#formalsEnd

    Returns
    -------

    Optional[QmlIR.Parameter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Parameter *QmlIR::Function::formalsEnd() const
    address = self.uglySide.call('ritual_ZNK5QmlIR8Function10formalsEndEv')
    return QmlIR.Parameter._cuteAt(address)

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
