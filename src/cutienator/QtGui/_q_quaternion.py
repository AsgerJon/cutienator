"""
QQuaternion binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qquaternion.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QVector3D, QVector4D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']
  QVector4D = WAIT['QVector4D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuaternion(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuaternion: a plain Python object standing in front
  of one C++ QQuaternion.

  C++ hands a QQuaternion around as a copy, so every C++ QQuaternion behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuaternion that has a ritual and that Python can
  call so far, 30 names in all: 'isNull', 'isIdentity', 'vector',
  'setVector', 'x', 'y', 'z', 'scalar', 'setX', 'setY', 'setZ', 'setScalar',
  'dotProduct', 'length', 'lengthSquared', 'normalized', 'normalize',
  'inverted', 'conjugated', 'rotatedVector', 'toVector4D',
  'fromAxisAndAngle', 'toEulerAngles', 'fromEulerAngles', 'getAxes',
  'fromAxes', 'fromDirection', 'rotationTo', 'slerp', 'nlerp'. It can be made
  from Python, in 5 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QVariant QQuaternion::operator QVariant() const': an operator,
    which is not reflected yet.
  - Qt's 'void QQuaternion::getAxisAndAngle(QVector3D *axis, float *angle)
    const': takes a number to change where it is.
  - Qt's 'void QQuaternion::getAxisAndAngle(float *x, float *y, float *z,
    float *angle) const': takes a number to change where it is.
  - Qt's 'void QQuaternion::getEulerAngles(float *pitch, float *yaw, float
    *roll) const': takes a number to change where it is.
  - Qt's 'Axes QQuaternion::toAxes() const': gives 'QQuaternion::Axes', which
    has no cute class yet.
  - Qt's 'QQuaternion QQuaternion::fromAxes(Axes axes)': names
    'QQuaternion::Axes', which has no cute class yet.
  - Qt's 'QQuaternion::~QQuaternion()': the destructor: Python removes its
    C++ QQuaternion by it, and has no other use for it.

  What has no ritual
  ------------------

  10 of the 54 functions Qt declares: 9 takes or gives a type that cannot be
  passed yet; 1 a template.

  What to expect
  --------------

  - The C++ QQuaternion is created at the first use, not by
    'QQuaternion(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuaternion back gives a copy the ritual made for
    Python, in a new cute QQuaternion.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(THIS, THIS)
  def dotProduct(q1: QQuaternion, q2: QQuaternion) -> float:
    """
    Calls Qt's 'float QQuaternion::dotProduct(const QQuaternion &q1, const
    QQuaternion &q2)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#dotProduct

    Parameters
    ----------

    q1 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    q2 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  float QQuaternion::dotProduct(const QQuaternion &q1, const QQuaternion
    #      &q2)
    return Rituals.call(
        'ritual_ZN11QQuaternion10dotProductERKS_S1_',
        CuteMixin._valueOf(q1), CuteMixin._valueOf(q2),
    )

  @staticmethod
  @overload(QVector3D, float)
  def fromAxisAndAngle(axis: QVector3D, angle: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::fromAxisAndAngle(const QVector3D
    &axis, float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#fromAxisAndAngle

    Parameters
    ----------

    axis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::fromAxisAndAngle(const QVector3D &axis, float
    #      angle)
    address = Rituals.call(
        'ritual_ZN11QQuaternion16fromAxisAndAngleERK9QVector3Df',
        CuteMixin._valueOf(axis), angle,
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(float, float, float, float)
  def fromAxisAndAngle(
      x: float,
      y: float,
      z: float,
      angle: float,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::fromAxisAndAngle(float x, float y,
    float z, float angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#fromAxisAndAngle

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.

    angle : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::fromAxisAndAngle(float x, float y, float z,
    #      float angle)
    address = Rituals.call(
        'ritual_ZN11QQuaternion16fromAxisAndAngleEffff', x, y, z, angle,
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(float, float, float)
  def fromEulerAngles(pitch: float, yaw: float, roll: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::fromEulerAngles(float pitch, float
    yaw, float roll)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#fromEulerAngles

    Parameters
    ----------

    pitch : float
      Passed on as it is.

    yaw : float
      Passed on as it is.

    roll : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::fromEulerAngles(float pitch, float yaw, float
    #      roll)
    address = Rituals.call(
        'ritual_ZN11QQuaternion15fromEulerAnglesEfff', pitch, yaw, roll,
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D, QVector3D)
  def fromAxes(
      xAxis: QVector3D,
      yAxis: QVector3D,
      zAxis: QVector3D,
  ) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::fromAxes(const QVector3D &xAxis,
    const QVector3D &yAxis, const QVector3D &zAxis)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#fromAxes

    Parameters
    ----------

    xAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    yAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    zAxis : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::fromAxes(const QVector3D &xAxis, const
    #      QVector3D &yAxis, const QVector3D &zAxis)
    address = Rituals.call(
        'ritual_ZN11QQuaternion8fromAxesERK9QVector3DS2_S2_',
        CuteMixin._valueOf(xAxis), CuteMixin._valueOf(yAxis),
        CuteMixin._valueOf(zAxis),
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D)
  def fromDirection(direction: QVector3D, up: QVector3D) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::fromDirection(const QVector3D
    &direction, const QVector3D &up)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#fromDirection

    Parameters
    ----------

    direction : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    up : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::fromDirection(const QVector3D &direction,
    #      const QVector3D &up)
    address = Rituals.call(
        'ritual_ZN11QQuaternion13fromDirectionERK9QVector3DS2_',
        CuteMixin._valueOf(direction), CuteMixin._valueOf(up),
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(QVector3D, QVector3D)
  def rotationTo(from_: QVector3D, to: QVector3D) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::rotationTo(const QVector3D &from,
    const QVector3D &to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#rotationTo

    Parameters
    ----------

    from_ : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    to : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::rotationTo(const QVector3D &from, const
    #      QVector3D &to)
    address = Rituals.call(
        'ritual_ZN11QQuaternion10rotationToERK9QVector3DS2_',
        CuteMixin._valueOf(from_), CuteMixin._valueOf(to),
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS, float)
  def slerp(q1: QQuaternion, q2: QQuaternion, t: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::slerp(const QQuaternion &q1, const
    QQuaternion &q2, float t)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#slerp

    Parameters
    ----------

    q1 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    q2 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    t : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::slerp(const QQuaternion &q1, const
    #      QQuaternion &q2, float t)
    address = Rituals.call(
        'ritual_ZN11QQuaternion5slerpERKS_S1_f',
        CuteMixin._valueOf(q1), CuteMixin._valueOf(q2), t,
    )
    return QQuaternion._cuteOwning(address)

  @staticmethod
  @overload(THIS, THIS, float)
  def nlerp(q1: QQuaternion, q2: QQuaternion, t: float) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::nlerp(const QQuaternion &q1, const
    QQuaternion &q2, float t)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#nlerp

    Parameters
    ----------

    q1 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    q2 : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.

    t : float
      Passed on as it is.

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::nlerp(const QQuaternion &q1, const
    #      QQuaternion &q2, float t)
    address = Rituals.call(
        'ritual_ZN11QQuaternion5nlerpERKS_S1_f',
        CuteMixin._valueOf(q1), CuteMixin._valueOf(q2), t,
    )
    return QQuaternion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuaternion'

  #  Qt's '~QQuaternion()'. Naming it makes this a value class: Python owns
  #  every C++ QQuaternion behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QQuaternionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQuaternion::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#isNull
    """
    #  bool QQuaternion::isNull() const
    return self.uglySide.call('ritual_ZNK11QQuaternion6isNullEv')

  def isIdentity(self) -> bool:
    """
    Calls Qt's 'bool QQuaternion::isIdentity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#isIdentity
    """
    #  bool QQuaternion::isIdentity() const
    return self.uglySide.call('ritual_ZNK11QQuaternion10isIdentityEv')

  def vector(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuaternion::vector() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#vector

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuaternion::vector() const
    address = self.uglySide.call('ritual_ZNK11QQuaternion6vectorEv')
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  def x(self) -> float:
    """
    Calls Qt's 'float QQuaternion::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#x
    """
    #  float QQuaternion::x() const
    return self.uglySide.call('ritual_ZNK11QQuaternion1xEv')

  def y(self) -> float:
    """
    Calls Qt's 'float QQuaternion::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#y
    """
    #  float QQuaternion::y() const
    return self.uglySide.call('ritual_ZNK11QQuaternion1yEv')

  def z(self) -> float:
    """
    Calls Qt's 'float QQuaternion::z() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#z
    """
    #  float QQuaternion::z() const
    return self.uglySide.call('ritual_ZNK11QQuaternion1zEv')

  def scalar(self) -> float:
    """
    Calls Qt's 'float QQuaternion::scalar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#scalar
    """
    #  float QQuaternion::scalar() const
    return self.uglySide.call('ritual_ZNK11QQuaternion6scalarEv')

  def length(self) -> float:
    """
    Calls Qt's 'float QQuaternion::length() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#length
    """
    #  float QQuaternion::length() const
    return self.uglySide.call('ritual_ZNK11QQuaternion6lengthEv')

  def lengthSquared(self) -> float:
    """
    Calls Qt's 'float QQuaternion::lengthSquared() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#lengthSquared
    """
    #  float QQuaternion::lengthSquared() const
    return self.uglySide.call('ritual_ZNK11QQuaternion13lengthSquaredEv')

  def normalized(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::normalized() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#normalized

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::normalized() const
    address = self.uglySide.call('ritual_ZNK11QQuaternion10normalizedEv')
    return QQuaternion._cuteOwning(address)

  def inverted(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::inverted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#inverted

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::inverted() const
    address = self.uglySide.call('ritual_ZNK11QQuaternion8invertedEv')
    return QQuaternion._cuteOwning(address)

  def conjugated(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QQuaternion::conjugated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#conjugated

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QQuaternion::conjugated() const
    address = self.uglySide.call('ritual_ZNK11QQuaternion10conjugatedEv')
    return QQuaternion._cuteOwning(address)

  @overload(QVector3D)
  def rotatedVector(self, vector: QVector3D) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuaternion::rotatedVector(const QVector3D &vector)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#rotatedVector

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuaternion::rotatedVector(const QVector3D &vector) const
    address = self.uglySide.call(
        'ritual_ZNK11QQuaternion13rotatedVectorERK9QVector3D',
        self._valueOf(vector),
    )
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  def toVector4D(self) -> QVector4D:
    """
    Calls Qt's 'QVector4D QQuaternion::toVector4D() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#toVector4D

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  QVector4D QQuaternion::toVector4D() const
    address = self.uglySide.call('ritual_ZNK11QQuaternion10toVector4DEv')
    from . import QVector4D
    return QVector4D._cuteOwning(address)

  def toEulerAngles(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QQuaternion::toEulerAngles() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#toEulerAngles

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QQuaternion::toEulerAngles() const
    address = self.uglySide.call('ritual_ZNK11QQuaternion13toEulerAnglesEv')
    from . import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setVector(self, vector: QVector3D) -> None:
    """
    Calls Qt's 'void QQuaternion::setVector(const QVector3D &vector)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#setVector

    Parameters
    ----------

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QQuaternion::setVector(const QVector3D &vector)
    self.uglySide.call(
        'ritual_ZN11QQuaternion9setVectorERK9QVector3D',
        self._valueOf(vector),
    )

  @overload(float, float, float)
  def setVector(self, x: float, y: float, z: float) -> None:
    """
    Calls Qt's 'void QQuaternion::setVector(float x, float y, float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#setVector

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    z : float
      Passed on as it is.
    """
    #  void QQuaternion::setVector(float x, float y, float z)
    self.uglySide.call('ritual_ZN11QQuaternion9setVectorEfff', x, y, z)

  @overload(float)
  def setX(self, x: float) -> None:
    """
    Calls Qt's 'void QQuaternion::setX(float x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#setX

    Parameters
    ----------

    x : float
      Passed on as it is.
    """
    #  void QQuaternion::setX(float x)
    self.uglySide.call('ritual_ZN11QQuaternion4setXEf', x)

  @overload(float)
  def setY(self, y: float) -> None:
    """
    Calls Qt's 'void QQuaternion::setY(float y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#setY

    Parameters
    ----------

    y : float
      Passed on as it is.
    """
    #  void QQuaternion::setY(float y)
    self.uglySide.call('ritual_ZN11QQuaternion4setYEf', y)

  @overload(float)
  def setZ(self, z: float) -> None:
    """
    Calls Qt's 'void QQuaternion::setZ(float z)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#setZ

    Parameters
    ----------

    z : float
      Passed on as it is.
    """
    #  void QQuaternion::setZ(float z)
    self.uglySide.call('ritual_ZN11QQuaternion4setZEf', z)

  @overload(float)
  def setScalar(self, scalar: float) -> None:
    """
    Calls Qt's 'void QQuaternion::setScalar(float scalar)'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#setScalar

    Parameters
    ----------

    scalar : float
      Passed on as it is.
    """
    #  void QQuaternion::setScalar(float scalar)
    self.uglySide.call('ritual_ZN11QQuaternion9setScalarEf', scalar)

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
    Notes what was given, for Qt's 'QQuaternion::QQuaternion()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#QQuaternion
    """
    #  QQuaternion::QQuaternion()
    self._noteCreation(QQuaternion, lambda: Rituals.call(
        'ritual_ZN11QQuaternionC1Ev',
    ))

  @overload(Qt.Initialization)
  def __init__(self, a0: Qt.Initialization) -> None:
    """
    Notes what was given, for Qt's
    'QQuaternion::QQuaternion(Qt::Initialization a0)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#QQuaternion

    Parameters
    ----------

    a0 : Qt.Initialization
      Passed on as its number.
    """
    #  QQuaternion::QQuaternion(Qt::Initialization a0)
    self._noteCreation(QQuaternion, lambda: Rituals.call(
        'ritual_ZN11QQuaternionC1EN2Qt14InitializationE', a0.value,
    ))

  @overload(float, float, float, float)
  def __init__(
      self,
      scalar: float,
      xpos: float,
      ypos: float,
      zpos: float,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQuaternion::QQuaternion(float scalar,
    float xpos, float ypos, float zpos)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#QQuaternion

    Parameters
    ----------

    scalar : float
      Passed on as it is.

    xpos : float
      Passed on as it is.

    ypos : float
      Passed on as it is.

    zpos : float
      Passed on as it is.
    """
    #  QQuaternion::QQuaternion(float scalar, float xpos, float ypos, float
    #      zpos)
    self._noteCreation(QQuaternion, lambda: Rituals.call(
        'ritual_ZN11QQuaternionC1Effff', scalar, xpos, ypos, zpos,
    ))

  @overload(float, QVector3D)
  def __init__(self, scalar: float, vector: QVector3D) -> None:
    """
    Notes what was given, for Qt's 'QQuaternion::QQuaternion(float scalar,
    const QVector3D &vector)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#QQuaternion

    Parameters
    ----------

    scalar : float
      Passed on as it is.

    vector : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  QQuaternion::QQuaternion(float scalar, const QVector3D &vector)
    self._noteCreation(QQuaternion, lambda: Rituals.call(
        'ritual_ZN11QQuaternionC1EfRK9QVector3D',
        scalar, self._valueOf(vector),
    ))

  @overload(QVector4D)
  def __init__(self, vector: QVector4D) -> None:
    """
    Notes what was given, for Qt's 'QQuaternion::QQuaternion(const QVector4D
    &vector)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#QQuaternion

    Parameters
    ----------

    vector : QVector4D
      Passed on as a value: Qt reads the C++ QVector4D, which stays Python's
      own.
    """
    #  QQuaternion::QQuaternion(const QVector4D &vector)
    self._noteCreation(QQuaternion, lambda: Rituals.call(
        'ritual_ZN11QQuaternionC1ERK9QVector4D', self._valueOf(vector),
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

  def normalize(self) -> None:
    """
    Calls Qt's 'void QQuaternion::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#normalize
    """
    #  void QQuaternion::normalize()
    self.uglySide.call('ritual_ZN11QQuaternion9normalizeEv')

  @overload(QVector3D, QVector3D, QVector3D)
  @overload(QVector3D, QVector3D, NoneType)
  @overload(QVector3D, NoneType, QVector3D)
  @overload(QVector3D, NoneType, NoneType)
  @overload(NoneType, QVector3D, QVector3D)
  @overload(NoneType, QVector3D, NoneType)
  @overload(NoneType, NoneType, QVector3D)
  @overload(NoneType, NoneType, NoneType)
  def getAxes(
      self,
      xAxis: Optional[QVector3D],
      yAxis: Optional[QVector3D],
      zAxis: Optional[QVector3D],
  ) -> None:
    """
    Calls Qt's 'void QQuaternion::getAxes(QVector3D *xAxis, QVector3D *yAxis,
    QVector3D *zAxis) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquaternion.html#getAxes

    Parameters
    ----------

    xAxis : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    yAxis : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    zAxis : Optional[QVector3D]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuaternion::getAxes(QVector3D *xAxis, QVector3D *yAxis,
    #      QVector3D *zAxis) const
    self.uglySide.call(
        'ritual_ZNK11QQuaternion7getAxesEP9QVector3DS1_S1_',
        self._addressOf(xAxis), self._addressOf(yAxis),
        self._addressOf(zAxis),
    )
