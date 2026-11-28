"""
QCharacterController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qcharactercontroller_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCharacterController to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from . import QAbstractPhysicsBody, QAbstractPhysicsNode

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCharacterController(QAbstractPhysicsBody):
  """
  The cute side of Qt's QCharacterController: a plain Python object standing
  in front of one C++ QCharacterController.

  It is built on the cute 'QAbstractPhysicsBody', as Qt's
  QCharacterController is built on Qt's QAbstractPhysicsBody, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCharacterController that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'movement',
  'setMovement', 'gravity', 'setGravity', 'getDisplacement', 'midAirControl',
  'setMidAirControl', 'teleport', 'enableShapeHitCallback',
  'setEnableShapeHitCallback', 'movementChanged', 'gravityChanged',
  'midAirControlChanged', 'collisionsChanged',
  'enableShapeHitCallbackChanged', 'shapeHit'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCharacterController::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCharacterController::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'bool QCharacterController::getTeleport(QVector3D &position)': takes
    a type Python has no way to hand over yet.
  - Qt's 'const Collisions &QCharacterController::collisions() const': gives
    a type Python has no way to take yet.
  - Qt's 'void QCharacterController::setCollisions(const Collisions
    &newCollisions)': takes a type Python has no way to hand over yet.
  - Qt's 'QAbstractPhysXNode *QCharacterController::createPhysXBackend()':
    gives 'QAbstractPhysXNode', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QCharacterController is created at the first use, not by
    'QCharacterController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCharacterController.
  - Qt tells when it has removed the C++ QCharacterController. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCharacterController that has no cute function yet,
    'collisions', 'getTeleport', 'setCollisions', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QCharacterController, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Collision(CuteFlags, scoped=True):
    """
    The flags enum 'QCharacterController::Collision' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QCharacterController::Collisions'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    NULL = 0x0
    Side = 0x1
    Up = 0x2
    Down = 0x4

  Collisions = Collision

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
    Calls Qt's 'QString QCharacterController::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcharactercontroller.html#tr

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
    #  QString QCharacterController::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QCharacterController2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCharacterController'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCharacterController::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCharacterController::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QCharacterController10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def movement(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QCharacterController::movement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcharactercontroller.html#movement

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QCharacterController::movement() const
    address = self.uglySide.call(
        'ritual_ZNK20QCharacterController8movementEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def gravity(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D &QCharacterController::gravity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcharactercontroller.html#gravity

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D &QCharacterController::gravity() const
    address = self.uglySide.call(
        'ritual_ZNK20QCharacterController7gravityEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def midAirControl(self) -> bool:
    """
    Calls Qt's 'bool QCharacterController::midAirControl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#midAirControl
    """
    #  bool QCharacterController::midAirControl() const
    return self.uglySide.call(
        'ritual_ZNK20QCharacterController13midAirControlEv',
    )

  def enableShapeHitCallback(self) -> bool:
    """
    Calls Qt's 'bool QCharacterController::enableShapeHitCallback() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#enableShapeHitCallback
    """
    #  bool QCharacterController::enableShapeHitCallback() const
    return self.uglySide.call(
        'ritual_ZNK20QCharacterController22enableShapeHitCallbackEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setMovement(self, newMovement: QVector3D) -> None:
    """
    Calls Qt's 'void QCharacterController::setMovement(const QVector3D
    &newMovement)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#setMovement

    Parameters
    ----------

    newMovement : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCharacterController::setMovement(const QVector3D &newMovement)
    self.uglySide.call(
        'ritual_ZN20QCharacterController11setMovementERK9QVector3D',
        self._valueOf(newMovement),
    )

  @overload(QVector3D)
  def setGravity(self, newGravity: QVector3D) -> None:
    """
    Calls Qt's 'void QCharacterController::setGravity(const QVector3D
    &newGravity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#setGravity

    Parameters
    ----------

    newGravity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCharacterController::setGravity(const QVector3D &newGravity)
    self.uglySide.call(
        'ritual_ZN20QCharacterController10setGravityERK9QVector3D',
        self._valueOf(newGravity),
    )

  @overload(bool)
  def setMidAirControl(self, newMidAirControl: bool) -> None:
    """
    Calls Qt's 'void QCharacterController::setMidAirControl(bool
    newMidAirControl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#setMidAirControl

    Parameters
    ----------

    newMidAirControl : bool
      Passed on as it is.
    """
    #  void QCharacterController::setMidAirControl(bool newMidAirControl)
    self.uglySide.call(
        'ritual_ZN20QCharacterController16setMidAirControlEb',
        newMidAirControl,
    )

  @overload(bool)
  def setEnableShapeHitCallback(
      self,
      newEnableShapeHitCallback: bool,
  ) -> None:
    """
    Calls Qt's 'void QCharacterController::setEnableShapeHitCallback(bool
    newEnableShapeHitCallback)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html

    Parameters
    ----------

    newEnableShapeHitCallback : bool
      Passed on as it is.
    """
    #  void QCharacterController::setEnableShapeHitCallback(bool
    #      newEnableShapeHitCallback)
    self.uglySide.call(
        'ritual_ZN20QCharacterController25setEnableShapeHitCallbackEb',
        newEnableShapeHitCallback,
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
    'QCharacterController::QCharacterController()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#QCharacterController
    """
    #  QCharacterController::QCharacterController()
    self._noteCreation(QCharacterController, lambda: Rituals.call(
        'ritual_ZN20QCharacterControllerC1Ev',
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
  def getDisplacement(self, deltaTime: float) -> QVector3D:
    """
    Calls Qt's 'QVector3D QCharacterController::getDisplacement(float
    deltaTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#getDisplacement

    Parameters
    ----------

    deltaTime : float
      Passed on as it is.

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QCharacterController::getDisplacement(float deltaTime)
    address = self.uglySide.call(
        'ritual_ZN20QCharacterController15getDisplacementEf', deltaTime,
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  @overload(QVector3D)
  def teleport(self, position: QVector3D) -> None:
    """
    Calls Qt's 'void QCharacterController::teleport(const QVector3D
    &position)'.

    Qt's own words: https://doc.qt.io/qt-6/qcharactercontroller.html#teleport

    Parameters
    ----------

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCharacterController::teleport(const QVector3D &position)
    self.uglySide.call(
        'ritual_ZN20QCharacterController8teleportERK9QVector3D',
        self._valueOf(position),
    )

  def movementChanged(self) -> None:
    """
    Calls Qt's 'void QCharacterController::movementChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#movementChanged
    """
    #  void QCharacterController::movementChanged()
    self.uglySide.call('ritual_ZN20QCharacterController15movementChangedEv')

  def gravityChanged(self) -> None:
    """
    Calls Qt's 'void QCharacterController::gravityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#gravityChanged
    """
    #  void QCharacterController::gravityChanged()
    self.uglySide.call('ritual_ZN20QCharacterController14gravityChangedEv')

  def midAirControlChanged(self) -> None:
    """
    Calls Qt's 'void QCharacterController::midAirControlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#midAirControlChanged
    """
    #  void QCharacterController::midAirControlChanged()
    self.uglySide.call(
        'ritual_ZN20QCharacterController20midAirControlChangedEv',
    )

  def collisionsChanged(self) -> None:
    """
    Calls Qt's 'void QCharacterController::collisionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html#collisionsChanged
    """
    #  void QCharacterController::collisionsChanged()
    self.uglySide.call(
        'ritual_ZN20QCharacterController17collisionsChangedEv',
    )

  def enableShapeHitCallbackChanged(self) -> None:
    """
    Calls Qt's 'void QCharacterController::enableShapeHitCallbackChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcharactercontroller.html
    """
    #  void QCharacterController::enableShapeHitCallbackChanged()
    self.uglySide.call(
        'ritual_ZN20QCharacterController29enableShapeHitCallbackChangedEv',
    )

  @overload(QAbstractPhysicsNode, QVector3D, QVector3D, QVector3D)
  @overload(NoneType, QVector3D, QVector3D, QVector3D)
  def shapeHit(
      self,
      body: Optional[QAbstractPhysicsNode],
      position: QVector3D,
      impulse: QVector3D,
      normal: QVector3D,
  ) -> None:
    """
    Calls Qt's 'void QCharacterController::shapeHit(QAbstractPhysicsNode
    *body, const QVector3D &position, const QVector3D &impulse, const
    QVector3D &normal)'.

    Qt's own words: https://doc.qt.io/qt-6/qcharactercontroller.html#shapeHit

    Parameters
    ----------

    body : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    impulse : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    normal : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCharacterController::shapeHit(QAbstractPhysicsNode *body, const
    #      QVector3D &position, const QVector3D &impulse, const QVector3D
    #      &normal)
    self.uglySide.call(
        'ritual_ZN20QCharacterController8shapeHitEP20QAbstractPhysicsNodeRK'
        '9QVector3DS4_S4_',
        self._addressOf(body), self._valueOf(position),
        self._valueOf(impulse), self._valueOf(normal),
    )

  @staticmethod
  def collisions(*__, **_) -> Never:
    """
    Qt's 'const Collisions &QCharacterController::collisions() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCharacterController.collisions' has no cute function yet. Qt's "
        "'const Collisions &QCharacterController::collisions() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def getTeleport(*__, **_) -> Never:
    """
    Qt's 'bool QCharacterController::getTeleport(QVector3D &position)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCharacterController.getTeleport' has no cute function yet. Qt's "
        "'bool QCharacterController::getTeleport(QVector3D &position)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setCollisions(*__, **_) -> Never:
    """
    Qt's 'void QCharacterController::setCollisions(const Collisions
    &newCollisions)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCharacterController.setCollisions' has no cute function yet. "
        "Qt's 'void QCharacterController::setCollisions(const Collisions "
        "&newCollisions)': takes a type Python has no way to hand over yet.")
