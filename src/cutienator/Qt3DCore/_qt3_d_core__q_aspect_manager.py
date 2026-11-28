"""
Qt3DCore::QAspectManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qaspectmanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::QAspectManager to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAspectManager(QObject, Qt3DCore.QAbstractFrontEndNodeManager):
  """
  The cute side of Qt's Qt3DCore::QAspectManager: a plain Python object
  standing in front of one C++ Qt3DCore::QAspectManager.

  It is built on the cute 'QObject', as Qt's Qt3DCore::QAspectManager is
  built on Qt's QObject, and has everything that class has. It is built on
  the cute 'Qt3DCore::QAbstractFrontEndNodeManager' as well, as Qt's
  Qt3DCore::QAspectManager is built on Qt's
  Qt3DCore::QAbstractFrontEndNodeManager too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QAspectManager that has a ritual and that
  Python can call so far, 23 names in all: 'metaObject', 'tr', 'engine',
  'scheduler', 'setRunMode', 'enterSimulationLoop', 'exitSimulationLoop',
  'isShuttingDown', 'initialize', 'shutdown', 'processFrame',
  'registerAspect', 'unregisterAspect', 'aspect', 'jobManager',
  'changeArbiter', 'serviceLocator', 'setPostConstructorInit', 'lookupNode',
  'scene', 'jobsInLastFrame', 'dumpJobsOnNextFrame', 'requestNextFrame'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DCore::QAspectManager::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DCore::QAspectManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DCore::QAspectManager::~QAspectManager()': the destructor:
    Python never removes a C++ Qt3DCore::QAspectManager.
  - Qt's 'void Qt3DCore::QAspectManager::setRootEntity(Qt3DCore::QEntity
    *root, const QList<QNode *> &nodes)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void Qt3DCore::QAspectManager::addNodes(const QList<QNode *>
    &nodes)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DCore::QAspectManager::removeNodes(const QList<QNode *>
    &nodes)': takes a type Python has no way to hand over yet.
  - Qt's 'const QList<QAbstractAspect *> &Qt3DCore::QAspectManager::aspects()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<QNode *> Qt3DCore::QAspectManager::lookupNodes(const
    QList<QNodeId> &ids) const': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DCore::QAspectManager is created at the first use, not by
    'Qt3DCore::QAspectManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QAspectManager.
  - Qt tells when it has removed the C++ Qt3DCore::QAspectManager. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DCore::QAspectManager that has no cute function yet,
    'addNodes', 'aspects', 'removeNodes', 'setRootEntity', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString Qt3DCore::QAspectManager::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#tr

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
    #  QString Qt3DCore::QAspectManager::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN8Qt3DCore14QAspectManager2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QAspectManager'

  #  Qt's Qt3DCore::QAspectManager is built on more than one class. The part
  #  of a C++ Qt3DCore::QAspectManager that belongs to a class after the
  #  first begins somewhere inside the object, and the ritual named for that
  #  class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'Qt3DCore::QAbstractFrontEndNodeManager':
          'ritual_cast_Qt3DCore_QAspectManager_Qt3DCore_QAbstractFrontEndNodeManager',
  }

  #  A C++ Qt3DCore::QAspectManager Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QAspectManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DCore::QAspectManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DCore::QAspectManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def engine(self) -> Optional[Qt3DCore.QAspectEngine]:
    """
    Calls Qt's 'QAspectEngine *Qt3DCore::QAspectManager::engine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#engine

    Returns
    -------

    Optional[Qt3DCore.QAspectEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectEngine *Qt3DCore::QAspectManager::engine() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager6engineEv',
    )
    return Qt3DCore.QAspectEngine._cuteAt(address)

  def scheduler(self) -> Optional[Qt3DCore.QScheduler]:
    """
    Calls Qt's 'QScheduler *Qt3DCore::QAspectManager::scheduler() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#scheduler

    Returns
    -------

    Optional[Qt3DCore.QScheduler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScheduler *Qt3DCore::QAspectManager::scheduler() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager9schedulerEv',
    )
    return Qt3DCore.QScheduler._cuteAt(address)

  def isShuttingDown(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QAspectManager::isShuttingDown() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#isShuttingDown
    """
    #  bool Qt3DCore::QAspectManager::isShuttingDown() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager14isShuttingDownEv',
    )

  @overload(str)
  def aspect(self, name: str) -> Optional[Qt3DCore.QAbstractAspect]:
    """
    Calls Qt's 'QAbstractAspect *Qt3DCore::QAspectManager::aspect(const
    QString &name) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#aspect

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspect *Qt3DCore::QAspectManager::aspect(const QString &name)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager6aspectERK7QString', name,
    )
    return Qt3DCore.QAbstractAspect._cuteAt(address)

  @overload(QMetaObject)
  @overload(NoneType)
  def aspect(
      self,
      metaType: Optional[QMetaObject],
  ) -> Optional[Qt3DCore.QAbstractAspect]:
    """
    Calls Qt's 'QAbstractAspect *Qt3DCore::QAspectManager::aspect(const
    QMetaObject *metaType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#aspect

    Parameters
    ----------

    metaType : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspect *Qt3DCore::QAspectManager::aspect(const QMetaObject
    #      *metaType) const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager6aspectEPK11QMetaObject',
        self._addressOf(metaType, 'QMetaObject'),
    )
    return Qt3DCore.QAbstractAspect._cuteAt(address)

  def jobManager(self) -> Optional[Qt3DCore.QAbstractAspectJobManager]:
    """
    Calls Qt's 'QAbstractAspectJobManager
    *Qt3DCore::QAspectManager::jobManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#jobManager

    Returns
    -------

    Optional[Qt3DCore.QAbstractAspectJobManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAspectJobManager *Qt3DCore::QAspectManager::jobManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager10jobManagerEv',
    )
    return Qt3DCore.QAbstractAspectJobManager._cuteAt(address)

  def changeArbiter(self) -> Optional[Qt3DCore.QChangeArbiter]:
    """
    Calls Qt's 'QChangeArbiter *Qt3DCore::QAspectManager::changeArbiter()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#changeArbiter

    Returns
    -------

    Optional[Qt3DCore.QChangeArbiter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChangeArbiter *Qt3DCore::QAspectManager::changeArbiter() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager13changeArbiterEv',
    )
    return Qt3DCore.QChangeArbiter._cuteAt(address)

  def serviceLocator(self) -> Optional[Qt3DCore.QServiceLocator]:
    """
    Calls Qt's 'QServiceLocator *Qt3DCore::QAspectManager::serviceLocator()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#serviceLocator

    Returns
    -------

    Optional[Qt3DCore.QServiceLocator]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QServiceLocator *Qt3DCore::QAspectManager::serviceLocator() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager14serviceLocatorEv',
    )
    return Qt3DCore.QServiceLocator._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QAspectManager::lookupNode(QNodeId id)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#lookupNode

    Parameters
    ----------

    id : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QAspectManager::lookupNode(QNodeId id) const
    ritual = 'ritual_ZNK8Qt3DCore14QAspectManager10lookupNodeENS_7QNodeIdE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8Qt3DCore14QAspectManager10lookupNodeENS_7QNodeIdE')
    address = self.uglySide.call(ritual, self._valueOf(id))
    return Qt3DCore.QNode._cuteAt(address)

  def scene(self) -> Optional[Qt3DCore.QScene]:
    """
    Calls Qt's 'QScene *Qt3DCore::QAspectManager::scene() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#scene

    Returns
    -------

    Optional[Qt3DCore.QScene]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScene *Qt3DCore::QAspectManager::scene() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager5sceneEv',
    )
    return Qt3DCore.QScene._cuteAt(address)

  def jobsInLastFrame(self) -> int:
    """
    Calls Qt's 'int Qt3DCore::QAspectManager::jobsInLastFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#jobsInLastFrame
    """
    #  int Qt3DCore::QAspectManager::jobsInLastFrame() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore14QAspectManager15jobsInLastFrameEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DCore.QAspectEngine.RunMode)
  def setRunMode(self, mode: Qt3DCore.QAspectEngine.RunMode) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAspectManager::setRunMode(QAspectEngine::RunMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#setRunMode

    Parameters
    ----------

    mode : Qt3DCore.QAspectEngine.RunMode
      Passed on as its number.
    """
    #  void Qt3DCore::QAspectManager::setRunMode(QAspectEngine::RunMode mode)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager10setRunModeENS_13QAspectEngine7'
        'RunModeE',
        mode.value,
    )

  @overload(WAIT['Qt3DCore.NodePostConstructorInit'])
  @overload(NoneType)
  def setPostConstructorInit(
      self,
      postConstructorInit: Optional[Qt3DCore.NodePostConstructorInit],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAspectManager::setPostConstructorInit(NodePostConstructorInit
    *postConstructorInit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html

    Parameters
    ----------

    postConstructorInit : Optional[Qt3DCore.NodePostConstructorInit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectManager::setPostConstructorInit(
    #      NodePostConstructorInit *postConstructorInit)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager22setPostConstructorInitEPNS_23N'
        'odePostConstructorInitE',
        self._addressOf(postConstructorInit),
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
  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def __init__(
      self,
      parent: Optional[Qt3DCore.QAspectEngine] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DCore::QAspectManager::QAspectManager(QAspectEngine *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#QAspectManager

    Parameters
    ----------

    parent : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QAspectManager::QAspectManager(QAspectEngine *parent)
    self._noteCreation(QAspectManager, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore14QAspectManagerC1EPNS_13QAspectEngineE',
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

  def enterSimulationLoop(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::enterSimulationLoop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#enterSimulationLoop
    """
    #  void Qt3DCore::QAspectManager::enterSimulationLoop()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager19enterSimulationLoopEv',
    )

  def exitSimulationLoop(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::exitSimulationLoop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#exitSimulationLoop
    """
    #  void Qt3DCore::QAspectManager::exitSimulationLoop()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager18exitSimulationLoopEv',
    )

  def initialize(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#initialize
    """
    #  void Qt3DCore::QAspectManager::initialize()
    self.uglySide.call('ritual_ZN8Qt3DCore14QAspectManager10initializeEv')

  def shutdown(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::shutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#shutdown
    """
    #  void Qt3DCore::QAspectManager::shutdown()
    self.uglySide.call('ritual_ZN8Qt3DCore14QAspectManager8shutdownEv')

  def processFrame(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::processFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#processFrame
    """
    #  void Qt3DCore::QAspectManager::processFrame()
    self.uglySide.call('ritual_ZN8Qt3DCore14QAspectManager12processFrameEv')

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def registerAspect(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAspectManager::registerAspect(Qt3DCore::QAbstractAspect
    *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#registerAspect

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void
    #      Qt3DCore::QAspectManager::registerAspect(Qt3DCore::QAbstractAspect
    #      *aspect)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager14registerAspectEPNS_15QAbstract'
        'AspectE',
        self._addressOf(aspect),
    )

  @overload(WAIT['Qt3DCore.QAbstractAspect'])
  @overload(NoneType)
  def unregisterAspect(
      self,
      aspect: Optional[Qt3DCore.QAbstractAspect],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DCore::QAspectManager::unregisterAspect(Qt3DCore::QAbstractAspect
    *aspect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#unregisterAspect

    Parameters
    ----------

    aspect : Optional[Qt3DCore.QAbstractAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QAspectManager::unregisterAspect(Qt3DCore::
    #      QAbstractAspect *aspect)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager16unregisterAspectEPNS_15QAbstra'
        'ctAspectE',
        self._addressOf(aspect),
    )

  def dumpJobsOnNextFrame(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::dumpJobsOnNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#dumpJobsOnNextFrame
    """
    #  void Qt3DCore::QAspectManager::dumpJobsOnNextFrame()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager19dumpJobsOnNextFrameEv',
    )

  def requestNextFrame(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QAspectManager::requestNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qaspectmanager.html#requestNextFrame
    """
    #  void Qt3DCore::QAspectManager::requestNextFrame()
    self.uglySide.call(
        'ritual_ZN8Qt3DCore14QAspectManager16requestNextFrameEv',
    )

  @staticmethod
  def addNodes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAspectManager::addNodes(const QList<QNode *>
    &nodes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectManager.addNodes' has no cute function yet. Qt's "
        "'void Qt3DCore::QAspectManager::addNodes(const QList<QNode *> "
        "&nodes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def aspects(*__, **_) -> Never:
    """
    Qt's 'const QList<QAbstractAspect *> &Qt3DCore::QAspectManager::aspects()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectManager.aspects' has no cute function yet. Qt's "
        "'const QList<QAbstractAspect *> "
        "&Qt3DCore::QAspectManager::aspects() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def removeNodes(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAspectManager::removeNodes(const QList<QNode *>
    &nodes)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectManager.removeNodes' has no cute function yet. "
        "Qt's 'void Qt3DCore::QAspectManager::removeNodes(const QList<QNode "
        "*> &nodes)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setRootEntity(*__, **_) -> Never:
    """
    Qt's 'void Qt3DCore::QAspectManager::setRootEntity(Qt3DCore::QEntity
    *root, const QList<QNode *> &nodes)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QAspectManager.setRootEntity' has no cute function yet. "
        "Qt's 'void "
        "Qt3DCore::QAspectManager::setRootEntity(Qt3DCore::QEntity *root, "
        "const QList<QNode *> &nodes)': takes a type Python has no way to "
        "hand over yet.")
