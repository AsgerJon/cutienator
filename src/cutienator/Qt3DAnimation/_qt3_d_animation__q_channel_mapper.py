"""
Qt3DAnimation::QChannelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qchannelmapper.h, Qt 6.12.0. Changes made here are lost.
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


class QChannelMapper(Qt3DCore.QNode):
  """
  The cute side of Qt's Qt3DAnimation::QChannelMapper: a plain Python object
  standing in front of one C++ Qt3DAnimation::QChannelMapper.

  It is built on the cute 'Qt3DCore::QNode', as Qt's
  Qt3DAnimation::QChannelMapper is built on Qt's Qt3DCore::QNode, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QChannelMapper that has a ritual and
  that Python can call so far, 5 names in all: 'metaObject', 'tr',
  'addMapping', 'removeMapping', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QChannelMapper::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DAnimation::QChannelMapper::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QChannelMapper::~QChannelMapper()': the destructor:
    Python never removes a C++ Qt3DAnimation::QChannelMapper.
  - Qt's 'QList<QAbstractChannelMapping *>
    Qt3DAnimation::QChannelMapper::mappings() const': gives a type Python has
    no way to take yet.
  - Qt's 'Qt3DAnimation::QChannelMapper::QChannelMapper(QChannelMapperPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QChannelMapperPrivate
    *Qt3DAnimation::QChannelMapper::d_func() const': takes in Python what
    'QChannelMapperPrivate *Qt3DAnimation::QChannelMapper::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QChannelMapper is created at the first use, not by
    'Qt3DAnimation::QChannelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QChannelMapper.
  - Qt tells when it has removed the C++ Qt3DAnimation::QChannelMapper. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DAnimation::QChannelMapper that has no cute function
    yet, 'mappings', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString Qt3DAnimation::QChannelMapper::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapper.html#tr

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
    #  QString Qt3DAnimation::QChannelMapper::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation14QChannelMapper2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QChannelMapper'

  #  A C++ Qt3DAnimation::QChannelMapper Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QChannelMapper'

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
    *Qt3DAnimation::QChannelMapper::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QChannelMapper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation14QChannelMapper10metaObjectEv',
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

  @overload()
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DAnimation::QChannelMapper::QChannelMapper(Qt3DCore::QNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapper.html#QChannelMapper

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QChannelMapper::QChannelMapper(Qt3DCore::QNode *parent)
    self._noteCreation(QChannelMapper, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation14QChannelMapperC1EPN8Qt3DCore5QNodeE',
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

  @overload(WAIT['Qt3DAnimation.QAbstractChannelMapping'])
  @overload(NoneType)
  def addMapping(
      self,
      mapping: Optional[Qt3DAnimation.QAbstractChannelMapping],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QChannelMapper::addMapping(QAbstractChannelMapping
    *mapping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapper.html#addMapping

    Parameters
    ----------

    mapping : Optional[Qt3DAnimation.QAbstractChannelMapping]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QChannelMapper::addMapping(QAbstractChannelMapping
    #      *mapping)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QChannelMapper10addMappingEPNS_23QAbstra'
        'ctChannelMappingE',
        self._addressOf(mapping),
    )

  @overload(WAIT['Qt3DAnimation.QAbstractChannelMapping'])
  @overload(NoneType)
  def removeMapping(
      self,
      mapping: Optional[Qt3DAnimation.QAbstractChannelMapping],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QChannelMapper::removeMapping(QAbstractChannelMapping
    *mapping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapper.html#removeMapping

    Parameters
    ----------

    mapping : Optional[Qt3DAnimation.QAbstractChannelMapping]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QChannelMapper::removeMapping(
    #      QAbstractChannelMapping *mapping)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QChannelMapper13removeMappingEPNS_23QAbs'
        'tractChannelMappingE',
        self._addressOf(mapping),
    )

  def d_func(self) -> Optional[Qt3DAnimation.QChannelMapperPrivate]:
    """
    Calls Qt's 'QChannelMapperPrivate
    *Qt3DAnimation::QChannelMapper::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapper.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QChannelMapperPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChannelMapperPrivate *Qt3DAnimation::QChannelMapper::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation14QChannelMapper6d_funcEv',
    )
    return Qt3DAnimation.QChannelMapperPrivate._cuteAt(address)

  @staticmethod
  def mappings(*__, **_) -> Never:
    """
    Qt's 'QList<QAbstractChannelMapping *>
    Qt3DAnimation::QChannelMapper::mappings() const': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.QChannelMapper.mappings' has no cute function yet. "
        "Qt's 'QList<QAbstractChannelMapping *> "
        "Qt3DAnimation::QChannelMapper::mappings() const': gives a type "
        "Python has no way to take yet.")
