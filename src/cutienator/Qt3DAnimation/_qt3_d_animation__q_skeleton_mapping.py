"""
Qt3DAnimation::QSkeletonMapping binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qskeletonmapping.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSkeletonMapping(Qt3DAnimation.QAbstractChannelMapping):
  """
  The cute side of Qt's Qt3DAnimation::QSkeletonMapping: a plain Python
  object standing in front of one C++ Qt3DAnimation::QSkeletonMapping.

  It is built on the cute 'Qt3DAnimation::QAbstractChannelMapping', as Qt's
  Qt3DAnimation::QSkeletonMapping is built on Qt's
  Qt3DAnimation::QAbstractChannelMapping, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QSkeletonMapping that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'skeleton', 'setSkeleton', 'skeletonChanged', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QSkeletonMapping::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int Qt3DAnimation::QSkeletonMapping::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QSkeletonMapping::~QSkeletonMapping()': the
    destructor: Python never removes a C++ Qt3DAnimation::QSkeletonMapping.
  - Qt's 'Qt3DAnimation::QSkeletonMapping::QSkeletonMapping(
    QSkeletonMappingPrivate &dd, Qt3DCore::QNode *parent)': takes a type
    Python has no way to hand over yet.
  - Qt's 'const QSkeletonMappingPrivate
    *Qt3DAnimation::QSkeletonMapping::d_func() const': takes in Python what
    'QSkeletonMappingPrivate *Qt3DAnimation::QSkeletonMapping::d_func()'
    takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QSkeletonMapping is created at the first use, not
    by 'Qt3DAnimation::QSkeletonMapping(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QSkeletonMapping.
  - Qt tells when it has removed the C++ Qt3DAnimation::QSkeletonMapping.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QSkeletonMapping::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QSkeletonMapping::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation16QSkeletonMapping2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QSkeletonMapping'

  #  A C++ Qt3DAnimation::QSkeletonMapping Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QSkeletonMapping'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *Qt3DAnimation::QSkeletonMapping::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QSkeletonMapping::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation16QSkeletonMapping10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def skeleton(self) -> Optional[Qt3DCore.QAbstractSkeleton]:
    """
    Calls Qt's 'Qt3DCore::QAbstractSkeleton
    *Qt3DAnimation::QSkeletonMapping::skeleton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html#skeleton

    Returns
    -------

    Optional[Qt3DCore.QAbstractSkeleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QAbstractSkeleton
    #      *Qt3DAnimation::QSkeletonMapping::skeleton() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation16QSkeletonMapping8skeletonEv',
    )
    return Qt3DCore.QAbstractSkeleton._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QAbstractSkeleton'])
  @overload(NoneType)
  def setSkeleton(
      self,
      skeleton: Optional[Qt3DCore.QAbstractSkeleton],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QSkeletonMapping::setSkeleton(Qt3DCore::QAbstractSkeleton
    *skeleton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html#setSkeleton

    Parameters
    ----------

    skeleton : Optional[Qt3DCore.QAbstractSkeleton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QSkeletonMapping::setSkeleton(Qt3DCore::
    #      QAbstractSkeleton *skeleton)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation16QSkeletonMapping11setSkeletonEPN8Qt3DCor'
        'e17QAbstractSkeletonE',
        self._addressOf(skeleton),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QSkeletonMapping::QSkeletonMapping(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QSkeletonMapping::QSkeletonMapping(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QSkeletonMapping, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation16QSkeletonMappingC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(WAIT['Qt3DCore.QAbstractSkeleton'])
  @overload(NoneType)
  def skeletonChanged(
      self,
      skeleton: Optional[Qt3DCore.QAbstractSkeleton],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QSkeletonMapping::skeletonChanged(Qt3DCore::
    QAbstractSkeleton *skeleton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html

    Parameters
    ----------

    skeleton : Optional[Qt3DCore.QAbstractSkeleton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QSkeletonMapping::skeletonChanged(Qt3DCore::
    #      QAbstractSkeleton *skeleton)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation16QSkeletonMapping15skeletonChangedEPN8Qt3'
        'DCore17QAbstractSkeletonE',
        self._addressOf(skeleton),
    )

  def d_func(self) -> Optional[Qt3DAnimation.QSkeletonMappingPrivate]:
    """
    Calls Qt's 'QSkeletonMappingPrivate
    *Qt3DAnimation::QSkeletonMapping::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qskeletonmapping.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QSkeletonMappingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSkeletonMappingPrivate *Qt3DAnimation::QSkeletonMapping::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation16QSkeletonMapping6d_funcEv',
    )
    return Qt3DAnimation.QSkeletonMappingPrivate._cuteAt(address)
