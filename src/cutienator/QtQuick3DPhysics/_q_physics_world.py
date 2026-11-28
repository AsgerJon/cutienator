"""
QPhysicsWorld binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsworld_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPhysicsWorld to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QVector3D
  from ..QtQuick3D import QQuick3DNode
  from . import QAbstractPhysicsNode, QPhysicsJoint
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractPhysicsNode = WAIT['QAbstractPhysicsNode']
  QPhysicsJoint = WAIT['QPhysicsJoint']
  QQuick3DNode = WAIT['QQuick3DNode']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPhysicsWorld(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QPhysicsWorld: a plain Python object standing in
  front of one C++ QPhysicsWorld.

  It is built on the cute 'QObject', as Qt's QPhysicsWorld is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QPhysicsWorld is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPhysicsWorld that has a ritual and that Python can
  call so far, 68 names in all: 'metaObject', 'tr', 'classBegin',
  'componentComplete', 'gravity', 'running', 'forceDebugDraw', 'enableCCD',
  'typicalLength', 'typicalSpeed', 'defaultDensity', 'minimumTimestep',
  'maximumTimestep', 'isNodeRemoved', 'getWorld', 'registerNode',
  'deregisterNode', 'registerJoint', 'deregisterJoint', 'viewport',
  'setHasIndividualDebugDraw', 'scene', 'numThreads',
  'reportKinematicKinematicCollisions',
  'setReportKinematicKinematicCollisions', 'reportStaticKinematicCollisions',
  'setReportStaticKinematicCollisions', 'cleanupRemovedJoints', 'setGravity',
  'setRunning', 'setForceDebugDraw', 'setEnableCCD', 'setTypicalLength',
  'setTypicalSpeed', 'setDefaultDensity', 'setViewport',
  'setMinimumTimestep', 'setMaximumTimestep', 'setScene', 'setNumThreads',
  'gravityChanged', 'runningChanged', 'enableCCDChanged',
  'forceDebugDrawChanged', 'typicalLengthChanged', 'typicalSpeedChanged',
  'defaultDensityChanged', 'viewportChanged', 'minimumTimestepChanged',
  'maximumTimestepChanged', 'frameDone', 'sceneChanged', 'numThreadsChanged',
  'reportKinematicKinematicCollisionsChanged',
  'reportStaticKinematicCollisionsChanged', 'simulateFrame', 'frameFinished',
  'frameFinishedDesignStudio', 'initPhysics', 'cleanupRemovedNodes',
  'updateDebugDraw', 'updateDebugDrawDesignStudio', 'setupDebugMaterials',
  'disableDebugDraw', 'matchOrphanNodes', 'matchOrphanJoints',
  'findPhysicsNodes', 'emitContactCallbacks'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPhysicsWorld::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QPhysicsWorld::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QPhysicsWorld::~QPhysicsWorld()': the destructor: Python never
    removes a C++ QPhysicsWorld.
  - Qt's 'void QPhysicsWorld::registerContact(QAbstractPhysicsNode *sender,
    QAbstractPhysicsNode *receiver, const QVector<QVector3D> &positions,
    const QVector<QVector3D> &impulses, const QVector<QVector3D> &normals)':
    takes a type Python has no way to hand over yet.
  - Qt's 'physx::PxControllerManager *QPhysicsWorld::controllerManager()':
    gives 'physx::PxControllerManager', which has no cute class yet.
  - Qt's 'physx::PxPhysics *QPhysicsWorld::getPhysics()': gives
    'physx::PxPhysics', which has no cute class yet.
  - Qt's 'physx::PxCooking *QPhysicsWorld::getCooking()': gives
    'physx::PxCooking', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 79 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPhysicsWorld is created at the first use, not by
    'QPhysicsWorld(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPhysicsWorld.
  - Qt tells when it has removed the C++ QPhysicsWorld. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPhysicsWorld that has no cute function yet,
    'controllerManager', 'getCooking', 'getPhysics', 'registerContact', holds
    a function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QPhysicsWorld::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#tr

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
    #  QString QPhysicsWorld::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QPhysicsWorld2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQuick3DNode)
  @overload(NoneType)
  def getWorld(node: Optional[QQuick3DNode]) -> Optional[QPhysicsWorld]:
    """
    Calls Qt's 'QPhysicsWorld *QPhysicsWorld::getWorld(QQuick3DNode *node)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#getWorld

    Parameters
    ----------

    node : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPhysicsWorld]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPhysicsWorld *QPhysicsWorld::getWorld(QQuick3DNode *node)
    address = Rituals.call(
        'ritual_ZN13QPhysicsWorld8getWorldEP12QQuick3DNode',
        CuteMixin._addressOf(node),
    )
    return QPhysicsWorld._cuteAt(address)

  @staticmethod
  @overload(QPhysicsJoint)
  def getWorld(joint: Optional[QPhysicsJoint]) -> Optional[QPhysicsWorld]:
    """
    Calls Qt's 'QPhysicsWorld *QPhysicsWorld::getWorld(QPhysicsJoint
    *joint)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#getWorld

    Parameters
    ----------

    joint : Optional[QPhysicsJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPhysicsWorld]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPhysicsWorld *QPhysicsWorld::getWorld(QPhysicsJoint *joint)
    address = Rituals.call(
        'ritual_ZN13QPhysicsWorld8getWorldEP13QPhysicsJoint',
        CuteMixin._addressOf(joint),
    )
    return QPhysicsWorld._cuteAt(address)

  @staticmethod
  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def registerNode(physicsNode: Optional[QAbstractPhysicsNode]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::registerNode(QAbstractPhysicsNode
    *physicsNode)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#registerNode

    Parameters
    ----------

    physicsNode : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::registerNode(QAbstractPhysicsNode *physicsNode)
    Rituals.call(
        'ritual_ZN13QPhysicsWorld12registerNodeEP20QAbstractPhysicsNode',
        CuteMixin._addressOf(physicsNode),
    )

  @staticmethod
  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def deregisterNode(physicsNode: Optional[QAbstractPhysicsNode]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::deregisterNode(QAbstractPhysicsNode
    *physicsNode)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#deregisterNode

    Parameters
    ----------

    physicsNode : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::deregisterNode(QAbstractPhysicsNode *physicsNode)
    Rituals.call(
        'ritual_ZN13QPhysicsWorld14deregisterNodeEP20QAbstractPhysicsNode',
        CuteMixin._addressOf(physicsNode),
    )

  @staticmethod
  @overload(QPhysicsJoint)
  @overload(NoneType)
  def registerJoint(joint: Optional[QPhysicsJoint]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::registerJoint(QPhysicsJoint *joint)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#registerJoint

    Parameters
    ----------

    joint : Optional[QPhysicsJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::registerJoint(QPhysicsJoint *joint)
    Rituals.call(
        'ritual_ZN13QPhysicsWorld13registerJointEP13QPhysicsJoint',
        CuteMixin._addressOf(joint),
    )

  @staticmethod
  @overload(QPhysicsJoint)
  @overload(NoneType)
  def deregisterJoint(joint: Optional[QPhysicsJoint]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::deregisterJoint(QPhysicsJoint *joint)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#deregisterJoint

    Parameters
    ----------

    joint : Optional[QPhysicsJoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::deregisterJoint(QPhysicsJoint *joint)
    Rituals.call(
        'ritual_ZN13QPhysicsWorld15deregisterJointEP13QPhysicsJoint',
        CuteMixin._addressOf(joint),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPhysicsWorld'

  #  Qt's QPhysicsWorld is built on more than one class. The part of a C++
  #  QPhysicsWorld that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QPhysicsWorld_QQmlParserStatus',
  }

  #  A C++ QPhysicsWorld Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPhysicsWorld'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPhysicsWorld::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPhysicsWorld::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsWorld10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def gravity(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QPhysicsWorld::gravity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#gravity

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QPhysicsWorld::gravity() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsWorld7gravityEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def running(self) -> bool:
    """
    Calls Qt's 'bool QPhysicsWorld::running() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#running
    """
    #  bool QPhysicsWorld::running() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld7runningEv')

  def forceDebugDraw(self) -> bool:
    """
    Calls Qt's 'bool QPhysicsWorld::forceDebugDraw() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#forceDebugDraw
    """
    #  bool QPhysicsWorld::forceDebugDraw() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld14forceDebugDrawEv')

  def enableCCD(self) -> bool:
    """
    Calls Qt's 'bool QPhysicsWorld::enableCCD() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#enableCCD
    """
    #  bool QPhysicsWorld::enableCCD() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld9enableCCDEv')

  def typicalLength(self) -> float:
    """
    Calls Qt's 'float QPhysicsWorld::typicalLength() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#typicalLength
    """
    #  float QPhysicsWorld::typicalLength() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld13typicalLengthEv')

  def typicalSpeed(self) -> float:
    """
    Calls Qt's 'float QPhysicsWorld::typicalSpeed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#typicalSpeed
    """
    #  float QPhysicsWorld::typicalSpeed() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld12typicalSpeedEv')

  def defaultDensity(self) -> float:
    """
    Calls Qt's 'float QPhysicsWorld::defaultDensity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#defaultDensity
    """
    #  float QPhysicsWorld::defaultDensity() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld14defaultDensityEv')

  def minimumTimestep(self) -> float:
    """
    Calls Qt's 'float QPhysicsWorld::minimumTimestep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#minimumTimestep
    """
    #  float QPhysicsWorld::minimumTimestep() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld15minimumTimestepEv')

  def maximumTimestep(self) -> float:
    """
    Calls Qt's 'float QPhysicsWorld::maximumTimestep() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#maximumTimestep
    """
    #  float QPhysicsWorld::maximumTimestep() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld15maximumTimestepEv')

  def viewport(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QPhysicsWorld::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#viewport

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QPhysicsWorld::viewport() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsWorld8viewportEv')
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def scene(self) -> Optional[QQuick3DNode]:
    """
    Calls Qt's 'QQuick3DNode *QPhysicsWorld::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#scene

    Returns
    -------

    Optional[QQuick3DNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DNode *QPhysicsWorld::scene() const
    address = self.uglySide.call('ritual_ZNK13QPhysicsWorld5sceneEv')
    from ..QtQuick3D import QQuick3DNode
    return QQuick3DNode._cuteAt(address)

  def numThreads(self) -> int:
    """
    Calls Qt's 'int QPhysicsWorld::numThreads() const'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#numThreads
    """
    #  int QPhysicsWorld::numThreads() const
    return self.uglySide.call('ritual_ZNK13QPhysicsWorld10numThreadsEv')

  def reportKinematicKinematicCollisions(self) -> bool:
    """
    Calls Qt's 'bool QPhysicsWorld::reportKinematicKinematicCollisions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html
    """
    #  bool QPhysicsWorld::reportKinematicKinematicCollisions() const
    return self.uglySide.call(
        'ritual_ZNK13QPhysicsWorld34reportKinematicKinematicCollisionsEv',
    )

  def reportStaticKinematicCollisions(self) -> bool:
    """
    Calls Qt's 'bool QPhysicsWorld::reportStaticKinematicCollisions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#reportStaticKinematicCollisions
    """
    #  bool QPhysicsWorld::reportStaticKinematicCollisions() const
    return self.uglySide.call(
        'ritual_ZNK13QPhysicsWorld31reportStaticKinematicCollisionsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setHasIndividualDebugDraw(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setHasIndividualDebugDraw()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setHasIndividualDebugDraw
    """
    #  void QPhysicsWorld::setHasIndividualDebugDraw()
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld25setHasIndividualDebugDrawEv',
    )

  @overload(bool)
  def setReportKinematicKinematicCollisions(
      self,
      newReportKinematicKinematicCollisions: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QPhysicsWorld::setReportKinematicKinematicCollisions(bool
    newReportKinematicKinematicCollisions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html

    Parameters
    ----------

    newReportKinematicKinematicCollisions : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::setReportKinematicKinematicCollisions(bool
    #      newReportKinematicKinematicCollisions)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld37setReportKinematicKinematicCollisionsEb',
        newReportKinematicKinematicCollisions,
    )

  @overload(bool)
  def setReportStaticKinematicCollisions(
      self,
      newReportStaticKinematicCollisions: bool,
  ) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setReportStaticKinematicCollisions(bool
    newReportStaticKinematicCollisions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html

    Parameters
    ----------

    newReportStaticKinematicCollisions : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::setReportStaticKinematicCollisions(bool
    #      newReportStaticKinematicCollisions)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld34setReportStaticKinematicCollisionsEb',
        newReportStaticKinematicCollisions,
    )

  @overload(QVector3D)
  def setGravity(self, gravity: QVector3D) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setGravity(QVector3D gravity)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setGravity

    Parameters
    ----------

    gravity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QPhysicsWorld::setGravity(QVector3D gravity)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld10setGravityE9QVector3D',
        self._valueOf(gravity),
    )

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setRunning(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::setRunning(bool running)
    self.uglySide.call('ritual_ZN13QPhysicsWorld10setRunningEb', running)

  @overload(bool)
  def setForceDebugDraw(self, forceDebugDraw: bool) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setForceDebugDraw(bool forceDebugDraw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setForceDebugDraw

    Parameters
    ----------

    forceDebugDraw : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::setForceDebugDraw(bool forceDebugDraw)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld17setForceDebugDrawEb', forceDebugDraw,
    )

  @overload(bool)
  def setEnableCCD(self, enableCCD: bool) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setEnableCCD(bool enableCCD)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setEnableCCD

    Parameters
    ----------

    enableCCD : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::setEnableCCD(bool enableCCD)
    self.uglySide.call('ritual_ZN13QPhysicsWorld12setEnableCCDEb', enableCCD)

  @overload(float)
  def setTypicalLength(self, typicalLength: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setTypicalLength(float typicalLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setTypicalLength

    Parameters
    ----------

    typicalLength : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::setTypicalLength(float typicalLength)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld16setTypicalLengthEf', typicalLength,
    )

  @overload(float)
  def setTypicalSpeed(self, typicalSpeed: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setTypicalSpeed(float typicalSpeed)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setTypicalSpeed

    Parameters
    ----------

    typicalSpeed : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::setTypicalSpeed(float typicalSpeed)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld15setTypicalSpeedEf', typicalSpeed,
    )

  @overload(float)
  def setDefaultDensity(self, defaultDensity: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setDefaultDensity(float defaultDensity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setDefaultDensity

    Parameters
    ----------

    defaultDensity : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::setDefaultDensity(float defaultDensity)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld17setDefaultDensityEf', defaultDensity,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setViewport(self, viewport: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setViewport(QQuick3DNode *viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setViewport

    Parameters
    ----------

    viewport : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::setViewport(QQuick3DNode *viewport)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld11setViewportEP12QQuick3DNode',
        self._addressOf(viewport),
    )

  @overload(float)
  def setMinimumTimestep(self, minTimestep: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setMinimumTimestep(float minTimestep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setMinimumTimestep

    Parameters
    ----------

    minTimestep : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::setMinimumTimestep(float minTimestep)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld18setMinimumTimestepEf', minTimestep,
    )

  @overload(float)
  def setMaximumTimestep(self, maxTimestep: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setMaximumTimestep(float maxTimestep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setMaximumTimestep

    Parameters
    ----------

    maxTimestep : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::setMaximumTimestep(float maxTimestep)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld18setMaximumTimestepEf', maxTimestep,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setScene(self, newScene: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setScene(QQuick3DNode *newScene)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setScene

    Parameters
    ----------

    newScene : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::setScene(QQuick3DNode *newScene)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld8setSceneEP12QQuick3DNode',
        self._addressOf(newScene),
    )

  @overload(int)
  def setNumThreads(self, newNumThreads: int) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setNumThreads(int newNumThreads)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#setNumThreads

    Parameters
    ----------

    newNumThreads : int
      Passed on as it is.
    """
    #  void QPhysicsWorld::setNumThreads(int newNumThreads)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld13setNumThreadsEi', newNumThreads,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QPhysicsWorld::QPhysicsWorld(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#QPhysicsWorld

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QPhysicsWorld::QPhysicsWorld(QObject *parent)
    self._noteCreation(QPhysicsWorld, lambda: Rituals.call(
        'ritual_ZN13QPhysicsWorldC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#classBegin
    """
    #  void QPhysicsWorld::classBegin()
    ritual = 'ritual_ZN13QPhysicsWorld10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPhysicsWorld10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#componentComplete
    """
    #  void QPhysicsWorld::componentComplete()
    ritual = 'ritual_ZN13QPhysicsWorld17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QPhysicsWorld17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QAbstractPhysicsNode)
  @overload(NoneType)
  def isNodeRemoved(self, object: Optional[QAbstractPhysicsNode]) -> bool:
    """
    Calls Qt's 'bool QPhysicsWorld::isNodeRemoved(QAbstractPhysicsNode
    *object)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#isNodeRemoved

    Parameters
    ----------

    object : Optional[QAbstractPhysicsNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPhysicsWorld::isNodeRemoved(QAbstractPhysicsNode *object)
    return self.uglySide.call(
        'ritual_ZN13QPhysicsWorld13isNodeRemovedEP20QAbstractPhysicsNode',
        self._addressOf(object),
    )

  def cleanupRemovedJoints(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::cleanupRemovedJoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#cleanupRemovedJoints
    """
    #  void QPhysicsWorld::cleanupRemovedJoints()
    self.uglySide.call('ritual_ZN13QPhysicsWorld20cleanupRemovedJointsEv')

  @overload(QVector3D)
  def gravityChanged(self, gravity: QVector3D) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::gravityChanged(QVector3D gravity)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#gravityChanged

    Parameters
    ----------

    gravity : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QPhysicsWorld::gravityChanged(QVector3D gravity)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld14gravityChangedE9QVector3D',
        self._valueOf(gravity),
    )

  @overload(bool)
  def runningChanged(self, running: bool) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::runningChanged(bool running)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#runningChanged

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::runningChanged(bool running)
    self.uglySide.call('ritual_ZN13QPhysicsWorld14runningChangedEb', running)

  @overload(bool)
  def enableCCDChanged(self, enableCCD: bool) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::enableCCDChanged(bool enableCCD)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#enableCCDChanged

    Parameters
    ----------

    enableCCD : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::enableCCDChanged(bool enableCCD)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld16enableCCDChangedEb', enableCCD,
    )

  @overload(bool)
  def forceDebugDrawChanged(self, forceDebugDraw: bool) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::forceDebugDrawChanged(bool
    forceDebugDraw)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#forceDebugDrawChanged

    Parameters
    ----------

    forceDebugDraw : bool
      Passed on as it is.
    """
    #  void QPhysicsWorld::forceDebugDrawChanged(bool forceDebugDraw)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld21forceDebugDrawChangedEb', forceDebugDraw,
    )

  @overload(float)
  def typicalLengthChanged(self, typicalLength: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::typicalLengthChanged(float
    typicalLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#typicalLengthChanged

    Parameters
    ----------

    typicalLength : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::typicalLengthChanged(float typicalLength)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld20typicalLengthChangedEf', typicalLength,
    )

  @overload(float)
  def typicalSpeedChanged(self, typicalSpeed: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::typicalSpeedChanged(float typicalSpeed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#typicalSpeedChanged

    Parameters
    ----------

    typicalSpeed : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::typicalSpeedChanged(float typicalSpeed)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld19typicalSpeedChangedEf', typicalSpeed,
    )

  @overload(float)
  def defaultDensityChanged(self, defaultDensity: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::defaultDensityChanged(float
    defaultDensity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#defaultDensityChanged

    Parameters
    ----------

    defaultDensity : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::defaultDensityChanged(float defaultDensity)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld21defaultDensityChangedEf', defaultDensity,
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def viewportChanged(self, viewport: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::viewportChanged(QQuick3DNode *viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#viewportChanged

    Parameters
    ----------

    viewport : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::viewportChanged(QQuick3DNode *viewport)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld15viewportChangedEP12QQuick3DNode',
        self._addressOf(viewport),
    )

  @overload(float)
  def minimumTimestepChanged(self, minimumTimestep: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::minimumTimestepChanged(float
    minimumTimestep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#minimumTimestepChanged

    Parameters
    ----------

    minimumTimestep : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::minimumTimestepChanged(float minimumTimestep)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld22minimumTimestepChangedEf',
        minimumTimestep,
    )

  @overload(float)
  def maximumTimestepChanged(self, maxTimestep: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::maximumTimestepChanged(float
    maxTimestep)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#maximumTimestepChanged

    Parameters
    ----------

    maxTimestep : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::maximumTimestepChanged(float maxTimestep)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld22maximumTimestepChangedEf', maxTimestep,
    )

  @overload(float)
  def frameDone(self, timestep: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::frameDone(float timestep)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#frameDone

    Parameters
    ----------

    timestep : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::frameDone(float timestep)
    self.uglySide.call('ritual_ZN13QPhysicsWorld9frameDoneEf', timestep)

  def sceneChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::sceneChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#sceneChanged
    """
    #  void QPhysicsWorld::sceneChanged()
    self.uglySide.call('ritual_ZN13QPhysicsWorld12sceneChangedEv')

  def numThreadsChanged(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::numThreadsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#numThreadsChanged
    """
    #  void QPhysicsWorld::numThreadsChanged()
    self.uglySide.call('ritual_ZN13QPhysicsWorld17numThreadsChangedEv')

  def reportKinematicKinematicCollisionsChanged(self) -> None:
    """
    Calls Qt's 'void
    QPhysicsWorld::reportKinematicKinematicCollisionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html
    """
    #  void QPhysicsWorld::reportKinematicKinematicCollisionsChanged()
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld41reportKinematicKinematicCollisionsChange'
        'dEv',
    )

  def reportStaticKinematicCollisionsChanged(self) -> None:
    """
    Calls Qt's 'void
    QPhysicsWorld::reportStaticKinematicCollisionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html
    """
    #  void QPhysicsWorld::reportStaticKinematicCollisionsChanged()
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld38reportStaticKinematicCollisionsChangedEv',
    )

  def simulateFrame(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::simulateFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#simulateFrame
    """
    #  void QPhysicsWorld::simulateFrame()
    self.uglySide.call('ritual_ZN13QPhysicsWorld13simulateFrameEv')

  @overload(float)
  def frameFinished(self, deltaTime: float) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::frameFinished(float deltaTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#frameFinished

    Parameters
    ----------

    deltaTime : float
      Passed on as it is.
    """
    #  void QPhysicsWorld::frameFinished(float deltaTime)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld13frameFinishedEf', deltaTime,
    )

  def frameFinishedDesignStudio(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::frameFinishedDesignStudio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#frameFinishedDesignStudio
    """
    #  void QPhysicsWorld::frameFinishedDesignStudio()
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld25frameFinishedDesignStudioEv',
    )

  def initPhysics(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::initPhysics()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#initPhysics
    """
    #  void QPhysicsWorld::initPhysics()
    self.uglySide.call('ritual_ZN13QPhysicsWorld11initPhysicsEv')

  def cleanupRemovedNodes(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::cleanupRemovedNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#cleanupRemovedNodes
    """
    #  void QPhysicsWorld::cleanupRemovedNodes()
    self.uglySide.call('ritual_ZN13QPhysicsWorld19cleanupRemovedNodesEv')

  def updateDebugDraw(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::updateDebugDraw()'.

    Qt's own words: https://doc.qt.io/qt-6/qphysicsworld.html#updateDebugDraw
    """
    #  void QPhysicsWorld::updateDebugDraw()
    self.uglySide.call('ritual_ZN13QPhysicsWorld15updateDebugDrawEv')

  def updateDebugDrawDesignStudio(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::updateDebugDrawDesignStudio()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#updateDebugDrawDesignStudio
    """
    #  void QPhysicsWorld::updateDebugDrawDesignStudio()
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld27updateDebugDrawDesignStudioEv',
    )

  @overload(QQuick3DNode)
  @overload(NoneType)
  def setupDebugMaterials(self, sceneNode: Optional[QQuick3DNode]) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::setupDebugMaterials(QQuick3DNode
    *sceneNode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#setupDebugMaterials

    Parameters
    ----------

    sceneNode : Optional[QQuick3DNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPhysicsWorld::setupDebugMaterials(QQuick3DNode *sceneNode)
    self.uglySide.call(
        'ritual_ZN13QPhysicsWorld19setupDebugMaterialsEP12QQuick3DNode',
        self._addressOf(sceneNode),
    )

  def disableDebugDraw(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::disableDebugDraw()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#disableDebugDraw
    """
    #  void QPhysicsWorld::disableDebugDraw()
    self.uglySide.call('ritual_ZN13QPhysicsWorld16disableDebugDrawEv')

  def matchOrphanNodes(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::matchOrphanNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#matchOrphanNodes
    """
    #  void QPhysicsWorld::matchOrphanNodes()
    self.uglySide.call('ritual_ZN13QPhysicsWorld16matchOrphanNodesEv')

  def matchOrphanJoints(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::matchOrphanJoints()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#matchOrphanJoints
    """
    #  void QPhysicsWorld::matchOrphanJoints()
    self.uglySide.call('ritual_ZN13QPhysicsWorld17matchOrphanJointsEv')

  def findPhysicsNodes(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::findPhysicsNodes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#findPhysicsNodes
    """
    #  void QPhysicsWorld::findPhysicsNodes()
    self.uglySide.call('ritual_ZN13QPhysicsWorld16findPhysicsNodesEv')

  def emitContactCallbacks(self) -> None:
    """
    Calls Qt's 'void QPhysicsWorld::emitContactCallbacks()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qphysicsworld.html#emitContactCallbacks
    """
    #  void QPhysicsWorld::emitContactCallbacks()
    self.uglySide.call('ritual_ZN13QPhysicsWorld20emitContactCallbacksEv')

  @staticmethod
  def controllerManager(*__, **_) -> Never:
    """
    Qt's 'physx::PxControllerManager *QPhysicsWorld::controllerManager()':
    gives 'physx::PxControllerManager', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPhysicsWorld.controllerManager' has no cute function yet. Qt's "
        "'physx::PxControllerManager *QPhysicsWorld::controllerManager()': "
        "gives 'physx::PxControllerManager', which has no cute class yet.")

  @staticmethod
  def getCooking(*__, **_) -> Never:
    """
    Qt's 'physx::PxCooking *QPhysicsWorld::getCooking()': gives
    'physx::PxCooking', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPhysicsWorld.getCooking' has no cute function yet. Qt's "
        "'physx::PxCooking *QPhysicsWorld::getCooking()': gives "
        "'physx::PxCooking', which has no cute class yet.")

  @staticmethod
  def getPhysics(*__, **_) -> Never:
    """
    Qt's 'physx::PxPhysics *QPhysicsWorld::getPhysics()': gives
    'physx::PxPhysics', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPhysicsWorld.getPhysics' has no cute function yet. Qt's "
        "'physx::PxPhysics *QPhysicsWorld::getPhysics()': gives "
        "'physx::PxPhysics', which has no cute class yet.")

  @staticmethod
  def registerContact(*__, **_) -> Never:
    """
    Qt's 'void QPhysicsWorld::registerContact(QAbstractPhysicsNode *sender,
    QAbstractPhysicsNode *receiver, const QVector<QVector3D> &positions,
    const QVector<QVector3D> &impulses, const QVector<QVector3D> &normals)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPhysicsWorld.registerContact' has no cute function yet. Qt's "
        "'void QPhysicsWorld::registerContact(QAbstractPhysicsNode *sender, "
        "QAbstractPhysicsNode *receiver, const QVector<QVector3D> "
        "&positions, const QVector<QVector3D> &impulses, const "
        "QVector<QVector3D> &normals)': takes a type Python has no way to "
        "hand over yet.")
