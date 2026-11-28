"""
Qt3DAnimation::QAbstractChannelMappingPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractchannelmapping_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::QAbstractChannelMappingPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractChannelMappingPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractChannelMappingPrivate: a
  plain Python object standing in front of one C++
  Qt3DAnimation::QAbstractChannelMappingPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DAnimation::QAbstractChannelMappingPrivate is built on Qt's
  Qt3DCore::QNodePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractChannelMappingPrivate that
  has a ritual and that Python can call so far, 2 names in all: 'get',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractChannelMapping
    *Qt3DAnimation::QAbstractChannelMappingPrivate::q_func() const': takes in
    Python what 'QAbstractChannelMapping
    *Qt3DAnimation::QAbstractChannelMappingPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractChannelMappingPrivate is created at the
    first use, not by 'Qt3DAnimation::QAbstractChannelMappingPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::QAbstractChannelMappingPrivate.
  """

  #  The enums Qt writes inside
  #  Qt3DAnimation::QAbstractChannelMappingPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MappingType(CuteNum):
    """
    The enum 'Qt3DAnimation::QAbstractChannelMappingPrivate::MappingType' of
    Qt, with the 3 names Qt gives in it.
    """

    ChannelMapping = Kee[int](0)
    SkeletonMapping = Kee[int](1)
    CallbackMapping = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DAnimation.QAbstractChannelMapping'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DAnimation.QAbstractChannelMapping],
  ) -> Optional[QAbstractChannelMappingPrivate]:
    """
    Calls Qt's 'const QAbstractChannelMappingPrivate
    *Qt3DAnimation::QAbstractChannelMappingPrivate::get(const
    Qt3DAnimation::QAbstractChannelMapping *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractchannelmappingprivate.html

    Parameters
    ----------

    q : Optional[Qt3DAnimation.QAbstractChannelMapping]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAbstractChannelMappingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QAbstractChannelMappingPrivate
    #      *Qt3DAnimation::QAbstractChannelMappingPrivate::get(const
    #      Qt3DAnimation::QAbstractChannelMapping *q)
    address = Rituals.call(
        'ritual_ZN13Qt3DAnimation30QAbstractChannelMappingPrivate3getEPKNS_'
        '23QAbstractChannelMappingE',
        CuteMixin._addressOf(q),
    )
    return QAbstractChannelMappingPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractChannelMappingPrivate'

  #  A C++ Qt3DAnimation::QAbstractChannelMappingPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAbstractChannelMappingPrivate'

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
    'Qt3DAnimation::QAbstractChannelMappingPrivate::
    QAbstractChannelMappingPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractchannelmappingprivate.html
    """
    #  Qt3DAnimation::QAbstractChannelMappingPrivate::
    #      QAbstractChannelMappingPrivate()
    self._noteCreation(QAbstractChannelMappingPrivate, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation30QAbstractChannelMappingPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DAnimation.QAbstractChannelMapping]:
    """
    Calls Qt's 'QAbstractChannelMapping
    *Qt3DAnimation::QAbstractChannelMappingPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractchannelmappingprivate.html

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractChannelMapping]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractChannelMapping
    #      *Qt3DAnimation::QAbstractChannelMappingPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation30QAbstractChannelMappingPrivate6q_funcEv',
    )
    return Qt3DAnimation.QAbstractChannelMapping._cuteAt(address)
