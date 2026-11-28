"""
Qt3DCore::QScene binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qscene_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means Qt3DCore::QScene to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteFlags, WAIT
from ..occult import Rituals
from . import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScene(Qt3DCore.QAbstractFrontEndNodeManager):
  """
  The cute side of Qt's Qt3DCore::QScene: a plain Python object standing in
  front of one C++ Qt3DCore::QScene.

  It is built on the cute 'Qt3DCore::QAbstractFrontEndNodeManager', as Qt's
  Qt3DCore::QScene is built on Qt's Qt3DCore::QAbstractFrontEndNodeManager,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DCore::QScene that has a ritual and that Python
  can call so far, 15 names in all: 'engine', 'addObservable',
  'removeObservable', 'lookupNode', 'rootNode', 'setArbiter', 'arbiter',
  'addEntityForComponent', 'removeEntityForComponent',
  'hasEntityForComponent', 'postConstructorInit', 'markDirty', 'dirtyBits',
  'clearDirtyBits', 'setRootNode'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::QScene::~QScene()': the destructor: Python never removes
    a C++ Qt3DCore::QScene.
  - Qt's 'QList<QNode *> Qt3DCore::QScene::lookupNodes(const QList<QNodeId>
    &ids) const': takes a type Python has no way to hand over yet.
  - Qt's 'QList<QNodeId> Qt3DCore::QScene::entitiesForComponent(QNodeId id)
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ Qt3DCore::QScene is created at the first use, not by
    'Qt3DCore::QScene(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DCore::QScene.
  - Each name of Qt's Qt3DCore::QScene that has no cute function yet,
    'd_func', 'entitiesForComponent', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside Qt3DCore::QScene, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DirtyNodeFlag(CuteFlags):
    """
    The flags enum 'Qt3DCore::QScene::DirtyNodeFlag' of Qt, with the 5 names
    Qt gives in it. Qt names the type of its combinations
    'Qt3DCore::QScene::DirtyNodeSet'.
    """

    TransformDirty = 0x1
    GeometryDirty = 0x2
    EntityEnabledDirty = 0x4
    BuffersDirty = 0x8
    AllDirty = 0xffffff

  DirtyNodeSet = DirtyNodeFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DCore::QScene'

  #  A C++ Qt3DCore::QScene Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DCore_QScene'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def engine(self) -> Optional[Qt3DCore.QAspectEngine]:
    """
    Calls Qt's 'QAspectEngine *Qt3DCore::QScene::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#engine

    Returns
    -------

    Optional[Qt3DCore.QAspectEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAspectEngine *Qt3DCore::QScene::engine() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QScene6engineEv')
    return Qt3DCore.QAspectEngine._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeId'])
  def lookupNode(self, id: Qt3DCore.QNodeId) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QScene::lookupNode(QNodeId id) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#lookupNode

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
    #  QNode *Qt3DCore::QScene::lookupNode(QNodeId id) const
    ritual = 'ritual_ZNK8Qt3DCore6QScene10lookupNodeENS_7QNodeIdE'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8Qt3DCore6QScene10lookupNodeENS_7QNodeIdE'
    address = self.uglySide.call(ritual, self._valueOf(id))
    return Qt3DCore.QNode._cuteAt(address)

  def rootNode(self) -> Optional[Qt3DCore.QNode]:
    """
    Calls Qt's 'QNode *Qt3DCore::QScene::rootNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#rootNode

    Returns
    -------

    Optional[Qt3DCore.QNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNode *Qt3DCore::QScene::rootNode() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QScene8rootNodeEv')
    return Qt3DCore.QNode._cuteAt(address)

  def arbiter(self) -> Optional[Qt3DCore.QChangeArbiter]:
    """
    Calls Qt's 'QChangeArbiter *Qt3DCore::QScene::arbiter() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#arbiter

    Returns
    -------

    Optional[Qt3DCore.QChangeArbiter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QChangeArbiter *Qt3DCore::QScene::arbiter() const
    address = self.uglySide.call('ritual_ZNK8Qt3DCore6QScene7arbiterEv')
    return Qt3DCore.QChangeArbiter._cuteAt(address)

  def postConstructorInit(
      self,
  ) -> Optional[Qt3DCore.NodePostConstructorInit]:
    """
    Calls Qt's 'NodePostConstructorInit
    *Qt3DCore::QScene::postConstructorInit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscene.html#postConstructorInit

    Returns
    -------

    Optional[Qt3DCore.NodePostConstructorInit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  NodePostConstructorInit *Qt3DCore::QScene::postConstructorInit() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore6QScene19postConstructorInitEv',
    )
    return Qt3DCore.NodePostConstructorInit._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QChangeArbiter'])
  @overload(NoneType)
  def setArbiter(self, arbiter: Optional[Qt3DCore.QChangeArbiter]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::setArbiter(QChangeArbiter *arbiter)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#setArbiter

    Parameters
    ----------

    arbiter : Optional[Qt3DCore.QChangeArbiter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QScene::setArbiter(QChangeArbiter *arbiter)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene10setArbiterEPNS_14QChangeArbiterE',
        self._addressOf(arbiter),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def setRootNode(self, root: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::setRootNode(QNode *root)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#setRootNode

    Parameters
    ----------

    root : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QScene::setRootNode(QNode *root)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene11setRootNodeEPNS_5QNodeE',
        self._addressOf(root),
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
      engine: Optional[Qt3DCore.QAspectEngine] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'Qt3DCore::QScene::QScene(QAspectEngine
    *engine)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#QScene

    Parameters
    ----------

    engine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DCore::QScene::QScene(QAspectEngine *engine)
    self._noteCreation(QScene, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore6QSceneC1EPNS_13QAspectEngineE',
        self._addressOf(engine),
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

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def addObservable(self, observable: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::addObservable(QNode *observable)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#addObservable

    Parameters
    ----------

    observable : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QScene::addObservable(QNode *observable)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene13addObservableEPNS_5QNodeE',
        self._addressOf(observable),
    )

  @overload(WAIT['Qt3DCore.QNode'])
  @overload(NoneType)
  def removeObservable(self, observable: Optional[Qt3DCore.QNode]) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::removeObservable(QNode *observable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscene.html#removeObservable

    Parameters
    ----------

    observable : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DCore::QScene::removeObservable(QNode *observable)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene16removeObservableEPNS_5QNodeE',
        self._addressOf(observable),
    )

  @overload(WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DCore.QNodeId'])
  def addEntityForComponent(
      self,
      componentUuid: Qt3DCore.QNodeId,
      entityUuid: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::addEntityForComponent(QNodeId
    componentUuid, QNodeId entityUuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscene.html#addEntityForComponent

    Parameters
    ----------

    componentUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    entityUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DCore::QScene::addEntityForComponent(QNodeId componentUuid,
    #      QNodeId entityUuid)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene21addEntityForComponentENS_7QNodeIdES1_',
        self._valueOf(componentUuid), self._valueOf(entityUuid),
    )

  @overload(WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DCore.QNodeId'])
  def removeEntityForComponent(
      self,
      componentUuid: Qt3DCore.QNodeId,
      entityUuid: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::removeEntityForComponent(QNodeId
    componentUuid, QNodeId entityUuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscene.html#removeEntityForComponent

    Parameters
    ----------

    componentUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    entityUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DCore::QScene::removeEntityForComponent(QNodeId componentUuid,
    #      QNodeId entityUuid)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene24removeEntityForComponentENS_7QNodeIdES1'
        '_',
        self._valueOf(componentUuid), self._valueOf(entityUuid),
    )

  @overload(WAIT['Qt3DCore.QNodeId'], WAIT['Qt3DCore.QNodeId'])
  def hasEntityForComponent(
      self,
      componentUuid: Qt3DCore.QNodeId,
      entityUuid: Qt3DCore.QNodeId,
  ) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::QScene::hasEntityForComponent(QNodeId
    componentUuid, QNodeId entityUuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscene.html#hasEntityForComponent

    Parameters
    ----------

    componentUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    entityUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  bool Qt3DCore::QScene::hasEntityForComponent(QNodeId componentUuid,
    #      QNodeId entityUuid)
    return self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene21hasEntityForComponentENS_7QNodeIdES1_',
        self._valueOf(componentUuid), self._valueOf(entityUuid),
    )

  @overload(DirtyNodeSet)
  def markDirty(self, changes: DirtyNodeSet) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::markDirty(DirtyNodeSet changes)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#markDirty

    Parameters
    ----------

    changes : DirtyNodeSet
      Passed on as its number.
    """
    #  void Qt3DCore::QScene::markDirty(DirtyNodeSet changes)
    self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene9markDirtyE6QFlagsINS0_13DirtyNodeFlagEE',
        changes.value,
    )

  def dirtyBits(self) -> DirtyNodeSet:
    """
    Calls Qt's 'DirtyNodeSet Qt3DCore::QScene::dirtyBits()'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dcore-qscene.html#dirtyBits

    Returns
    -------

    DirtyNodeSet
      The value standing for the combination Qt gave back.
    """
    #  DirtyNodeSet Qt3DCore::QScene::dirtyBits()
    return QScene.DirtyNodeSet(self.uglySide.call(
        'ritual_ZN8Qt3DCore6QScene9dirtyBitsEv',
    ))

  def clearDirtyBits(self) -> None:
    """
    Calls Qt's 'void Qt3DCore::QScene::clearDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-qscene.html#clearDirtyBits
    """
    #  void Qt3DCore::QScene::clearDirtyBits()
    self.uglySide.call('ritual_ZN8Qt3DCore6QScene14clearDirtyBitsEv')

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QScenePrivate *Qt3DCore::QScene::d_func()': the compiler refuses
      its ritual as it would be written here: unknown type name
      'QScenePrivate'; did you mean 'Qt3DCore::QScenePrivate'?.
    - Qt's 'const QScenePrivate *Qt3DCore::QScene::d_func() const': the
      compiler refuses its ritual as it would be written here: unknown type
      name 'QScenePrivate'; did you mean 'Qt3DCore::QScenePrivate'?.
    """
    raise NotImplementedError(
        "'Qt3DCore.QScene.d_func' has no cute function yet. Qt's "
        "'QScenePrivate *Qt3DCore::QScene::d_func()': the compiler refuses "
        "its ritual as it would be written here: unknown type name "
        "'QScenePrivate'; did you mean 'Qt3DCore::QScenePrivate'?. Qt's "
        "'const QScenePrivate *Qt3DCore::QScene::d_func() const': the "
        "compiler refuses its ritual as it would be written here: unknown "
        "type name 'QScenePrivate'; did you mean 'Qt3DCore::QScenePrivate'?."
    )

  @staticmethod
  def entitiesForComponent(*__, **_) -> Never:
    """
    Qt's 'QList<QNodeId> Qt3DCore::QScene::entitiesForComponent(QNodeId id)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DCore.QScene.entitiesForComponent' has no cute function yet. "
        "Qt's 'QList<QNodeId> "
        "Qt3DCore::QScene::entitiesForComponent(QNodeId id) const': gives a "
        "type Python has no way to take yet.")
