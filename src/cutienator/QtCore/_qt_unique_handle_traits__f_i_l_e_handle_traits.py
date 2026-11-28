"""
QtUniqueHandleTraits::FILEHandleTraits binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/quniquehandle_types_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtUniqueHandleTraits::FILEHandleTraits to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class FILEHandleTraits(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtUniqueHandleTraits::FILEHandleTraits: a plain
  Python object standing in front of one C++
  QtUniqueHandleTraits::FILEHandleTraits.

  C++ hands a QtUniqueHandleTraits::FILEHandleTraits around as a copy, so
  every C++ QtUniqueHandleTraits::FILEHandleTraits behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  No function of Qt's QtUniqueHandleTraits::FILEHandleTraits yet. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Type QtUniqueHandleTraits::FILEHandleTraits::invalidValue()': gives
    'FILE', which has no cute class yet.
  - Qt's 'bool QtUniqueHandleTraits::FILEHandleTraits::close(Type handle)':
    names 'FILE', which has no cute class yet.
  - Qt's 'QtUniqueHandleTraits::FILEHandleTraits::~FILEHandleTraits()': the
    destructor: Python removes its C++ QtUniqueHandleTraits::FILEHandleTraits
    by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtUniqueHandleTraits::FILEHandleTraits is created at the first
    use, not by 'QtUniqueHandleTraits::FILEHandleTraits(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtUniqueHandleTraits::FILEHandleTraits back gives a
    copy the ritual made for Python, in a new cute
    QtUniqueHandleTraits::FILEHandleTraits.
  - Each name of Qt's QtUniqueHandleTraits::FILEHandleTraits that has no cute
    function yet, 'close', 'invalidValue', holds a function that raises
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
  __qt_class__ = 'QtUniqueHandleTraits::FILEHandleTraits'

  #  Qt's '~QtUniqueHandleTraits::FILEHandleTraits()'. Naming it makes this a
  #  value class: Python owns every C++
  #  QtUniqueHandleTraits::FILEHandleTraits behind a cute one, and removes it
  #  by this ritual.
  __delete_ritual__ = 'ritual_ZN20QtUniqueHandleTraits16FILEHandleTraitsD1Ev'

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

  @staticmethod
  def close(*__, **_) -> Never:
    """
    Qt's 'bool QtUniqueHandleTraits::FILEHandleTraits::close(Type handle)':
    names 'FILE', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtUniqueHandleTraits.FILEHandleTraits.close' has no cute function "
        "yet. Qt's 'bool QtUniqueHandleTraits::FILEHandleTraits::close(Type "
        "handle)': names 'FILE', which has no cute class yet.")

  @staticmethod
  def invalidValue(*__, **_) -> Never:
    """
    Qt's 'Type QtUniqueHandleTraits::FILEHandleTraits::invalidValue()': gives
    'FILE', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QtUniqueHandleTraits.FILEHandleTraits.invalidValue' has no cute "
        "function yet. Qt's 'Type "
        "QtUniqueHandleTraits::FILEHandleTraits::invalidValue()': gives "
        "'FILE', which has no cute class yet.")
