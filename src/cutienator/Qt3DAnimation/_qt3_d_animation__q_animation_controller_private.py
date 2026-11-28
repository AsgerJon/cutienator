"""
Qt3DAnimation::QAnimationControllerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationcontroller_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::QAnimationControllerPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QAnimationControllerPrivate(QObjectPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QAnimationControllerPrivate: a plain
  Python object standing in front of one C++
  Qt3DAnimation::QAnimationControllerPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  Qt3DAnimation::QAnimationControllerPrivate is built on Qt's QObjectPrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAnimationControllerPrivate that has
  a ritual and that Python can call so far, 6 names in all: 'updatePosition',
  'extractAnimations', 'clearAnimations', 'findGroup', 'scaledPosition',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAnimationController
    *Qt3DAnimation::QAnimationControllerPrivate::q_func() const': takes in
    Python what 'QAnimationController
    *Qt3DAnimation::QAnimationControllerPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAnimationControllerPrivate is created at the
    first use, not by 'Qt3DAnimation::QAnimationControllerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAnimationControllerPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAnimationControllerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def scaledPosition(self, position: float) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::QAnimationControllerPrivate::scaledPosition(float
    position) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  float Qt3DAnimation::QAnimationControllerPrivate::scaledPosition(float
    #      position) const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation27QAnimationControllerPrivate14scaledPosi'
        'tionEf',
        position,
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
    'Qt3DAnimation::QAnimationControllerPrivate::QAnimationControllerPrivate(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html
    """
    #  Qt3DAnimation::QAnimationControllerPrivate::
    #      QAnimationControllerPrivate()
    self._noteCreation(QAnimationControllerPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation27QAnimationControllerPrivateC1Ev',
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
    Qt3DAnimation::QAnimationControllerPrivate::updatePosition(float
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAnimationControllerPrivate::updatePosition(float
    #      position)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate14updatePosit'
        'ionEf',
        position,
    )

  def extractAnimations(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationControllerPrivate::extractAnimations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html
    """
    #  void Qt3DAnimation::QAnimationControllerPrivate::extractAnimations()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate17extractAnim'
        'ationsEv',
    )

  def clearAnimations(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAnimationControllerPrivate::clearAnimations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html
    """
    #  void Qt3DAnimation::QAnimationControllerPrivate::clearAnimations()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate15clearAnimat'
        'ionsEv',
    )

  @overload(str)
  def findGroup(self, name: str) -> Optional[Qt3DAnimation.QAnimationGroup]:
    """
    Calls Qt's 'QAnimationGroup
    *Qt3DAnimation::QAnimationControllerPrivate::findGroup(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationGroup
    #      *Qt3DAnimation::QAnimationControllerPrivate::findGroup(const
    #      QString &name)
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate9findGroupERK'
        '7QString',
        name,
    )
    return Qt3DAnimation.QAnimationGroup._cuteAt(address)

  def q_func(self) -> Optional[Qt3DAnimation.QAnimationController]:
    """
    Calls Qt's 'QAnimationController
    *Qt3DAnimation::QAnimationControllerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qanimationcontrollerprivate.html

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationController]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationController
    #      *Qt3DAnimation::QAnimationControllerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate6q_funcEv',
    )
    return Qt3DAnimation.QAnimationController._cuteAt(address)
