"""
Qt3DExtras::QSkyboxEntityPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qskyboxentity_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DExtras::QSkyboxEntityPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QSkyboxEntityPrivate(Qt3DCore.QEntityPrivate):
  """
  The cute side of Qt's Qt3DExtras::QSkyboxEntityPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QSkyboxEntityPrivate.

  It is built on the cute 'Qt3DCore::QEntityPrivate', as Qt's
  Qt3DExtras::QSkyboxEntityPrivate is built on Qt's Qt3DCore::QEntityPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSkyboxEntityPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'init', 'reloadTexture',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSkyboxEntity *Qt3DExtras::QSkyboxEntityPrivate::q_func()
    const': takes in Python what 'QSkyboxEntity
    *Qt3DExtras::QSkyboxEntityPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSkyboxEntityPrivate is created at the first use, not
    by 'Qt3DExtras::QSkyboxEntityPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSkyboxEntityPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSkyboxEntityPrivate'

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
    'Qt3DExtras::QSkyboxEntityPrivate::QSkyboxEntityPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentityprivate.html
    """
    #  Qt3DExtras::QSkyboxEntityPrivate::QSkyboxEntityPrivate()
    self._noteCreation(QSkyboxEntityPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras20QSkyboxEntityPrivateC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntityPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentityprivate.html#init
    """
    #  void Qt3DExtras::QSkyboxEntityPrivate::init()
    self.uglySide.call('ritual_ZN10Qt3DExtras20QSkyboxEntityPrivate4initEv')

  def reloadTexture(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSkyboxEntityPrivate::reloadTexture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentityprivate.html#reloadTexture
    """
    #  void Qt3DExtras::QSkyboxEntityPrivate::reloadTexture()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras20QSkyboxEntityPrivate13reloadTextureEv',
    )

  def q_func(self) -> Optional[Qt3DExtras.QSkyboxEntity]:
    """
    Calls Qt's 'QSkyboxEntity *Qt3DExtras::QSkyboxEntityPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qskyboxentityprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QSkyboxEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSkyboxEntity *Qt3DExtras::QSkyboxEntityPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras20QSkyboxEntityPrivate6q_funcEv',
    )
    return Qt3DExtras.QSkyboxEntity._cuteAt(address)
