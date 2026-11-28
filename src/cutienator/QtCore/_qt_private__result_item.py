"""
QtPrivate::ResultItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qresultstore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class ResultItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::ResultItem: a plain Python object standing
  in front of one C++ QtPrivate::ResultItem.

  C++ hands a QtPrivate::ResultItem around as a copy, so every C++
  QtPrivate::ResultItem behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::ResultItem that has a ritual and that
  Python can call so far, 3 names in all: 'isValid', 'isVector', 'count'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::ResultItem::ResultItem(const void *_result, int
    _count)': names 'void', which has no cute class yet.
  - Qt's 'QtPrivate::ResultItem::ResultItem(const void *_result)': names
    'void', which has no cute class yet.
  - Qt's 'QtPrivate::ResultItem::~ResultItem()': the destructor: Python
    removes its C++ QtPrivate::ResultItem by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::ResultItem is created at the first use, not by
    'QtPrivate::ResultItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::ResultItem back gives a copy the ritual
    made for Python, in a new cute QtPrivate::ResultItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::ResultItem'

  #  Qt's '~QtPrivate::ResultItem()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::ResultItem behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate10ResultItemD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultItem::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-resultitem.html#isValid
    """
    #  bool QtPrivate::ResultItem::isValid() const
    return self.uglySide.call('ritual_ZNK9QtPrivate10ResultItem7isValidEv')

  def isVector(self) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ResultItem::isVector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-resultitem.html#isVector
    """
    #  bool QtPrivate::ResultItem::isVector() const
    return self.uglySide.call('ritual_ZNK9QtPrivate10ResultItem8isVectorEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QtPrivate::ResultItem::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtprivate-resultitem.html#count
    """
    #  int QtPrivate::ResultItem::count() const
    return self.uglySide.call('ritual_ZNK9QtPrivate10ResultItem5countEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtPrivate::ResultItem::ResultItem()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-resultitem.html#ResultItem
    """
    #  QtPrivate::ResultItem::ResultItem()
    self._noteCreation(ResultItem, lambda: Rituals.call(
        'ritual_ZN9QtPrivate10ResultItemC1Ev',
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
