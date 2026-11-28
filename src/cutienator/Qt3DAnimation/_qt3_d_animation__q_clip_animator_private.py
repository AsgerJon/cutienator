"""
Qt3DAnimation::QClipAnimatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qclipanimator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::QClipAnimatorPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QClipAnimatorPrivate(Qt3DAnimation.QAbstractClipAnimatorPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QClipAnimatorPrivate: a plain Python
  object standing in front of one C++ Qt3DAnimation::QClipAnimatorPrivate.

  It is built on the cute 'Qt3DAnimation::QAbstractClipAnimatorPrivate', as
  Qt's Qt3DAnimation::QClipAnimatorPrivate is built on Qt's
  Qt3DAnimation::QAbstractClipAnimatorPrivate, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QClipAnimatorPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'canPlay',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QClipAnimator *Qt3DAnimation::QClipAnimatorPrivate::q_func()
    const': takes in Python what 'QClipAnimator
    *Qt3DAnimation::QClipAnimatorPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QClipAnimatorPrivate is created at the first use,
    not by 'Qt3DAnimation::QClipAnimatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QClipAnimatorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QClipAnimatorPrivate'

  #  A C++ Qt3DAnimation::QClipAnimatorPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QClipAnimatorPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def canPlay(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::QClipAnimatorPrivate::canPlay() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qclipanimatorprivate.html#canPlay
    """
    #  bool Qt3DAnimation::QClipAnimatorPrivate::canPlay() const
    ritual = 'ritual_ZNK13Qt3DAnimation20QClipAnimatorPrivate7canPlayEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13Qt3DAnimation20QClipAnimatorPrivate7canPlayEv')
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
    'Qt3DAnimation::QClipAnimatorPrivate::QClipAnimatorPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qclipanimatorprivate.html
    """
    #  Qt3DAnimation::QClipAnimatorPrivate::QClipAnimatorPrivate()
    self._noteCreation(QClipAnimatorPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation20QClipAnimatorPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DAnimation.QClipAnimator]:
    """
    Calls Qt's 'QClipAnimator
    *Qt3DAnimation::QClipAnimatorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qclipanimatorprivate.html#q_func

    Returns
    -------

    Optional[Qt3DAnimation.QClipAnimator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QClipAnimator *Qt3DAnimation::QClipAnimatorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation20QClipAnimatorPrivate6q_funcEv',
    )
    return Qt3DAnimation.QClipAnimator._cuteAt(address)
