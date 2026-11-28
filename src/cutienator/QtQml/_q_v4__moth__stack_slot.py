"""
QV4::Moth::StackSlot binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Moth::StackSlot to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class StackSlot(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Moth::StackSlot: a plain Python object standing
  in front of one C++ QV4::Moth::StackSlot.

  C++ hands a QV4::Moth::StackSlot around as a copy, so every C++
  QV4::Moth::StackSlot behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::Moth::StackSlot that has a ritual and that
  Python can call so far, 2 names in all: 'createRegister', 'stackSlot'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QV4::Moth::StackSlot::operator int() const': an operator Python
    has no name for.
  - Qt's 'QV4::Moth::StackSlot::~StackSlot()': the destructor: Python removes
    its C++ QV4::Moth::StackSlot by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::Moth::StackSlot is created at the first use, not by
    'QV4::Moth::StackSlot(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::Moth::StackSlot back gives a copy the ritual
    made for Python, in a new cute QV4::Moth::StackSlot.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def createRegister(index: int) -> StackSlot:
    """
    Calls Qt's 'StackSlot QV4::Moth::StackSlot::createRegister(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-stackslot.html#createRegister

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    StackSlot
      A new cute QV4::Moth::StackSlot around the copy Qt gave back. Python
      owns it.
    """
    #  StackSlot QV4::Moth::StackSlot::createRegister(int index)
    address = Rituals.call(
        'ritual_ZN3QV44Moth9StackSlot14createRegisterEi', index,
    )
    return StackSlot._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Moth::StackSlot'

  #  Qt's '~QV4::Moth::StackSlot()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::Moth::StackSlot behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV44Moth9StackSlotD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def stackSlot(self) -> int:
    """
    Calls Qt's 'int QV4::Moth::StackSlot::stackSlot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-moth-stackslot.html#stackSlot
    """
    #  int QV4::Moth::StackSlot::stackSlot() const
    return self.uglySide.call('ritual_ZNK3QV44Moth9StackSlot9stackSlotEv')

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
