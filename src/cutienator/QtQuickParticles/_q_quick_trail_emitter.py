"""
QQuickTrailEmitter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquicktrailemitter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickTrailEmitter to be private: it declares the class in a
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
from . import QQuickParticleEmitter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickParticleExtruder, QQuickV4ParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickParticleExtruder = WAIT['QQuickParticleExtruder']
  QQuickV4ParticleData = WAIT['QQuickV4ParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTrailEmitter(QQuickParticleEmitter):
  """
  The cute side of Qt's QQuickTrailEmitter: a plain Python object standing in
  front of one C++ QQuickTrailEmitter.

  It is built on the cute 'QQuickParticleEmitter', as Qt's QQuickTrailEmitter
  is built on Qt's QQuickParticleEmitter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTrailEmitter that has a ritual and that Python
  can call so far, 22 names in all: 'metaObject', 'tr', 'emitWindow',
  'reset', 'particlesPerParticlePerSecond', 'emitterXVariation',
  'emitterYVariation', 'follow', 'emissonShape', 'emitFollowParticles',
  'particlesPerParticlePerSecondChanged', 'emitterXVariationChanged',
  'emitterYVariationChanged', 'followChanged', 'emissionShapeChanged',
  'setParticlesPerParticlePerSecond', 'setEmitterXVariation',
  'setEmitterYVariation', 'setFollow', 'setEmissionShape',
  'recalcParticlesPerSecond', 'isEmitFollowConnected'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTrailEmitter::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTrailEmitter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTrailEmitter is created at the first use, not by
    'QQuickTrailEmitter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTrailEmitter.
  - Qt tells when it has removed the C++ QQuickTrailEmitter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTrailEmitter, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class EmitSize(CuteNum):
    """
    The enum 'QQuickTrailEmitter::EmitSize' of Qt, with the 1 names Qt gives
    in it.
    """

    ParticleSize = Kee[int](-2)

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
    Calls Qt's 'QString QQuickTrailEmitter::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktrailemitter.html#tr

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
    #  QString QQuickTrailEmitter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickTrailEmitter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTrailEmitter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTrailEmitter::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktrailemitter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTrailEmitter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickTrailEmitter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def particlesPerParticlePerSecond(self) -> int:
    """
    Calls Qt's 'int QQuickTrailEmitter::particlesPerParticlePerSecond()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html
    """
    #  int QQuickTrailEmitter::particlesPerParticlePerSecond() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickTrailEmitter29particlesPerParticlePerSecondEv',
    )

  def emitterXVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickTrailEmitter::emitterXVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emitterXVariation
    """
    #  qreal QQuickTrailEmitter::emitterXVariation() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickTrailEmitter17emitterXVariationEv',
    )

  def emitterYVariation(self) -> float:
    """
    Calls Qt's 'qreal QQuickTrailEmitter::emitterYVariation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emitterYVariation
    """
    #  qreal QQuickTrailEmitter::emitterYVariation() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickTrailEmitter17emitterYVariationEv',
    )

  def follow(self) -> str:
    """
    Calls Qt's 'QString QQuickTrailEmitter::follow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktrailemitter.html#follow

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTrailEmitter::follow() const
    return self.uglySide.call('ritual_ZNK18QQuickTrailEmitter6followEv')

  def emissonShape(self) -> Optional[QQuickParticleExtruder]:
    """
    Calls Qt's 'QQuickParticleExtruder *QQuickTrailEmitter::emissonShape()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emissonShape

    Returns
    -------

    Optional[QQuickParticleExtruder]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickParticleExtruder *QQuickTrailEmitter::emissonShape() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickTrailEmitter12emissonShapeEv',
    )
    from . import QQuickParticleExtruder
    return QQuickParticleExtruder._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setParticlesPerParticlePerSecond(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::setParticlesPerParticlePerSecond(int
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::setParticlesPerParticlePerSecond(int arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter32setParticlesPerParticlePerSecondEi',
        arg,
    )

  @overload(float)
  def setEmitterXVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::setEmitterXVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#setEmitterXVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::setEmitterXVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter20setEmitterXVariationEd', arg,
    )

  @overload(float)
  def setEmitterYVariation(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::setEmitterYVariation(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#setEmitterYVariation

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::setEmitterYVariation(qreal arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter20setEmitterYVariationEd', arg,
    )

  @overload(str)
  def setFollow(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::setFollow(const QString &arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktrailemitter.html#setFollow

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTrailEmitter::setFollow(const QString &arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter9setFollowERK7QString', arg,
    )

  @overload(QQuickParticleExtruder)
  @overload(NoneType)
  def setEmissionShape(self, arg: Optional[QQuickParticleExtruder]) -> None:
    """
    Calls Qt's 'void
    QQuickTrailEmitter::setEmissionShape(QQuickParticleExtruder *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#setEmissionShape

    Parameters
    ----------

    arg : Optional[QQuickParticleExtruder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTrailEmitter::setEmissionShape(QQuickParticleExtruder *arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter16setEmissionShapeEP22QQuickParticleE'
        'xtruder',
        self._addressOf(arg),
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
    'QQuickTrailEmitter::QQuickTrailEmitter(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#QQuickTrailEmitter

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTrailEmitter::QQuickTrailEmitter(QQuickItem *parent)
    self._noteCreation(QQuickTrailEmitter, lambda: Rituals.call(
        'ritual_ZN18QQuickTrailEmitterC1EP10QQuickItem',
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
    Calls Qt's 'void QQuickTrailEmitter::emitWindow(int timeStamp)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktrailemitter.html#emitWindow

    Parameters
    ----------

    timeStamp : int
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::emitWindow(int timeStamp)
    ritual = 'ritual_ZN18QQuickTrailEmitter10emitWindowEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickTrailEmitter10emitWindowEi'
    self.uglySide.call(ritual, timeStamp)

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktrailemitter.html#reset
    """
    #  void QQuickTrailEmitter::reset()
    ritual = 'ritual_ZN18QQuickTrailEmitter5resetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickTrailEmitter5resetEv'
    self.uglySide.call(ritual)

  @overload(QList[QQuickV4ParticleData], QQuickV4ParticleData)
  def emitFollowParticles(
      self,
      particles: QList[QQuickV4ParticleData],
      followed: QQuickV4ParticleData,
  ) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::emitFollowParticles(const
    QList<QQuickV4ParticleData> &particles, const QQuickV4ParticleData
    &followed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emitFollowParticles

    Parameters
    ----------

    particles : QList[QQuickV4ParticleData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    followed : QQuickV4ParticleData
      Passed on as a value: Qt reads the C++ QQuickV4ParticleData, which
      stays Python's own.
    """
    #  void QQuickTrailEmitter::emitFollowParticles(const
    #      QList<QQuickV4ParticleData> &particles, const QQuickV4ParticleData
    #      &followed)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter19emitFollowParticlesERK5QListI20QQui'
        'ckV4ParticleDataERKS1_',
        self._valueOf(particles), self._valueOf(followed),
    )

  @overload(int)
  def particlesPerParticlePerSecondChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void
    QQuickTrailEmitter::particlesPerParticlePerSecondChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::particlesPerParticlePerSecondChanged(int arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter36particlesPerParticlePerSecondChange'
        'dEi',
        arg,
    )

  @overload(float)
  def emitterXVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::emitterXVariationChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emitterXVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::emitterXVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter24emitterXVariationChangedEd', arg,
    )

  @overload(float)
  def emitterYVariationChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::emitterYVariationChanged(qreal
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emitterYVariationChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickTrailEmitter::emitterYVariationChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter24emitterYVariationChangedEd', arg,
    )

  @overload(str)
  def followChanged(self, arg: str) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::followChanged(const QString &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#followChanged

    Parameters
    ----------

    arg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTrailEmitter::followChanged(const QString &arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter13followChangedERK7QString', arg,
    )

  @overload(QQuickParticleExtruder)
  @overload(NoneType)
  def emissionShapeChanged(
      self,
      arg: Optional[QQuickParticleExtruder],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickTrailEmitter::emissionShapeChanged(QQuickParticleExtruder *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#emissionShapeChanged

    Parameters
    ----------

    arg : Optional[QQuickParticleExtruder]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTrailEmitter::emissionShapeChanged(QQuickParticleExtruder
    #      *arg)
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter20emissionShapeChangedEP22QQuickParti'
        'cleExtruder',
        self._addressOf(arg),
    )

  def recalcParticlesPerSecond(self) -> None:
    """
    Calls Qt's 'void QQuickTrailEmitter::recalcParticlesPerSecond()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#recalcParticlesPerSecond
    """
    #  void QQuickTrailEmitter::recalcParticlesPerSecond()
    self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter24recalcParticlesPerSecondEv',
    )

  def isEmitFollowConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickTrailEmitter::isEmitFollowConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktrailemitter.html#isEmitFollowConnected
    """
    #  bool QQuickTrailEmitter::isEmitFollowConnected()
    return self.uglySide.call(
        'ritual_ZN18QQuickTrailEmitter21isEmitFollowConnectedEv',
    )
