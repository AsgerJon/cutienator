"""
QQuickCustomAffector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickcustomaffector_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickCustomAffector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtQuick import QQuickItem
from . import QQuickParticleAffector

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickDirection, QQuickParticleData, QQuickV4ParticleData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickDirection = WAIT['QQuickDirection']
  QQuickParticleData = WAIT['QQuickParticleData']
  QQuickV4ParticleData = WAIT['QQuickV4ParticleData']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickCustomAffector(QQuickParticleAffector):
  """
  The cute side of Qt's QQuickCustomAffector: a plain Python object standing
  in front of one C++ QQuickCustomAffector.

  It is built on the cute 'QQuickParticleAffector', as Qt's
  QQuickCustomAffector is built on Qt's QQuickParticleAffector, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickCustomAffector that has a ritual and that
  Python can call so far, 22 names in all: 'metaObject', 'tr',
  'affectSystem', 'position', 'velocity', 'acceleration', 'positionReset',
  'velocityReset', 'accelerationReset', 'relative', 'affectParticles',
  'positionChanged', 'velocityChanged', 'accelerationChanged',
  'relativeChanged', 'setPosition', 'setVelocity', 'setAcceleration',
  'setRelative', 'isAffectConnected', 'affectParticle', 'affectProperties'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickCustomAffector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickCustomAffector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickCustomAffector is created at the first use, not by
    'QQuickCustomAffector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickCustomAffector.
  - Qt tells when it has removed the C++ QQuickCustomAffector. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickCustomAffector::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcustomaffector.html#tr

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
    #  QString QQuickCustomAffector::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickCustomAffector2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickCustomAffector'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickCustomAffector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickCustomAffector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickCustomAffector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickCustomAffector::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcustomaffector.html#position

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickCustomAffector::position() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickCustomAffector8positionEv',
    )
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def velocity(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickCustomAffector::velocity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcustomaffector.html#velocity

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickCustomAffector::velocity() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickCustomAffector8velocityEv',
    )
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def acceleration(self) -> Optional[QQuickDirection]:
    """
    Calls Qt's 'QQuickDirection *QQuickCustomAffector::acceleration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#acceleration

    Returns
    -------

    Optional[QQuickDirection]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDirection *QQuickCustomAffector::acceleration() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickCustomAffector12accelerationEv',
    )
    from . import QQuickDirection
    return QQuickDirection._cuteAt(address)

  def relative(self) -> bool:
    """
    Calls Qt's 'bool QQuickCustomAffector::relative() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcustomaffector.html#relative
    """
    #  bool QQuickCustomAffector::relative() const
    return self.uglySide.call('ritual_ZNK20QQuickCustomAffector8relativeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDirection)
  @overload(NoneType)
  def setPosition(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::setPosition(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#setPosition

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCustomAffector::setPosition(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector11setPositionEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def setVelocity(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::setVelocity(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#setVelocity

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCustomAffector::setVelocity(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector11setVelocityEP15QQuickDirection',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def setAcceleration(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::setAcceleration(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#setAcceleration

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCustomAffector::setAcceleration(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector15setAccelerationEP15QQuickDirectio'
        'n',
        self._addressOf(arg),
    )

  @overload(bool)
  def setRelative(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::setRelative(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#setRelative

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickCustomAffector::setRelative(bool arg)
    self.uglySide.call('ritual_ZN20QQuickCustomAffector11setRelativeEb', arg)

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
    'QQuickCustomAffector::QQuickCustomAffector(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#QQuickCustomAffector

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickCustomAffector::QQuickCustomAffector(QQuickItem *parent)
    self._noteCreation(QQuickCustomAffector, lambda: Rituals.call(
        'ritual_ZN20QQuickCustomAffectorC1EP10QQuickItem',
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

  @overload(float)
  def affectSystem(self, dt: float) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::affectSystem(qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#affectSystem

    Parameters
    ----------

    dt : float
      Passed on as it is.
    """
    #  void QQuickCustomAffector::affectSystem(qreal dt)
    ritual = 'ritual_ZN20QQuickCustomAffector12affectSystemEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickCustomAffector12affectSystemEd'
    self.uglySide.call(ritual, dt)

  def positionReset(self) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::positionReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#positionReset
    """
    #  void QQuickCustomAffector::positionReset()
    self.uglySide.call('ritual_ZN20QQuickCustomAffector13positionResetEv')

  def velocityReset(self) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::velocityReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#velocityReset
    """
    #  void QQuickCustomAffector::velocityReset()
    self.uglySide.call('ritual_ZN20QQuickCustomAffector13velocityResetEv')

  def accelerationReset(self) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::accelerationReset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#accelerationReset
    """
    #  void QQuickCustomAffector::accelerationReset()
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector17accelerationResetEv',
    )

  @overload(QList[QQuickV4ParticleData], float)
  def affectParticles(
      self,
      particles: QList[QQuickV4ParticleData],
      dt: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::affectParticles(const
    QList<QQuickV4ParticleData> &particles, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#affectParticles

    Parameters
    ----------

    particles : QList[QQuickV4ParticleData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    dt : float
      Passed on as it is.
    """
    #  void QQuickCustomAffector::affectParticles(const
    #      QList<QQuickV4ParticleData> &particles, qreal dt)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector15affectParticlesERK5QListI20QQuick'
        'V4ParticleDataEd',
        self._valueOf(particles), dt,
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def positionChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::positionChanged(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#positionChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCustomAffector::positionChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector15positionChangedEP15QQuickDirectio'
        'n',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def velocityChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::velocityChanged(QQuickDirection
    *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#velocityChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCustomAffector::velocityChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector15velocityChangedEP15QQuickDirectio'
        'n',
        self._addressOf(arg),
    )

  @overload(QQuickDirection)
  @overload(NoneType)
  def accelerationChanged(self, arg: Optional[QQuickDirection]) -> None:
    """
    Calls Qt's 'void
    QQuickCustomAffector::accelerationChanged(QQuickDirection *arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#accelerationChanged

    Parameters
    ----------

    arg : Optional[QQuickDirection]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickCustomAffector::accelerationChanged(QQuickDirection *arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector19accelerationChangedEP15QQuickDire'
        'ction',
        self._addressOf(arg),
    )

  @overload(bool)
  def relativeChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::relativeChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#relativeChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickCustomAffector::relativeChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector15relativeChangedEb', arg,
    )

  def isAffectConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickCustomAffector::isAffectConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#isAffectConnected
    """
    #  bool QQuickCustomAffector::isAffectConnected()
    return self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector17isAffectConnectedEv',
    )

  @overload(QQuickParticleData, float)
  @overload(NoneType, float)
  def affectParticle(
      self,
      d: Optional[QQuickParticleData],
      dt: float,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickCustomAffector::affectParticle(QQuickParticleData
    *d, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#affectParticle

    Parameters
    ----------

    d : Optional[QQuickParticleData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dt : float
      Passed on as it is.
    """
    #  bool QQuickCustomAffector::affectParticle(QQuickParticleData *d, qreal
    #      dt)
    ritual = (
        'ritual_ZN20QQuickCustomAffector14affectParticleEP18QQuickParticleD'
        'atad')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickCustomAffector14affectParticleEP18QQuickPar'
          'ticleDatad')
    return self.uglySide.call(ritual, self._addressOf(d), dt)

  @overload(QList[QQuickParticleData], float)
  def affectProperties(
      self,
      particles: QList[QQuickParticleData],
      dt: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickCustomAffector::affectProperties(const
    QList<QQuickParticleData *> &particles, qreal dt)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcustomaffector.html#affectProperties

    Parameters
    ----------

    particles : QList[QQuickParticleData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    dt : float
      Passed on as it is.
    """
    #  void QQuickCustomAffector::affectProperties(const
    #      QList<QQuickParticleData *> &particles, qreal dt)
    self.uglySide.call(
        'ritual_ZN20QQuickCustomAffector16affectPropertiesERK5QListIP18QQui'
        'ckParticleDataEd',
        self._valueOf(particles), dt,
    )
