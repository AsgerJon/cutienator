"""
Qt3DAnimation::Animation::AdditiveClipBlend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/additiveclipblend_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::AdditiveClipBlend to be private: it
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


class AdditiveClipBlend(Qt3DAnimation.Animation.ClipBlendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::AdditiveClipBlend: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::AdditiveClipBlend.

  It is built on the cute 'Qt3DAnimation::Animation::ClipBlendNode', as Qt's
  Qt3DAnimation::Animation::AdditiveClipBlend is built on Qt's
  Qt3DAnimation::Animation::ClipBlendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::AdditiveClipBlend that has
  a ritual and that Python can call so far, 8 names in all: 'baseClipId',
  'setBaseClipId', 'additiveClipId', 'setAdditiveClipId', 'additiveFactor',
  'setAdditiveFactor', 'syncFromFrontEnd', 'duration'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DAnimation::Animation::AdditiveClipBlend::~AdditiveClipBlend()':
    the destructor: Python never removes a C++
    Qt3DAnimation::Animation::AdditiveClipBlend.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::AdditiveClipBlend::allDependencyIds() const':
    gives a type Python has no way to take yet.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DAnimation::Animation::AdditiveClipBlend::currentDependencyIds()
    const': gives a type Python has no way to take yet.
  - Qt's 'ClipResults
    Qt3DAnimation::Animation::AdditiveClipBlend::doBlend(const
    QList<ClipResults> &blendData) const': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::AdditiveClipBlend is created at the
    first use, not by 'Qt3DAnimation::Animation::AdditiveClipBlend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::AdditiveClipBlend.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::AdditiveClipBlend'

  #  A C++ Qt3DAnimation::Animation::AdditiveClipBlend Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DAnimation_Animation_AdditiveClipBlend'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def baseClipId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::AdditiveClipBlend::baseClipId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::AdditiveClipBlend::baseClipId() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend10baseClipId'
        'Ev',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def additiveClipId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::AdditiveClipBlend::additiveClipId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::AdditiveClipBlend::additiveClipId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend14additiveCl'
        'ipIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def additiveFactor(self) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::Animation::AdditiveClipBlend::additiveFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html
    """
    #  float Qt3DAnimation::Animation::AdditiveClipBlend::additiveFactor()
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend14additiveFa'
        'ctorEv',
    )

  def duration(self) -> float:
    """
    Calls Qt's 'double
    Qt3DAnimation::Animation::AdditiveClipBlend::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html
    """
    #  double Qt3DAnimation::Animation::AdditiveClipBlend::duration() const
    ritual = (
        'ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend8durationEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend8durat'
          'ionEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setBaseClipId(self, baseClipId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AdditiveClipBlend::setBaseClipId(Qt3DCore::
    QNodeId baseClipId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html

    Parameters
    ----------

    baseClipId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::AdditiveClipBlend::setBaseClipId(
    #      Qt3DCore::QNodeId baseClipId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend13setBaseClip'
        'IdEN8Qt3DCore7QNodeIdE',
        self._valueOf(baseClipId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setAdditiveClipId(self, additiveClipId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveClipId(
    Qt3DCore::QNodeId additiveClipId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html

    Parameters
    ----------

    additiveClipId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveClipId(
    #      Qt3DCore::QNodeId additiveClipId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend17setAdditive'
        'ClipIdEN8Qt3DCore7QNodeIdE',
        self._valueOf(additiveClipId),
    )

  @overload(float)
  def setAdditiveFactor(self, additiveFactor: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveFactor(float
    additiveFactor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html

    Parameters
    ----------

    additiveFactor : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveFactor(
    #      float additiveFactor)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend17setAdditive'
        'FactorEf',
        additiveFactor,
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
    'Qt3DAnimation::Animation::AdditiveClipBlend::AdditiveClipBlend()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html
    """
    #  Qt3DAnimation::Animation::AdditiveClipBlend::AdditiveClipBlend()
    self._noteCreation(AdditiveClipBlend, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlendC1Ev',
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
    Qt3DAnimation::Animation::AdditiveClipBlend::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-additiveclipblend.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::AdditiveClipBlend::syncFromFrontEnd(
    #      const Qt3DCore::QNode *frontEnd, bool firstTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend16syncFromFro'
        'ntEndEPKN8Qt3DCore5QNodeEb',
        self._addressOf(frontEnd), firstTime,
    )
