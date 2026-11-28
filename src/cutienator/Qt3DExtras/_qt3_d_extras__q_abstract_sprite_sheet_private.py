"""
Qt3DExtras::QAbstractSpriteSheetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qabstractspritesheet_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QAbstractSpriteSheetPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSpriteSheetPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DExtras::QAbstractSpriteSheetPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::QAbstractSpriteSheetPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DExtras::QAbstractSpriteSheetPrivate is built on Qt's
  Qt3DCore::QNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QAbstractSpriteSheetPrivate that has a
  ritual and that Python can call so far, 7 names in all: 'init',
  'updateTexture', 'updateIndex', 'maxIndex', 'updateSizes',
  'updateTransform', 'q_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractSpriteSheet
    *Qt3DExtras::QAbstractSpriteSheetPrivate::q_func() const': takes in
    Python what 'QAbstractSpriteSheet
    *Qt3DExtras::QAbstractSpriteSheetPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QAbstractSpriteSheetPrivate is created at the first
    use, not by 'Qt3DExtras::QAbstractSpriteSheetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QAbstractSpriteSheetPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QAbstractSpriteSheetPrivate'

  #  A C++ Qt3DExtras::QAbstractSpriteSheetPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QAbstractSpriteSheetPrivate'

  #  The functions Qt calls itself that
  #  Qt3DExtras::QAbstractSpriteSheetPrivate is the first to declare. A class
  #  of a program built on it can write one anew, and Qt then calls that. For
  #  each name: the key C++ knows the function by, what it gives, and what it
  #  takes.
  __virtual_functions__ = {
      'init': (
          ('_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate4initEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'maxIndex': (
          ('_ZNK10Qt3DExtras27QAbstractSpriteSheetPrivate8maxIndexEv',
           ('int', 'number', ''),
           ()),
      ),
      'updateSizes': (
          ('_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate11updateSizesEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'updateTransform': (
          ('_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate15updateTransformEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def maxIndex(self) -> int:
    """
    Calls Qt's 'int Qt3DExtras::QAbstractSpriteSheetPrivate::maxIndex()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html
    """
    #  int Qt3DExtras::QAbstractSpriteSheetPrivate::maxIndex() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DExtras27QAbstractSpriteSheetPrivate8maxIndexEv',
    )

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
    'Qt3DExtras::QAbstractSpriteSheetPrivate::QAbstractSpriteSheetPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html
    """
    #  Qt3DExtras::QAbstractSpriteSheetPrivate::QAbstractSpriteSheetPrivate()
    self._noteCreation(QAbstractSpriteSheetPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QAbstractSpriteSheetPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html#init
    """
    #  void Qt3DExtras::QAbstractSpriteSheetPrivate::init()
    ritual = 'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate4initEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate4initEv')
    self.uglySide.call(ritual)

  @overload(WAIT['Qt3DRender.QAbstractTexture'])
  @overload(NoneType)
  def updateTexture(
      self,
      texture: Optional[Qt3DRender.QAbstractTexture],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractSpriteSheetPrivate::updateTexture(Qt3DRender::
    QAbstractTexture *texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html

    Parameters
    ----------

    texture : Optional[Qt3DRender.QAbstractTexture]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateTexture(
    #      Qt3DRender::QAbstractTexture *texture)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate13updateTextureE'
        'PN10Qt3DRender16QAbstractTextureE',
        self._addressOf(texture),
    )

  @overload(int)
  def updateIndex(self, newIndex: int) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QAbstractSpriteSheetPrivate::updateIndex(int
    newIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html

    Parameters
    ----------

    newIndex : int
      Passed on as it is.
    """
    #  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateIndex(int
    #      newIndex)
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate11updateIndexEi',
        newIndex,
    )

  def updateSizes(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QAbstractSpriteSheetPrivate::updateSizes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html
    """
    #  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateSizes()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate11updateSizesEv',
    )

  def updateTransform(self) -> None:
    """
    Calls Qt's 'void
    Qt3DExtras::QAbstractSpriteSheetPrivate::updateTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html
    """
    #  void Qt3DExtras::QAbstractSpriteSheetPrivate::updateTransform()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate15updateTransfor'
        'mEv',
    )

  def q_func(self) -> Optional[Qt3DExtras.QAbstractSpriteSheet]:
    """
    Calls Qt's 'QAbstractSpriteSheet
    *Qt3DExtras::QAbstractSpriteSheetPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qabstractspritesheetprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QAbstractSpriteSheet]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSpriteSheet
    #      *Qt3DExtras::QAbstractSpriteSheetPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras27QAbstractSpriteSheetPrivate6q_funcEv',
    )
    return Qt3DExtras.QAbstractSpriteSheet._cuteAt(address)
