"""
Qt3DAnimation::Animation::ClipBlendValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendvalue_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ClipBlendValue to be private: it
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

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ClipBlendValue(Qt3DAnimation.Animation.ClipBlendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ClipBlendValue: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::ClipBlendValue.

  It is built on the cute 'Qt3DAnimation::Animation::ClipBlendNode', as Qt's
  Qt3DAnimation::Animation::ClipBlendValue is built on Qt's
  Qt3DAnimation::Animation::ClipBlendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ClipBlendValue that has a
  ritual and that Python can call so far, 6 names in all: 'clipId',
  'setClipId', 'syncFromFrontEnd', 'duration', 'setClipFormat', 'clipFormat'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::ClipBlendValue::~ClipBlendValue()': the
    destructor: Python never removes a C++
    Qt3DAnimation::Animation::ClipBlendValue.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::ClipBlendValue::allDependencyIds() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::ClipBlendValue::currentDependencyIds() const':
    gives a type Python has no way to take yet.
  - Qt's 'ClipFormat
    &Qt3DAnimation::Animation::ClipBlendValue::clipFormat(Qt3DCore::QNodeId
    animatorId)': gives a type Python has no way to take yet.
  - Qt's 'ClipResults Qt3DAnimation::Animation::ClipBlendValue::doBlend(const
    QList<ClipResults> &blendData) const': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ClipBlendValue is created at the first
    use, not by 'Qt3DAnimation::Animation::ClipBlendValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::ClipBlendValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ClipBlendValue'

  #  A C++ Qt3DAnimation::Animation::ClipBlendValue Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_Animation_ClipBlendValue'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clipId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::ClipBlendValue::clipId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html#clipId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipBlendValue::clipId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue6clipIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def duration(self) -> float:
    """
    Calls Qt's 'double Qt3DAnimation::Animation::ClipBlendValue::duration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html
    """
    #  double Qt3DAnimation::Animation::ClipBlendValue::duration() const
    ritual = 'ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue8durationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13Qt3DAnimation9Animation14ClipBlendValue8duration'
          'Ev')
    return self.uglySide.call(ritual)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def clipFormat(
      self,
      animatorId: Qt3DCore.QNodeId,
  ) -> Qt3DAnimation.Animation.ClipFormat:
    """
    Calls Qt's 'const ClipFormat
    &Qt3DAnimation::Animation::ClipBlendValue::clipFormat(Qt3DCore::QNodeId
    animatorId) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html

    Parameters
    ----------

    animatorId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Qt3DAnimation.Animation.ClipFormat
      A new cute Qt3DAnimation::Animation::ClipFormat around the copy Qt gave
      back. Python owns it.
    """
    #  const ClipFormat
    #      &Qt3DAnimation::Animation::ClipBlendValue::clipFormat(Qt3DCore::
    #      QNodeId animatorId) const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8'
        'Qt3DCore7QNodeIdE',
        self._valueOf(animatorId),
    )
    return Qt3DAnimation.Animation.ClipFormat._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setClipId(self, clipId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendValue::setClipId(Qt3DCore::QNodeId
    clipId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html

    Parameters
    ----------

    clipId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipBlendValue::setClipId(Qt3DCore::
    #      QNodeId clipId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue9setClipIdEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(clipId),
    )

  @overload(
      WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DAnimation.Animation.ClipFormat'],
  )
  def setClipFormat(
      self,
      animatorId: Qt3DCore.QNodeId,
      formatIndices: Qt3DAnimation.Animation.ClipFormat,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendValue::setClipFormat(Qt3DCore::QNodeId
    animatorId, const ClipFormat &formatIndices)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html

    Parameters
    ----------

    animatorId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    formatIndices : Qt3DAnimation.Animation.ClipFormat
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::Animation::ClipFormat, which stays Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipBlendValue::setClipFormat(
    #      Qt3DCore::QNodeId animatorId, const ClipFormat &formatIndices)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue13setClipFormatE'
        'N8Qt3DCore7QNodeIdERKNS0_10ClipFormatE',
        self._valueOf(animatorId), self._valueOf(formatIndices),
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
    'Qt3DAnimation::Animation::ClipBlendValue::ClipBlendValue()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html
    """
    #  Qt3DAnimation::Animation::ClipBlendValue::ClipBlendValue()
    self._noteCreation(ClipBlendValue, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation14ClipBlendValueC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipblendvalue.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue16syncFromFrontE'
        'ndEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation14ClipBlendValue16syncFrom'
          'FrontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
