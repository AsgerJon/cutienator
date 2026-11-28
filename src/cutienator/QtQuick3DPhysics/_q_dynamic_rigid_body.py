"""
QDynamicRigidBody binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qdynamicrigidbody_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDynamicRigidBody to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QAbstractPhysicsBody

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDynamicRigidBody(QAbstractPhysicsBody):
  """
  The cute side of Qt's QDynamicRigidBody: a plain Python object standing in
  front of one C++ QDynamicRigidBody.

  It is built on the cute 'QAbstractPhysicsBody', as Qt's QDynamicRigidBody
  is built on Qt's QAbstractPhysicsBody, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDynamicRigidBody that has a ritual and that Python
  can call so far, 57 names in all: 'metaObject', 'tr', 'mass', 'setMass',
  'density', 'setDensity', 'isKinematic', 'setIsKinematic', 'linearAxisLock',
  'setLinearAxisLock', 'angularAxisLock', 'setAngularAxisLock',
  'gravityEnabled', 'setGravityEnabled', 'applyCentralForce', 'applyForce',
  'applyTorque', 'applyCentralImpulse', 'applyImpulse', 'applyTorqueImpulse',
  'setAngularVelocity', 'setLinearVelocity', 'reset', 'updateDefaultDensity',
  'massMode', 'inertiaTensor', 'setInertiaTensor', 'centerOfMassPosition',
  'setCenterOfMassPosition', 'centerOfMassRotation',
  'setCenterOfMassRotation', 'setKinematicPosition', 'kinematicPosition',
  'setKinematicRotation', 'kinematicRotation', 'setKinematicEulerRotation',
  'kinematicEulerRotation', 'setKinematicPivot', 'kinematicPivot',
  'setIsSleeping', 'isSleeping', 'massChanged', 'densityChanged',
  'isKinematicChanged', 'linearAxisLockChanged', 'angularAxisLockChanged',
  'gravityEnabledChanged', 'massModeChanged', 'inertiaTensorChanged',
  'centerOfMassPositionChanged', 'centerOfMassRotationChanged',
  'inertiaMatrixChanged', 'kinematicPositionChanged',
  'kinematicRotationChanged', 'kinematicEulerRotationChanged',
  'kinematicPivotChanged', 'isSleepingChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDynamicRigidBody::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDynamicRigidBody::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDynamicRigidBody::~QDynamicRigidBody()': the destructor: Python
    never removes a C++ QDynamicRigidBody.
  - Qt's 'QQueue<QPhysicsCommand *> &QDynamicRigidBody::commandQueue()':
    gives a type Python has no way to take yet.
  - Qt's 'void QDynamicRigidBody::setMassMode(const MassMode newMassMode)':
    takes a type Python has no way to hand over yet.
  - Qt's 'const QList<float> &QDynamicRigidBody::readInertiaMatrix() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QDynamicRigidBody::setInertiaMatrix(const QList<float>
    &newInertiaMatrix)': takes a type Python has no way to hand over yet.
  - Qt's 'const QMatrix3x3 &QDynamicRigidBody::inertiaMatrix() const': gives
    a type Python has no way to take yet.
  - Qt's 'QAbstractPhysXNode *QDynamicRigidBody::createPhysXBackend()': gives
    'QAbstractPhysXNode', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 69 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDynamicRigidBody is created at the first use, not by
    'QDynamicRigidBody(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDynamicRigidBody.
  - Qt tells when it has removed the C++ QDynamicRigidBody. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDynamicRigidBody that has no cute function yet,
    'commandQueue', 'inertiaMatrix', 'readInertiaMatrix', 'setInertiaMatrix',
    'setMassMode', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QDynamicRigidBody, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AxisLock(CuteNum):
    """
    The enum 'QDynamicRigidBody::AxisLock' of Qt, with the 4 names Qt gives
    in it.
    """

    LockNone = Kee[int](0)
    LockX = Kee[int](1)
    LockY = Kee[int](2)
    LockZ = Kee[int](4)

  class MassMode(CuteNum, scoped=True):
    """
    The enum 'QDynamicRigidBody::MassMode' of Qt, with the 5 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    DefaultDensity = Kee[int](0)
    CustomDensity = Kee[int](1)
    Mass = Kee[int](2)
    MassAndInertiaTensor = Kee[int](3)
    MassAndInertiaMatrix = Kee[int](4)

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
    Calls Qt's 'QString QDynamicRigidBody::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#tr

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
    #  QString QDynamicRigidBody::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QDynamicRigidBody2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDynamicRigidBody'

  #  A C++ QDynamicRigidBody Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDynamicRigidBody'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDynamicRigidBody::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDynamicRigidBody::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mass(self) -> float:
    """
    Calls Qt's 'float QDynamicRigidBody::mass() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#mass
    """
    #  float QDynamicRigidBody::mass() const
    return self.uglySide.call('ritual_ZNK17QDynamicRigidBody4massEv')

  def density(self) -> float:
    """
    Calls Qt's 'float QDynamicRigidBody::density() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#density
    """
    #  float QDynamicRigidBody::density() const
    return self.uglySide.call('ritual_ZNK17QDynamicRigidBody7densityEv')

  def isKinematic(self) -> bool:
    """
    Calls Qt's 'bool QDynamicRigidBody::isKinematic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#isKinematic
    """
    #  bool QDynamicRigidBody::isKinematic() const
    return self.uglySide.call('ritual_ZNK17QDynamicRigidBody11isKinematicEv')

  def linearAxisLock(self) -> AxisLock:
    """
    Calls Qt's 'AxisLock QDynamicRigidBody::linearAxisLock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#linearAxisLock

    Returns
    -------

    AxisLock
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AxisLock(number)' gives.
    """
    #  AxisLock QDynamicRigidBody::linearAxisLock() const
    return QDynamicRigidBody.AxisLock(self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody14linearAxisLockEv',
    ))

  def angularAxisLock(self) -> AxisLock:
    """
    Calls Qt's 'AxisLock QDynamicRigidBody::angularAxisLock() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#angularAxisLock

    Returns
    -------

    AxisLock
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'AxisLock(number)' gives.
    """
    #  AxisLock QDynamicRigidBody::angularAxisLock() const
    return QDynamicRigidBody.AxisLock(self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody15angularAxisLockEv',
    ))

  def gravityEnabled(self) -> bool:
    """
    Calls Qt's 'bool QDynamicRigidBody::gravityEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#gravityEnabled
    """
    #  bool QDynamicRigidBody::gravityEnabled() const
    return self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody14gravityEnabledEv',
    )

  def massMode(self) -> MassMode:
    """
    Calls Qt's 'MassMode QDynamicRigidBody::massMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#massMode

    Returns
    -------

    MassMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'MassMode(number)' gives.
    """
    #  MassMode QDynamicRigidBody::massMode() const
    return QDynamicRigidBody.MassMode(self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody8massModeEv',
    ))

  def inertiaTensor(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QDynamicRigidBody::inertiaTensor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#inertiaTensor

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QDynamicRigidBody::inertiaTensor() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody13inertiaTensorEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def centerOfMassPosition(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QDynamicRigidBody::centerOfMassPosition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#centerOfMassPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QDynamicRigidBody::centerOfMassPosition() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody20centerOfMassPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def centerOfMassRotation(self) -> QQuaternion:
    """
    Calls Qt's 'const QQuaternion &QDynamicRigidBody::centerOfMassRotation()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#centerOfMassRotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  const QQuaternion &QDynamicRigidBody::centerOfMassRotation() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody20centerOfMassRotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def kinematicPosition(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QDynamicRigidBody::kinematicPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicPosition

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QDynamicRigidBody::kinematicPosition() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody17kinematicPositionEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def kinematicRotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QDynamicRigidBody::kinematicRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicRotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QDynamicRigidBody::kinematicRotation() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody17kinematicRotationEv',
    )
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def kinematicEulerRotation(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QDynamicRigidBody::kinematicEulerRotation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicEulerRotation

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QDynamicRigidBody::kinematicEulerRotation() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody22kinematicEulerRotationEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def kinematicPivot(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QDynamicRigidBody::kinematicPivot() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicPivot

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QDynamicRigidBody::kinematicPivot() const
    address = self.uglySide.call(
        'ritual_ZNK17QDynamicRigidBody14kinematicPivotEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def isSleeping(self) -> bool:
    """
    Calls Qt's 'bool QDynamicRigidBody::isSleeping() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#isSleeping
    """
    #  bool QDynamicRigidBody::isSleeping() const
    return self.uglySide.call('ritual_ZNK17QDynamicRigidBody10isSleepingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setMass(self, mass: float) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setMass(float mass)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#setMass

    Parameters
    ----------

    mass : float
      Passed on as it is.
    """
    #  void QDynamicRigidBody::setMass(float mass)
    self.uglySide.call('ritual_ZN17QDynamicRigidBody7setMassEf', mass)

  @overload(float)
  def setDensity(self, density: float) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setDensity(float density)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#setDensity

    Parameters
    ----------

    density : float
      Passed on as it is.
    """
    #  void QDynamicRigidBody::setDensity(float density)
    self.uglySide.call('ritual_ZN17QDynamicRigidBody10setDensityEf', density)

  @overload(bool)
  def setIsKinematic(self, isKinematic: bool) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setIsKinematic(bool isKinematic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setIsKinematic

    Parameters
    ----------

    isKinematic : bool
      Passed on as it is.
    """
    #  void QDynamicRigidBody::setIsKinematic(bool isKinematic)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody14setIsKinematicEb', isKinematic,
    )

  @overload(AxisLock)
  def setLinearAxisLock(self, newAxisLockLinear: AxisLock) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setLinearAxisLock(AxisLock
    newAxisLockLinear)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setLinearAxisLock

    Parameters
    ----------

    newAxisLockLinear : AxisLock
      Passed on as its number.
    """
    #  void QDynamicRigidBody::setLinearAxisLock(AxisLock newAxisLockLinear)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody17setLinearAxisLockENS_8AxisLockE',
        newAxisLockLinear.value,
    )

  @overload(AxisLock)
  def setAngularAxisLock(self, newAxisLockAngular: AxisLock) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setAngularAxisLock(AxisLock
    newAxisLockAngular)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setAngularAxisLock

    Parameters
    ----------

    newAxisLockAngular : AxisLock
      Passed on as its number.
    """
    #  void QDynamicRigidBody::setAngularAxisLock(AxisLock
    #      newAxisLockAngular)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody18setAngularAxisLockENS_8AxisLockE',
        newAxisLockAngular.value,
    )

  @overload(bool)
  def setGravityEnabled(self, gravityEnabled: bool) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setGravityEnabled(bool
    gravityEnabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setGravityEnabled

    Parameters
    ----------

    gravityEnabled : bool
      Passed on as it is.
    """
    #  void QDynamicRigidBody::setGravityEnabled(bool gravityEnabled)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody17setGravityEnabledEb', gravityEnabled,
    )

  @overload(QVector3D)
  def setAngularVelocity(self, angularVelocity: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setAngularVelocity(const QVector3D
    &angularVelocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setAngularVelocity

    Parameters
    ----------

    angularVelocity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setAngularVelocity(const QVector3D
    #      &angularVelocity)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody18setAngularVelocityERK9QVector3D',
        self._valueOf(angularVelocity),
    )

  @overload(QVector3D)
  def setLinearVelocity(self, linearVelocity: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setLinearVelocity(const QVector3D
    &linearVelocity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setLinearVelocity

    Parameters
    ----------

    linearVelocity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setLinearVelocity(const QVector3D
    #      &linearVelocity)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody17setLinearVelocityERK9QVector3D',
        self._valueOf(linearVelocity),
    )

  @overload(QVector3D)
  def setInertiaTensor(self, newInertiaTensor: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setInertiaTensor(const QVector3D
    &newInertiaTensor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setInertiaTensor

    Parameters
    ----------

    newInertiaTensor : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setInertiaTensor(const QVector3D
    #      &newInertiaTensor)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody16setInertiaTensorERK9QVector3D',
        self._valueOf(newInertiaTensor),
    )

  @overload(QVector3D)
  def setCenterOfMassPosition(
      self,
      newCenterOfMassPosition: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setCenterOfMassPosition(const
    QVector3D &newCenterOfMassPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setCenterOfMassPosition

    Parameters
    ----------

    newCenterOfMassPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setCenterOfMassPosition(const QVector3D
    #      &newCenterOfMassPosition)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody23setCenterOfMassPositionERK9QVector3D',
        self._valueOf(newCenterOfMassPosition),
    )

  @overload(QQuaternion)
  def setCenterOfMassRotation(
      self,
      newCenterOfMassRotation: QQuaternion,
  ) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setCenterOfMassRotation(const
    QQuaternion &newCenterOfMassRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setCenterOfMassRotation

    Parameters
    ----------

    newCenterOfMassRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QDynamicRigidBody::setCenterOfMassRotation(const QQuaternion
    #      &newCenterOfMassRotation)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody23setCenterOfMassRotationERK11QQuatern'
        'ion',
        self._valueOf(newCenterOfMassRotation),
    )

  @overload(QVector3D)
  def setKinematicPosition(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setKinematicPosition(const QVector3D
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setKinematicPosition

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setKinematicPosition(const QVector3D
    #      &position)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody20setKinematicPositionERK9QVector3D',
        self._valueOf(position),
    )

  @overload(QQuaternion)
  def setKinematicRotation(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setKinematicRotation(const
    QQuaternion &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setKinematicRotation

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QDynamicRigidBody::setKinematicRotation(const QQuaternion
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody20setKinematicRotationERK11QQuaternion',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def setKinematicEulerRotation(self, rotation: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setKinematicEulerRotation(const
    QVector3D &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setKinematicEulerRotation

    Parameters
    ----------

    rotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setKinematicEulerRotation(const QVector3D
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody25setKinematicEulerRotationERK9QVector'
        '3D',
        self._valueOf(rotation),
    )

  @overload(QVector3D)
  def setKinematicPivot(self, pivot: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setKinematicPivot(const QVector3D
    &pivot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setKinematicPivot

    Parameters
    ----------

    pivot : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::setKinematicPivot(const QVector3D &pivot)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody17setKinematicPivotERK9QVector3D',
        self._valueOf(pivot),
    )

  @overload(bool)
  def setIsSleeping(self, newIsSleeping: bool) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::setIsSleeping(bool newIsSleeping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#setIsSleeping

    Parameters
    ----------

    newIsSleeping : bool
      Passed on as it is.
    """
    #  void QDynamicRigidBody::setIsSleeping(bool newIsSleeping)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody13setIsSleepingEb', newIsSleeping,
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
    Notes what was given, for Qt's 'QDynamicRigidBody::QDynamicRigidBody()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#QDynamicRigidBody
    """
    #  QDynamicRigidBody::QDynamicRigidBody()
    self._noteCreation(QDynamicRigidBody, lambda: Rituals.call(
        'ritual_ZN17QDynamicRigidBodyC1Ev',
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

  @overload(QVector3D)
  def applyCentralForce(self, force: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::applyCentralForce(const QVector3D
    &force)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#applyCentralForce

    Parameters
    ----------

    force : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::applyCentralForce(const QVector3D &force)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody17applyCentralForceERK9QVector3D',
        self._valueOf(force),
    )

  @overload(QVector3D, QVector3D)
  def applyForce(self, force: QVector3D, position: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::applyForce(const QVector3D &force,
    const QVector3D &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#applyForce

    Parameters
    ----------

    force : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::applyForce(const QVector3D &force, const
    #      QVector3D &position)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody10applyForceERK9QVector3DS2_',
        self._valueOf(force), self._valueOf(position),
    )

  @overload(QVector3D)
  def applyTorque(self, torque: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::applyTorque(const QVector3D
    &torque)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#applyTorque

    Parameters
    ----------

    torque : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::applyTorque(const QVector3D &torque)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody11applyTorqueERK9QVector3D',
        self._valueOf(torque),
    )

  @overload(QVector3D)
  def applyCentralImpulse(self, impulse: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::applyCentralImpulse(const QVector3D
    &impulse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#applyCentralImpulse

    Parameters
    ----------

    impulse : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::applyCentralImpulse(const QVector3D &impulse)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody19applyCentralImpulseERK9QVector3D',
        self._valueOf(impulse),
    )

  @overload(QVector3D, QVector3D)
  def applyImpulse(self, impulse: QVector3D, position: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::applyImpulse(const QVector3D
    &impulse, const QVector3D &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#applyImpulse

    Parameters
    ----------

    impulse : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::applyImpulse(const QVector3D &impulse, const
    #      QVector3D &position)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody12applyImpulseERK9QVector3DS2_',
        self._valueOf(impulse), self._valueOf(position),
    )

  @overload(QVector3D)
  def applyTorqueImpulse(self, impulse: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::applyTorqueImpulse(const QVector3D
    &impulse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#applyTorqueImpulse

    Parameters
    ----------

    impulse : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::applyTorqueImpulse(const QVector3D &impulse)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody18applyTorqueImpulseERK9QVector3D',
        self._valueOf(impulse),
    )

  @overload(QVector3D, QVector3D)
  def reset(self, position: QVector3D, eulerRotation: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::reset(const QVector3D &position,
    const QVector3D &eulerRotation)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#reset

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    eulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::reset(const QVector3D &position, const
    #      QVector3D &eulerRotation)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody5resetERK9QVector3DS2_',
        self._valueOf(position), self._valueOf(eulerRotation),
    )

  @overload(float)
  def updateDefaultDensity(self, defaultDensity: float) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::updateDefaultDensity(float
    defaultDensity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#updateDefaultDensity

    Parameters
    ----------

    defaultDensity : float
      Passed on as it is.
    """
    #  void QDynamicRigidBody::updateDefaultDensity(float defaultDensity)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody20updateDefaultDensityEf',
        defaultDensity,
    )

  @overload(float)
  def massChanged(self, mass: float) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::massChanged(float mass)'.

    Qt's own words: https://doc.qt.io/qt-6/qdynamicrigidbody.html#massChanged

    Parameters
    ----------

    mass : float
      Passed on as it is.
    """
    #  void QDynamicRigidBody::massChanged(float mass)
    self.uglySide.call('ritual_ZN17QDynamicRigidBody11massChangedEf', mass)

  @overload(float)
  def densityChanged(self, density: float) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::densityChanged(float density)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#densityChanged

    Parameters
    ----------

    density : float
      Passed on as it is.
    """
    #  void QDynamicRigidBody::densityChanged(float density)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody14densityChangedEf', density,
    )

  @overload(bool)
  def isKinematicChanged(self, isKinematic: bool) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::isKinematicChanged(bool
    isKinematic)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#isKinematicChanged

    Parameters
    ----------

    isKinematic : bool
      Passed on as it is.
    """
    #  void QDynamicRigidBody::isKinematicChanged(bool isKinematic)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody18isKinematicChangedEb', isKinematic,
    )

  def linearAxisLockChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::linearAxisLockChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#linearAxisLockChanged
    """
    #  void QDynamicRigidBody::linearAxisLockChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody21linearAxisLockChangedEv',
    )

  def angularAxisLockChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::angularAxisLockChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#angularAxisLockChanged
    """
    #  void QDynamicRigidBody::angularAxisLockChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody22angularAxisLockChangedEv',
    )

  def gravityEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::gravityEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#gravityEnabledChanged
    """
    #  void QDynamicRigidBody::gravityEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody21gravityEnabledChangedEv',
    )

  def massModeChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::massModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#massModeChanged
    """
    #  void QDynamicRigidBody::massModeChanged()
    self.uglySide.call('ritual_ZN17QDynamicRigidBody15massModeChangedEv')

  def inertiaTensorChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::inertiaTensorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#inertiaTensorChanged
    """
    #  void QDynamicRigidBody::inertiaTensorChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody20inertiaTensorChangedEv',
    )

  def centerOfMassPositionChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::centerOfMassPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#centerOfMassPositionChanged
    """
    #  void QDynamicRigidBody::centerOfMassPositionChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody27centerOfMassPositionChangedEv',
    )

  def centerOfMassRotationChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::centerOfMassRotationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#centerOfMassRotationChanged
    """
    #  void QDynamicRigidBody::centerOfMassRotationChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody27centerOfMassRotationChangedEv',
    )

  def inertiaMatrixChanged(self) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::inertiaMatrixChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#inertiaMatrixChanged
    """
    #  void QDynamicRigidBody::inertiaMatrixChanged()
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody20inertiaMatrixChangedEv',
    )

  @overload(QVector3D)
  def kinematicPositionChanged(self, kinematicPosition: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::kinematicPositionChanged(const
    QVector3D &kinematicPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicPositionChanged

    Parameters
    ----------

    kinematicPosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::kinematicPositionChanged(const QVector3D
    #      &kinematicPosition)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody24kinematicPositionChangedERK9QVector3'
        'D',
        self._valueOf(kinematicPosition),
    )

  @overload(QQuaternion)
  def kinematicRotationChanged(self, kinematicRotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::kinematicRotationChanged(const
    QQuaternion &kinematicRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicRotationChanged

    Parameters
    ----------

    kinematicRotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QDynamicRigidBody::kinematicRotationChanged(const QQuaternion
    #      &kinematicRotation)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody24kinematicRotationChangedERK11QQuater'
        'nion',
        self._valueOf(kinematicRotation),
    )

  @overload(QVector3D)
  def kinematicEulerRotationChanged(
      self,
      kinematicEulerRotation: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::kinematicEulerRotationChanged(const
    QVector3D &kinematicEulerRotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html

    Parameters
    ----------

    kinematicEulerRotation : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::kinematicEulerRotationChanged(const QVector3D
    #      &kinematicEulerRotation)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody29kinematicEulerRotationChangedERK9QVe'
        'ctor3D',
        self._valueOf(kinematicEulerRotation),
    )

  @overload(QVector3D)
  def kinematicPivotChanged(self, kinematicPivot: QVector3D) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::kinematicPivotChanged(const QVector3D
    &kinematicPivot)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#kinematicPivotChanged

    Parameters
    ----------

    kinematicPivot : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QDynamicRigidBody::kinematicPivotChanged(const QVector3D
    #      &kinematicPivot)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody21kinematicPivotChangedERK9QVector3D',
        self._valueOf(kinematicPivot),
    )

  @overload(bool)
  def isSleepingChanged(self, isSleeping: bool) -> None:
    """
    Calls Qt's 'void QDynamicRigidBody::isSleepingChanged(bool isSleeping)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdynamicrigidbody.html#isSleepingChanged

    Parameters
    ----------

    isSleeping : bool
      Passed on as it is.
    """
    #  void QDynamicRigidBody::isSleepingChanged(bool isSleeping)
    self.uglySide.call(
        'ritual_ZN17QDynamicRigidBody17isSleepingChangedEb', isSleeping,
    )

  @staticmethod
  def commandQueue(*__, **_) -> Never:
    """
    Qt's 'QQueue<QPhysicsCommand *> &QDynamicRigidBody::commandQueue()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDynamicRigidBody.commandQueue' has no cute function yet. Qt's "
        "'QQueue<QPhysicsCommand *> &QDynamicRigidBody::commandQueue()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def inertiaMatrix(*__, **_) -> Never:
    """
    Qt's 'const QMatrix3x3 &QDynamicRigidBody::inertiaMatrix() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDynamicRigidBody.inertiaMatrix' has no cute function yet. Qt's "
        "'const QMatrix3x3 &QDynamicRigidBody::inertiaMatrix() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def readInertiaMatrix(*__, **_) -> Never:
    """
    Qt's 'const QList<float> &QDynamicRigidBody::readInertiaMatrix() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QDynamicRigidBody.readInertiaMatrix' has no cute function yet. "
        "Qt's 'const QList<float> &QDynamicRigidBody::readInertiaMatrix() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setInertiaMatrix(*__, **_) -> Never:
    """
    Qt's 'void QDynamicRigidBody::setInertiaMatrix(const QList<float>
    &newInertiaMatrix)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDynamicRigidBody.setInertiaMatrix' has no cute function yet. "
        "Qt's 'void QDynamicRigidBody::setInertiaMatrix(const QList<float> "
        "&newInertiaMatrix)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def setMassMode(*__, **_) -> Never:
    """
    Qt's 'void QDynamicRigidBody::setMassMode(const MassMode newMassMode)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDynamicRigidBody.setMassMode' has no cute function yet. Qt's "
        "'void QDynamicRigidBody::setMassMode(const MassMode newMassMode)': "
        "takes a type Python has no way to hand over yet.")
