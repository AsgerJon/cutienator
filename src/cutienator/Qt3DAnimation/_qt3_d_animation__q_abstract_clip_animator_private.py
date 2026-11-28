"""
Qt3DAnimation::QAbstractClipAnimatorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractclipanimator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::QAbstractClipAnimatorPrivate to be private: it
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


class QAbstractClipAnimatorPrivate(Qt3DCore.QComponentPrivate):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractClipAnimatorPrivate: a plain
  Python object standing in front of one C++
  Qt3DAnimation::QAbstractClipAnimatorPrivate.

  It is built on the cute 'Qt3DCore::QComponentPrivate', as Qt's
  Qt3DAnimation::QAbstractClipAnimatorPrivate is built on Qt's
  Qt3DCore::QComponentPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractClipAnimatorPrivate that has
  a ritual and that Python can call so far, 2 names in all: 'canPlay',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractClipAnimator
    *Qt3DAnimation::QAbstractClipAnimatorPrivate::q_func() const': takes in
    Python what 'QAbstractClipAnimator
    *Qt3DAnimation::QAbstractClipAnimatorPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractClipAnimatorPrivate is created at the
    first use, not by 'Qt3DAnimation::QAbstractClipAnimatorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAbstractClipAnimatorPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractClipAnimatorPrivate'

  #  A C++ Qt3DAnimation::QAbstractClipAnimatorPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAbstractClipAnimatorPrivate'

  #  The functions Qt calls itself that
  #  Qt3DAnimation::QAbstractClipAnimatorPrivate is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'canPlay': (
          ('_ZNK13Qt3DAnimation28QAbstractClipAnimatorPrivate7canPlayEv',
           ('bool', 'number', ''),
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

  def canPlay(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::QAbstractClipAnimatorPrivate::canPlay()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimatorprivate.html
    """
    #  bool Qt3DAnimation::QAbstractClipAnimatorPrivate::canPlay() const
    ritual = (
        'ritual_ZNK13Qt3DAnimation28QAbstractClipAnimatorPrivate7canPlayEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13Qt3DAnimation28QAbstractClipAnimatorPrivate7canP'
          'layEv')
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
    'Qt3DAnimation::QAbstractClipAnimatorPrivate::
    QAbstractClipAnimatorPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimatorprivate.html
    """
    #  Qt3DAnimation::QAbstractClipAnimatorPrivate::
    #      QAbstractClipAnimatorPrivate()
    self._noteCreation(QAbstractClipAnimatorPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation28QAbstractClipAnimatorPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DAnimation.QAbstractClipAnimator]:
    """
    Calls Qt's 'QAbstractClipAnimator
    *Qt3DAnimation::QAbstractClipAnimatorPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractclipanimatorprivate.html

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractClipAnimator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractClipAnimator
    #      *Qt3DAnimation::QAbstractClipAnimatorPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation28QAbstractClipAnimatorPrivate6q_funcEv',
    )
    return Qt3DAnimation.QAbstractClipAnimator._cuteAt(address)
