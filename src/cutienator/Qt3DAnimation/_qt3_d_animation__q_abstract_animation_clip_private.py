"""
Qt3DAnimation::QAbstractAnimationClipPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractanimationclip_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::QAbstractAnimationClipPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QAbstractAnimationClipPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractAnimationClipPrivate: a plain
  Python object standing in front of one C++
  Qt3DAnimation::QAbstractAnimationClipPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DAnimation::QAbstractAnimationClipPrivate is built on Qt's
  Qt3DCore::QNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractAnimationClipPrivate that
  has a ritual and that Python can call so far, 2 names in all: 'q_func',
  'setDuration'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractAnimationClip
    *Qt3DAnimation::QAbstractAnimationClipPrivate::q_func() const': takes in
    Python what 'QAbstractAnimationClip
    *Qt3DAnimation::QAbstractAnimationClipPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractAnimationClipPrivate is created at the
    first use, not by 'Qt3DAnimation::QAbstractAnimationClipPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::QAbstractAnimationClipPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractAnimationClipPrivate'

  #  A C++ Qt3DAnimation::QAbstractAnimationClipPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAbstractAnimationClipPrivate'

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

  @overload(float)
  def setDuration(self, duration: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QAbstractAnimationClipPrivate::setDuration(float
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclipprivate.html

    Parameters
    ----------

    duration : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::QAbstractAnimationClipPrivate::setDuration(float
    #      duration)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation29QAbstractAnimationClipPrivate11setDurati'
        'onEf',
        duration,
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
    'Qt3DAnimation::QAbstractAnimationClipPrivate::
    QAbstractAnimationClipPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclipprivate.html
    """
    #  Qt3DAnimation::QAbstractAnimationClipPrivate::
    #      QAbstractAnimationClipPrivate()
    self._noteCreation(QAbstractAnimationClipPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation29QAbstractAnimationClipPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DAnimation.QAbstractAnimationClip]:
    """
    Calls Qt's 'QAbstractAnimationClip
    *Qt3DAnimation::QAbstractAnimationClipPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractanimationclipprivate.html

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractAnimationClip]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationClip
    #      *Qt3DAnimation::QAbstractAnimationClipPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation29QAbstractAnimationClipPrivate6q_funcEv',
    )
    return Qt3DAnimation.QAbstractAnimationClip._cuteAt(address)
