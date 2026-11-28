"""
Qt3DAnimation::QAnimationGroupPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationgroup_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::QAnimationGroupPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
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


class QAnimationGroupPrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationGroupPrivate: a plain Python
  object standing in front of one C++ Qt3DAnimation::QAnimationGroupPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DAnimation::QAnimationGroupPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationGroupPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'updatePosition',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAnimationGroup
    *Qt3DAnimation::QAnimationGroupPrivate::q_func() const': takes in Python
    what 'QAnimationGroup *Qt3DAnimation::QAnimationGroupPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationGroupPrivate is created at the first
    use, not by 'Qt3DAnimation::QAnimationGroupPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAnimationGroupPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationGroupPrivate'

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
    'Qt3DAnimation::QAnimationGroupPrivate::QAnimationGroupPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroupprivate.html
    """
    #  Qt3DAnimation::QAnimationGroupPrivate::QAnimationGroupPrivate()
    self._noteCreation(QAnimationGroupPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation22QAnimationGroupPrivateC1Ev',
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
  def updatePosition(self, position: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationGroupPrivate::updatePosition(float position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroupprivate.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationGroupPrivate::updatePosition(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation22QAnimationGroupPrivate14updatePositionEf',
        position,
    )

  def q_func(self) -> Optional[Qt3DAnimation.QAnimationGroup]:
    """
    Calls Qt's 'QAnimationGroup
    *Qt3DAnimation::QAnimationGroupPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationgroupprivate.html#q_func

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationGroup *Qt3DAnimation::QAnimationGroupPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation22QAnimationGroupPrivate6q_funcEv',
    )
    return Qt3DAnimation.QAnimationGroup._cuteAt(address)
