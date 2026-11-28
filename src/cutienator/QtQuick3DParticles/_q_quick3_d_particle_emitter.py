"""
QQuick3DParticleEmitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleemitter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DParticleEmitter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtQuick3D import QQuick3DNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMatrix4x4, QQuaternion, QVector3D
  from . import QQuick3DParticle, QQuick3DParticleAbstractShape
  from . import QQuick3DParticleDirection, QQuick3DParticleEmitBurst
  from . import QQuick3DParticleEmitBurstData
  from . import QQuick3DParticleModelBlendParticle, QQuick3DParticleSystem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMatrix4x4 = WAIT['QMatrix4x4']
  QQuaternion = WAIT['QQuaternion']
  QQuick3DParticle = WAIT['QQuick3DParticle']
  QQuick3DParticleAbstractShape = WAIT['QQuick3DParticleAbstractShape']
  QQuick3DParticleDirection = WAIT['QQuick3DParticleDirection']
  QQuick3DParticleEmitBurst = WAIT['QQuick3DParticleEmitBurst']
  QQuick3DParticleEmitBurstData = WAIT['QQuick3DParticleEmitBurstData']
  QQuick3DParticleModelBlendParticle = WAIT['QQuick3DParticleModelBlendParticle']
  QQuick3DParticleSystem = WAIT['QQuick3DParticleSystem']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DParticleEmitter(QQuick3DNode):
  """
  The cute side of Qt's QQuick3DParticleEmitter: a plain Python object
  standing in front of one C++ QQuick3DParticleEmitter.

  It is built on the cute 'QQuick3DNode', as Qt's QQuick3DParticleEmitter is
  built on Qt's QQuick3DNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DParticleEmitter that has a ritual and that
  Python can call so far, 77 names in all: 'metaObject', 'tr', 'enabled',
  'velocity', 'system', 'emitRate', 'particleScale', 'particleEndScale',
  'particleScaleVariation', 'particleEndScaleVariation', 'lifeSpan',
  'lifeSpanVariation', 'particle', 'shape', 'particleRotation',
  'particleRotationVariation', 'particleRotationVelocity',
  'particleRotationVelocityVariation', 'depthBias', 'reversed', 'emitMode',
  'burst', 'setEnabled', 'setVelocity', 'setSystem', 'setEmitRate',
  'setParticleScale', 'setParticleEndScale', 'setParticleScaleVariation',
  'setParticleEndScaleVariation', 'setLifeSpan', 'setLifeSpanVariation',
  'setParticle', 'setShape', 'setParticleRotation',
  'setParticleRotationVariation', 'setParticleRotationVelocity',
  'setParticleRotationVelocityVariation', 'setDepthBias', 'setReversed',
  'setEmitMode', 'velocityChanged', 'systemChanged', 'emitRateChanged',
  'particleScaleChanged', 'particleEndScaleChanged',
  'particleScaleVariationChanged', 'particleEndScaleVariationChanged',
  'lifeSpanChanged', 'lifeSpanVariationChanged', 'particleChanged',
  'shapeChanged', 'particleRotationChanged',
  'particleRotationVariationChanged', 'particleRotationVelocityChanged',
  'particleRotationVariationVelocityChanged', 'enabledChanged',
  'depthBiasChanged', 'reversedChanged', 'emitModeChanged',
  'componentComplete', 'registerEmitBurst', 'unRegisterEmitBurst',
  'generateEmitBursts', 'emitParticle', 'emitParticles',
  'emitActivationNodeParticles', 'emitParticlesBurst', 'getEmitAmount',
  'getEmitAmountFromDynamicBursts', 'reset', 'appendEmitBurst',
  'emitBurstCount', 'emitBurst', 'clearEmitBursts', 'replaceEmitBurst',
  'removeLastEmitBurst'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DParticleEmitter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DParticleEmitter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DParticleEmitter::~QQuick3DParticleEmitter()': the
    destructor: Python never removes a C++ QQuick3DParticleEmitter.
  - Qt's 'QQmlListProperty<QQuick3DParticleEmitBurst>
    QQuick3DParticleEmitter::emitBursts()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuick3DParticleEmitter::appendEmitBurst(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0,
    QQuick3DParticleEmitBurst *a1)': names
    'QQmlListProperty<QQuick3DParticleEmitBurst>', which has no cute class
    yet.
  - Qt's 'qsizetype QQuick3DParticleEmitter::emitBurstCount(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0)': names
    'QQmlListProperty<QQuick3DParticleEmitBurst>', which has no cute class
    yet.
  - Qt's 'QQuick3DParticleEmitBurst *QQuick3DParticleEmitter::emitBurst(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0, qsizetype a1)': names
    'QQmlListProperty<QQuick3DParticleEmitBurst>', which has no cute class
    yet.
  - Qt's 'void QQuick3DParticleEmitter::clearEmitBursts(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0)': names
    'QQmlListProperty<QQuick3DParticleEmitBurst>', which has no cute class
    yet.
  - Qt's 'void QQuick3DParticleEmitter::replaceEmitBurst(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0, qsizetype a1,
    QQuick3DParticleEmitBurst *a2)': names
    'QQmlListProperty<QQuick3DParticleEmitBurst>', which has no cute class
    yet.
  - Qt's 'void QQuick3DParticleEmitter::removeLastEmitBurst(
    QQmlListProperty<QQuick3DParticleEmitBurst> *a0)': names
    'QQmlListProperty<QQuick3DParticleEmitBurst>', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 92 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DParticleEmitter is created at the first use, not by
    'QQuick3DParticleEmitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DParticleEmitter.
  - Qt tells when it has removed the C++ QQuick3DParticleEmitter. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DParticleEmitter that has no cute function yet,
    'emitBursts', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DParticleEmitter, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class EmitMode(CuteNum):
    """
    The enum 'QQuick3DParticleEmitter::EmitMode' of Qt, with the 3 names Qt
    gives in it.
    """

    Default = Kee[int](0)
    SurfaceNormal = Kee[int](1)
    SurfaceReflected = Kee[int](2)

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
    Calls Qt's 'QString QQuick3DParticleEmitter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitter.html#tr

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
    #  QString QQuick3DParticleEmitter::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuick3DParticleEmitter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DParticleEmitter'

  #  A C++ QQuick3DParticleEmitter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DParticleEmitter'

  #  The functions Qt calls itself that QQuick3DParticleEmitter is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'burst': (
          ('_ZN23QQuick3DParticleEmitter5burstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
          ('_ZN23QQuick3DParticleEmitter5burstEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
          ('_ZN23QQuick3DParticleEmitter5burstEiiRK9QVector3D',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QVector3D'),
           )),
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
    Calls Qt's 'const QMetaObject *QQuick3DParticleEmitter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DParticleEmitter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleEmitter::enabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#enabled
    """
    #  bool QQuick3DParticleEmitter::enabled() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter7enabledEv',
    )

  def velocity(self) -> Optional[QQuick3DParticleDirection]:
    """
    Calls Qt's 'QQuick3DParticleDirection
    *QQuick3DParticleEmitter::velocity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#velocity

    Returns
    -------

    Optional[QQuick3DParticleDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleDirection *QQuick3DParticleEmitter::velocity() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter8velocityEv',
    )
    from . import QQuick3DParticleDirection
    return QQuick3DParticleDirection._cuteAt(address)

  def system(self) -> Optional[QQuick3DParticleSystem]:
    """
    Calls Qt's 'QQuick3DParticleSystem *QQuick3DParticleEmitter::system()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#system

    Returns
    -------

    Optional[QQuick3DParticleSystem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleSystem *QQuick3DParticleEmitter::system() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter6systemEv',
    )
    from . import QQuick3DParticleSystem
    return QQuick3DParticleSystem._cuteAt(address)

  def emitRate(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleEmitter::emitRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitRate
    """
    #  float QQuick3DParticleEmitter::emitRate() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter8emitRateEv',
    )

  def particleScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleEmitter::particleScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#particleScale
    """
    #  float QQuick3DParticleEmitter::particleScale() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter13particleScaleEv',
    )

  def particleEndScale(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleEmitter::particleEndScale() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#particleEndScale
    """
    #  float QQuick3DParticleEmitter::particleEndScale() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter16particleEndScaleEv',
    )

  def particleScaleVariation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleEmitter::particleScaleVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  float QQuick3DParticleEmitter::particleScaleVariation() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter22particleScaleVariationEv',
    )

  def particleEndScaleVariation(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleEmitter::particleEndScaleVariation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  float QQuick3DParticleEmitter::particleEndScaleVariation() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter25particleEndScaleVariationEv',
    )

  def lifeSpan(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleEmitter::lifeSpan() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#lifeSpan
    """
    #  int QQuick3DParticleEmitter::lifeSpan() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter8lifeSpanEv',
    )

  def lifeSpanVariation(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleEmitter::lifeSpanVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#lifeSpanVariation
    """
    #  int QQuick3DParticleEmitter::lifeSpanVariation() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter17lifeSpanVariationEv',
    )

  def particle(self) -> Optional[QQuick3DParticle]:
    """
    Calls Qt's 'QQuick3DParticle *QQuick3DParticleEmitter::particle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#particle

    Returns
    -------

    Optional[QQuick3DParticle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticle *QQuick3DParticleEmitter::particle() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter8particleEv',
    )
    from . import QQuick3DParticle
    return QQuick3DParticle._cuteAt(address)

  def shape(self) -> Optional[QQuick3DParticleAbstractShape]:
    """
    Calls Qt's 'QQuick3DParticleAbstractShape
    *QQuick3DParticleEmitter::shape() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitter.html#shape

    Returns
    -------

    Optional[QQuick3DParticleAbstractShape]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleAbstractShape *QQuick3DParticleEmitter::shape() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter5shapeEv',
    )
    from . import QQuick3DParticleAbstractShape
    return QQuick3DParticleAbstractShape._cuteAt(address)

  def particleRotation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleEmitter::particleRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#particleRotation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleEmitter::particleRotation() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter16particleRotationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def particleRotationVariation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleEmitter::particleRotationVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleEmitter::particleRotationVariation() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter25particleRotationVariationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def particleRotationVelocity(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuick3DParticleEmitter::particleRotationVelocity()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleEmitter::particleRotationVelocity() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter24particleRotationVelocityEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def particleRotationVelocityVariation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D
    QQuick3DParticleEmitter::particleRotationVelocityVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuick3DParticleEmitter::particleRotationVelocityVariation()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter33particleRotationVelocityVaria'
        'tionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def depthBias(self) -> float:
    """
    Calls Qt's 'float QQuick3DParticleEmitter::depthBias() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#depthBias
    """
    #  float QQuick3DParticleEmitter::depthBias() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter9depthBiasEv',
    )

  def reversed(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DParticleEmitter::reversed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#reversed
    """
    #  bool QQuick3DParticleEmitter::reversed() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter8reversedEv',
    )

  def emitMode(self) -> EmitMode:
    """
    Calls Qt's 'EmitMode QQuick3DParticleEmitter::emitMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitMode

    Returns
    -------

    EmitMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'EmitMode(number)' gives.
    """
    #  EmitMode QQuick3DParticleEmitter::emitMode() const
    return QQuick3DParticleEmitter.EmitMode(self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter8emitModeEv',
    ))

  def emitBurstCount(self) -> int:
    """
    Calls Qt's 'qsizetype QQuick3DParticleEmitter::emitBurstCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitBurstCount
    """
    #  qsizetype QQuick3DParticleEmitter::emitBurstCount() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter14emitBurstCountEv',
    )

  @overload(int)
  def emitBurst(self, a0: int) -> Optional[QQuick3DParticleEmitBurst]:
    """
    Calls Qt's 'QQuick3DParticleEmitBurst
    *QQuick3DParticleEmitter::emitBurst(qsizetype a0) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitBurst

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuick3DParticleEmitBurst]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DParticleEmitBurst
    #      *QQuick3DParticleEmitter::emitBurst(qsizetype a0) const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DParticleEmitter9emitBurstEx', a0,
    )
    from . import QQuick3DParticleEmitBurst
    return QQuick3DParticleEmitBurst._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter10setEnabledEb', enabled,
    )

  @overload(QQuick3DParticleDirection)
  @overload(NoneType)
  def setVelocity(
      self,
      velocity: Optional[QQuick3DParticleDirection],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setVelocity(QQuick3DParticleDirection
    *velocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setVelocity

    Parameters
    ----------

    velocity : Optional[QQuick3DParticleDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::setVelocity(QQuick3DParticleDirection
    #      *velocity)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter11setVelocityEP25QQuick3DParticl'
        'eDirection',
        self._addressOf(velocity),
    )

  @overload(QQuick3DParticleSystem)
  @overload(NoneType)
  def setSystem(self, system: Optional[QQuick3DParticleSystem]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setSystem(QQuick3DParticleSystem *system)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setSystem

    Parameters
    ----------

    system : Optional[QQuick3DParticleSystem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::setSystem(QQuick3DParticleSystem
    #      *system)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter9setSystemEP22QQuick3DParticleSy'
        'stem',
        self._addressOf(system),
    )

  @overload(float)
  def setEmitRate(self, emitRate: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setEmitRate(float emitRate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setEmitRate

    Parameters
    ----------

    emitRate : float
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setEmitRate(float emitRate)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter11setEmitRateEf', emitRate,
    )

  @overload(float)
  def setParticleScale(self, particleScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setParticleScale(float
    particleScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setParticleScale

    Parameters
    ----------

    particleScale : float
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setParticleScale(float particleScale)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter16setParticleScaleEf',
        particleScale,
    )

  @overload(float)
  def setParticleEndScale(self, particleEndScale: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setParticleEndScale(float
    particleEndScale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setParticleEndScale

    Parameters
    ----------

    particleEndScale : float
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setParticleEndScale(float
    #      particleEndScale)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter19setParticleEndScaleEf',
        particleEndScale,
    )

  @overload(float)
  def setParticleScaleVariation(self, particleScaleVariation: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setParticleScaleVariation(float
    particleScaleVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    particleScaleVariation : float
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setParticleScaleVariation(float
    #      particleScaleVariation)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter25setParticleScaleVariationEf',
        particleScaleVariation,
    )

  @overload(float)
  def setParticleEndScaleVariation(
      self,
      particleEndScaleVariation: float,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setParticleEndScaleVariation(float
    particleEndScaleVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    particleEndScaleVariation : float
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setParticleEndScaleVariation(float
    #      particleEndScaleVariation)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter28setParticleEndScaleVariationEf',
        particleEndScaleVariation,
    )

  @overload(int)
  def setLifeSpan(self, lifeSpan: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setLifeSpan(int lifeSpan)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setLifeSpan

    Parameters
    ----------

    lifeSpan : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setLifeSpan(int lifeSpan)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter11setLifeSpanEi', lifeSpan,
    )

  @overload(int)
  def setLifeSpanVariation(self, lifeSpanVariation: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setLifeSpanVariation(int
    lifeSpanVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setLifeSpanVariation

    Parameters
    ----------

    lifeSpanVariation : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setLifeSpanVariation(int
    #      lifeSpanVariation)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter20setLifeSpanVariationEi',
        lifeSpanVariation,
    )

  @overload(QQuick3DParticle)
  @overload(NoneType)
  def setParticle(self, particle: Optional[QQuick3DParticle]) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setParticle(QQuick3DParticle
    *particle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setParticle

    Parameters
    ----------

    particle : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::setParticle(QQuick3DParticle *particle)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter11setParticleEP16QQuick3DParticl'
        'e',
        self._addressOf(particle),
    )

  @overload(QQuick3DParticleAbstractShape)
  @overload(NoneType)
  def setShape(self, shape: Optional[QQuick3DParticleAbstractShape]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setShape(QQuick3DParticleAbstractShape *shape)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setShape

    Parameters
    ----------

    shape : Optional[QQuick3DParticleAbstractShape]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::setShape(QQuick3DParticleAbstractShape
    #      *shape)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter8setShapeEP29QQuick3DParticleAbs'
        'tractShape',
        self._addressOf(shape),
    )

  @overload(QVector3D)
  def setParticleRotation(self, particleRotation: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setParticleRotation(const
    QVector3D &particleRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setParticleRotation

    Parameters
    ----------

    particleRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleEmitter::setParticleRotation(const QVector3D
    #      &particleRotation)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter19setParticleRotationERK9QVector'
        '3D',
        self._valueOf(particleRotation),
    )

  @overload(QVector3D)
  def setParticleRotationVariation(
      self,
      particleRotationVariation: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setParticleRotationVariation(const QVector3D
    &particleRotationVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    particleRotationVariation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleEmitter::setParticleRotationVariation(const
    #      QVector3D &particleRotationVariation)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter28setParticleRotationVariationER'
        'K9QVector3D',
        self._valueOf(particleRotationVariation),
    )

  @overload(QVector3D)
  def setParticleRotationVelocity(
      self,
      particleRotationVelocity: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setParticleRotationVelocity(const QVector3D
    &particleRotationVelocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    particleRotationVelocity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleEmitter::setParticleRotationVelocity(const
    #      QVector3D &particleRotationVelocity)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter27setParticleRotationVelocityERK'
        '9QVector3D',
        self._valueOf(particleRotationVelocity),
    )

  @overload(QVector3D)
  def setParticleRotationVelocityVariation(
      self,
      particleRotationVelocityVariation: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::setParticleRotationVelocityVariation(const
    QVector3D &particleRotationVelocityVariation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    particleRotationVelocityVariation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleEmitter::setParticleRotationVelocityVariation(
    #      const QVector3D &particleRotationVelocityVariation)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter36setParticleRotationVelocityVar'
        'iationERK9QVector3D',
        self._valueOf(particleRotationVelocityVariation),
    )

  @overload(float)
  def setDepthBias(self, bias: float) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setDepthBias(float bias)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setDepthBias

    Parameters
    ----------

    bias : float
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setDepthBias(float bias)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter12setDepthBiasEf', bias,
    )

  @overload(bool)
  def setReversed(self, reversed: bool) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setReversed(bool reversed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setReversed

    Parameters
    ----------

    reversed : bool
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::setReversed(bool reversed)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter11setReversedEb', reversed,
    )

  @overload(EmitMode)
  def setEmitMode(self, mode: EmitMode) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::setEmitMode(EmitMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#setEmitMode

    Parameters
    ----------

    mode : EmitMode
      Passed on as its number.
    """
    #  void QQuick3DParticleEmitter::setEmitMode(EmitMode mode)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter11setEmitModeENS_8EmitModeE',
        mode.value,
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
    'QQuick3DParticleEmitter::QQuick3DParticleEmitter(QQuick3DNode *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    parent : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DParticleEmitter::QQuick3DParticleEmitter(QQuick3DNode *parent)
    self._noteCreation(QQuick3DParticleEmitter, lambda: Rituals.call(
        'ritual_ZN23QQuick3DParticleEmitterC1EP12QQuick3DNode',
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
  def burst(self, count: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::burst(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitter.html#burst

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::burst(int count)
    ritual = 'ritual_ZN23QQuick3DParticleEmitter5burstEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuick3DParticleEmitter5burstEi'
    self.uglySide.call(ritual, count)

  @overload(int, int)
  def burst(self, count: int, duration: int) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::burst(int count, int
    duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitter.html#burst

    Parameters
    ----------

    count : int
      Passed on as it is.

    duration : int
      Passed on as it is.
    """
    #  void QQuick3DParticleEmitter::burst(int count, int duration)
    ritual = 'ritual_ZN23QQuick3DParticleEmitter5burstEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuick3DParticleEmitter5burstEii'
    self.uglySide.call(ritual, count, duration)

  @overload(int, int, QVector3D)
  def burst(self, count: int, duration: int, position: QVector3D) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::burst(int count, int duration,
    const QVector3D &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitter.html#burst

    Parameters
    ----------

    count : int
      Passed on as it is.

    duration : int
      Passed on as it is.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuick3DParticleEmitter::burst(int count, int duration, const
    #      QVector3D &position)
    ritual = 'ritual_ZN23QQuick3DParticleEmitter5burstEiiRK9QVector3D'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuick3DParticleEmitter5burstEiiRK9QVector3D'
    self.uglySide.call(ritual, count, duration, self._valueOf(position))

  def velocityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::velocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#velocityChanged
    """
    #  void QQuick3DParticleEmitter::velocityChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15velocityChangedEv',
    )

  def systemChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::systemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#systemChanged
    """
    #  void QQuick3DParticleEmitter::systemChanged()
    self.uglySide.call('ritual_ZN23QQuick3DParticleEmitter13systemChangedEv')

  def emitRateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::emitRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitRateChanged
    """
    #  void QQuick3DParticleEmitter::emitRateChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15emitRateChangedEv',
    )

  def particleScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::particleScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#particleScaleChanged
    """
    #  void QQuick3DParticleEmitter::particleScaleChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter20particleScaleChangedEv',
    )

  def particleEndScaleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::particleEndScaleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::particleEndScaleChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter23particleEndScaleChangedEv',
    )

  def particleScaleVariationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::particleScaleVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::particleScaleVariationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter29particleScaleVariationChangedE'
        'v',
    )

  def particleEndScaleVariationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::particleEndScaleVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::particleEndScaleVariationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter32particleEndScaleVariationChang'
        'edEv',
    )

  def lifeSpanChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::lifeSpanChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#lifeSpanChanged
    """
    #  void QQuick3DParticleEmitter::lifeSpanChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15lifeSpanChangedEv',
    )

  def lifeSpanVariationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::lifeSpanVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::lifeSpanVariationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter24lifeSpanVariationChangedEv',
    )

  def particleChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::particleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#particleChanged
    """
    #  void QQuick3DParticleEmitter::particleChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15particleChangedEv',
    )

  def shapeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::shapeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#shapeChanged
    """
    #  void QQuick3DParticleEmitter::shapeChanged()
    self.uglySide.call('ritual_ZN23QQuick3DParticleEmitter12shapeChangedEv')

  def particleRotationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::particleRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::particleRotationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter23particleRotationChangedEv',
    )

  def particleRotationVariationChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::particleRotationVariationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::particleRotationVariationChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter32particleRotationVariationChang'
        'edEv',
    )

  def particleRotationVelocityChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::particleRotationVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void QQuick3DParticleEmitter::particleRotationVelocityChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter31particleRotationVelocityChange'
        'dEv',
    )

  def particleRotationVariationVelocityChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::particleRotationVariationVelocityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html
    """
    #  void
    #      QQuick3DParticleEmitter::particleRotationVariationVelocityChanged(
    #      )
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter40particleRotationVariationVeloc'
        'ityChangedEv',
    )

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#enabledChanged
    """
    #  void QQuick3DParticleEmitter::enabledChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter14enabledChangedEv',
    )

  def depthBiasChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::depthBiasChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#depthBiasChanged
    """
    #  void QQuick3DParticleEmitter::depthBiasChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter16depthBiasChangedEv',
    )

  def reversedChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::reversedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#reversedChanged
    """
    #  void QQuick3DParticleEmitter::reversedChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15reversedChangedEv',
    )

  def emitModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::emitModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitModeChanged
    """
    #  void QQuick3DParticleEmitter::emitModeChanged()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15emitModeChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#componentComplete
    """
    #  void QQuick3DParticleEmitter::componentComplete()
    ritual = 'ritual_ZN23QQuick3DParticleEmitter17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuick3DParticleEmitter17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuick3DParticleEmitBurst)
  @overload(NoneType)
  def registerEmitBurst(
      self,
      emitBurst: Optional[QQuick3DParticleEmitBurst],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::registerEmitBurst(QQuick3DParticleEmitBurst
    *emitBurst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#registerEmitBurst

    Parameters
    ----------

    emitBurst : Optional[QQuick3DParticleEmitBurst]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::registerEmitBurst(
    #      QQuick3DParticleEmitBurst *emitBurst)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter17registerEmitBurstEP25QQuick3DP'
        'articleEmitBurst',
        self._addressOf(emitBurst),
    )

  @overload(QQuick3DParticleEmitBurst)
  @overload(NoneType)
  def unRegisterEmitBurst(
      self,
      emitBurst: Optional[QQuick3DParticleEmitBurst],
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::unRegisterEmitBurst(QQuick3DParticleEmitBurst
    *emitBurst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#unRegisterEmitBurst

    Parameters
    ----------

    emitBurst : Optional[QQuick3DParticleEmitBurst]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::unRegisterEmitBurst(
    #      QQuick3DParticleEmitBurst *emitBurst)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter19unRegisterEmitBurstEP25QQuick3'
        'DParticleEmitBurst',
        self._addressOf(emitBurst),
    )

  def generateEmitBursts(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::generateEmitBursts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#generateEmitBursts
    """
    #  void QQuick3DParticleEmitter::generateEmitBursts()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter18generateEmitBurstsEv',
    )

  @overload(QQuick3DParticle, float, QMatrix4x4, QQuaternion, QVector3D)
  @overload(NoneType, float, QMatrix4x4, QQuaternion, QVector3D)
  @overload(QQuick3DParticle, float, QMatrix4x4, QQuaternion, QVector3D, int)
  @overload(NoneType, float, QMatrix4x4, QQuaternion, QVector3D, int)
  @overload(
      QQuick3DParticle, float, QMatrix4x4, QQuaternion, QVector3D, int,
      QVector3D,
  )
  @overload(
      NoneType, float, QMatrix4x4, QQuaternion, QVector3D, int, QVector3D,
  )
  @overload(
      QQuick3DParticle, float, QMatrix4x4, QQuaternion, QVector3D, int,
      QVector3D, QVector3D,
  )
  @overload(
      NoneType, float, QMatrix4x4, QQuaternion, QVector3D, int, QVector3D,
      QVector3D,
  )
  def emitParticle(
      self,
      particle: Optional[QQuick3DParticle],
      startTime: float,
      transform: QMatrix4x4,
      parentRotation: QQuaternion,
      centerPos: QVector3D,
      index: int = -1,
      velocity: Optional[QVector3D] = None,
      normal: Optional[QVector3D] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::emitParticle(QQuick3DParticle
    *particle, float startTime, const QMatrix4x4 &transform, const
    QQuaternion &parentRotation, const QVector3D &centerPos, int index, const
    QVector3D &velocity, const QVector3D &normal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitParticle

    Parameters
    ----------

    particle : Optional[QQuick3DParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    startTime : float
      Passed on as it is.

    transform : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    parentRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    centerPos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    index : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    velocity : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D()' is then passed on.

    normal : Optional[QVector3D]
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own. May be left out, as in Qt: a new 'QVector3D()' is then passed on.
    """
    #  void QQuick3DParticleEmitter::emitParticle(QQuick3DParticle *particle,
    #      float startTime, const QMatrix4x4 &transform, const QQuaternion
    #      &parentRotation, const QVector3D &centerPos, int index, const
    #      QVector3D &velocity, const QVector3D &normal)
    if velocity is None:
      from ..QtGui import QVector3D
      velocity = QVector3D()
    if normal is None:
      from ..QtGui import QVector3D
      normal = QVector3D()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter12emitParticleEP16QQuick3DPartic'
        'lefRK10QMatrix4x4RK11QQuaternionRK9QVector3DiSA_SA_',
        self._addressOf(particle), startTime, self._valueOf(transform),
        self._valueOf(parentRotation), self._valueOf(centerPos), index,
        self._valueOf(velocity), self._valueOf(normal),
    )

  def emitParticles(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::emitParticles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitParticles
    """
    #  void QQuick3DParticleEmitter::emitParticles()
    self.uglySide.call('ritual_ZN23QQuick3DParticleEmitter13emitParticlesEv')

  @overload(QQuick3DParticleModelBlendParticle)
  @overload(NoneType)
  def emitActivationNodeParticles(
      self,
      particle: Optional[QQuick3DParticleModelBlendParticle],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::emitActivationNodeParticles(
    QQuick3DParticleModelBlendParticle *particle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    particle : Optional[QQuick3DParticleModelBlendParticle]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::emitActivationNodeParticles(
    #      QQuick3DParticleModelBlendParticle *particle)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter27emitActivationNodeParticlesEP3'
        '4QQuick3DParticleModelBlendParticle',
        self._addressOf(particle),
    )

  @overload(QQuick3DParticleEmitBurstData)
  def emitParticlesBurst(self, burst: QQuick3DParticleEmitBurstData) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::emitParticlesBurst(const
    QQuick3DParticleEmitBurstData &burst)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#emitParticlesBurst

    Parameters
    ----------

    burst : QQuick3DParticleEmitBurstData
      Passed on as a value: Qt reads the C++ QQuick3DParticleEmitBurstData,
      which stays Python's own.
    """
    #  void QQuick3DParticleEmitter::emitParticlesBurst(const
    #      QQuick3DParticleEmitBurstData &burst)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter18emitParticlesBurstERK29QQuick3'
        'DParticleEmitBurstData',
        self._valueOf(burst),
    )

  def getEmitAmount(self) -> int:
    """
    Calls Qt's 'int QQuick3DParticleEmitter::getEmitAmount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#getEmitAmount
    """
    #  int QQuick3DParticleEmitter::getEmitAmount()
    return self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter13getEmitAmountEv',
    )

  @overload()
  @overload(int)
  def getEmitAmountFromDynamicBursts(self, triggerType: int = 0) -> int:
    """
    Calls Qt's 'int
    QQuick3DParticleEmitter::getEmitAmountFromDynamicBursts(int
    triggerType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html

    Parameters
    ----------

    triggerType : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QQuick3DParticleEmitter::getEmitAmountFromDynamicBursts(int
    #      triggerType)
    return self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter30getEmitAmountFromDynamicBursts'
        'Ei',
        triggerType,
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dparticleemitter.html#reset
    """
    #  void QQuick3DParticleEmitter::reset()
    self.uglySide.call('ritual_ZN23QQuick3DParticleEmitter5resetEv')

  @overload(QQuick3DParticleEmitBurst)
  @overload(NoneType)
  def appendEmitBurst(self, a0: Optional[QQuick3DParticleEmitBurst]) -> None:
    """
    Calls Qt's 'void
    QQuick3DParticleEmitter::appendEmitBurst(QQuick3DParticleEmitBurst *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#appendEmitBurst

    Parameters
    ----------

    a0 : Optional[QQuick3DParticleEmitBurst]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      QQuick3DParticleEmitter::appendEmitBurst(QQuick3DParticleEmitBurst
    #      *a0)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15appendEmitBurstEP25QQuick3DPar'
        'ticleEmitBurst',
        self._addressOf(a0),
    )

  def clearEmitBursts(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::clearEmitBursts()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#clearEmitBursts
    """
    #  void QQuick3DParticleEmitter::clearEmitBursts()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter15clearEmitBurstsEv',
    )

  @overload(int, QQuick3DParticleEmitBurst)
  @overload(int, NoneType)
  def replaceEmitBurst(
      self,
      a0: int,
      a1: Optional[QQuick3DParticleEmitBurst],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::replaceEmitBurst(qsizetype a0,
    QQuick3DParticleEmitBurst *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#replaceEmitBurst

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : Optional[QQuick3DParticleEmitBurst]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DParticleEmitter::replaceEmitBurst(qsizetype a0,
    #      QQuick3DParticleEmitBurst *a1)
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter16replaceEmitBurstExP25QQuick3DP'
        'articleEmitBurst',
        a0, self._addressOf(a1),
    )

  def removeLastEmitBurst(self) -> None:
    """
    Calls Qt's 'void QQuick3DParticleEmitter::removeLastEmitBurst()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dparticleemitter.html#removeLastEmitBurst
    """
    #  void QQuick3DParticleEmitter::removeLastEmitBurst()
    self.uglySide.call(
        'ritual_ZN23QQuick3DParticleEmitter19removeLastEmitBurstEv',
    )

  @staticmethod
  def emitBursts(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuick3DParticleEmitBurst>
    QQuick3DParticleEmitter::emitBursts()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DParticleEmitter.emitBursts' has no cute function yet. "
        "Qt's 'QQmlListProperty<QQuick3DParticleEmitBurst> "
        "QQuick3DParticleEmitter::emitBursts()': gives a type Python has no "
        "way to take yet.")
