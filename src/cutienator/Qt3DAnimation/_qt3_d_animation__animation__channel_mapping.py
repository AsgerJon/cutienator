"""
Qt3DAnimation::Animation::ChannelMapping binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/channelmapping_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ChannelMapping to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChannelMapping(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ChannelMapping: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::ChannelMapping.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::ChannelMapping is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ChannelMapping that has a
  ritual and that Python can call so far, 21 names in all: 'cleanup',
  'syncFromFrontEnd', 'setChannelName', 'channelName', 'setTargetId',
  'targetId', 'setType', 'type', 'setPropertyName', 'propertyName',
  'setComponentCount', 'componentCount', 'setCallback', 'callback',
  'setCallbackFlags', 'callbackFlags', 'setSkeletonId', 'skeletonId',
  'skeleton', 'setMappingType', 'mappingType'. It can be made from Python, in
  1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ChannelMapping is created at the first
    use, not by 'Qt3DAnimation::Animation::ChannelMapping(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::ChannelMapping.
  """

  #  The enums Qt writes inside Qt3DAnimation::Animation::ChannelMapping,
  #  each a class in here as in C++, and the names Qt has for the
  #  combinations of its flags enums.

  class MappingType(CuteNum):
    """
    The enum 'Qt3DAnimation::Animation::ChannelMapping::MappingType' of Qt,
    with the 3 names Qt gives in it.
    """

    ChannelMappingType = Kee[int](0)
    SkeletonMappingType = Kee[int](1)
    CallbackMappingType = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ChannelMapping'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def channelName(self) -> str:
    """
    Calls Qt's 'QString
    Qt3DAnimation::Animation::ChannelMapping::channelName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DAnimation::Animation::ChannelMapping::channelName() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping11channelNameEv',
    )

  def targetId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::ChannelMapping::targetId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DAnimation::Animation::ChannelMapping::targetId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping8targetIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def type(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::ChannelMapping::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html#type
    """
    #  int Qt3DAnimation::Animation::ChannelMapping::type() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping4typeEv',
    )

  def propertyName(self) -> Optional[str]:
    """
    Calls Qt's 'const char
    *Qt3DAnimation::Animation::ChannelMapping::propertyName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *Qt3DAnimation::Animation::ChannelMapping::propertyName()
    #      const
    chars = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping12propertyNameE'
        'v',
    )
    return None if chars is None else chars.decode()

  def componentCount(self) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::ChannelMapping::componentCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html
    """
    #  int Qt3DAnimation::Animation::ChannelMapping::componentCount() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping14componentCoun'
        'tEv',
    )

  def callback(self) -> Optional[Qt3DAnimation.QAnimationCallback]:
    """
    Calls Qt's 'QAnimationCallback
    *Qt3DAnimation::Animation::ChannelMapping::callback() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    Optional[Qt3DAnimation.QAnimationCallback]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAnimationCallback
    #      *Qt3DAnimation::Animation::ChannelMapping::callback() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping8callbackEv',
    )
    return Qt3DAnimation.QAnimationCallback._cuteAt(address)

  def callbackFlags(self) -> Qt3DAnimation.QAnimationCallback.Flags:
    """
    Calls Qt's 'QAnimationCallback::Flags
    Qt3DAnimation::Animation::ChannelMapping::callbackFlags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    Qt3DAnimation.QAnimationCallback.Flags
      The value standing for the combination Qt gave back.
    """
    #  QAnimationCallback::Flags
    #      Qt3DAnimation::Animation::ChannelMapping::callbackFlags() const
    return Qt3DAnimation.QAnimationCallback.Flags(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping13callbackFlags'
        'Ev',
    ))

  def skeletonId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::ChannelMapping::skeletonId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::ChannelMapping::skeletonId() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping10skeletonIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def skeleton(self) -> Optional[Qt3DAnimation.Animation.Skeleton]:
    """
    Calls Qt's 'Skeleton
    *Qt3DAnimation::Animation::ChannelMapping::skeleton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    Optional[Qt3DAnimation.Animation.Skeleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Skeleton *Qt3DAnimation::Animation::ChannelMapping::skeleton() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping8skeletonEv',
    )
    return Qt3DAnimation.Animation.Skeleton._cuteAt(address)

  def mappingType(self) -> MappingType:
    """
    Calls Qt's 'MappingType
    Qt3DAnimation::Animation::ChannelMapping::mappingType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Returns
    -------

    MappingType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MappingType(number)'
      gives.
    """
    #  MappingType Qt3DAnimation::Animation::ChannelMapping::mappingType()
    #      const
    return ChannelMapping.MappingType(self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ChannelMapping11mappingTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setChannelName(self, channelName: str) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setChannelName(const QString
    &channelName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    channelName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setChannelName(const
    #      QString &channelName)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping14setChannelName'
        'ERK7QString',
        channelName,
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setTargetId(self, targetId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setTargetId(Qt3DCore::QNodeId
    targetId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    targetId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setTargetId(Qt3DCore::
    #      QNodeId targetId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping11setTargetIdEN8'
        'Qt3DCore7QNodeIdE',
        self._valueOf(targetId),
    )

  @overload(int)
  def setType(self, type: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::ChannelMapping::setType(int
    type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    type : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setType(int type)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping7setTypeEi', type,
    )

  @overload(str)
  @overload(NoneType)
  def setPropertyName(self, propertyName: Optional[str]) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setPropertyName(const char
    *propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setPropertyName(const
    #      char *propertyName)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping15setPropertyNam'
        'eEPKc',
        self._bytesOf(propertyName),
    )

  @overload(int)
  def setComponentCount(self, componentCount: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setComponentCount(int
    componentCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    componentCount : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setComponentCount(int
    #      componentCount)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping17setComponentCo'
        'untEi',
        componentCount,
    )

  @overload(WAIT['Qt3DAnimation.QAnimationCallback'])
  @overload(NoneType)
  def setCallback(
      self,
      callback: Optional[Qt3DAnimation.QAnimationCallback],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setCallback(QAnimationCallback
    *callback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    callback : Optional[Qt3DAnimation.QAnimationCallback]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setCallback(
    #      QAnimationCallback *callback)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping11setCallbackEPN'
        'S_18QAnimationCallbackE',
        self._addressOf(callback),
    )

  @overload(Qt3DAnimation.QAnimationCallback.Flags)
  def setCallbackFlags(
      self,
      flags: Qt3DAnimation.QAnimationCallback.Flags,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setCallbackFlags(
    QAnimationCallback::Flags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    flags : Qt3DAnimation.QAnimationCallback.Flags
      Passed on as its number.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setCallbackFlags(
    #      QAnimationCallback::Flags flags)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping16setCallbackFla'
        'gsE6QFlagsINS_18QAnimationCallback4FlagEE',
        flags.value,
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setSkeletonId(self, skeletonId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setSkeletonId(Qt3DCore::QNodeId
    skeletonId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    skeletonId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setSkeletonId(
    #      Qt3DCore::QNodeId skeletonId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping13setSkeletonIdE'
        'N8Qt3DCore7QNodeIdE',
        self._valueOf(skeletonId),
    )

  @overload(MappingType)
  def setMappingType(self, mappingType: MappingType) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::setMappingType(MappingType
    mappingType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    mappingType : MappingType
      Passed on as its number.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::setMappingType(
    #      MappingType mappingType)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping14setMappingType'
        'ENS1_11MappingTypeE',
        mappingType.value,
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
    'Qt3DAnimation::Animation::ChannelMapping::ChannelMapping()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html
    """
    #  Qt3DAnimation::Animation::ChannelMapping::ChannelMapping()
    self._noteCreation(ChannelMapping, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMappingC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::ChannelMapping::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping7cleanupEv',
    )

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapping::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapping.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ChannelMapping::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation14ChannelMapping16syncFromFrontE'
        'ndEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation14ChannelMapping16syncFrom'
          'FrontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
