"""
QtPrivate::ModelIndex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectabstractitemmodeltypes_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QtPrivate::ModelIndex to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class ModelIndex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtPrivate::ModelIndex: a plain Python object standing
  in front of one C++ QtPrivate::ModelIndex.

  C++ hands a QtPrivate::ModelIndex around as a copy, so every C++
  QtPrivate::ModelIndex behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtPrivate::ModelIndex that has a ritual and that
  Python can call so far, 2 names in all: '__eq__', '__ne__'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtPrivate::ModelIndex::~ModelIndex()': the destructor: Python
    removes its C++ QtPrivate::ModelIndex by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtPrivate::ModelIndex is created at the first use, not by
    'QtPrivate::ModelIndex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtPrivate::ModelIndex back gives a copy the ritual
    made for Python, in a new cute QtPrivate::ModelIndex.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtPrivate::ModelIndex'

  #  Qt's '~QtPrivate::ModelIndex()'. Naming it makes this a value class:
  #  Python owns every C++ QtPrivate::ModelIndex behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QtPrivate10ModelIndexD1Ev'

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

  @overload(THIS)
  def __eq__(self, other: ModelIndex) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ModelIndex::operator==(const ModelIndex
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-modelindex.html#operator==

    Parameters
    ----------

    other : ModelIndex
      Passed on as a value: Qt reads the C++ QtPrivate::ModelIndex, which
      stays Python's own.
    """
    #  bool QtPrivate::ModelIndex::operator==(const ModelIndex &other) const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate10ModelIndexeqERKS0_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: ModelIndex) -> bool:
    """
    Calls Qt's 'bool QtPrivate::ModelIndex::operator!=(const ModelIndex
    &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-modelindex.html#operator!=

    Parameters
    ----------

    other : ModelIndex
      Passed on as a value: Qt reads the C++ QtPrivate::ModelIndex, which
      stays Python's own.
    """
    #  bool QtPrivate::ModelIndex::operator!=(const ModelIndex &other) const
    return self.uglySide.call(
        'ritual_ZNK9QtPrivate10ModelIndexneERKS0_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtPrivate::ModelIndex::ModelIndex()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-modelindex.html#ModelIndex
    """
    #  QtPrivate::ModelIndex::ModelIndex()
    self._noteCreation(ModelIndex, lambda: Rituals.call(
        'ritual_ZN9QtPrivate10ModelIndexC1Ev',
    ))

  @overload(int, int)
  def __init__(self, row_: int, column_: int) -> None:
    """
    Notes what was given, for Qt's 'QtPrivate::ModelIndex::ModelIndex(int
    row_, int column_)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprivate-modelindex.html#ModelIndex

    Parameters
    ----------

    row_ : int
      Passed on as it is.

    column_ : int
      Passed on as it is.
    """
    #  QtPrivate::ModelIndex::ModelIndex(int row_, int column_)
    self._noteCreation(ModelIndex, lambda: Rituals.call(
        'ritual_ZN9QtPrivate10ModelIndexC1Eii', row_, column_,
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
