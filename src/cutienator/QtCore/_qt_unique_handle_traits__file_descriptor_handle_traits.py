"""
QtUniqueHandleTraits::FileDescriptorHandleTraits binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/quniquehandle_types_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtUniqueHandleTraits::FileDescriptorHandleTraits to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class FileDescriptorHandleTraits(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtUniqueHandleTraits::FileDescriptorHandleTraits: a
  plain Python object standing in front of one C++
  QtUniqueHandleTraits::FileDescriptorHandleTraits.

  C++ hands a QtUniqueHandleTraits::FileDescriptorHandleTraits around as a
  copy, so every C++ QtUniqueHandleTraits::FileDescriptorHandleTraits behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtUniqueHandleTraits::FileDescriptorHandleTraits
  that has a ritual and that Python can call so far, 2 names in all:
  'invalidValue', 'close'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtUniqueHandleTraits::FileDescriptorHandleTraits::
    ~FileDescriptorHandleTraits()': the destructor: Python removes its C++
    QtUniqueHandleTraits::FileDescriptorHandleTraits by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QtUniqueHandleTraits::FileDescriptorHandleTraits is created at
    the first use, not by
    'QtUniqueHandleTraits::FileDescriptorHandleTraits(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtUniqueHandleTraits::FileDescriptorHandleTraits back
    gives a copy the ritual made for Python, in a new cute
    QtUniqueHandleTraits::FileDescriptorHandleTraits.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def invalidValue() -> int:
    """
    Calls Qt's 'Type
    QtUniqueHandleTraits::FileDescriptorHandleTraits::invalidValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtuniquehandletraits-filedescriptorhandletraits.html
    """
    #  Type QtUniqueHandleTraits::FileDescriptorHandleTraits::invalidValue()
    return Rituals.call(
        'ritual_ZN20QtUniqueHandleTraits26FileDescriptorHandleTraits12inval'
        'idValueEv',
    )

  @staticmethod
  @overload(int)
  def close(handle: int) -> bool:
    """
    Calls Qt's 'bool
    QtUniqueHandleTraits::FileDescriptorHandleTraits::close(Type handle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtuniquehandletraits-filedescriptorhandletraits.html

    Parameters
    ----------

    handle : int
      Passed on as it is.
    """
    #  bool QtUniqueHandleTraits::FileDescriptorHandleTraits::close(Type
    #      handle)
    return Rituals.call(
        'ritual_ZN20QtUniqueHandleTraits26FileDescriptorHandleTraits5closeE'
        'i',
        handle,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtUniqueHandleTraits::FileDescriptorHandleTraits'

  #  Qt's '~QtUniqueHandleTraits::FileDescriptorHandleTraits()'. Naming it
  #  makes this a value class: Python owns every C++
  #  QtUniqueHandleTraits::FileDescriptorHandleTraits behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN20QtUniqueHandleTraits26FileDescriptorHandleTraitsD1Ev')

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
