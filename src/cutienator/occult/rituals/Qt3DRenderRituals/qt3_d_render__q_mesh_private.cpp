//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QMeshPrivate that Python can take functions over in. Every Qt3DRender::QMeshPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QMeshPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QMeshPrivateCall1)(const void *, Qt3DCore::QGeometryView *, int *);
typedef void (*CuteQt3DRender_QMeshPrivateCall2)(const void *, int *);
class CuteQt3DRender_QMeshPrivate : public Qt3DRender::QMeshPrivate {
public:
  using Qt3DRender::QMeshPrivate::QMeshPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGeometryViewE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::QMeshPrivate::setScene(Qt3DCore::QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QMeshPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QMeshPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DRender::QMeshPrivate::setScene(scene);
  }

  //  void
  //      Qt3DRender::QGeometryRendererPrivate::setView(Qt3DCore::QGeometry
  //      View *view)
  void setView(Qt3DCore::QGeometryView *view) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QMeshPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QMeshPrivateCall1>(taken[1]);
      call(this, view, &handled);
      if (handled) return;
    }
    Qt3DRender::QGeometryRendererPrivate::setView(view);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QMeshPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QMeshPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QMeshPrivate::QMeshPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QMeshPrivate *ritual_ZN10Qt3DRender12QMeshPrivateC1Ev() {
  return new CuteQt3DRender_QMeshPrivate();
}

//  QMesh *Qt3DRender::QMeshPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QMesh *ritual_ZN10Qt3DRender12QMeshPrivate6q_funcEv(
    Qt3DRender::QMeshPrivate *self) {
  return self->q_func();
}

//  const QMesh *Qt3DRender::QMeshPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QMesh *ritual_ZNK10Qt3DRender12QMeshPrivate6q_funcEv(
    const Qt3DRender::QMeshPrivate *self) {
  return self->q_func();
}

//  QMeshPrivate *Qt3DRender::QMeshPrivate::get(QMesh *q)
extern "C" Q_DECL_EXPORT
Qt3DRender::QMeshPrivate *ritual_ZN10Qt3DRender12QMeshPrivate3getEPNS_5QMeshE(
    Qt3DRender::QMesh *q) {
  return Qt3DRender::QMeshPrivate::get(q);
}

//  void Qt3DRender::QMeshPrivate::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QMeshPrivate8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DRender::QMeshPrivate *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  void Qt3DRender::QMeshPrivate::updateFunctor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QMeshPrivate13updateFunctorEv(
    Qt3DRender::QMeshPrivate *self) {
  self->updateFunctor();
}

//  void Qt3DRender::QMeshPrivate::setStatus(QMesh::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QMeshPrivate9setStatusENS_5QMesh6StatusE(
    Qt3DRender::QMeshPrivate *self,
    Qt3DRender::QMesh::Status status) {
  self->setStatus(status);
}

//  a Python function taken by a CuteQt3DRender_QMeshPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QMeshPrivate(
    Qt3DRender::QMeshPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QMeshPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QMeshPrivate::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender12QMeshPrivate8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DRender::QMeshPrivate *self,
    Qt3DCore::QScene *scene) {
  self->Qt3DRender::QMeshPrivate::setScene(scene);
}
