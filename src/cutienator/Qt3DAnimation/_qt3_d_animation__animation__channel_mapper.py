"""
Qt3DAnimation::Animation::ChannelMapper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/channelmapper_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ChannelMapper to be private: it
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
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ChannelMapper(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ChannelMapper: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::ChannelMapper.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::ChannelMapper is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ChannelMapper that has a
  ritual and that Python can call so far, 3 names in all: 'cleanup',
  'syncFromFrontEnd', 'updateMappings'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DAnimation::Animation::ChannelMapper::setMappingIds(const
    Qt3DCore::QNodeIdVector &mappingIds)': takes a type Python has no way to
    hand over yet.
  - Qt's 'Qt3DCore::QNodeIdVector
    Qt3DAnimation::Animation::ChannelMapper::mappingIds() const': gives a
    type Python has no way to take yet.
  - Qt's 'QVector<ChannelMapping *>
    Qt3DAnimation::Animation::ChannelMapper::mappings() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ChannelMapper is created at the first
    use, not by 'Qt3DAnimation::Animation::ChannelMapper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::ChannelMapper.
  - Each name of Qt's Qt3DAnimation::Animation::ChannelMapper that has no
    cute function yet, 'mappingIds', 'mappings', 'setMappingIds', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ChannelMapper'

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
    'Qt3DAnimation::Animation::ChannelMapper::ChannelMapper()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapper.html
    """
    #  Qt3DAnimation::Animation::ChannelMapper::ChannelMapper()
    self._noteCreation(ChannelMapper, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation13ChannelMapperC1Ev',
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
    Calls Qt's 'void Qt3DAnimation::Animation::ChannelMapper::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapper.html#cleanup
    """
    #  void Qt3DAnimation::Animation::ChannelMapper::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13ChannelMapper7cleanupEv',
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
    Qt3DAnimation::Animation::ChannelMapper::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapper.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ChannelMapper::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation13ChannelMapper16syncFromFrontEn'
        'dEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation13ChannelMapper16syncFromF'
          'rontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def updateMappings(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ChannelMapper::updateMappings() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-channelmapper.html
    """
    #  void Qt3DAnimation::Animation::ChannelMapper::updateMappings() const
    self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13ChannelMapper14updateMappings'
        'Ev',
    )

  @staticmethod
  def mappingIds(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeIdVector
    Qt3DAnimation::Animation::ChannelMapper::mappingIds() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ChannelMapper.mappingIds' has no cute "
        "function yet. Qt's 'Qt3DCore::QNodeIdVector "
        "Qt3DAnimation::Animation::ChannelMapper::mappingIds() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def mappings(*__, **_) -> Never:
    """
    Qt's 'QVector<ChannelMapping *>
    Qt3DAnimation::Animation::ChannelMapper::mappings() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ChannelMapper.mappings' has no cute "
        "function yet. Qt's 'QVector<ChannelMapping *> "
        "Qt3DAnimation::Animation::ChannelMapper::mappings() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setMappingIds(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::Animation::ChannelMapper::setMappingIds(const
    Qt3DCore::QNodeIdVector &mappingIds)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ChannelMapper.setMappingIds' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ChannelMapper::setMappingIds(const "
        "Qt3DCore::QNodeIdVector &mappingIds)': takes a type Python has no "
        "way to hand over yet.")
