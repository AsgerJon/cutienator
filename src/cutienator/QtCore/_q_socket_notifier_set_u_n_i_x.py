"""
QSocketNotifierSetUNIX binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QSocketNotifierSetUNIX to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QSocketNotifierSetUNIX(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSocketNotifierSetUNIX: a plain Python object
  standing in front of one C++ QSocketNotifierSetUNIX.

  C++ hands a QSocketNotifierSetUNIX around as a copy, so every C++
  QSocketNotifierSetUNIX behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSocketNotifierSetUNIX that has a ritual and that
  Python can call so far, 2 names in all: 'isEmpty', 'events'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSocketNotifierSetUNIX::~QSocketNotifierSetUNIX()': the destructor:
    Python removes its C++ QSocketNotifierSetUNIX by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QSocketNotifierSetUNIX is created at the first use, not by
    'QSocketNotifierSetUNIX(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSocketNotifierSetUNIX back gives a copy the ritual
    made for Python, in a new cute QSocketNotifierSetUNIX.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSocketNotifierSetUNIX'

  #  Qt's '~QSocketNotifierSetUNIX()'. Naming it makes this a value class:
  #  Python owns every C++ QSocketNotifierSetUNIX behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN22QSocketNotifierSetUNIXD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QSocketNotifierSetUNIX::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocketnotifiersetunix.html#isEmpty
    """
    #  bool QSocketNotifierSetUNIX::isEmpty() const
    return self.uglySide.call('ritual_ZNK22QSocketNotifierSetUNIX7isEmptyEv')

  def events(self) -> int:
    """
    Calls Qt's 'short QSocketNotifierSetUNIX::events() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsocketnotifiersetunix.html#events
    """
    #  short QSocketNotifierSetUNIX::events() const
    return self.uglySide.call('ritual_ZNK22QSocketNotifierSetUNIX6eventsEv')

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
    'QSocketNotifierSetUNIX::QSocketNotifierSetUNIX()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsocketnotifiersetunix.html#QSocketNotifierSetUNIX
    """
    #  QSocketNotifierSetUNIX::QSocketNotifierSetUNIX()
    self._noteCreation(QSocketNotifierSetUNIX, lambda: Rituals.call(
        'ritual_ZN22QSocketNotifierSetUNIXC1Ev',
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
