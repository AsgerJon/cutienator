//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, instances of templates of the class:
//  18. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>
#include <QtCore/qlist.h>

//  A Qt3DRender::Render::Entity that Python can take functions over in. Every Qt3DRender::Render::Entity
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_EntityCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Entity : public Qt3DRender::Render::Entity {
public:
  using Qt3DRender::Render::Entity::Entity;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Entity::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_EntityCall0 call = reinterpret_cast<CuteQt3DRender_Render_EntityCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Entity::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Entity::Entity()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity *ritual_ZN10Qt3DRender6Render6EntityC1Ev() {
  return new CuteQt3DRender_Render_Entity();
}

//  Qt3DRender::Render::Entity::~Entity()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6EntityD1Ev(
    Qt3DRender::Render::Entity *self) {
  delete self;
}

//  void Qt3DRender::Render::Entity::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity7cleanupEv(
    Qt3DRender::Render::Entity *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Entity::setParentHandle(HEntity parentHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity15setParentHandleEN8Qt3DCore7QHandleIS1_EE(
    Qt3DRender::Render::Entity *self,
    const Qt3DRender::Render::HEntity *parentHandle) {
  self->setParentHandle(*parentHandle);
}

//  void Qt3DRender::Render::Entity::setNodeManagers(NodeManagers *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity15setNodeManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::Entity *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setNodeManagers(manager);
}

//  void Qt3DRender::Render::Entity::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Entity *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::Entity::dump() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render6Entity4dumpEv(
    const Qt3DRender::Render::Entity *self) {
  self->dump();
}

//  void Qt3DRender::Render::Entity::setHandle(HEntity handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity9setHandleEN8Qt3DCore7QHandleIS1_EE(
    Qt3DRender::Render::Entity *self,
    const Qt3DRender::Render::HEntity *handle) {
  self->setHandle(*handle);
}

//  HEntity Qt3DRender::Render::Entity::handle() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::HEntity *ritual_ZNK10Qt3DRender6Render6Entity6handleEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DRender::Render::HEntity(self->handle());
}

//  Entity *Qt3DRender::Render::Entity::parent() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity *ritual_ZNK10Qt3DRender6Render6Entity6parentEv(
    const Qt3DRender::Render::Entity *self) {
  return self->parent();
}

//  HEntity Qt3DRender::Render::Entity::parentHandle() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::HEntity *ritual_ZNK10Qt3DRender6Render6Entity12parentHandleEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DRender::Render::HEntity(self->parentHandle());
}

//  void Qt3DRender::Render::Entity::removeFromParentChildHandles()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity28removeFromParentChildHandlesEv(
    Qt3DRender::Render::Entity *self) {
  self->removeFromParentChildHandles();
}

//  void Qt3DRender::Render::Entity::removeChildHandle(HEntity childHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity17removeChildHandleEN8Qt3DCore7QHandleIS1_EE(
    Qt3DRender::Render::Entity *self,
    const Qt3DRender::Render::HEntity *childHandle) {
  self->removeChildHandle(*childHandle);
}

//  const QList<HEntity> &Qt3DRender::Render::Entity::childrenHandles() const
extern "C" Q_DECL_EXPORT
const QList<Qt3DRender::Render::HEntity> *ritual_ZNK10Qt3DRender6Render6Entity15childrenHandlesEv(
    const Qt3DRender::Render::Entity *self) {
  return &(self->childrenHandles());
}

//  QList<Entity *> Qt3DRender::Render::Entity::children() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::Render::Entity *> *ritual_ZNK10Qt3DRender6Render6Entity8childrenEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DRender::Render::Entity *>(self->children());
}

//  bool Qt3DRender::Render::Entity::hasChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity11hasChildrenEv(
    const Qt3DRender::Render::Entity *self) {
  return self->hasChildren();
}

//  void Qt3DRender::Render::Entity::traverse(const std::function<void
//      (Entity *)> &operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity8traverseERKSt8functionIFvPS1_EE(
    Qt3DRender::Render::Entity *self,
    const std::function<void (Qt3DRender::Render::Entity *)> *operation) {
  self->traverse(*operation);
}

//  void Qt3DRender::Render::Entity::traverse(const std::function<void (const
//      Entity *)> &operation) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender6Render6Entity8traverseERKSt8functionIFvPKS1_EE(
    const Qt3DRender::Render::Entity *self,
    const std::function<void (const Qt3DRender::Render::Entity *)> *operation) {
  self->traverse(*operation);
}

//  Matrix4x4 *Qt3DRender::Render::Entity::worldTransform()
extern "C" Q_DECL_EXPORT
Matrix4x4 *ritual_ZN10Qt3DRender6Render6Entity14worldTransformEv(
    Qt3DRender::Render::Entity *self) {
  return self->worldTransform();
}

//  const Matrix4x4 *Qt3DRender::Render::Entity::worldTransform() const
extern "C" Q_DECL_EXPORT
const Matrix4x4 *ritual_ZNK10Qt3DRender6Render6Entity14worldTransformEv(
    const Qt3DRender::Render::Entity *self) {
  return self->worldTransform();
}

//  bool Qt3DRender::Render::Entity::isParentLessTransform() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity21isParentLessTransformEv(
    const Qt3DRender::Render::Entity *self) {
  return self->isParentLessTransform();
}

//  void Qt3DRender::Render::Entity::setParentLessTransform(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity22setParentLessTransformEb(
    Qt3DRender::Render::Entity *self,
    bool v) {
  self->setParentLessTransform(v);
}

//  Sphere *Qt3DRender::Render::Entity::localBoundingVolume() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Sphere *ritual_ZNK10Qt3DRender6Render6Entity19localBoundingVolumeEv(
    const Qt3DRender::Render::Entity *self) {
  return self->localBoundingVolume();
}

//  Sphere *Qt3DRender::Render::Entity::worldBoundingVolume() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Sphere *ritual_ZNK10Qt3DRender6Render6Entity19worldBoundingVolumeEv(
    const Qt3DRender::Render::Entity *self) {
  return self->worldBoundingVolume();
}

//  Sphere *Qt3DRender::Render::Entity::worldBoundingVolumeWithChildren()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Sphere *ritual_ZNK10Qt3DRender6Render6Entity31worldBoundingVolumeWithChildrenEv(
    const Qt3DRender::Render::Entity *self) {
  return self->worldBoundingVolumeWithChildren();
}

//  void Qt3DRender::Render::Entity::addComponent(Qt3DCore::QNodeIdTypePair
//      idAndType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity12addComponentEN8Qt3DCore15QNodeIdTypePairE(
    Qt3DRender::Render::Entity *self,
    const Qt3DCore::QNodeIdTypePair *idAndType) {
  self->addComponent(*idAndType);
}

//  void Qt3DRender::Render::Entity::removeComponent(Qt3DCore::QNodeId
//      nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity15removeComponentEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Entity *self,
    const Qt3DCore::QNodeId *nodeId) {
  self->removeComponent(*nodeId);
}

//  bool Qt3DRender::Render::Entity::isBoundingVolumeDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity21isBoundingVolumeDirtyEv(
    const Qt3DRender::Render::Entity *self) {
  return self->isBoundingVolumeDirty();
}

//  void Qt3DRender::Render::Entity::unsetBoundingVolumeDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity24unsetBoundingVolumeDirtyEv(
    Qt3DRender::Render::Entity *self) {
  self->unsetBoundingVolumeDirty();
}

//  void Qt3DRender::Render::Entity::setTreeEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity14setTreeEnabledEb(
    Qt3DRender::Render::Entity *self,
    bool enabled) {
  self->setTreeEnabled(enabled);
}

//  bool Qt3DRender::Render::Entity::isTreeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity13isTreeEnabledEv(
    const Qt3DRender::Render::Entity *self) {
  return self->isTreeEnabled();
}

//  Qt3DCore::QNodeIdVector Qt3DRender::Render::Entity::layerIds() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdVector *ritual_ZNK10Qt3DRender6Render6Entity8layerIdsEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QNodeIdVector(self->layerIds());
}

//  void Qt3DRender::Render::Entity::addRecursiveLayerId(const
//      Qt3DCore::QNodeId layerId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity19addRecursiveLayerIdEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Entity *self,
    const Qt3DCore::QNodeId *layerId) {
  self->addRecursiveLayerId(*layerId);
}

//  void Qt3DRender::Render::Entity::removeRecursiveLayerId(const
//      Qt3DCore::QNodeId layerId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity22removeRecursiveLayerIdEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Entity *self,
    const Qt3DCore::QNodeId *layerId) {
  self->removeRecursiveLayerId(*layerId);
}

//  void Qt3DRender::Render::Entity::clearRecursiveLayerIds()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Entity22clearRecursiveLayerIdsEv(
    Qt3DRender::Render::Entity *self) {
  self->clearRecursiveLayerIds();
}

//  EntityPrivate *Qt3DRender::Render::Entity::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EntityPrivate *ritual_ZN10Qt3DRender6Render6Entity6d_funcEv(
    Qt3DRender::Render::Entity *self) {
  return self->d_func();
}

//  const EntityPrivate *Qt3DRender::Render::Entity::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::EntityPrivate *ritual_ZNK10Qt3DRender6Render6Entity6d_funcEv(
    const Qt3DRender::Render::Entity *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_Render_Entity, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Entity(
    Qt3DRender::Render::Entity *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Entity *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Entity::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render6Entity16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Entity *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Entity::syncFromFrontEnd(frontEnd, firstTime);
}

//  a Qt3DRender::Render::HEntity a ritual of Qt3DRender::Render::Entity gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Entity__Qt3DRender_Render_HEntity(
    Qt3DRender::Render::HEntity *self) {
  delete self;
}

//  a QList<Qt3DRender::Render::Entity *> a ritual of
//      Qt3DRender::Render::Entity gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Entity__QList_Qt3DRender_Render_Entity(
    QList<Qt3DRender::Render::Entity *> *self) {
  delete self;
}

//  a Qt3DCore::QNodeIdVector a ritual of Qt3DRender::Render::Entity gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Entity__Qt3DCore_QNodeIdVector(
    Qt3DCore::QNodeIdVector *self) {
  delete self;
}

//  Qt3DCore::QHandle<Qt3DRender::Render::Material>
//      Qt3DRender::Render::Entity::componentHandle<Qt3DRender::Render::Material>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QHandle<Qt3DRender::Render::Material> * ritual_ZNK10Qt3DRender6Render6Entity15componentHandleINS0_8MaterialEEEN8Qt3DCore7QHandleIT_EEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QHandle<Qt3DRender::Render::Material>(self->componentHandle<Qt3DRender::Render::Material>());
}

//  Qt3DRender::Render::Material
//      *Qt3DRender::Render::Entity::renderComponent<Qt3DRender::Render::Material>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Material * ritual_ZNK10Qt3DRender6Render6Entity15renderComponentINS0_8MaterialEEEPT_v(
    const Qt3DRender::Render::Entity *self) {
  return self->renderComponent<Qt3DRender::Render::Material>();
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::Entity::componentUuid<Qt3DRender::Render::Material>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId * ritual_ZNK10Qt3DRender6Render6Entity13componentUuidINS0_8MaterialEEEN8Qt3DCore7QNodeIdEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QNodeId(self->componentUuid<Qt3DRender::Render::Material>());
}

//  bool
//      Qt3DRender::Render::Entity::containsComponentsOfType<Qt3DRender::Render::Material>()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity24containsComponentsOfTypeINS0_8MaterialEEEbv(
    const Qt3DRender::Render::Entity *self) {
  return self->containsComponentsOfType<Qt3DRender::Render::Material>();
}

//  Qt3DCore::QHandle<Qt3DRender::Render::Transform>
//      Qt3DRender::Render::Entity::componentHandle<Qt3DRender::Render::Transform>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QHandle<Qt3DRender::Render::Transform> * ritual_ZNK10Qt3DRender6Render6Entity15componentHandleINS0_9TransformEEEN8Qt3DCore7QHandleIT_EEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QHandle<Qt3DRender::Render::Transform>(self->componentHandle<Qt3DRender::Render::Transform>());
}

//  Qt3DRender::Render::Transform
//      *Qt3DRender::Render::Entity::renderComponent<Qt3DRender::Render::Transform>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Transform * ritual_ZNK10Qt3DRender6Render6Entity15renderComponentINS0_9TransformEEEPT_v(
    const Qt3DRender::Render::Entity *self) {
  return self->renderComponent<Qt3DRender::Render::Transform>();
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::Entity::componentUuid<Qt3DRender::Render::Transform>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId * ritual_ZNK10Qt3DRender6Render6Entity13componentUuidINS0_9TransformEEEN8Qt3DCore7QNodeIdEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QNodeId(self->componentUuid<Qt3DRender::Render::Transform>());
}

//  bool
//      Qt3DRender::Render::Entity::containsComponentsOfType<Qt3DRender::Render::Transform>()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity24containsComponentsOfTypeINS0_9TransformEEEbv(
    const Qt3DRender::Render::Entity *self) {
  return self->containsComponentsOfType<Qt3DRender::Render::Transform>();
}

//  Qt3DCore::QHandle<Qt3DRender::Render::CameraLens>
//      Qt3DRender::Render::Entity::componentHandle<Qt3DRender::Render::CameraLens>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QHandle<Qt3DRender::Render::CameraLens> * ritual_ZNK10Qt3DRender6Render6Entity15componentHandleINS0_10CameraLensEEEN8Qt3DCore7QHandleIT_EEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QHandle<Qt3DRender::Render::CameraLens>(self->componentHandle<Qt3DRender::Render::CameraLens>());
}

//  Qt3DRender::Render::CameraLens
//      *Qt3DRender::Render::Entity::renderComponent<Qt3DRender::Render::CameraLens>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::CameraLens * ritual_ZNK10Qt3DRender6Render6Entity15renderComponentINS0_10CameraLensEEEPT_v(
    const Qt3DRender::Render::Entity *self) {
  return self->renderComponent<Qt3DRender::Render::CameraLens>();
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::Entity::componentUuid<Qt3DRender::Render::CameraLens>()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId * ritual_ZNK10Qt3DRender6Render6Entity13componentUuidINS0_10CameraLensEEEN8Qt3DCore7QNodeIdEv(
    const Qt3DRender::Render::Entity *self) {
  return new Qt3DCore::QNodeId(self->componentUuid<Qt3DRender::Render::CameraLens>());
}

//  bool
//      Qt3DRender::Render::Entity::containsComponentsOfType<Qt3DRender::Render::CameraLens>()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity24containsComponentsOfTypeINS0_10CameraLensEEEbv(
    const Qt3DRender::Render::Entity *self) {
  return self->containsComponentsOfType<Qt3DRender::Render::CameraLens>();
}

//  QList<Qt3DCore::QHandle<Qt3DRender::Render::Layer>>
//      Qt3DRender::Render::Entity::componentsHandle<Qt3DRender::Render::Layer>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QHandle<Qt3DRender::Render::Layer>> * ritual_ZNK10Qt3DRender6Render6Entity16componentsHandleINS0_5LayerEEE5QListIN8Qt3DCore7QHandleIT_EEEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DCore::QHandle<Qt3DRender::Render::Layer>>(self->componentsHandle<Qt3DRender::Render::Layer>());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::Entity::componentsUuid<Qt3DRender::Render::Layer>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> * ritual_ZNK10Qt3DRender6Render6Entity14componentsUuidINS0_5LayerEEE5QListIN8Qt3DCore7QNodeIdEEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DCore::QNodeId>(self->componentsUuid<Qt3DRender::Render::Layer>());
}

//  QList<Qt3DCore::QHandle<Qt3DRender::Render::ShaderData>>
//      Qt3DRender::Render::Entity::componentsHandle<Qt3DRender::Render::ShaderData>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QHandle<Qt3DRender::Render::ShaderData>> * ritual_ZNK10Qt3DRender6Render6Entity16componentsHandleINS0_10ShaderDataEEE5QListIN8Qt3DCore7QHandleIT_EEEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DCore::QHandle<Qt3DRender::Render::ShaderData>>(self->componentsHandle<Qt3DRender::Render::ShaderData>());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::Entity::componentsUuid<Qt3DRender::Render::ShaderData>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> * ritual_ZNK10Qt3DRender6Render6Entity14componentsUuidINS0_10ShaderDataEEE5QListIN8Qt3DCore7QNodeIdEEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DCore::QNodeId>(self->componentsUuid<Qt3DRender::Render::ShaderData>());
}

//  QList<Qt3DCore::QHandle<Qt3DRender::Render::Light>>
//      Qt3DRender::Render::Entity::componentsHandle<Qt3DRender::Render::Light>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QHandle<Qt3DRender::Render::Light>> * ritual_ZNK10Qt3DRender6Render6Entity16componentsHandleINS0_5LightEEE5QListIN8Qt3DCore7QHandleIT_EEEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DCore::QHandle<Qt3DRender::Render::Light>>(self->componentsHandle<Qt3DRender::Render::Light>());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::Entity::componentsUuid<Qt3DRender::Render::Light>()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> * ritual_ZNK10Qt3DRender6Render6Entity14componentsUuidINS0_5LightEEE5QListIN8Qt3DCore7QNodeIdEEv(
    const Qt3DRender::Render::Entity *self) {
  return new QList<Qt3DCore::QNodeId>(self->componentsUuid<Qt3DRender::Render::Light>());
}
