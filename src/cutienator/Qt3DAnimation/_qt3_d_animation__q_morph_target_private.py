"""
Qt3DAnimation::QMorphTargetPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qmorphtarget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::QMorphTargetPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QMorphTargetPrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QMorphTargetPrivate: a plain Python
  object standing in front of one C++ Qt3DAnimation::QMorphTargetPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DAnimation::QMorphTargetPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QMorphTargetPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'updateAttributeNames',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMorphTarget *Qt3DAnimation::QMorphTargetPrivate::q_func()
    const': takes in Python what 'QMorphTarget
    *Qt3DAnimation::QMorphTargetPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QMorphTargetPrivate is created at the first use,
    not by 'Qt3DAnimation::QMorphTargetPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QMorphTargetPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QMorphTargetPrivate'

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
    'Qt3DAnimation::QMorphTargetPrivate::QMorphTargetPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtargetprivate.html
    """
    #  Qt3DAnimation::QMorphTargetPrivate::QMorphTargetPrivate()
    self._noteCreation(QMorphTargetPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation19QMorphTargetPrivateC1Ev',
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

  def updateAttributeNames(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphTargetPrivate::updateAttributeNames()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtargetprivate.html
    """
    #  void Qt3DAnimation::QMorphTargetPrivate::updateAttributeNames()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation19QMorphTargetPrivate20updateAttributeName'
        'sEv',
    )

  def q_func(self) -> Optional[Qt3DAnimation.QMorphTarget]:
    """
    Calls Qt's 'QMorphTarget *Qt3DAnimation::QMorphTargetPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphtargetprivate.html#q_func

    Returns
    -------

    Optional[Qt3DAnimation.QMorphTarget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphTarget *Qt3DAnimation::QMorphTargetPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation19QMorphTargetPrivate6q_funcEv',
    )
    return Qt3DAnimation.QMorphTarget._cuteAt(address)
