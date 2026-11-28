"""
Qt3DAnimation::QMorphingAnimationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qmorphinganimation_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::QMorphingAnimationPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QAbstractAnimationPrivate
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QMorphingAnimationPrivate(QAbstractAnimationPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QMorphingAnimationPrivate: a plain
  Python object standing in front of one C++
  Qt3DAnimation::QMorphingAnimationPrivate.

  It is built on the cute 'QAbstractAnimationPrivate', as Qt's
  Qt3DAnimation::QMorphingAnimationPrivate is built on Qt's
  QAbstractAnimationPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QMorphingAnimationPrivate that has a
  ritual and that Python can call so far, 3 names in all: 'updateAnimation',
  'setTargetInterpolated', 'q_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DAnimation::QMorphingAnimationPrivate::~QMorphingAnimationPrivate()':
    the destructor: Python never removes a C++
    Qt3DAnimation::QMorphingAnimationPrivate.
  - Qt's 'const QMorphingAnimation
    *Qt3DAnimation::QMorphingAnimationPrivate::q_func() const': takes in
    Python what 'QMorphingAnimation
    *Qt3DAnimation::QMorphingAnimationPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QMorphingAnimationPrivate is created at the first
    use, not by 'Qt3DAnimation::QMorphingAnimationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QMorphingAnimationPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QMorphingAnimationPrivate'

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

  @overload(int)
  def setTargetInterpolated(self, morphTarget: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimationPrivate::setTargetInterpolated(int
    morphTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimationprivate.html

    Parameters
    ----------

    morphTarget : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::QMorphingAnimationPrivate::setTargetInterpolated(
    #      int morphTarget)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivate21setTargetInte'
        'rpolatedEi',
        morphTarget,
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
    'Qt3DAnimation::QMorphingAnimationPrivate::QMorphingAnimationPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimationprivate.html
    """
    #  Qt3DAnimation::QMorphingAnimationPrivate::QMorphingAnimationPrivate()
    self._noteCreation(QMorphingAnimationPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivateC1Ev',
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

  @overload(float)
  def updateAnimation(self, position: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QMorphingAnimationPrivate::updateAnimation(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimationprivate.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QMorphingAnimationPrivate::updateAnimation(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivate15updateAnimati'
        'onEf',
        position,
    )

  def q_func(self) -> Optional[Qt3DAnimation.QMorphingAnimation]:
    """
    Calls Qt's 'QMorphingAnimation
    *Qt3DAnimation::QMorphingAnimationPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qmorphinganimationprivate.html

    Returns
    -------

    Optional[Qt3DAnimation.QMorphingAnimation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMorphingAnimation *Qt3DAnimation::QMorphingAnimationPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivate6q_funcEv',
    )
    return Qt3DAnimation.QMorphingAnimation._cuteAt(address)
