"""
QQuickLoaderIncubator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickloader_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickLoaderIncubator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQml import QQmlIncubator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from . import QQuickLoaderPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickLoaderPrivate = WAIT['QQuickLoaderPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLoaderIncubator(QQmlIncubator):
  """
  The cute side of Qt's QQuickLoaderIncubator: a plain Python object standing
  in front of one C++ QQuickLoaderIncubator.

  It is built on the cute 'QQmlIncubator', as Qt's QQuickLoaderIncubator is
  built on Qt's QQmlIncubator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLoaderIncubator that has a ritual and that
  Python can call so far, 2 names in all: 'statusChanged', 'setInitialState'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuickLoaderIncubator is created at the first use, not by
    'QQuickLoaderIncubator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLoaderIncubator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLoaderIncubator'

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

  @overload(QObject)
  @overload(NoneType)
  def setInitialState(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickLoaderIncubator::setInitialState(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderincubator.html#setInitialState

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLoaderIncubator::setInitialState(QObject *a0)
    ritual = 'ritual_ZN21QQuickLoaderIncubator15setInitialStateEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickLoaderIncubator15setInitialStateEP7QObject')
    self.uglySide.call(ritual, self._addressOf(a0, 'QObject'))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickLoaderPrivate, QQmlIncubator.IncubationMode)
  @overload(NoneType, QQmlIncubator.IncubationMode)
  def __init__(
      self,
      l: Optional[QQuickLoaderPrivate],
      mode: QQmlIncubator.IncubationMode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickLoaderIncubator::QQuickLoaderIncubator(QQuickLoaderPrivate *l,
    IncubationMode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderincubator.html#QQuickLoaderIncubator

    Parameters
    ----------

    l : Optional[QQuickLoaderPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QQmlIncubator.IncubationMode
      Passed on as its number.
    """
    #  QQuickLoaderIncubator::QQuickLoaderIncubator(QQuickLoaderPrivate *l,
    #      IncubationMode mode)
    self._noteCreation(QQuickLoaderIncubator, lambda: Rituals.call(
        'ritual_ZN21QQuickLoaderIncubatorC1EP19QQuickLoaderPrivateN13QQmlIn'
        'cubator14IncubationModeE',
        self._addressOf(l), mode.value,
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

  @overload(QQmlIncubator.Status)
  def statusChanged(self, a0: QQmlIncubator.Status) -> None:
    """
    Calls Qt's 'void QQuickLoaderIncubator::statusChanged(Status a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickloaderincubator.html#statusChanged

    Parameters
    ----------

    a0 : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQuickLoaderIncubator::statusChanged(Status a0)
    ritual = (
        'ritual_ZN21QQuickLoaderIncubator13statusChangedEN13QQmlIncubator6S'
        'tatusE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickLoaderIncubator13statusChangedEN13QQmlIncub'
          'ator6StatusE')
    self.uglySide.call(ritual, a0.value)
