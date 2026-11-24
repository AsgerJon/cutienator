//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qcameraselector_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qcameraselector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QCameraSelectorPrivate that Python can take functions over in. Every Qt3DRender::QCameraSelectorPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QCameraSelectorPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QCameraSelectorPrivateCall1)(const void *, int *);
class CuteQt3DRender_QCameraSelectorPrivate : public Qt3DRender::QCameraSelectorPrivate {
public:
  using Qt3DRender::QCameraSelectorPrivate::QCameraSelectorPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QCameraSelectorPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QCameraSelectorPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QCameraSelectorPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QCameraSelectorPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QCameraSelector *Qt3DRender::QCameraSelectorPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QCameraSelector *ritual_ZN10Qt3DRender22QCameraSelectorPrivate6q_funcEv(
    Qt3DRender::QCameraSelectorPrivate *self) {
  return self->q_func();
}

//  const QCameraSelector *Qt3DRender::QCameraSelectorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QCameraSelector *ritual_ZNK10Qt3DRender22QCameraSelectorPrivate6q_funcEv(
    const Qt3DRender::QCameraSelectorPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QCameraSelectorPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QCameraSelectorPrivate(
    Qt3DRender::QCameraSelectorPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QCameraSelectorPrivate *>(self)->take(key, call);
}
