"""
QQuickParticleSystem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleSystem to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleAffector, QQuickParticleData
  from . import QQuickParticleEmitter, QQuickParticleGroup
  from . import QQuickParticleGroupData, QQuickParticlePainter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleAffector = WAIT['QQuickParticleAffector']
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickParticleEmitter = WAIT['QQuickParticleEmitter']
  QQuickParticleGroup = WAIT['QQuickParticleGroup']
  QQuickParticleGroupData = WAIT['QQuickParticleGroupData']
  QQuickParticlePainter = WAIT['QQuickParticlePainter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleSystem(QQuickItem):
  """
  The cute side of Qt's QQuickParticleSystem: a plain Python object standing
  in front of one C++ QQuickParticleSystem.

  It is built on the cute 'QQuickItem', as Qt's QQuickParticleSystem is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParticleSystem that has a ritual and that
  Python can call so far, 45 names in all: 'metaObject', 'tr', 'isRunning',
  'count', 'systemInitialized', 'runningChanged', 'pausedChanged',
  'emptyChanged', 'start', 'stop', 'restart', 'pause', 'resume', 'reset',
  'setRunning', 'setPaused', 'duration', 'componentComplete',
  'emittersChanged', 'loadPainter', 'createEngine', 'particleStateChange',
  'emitParticle', 'newDatum', 'finishNewDatum', 'moveGroups',
  'nextSystemIndex', 'systemSync', 'registerParticleGroupData',
  'updateCurrentTime', 'registerParticlePainter', 'registerParticleEmitter',
  'finishRegisteringParticleEmitter', 'registerParticleAffector',
  'registerParticleGroup', 'unregisterParticlePainter',
  'unregisterParticleEmitter', 'unregisterParticleAffector', 'stateRedirect',
  'isPaused', 'isEmpty', 'searchNextFreeGroupId', 'emitterAdded',
  'postProcessEmitters', 'initGroups'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParticleSystem::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickParticleSystem::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickParticleSystem::~QQuickParticleSystem()': the destructor:
    Python never removes a C++ QQuickParticleSystem.
  - Qt's 'void
    QQuickParticleSystem::statePropertyRedirect(QQmlListProperty<QObject>
    *prop, QObject *value)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.

  What has no ritual
  ------------------

  3 of the 53 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickParticleSystem is created at the first use, not by
    'QQuickParticleSystem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParticleSystem.
  - Qt tells when it has removed the C++ QQuickParticleSystem. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickParticleSystem that has no cute function yet,
    'statePropertyRedirect', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickParticleSystem::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#tr

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
    #  QString QQuickParticleSystem::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickParticleSystem2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQuickParticleGroup, THIS, QObject)
  @overload(QQuickParticleGroup, THIS, NoneType)
  @overload(QQuickParticleGroup, NoneType, QObject)
  @overload(QQuickParticleGroup, NoneType, NoneType)
  @overload(NoneType, THIS, QObject)
  @overload(NoneType, THIS, NoneType)
  @overload(NoneType, NoneType, QObject)
  @overload(NoneType, NoneType, NoneType)
  def stateRedirect(
      group: Optional[QQuickParticleGroup],
      sys: Optional[QQuickParticleSystem],
      value: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::stateRedirect(QQuickParticleGroup
    *group, QQuickParticleSystem *sys, QObject *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#stateRedirect

    Parameters
    ----------

    group : Optional[QQuickParticleGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sys : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::stateRedirect(QQuickParticleGroup *group,
    #      QQuickParticleSystem *sys, QObject *value)
    Rituals.call(
        'ritual_ZN20QQuickParticleSystem13stateRedirectEP19QQuickParticleGr'
        'oupPS_P7QObject',
        CuteMixin._addressOf(group), CuteMixin._addressOf(sys),
        CuteMixin._addressOf(value, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleSystem'

  #  A C++ QQuickParticleSystem Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickParticleSystem'

  #  The functions Qt calls itself that QQuickParticleSystem is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'duration': (
          ('_ZNK20QQuickParticleSystem8durationEv',
           ('int', 'number', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickParticleSystem::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParticleSystem::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickParticleSystem10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleSystem::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#isRunning
    """
    #  bool QQuickParticleSystem::isRunning() const
    return self.uglySide.call('ritual_ZNK20QQuickParticleSystem9isRunningEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickParticleSystem::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#count
    """
    #  int QQuickParticleSystem::count() const
    return self.uglySide.call('ritual_ZNK20QQuickParticleSystem5countEv')

  def duration(self) -> int:
    """
    Calls Qt's 'int QQuickParticleSystem::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#duration
    """
    #  int QQuickParticleSystem::duration() const
    ritual = 'ritual_ZNK20QQuickParticleSystem8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QQuickParticleSystem8durationEv'
    return self.uglySide.call(ritual)

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleSystem::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#isPaused
    """
    #  bool QQuickParticleSystem::isPaused() const
    return self.uglySide.call('ritual_ZNK20QQuickParticleSystem8isPausedEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleSystem::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#isEmpty
    """
    #  bool QQuickParticleSystem::isEmpty() const
    return self.uglySide.call('ritual_ZNK20QQuickParticleSystem7isEmptyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::setRunning(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#setRunning

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleSystem::setRunning(bool arg)
    self.uglySide.call('ritual_ZN20QQuickParticleSystem10setRunningEb', arg)

  @overload(bool)
  def setPaused(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::setPaused(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#setPaused

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleSystem::setPaused(bool arg)
    self.uglySide.call('ritual_ZN20QQuickParticleSystem9setPausedEb', arg)

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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickParticleSystem::QQuickParticleSystem(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#QQuickParticleSystem

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickParticleSystem::QQuickParticleSystem(QQuickItem *parent)
    self._noteCreation(QQuickParticleSystem, lambda: Rituals.call(
        'ritual_ZN20QQuickParticleSystemC1EP10QQuickItem',
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

  def systemInitialized(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::systemInitialized()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#systemInitialized
    """
    #  void QQuickParticleSystem::systemInitialized()
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem17systemInitializedEv',
    )

  @overload(bool)
  def runningChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::runningChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#runningChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleSystem::runningChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem14runningChangedEb', arg,
    )

  @overload(bool)
  def pausedChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::pausedChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#pausedChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleSystem::pausedChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem13pausedChangedEb', arg,
    )

  @overload(bool)
  def emptyChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::emptyChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#emptyChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleSystem::emptyChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem12emptyChangedEb', arg,
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#start
    """
    #  void QQuickParticleSystem::start()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#stop
    """
    #  void QQuickParticleSystem::stop()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem4stopEv')

  def restart(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#restart
    """
    #  void QQuickParticleSystem::restart()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem7restartEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#pause
    """
    #  void QQuickParticleSystem::pause()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#resume
    """
    #  void QQuickParticleSystem::resume()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem6resumeEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#reset
    """
    #  void QQuickParticleSystem::reset()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem5resetEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#componentComplete
    """
    #  void QQuickParticleSystem::componentComplete()
    ritual = 'ritual_ZN20QQuickParticleSystem17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickParticleSystem17componentCompleteEv'
    self.uglySide.call(ritual)

  def emittersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::emittersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#emittersChanged
    """
    #  void QQuickParticleSystem::emittersChanged()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem15emittersChangedEv')

  @overload(QQuickParticlePainter)
  @overload(NoneType)
  def loadPainter(self, p: Optional[QQuickParticlePainter]) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::loadPainter(QQuickParticlePainter
    *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#loadPainter

    Parameters
    ----------

    p : Optional[QQuickParticlePainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::loadPainter(QQuickParticlePainter *p)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem11loadPainterEP21QQuickParticlePain'
        'ter',
        self._addressOf(p),
    )

  def createEngine(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::createEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#createEngine
    """
    #  void QQuickParticleSystem::createEngine()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem12createEngineEv')

  @overload(int)
  def particleStateChange(self, idx: int) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::particleStateChange(int idx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#particleStateChange

    Parameters
    ----------

    idx : int
      Passed on as it is.
    """
    #  void QQuickParticleSystem::particleStateChange(int idx)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem19particleStateChangeEi', idx,
    )

  @overload(QQuickParticleData, QQuickParticleEmitter)
  @overload(QQuickParticleData, NoneType)
  @overload(NoneType, QQuickParticleEmitter)
  @overload(NoneType, NoneType)
  def emitParticle(
      self,
      p: Optional[QQuickParticleData],
      particleEmitter: Optional[QQuickParticleEmitter],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::emitParticle(QQuickParticleData
    *p, QQuickParticleEmitter *particleEmitter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#emitParticle

    Parameters
    ----------

    p : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    particleEmitter : Optional[QQuickParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::emitParticle(QQuickParticleData *p,
    #      QQuickParticleEmitter *particleEmitter)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem12emitParticleEP18QQuickParticleDat'
        'aP21QQuickParticleEmitter',
        self._addressOf(p), self._addressOf(particleEmitter),
    )

  @overload(int)
  @overload(int, bool)
  @overload(int, bool, int)
  @overload(int, bool, int, QQuickParticleData)
  @overload(int, bool, int, NoneType)
  def newDatum(
      self,
      groupId: int,
      respectLimits: bool = True,
      sysIdx: int = -1,
      cloneFrom: Optional[QQuickParticleData] = None,
  ) -> Optional[QQuickParticleData]:
    """
    Calls Qt's 'QQuickParticleData *QQuickParticleSystem::newDatum(int
    groupId, bool respectLimits, int sysIdx, const QQuickParticleData
    *cloneFrom)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticlesystem.html#newDatum

    Parameters
    ----------

    groupId : int
      Passed on as it is.

    respectLimits : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    sysIdx : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    cloneFrom : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QQuickParticleData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleData *QQuickParticleSystem::newDatum(int groupId, bool
    #      respectLimits, int sysIdx, const QQuickParticleData *cloneFrom)
    address = self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem8newDatumEibiPK18QQuickParticleData',
        groupId, respectLimits, sysIdx, self._addressOf(cloneFrom),
    )
    from . import QQuickParticleData
    return QQuickParticleData._cuteAt(address)

  @overload(QQuickParticleData)
  @overload(NoneType)
  def finishNewDatum(self, a0: Optional[QQuickParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::finishNewDatum(QQuickParticleData
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#finishNewDatum

    Parameters
    ----------

    a0 : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::finishNewDatum(QQuickParticleData *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem14finishNewDatumEP18QQuickParticleD'
        'ata',
        self._addressOf(a0),
    )

  @overload(QQuickParticleData, int)
  @overload(NoneType, int)
  def moveGroups(
      self,
      d: Optional[QQuickParticleData],
      newGIdx: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::moveGroups(QQuickParticleData *d,
    int newGIdx)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#moveGroups

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newGIdx : int
      Passed on as it is.
    """
    #  void QQuickParticleSystem::moveGroups(QQuickParticleData *d, int
    #      newGIdx)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem10moveGroupsEP18QQuickParticleDatai',
        self._addressOf(d), newGIdx,
    )

  def nextSystemIndex(self) -> int:
    """
    Calls Qt's 'int QQuickParticleSystem::nextSystemIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#nextSystemIndex
    """
    #  int QQuickParticleSystem::nextSystemIndex()
    return self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem15nextSystemIndexEv',
    )

  @overload(QQuickParticlePainter)
  @overload(NoneType)
  def systemSync(self, p: Optional[QQuickParticlePainter]) -> int:
    """
    Calls Qt's 'int QQuickParticleSystem::systemSync(QQuickParticlePainter
    *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#systemSync

    Parameters
    ----------

    p : Optional[QQuickParticlePainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickParticleSystem::systemSync(QQuickParticlePainter *p)
    return self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem10systemSyncEP21QQuickParticlePaint'
        'er',
        self._addressOf(p),
    )

  @overload(str, QQuickParticleGroupData)
  @overload(str, NoneType)
  def registerParticleGroupData(
      self,
      name: str,
      pgd: Optional[QQuickParticleGroupData],
  ) -> int:
    """
    Calls Qt's 'int QQuickParticleSystem::registerParticleGroupData(const
    QString &name, QQuickParticleGroupData *pgd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    pgd : Optional[QQuickParticleGroupData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickParticleSystem::registerParticleGroupData(const QString
    #      &name, QQuickParticleGroupData *pgd)
    return self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem25registerParticleGroupDataERK7QStr'
        'ingP23QQuickParticleGroupData',
        name, self._addressOf(pgd),
    )

  @overload(int)
  def updateCurrentTime(self, currentTime: int) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::updateCurrentTime(int
    currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#updateCurrentTime

    Parameters
    ----------

    currentTime : int
      Passed on as it is.
    """
    #  void QQuickParticleSystem::updateCurrentTime(int currentTime)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem17updateCurrentTimeEi', currentTime,
    )

  @overload(QQuickParticlePainter)
  @overload(NoneType)
  def registerParticlePainter(
      self,
      p: Optional[QQuickParticlePainter],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::registerParticlePainter(QQuickParticlePainter *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#registerParticlePainter

    Parameters
    ----------

    p : Optional[QQuickParticlePainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::registerParticlePainter(
    #      QQuickParticlePainter *p)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem23registerParticlePainterEP21QQuick'
        'ParticlePainter',
        self._addressOf(p),
    )

  @overload(QQuickParticleEmitter)
  @overload(NoneType)
  def registerParticleEmitter(
      self,
      e: Optional[QQuickParticleEmitter],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::registerParticleEmitter(QQuickParticleEmitter *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#registerParticleEmitter

    Parameters
    ----------

    e : Optional[QQuickParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::registerParticleEmitter(
    #      QQuickParticleEmitter *e)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem23registerParticleEmitterEP21QQuick'
        'ParticleEmitter',
        self._addressOf(e),
    )

  @overload(QQuickParticleEmitter)
  @overload(NoneType)
  def finishRegisteringParticleEmitter(
      self,
      e: Optional[QQuickParticleEmitter],
  ) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::finishRegisteringParticleEmitter(
    QQuickParticleEmitter *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html

    Parameters
    ----------

    e : Optional[QQuickParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::finishRegisteringParticleEmitter(
    #      QQuickParticleEmitter *e)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem32finishRegisteringParticleEmitterE'
        'P21QQuickParticleEmitter',
        self._addressOf(e),
    )

  @overload(QQuickParticleAffector)
  @overload(NoneType)
  def registerParticleAffector(
      self,
      a: Optional[QQuickParticleAffector],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::registerParticleAffector(QQuickParticleAffector
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#registerParticleAffector

    Parameters
    ----------

    a : Optional[QQuickParticleAffector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::registerParticleAffector(
    #      QQuickParticleAffector *a)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem24registerParticleAffectorEP22QQuic'
        'kParticleAffector',
        self._addressOf(a),
    )

  @overload(QQuickParticleGroup)
  @overload(NoneType)
  def registerParticleGroup(self, g: Optional[QQuickParticleGroup]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::registerParticleGroup(QQuickParticleGroup *g)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#registerParticleGroup

    Parameters
    ----------

    g : Optional[QQuickParticleGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::registerParticleGroup(QQuickParticleGroup
    #      *g)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem21registerParticleGroupEP19QQuickPa'
        'rticleGroup',
        self._addressOf(g),
    )

  @overload(QQuickParticlePainter)
  @overload(NoneType)
  def unregisterParticlePainter(
      self,
      p: Optional[QQuickParticlePainter],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::unregisterParticlePainter(QQuickParticlePainter
    *p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html

    Parameters
    ----------

    p : Optional[QQuickParticlePainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::unregisterParticlePainter(
    #      QQuickParticlePainter *p)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem25unregisterParticlePainterEP21QQui'
        'ckParticlePainter',
        self._addressOf(p),
    )

  @overload(QQuickParticleEmitter)
  @overload(NoneType)
  def unregisterParticleEmitter(
      self,
      e: Optional[QQuickParticleEmitter],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::unregisterParticleEmitter(QQuickParticleEmitter
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html

    Parameters
    ----------

    e : Optional[QQuickParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::unregisterParticleEmitter(
    #      QQuickParticleEmitter *e)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem25unregisterParticleEmitterEP21QQui'
        'ckParticleEmitter',
        self._addressOf(e),
    )

  @overload(QQuickParticleAffector)
  @overload(NoneType)
  def unregisterParticleAffector(
      self,
      a: Optional[QQuickParticleAffector],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickParticleSystem::unregisterParticleAffector(QQuickParticleAffector
    *a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html

    Parameters
    ----------

    a : Optional[QQuickParticleAffector]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::unregisterParticleAffector(
    #      QQuickParticleAffector *a)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem26unregisterParticleAffectorEP22QQu'
        'ickParticleAffector',
        self._addressOf(a),
    )

  def searchNextFreeGroupId(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::searchNextFreeGroupId()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#searchNextFreeGroupId
    """
    #  void QQuickParticleSystem::searchNextFreeGroupId()
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem21searchNextFreeGroupIdEv',
    )

  @overload(QQuickParticleEmitter)
  @overload(NoneType)
  def emitterAdded(self, e: Optional[QQuickParticleEmitter]) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::emitterAdded(QQuickParticleEmitter
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#emitterAdded

    Parameters
    ----------

    e : Optional[QQuickParticleEmitter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleSystem::emitterAdded(QQuickParticleEmitter *e)
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem12emitterAddedEP21QQuickParticleEmi'
        'tter',
        self._addressOf(e),
    )

  def postProcessEmitters(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::postProcessEmitters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#postProcessEmitters
    """
    #  void QQuickParticleSystem::postProcessEmitters()
    self.uglySide.call(
        'ritual_ZN20QQuickParticleSystem19postProcessEmittersEv',
    )

  def initGroups(self) -> None:
    """
    Calls Qt's 'void QQuickParticleSystem::initGroups()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticlesystem.html#initGroups
    """
    #  void QQuickParticleSystem::initGroups()
    self.uglySide.call('ritual_ZN20QQuickParticleSystem10initGroupsEv')

  @staticmethod
  def statePropertyRedirect(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickParticleSystem::statePropertyRedirect(QQmlListProperty<QObject>
    *prop, QObject *value)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickParticleSystem.statePropertyRedirect' has no cute function "
        "yet. Qt's 'void "
        "QQuickParticleSystem::statePropertyRedirect(QQmlListProperty<QObjec"
        "t> *prop, QObject *value)': names 'QQmlListProperty<QObject>', "
        "which has no cute class yet.")
