"""
Qt3DCore::QAbstractSkeletonPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qabstractskeleton_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAbstractSkeletonPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractSkeletonPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DCore::QAbstractSkeletonPrivate: a plain Python
  object standing in front of one C++ Qt3DCore::QAbstractSkeletonPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DCore::QAbstractSkeletonPrivate is built on Qt's Qt3DCore::QNodePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAbstractSkeletonPrivate that has a ritual
  and that Python can call so far, 3 names in all: 'setJointCount', 'q_func',
  'get'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractSkeleton
    *Qt3DCore::QAbstractSkeletonPrivate::q_func() const': takes in Python
    what 'QAbstractSkeleton *Qt3DCore::QAbstractSkeletonPrivate::q_func()'
    takes.
  - Qt's 'QAbstractSkeletonPrivate
    *Qt3DCore::QAbstractSkeletonPrivate::get(QAbstractSkeleton *q)': takes in
    Python what 'const QAbstractSkeletonPrivate
    *Qt3DCore::QAbstractSkeletonPrivate::get(const QAbstractSkeleton *q)'
    takes.

  What to expect
  --------------

  - The C++ Qt3DCore::QAbstractSkeletonPrivate is created at the first use,
    not by 'Qt3DCore::QAbstractSkeletonPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAbstractSkeletonPrivate.
  """

  #  The enums Qt writes inside Qt3DCore::QAbstractSkeletonPrivate, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class SkeletonType(CuteNum):
    """
    The enum 'Qt3DCore::QAbstractSkeletonPrivate::SkeletonType' of Qt, with
    the 2 names Qt gives in it.
    """

    Skeleton = Kee[int](0)
    SkeletonLoader = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QAbstractSkeleton'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DCore.QAbstractSkeleton],
  ) -> Optional[QAbstractSkeletonPrivate]:
    """
    Calls Qt's 'const QAbstractSkeletonPrivate
    *Qt3DCore::QAbstractSkeletonPrivate::get(const QAbstractSkeleton *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractskeletonprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DCore.QAbstractSkeleton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractSkeletonPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractSkeletonPrivate
    #      *Qt3DCore::QAbstractSkeletonPrivate::get(const QAbstractSkeleton
    #      *q)
    address = Rituals.call(
        'ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate3getEPKNS_17QAbstractS'
        'keletonE',
        CuteMixin._addressOf(q),
    )
    return QAbstractSkeletonPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAbstractSkeletonPrivate'

  #  A C++ Qt3DCore::QAbstractSkeletonPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAbstractSkeletonPrivate'

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
  def setJointCount(self, jointCount: int) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAbstractSkeletonPrivate::setJointCount(int
    jointCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractskeletonprivate.html

    Parameters
    ----------

    jointCount : int
      Passed on as it is.
    """
    #  void Qt3DCore::QAbstractSkeletonPrivate::setJointCount(int jointCount)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate13setJointCountEi',
        jointCount,
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
    'Qt3DCore::QAbstractSkeletonPrivate::QAbstractSkeletonPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractskeletonprivate.html
    """
    #  Qt3DCore::QAbstractSkeletonPrivate::QAbstractSkeletonPrivate()
    self._noteCreation(QAbstractSkeletonPrivate, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore24QAbstractSkeletonPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DCore.QAbstractSkeleton]:
    """
    Calls Qt's 'QAbstractSkeleton
    *Qt3DCore::QAbstractSkeletonPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qabstractskeletonprivate.html#q_func

    Returns
    -------

    Optional[Qt3DCore.QAbstractSkeleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractSkeleton *Qt3DCore::QAbstractSkeletonPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate6q_funcEv',
    )
    return Qt3DCore.QAbstractSkeleton._cuteAt(address)
