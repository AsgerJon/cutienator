"""
Qt3DAnimation::Animation::ClipAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipanimator_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::ClipAnimator to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class ClipAnimator(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::ClipAnimator: a plain
  Python object standing in front of one C++
  Qt3DAnimation::Animation::ClipAnimator.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::ClipAnimator is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::ClipAnimator that has a
  ritual and that Python can call so far, 29 names in all: 'cleanup',
  'setClipId', 'clipId', 'setMapperId', 'mapperId', 'setClockId', 'clockId',
  'setRunning', 'isRunning', 'setLoops', 'loops', 'setNormalizedLocalTime',
  'normalizedLocalTime', 'syncFromFrontEnd', 'setHandler', 'canRun',
  'setStartTime', 'currentLoop', 'setCurrentLoop',
  'animationClipMarkedDirty', 'setClipFormat', 'clipFormat',
  'nsSincePreviousFrame', 'setLastGlobalTimeNS', 'lastLocalTime',
  'setLastLocalTime', 'lastNormalizedLocalTime',
  'setLastNormalizedLocalTime', 'isSeeking'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DAnimation::Animation::ClipAnimator::setMappingData(const
    QVector<MappingData> &mappingData)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QVector<MappingData>
    Qt3DAnimation::Animation::ClipAnimator::mappingData() const': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::ClipAnimator is created at the first
    use, not by 'Qt3DAnimation::Animation::ClipAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DAnimation::Animation::ClipAnimator.
  - Each name of Qt's Qt3DAnimation::Animation::ClipAnimator that has no cute
    function yet, 'mappingData', 'setMappingData', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::ClipAnimator'

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
    Qt3DAnimation::Animation::ClipAnimator::clipId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#clipId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::clipId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator6clipIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def mapperId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::ClipAnimator::mapperId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#mapperId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::mapperId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator8mapperIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def clockId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::ClipAnimator::clockId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#clockId

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::clockId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator7clockIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::Animation::ClipAnimator::isRunning()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  bool Qt3DAnimation::Animation::ClipAnimator::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator9isRunningEv',
    )

  def loops(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::ClipAnimator::loops() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#loops
    """
    #  int Qt3DAnimation::Animation::ClipAnimator::loops() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator5loopsEv',
    )

  def normalizedLocalTime(self) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::Animation::ClipAnimator::normalizedLocalTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  float Qt3DAnimation::Animation::ClipAnimator::normalizedLocalTime()
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator19normalizedLocal'
        'TimeEv',
    )

  def canRun(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::Animation::ClipAnimator::canRun() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#canRun
    """
    #  bool Qt3DAnimation::Animation::ClipAnimator::canRun() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator6canRunEv',
    )

  def currentLoop(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::ClipAnimator::currentLoop()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  int Qt3DAnimation::Animation::ClipAnimator::currentLoop() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator11currentLoopEv',
    )

  def clipFormat(self) -> Qt3DAnimation.Animation.ClipFormat:
    """
    Calls Qt's 'ClipFormat
    Qt3DAnimation::Animation::ClipAnimator::clipFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Returns
    -------

    Qt3DAnimation.Animation.ClipFormat
      A new cute Qt3DAnimation::Animation::ClipFormat around the copy Qt gave
      back. Python owns it.
    """
    #  ClipFormat Qt3DAnimation::Animation::ClipAnimator::clipFormat() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator10clipFormatEv',
    )
    return Qt3DAnimation.Animation.ClipFormat._cuteOwning(address)

  def lastLocalTime(self) -> float:
    """
    Calls Qt's 'double
    Qt3DAnimation::Animation::ClipAnimator::lastLocalTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  double Qt3DAnimation::Animation::ClipAnimator::lastLocalTime() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator13lastLocalTimeEv',
    )

  def isSeeking(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::Animation::ClipAnimator::isSeeking()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  bool Qt3DAnimation::Animation::ClipAnimator::isSeeking() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator9isSeekingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setClipId(self, clipId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setClipId(Qt3DCore::QNodeId
    clipId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    clipId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setClipId(Qt3DCore::
    #      QNodeId clipId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator9setClipIdEN8Qt3DC'
        'ore7QNodeIdE',
        self._valueOf(clipId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setMapperId(self, mapperId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setMapperId(Qt3DCore::QNodeId
    mapperId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    mapperId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setMapperId(Qt3DCore::
    #      QNodeId mapperId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator11setMapperIdEN8Qt'
        '3DCore7QNodeIdE',
        self._valueOf(mapperId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setClockId(self, clockId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setClockId(Qt3DCore::QNodeId
    clockId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    clockId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setClockId(Qt3DCore::
    #      QNodeId clockId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setClockIdEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(clockId),
    )

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::ClipAnimator::setRunning(bool
    running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setRunningEb',
        running,
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::ClipAnimator::setLoops(int
    loops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setLoops(int loops)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator8setLoopsEi', loops,
    )

  @overload(float)
  @overload(float, bool)
  def setNormalizedLocalTime(
      self,
      normalizedLocalTime: float,
      allowMarkDirty: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setNormalizedLocalTime(float
    normalizedLocalTime, bool allowMarkDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    normalizedLocalTime : float
      Passed on as it is.

    allowMarkDirty : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setNormalizedLocalTime(
    #      float normalizedLocalTime, bool allowMarkDirty)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator22setNormalizedLoc'
        'alTimeEfb',
        normalizedLocalTime, allowMarkDirty,
    )

  @overload(WAIT['Qt3DAnimation.Animation.Handler'])
  @overload(NoneType)
  def setHandler(
      self,
      handler: Optional[Qt3DAnimation.Animation.Handler],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setHandler(Handler *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    handler : Optional[Qt3DAnimation.Animation.Handler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setHandler(Handler
    #      *handler)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setHandlerEPNS0_'
        '7HandlerE',
        self._addressOf(handler),
    )

  @overload(int)
  def setStartTime(self, globalTime: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setStartTime(qint64 globalTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    globalTime : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setStartTime(qint64
    #      globalTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator12setStartTimeEx',
        globalTime,
    )

  @overload(int)
  def setCurrentLoop(self, currentLoop: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setCurrentLoop(int currentLoop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    currentLoop : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setCurrentLoop(int
    #      currentLoop)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator14setCurrentLoopEi',
        currentLoop,
    )

  @overload(WAIT['Qt3DAnimation.Animation.ClipFormat'])
  def setClipFormat(
      self,
      clipFormat: Qt3DAnimation.Animation.ClipFormat,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setClipFormat(const ClipFormat
    &clipFormat)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    clipFormat : Qt3DAnimation.Animation.ClipFormat
      Passed on as a value: Qt reads the C++
      Qt3DAnimation::Animation::ClipFormat, which stays Python's own.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setClipFormat(const
    #      ClipFormat &clipFormat)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator13setClipFormatERK'
        'NS0_10ClipFormatE',
        self._valueOf(clipFormat),
    )

  @overload(int)
  def setLastGlobalTimeNS(self, lastGlobalTimeNS: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setLastGlobalTimeNS(qint64
    lastGlobalTimeNS)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    lastGlobalTimeNS : int
      Passed on as it is.
    """
    #  void
    #      Qt3DAnimation::Animation::ClipAnimator::setLastGlobalTimeNS(qint64
    #      lastGlobalTimeNS)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator19setLastGlobalTim'
        'eNSEx',
        lastGlobalTimeNS,
    )

  @overload(float)
  def setLastLocalTime(self, lastLocalTime: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setLastLocalTime(double
    lastLocalTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    lastLocalTime : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::setLastLocalTime(double
    #      lastLocalTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator16setLastLocalTime'
        'Ed',
        lastLocalTime,
    )

  @overload(float)
  def setLastNormalizedLocalTime(self, normalizedLocalTime: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::setLastNormalizedLocalTime(float
    normalizedLocalTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    normalizedLocalTime : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::
    #      setLastNormalizedLocalTime(float normalizedLocalTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator26setLastNormalize'
        'dLocalTimeEf',
        normalizedLocalTime,
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
    'Qt3DAnimation::Animation::ClipAnimator::ClipAnimator()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  Qt3DAnimation::Animation::ClipAnimator::ClipAnimator()
    self._noteCreation(ClipAnimator, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimatorC1Ev',
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
    Calls Qt's 'void Qt3DAnimation::Animation::ClipAnimator::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html#cleanup
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator7cleanupEv',
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
    Qt3DAnimation::Animation::ClipAnimator::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::ClipAnimator::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator16syncFromFrontEnd'
        'EPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation12ClipAnimator16syncFromFr'
          'ontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def animationClipMarkedDirty(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::ClipAnimator::animationClipMarkedDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  void
    #      Qt3DAnimation::Animation::ClipAnimator::animationClipMarkedDirty()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator24animationClipMar'
        'kedDirtyEv',
    )

  @overload(int)
  def nsSincePreviousFrame(self, currentGlobalTimeNS: int) -> int:
    """
    Calls Qt's 'qint64
    Qt3DAnimation::Animation::ClipAnimator::nsSincePreviousFrame(qint64
    currentGlobalTimeNS)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html

    Parameters
    ----------

    currentGlobalTimeNS : int
      Passed on as it is.
    """
    #  qint64 Qt3DAnimation::Animation::ClipAnimator::nsSincePreviousFrame(
    #      qint64 currentGlobalTimeNS)
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator20nsSincePreviousF'
        'rameEx',
        currentGlobalTimeNS,
    )

  def lastNormalizedLocalTime(self) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::Animation::ClipAnimator::lastNormalizedLocalTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-clipanimator.html
    """
    #  float
    #      Qt3DAnimation::Animation::ClipAnimator::lastNormalizedLocalTime()
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation12ClipAnimator23lastNormalizedLo'
        'calTimeEv',
    )

  @staticmethod
  def mappingData(*__, **_) -> Never:
    """
    Qt's 'QVector<MappingData>
    Qt3DAnimation::Animation::ClipAnimator::mappingData() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipAnimator.mappingData' has no cute "
        "function yet. Qt's 'QVector<MappingData> "
        "Qt3DAnimation::Animation::ClipAnimator::mappingData() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setMappingData(*__, **_) -> Never:
    """
    Qt's 'void Qt3DAnimation::Animation::ClipAnimator::setMappingData(const
    QVector<MappingData> &mappingData)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.ClipAnimator.setMappingData' has no cute "
        "function yet. Qt's 'void "
        "Qt3DAnimation::Animation::ClipAnimator::setMappingData(const "
        "QVector<MappingData> &mappingData)': takes a type Python has no "
        "way to hand over yet.")
