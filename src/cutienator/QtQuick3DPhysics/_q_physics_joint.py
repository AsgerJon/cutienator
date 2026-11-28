"""
QPhysicsJoint binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qjoint_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPhysicsJoint to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QQuaternion, QVector3D
  from . import QAbstractPhysicsBody
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractPhysicsBody = WAIT['QAbstractPhysicsBody']
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPhysicsJoint(QObject):
  """
  The cute side of Qt's QPhysicsJoint: a plain Python object standing in
  front of one C++ QPhysicsJoint.

  It is built on the cute 'QObject', as Qt's QPhysicsJoint is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPhysicsJoint that has a ritual and that Python can
  call so far, 23 names in all: 'metaObject', 'tr', 'bodyA', 'setBodyA',
  'bodyB', 'setBodyB', 'positionA', 'setPositionA', 'positionB',
  'setPositionB', 'orientationA', 'setOrientationA', 'orientationB',
  'setOrientationB', 'updatePhysXBackend', 'bodyAChanged', 'bodyBChanged',
  'positionAChanged', 'positionBChanged', 'orientationAChanged',
  'orientationBChanged', 'setJointProperties', 'onBodyDestroyed'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPhysicsJoint::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPhysicsJoint::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QPhysicsJoint::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QPhysicsJoint::~QPhysicsJoint()': the destructor: Python never
    removes a C++ QPhysicsJoint.
  - Qt's 'physx::PxJoint *QPhysicsJoint::getPhysXBackend() const': gives
    'physx::PxJoint', which has no cute class yet.
  - Qt's 'physx::PxJoint *QPhysicsJoint::createPhysxJoint(physx::PxRigidActor
    *actorA, physx::PxRigidActor *actorB, const physx::PxTransform &trfA,
    const physx::PxTransform &trfB)': names 'physx::PxRigidActor', which has
    no cute class yet.

  What has no ritual
  ------------------

  3 of the 32 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QPhysicsJoint is created at the first use, not by
    'QPhysicsJoint(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPhysicsJoint.
  - Qt tells when it has removed the C++ QPhysicsJoint. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPhysicsJoint that has no cute function yet,
    '__init__', 'createPhysxJoint', 'getPhysXBackend', holds a function that
    raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QPhysicsJoint::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#tr

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
    #  QString QPhysicsJoint::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPhysicsJoint2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPhysicsJoint'

  #  A C++ QPhysicsJoint Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPhysicsJoint'

  #  The functions Qt calls itself that QPhysicsJoint is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'createPhysxJoint': (
          'physx::PxJoint '
          '*QPhysicsJoint::createPhysxJoint(physx::PxRigidActor *, '
          'physx::PxRigidActor *, const physx::PxTransform &, const '
          'physx::PxTransform &)',
      ),
  }

  #  The functions Qt calls itself that QPhysicsJoint is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'setJointProperties': (
          ('_ZN13QPhysicsJoint18setJointPropertiesEv',
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
    Calls Qt's 'const QMetaObject *QPhysicsJoint::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPhysicsJoint::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bodyA(self) -> Optional[QAbstractPhysicsBody]:
    """
    Calls Qt's 'QAbstractPhysicsBody *QPhysicsJoint::bodyA() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#bodyA

    Returns
    -------

    Optional[QAbstractPhysicsBody]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicsBody *QPhysicsJoint::bodyA() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint5bodyAEv')
    from . import QAbstractPhysicsBody
    return QAbstractPhysicsBody._cuteAt(address)

  def bodyB(self) -> Optional[QAbstractPhysicsBody]:
    """
    Calls Qt's 'QAbstractPhysicsBody *QPhysicsJoint::bodyB() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#bodyB

    Returns
    -------

    Optional[QAbstractPhysicsBody]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPhysicsBody *QPhysicsJoint::bodyB() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint5bodyBEv')
    from . import QAbstractPhysicsBody
    return QAbstractPhysicsBody._cuteAt(address)

  def positionA(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QPhysicsJoint::positionA() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#positionA

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QPhysicsJoint::positionA() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint9positionAEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def positionB(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QPhysicsJoint::positionB() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#positionB

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QPhysicsJoint::positionB() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint9positionBEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def orientationA(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QPhysicsJoint::orientationA() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#orientationA

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QPhysicsJoint::orientationA() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint12orientationAEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def orientationB(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QPhysicsJoint::orientationB() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#orientationB

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QPhysicsJoint::orientationB() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsJoint12orientationBEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractPhysicsBody)
  @overload(NoneType)
  def setBodyA(self, newBodyA: Optional[QAbstractPhysicsBody]) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setBodyA(QAbstractPhysicsBody
    *newBodyA)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#setBodyA

    Parameters
    ----------

    newBodyA : Optional[QAbstractPhysicsBody]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsJoint::setBodyA(QAbstractPhysicsBody *newBodyA)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint8setBodyAEP20QAbstractPhysicsBody',
        self._addressOf(newBodyA),
    )

  @overload(QAbstractPhysicsBody)
  @overload(NoneType)
  def setBodyB(self, newBodyB: Optional[QAbstractPhysicsBody]) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setBodyB(QAbstractPhysicsBody
    *newBodyB)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#setBodyB

    Parameters
    ----------

    newBodyB : Optional[QAbstractPhysicsBody]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsJoint::setBodyB(QAbstractPhysicsBody *newBodyB)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint8setBodyBEP20QAbstractPhysicsBody',
        self._addressOf(newBodyB),
    )

  @overload(QVector3D)
  def setPositionA(self, newPositionA: QVector3D) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setPositionA(const QVector3D
    &newPositionA)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#setPositionA

    Parameters
    ----------

    newPositionA : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QPhysicsJoint::setPositionA(const QVector3D &newPositionA)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint12setPositionAERK9QVector3D',
        self._valueOf(newPositionA),
    )

  @overload(QVector3D)
  def setPositionB(self, newPositionB: QVector3D) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setPositionB(const QVector3D
    &newPositionB)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#setPositionB

    Parameters
    ----------

    newPositionB : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QPhysicsJoint::setPositionB(const QVector3D &newPositionB)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint12setPositionBERK9QVector3D',
        self._valueOf(newPositionB),
    )

  @overload(QQuaternion)
  def setOrientationA(self, newOrientationA: QQuaternion) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setOrientationA(const QQuaternion
    &newOrientationA)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#setOrientationA

    Parameters
    ----------

    newOrientationA : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QPhysicsJoint::setOrientationA(const QQuaternion
    #      &newOrientationA)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint15setOrientationAERK11QQuaternion',
        self._valueOf(newOrientationA),
    )

  @overload(QQuaternion)
  def setOrientationB(self, newOrientationB: QQuaternion) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setOrientationB(const QQuaternion
    &newOrientationB)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#setOrientationB

    Parameters
    ----------

    newOrientationB : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QPhysicsJoint::setOrientationB(const QQuaternion
    #      &newOrientationB)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint15setOrientationBERK11QQuaternion',
        self._valueOf(newOrientationB),
    )

  def setJointProperties(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::setJointProperties()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsjoint.html#setJointProperties
    """
    #  void QPhysicsJoint::setJointProperties()
    self.uglySide.call('ritual_ZN13QPhysicsJoint18setJointPropertiesEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPhysicsJoint::QPhysicsJoint()': the class is abstract, so C++
    cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QPhysicsJoint.__init__' has no cute function yet. Qt's "
        "'QPhysicsJoint::QPhysicsJoint()': the class is abstract, so C++ "
        "cannot make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  def updatePhysXBackend(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::updatePhysXBackend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsjoint.html#updatePhysXBackend
    """
    #  void QPhysicsJoint::updatePhysXBackend()
    self.uglySide.call('ritual_ZN13QPhysicsJoint18updatePhysXBackendEv')

  def bodyAChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::bodyAChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#bodyAChanged
    """
    #  void QPhysicsJoint::bodyAChanged()
    self.uglySide.call('ritual_ZN13QPhysicsJoint12bodyAChangedEv')

  def bodyBChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::bodyBChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#bodyBChanged
    """
    #  void QPhysicsJoint::bodyBChanged()
    self.uglySide.call('ritual_ZN13QPhysicsJoint12bodyBChangedEv')

  def positionAChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::positionAChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsjoint.html#positionAChanged
    """
    #  void QPhysicsJoint::positionAChanged()
    self.uglySide.call('ritual_ZN13QPhysicsJoint16positionAChangedEv')

  def positionBChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::positionBChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsjoint.html#positionBChanged
    """
    #  void QPhysicsJoint::positionBChanged()
    self.uglySide.call('ritual_ZN13QPhysicsJoint16positionBChangedEv')

  def orientationAChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::orientationAChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsjoint.html#orientationAChanged
    """
    #  void QPhysicsJoint::orientationAChanged()
    self.uglySide.call('ritual_ZN13QPhysicsJoint19orientationAChangedEv')

  def orientationBChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::orientationBChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsjoint.html#orientationBChanged
    """
    #  void QPhysicsJoint::orientationBChanged()
    self.uglySide.call('ritual_ZN13QPhysicsJoint19orientationBChangedEv')

  @overload(QObject)
  @overload(NoneType)
  def onBodyDestroyed(self, body: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QPhysicsJoint::onBodyDestroyed(QObject *body)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsjoint.html#onBodyDestroyed

    Parameters
    ----------

    body : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsJoint::onBodyDestroyed(QObject *body)
    self.uglySide.call(
        'ritual_ZN13QPhysicsJoint15onBodyDestroyedEP7QObject',
        self._addressOf(body, 'QObject'),
    )

  @staticmethod
  def createPhysxJoint(*__, **_) -> Never:
    """
    Qt's 'physx::PxJoint *QPhysicsJoint::createPhysxJoint(physx::PxRigidActor
    *actorA, physx::PxRigidActor *actorB, const physx::PxTransform &trfA,
    const physx::PxTransform &trfB)': names 'physx::PxRigidActor', which has
    no cute class yet.
    """
    raise NotImplementedError(
        "'QPhysicsJoint.createPhysxJoint' has no cute function yet. Qt's "
        "'physx::PxJoint "
        "*QPhysicsJoint::createPhysxJoint(physx::PxRigidActor *actorA, "
        "physx::PxRigidActor *actorB, const physx::PxTransform &trfA, const "
        "physx::PxTransform &trfB)': names 'physx::PxRigidActor', which has "
        "no cute class yet.")

  @staticmethod
  def getPhysXBackend(*__, **_) -> Never:
    """
    Qt's 'physx::PxJoint *QPhysicsJoint::getPhysXBackend() const': gives
    'physx::PxJoint', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPhysicsJoint.getPhysXBackend' has no cute function yet. Qt's "
        "'physx::PxJoint *QPhysicsJoint::getPhysXBackend() const': gives "
        "'physx::PxJoint', which has no cute class yet.")
