"""
Qt3DAnimation::Animation::LerpClipBlend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/lerpclipblend_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::LerpClipBlend to be private: it
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


class LerpClipBlend(Qt3DAnimation.Animation.ClipBlendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::LerpClipBlend: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::LerpClipBlend.

  It is built on the cute 'Qt3DAnimation::Animation::ClipBlendNode', as Qt's
  Qt3DAnimation::Animation::LerpClipBlend is built on Qt's
  Qt3DAnimation::Animation::ClipBlendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::LerpClipBlend that has a
  ritual and that Python can call so far, 8 names in all: 'blendFactor',
  'setBlendFactor', 'startClipId', 'setStartClipId', 'endClipId',
  'setEndClipId', 'syncFromFrontEnd', 'duration'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::LerpClipBlend::~LerpClipBlend()': the
    destructor: Python never removes a C++
    Qt3DAnimation::Animation::LerpClipBlend.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::LerpClipBlend::allDependencyIds() const': gives
    a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::LerpClipBlend::currentDependencyIds() const':
    gives a type Python has no way to take yet.
  - Qt's 'ClipResults Qt3DAnimation::Animation::LerpClipBlend::doBlend(const
    QList<ClipResults> &blendData) const': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::LerpClipBlend is created at the first
    use, not by 'Qt3DAnimation::Animation::LerpClipBlend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::LerpClipBlend.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::LerpClipBlend'

  #  A C++ Qt3DAnimation::Animation::LerpClipBlend Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_Animation_LerpClipBlend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def blendFactor(self) -> float:
    """
    Calls Qt's 'float Qt3DAnimation::Animation::LerpClipBlend::blendFactor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html
    """
    #  float Qt3DAnimation::Animation::LerpClipBlend::blendFactor() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend11blendFactorEv',
    )

  def startClipId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::LerpClipBlend::startClipId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::LerpClipBlend::startClipId() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend11startClipIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def endClipId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::LerpClipBlend::endClipId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DAnimation::Animation::LerpClipBlend::endClipId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend9endClipIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def duration(self) -> float:
    """
    Calls Qt's 'double Qt3DAnimation::Animation::LerpClipBlend::duration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html
    """
    #  double Qt3DAnimation::Animation::LerpClipBlend::duration() const
    ritual = 'ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend8durationEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13Qt3DAnimation9Animation13LerpClipBlend8durationE'
          'v')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setBlendFactor(self, blendFactor: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::LerpClipBlend::setBlendFactor(float
    blendFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html

    Parameters
    ----------

    blendFactor : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::LerpClipBlend::setBlendFactor(float
    #      blendFactor)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend14setBlendFactorE'
        'f',
        blendFactor,
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setStartClipId(self, startClipId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::LerpClipBlend::setStartClipId(Qt3DCore::QNodeId
    startClipId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html

    Parameters
    ----------

    startClipId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::LerpClipBlend::setStartClipId(
    #      Qt3DCore::QNodeId startClipId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend14setStartClipIdE'
        'N8Qt3DCore7QNodeIdE',
        self._valueOf(startClipId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setEndClipId(self, endClipId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::LerpClipBlend::setEndClipId(Qt3DCore::QNodeId
    endClipId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html

    Parameters
    ----------

    endClipId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::LerpClipBlend::setEndClipId(Qt3DCore::
    #      QNodeId endClipId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend12setEndClipIdEN8'
        'Qt3DCore7QNodeIdE',
        self._valueOf(endClipId),
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
    'Qt3DAnimation::Animation::LerpClipBlend::LerpClipBlend()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html
    """
    #  Qt3DAnimation::Animation::LerpClipBlend::LerpClipBlend()
    self._noteCreation(LerpClipBlend, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation13LerpClipBlendC1Ev',
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
    Qt3DAnimation::Animation::LerpClipBlend::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-lerpclipblend.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::LerpClipBlend::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend16syncFromFrontEn'
        'dEPKN8Qt3DCore5QNodeEb',
        self._addressOf(frontEnd), firstTime,
    )
