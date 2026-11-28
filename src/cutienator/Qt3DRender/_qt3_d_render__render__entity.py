"""
Qt3DRender::Render::Entity binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::Render::Entity to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QMatrix4x4

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Entity(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Entity: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Entity.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Entity is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Entity that has a ritual and
  that Python can call so far, 23 names in all: 'cleanup', 'setNodeManagers',
  'syncFromFrontEnd', 'dump', 'parent', 'removeFromParentChildHandles',
  'hasChildren', 'worldTransform', 'isParentLessTransform',
  'setParentLessTransform', 'localBoundingVolume', 'worldBoundingVolume',
  'worldBoundingVolumeWithChildren', 'addComponent', 'removeComponent',
  'isBoundingVolumeDirty', 'unsetBoundingVolumeDirty', 'setTreeEnabled',
  'isTreeEnabled', 'addRecursiveLayerId', 'removeRecursiveLayerId',
  'clearRecursiveLayerIds', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::Entity::~Entity()': the destructor: Python
    never removes a C++ Qt3DRender::Render::Entity.
  - Qt's 'void Qt3DRender::Render::Entity::setParentHandle(HEntity
    parentHandle)': takes a type Python has no way to hand over yet.
  - Qt's 'void Qt3DRender::Render::Entity::setHandle(HEntity handle)': takes
    a type Python has no way to hand over yet.
  - Qt's 'HEntity Qt3DRender::Render::Entity::handle() const': gives a type
    Python has no way to take yet.
  - Qt's 'HEntity Qt3DRender::Render::Entity::parentHandle() const': gives a
    type Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::Entity::removeChildHandle(HEntity
    childHandle)': takes a type Python has no way to hand over yet.
  - Qt's 'const QList<HEntity> &Qt3DRender::Render::Entity::childrenHandles()
    const': gives a type Python has no way to take yet.
  - Qt's 'QList<Entity *> Qt3DRender::Render::Entity::children() const':
    gives a type Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::Entity::traverse(const std::function<void
    (Entity *)> &operation)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void Qt3DRender::Render::Entity::traverse(const std::function<void
    (const Entity *)> &operation) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'const Matrix4x4 *Qt3DRender::Render::Entity::worldTransform()
    const': takes in Python what 'Matrix4x4
    *Qt3DRender::Render::Entity::worldTransform()' takes.
  - Qt's 'Qt3DCore::QNodeIdVector Qt3DRender::Render::Entity::layerIds()
    const': gives a type Python has no way to take yet.
  - Qt's 'const EntityPrivate *Qt3DRender::Render::Entity::d_func() const':
    takes in Python what 'EntityPrivate
    *Qt3DRender::Render::Entity::d_func()' takes.

  What has no ritual
  ------------------

  9 of the 46 functions Qt declares: 8 a template; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Entity is created at the first use, not by
    'Qt3DRender::Render::Entity(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Entity.
  - Each name of Qt's Qt3DRender::Render::Entity that has no cute function
    yet, 'appendChildHandle', 'children', 'childrenHandles',
    'componentHandle', 'componentUuid', 'componentsHandle', 'componentsUuid',
    'containsComponentsOfType', 'handle', 'layerIds', 'parentHandle',
    'removeChildHandle', 'renderComponent', 'renderComponents', 'setHandle',
    'setParentHandle', 'traverse', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Entity'

  #  A C++ Qt3DRender::Render::Entity Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_Entity'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parent(self) -> Optional[Entity]:
    """
    Calls Qt's 'Entity *Qt3DRender::Render::Entity::parent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#parent

    Returns
    -------

    Optional[Entity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Entity *Qt3DRender::Render::Entity::parent() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity6parentEv',
    )
    return Entity._cuteAt(address)

  def hasChildren(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Entity::hasChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#hasChildren
    """
    #  bool Qt3DRender::Render::Entity::hasChildren() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity11hasChildrenEv',
    )

  def isParentLessTransform(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Entity::isParentLessTransform()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html
    """
    #  bool Qt3DRender::Render::Entity::isParentLessTransform() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity21isParentLessTransformEv',
    )

  def localBoundingVolume(self) -> Optional[Qt3DRender.Render.Sphere]:
    """
    Calls Qt's 'Sphere *Qt3DRender::Render::Entity::localBoundingVolume()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#localBoundingVolume

    Returns
    -------

    Optional[Qt3DRender.Render.Sphere]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Sphere *Qt3DRender::Render::Entity::localBoundingVolume() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity19localBoundingVolumeEv',
    )
    return Qt3DRender.Render.Sphere._cuteAt(address)

  def worldBoundingVolume(self) -> Optional[Qt3DRender.Render.Sphere]:
    """
    Calls Qt's 'Sphere *Qt3DRender::Render::Entity::worldBoundingVolume()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#worldBoundingVolume

    Returns
    -------

    Optional[Qt3DRender.Render.Sphere]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Sphere *Qt3DRender::Render::Entity::worldBoundingVolume() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity19worldBoundingVolumeEv',
    )
    return Qt3DRender.Render.Sphere._cuteAt(address)

  def worldBoundingVolumeWithChildren(
      self,
  ) -> Optional[Qt3DRender.Render.Sphere]:
    """
    Calls Qt's 'Sphere
    *Qt3DRender::Render::Entity::worldBoundingVolumeWithChildren() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html

    Returns
    -------

    Optional[Qt3DRender.Render.Sphere]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Sphere *Qt3DRender::Render::Entity::worldBoundingVolumeWithChildren()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity31worldBoundingVolumeWithChild'
        'renEv',
    )
    return Qt3DRender.Render.Sphere._cuteAt(address)

  def isBoundingVolumeDirty(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Entity::isBoundingVolumeDirty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html
    """
    #  bool Qt3DRender::Render::Entity::isBoundingVolumeDirty() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity21isBoundingVolumeDirtyEv',
    )

  def isTreeEnabled(self) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::Render::Entity::isTreeEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#isTreeEnabled
    """
    #  bool Qt3DRender::Render::Entity::isTreeEnabled() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render6Entity13isTreeEnabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManagers(
      self,
      manager: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::setNodeManagers(NodeManagers
    *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#setNodeManagers

    Parameters
    ----------

    manager : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::Entity::setNodeManagers(NodeManagers
    #      *manager)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity15setNodeManagersEPNS0_12NodeMa'
        'nagersE',
        self._addressOf(manager),
    )

  @overload(bool)
  def setParentLessTransform(self, v: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::setParentLessTransform(bool
    v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html

    Parameters
    ----------

    v : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Entity::setParentLessTransform(bool v)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity22setParentLessTransformEb', v,
    )

  @overload(bool)
  def setTreeEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::setTreeEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#setTreeEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Entity::setTreeEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity14setTreeEnabledEb', enabled,
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
    Notes what was given, for Qt's 'Qt3DRender::Render::Entity::Entity()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#Entity
    """
    #  Qt3DRender::Render::Entity::Entity()
    self._noteCreation(Entity, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render6EntityC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#cleanup
    """
    #  void Qt3DRender::Render::Entity::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render6Entity7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Entity::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render6Entity16syncFromFrontEndEPKN8Qt3DCore'
        '5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render6Entity16syncFromFrontEndEPKN8Qt'
          '3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  def dump(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::dump() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-render-entity.html#dump
    """
    #  void Qt3DRender::Render::Entity::dump() const
    self.uglySide.call('ritual_ZNK10Qt3DRender6Render6Entity4dumpEv')

  def removeFromParentChildHandles(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Entity::removeFromParentChildHandles()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html
    """
    #  void Qt3DRender::Render::Entity::removeFromParentChildHandles()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity28removeFromParentChildHandlesE'
        'v',
    )

  def worldTransform(self) -> Optional[QMatrix4x4]:
    """
    Calls Qt's 'Matrix4x4 *Qt3DRender::Render::Entity::worldTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#worldTransform

    Returns
    -------

    Optional[QMatrix4x4]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Matrix4x4 *Qt3DRender::Render::Entity::worldTransform()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity14worldTransformEv',
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteAt(address)

  @overload(WAIT['Qt3DCore.QNodeIdTypePair'])
  def addComponent(self, idAndType: Qt3DCore.QNodeIdTypePair) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Entity::addComponent(Qt3DCore::QNodeIdTypePair
    idAndType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#addComponent

    Parameters
    ----------

    idAndType : Qt3DCore.QNodeIdTypePair
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeIdTypePair, which
      stays Python's own.
    """
    #  void
    #      Qt3DRender::Render::Entity::addComponent(Qt3DCore::QNodeIdTypePair
    #      idAndType)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity12addComponentEN8Qt3DCore15QNod'
        'eIdTypePairE',
        self._valueOf(idAndType),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeComponent(self, nodeId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::Entity::removeComponent(Qt3DCore::QNodeId nodeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#removeComponent

    Parameters
    ----------

    nodeId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Entity::removeComponent(Qt3DCore::QNodeId
    #      nodeId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity15removeComponentEN8Qt3DCore7QN'
        'odeIdE',
        self._valueOf(nodeId),
    )

  def unsetBoundingVolumeDirty(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::unsetBoundingVolumeDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html
    """
    #  void Qt3DRender::Render::Entity::unsetBoundingVolumeDirty()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity24unsetBoundingVolumeDirtyEv',
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def addRecursiveLayerId(self, layerId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::addRecursiveLayerId(const
    Qt3DCore::QNodeId layerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#addRecursiveLayerId

    Parameters
    ----------

    layerId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Entity::addRecursiveLayerId(const
    #      Qt3DCore::QNodeId layerId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity19addRecursiveLayerIdEN8Qt3DCor'
        'e7QNodeIdE',
        self._valueOf(layerId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeRecursiveLayerId(self, layerId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::removeRecursiveLayerId(const
    Qt3DCore::QNodeId layerId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html

    Parameters
    ----------

    layerId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::Entity::removeRecursiveLayerId(const
    #      Qt3DCore::QNodeId layerId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity22removeRecursiveLayerIdEN8Qt3D'
        'Core7QNodeIdE',
        self._valueOf(layerId),
    )

  def clearRecursiveLayerIds(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Entity::clearRecursiveLayerIds()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html
    """
    #  void Qt3DRender::Render::Entity::clearRecursiveLayerIds()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity22clearRecursiveLayerIdsEv',
    )

  def d_func(self) -> Optional[Qt3DRender.Render.EntityPrivate]:
    """
    Calls Qt's 'EntityPrivate *Qt3DRender::Render::Entity::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-entity.html#d_func

    Returns
    -------

    Optional[Qt3DRender.Render.EntityPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  EntityPrivate *Qt3DRender::Render::Entity::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render6Entity6d_funcEv',
    )
    return Qt3DRender.Render.EntityPrivate._cuteAt(address)

  @staticmethod
  def appendChildHandle(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Entity::appendChildHandle(HEntity
    childHandle)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.appendChildHandle' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::Render::Entity::appendChildHandle(HEntity "
        "childHandle)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def children(*__, **_) -> Never:
    """
    Qt's 'QList<Entity *> Qt3DRender::Render::Entity::children() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.children' has no cute function yet. Qt's "
        "'QList<Entity *> Qt3DRender::Render::Entity::children() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def childrenHandles(*__, **_) -> Never:
    """
    Qt's 'const QList<HEntity> &Qt3DRender::Render::Entity::childrenHandles()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.childrenHandles' has no cute function "
        "yet. Qt's 'const QList<HEntity> "
        "&Qt3DRender::Render::Entity::childrenHandles() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def componentHandle(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::componentHandle': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.componentHandle' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::Entity::componentHandle': a "
        "template: a pattern and no single function.")

  @staticmethod
  def componentUuid(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::componentUuid': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.componentUuid' has no cute function yet. "
        "Qt's 'Qt3DRender::Render::Entity::componentUuid': a template: a "
        "pattern and no single function.")

  @staticmethod
  def componentsHandle(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::componentsHandle': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.componentsHandle' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::Entity::componentsHandle': a "
        "template: a pattern and no single function.")

  @staticmethod
  def componentsUuid(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::componentsUuid': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.componentsUuid' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::Entity::componentsUuid': a "
        "template: a pattern and no single function.")

  @staticmethod
  def containsComponentsOfType(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::containsComponentsOfType': a template:
    a pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.containsComponentsOfType' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::Render::Entity::containsComponentsOfType': a "
        "template: a pattern and no single function.")

  @staticmethod
  def handle(*__, **_) -> Never:
    """
    Qt's 'HEntity Qt3DRender::Render::Entity::handle() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.handle' has no cute function yet. Qt's "
        "'HEntity Qt3DRender::Render::Entity::handle() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def layerIds(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QNodeIdVector Qt3DRender::Render::Entity::layerIds()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.layerIds' has no cute function yet. Qt's "
        "'Qt3DCore::QNodeIdVector Qt3DRender::Render::Entity::layerIds() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def parentHandle(*__, **_) -> Never:
    """
    Qt's 'HEntity Qt3DRender::Render::Entity::parentHandle() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.parentHandle' has no cute function yet. "
        "Qt's 'HEntity Qt3DRender::Render::Entity::parentHandle() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def removeChildHandle(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Entity::removeChildHandle(HEntity
    childHandle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.removeChildHandle' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::Render::Entity::removeChildHandle(HEntity "
        "childHandle)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def renderComponent(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::renderComponent': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.renderComponent' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::Entity::renderComponent': a "
        "template: a pattern and no single function.")

  @staticmethod
  def renderComponents(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::Render::Entity::renderComponents': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.renderComponents' has no cute function "
        "yet. Qt's 'Qt3DRender::Render::Entity::renderComponents': a "
        "template: a pattern and no single function.")

  @staticmethod
  def setHandle(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Entity::setHandle(HEntity handle)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.setHandle' has no cute function yet. "
        "Qt's 'void Qt3DRender::Render::Entity::setHandle(HEntity handle)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setParentHandle(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::Entity::setParentHandle(HEntity
    parentHandle)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.setParentHandle' has no cute function "
        "yet. Qt's 'void "
        "Qt3DRender::Render::Entity::setParentHandle(HEntity "
        "parentHandle)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def traverse(*__, **_) -> Never:
    """
    - Qt's 'void Qt3DRender::Render::Entity::traverse(const
      std::function<void (Entity *)> &operation)': takes a type Python has no
      way to hand over yet.
    - Qt's 'void Qt3DRender::Render::Entity::traverse(const
      std::function<void (const Entity *)> &operation) const': takes a type
      Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.Entity.traverse' has no cute function yet. Qt's "
        "'void Qt3DRender::Render::Entity::traverse(const "
        "std::function<void (Entity *)> &operation)': takes a type Python "
        "has no way to hand over yet. Qt's 'void "
        "Qt3DRender::Render::Entity::traverse(const std::function<void "
        "(const Entity *)> &operation) const': takes a type Python has no "
        "way to hand over yet.")
