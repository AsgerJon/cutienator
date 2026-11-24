//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/entity_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/entity_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::EntityPrivate that Python can take functions over in. Every Qt3DRender::Render::EntityPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_EntityPrivateCall0)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DRender_Render_EntityPrivateCall1)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DRender_Render_EntityPrivateCall2)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DRender_Render_EntityPrivateCall3)(const void *, Qt3DCore::QNode *, int *);
class CuteQt3DRender_Render_EntityPrivate : public Qt3DRender::Render::EntityPrivate {
public:
  using Qt3DRender::Render::EntityPrivate::EntityPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNodeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNodeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QNodeE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void
  //      Qt3DRender::Render::EntityPrivate::componentAdded(Qt3DCore::QNode
  //      *frontend)
  void componentAdded(Qt3DCore::QNode *frontend) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_EntityPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Render_EntityPrivateCall0>(taken[0]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::EntityPrivate::componentAdded(frontend);
  }

  //  void
  //      Qt3DRender::Render::EntityPrivate::componentRemoved(Qt3DCore::QNo
  //      de *frontend)
  void componentRemoved(Qt3DCore::QNode *frontend) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_EntityPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Render_EntityPrivateCall1>(taken[1]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::EntityPrivate::componentRemoved(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode *frontend)
  void addedToEntity(Qt3DCore::QNode *frontend) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_EntityPrivateCall2 call = reinterpret_cast<CuteQt3DRender_Render_EntityPrivateCall2>(taken[2]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::addedToEntity(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode
  //      *frontend)
  void removedFromEntity(Qt3DCore::QNode *frontend) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Render_EntityPrivateCall3 call = reinterpret_cast<CuteQt3DRender_Render_EntityPrivateCall3>(taken[3]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::removedFromEntity(frontend);
  }
};

//  Entity *Qt3DRender::Render::EntityPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity *ritual_ZN10Qt3DRender6Render13EntityPrivate6q_funcEv(
    Qt3DRender::Render::EntityPrivate *self) {
  return self->q_func();
}

//  const Entity *Qt3DRender::Render::EntityPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Entity *ritual_ZNK10Qt3DRender6Render13EntityPrivate6q_funcEv(
    const Qt3DRender::Render::EntityPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_Render_EntityPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_EntityPrivate(
    Qt3DRender::Render::EntityPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_EntityPrivate *>(self)->take(key, call);
}
