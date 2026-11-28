"""
Qt3DRender::QSceneLoaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qsceneloader_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QSceneLoaderPrivate to be private: it declares the
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSceneLoaderPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DRender::QSceneLoaderPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QSceneLoaderPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DRender::QSceneLoaderPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSceneLoaderPrivate that has a ritual
  and that Python can call so far, 4 names in all: 'setStatus',
  'setSceneRoot', 'q_func', 'populateEntityMap'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSceneLoader *Qt3DRender::QSceneLoaderPrivate::q_func()
    const': takes in Python what 'QSceneLoader
    *Qt3DRender::QSceneLoaderPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QSceneLoaderPrivate is created at the first use, not
    by 'Qt3DRender::QSceneLoaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSceneLoaderPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSceneLoaderPrivate'

  #  A C++ Qt3DRender::QSceneLoaderPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSceneLoaderPrivate'

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

  @overload(Qt3DRender.QSceneLoader.Status)
  def setStatus(self, status: Qt3DRender.QSceneLoader.Status) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QSceneLoaderPrivate::setStatus(QSceneLoader::Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloaderprivate.html#setStatus

    Parameters
    ----------

    status : Qt3DRender.QSceneLoader.Status
      Passed on as its number.
    """
    #  void Qt3DRender::QSceneLoaderPrivate::setStatus(QSceneLoader::Status
    #      status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QSceneLoaderPrivate9setStatusENS_12QSceneLo'
        'ader6StatusE',
        status.value,
    )

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def setSceneRoot(self, root: Optional[Qt3DCore.QEntity]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QSceneLoaderPrivate::setSceneRoot(Qt3DCore::QEntity *root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloaderprivate.html#setSceneRoot

    Parameters
    ----------

    root : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QSceneLoaderPrivate::setSceneRoot(Qt3DCore::QEntity
    #      *root)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QSceneLoaderPrivate12setSceneRootEPN8Qt3DCo'
        're7QEntityE',
        self._addressOf(root),
    )

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
    'Qt3DRender::QSceneLoaderPrivate::QSceneLoaderPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloaderprivate.html
    """
    #  Qt3DRender::QSceneLoaderPrivate::QSceneLoaderPrivate()
    self._noteCreation(QSceneLoaderPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19QSceneLoaderPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QSceneLoader]:
    """
    Calls Qt's 'QSceneLoader *Qt3DRender::QSceneLoaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloaderprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QSceneLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSceneLoader *Qt3DRender::QSceneLoaderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender19QSceneLoaderPrivate6q_funcEv',
    )
    return Qt3DRender.QSceneLoader._cuteAt(address)

  @overload(WAIT['Qt3DCore.QEntity'])
  @overload(NoneType)
  def populateEntityMap(
      self,
      parentEntity: Optional[Qt3DCore.QEntity],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QSceneLoaderPrivate::populateEntityMap(Qt3DCore::QEntity
    *parentEntity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloaderprivate.html

    Parameters
    ----------

    parentEntity : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QSceneLoaderPrivate::populateEntityMap(Qt3DCore::
    #      QEntity *parentEntity)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender19QSceneLoaderPrivate17populateEntityMapEPN8Q'
        't3DCore7QEntityE',
        self._addressOf(parentEntity),
    )
