//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

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

//  bool Qt3DRender::Render::Entity::hasChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Entity11hasChildrenEv(
    const Qt3DRender::Render::Entity *self) {
  return self->hasChildren();
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
