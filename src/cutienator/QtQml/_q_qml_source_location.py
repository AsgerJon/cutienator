"""
QQmlSourceLocation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlglobal_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlSourceLocation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QQmlSourceLocation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlSourceLocation: a plain Python object standing in
  front of one C++ QQmlSourceLocation.

  C++ hands a QQmlSourceLocation around as a copy, so every C++
  QQmlSourceLocation behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QQmlSourceLocation yet. It can be made from Python, in
  2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlSourceLocation::~QQmlSourceLocation()': the destructor: Python
    removes its C++ QQmlSourceLocation by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlSourceLocation is created at the first use, not by
    'QQmlSourceLocation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlSourceLocation back gives a copy the ritual made
    for Python, in a new cute QQmlSourceLocation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlSourceLocation'

  #  Qt's '~QQmlSourceLocation()'. Naming it makes this a value class: Python
  #  owns every C++ QQmlSourceLocation behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QQmlSourceLocationD1Ev'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSourceLocation::QQmlSourceLocation()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsourcelocation.html#QQmlSourceLocation
    """
    #  QQmlSourceLocation::QQmlSourceLocation()
    self._noteCreation(QQmlSourceLocation, lambda: Rituals.call(
        'ritual_ZN18QQmlSourceLocationC1Ev',
    ))

  @overload(str, int, int)
  def __init__(self, sourceFile: str, line: int, column: int) -> None:
    """
    Notes what was given, for Qt's
    'QQmlSourceLocation::QQmlSourceLocation(const QString &sourceFile,
    quint16 line, quint16 column)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlsourcelocation.html#QQmlSourceLocation

    Parameters
    ----------

    sourceFile : str
      Passed on as it is: a QString is made of it for the call.

    line : int
      Passed on as it is.

    column : int
      Passed on as it is.
    """
    #  QQmlSourceLocation::QQmlSourceLocation(const QString &sourceFile,
    #      quint16 line, quint16 column)
    self._noteCreation(QQmlSourceLocation, lambda: Rituals.call(
        'ritual_ZN18QQmlSourceLocationC1ERK7QStringtt',
        sourceFile, line, column,
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
