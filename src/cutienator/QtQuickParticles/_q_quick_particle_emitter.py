"""
QQuickParticleEmitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticleemitter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickParticleEmitter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickDirection, QQuickParticleExtruder, QQuickParticleSystem
  from . import QQuickV4ParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickDirection = WAIT['QQuickDirection']
  QQuickParticleExtruder = WAIT['QQuickParticleExtruder']
  QQuickParticleSystem = WAIT['QQuickParticleSystem']
  QQuickV4ParticleData = WAIT['QQuickV4ParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParticleEmitter(QQuickItem):
  """
  The cute side of Qt's QQuickParticleEmitter: a plain Python object standing
  in front of one C++ QQuickParticleEmitter.

  It is built on the cute 'QQuickItem', as Qt's QQuickParticleEmitter is
  built on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParticleEmitter that has a ritual and that
  Python can call so far, 60 names in all: 'metaObject', 'tr', 'emitWindow',
  'enabled', 'particlesPerSecond', 'particleDuration', 'system', 'group',
  'groupId', 'particleDurationVariation', 'velocityFromMovement',
  'setVelocityFromMovement', 'componentComplete', 'emitParticles',
  'particlesPerSecondChanged', 'particleDurationChanged', 'enabledChanged',
  'systemChanged', 'groupChanged', 'particleDurationVariationChanged',
  'extruderChanged', 'particleSizeChanged', 'particleEndSizeChanged',
  'particleSizeVariationChanged', 'velocityChanged', 'accelerationChanged',
  'maximumEmittedChanged', 'particleCountChanged',
  'velocityFromMovementChanged', 'startTimeChanged', 'pulse', 'burst',
  'setEnabled', 'setParticlesPerSecond', 'setParticleDuration', 'setSystem',
  'setGroup', 'setParticleDurationVariation', 'setExtruder',
  'setParticleSize', 'setParticleEndSize', 'setParticleSizeVariation',
  'setVelocity', 'setAcceleration', 'setMaxParticleCount', 'setStartTime',
  'reset', 'particleCount', 'extruder', 'particleSize', 'particleEndSize',
  'particleSizeVariation', 'velocity', 'acceleration', 'maxParticleCount',
  'startTime', 'reclaculateGroupId', 'effectiveExtruder', 'isEmitConnected',
  'callSystemEmittersChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParticleEmitter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickParticleEmitter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickParticleEmitter::~QQuickParticleEmitter()': the destructor:
    Python never removes a C++ QQuickParticleEmitter.

  What has no ritual
  ------------------

  2 of the 67 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickParticleEmitter is created at the first use, not by
    'QQuickParticleEmitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParticleEmitter.
  - Qt tells when it has removed the C++ QQuickParticleEmitter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickParticleEmitter, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Lifetime(CuteNum):
    """
    The enum 'QQuickParticleEmitter::Lifetime' of Qt, with the 1 names Qt
    gives in it.
    """

    InfiniteLife = Kee[int](600000)

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
    Calls Qt's 'QString QQuickParticleEmitter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#tr

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
    #  QString QQuickParticleEmitter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickParticleEmitter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParticleEmitter'

  #  A C++ QQuickParticleEmitter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickParticleEmitter'

  #  The functions Qt calls itself that QQuickParticleEmitter is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'emitWindow': (
          ('_ZN21QQuickParticleEmitter10emitWindowEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'reset': (
          ('_ZN21QQuickParticleEmitter5resetEv',
           ('nothing', 'nothing', ''),
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
    Calls Qt's 'const QMetaObject *QQuickParticleEmitter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParticleEmitter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleEmitter::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#enabled
    """
    #  bool QQuickParticleEmitter::enabled() const
    return self.uglySide.call('ritual_ZNK21QQuickParticleEmitter7enabledEv')

  def particlesPerSecond(self) -> float:
    """
    Calls Qt's 'qreal QQuickParticleEmitter::particlesPerSecond() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particlesPerSecond
    """
    #  qreal QQuickParticleEmitter::particlesPerSecond() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter18particlesPerSecondEv',
    )

  def particleDuration(self) -> int:
    """
    Calls Qt's 'int QQuickParticleEmitter::particleDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleDuration
    """
    #  int QQuickParticleEmitter::particleDuration() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter16particleDurationEv',
    )

  def system(self) -> Optional[QQuickParticleSystem]:
    """
    Calls Qt's 'QQuickParticleSystem *QQuickParticleEmitter::system() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#system

    Returns
    -------

    Optional[QQuickParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleSystem *QQuickParticleEmitter::system() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter6systemEv',
    )
    from . import QQuickParticleSystem
    return QQuickParticleSystem._cuteAt(address)

  def group(self) -> str:
    """
    Calls Qt's 'QString QQuickParticleEmitter::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#group

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickParticleEmitter::group() const
    return self.uglySide.call('ritual_ZNK21QQuickParticleEmitter5groupEv')

  def groupId(self) -> int:
    """
    Calls Qt's 'QQuickParticleGroupData::ID QQuickParticleEmitter::groupId()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#groupId
    """
    #  QQuickParticleGroupData::ID QQuickParticleEmitter::groupId() const
    return self.uglySide.call('ritual_ZNK21QQuickParticleEmitter7groupIdEv')

  def particleDurationVariation(self) -> int:
    """
    Calls Qt's 'int QQuickParticleEmitter::particleDurationVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html
    """
    #  int QQuickParticleEmitter::particleDurationVariation() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter25particleDurationVariationEv',
    )

  def velocityFromMovement(self) -> float:
    """
    Calls Qt's 'qreal QQuickParticleEmitter::velocityFromMovement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#velocityFromMovement
    """
    #  qreal QQuickParticleEmitter::velocityFromMovement() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter20velocityFromMovementEv',
    )

  def particleCount(self) -> int:
    """
    Calls Qt's 'int QQuickParticleEmitter::particleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleCount
    """
    #  int QQuickParticleEmitter::particleCount() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter13particleCountEv',
    )

  def extruder(self) -> Optional[QQuickParticleExtruder]:
    """
    Calls Qt's 'QQuickParticleExtruder *QQuickParticleEmitter::extruder()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#extruder

    Returns
    -------

    Optional[QQuickParticleExtruder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleExtruder *QQuickParticleEmitter::extruder() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter8extruderEv',
    )
    from . import QQuickParticleExtruder
    return QQuickParticleExtruder._cuteAt(address)

  def particleSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickParticleEmitter::particleSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleSize
    """
    #  qreal QQuickParticleEmitter::particleSize() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter12particleSizeEv',
    )

  def particleEndSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickParticleEmitter::particleEndSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleEndSize
    """
    #  qreal QQuickParticleEmitter::particleEndSize() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter15particleEndSizeEv',
    )

  def particleSizeVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickParticleEmitter::particleSizeVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleSizeVariation
    """
    #  qreal QQuickParticleEmitter::particleSizeVariation() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter21particleSizeVariationEv',
    )

  def velocity(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickParticleEmitter::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#velocity

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickParticleEmitter::velocity() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter8velocityEv',
    )
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def acceleration(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickParticleEmitter::acceleration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#acceleration

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickParticleEmitter::acceleration() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter12accelerationEv',
    )
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def maxParticleCount(self) -> int:
    """
    Calls Qt's 'int QQuickParticleEmitter::maxParticleCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#maxParticleCount
    """
    #  int QQuickParticleEmitter::maxParticleCount() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter16maxParticleCountEv',
    )

  def startTime(self) -> int:
    """
    Calls Qt's 'int QQuickParticleEmitter::startTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#startTime
    """
    #  int QQuickParticleEmitter::startTime() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter9startTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setVelocityFromMovement(self, s: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setVelocityFromMovement(qreal
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setVelocityFromMovement

    Parameters
    ----------

    s : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setVelocityFromMovement(qreal s)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter23setVelocityFromMovementEd', s,
    )

  @overload(bool)
  def setEnabled(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setEnabled(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setEnabled

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setEnabled(bool arg)
    self.uglySide.call('ritual_ZN21QQuickParticleEmitter10setEnabledEb', arg)

  @overload(float)
  def setParticlesPerSecond(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setParticlesPerSecond(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setParticlesPerSecond

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setParticlesPerSecond(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter21setParticlesPerSecondEd', arg,
    )

  @overload(int)
  def setParticleDuration(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setParticleDuration(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setParticleDuration

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setParticleDuration(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter19setParticleDurationEi', arg,
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def setSystem(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setSystem(QQuickParticleSystem
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setSystem

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::setSystem(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter9setSystemEP20QQuickParticleSystem',
        self._addressOf(arg),
    )

  @overload(str)
  def setGroup(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setGroup(const QString &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setGroup

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickParticleEmitter::setGroup(const QString &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter8setGroupERK7QString', arg,
    )

  @overload(int)
  def setParticleDurationVariation(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setParticleDurationVariation(int
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setParticleDurationVariation(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter28setParticleDurationVariationEi',
        arg,
    )

  @overload(QQuickParticleExtruder)
  @overload(NoneType)
  def setExtruder(self, arg: Optional[QQuickParticleExtruder]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleEmitter::setExtruder(QQuickParticleExtruder *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setExtruder

    Parameters
    ----------

    arg : Optional[QQuickParticleExtruder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::setExtruder(QQuickParticleExtruder *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter11setExtruderEP22QQuickParticleExt'
        'ruder',
        self._addressOf(arg),
    )

  @overload(float)
  def setParticleSize(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setParticleSize(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setParticleSize

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setParticleSize(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter15setParticleSizeEd', arg,
    )

  @overload(float)
  def setParticleEndSize(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setParticleEndSize(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setParticleEndSize

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setParticleEndSize(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter18setParticleEndSizeEd', arg,
    )

  @overload(float)
  def setParticleSizeVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setParticleSizeVariation(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setParticleSizeVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter24setParticleSizeVariationEd', arg,
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def setVelocity(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setVelocity(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setVelocity

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::setVelocity(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter11setVelocityEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def setAcceleration(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setAcceleration(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setAcceleration

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::setAcceleration(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter15setAccelerationEP15QQuickDirecti'
        'on',
        self._addressOf(arg),
    )

  @overload(int)
  def setMaxParticleCount(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setMaxParticleCount(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setMaxParticleCount

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setMaxParticleCount(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter19setMaxParticleCountEi', arg,
    )

  @overload(int)
  def setStartTime(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::setStartTime(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#setStartTime

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::setStartTime(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter12setStartTimeEi', arg,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickParticleEmitter::QQuickParticleEmitter(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#QQuickParticleEmitter

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickParticleEmitter::QQuickParticleEmitter(QQuickItem *parent)
    self._noteCreation(QQuickParticleEmitter, lambda: Rituals.call(
        'ritual_ZN21QQuickParticleEmitterC1EP10QQuickItem',
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

  @overload(int)
  def emitWindow(self, timeStamp: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::emitWindow(int timeStamp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#emitWindow

    Parameters
    ----------

    timeStamp : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::emitWindow(int timeStamp)
    ritual = 'ritual_ZN21QQuickParticleEmitter10emitWindowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticleEmitter10emitWindowEi'
    self.uglySide.call(ritual, timeStamp)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#componentComplete
    """
    #  void QQuickParticleEmitter::componentComplete()
    ritual = 'ritual_ZN21QQuickParticleEmitter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticleEmitter17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QList[QQuickV4ParticleData])
  def emitParticles(self, particles: QList[QQuickV4ParticleData]) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::emitParticles(const
    QList<QQuickV4ParticleData> &particles)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#emitParticles

    Parameters
    ----------

    particles : QList[QQuickV4ParticleData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickParticleEmitter::emitParticles(const
    #      QList<QQuickV4ParticleData> &particles)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter13emitParticlesERK5QListI20QQuickV'
        '4ParticleDataE',
        self._valueOf(particles),
    )

  @overload(float)
  def particlesPerSecondChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::particlesPerSecondChanged(qreal
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::particlesPerSecondChanged(qreal a0)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter25particlesPerSecondChangedEd', a0,
    )

  @overload(int)
  def particleDurationChanged(self, a0: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::particleDurationChanged(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleDurationChanged

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::particleDurationChanged(int a0)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter23particleDurationChangedEi', a0,
    )

  @overload(bool)
  def enabledChanged(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::enabledChanged(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#enabledChanged

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::enabledChanged(bool a0)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter14enabledChangedEb', a0,
    )

  @overload(QQuickParticleSystem)
  @overload(NoneType)
  def systemChanged(self, arg: Optional[QQuickParticleSystem]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleEmitter::systemChanged(QQuickParticleSystem *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#systemChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::systemChanged(QQuickParticleSystem *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter13systemChangedEP20QQuickParticleS'
        'ystem',
        self._addressOf(arg),
    )

  @overload(str)
  def groupChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::groupChanged(const QString
    &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#groupChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickParticleEmitter::groupChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter12groupChangedERK7QString', arg,
    )

  @overload(int)
  def particleDurationVariationChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void
    QQuickParticleEmitter::particleDurationVariationChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::particleDurationVariationChanged(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter32particleDurationVariationChanged'
        'Ei',
        arg,
    )

  @overload(QQuickParticleExtruder)
  @overload(NoneType)
  def extruderChanged(self, arg: Optional[QQuickParticleExtruder]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleEmitter::extruderChanged(QQuickParticleExtruder *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#extruderChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleExtruder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::extruderChanged(QQuickParticleExtruder
    #      *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter15extruderChangedEP22QQuickParticl'
        'eExtruder',
        self._addressOf(arg),
    )

  @overload(float)
  def particleSizeChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::particleSizeChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleSizeChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::particleSizeChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter19particleSizeChangedEd', arg,
    )

  @overload(float)
  def particleEndSizeChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::particleEndSizeChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleEndSizeChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::particleEndSizeChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter22particleEndSizeChangedEd', arg,
    )

  @overload(float)
  def particleSizeVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void
    QQuickParticleEmitter::particleSizeVariationChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::particleSizeVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter28particleSizeVariationChangedEd',
        arg,
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def velocityChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::velocityChanged(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#velocityChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::velocityChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter15velocityChangedEP15QQuickDirecti'
        'on',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def accelerationChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void
    QQuickParticleEmitter::accelerationChanged(QQuickDirection *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#accelerationChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParticleEmitter::accelerationChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter19accelerationChangedEP15QQuickDir'
        'ection',
        self._addressOf(arg),
    )

  @overload(int)
  def maximumEmittedChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::maximumEmittedChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#maximumEmittedChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::maximumEmittedChanged(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter21maximumEmittedChangedEi', arg,
    )

  def particleCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::particleCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#particleCountChanged
    """
    #  void QQuickParticleEmitter::particleCountChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter20particleCountChangedEv',
    )

  def velocityFromMovementChanged(self) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::velocityFromMovementChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html
    """
    #  void QQuickParticleEmitter::velocityFromMovementChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter27velocityFromMovementChangedEv',
    )

  @overload(int)
  def startTimeChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::startTimeChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#startTimeChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::startTimeChanged(int arg)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter16startTimeChangedEi', arg,
    )

  @overload(int)
  def pulse(self, milliseconds: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::pulse(int milliseconds)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#pulse

    Parameters
    ----------

    milliseconds : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::pulse(int milliseconds)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter5pulseEi', milliseconds,
    )

  @overload(int)
  def burst(self, num: int) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::burst(int num)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#burst

    Parameters
    ----------

    num : int
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::burst(int num)
    self.uglySide.call('ritual_ZN21QQuickParticleEmitter5burstEi', num)

  @overload(int, float, float)
  def burst(self, num: int, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::burst(int num, qreal x, qreal
    y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#burst

    Parameters
    ----------

    num : int
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickParticleEmitter::burst(int num, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter5burstEidd', num, x, y,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparticleemitter.html#reset
    """
    #  void QQuickParticleEmitter::reset()
    ritual = 'ritual_ZN21QQuickParticleEmitter5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickParticleEmitter5resetEv'
    self.uglySide.call(ritual)

  def reclaculateGroupId(self) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::reclaculateGroupId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#reclaculateGroupId
    """
    #  void QQuickParticleEmitter::reclaculateGroupId() const
    self.uglySide.call(
        'ritual_ZNK21QQuickParticleEmitter18reclaculateGroupIdEv',
    )

  def effectiveExtruder(self) -> Optional[QQuickParticleExtruder]:
    """
    Calls Qt's 'QQuickParticleExtruder
    *QQuickParticleEmitter::effectiveExtruder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#effectiveExtruder

    Returns
    -------

    Optional[QQuickParticleExtruder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleExtruder *QQuickParticleEmitter::effectiveExtruder()
    address = self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter17effectiveExtruderEv',
    )
    from . import QQuickParticleExtruder
    return QQuickParticleExtruder._cuteAt(address)

  def isEmitConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickParticleEmitter::isEmitConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html#isEmitConnected
    """
    #  bool QQuickParticleEmitter::isEmitConnected()
    return self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter15isEmitConnectedEv',
    )

  def callSystemEmittersChanged(self) -> None:
    """
    Calls Qt's 'void QQuickParticleEmitter::callSystemEmittersChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparticleemitter.html
    """
    #  void QQuickParticleEmitter::callSystemEmittersChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickParticleEmitter25callSystemEmittersChangedEv',
    )
