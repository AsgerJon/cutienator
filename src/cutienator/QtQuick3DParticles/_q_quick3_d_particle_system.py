"""
QQuick3DParticleSystem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleSystem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QPRand, QQuick3DParticle, QQuick3DParticleAffector
  from . import QQuick3DParticleEmitter, QQuick3DParticleSystemLogging
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DParticle = WAIT['QQuick3DParticle']
  QQuick3DParticleAffector = WAIT['QQuick3DParticleAffector']
  QQuick3DParticleEmitter = WAIT['QQuick3DParticleEmitter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleSystem(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DParticleSystem: a plain Python object
  standing in front of one C++ QQuick3DParticleSystem.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DParticleSystem is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleSystem that has a ritual and that
  Python can call so far, 46 names in all: 'metaObject', 'tr', 'isRunning',
  'isPaused', 'startTime', 'time', 'useRandomSeed', 'seed', 'particleCount',
  'logging', 'loggingData', 'registerParticle', 'unRegisterParticle',
  'registerParticleEmitter', 'unRegisterParticleEmitter',
  'registerParticleAffector', 'unRegisterParticleAffector',
  'updateCurrentTime', 'rand', 'isShared', 'currentTime', 'reset',
  'setRunning', 'setPaused', 'setStartTime', 'setTime', 'setUseRandomSeed',
  'setSeed', 'setLogging', 'setEditorTime', 'runningChanged',
  'pausedChanged', 'timeChanged', 'startTimeChanged', 'useRandomSeedChanged',
  'seedChanged', 'loggingChanged', 'loggingDataChanged', 'componentComplete',
  'updateLoggingData', 'resetLoggingVariables', 'doSeedRandomization',
  'refresh', 'markDirty', 'isGloballyDisabled', 'isEditorModeOn'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleSystem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DParticleSystem::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleSystem::~QQuick3DParticleSystem()': the destructor:
    Python never removes a C++ QQuick3DParticleSystem.
  - Qt's 'void QQuick3DParticleSystem::processModelParticle(
    QQuick3DParticleModelParticle *modelParticle, const QVector<TrailEmits>
    &trailEmits, float timeS)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuick3DParticleSystem::processSpriteParticle(
    QQuick3DParticleSpriteParticle *spriteParticle, const QVector<TrailEmits>
    &trailEmits, float timeS)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuick3DParticleSystem::processModelBlendParticle(
    QQuick3DParticleModelBlendParticle *particle, const QVector<TrailEmits>
    &trailEmits, float timeS)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void
    QQuick3DParticleSystem::processParticleCommon(QQuick3DParticleDataCurrent
    &currentData, const QQuick3DParticleData *d, float particleTimeS)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QQuick3DParticleSystem::processParticleFadeInOut(
    QQuick3DParticleDataCurrent &currentData, const QQuick3DParticle
    *particle, float particleTimeS, float particleTimeLeftS)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QQuick3DParticleSystem::processParticleAlignment(
    QQuick3DParticleDataCurrent &currentData, const QQuick3DParticle
    *particle, const QQuick3DParticleData *d)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 58 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleSystem is created at the first use, not by
    'QQuick3DParticleSystem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleSystem.
  - Qt tells when it has removed the C++ QQuick3DParticleSystem. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DParticleSystem that has no cute function yet,
    'processModelBlendParticle', 'processModelParticle',
    'processParticleAlignment', 'processParticleCommon',
    'processParticleFadeInOut', 'processSpriteParticle', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuick3DParticleSystem, each a class in
  #  here as in C++.

  class TrailEmits(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DParticleSystem::TrailEmits: a plain Python
    object standing in front of one C++ QQuick3DParticleSystem::TrailEmits.

    C++ hands a QQuick3DParticleSystem::TrailEmits around as a copy, so every
    C++ QQuick3DParticleSystem::TrailEmits behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuick3DParticleSystem::TrailEmits yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DParticleSystem::TrailEmits::~TrailEmits()': the
      destructor: Python removes its C++ QQuick3DParticleSystem::TrailEmits
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DParticleSystem::TrailEmits is created at the first use,
      not by 'QQuick3DParticleSystem::TrailEmits(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DParticleSystem::TrailEmits back gives a
      copy the ritual made for Python, in a new cute
      QQuick3DParticleSystem::TrailEmits.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DParticleSystem::TrailEmits'

    #  Qt's '~QQuick3DParticleSystem::TrailEmits()'. Naming it makes this a
    #  value class: Python owns every C++ QQuick3DParticleSystem::TrailEmits
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN22QQuick3DParticleSystem10TrailEmitsD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QQuick3DParticleSystem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlesystem.html#tr

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
    #  QString QQuick3DParticleSystem::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQuick3DParticleSystem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def isGloballyDisabled() -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::isGloballyDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#isGloballyDisabled
    """
    #  bool QQuick3DParticleSystem::isGloballyDisabled()
    return Rituals.call(
        'ritual_ZN22QQuick3DParticleSystem18isGloballyDisabledEv',
    )

  @staticmethod
  def isEditorModeOn() -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::isEditorModeOn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#isEditorModeOn
    """
    #  bool QQuick3DParticleSystem::isEditorModeOn()
    return Rituals.call(
        'ritual_ZN22QQuick3DParticleSystem14isEditorModeOnEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleSystem'

  #  A C++ QQuick3DParticleSystem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleSystem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DParticleSystem::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleSystem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#isRunning
    """
    #  bool QQuick3DParticleSystem::isRunning() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem9isRunningEv',
    )

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::isPaused() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#isPaused
    """
    #  bool QQuick3DParticleSystem::isPaused() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem8isPausedEv',
    )

  def startTime(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystem::startTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#startTime
    """
    #  int QQuick3DParticleSystem::startTime() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem9startTimeEv',
    )

  def time(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystem::time() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlesystem.html#time
    """
    #  int QQuick3DParticleSystem::time() const
    return self.uglySide.call('ritual_ZNK22QQuick3DParticleSystem4timeEv')

  def useRandomSeed(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::useRandomSeed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#useRandomSeed
    """
    #  bool QQuick3DParticleSystem::useRandomSeed() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem13useRandomSeedEv',
    )

  def seed(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystem::seed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlesystem.html#seed
    """
    #  int QQuick3DParticleSystem::seed() const
    return self.uglySide.call('ritual_ZNK22QQuick3DParticleSystem4seedEv')

  def particleCount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystem::particleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#particleCount
    """
    #  int QQuick3DParticleSystem::particleCount() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem13particleCountEv',
    )

  def logging(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::logging() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#logging
    """
    #  bool QQuick3DParticleSystem::logging() const
    return self.uglySide.call('ritual_ZNK22QQuick3DParticleSystem7loggingEv')

  def loggingData(self) -> Optional[QQuick3DParticleSystemLogging]:
    """
    Calls Qt's 'QQuick3DParticleSystemLogging
    *QQuick3DParticleSystem::loggingData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#loggingData

    Returns
    -------

    Optional[QQuick3DParticleSystemLogging]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleSystemLogging *QQuick3DParticleSystem::loggingData()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem11loggingDataEv',
    )
    from . import QQuick3DParticleSystemLogging
    return QQuick3DParticleSystemLogging._cuteAt(address)

  @overload(QQuick3DParticle)
  @overload(NoneType)
  def isShared(self, particle: Optional[QQuick3DParticle]) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleSystem::isShared(const QQuick3DParticle
    *particle) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#isShared

    Parameters
    ----------

    particle : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DParticleSystem::isShared(const QQuick3DParticle
    #      *particle) const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem8isSharedEPK16QQuick3DParticle',
        self._addressOf(particle),
    )

  def currentTime(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleSystem::currentTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#currentTime
    """
    #  int QQuick3DParticleSystem::currentTime() const
    return self.uglySide.call(
        'ritual_ZNK22QQuick3DParticleSystem11currentTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setRunning(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem10setRunningEb', running,
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setPaused(bool paused)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setPaused(bool paused)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem9setPausedEb', paused,
    )

  @overload(int)
  def setStartTime(self, startTime: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setStartTime(int startTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setStartTime

    Parameters
    ----------

    startTime : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setStartTime(int startTime)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem12setStartTimeEi', startTime,
    )

  @overload(int)
  def setTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setTime(int time)
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem7setTimeEi', time)

  @overload(bool)
  def setUseRandomSeed(self, randomize: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setUseRandomSeed(bool
    randomize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setUseRandomSeed

    Parameters
    ----------

    randomize : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setUseRandomSeed(bool randomize)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem16setUseRandomSeedEb', randomize,
    )

  @overload(int)
  def setSeed(self, seed: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setSeed(int seed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setSeed

    Parameters
    ----------

    seed : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setSeed(int seed)
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem7setSeedEi', seed)

  @overload(bool)
  def setLogging(self, logging: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setLogging(bool logging)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setLogging

    Parameters
    ----------

    logging : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setLogging(bool logging)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem10setLoggingEb', logging,
    )

  @overload(int)
  def setEditorTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::setEditorTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#setEditorTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::setEditorTime(int time)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem13setEditorTimeEi', time,
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
  @overload(QQuick3DNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DParticleSystem::QQuick3DParticleSystem(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#QQuick3DParticleSystem

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleSystem::QQuick3DParticleSystem(QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleSystem, lambda: Rituals.call(
        'ritual_ZN22QQuick3DParticleSystemC1EP12QQuick3DNode',
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

  @overload(QQuick3DParticle)
  @overload(NoneType)
  def registerParticle(self, particle: Optional[QQuick3DParticle]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSystem::registerParticle(QQuick3DParticle *particle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#registerParticle

    Parameters
    ----------

    particle : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSystem::registerParticle(QQuick3DParticle
    #      *particle)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem16registerParticleEP16QQuick3DPar'
        'ticle',
        self._addressOf(particle),
    )

  @overload(QQuick3DParticle)
  @overload(NoneType)
  def unRegisterParticle(self, particle: Optional[QQuick3DParticle]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSystem::unRegisterParticle(QQuick3DParticle *particle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#unRegisterParticle

    Parameters
    ----------

    particle : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSystem::unRegisterParticle(QQuick3DParticle
    #      *particle)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem18unRegisterParticleEP16QQuick3DP'
        'article',
        self._addressOf(particle),
    )

  @overload(QQuick3DParticleEmitter)
  @overload(NoneType)
  def registerParticleEmitter(
      self,
      e: Optional[QQuick3DParticleEmitter],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSystem::registerParticleEmitter(QQuick3DParticleEmitter
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html

    Parameters
    ----------

    e : Optional[QQuick3DParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSystem::registerParticleEmitter(
    #      QQuick3DParticleEmitter *e)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem23registerParticleEmitterEP23QQui'
        'ck3DParticleEmitter',
        self._addressOf(e),
    )

  @overload(QQuick3DParticleEmitter)
  @overload(NoneType)
  def unRegisterParticleEmitter(
      self,
      e: Optional[QQuick3DParticleEmitter],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSystem::unRegisterParticleEmitter(QQuick3DParticleEmitter
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html

    Parameters
    ----------

    e : Optional[QQuick3DParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSystem::unRegisterParticleEmitter(
    #      QQuick3DParticleEmitter *e)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem25unRegisterParticleEmitterEP23QQ'
        'uick3DParticleEmitter',
        self._addressOf(e),
    )

  @overload(QQuick3DParticleAffector)
  @overload(NoneType)
  def registerParticleAffector(
      self,
      a: Optional[QQuick3DParticleAffector],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleSystem::registerParticleAffector(QQuick3DParticleAffector
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html

    Parameters
    ----------

    a : Optional[QQuick3DParticleAffector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSystem::registerParticleAffector(
    #      QQuick3DParticleAffector *a)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem24registerParticleAffectorEP24QQu'
        'ick3DParticleAffector',
        self._addressOf(a),
    )

  @overload(QQuick3DParticleAffector)
  @overload(NoneType)
  def unRegisterParticleAffector(
      self,
      a: Optional[QQuick3DParticleAffector],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::unRegisterParticleAffector(
    QQuick3DParticleAffector *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html

    Parameters
    ----------

    a : Optional[QQuick3DParticleAffector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleSystem::unRegisterParticleAffector(
    #      QQuick3DParticleAffector *a)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem26unRegisterParticleAffectorEP24Q'
        'Quick3DParticleAffector',
        self._addressOf(a),
    )

  @overload(int)
  def updateCurrentTime(self, currentTime: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::updateCurrentTime(int
    currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#updateCurrentTime

    Parameters
    ----------

    currentTime : int
      Passed on as it is.
    """
    #  void QQuick3DParticleSystem::updateCurrentTime(int currentTime)
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem17updateCurrentTimeEi',
        currentTime,
    )

  def rand(self) -> Optional[QPRand]:
    """
    Calls Qt's 'QPRand *QQuick3DParticleSystem::rand()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlesystem.html#rand

    Returns
    -------

    Optional[QPRand]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPRand *QQuick3DParticleSystem::rand()
    address = self.uglySide.call('ritual_ZN22QQuick3DParticleSystem4randEv')
    from . import QPRand
    return QPRand._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticlesystem.html#reset
    """
    #  void QQuick3DParticleSystem::reset()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem5resetEv')

  def runningChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::runningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#runningChanged
    """
    #  void QQuick3DParticleSystem::runningChanged()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem14runningChangedEv')

  def pausedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::pausedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#pausedChanged
    """
    #  void QQuick3DParticleSystem::pausedChanged()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem13pausedChangedEv')

  def timeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::timeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#timeChanged
    """
    #  void QQuick3DParticleSystem::timeChanged()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem11timeChangedEv')

  def startTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::startTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#startTimeChanged
    """
    #  void QQuick3DParticleSystem::startTimeChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem16startTimeChangedEv',
    )

  def useRandomSeedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::useRandomSeedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#useRandomSeedChanged
    """
    #  void QQuick3DParticleSystem::useRandomSeedChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem20useRandomSeedChangedEv',
    )

  def seedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::seedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#seedChanged
    """
    #  void QQuick3DParticleSystem::seedChanged()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem11seedChangedEv')

  def loggingChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::loggingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#loggingChanged
    """
    #  void QQuick3DParticleSystem::loggingChanged()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem14loggingChangedEv')

  def loggingDataChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::loggingDataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#loggingDataChanged
    """
    #  void QQuick3DParticleSystem::loggingDataChanged()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem18loggingDataChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#componentComplete
    """
    #  void QQuick3DParticleSystem::componentComplete()
    ritual = 'ritual_ZN22QQuick3DParticleSystem17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuick3DParticleSystem17componentCompleteEv'
    self.uglySide.call(ritual)

  def updateLoggingData(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::updateLoggingData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#updateLoggingData
    """
    #  void QQuick3DParticleSystem::updateLoggingData()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem17updateLoggingDataEv',
    )

  def resetLoggingVariables(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::resetLoggingVariables()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#resetLoggingVariables
    """
    #  void QQuick3DParticleSystem::resetLoggingVariables()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem21resetLoggingVariablesEv',
    )

  def doSeedRandomization(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::doSeedRandomization()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#doSeedRandomization
    """
    #  void QQuick3DParticleSystem::doSeedRandomization()
    self.uglySide.call(
        'ritual_ZN22QQuick3DParticleSystem19doSeedRandomizationEv',
    )

  def refresh(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::refresh()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#refresh
    """
    #  void QQuick3DParticleSystem::refresh()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem7refreshEv')

  def markDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleSystem::markDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticlesystem.html#markDirty
    """
    #  void QQuick3DParticleSystem::markDirty()
    self.uglySide.call('ritual_ZN22QQuick3DParticleSystem9markDirtyEv')

  @staticmethod
  def processModelBlendParticle(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSystem::processModelBlendParticle(
    QQuick3DParticleModelBlendParticle *particle, const QVector<TrailEmits>
    &trailEmits, float timeS)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSystem.processModelBlendParticle' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSystem::processModelBlendParticle(QQuick3DParticleM"
        "odelBlendParticle *particle, const QVector<TrailEmits> "
        "&trailEmits, float timeS)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def processModelParticle(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSystem::processModelParticle(
    QQuick3DParticleModelParticle *modelParticle, const QVector<TrailEmits>
    &trailEmits, float timeS)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSystem.processModelParticle' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DParticleSystem::processModelParticle(QQuick3DParticleModelP"
        "article *modelParticle, const QVector<TrailEmits> &trailEmits, "
        "float timeS)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def processParticleAlignment(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSystem::processParticleAlignment(
    QQuick3DParticleDataCurrent &currentData, const QQuick3DParticle
    *particle, const QQuick3DParticleData *d)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSystem.processParticleAlignment' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSystem::processParticleAlignment(QQuick3DParticleDa"
        "taCurrent &currentData, const QQuick3DParticle *particle, const "
        "QQuick3DParticleData *d)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def processParticleCommon(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DParticleSystem::processParticleCommon(QQuick3DParticleDataCurrent
    &currentData, const QQuick3DParticleData *d, float particleTimeS)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSystem.processParticleCommon' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSystem::processParticleCommon(QQuick3DParticleDataC"
        "urrent &currentData, const QQuick3DParticleData *d, float "
        "particleTimeS)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def processParticleFadeInOut(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSystem::processParticleFadeInOut(
    QQuick3DParticleDataCurrent &currentData, const QQuick3DParticle
    *particle, float particleTimeS, float particleTimeLeftS)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSystem.processParticleFadeInOut' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSystem::processParticleFadeInOut(QQuick3DParticleDa"
        "taCurrent &currentData, const QQuick3DParticle *particle, float "
        "particleTimeS, float particleTimeLeftS)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def processSpriteParticle(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DParticleSystem::processSpriteParticle(
    QQuick3DParticleSpriteParticle *spriteParticle, const QVector<TrailEmits>
    &trailEmits, float timeS)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleSystem.processSpriteParticle' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DParticleSystem::processSpriteParticle(QQuick3DParticleSprit"
        "eParticle *spriteParticle, const QVector<TrailEmits> &trailEmits, "
        "float timeS)': takes a type Python has no way to hand over yet.")
