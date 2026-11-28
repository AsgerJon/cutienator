"""
Qt3DRender::QAbstractLightPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qabstractlight_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QAbstractLightPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QAbstractLightPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QAbstractLightPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QAbstractLightPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QAbstractLightPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QAbstractLightPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QAbstractLightPrivate::~QAbstractLightPrivate()': the
    destructor: Python never removes a C++ Qt3DRender::QAbstractLightPrivate.
  - Qt's 'const QAbstractLight *Qt3DRender::QAbstractLightPrivate::q_func()
    const': takes in Python what 'QAbstractLight
    *Qt3DRender::QAbstractLightPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QAbstractLightPrivate is created at the first use,
    not by 'Qt3DRender::QAbstractLightPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QAbstractLightPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QAbstractLightPrivate'

  #  A C++ Qt3DRender::QAbstractLightPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QAbstractLightPrivate'

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

  @overload(Qt3DRender.QAbstractLight.Type)
  def __init__(self, type: Qt3DRender.QAbstractLight.Type) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QAbstractLightPrivate::QAbstractLightPrivate(
    QAbstractLight::Type type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlightprivate.html

    Parameters
    ----------

    type : Qt3DRender.QAbstractLight.Type
      Passed on as its number.
    """
    #  Qt3DRender::QAbstractLightPrivate::QAbstractLightPrivate(
    #      QAbstractLight::Type type)
    self._noteCreation(QAbstractLightPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender21QAbstractLightPrivateC1ENS_14QAbstractLight'
        '4TypeE',
        type.value,
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

  def q_func(self) -> Optional[Qt3DRender.QAbstractLight]:
    """
    Calls Qt's 'QAbstractLight *Qt3DRender::QAbstractLightPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qabstractlightprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QAbstractLight]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractLight *Qt3DRender::QAbstractLightPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender21QAbstractLightPrivate6q_funcEv',
    )
    return Qt3DRender.QAbstractLight._cuteAt(address)
