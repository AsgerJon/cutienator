"""
Qt3DAnimation::QChannelMapping binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/qchannelmapping.h, Qt 6.12.0. Changes made here are lost.
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


class QChannelMapping(Qt3DAnimation.QAbstractChannelMapping):
  """
  The cute side of Qt's Qt3DAnimation::QChannelMapping: a plain Python object
  standing in front of one C++ Qt3DAnimation::QChannelMapping.

  It is built on the cute 'Qt3DAnimation::QAbstractChannelMapping', as Qt's
  Qt3DAnimation::QChannelMapping is built on Qt's
  Qt3DAnimation::QAbstractChannelMapping, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::QChannelMapping that has a ritual and
  that Python can call so far, 12 names in all: 'metaObject', 'tr',
  'channelName', 'target', 'property', 'setChannelName', 'setTarget',
  'setProperty', 'channelNameChanged', 'targetChanged', 'propertyChanged',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DAnimation::QChannelMapping::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int Qt3DAnimation::QChannelMapping::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DAnimation::QChannelMapping::~QChannelMapping()': the
    destructor: Python never removes a C++ Qt3DAnimation::QChannelMapping.
  - Qt's
    'Qt3DAnimation::QChannelMapping::QChannelMapping(QChannelMappingPrivate
    &dd, Qt3DCore::QNode *parent)': takes a type Python has no way to hand
    over yet.
  - Qt's 'const QChannelMappingPrivate
    *Qt3DAnimation::QChannelMapping::d_func() const': takes in Python what
    'QChannelMappingPrivate *Qt3DAnimation::QChannelMapping::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 20 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DAnimation::QChannelMapping is created at the first use, not
    by 'Qt3DAnimation::QChannelMapping(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::QChannelMapping.
  - Qt tells when it has removed the C++ Qt3DAnimation::QChannelMapping.
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
    Calls Qt's 'QString Qt3DAnimation::QChannelMapping::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#tr

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
    #  QString Qt3DAnimation::QChannelMapping::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::QChannelMapping'

  #  A C++ Qt3DAnimation::QChannelMapping Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_QChannelMapping'

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
    *Qt3DAnimation::QChannelMapping::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DAnimation::QChannelMapping::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QChannelMapping10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def channelName(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QChannelMapping::channelName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#channelName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QChannelMapping::channelName() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QChannelMapping11channelNameEv',
    )

  def target(self) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'Qt3DCore::QNode *Qt3DAnimation::QChannelMapping::target()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#target

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QNode *Qt3DAnimation::QChannelMapping::target() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QChannelMapping6targetEv',
    )
    return Qt3DCore.QNode._cuteAt(address)

  def property(self) -> str:
    """
    Calls Qt's 'QString Qt3DAnimation::QChannelMapping::property() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#property

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::QChannelMapping::property() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation15QChannelMapping8propertyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setChannelName(self, channelName: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelMapping::setChannelName(const
    QString &channelName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#setChannelName

    Parameters
    ----------

    channelName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QChannelMapping::setChannelName(const QString
    #      &channelName)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping14setChannelNameERK7QStri'
        'ng',
        channelName,
    )

  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def setTarget(self, target: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QChannelMapping::setTarget(Qt3DCore::QNode *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#setTarget

    Parameters
    ----------

    target : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QChannelMapping::setTarget(Qt3DCore::QNode
    #      *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping9setTargetEPN8Qt3DCore5QN'
        'odeE',
        self._addressOf(target),
    )

  @overload(str)
  def setProperty(self, property: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelMapping::setProperty(const
    QString &property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#setProperty

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QChannelMapping::setProperty(const QString
    #      &property)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping11setPropertyERK7QString',
        property,
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
    'Qt3DAnimation::QChannelMapping::QChannelMapping(Qt3DCore::QNode
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#QChannelMapping

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DAnimation::QChannelMapping::QChannelMapping(Qt3DCore::QNode
    #      *parent)
    self._noteCreation(QChannelMapping, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation15QChannelMappingC1EPN8Qt3DCore5QNodeE',
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

  @overload(str)
  def channelNameChanged(self, channelName: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QChannelMapping::channelNameChanged(QString channelName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html

    Parameters
    ----------

    channelName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QChannelMapping::channelNameChanged(QString
    #      channelName)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping18channelNameChangedE7QSt'
        'ring',
        channelName,
    )

  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def targetChanged(self, target: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::QChannelMapping::targetChanged(Qt3DCore::QNode *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#targetChanged

    Parameters
    ----------

    target : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::QChannelMapping::targetChanged(Qt3DCore::QNode
    #      *target)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping13targetChangedEPN8Qt3DCo'
        're5QNodeE',
        self._addressOf(target),
    )

  @overload(str)
  def propertyChanged(self, property: str) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::QChannelMapping::propertyChanged(QString
    property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#propertyChanged

    Parameters
    ----------

    property : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::QChannelMapping::propertyChanged(QString property)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping15propertyChangedE7QStrin'
        'g',
        property,
    )

  def d_func(self) -> Optional[Qt3DAnimation.QChannelMappingPrivate]:
    """
    Calls Qt's 'QChannelMappingPrivate
    *Qt3DAnimation::QChannelMapping::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-qchannelmapping.html#d_func

    Returns
    -------

    Optional[Qt3DAnimation.QChannelMappingPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChannelMappingPrivate *Qt3DAnimation::QChannelMapping::d_func()
    address = self.uglySide.call(
        'ritual_ZN13Qt3DAnimation15QChannelMapping6d_funcEv',
    )
    return Qt3DAnimation.QChannelMappingPrivate._cuteAt(address)
