"""
Qt3DAnimation::Animation::BlendedClipAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DAnimation/6.12.0/Qt3DAnimation/private/blendedclipanimator_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DAnimation::Animation::BlendedClipAnimator to be private: it
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


class BlendedClipAnimator(Qt3DAnimation.Animation.BackendNode):
  """
  The cute side of Qt's Qt3DAnimation::Animation::BlendedClipAnimator: a
  plain Python object standing in front of one C++
  Qt3DAnimation::Animation::BlendedClipAnimator.

  It is built on the cute 'Qt3DAnimation::Animation::BackendNode', as Qt's
  Qt3DAnimation::Animation::BlendedClipAnimator is built on Qt's
  Qt3DAnimation::Animation::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DAnimation::Animation::BlendedClipAnimator that
  has a ritual and that Python can call so far, 26 names in all: 'cleanup',
  'syncFromFrontEnd', 'blendTreeRootId', 'mapperId', 'clockId', 'isRunning',
  'setNormalizedLocalTime', 'normalizedLocalTime', 'canRun',
  'setBlendTreeRootId', 'setMapperId', 'setClockId', 'setRunning',
  'setStartTime', 'setLoops', 'loops', 'currentLoop', 'setCurrentLoop',
  'animationClipMarkedDirty', 'nsSincePreviousFrame', 'setLastGlobalTimeNS',
  'lastLocalTime', 'setLastLocalTime', 'lastNormalizedLocalTime',
  'setLastNormalizedLocalTime', 'isSeeking'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setMappingData(const
    QVector<MappingData> &mappingData)': takes a type Python has no way to
    hand over yet.
  - Qt's 'QVector<MappingData>
    Qt3DAnimation::Animation::BlendedClipAnimator::mappingData() const':
    gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DAnimation::Animation::BlendedClipAnimator is created at the
    first use, not by 'Qt3DAnimation::Animation::BlendedClipAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    Qt3DAnimation::Animation::BlendedClipAnimator.
  - Each name of Qt's Qt3DAnimation::Animation::BlendedClipAnimator that has
    no cute function yet, 'mappingData', 'setMappingData', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DAnimation::Animation::BlendedClipAnimator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def blendTreeRootId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::BlendedClipAnimator::blendTreeRootId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::BlendedClipAnimator::blendTreeRootId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator15blendTre'
        'eRootIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def mapperId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::BlendedClipAnimator::mapperId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::BlendedClipAnimator::mapperId() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator8mapperIdE'
        'v',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def clockId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DAnimation::Animation::BlendedClipAnimator::clockId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId
    #      Qt3DAnimation::Animation::BlendedClipAnimator::clockId() const
    address = self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator7clockIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DAnimation::Animation::BlendedClipAnimator::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  bool Qt3DAnimation::Animation::BlendedClipAnimator::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator9isRunning'
        'Ev',
    )

  def normalizedLocalTime(self) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::Animation::BlendedClipAnimator::normalizedLocalTime()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  float Qt3DAnimation::Animation::BlendedClipAnimator::
    #      normalizedLocalTime() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator19normaliz'
        'edLocalTimeEv',
    )

  def canRun(self) -> bool:
    """
    Calls Qt's 'bool Qt3DAnimation::Animation::BlendedClipAnimator::canRun()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  bool Qt3DAnimation::Animation::BlendedClipAnimator::canRun() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator6canRunEv',
    )

  def loops(self) -> int:
    """
    Calls Qt's 'int Qt3DAnimation::Animation::BlendedClipAnimator::loops()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  int Qt3DAnimation::Animation::BlendedClipAnimator::loops() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator5loopsEv',
    )

  def currentLoop(self) -> int:
    """
    Calls Qt's 'int
    Qt3DAnimation::Animation::BlendedClipAnimator::currentLoop() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  int Qt3DAnimation::Animation::BlendedClipAnimator::currentLoop() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator11currentL'
        'oopEv',
    )

  def lastLocalTime(self) -> float:
    """
    Calls Qt's 'double
    Qt3DAnimation::Animation::BlendedClipAnimator::lastLocalTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  double Qt3DAnimation::Animation::BlendedClipAnimator::lastLocalTime()
    #      const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator13lastLoca'
        'lTimeEv',
    )

  def isSeeking(self) -> bool:
    """
    Calls Qt's 'bool
    Qt3DAnimation::Animation::BlendedClipAnimator::isSeeking() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  bool Qt3DAnimation::Animation::BlendedClipAnimator::isSeeking() const
    return self.uglySide.call(
        'ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator9isSeeking'
        'Ev',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  @overload(float, bool)
  def setNormalizedLocalTime(
      self,
      normalizedTime: float,
      allowMarkDirty: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setNormalizedLocalTime(
    float normalizedTime, bool allowMarkDirty)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    normalizedTime : float
      Passed on as it is.

    allowMarkDirty : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::
    #      setNormalizedLocalTime(float normalizedTime, bool allowMarkDirty)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator22setNormal'
        'izedLocalTimeEfb',
        normalizedTime, allowMarkDirty,
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setBlendTreeRootId(self, blendTreeRootId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setBlendTreeRootId(
    Qt3DCore::QNodeId blendTreeRootId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    blendTreeRootId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void
    #      Qt3DAnimation::Animation::BlendedClipAnimator::setBlendTreeRootId(
    #      Qt3DCore::QNodeId blendTreeRootId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator18setBlendT'
        'reeRootIdEN8Qt3DCore7QNodeIdE',
        self._valueOf(blendTreeRootId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setMapperId(self, mapperId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setMapperId(Qt3DCore::
    QNodeId mapperId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    mapperId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::setMapperId(
    #      Qt3DCore::QNodeId mapperId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator11setMapper'
        'IdEN8Qt3DCore7QNodeIdE',
        self._valueOf(mapperId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def setClockId(self, clockId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setClockId(Qt3DCore::
    QNodeId clockId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    clockId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::setClockId(
    #      Qt3DCore::QNodeId clockId)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setClockI'
        'dEN8Qt3DCore7QNodeIdE',
        self._valueOf(clockId),
    )

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setRunning(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::setRunning(bool
    #      running)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setRunnin'
        'gEb',
        running,
    )

  @overload(int)
  def setStartTime(self, globalTime: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setStartTime(qint64
    globalTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    globalTime : int
      Passed on as it is.
    """
    #  void
    #      Qt3DAnimation::Animation::BlendedClipAnimator::setStartTime(qint64
    #      globalTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator12setStartT'
        'imeEx',
        globalTime,
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setLoops(int loops)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::setLoops(int
    #      loops)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator8setLoopsEi',
        loops,
    )

  @overload(int)
  def setCurrentLoop(self, currentLoop: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setCurrentLoop(int
    currentLoop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    currentLoop : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::setCurrentLoop(int
    #      currentLoop)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator14setCurren'
        'tLoopEi',
        currentLoop,
    )

  @overload(int)
  def setLastGlobalTimeNS(self, lastGlobalTimeNS: int) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setLastGlobalTimeNS(const
    qint64 &lastGlobalTimeNS)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    lastGlobalTimeNS : int
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::
    #      setLastGlobalTimeNS(const qint64 &lastGlobalTimeNS)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator19setLastGl'
        'obalTimeNSERKx',
        lastGlobalTimeNS,
    )

  @overload(float)
  def setLastLocalTime(self, lastLocalTime: float) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setLastLocalTime(double
    lastLocalTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    lastLocalTime : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::setLastLocalTime(
    #      double lastLocalTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator16setLastLo'
        'calTimeEd',
        lastLocalTime,
    )

  @overload(float)
  def setLastNormalizedLocalTime(self, normalizedTime: float) -> None:
    """
    Calls Qt's 'void Qt3DAnimation::Animation::BlendedClipAnimator::
    setLastNormalizedLocalTime(float normalizedTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    normalizedTime : float
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::
    #      setLastNormalizedLocalTime(float normalizedTime)
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator26setLastNo'
        'rmalizedLocalTimeEf',
        normalizedTime,
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
    'Qt3DAnimation::Animation::BlendedClipAnimator::BlendedClipAnimator()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  Qt3DAnimation::Animation::BlendedClipAnimator::BlendedClipAnimator()
    self._noteCreation(BlendedClipAnimator, lambda: Rituals.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimatorC1Ev',
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
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::cleanup()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator7cleanupEv',
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
    Qt3DAnimation::Animation::BlendedClipAnimator::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::syncFromFrontEnd(
    #      const Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator16syncFromF'
        'rontEndEPKN8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13Qt3DAnimation9Animation19BlendedClipAnimator16syn'
          'cFromFrontEndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def animationClipMarkedDirty(self) -> None:
    """
    Calls Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::animationClipMarkedDirty(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  void Qt3DAnimation::Animation::BlendedClipAnimator::
    #      animationClipMarkedDirty()
    self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator24animation'
        'ClipMarkedDirtyEv',
    )

  @overload(int)
  def nsSincePreviousFrame(self, currentGlobalTimeNS: int) -> int:
    """
    Calls Qt's 'qint64
    Qt3DAnimation::Animation::BlendedClipAnimator::nsSincePreviousFrame(
    qint64 currentGlobalTimeNS)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html

    Parameters
    ----------

    currentGlobalTimeNS : int
      Passed on as it is.
    """
    #  qint64 Qt3DAnimation::Animation::BlendedClipAnimator::
    #      nsSincePreviousFrame(qint64 currentGlobalTimeNS)
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator20nsSincePr'
        'eviousFrameEx',
        currentGlobalTimeNS,
    )

  def lastNormalizedLocalTime(self) -> float:
    """
    Calls Qt's 'float
    Qt3DAnimation::Animation::BlendedClipAnimator::lastNormalizedLocalTime(
    )'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3danimation-animation-blendedclipanimator.html
    """
    #  float Qt3DAnimation::Animation::BlendedClipAnimator::
    #      lastNormalizedLocalTime()
    return self.uglySide.call(
        'ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator23lastNorma'
        'lizedLocalTimeEv',
    )

  @staticmethod
  def mappingData(*__, **_) -> Never:
    """
    Qt's 'QVector<MappingData>
    Qt3DAnimation::Animation::BlendedClipAnimator::mappingData() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BlendedClipAnimator.mappingData' has no "
        "cute function yet. Qt's 'QVector<MappingData> "
        "Qt3DAnimation::Animation::BlendedClipAnimator::mappingData() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setMappingData(*__, **_) -> Never:
    """
    Qt's 'void
    Qt3DAnimation::Animation::BlendedClipAnimator::setMappingData(const
    QVector<MappingData> &mappingData)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DAnimation.Animation.BlendedClipAnimator.setMappingData' has "
        "no cute function yet. Qt's 'void "
        "Qt3DAnimation::Animation::BlendedClipAnimator::setMappingData(const"
        " QVector<MappingData> &mappingData)': takes a type Python has no "
        "way to hand over yet.")
