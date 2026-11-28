"""
Qt3DExtras::QSpriteGridPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qspritegrid_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DExtras::QSpriteGridPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QSpriteGridPrivate(Qt3DExtras.QAbstractSpriteSheetPrivate):
  """
  The cute side of Qt's Qt3DExtras::QSpriteGridPrivate: a plain Python object
  standing in front of one C++ Qt3DExtras::QSpriteGridPrivate.

  It is built on the cute 'Qt3DExtras::QAbstractSpriteSheetPrivate', as Qt's
  Qt3DExtras::QSpriteGridPrivate is built on Qt's
  Qt3DExtras::QAbstractSpriteSheetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSpriteGridPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'maxIndex', 'updateSizes',
  'updateTransform', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSpriteGrid *Qt3DExtras::QSpriteGridPrivate::q_func() const':
    takes in Python what 'QSpriteGrid
    *Qt3DExtras::QSpriteGridPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSpriteGridPrivate is created at the first use, not
    by 'Qt3DExtras::QSpriteGridPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSpriteGridPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSpriteGridPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def maxIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QSpriteGridPrivate::maxIndex() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegridprivate.html#maxIndex
    """
    #  int Qt3DExtras::QSpriteGridPrivate::maxIndex() const
    ritual = 'ritual_ZNK10Qt3DExtras18QSpriteGridPrivate8maxIndexEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DExtras18QSpriteGridPrivate8maxIndexEv'
    return self.uglySide.call(ritual)

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
    'Qt3DExtras::QSpriteGridPrivate::QSpriteGridPrivate()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegridprivate.html
    """
    #  Qt3DExtras::QSpriteGridPrivate::QSpriteGridPrivate()
    self._noteCreation(QSpriteGridPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras18QSpriteGridPrivateC1Ev',
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

  def updateSizes(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteGridPrivate::updateSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegridprivate.html#updateSizes
    """
    #  void Qt3DExtras::QSpriteGridPrivate::updateSizes()
    ritual = 'ritual_ZN10Qt3DExtras18QSpriteGridPrivate11updateSizesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DExtras18QSpriteGridPrivate11updateSizesEv'
    self.uglySide.call(ritual)

  def updateTransform(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSpriteGridPrivate::updateTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegridprivate.html#updateTransform
    """
    #  void Qt3DExtras::QSpriteGridPrivate::updateTransform()
    ritual = 'ritual_ZN10Qt3DExtras18QSpriteGridPrivate15updateTransformEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras18QSpriteGridPrivate15updateTransformEv')
    self.uglySide.call(ritual)

  def q_func(self) -> Optional[Qt3DExtras.QSpriteGrid]:
    """
    Calls Qt's 'QSpriteGrid *Qt3DExtras::QSpriteGridPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspritegridprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QSpriteGrid]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSpriteGrid *Qt3DExtras::QSpriteGridPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras18QSpriteGridPrivate6q_funcEv',
    )
    return Qt3DExtras.QSpriteGrid._cuteAt(address)
