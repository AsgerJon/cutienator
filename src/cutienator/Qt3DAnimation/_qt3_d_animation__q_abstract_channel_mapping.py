"""
Qt3DAnimation::QAbstractChannelMapping binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qabstractchannelmapping.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractChannelMapping(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DAnimation::QAbstractChannelMapping: a plain
  Python object standing in front of one C++
  Qt3DAnimation::QAbstractChannelMapping.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DAnimation::QAbstractChannelMapping is built on Qt's Qt3DCore::QNode,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QAbstractChannelMapping that has a
  ritual and that Python can call so far, 3 names in all: 'metaObject', 'tr',
  'd_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QAbstractChannelMapping::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    Qt3DAnimation::QAbstractChannelMapping::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'Qt3DAnimation::QAbstractChannelMapping::~QAbstractChannelMapping()': the
    destructor: Python never removes a C++
    Qt3DAnimation::QAbstractChannelMapping.
  - Qt's 'Qt3DAnimation::QAbstractChannelMapping::QAbstractChannelMapping(
    QAbstractChannelMappingPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
  - Qt's 'const QAbstractChannelMappingPrivate
    *Qt3DAnimation::QAbstractChannelMapping::d_func() const': takes in Python
    what 'QAbstractChannelMappingPrivate
    *Qt3DAnimation::QAbstractChannelMapping::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QAbstractChannelMapping is created at the first
    use, not by 'Qt3DAnimation::QAbstractChannelMapping(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QAbstractChannelMapping.
  - Qt tells when it has removed the C++
    Qt3DAnimation::QAbstractChannelMapping. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QAbstractChannelMapping that has no cute
    function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DAnimation::QAbstractChannelMapping::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractchannelmapping.html#tr

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
    #  QString Qt3DAnimation::QAbstractChannelMapping::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation23QAbstractChannelMapping2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QAbstractChannelMapping'

  #  A C++ Qt3DAnimation::QAbstractChannelMapping Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QAbstractChannelMapping'

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
    *Qt3DAnimation::QAbstractChannelMapping::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractchannelmapping.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *Qt3DAnimation::QAbstractChannelMapping::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation23QAbstractChannelMapping10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DAnimation::QAbstractChannelMapping::QAbstractChannelMapping(
    QAbstractChannelMappingPrivate &dd, Qt3DCore::QNode *parent)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QAbstractChannelMapping.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DAnimation::QAbstractChannelMapping::QAbstractChannelMapping(QA"
        "bstractChannelMappingPrivate &dd, Qt3DCore::QNode *parent)': takes "
        "a type Python has no way to hand over yet.")

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

  def d_func(self) -> Optional[Qt3DAnimation.QAbstractChannelMappingPrivate]:
    """
    Calls Qt's 'QAbstractChannelMappingPrivate
    *Qt3DAnimation::QAbstractChannelMapping::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qabstractchannelmapping.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QAbstractChannelMappingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractChannelMappingPrivate
    #      *Qt3DAnimation::QAbstractChannelMapping::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation23QAbstractChannelMapping6d_funcEv',
    )
    return Qt3DAnimation.QAbstractChannelMappingPrivate._cuteAt(address)
