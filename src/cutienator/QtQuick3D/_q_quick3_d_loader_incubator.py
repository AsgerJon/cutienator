"""
QQuick3DLoaderIncubator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dloader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DLoaderIncubator to be private: it declares the class in a
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
  from . import QQuick3DLoader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuick3DLoader = WAIT['QQuick3DLoader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DLoaderIncubator(QQmlIncubator):
  """
  The cute side of Qt's QQuick3DLoaderIncubator: a plain Python object
  standing in front of one C++ QQuick3DLoaderIncubator.

  It is built on the cute 'QQmlIncubator', as Qt's QQuick3DLoaderIncubator is
  built on Qt's QQmlIncubator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DLoaderIncubator that has a ritual and that
  Python can call so far, 2 names in all: 'statusChanged', 'setInitialState'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QQuick3DLoaderIncubator is created at the first use, not by
    'QQuick3DLoaderIncubator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DLoaderIncubator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DLoaderIncubator'

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
    Calls Qt's 'void QQuick3DLoaderIncubator::setInitialState(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloaderincubator.html#setInitialState

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DLoaderIncubator::setInitialState(QObject *a0)
    ritual = 'ritual_ZN23QQuick3DLoaderIncubator15setInitialStateEP7QObject'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DLoaderIncubator15setInitialStateEP7QObjec'
          't')
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

  @overload(QQuick3DLoader, QQmlIncubator.IncubationMode)
  @overload(NoneType, QQmlIncubator.IncubationMode)
  def __init__(
      self,
      l: Optional[QQuick3DLoader],
      mode: QQmlIncubator.IncubationMode,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DLoaderIncubator::QQuick3DLoaderIncubator(QQuick3DLoader *l,
    IncubationMode mode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloaderincubator.html

    Parameters
    ----------

    l : Optional[QQuick3DLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    mode : QQmlIncubator.IncubationMode
      Passed on as its number.
    """
    #  QQuick3DLoaderIncubator::QQuick3DLoaderIncubator(QQuick3DLoader *l,
    #      IncubationMode mode)
    self._noteCreation(QQuick3DLoaderIncubator, lambda: Rituals.call(
        'ritual_ZN23QQuick3DLoaderIncubatorC1EP14QQuick3DLoaderN13QQmlIncub'
        'ator14IncubationModeE',
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
    Calls Qt's 'void QQuick3DLoaderIncubator::statusChanged(Status a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dloaderincubator.html#statusChanged

    Parameters
    ----------

    a0 : QQmlIncubator.Status
      Passed on as its number.
    """
    #  void QQuick3DLoaderIncubator::statusChanged(Status a0)
    ritual = (
        'ritual_ZN23QQuick3DLoaderIncubator13statusChangedEN13QQmlIncubator'
        '6StatusE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQuick3DLoaderIncubator13statusChangedEN13QQmlInc'
          'ubator6StatusE')
    self.uglySide.call(ritual, a0.value)
