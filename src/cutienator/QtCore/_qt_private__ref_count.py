"""
QtPrivate::RefCount binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qrefcount.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute


class RefCount(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::RefCount: a plain Python object standing
  in front of one C++ QtPrivate::RefCount.

  What exists
  -----------

  Every function of Qt's QtPrivate::RefCount that has a ritual and that
  Python can call so far, 6 names in all: 'ref', 'deref', 'isStatic',
  'isShared', 'initializeOwned', 'initializeUnsharable'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What to expect
  --------------

  - The C++ QtPrivate::RefCount is created at the first use, not by
    'QtPrivate::RefCount(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtPrivate::RefCount.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::RefCount'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isStatic(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::RefCount::isStatic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcount.html#isStatic
    """
    #  bool QtPrivate::RefCount::isStatic() const
    return self.uglySide.call('ritual_ZNK9QtPrivate8RefCount8isStaticEv')

  def isShared(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::RefCount::isShared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcount.html#isShared
    """
    #  bool QtPrivate::RefCount::isShared() const
    return self.uglySide.call('ritual_ZNK9QtPrivate8RefCount8isSharedEv')

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

  def ref(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::RefCount::ref()'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcount.html#ref
    """
    #  bool QtPrivate::RefCount::ref()
    return self.uglySide.call('ritual_ZN9QtPrivate8RefCount3refEv')

  def deref(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::RefCount::deref()'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-refcount.html#deref
    """
    #  bool QtPrivate::RefCount::deref()
    return self.uglySide.call('ritual_ZN9QtPrivate8RefCount5derefEv')

  def initializeOwned(self) -> None:
    """
    Calls Qt's 'void QtPrivate::RefCount::initializeOwned()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-refcount.html#initializeOwned
    """
    #  void QtPrivate::RefCount::initializeOwned()
    self.uglySide.call('ritual_ZN9QtPrivate8RefCount15initializeOwnedEv')

  def initializeUnsharable(self) -> None:
    """
    Calls Qt's 'void QtPrivate::RefCount::initializeUnsharable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-refcount.html#initializeUnsharable
    """
    #  void QtPrivate::RefCount::initializeUnsharable()
    self.uglySide.call(
        'ritual_ZN9QtPrivate8RefCount20initializeUnsharableEv',
    )
