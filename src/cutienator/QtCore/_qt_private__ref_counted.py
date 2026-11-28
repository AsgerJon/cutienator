"""
QtPrivate::RefCounted binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute


class RefCounted(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::RefCounted: a plain Python object standing
  in front of one C++ QtPrivate::RefCounted.

  C++ hands a QtPrivate::RefCounted around as a copy, so every C++
  QtPrivate::RefCounted behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::RefCounted that has a ritual and that
  Python can call so far, 3 names in all: 'refCount', 'addRef', 'deref'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::RefCounted::~RefCounted()': the destructor: Python
    removes its C++ QtPrivate::RefCounted by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::RefCounted is created at the first use, not by
    'QtPrivate::RefCounted(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::RefCounted back gives a copy the ritual
    made for Python, in a new cute QtPrivate::RefCounted.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::RefCounted'

  #  Qt's '~QtPrivate::RefCounted()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::RefCounted behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate10RefCountedD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def refCount(self) -> int:
    """
    Calls Qt's 'int QtPrivate::RefCounted::refCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcounted.html#refCount
    """
    #  int QtPrivate::RefCounted::refCount() const
    return self.uglySide.call('ritual_ZNK9QtPrivate10RefCounted8refCountEv')

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

  def addRef(self) -> None:
    """
    Calls Qt's 'void QtPrivate::RefCounted::addRef()'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcounted.html#addRef
    """
    #  void QtPrivate::RefCounted::addRef()
    self.uglySide.call('ritual_ZN9QtPrivate10RefCounted6addRefEv')

  def deref(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::RefCounted::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcounted.html#deref
    """
    #  bool QtPrivate::RefCounted::deref()
    return self.uglySide.call('ritual_ZN9QtPrivate10RefCounted5derefEv')
