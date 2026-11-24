//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtechniquefilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtechniquefilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QTechniqueFilterPrivate that Python can take functions over in. Every Qt3DRender::QTechniqueFilterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QTechniqueFilterPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QTechniqueFilterPrivateCall1)(const void *, int *);
class CuteQt3DRender_QTechniqueFilterPrivate : public Qt3DRender::QTechniqueFilterPrivate {
public:
  using Qt3DRender::QTechniqueFilterPrivate::QTechniqueFilterPrivate;
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
      CuteQt3DRender_QTechniqueFilterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QTechniqueFilterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QTechniqueFilterPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QTechniqueFilter *Qt3DRender::QTechniqueFilterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTechniqueFilter *ritual_ZN10Qt3DRender23QTechniqueFilterPrivate6q_funcEv(
    Qt3DRender::QTechniqueFilterPrivate *self) {
  return self->q_func();
}

//  const QTechniqueFilter *Qt3DRender::QTechniqueFilterPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTechniqueFilter *ritual_ZNK10Qt3DRender23QTechniqueFilterPrivate6q_funcEv(
    const Qt3DRender::QTechniqueFilterPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QTechniqueFilterPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QTechniqueFilterPrivate(
    Qt3DRender::QTechniqueFilterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QTechniqueFilterPrivate *>(self)->take(key, call);
}
