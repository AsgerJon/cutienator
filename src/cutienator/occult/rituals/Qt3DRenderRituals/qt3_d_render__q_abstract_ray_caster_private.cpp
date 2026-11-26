//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qabstractraycaster_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qabstractraycaster_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QAbstractRayCasterPrivate that Python can take functions over in. Every Qt3DRender::QAbstractRayCasterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QAbstractRayCasterPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QAbstractRayCasterPrivateCall1)(const void *, int *);
class CuteQt3DRender_QAbstractRayCasterPrivate : public Qt3DRender::QAbstractRayCasterPrivate {
public:
  using Qt3DRender::QAbstractRayCasterPrivate::QAbstractRayCasterPrivate;
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
      CuteQt3DRender_QAbstractRayCasterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QAbstractRayCasterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QAbstractRayCasterPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QAbstractRayCasterPrivate::QAbstractRayCasterPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCasterPrivate *ritual_ZN10Qt3DRender25QAbstractRayCasterPrivateC1Ev() {
  return new CuteQt3DRender_QAbstractRayCasterPrivate();
}

//  QAbstractRayCasterPrivate
//      *Qt3DRender::QAbstractRayCasterPrivate::get(QAbstractRayCaster *obj)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCasterPrivate *ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate3getEPNS_18QAbstractRayCasterE(
    Qt3DRender::QAbstractRayCaster *obj) {
  return Qt3DRender::QAbstractRayCasterPrivate::get(obj);
}

//  const QAbstractRayCasterPrivate
//      *Qt3DRender::QAbstractRayCasterPrivate::get(const QAbstractRayCaster
//      *obj)
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractRayCasterPrivate *ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate3getEPKNS_18QAbstractRayCasterE(
    const Qt3DRender::QAbstractRayCaster *obj) {
  return Qt3DRender::QAbstractRayCasterPrivate::get(obj);
}

//  void Qt3DRender::QAbstractRayCasterPrivate::updateHitEntites(QAbstractRay
//      Caster::Hits &hits, Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate16updateHitEntitesER5QListINS_13QRayCasterHitEEPN8Qt3DCore6QSceneE(
    Qt3DRender::QAbstractRayCaster::Hits *hits,
    Qt3DCore::QScene *scene) {
  Qt3DRender::QAbstractRayCasterPrivate::updateHitEntites(*hits, scene);
}

//  QAbstractRayCaster::Hits Qt3DRender::QAbstractRayCasterPrivate::pick()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::Hits *ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate4pickEv(
    Qt3DRender::QAbstractRayCasterPrivate *self) {
  return new Qt3DRender::QAbstractRayCaster::Hits(self->pick());
}

//  void Qt3DRender::QAbstractRayCasterPrivate::dispatchHits(const
//      QAbstractRayCaster::Hits &hits)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate12dispatchHitsERK5QListINS_13QRayCasterHitEE(
    Qt3DRender::QAbstractRayCasterPrivate *self,
    const Qt3DRender::QAbstractRayCaster::Hits *hits) {
  self->dispatchHits(*hits);
}

//  QAbstractRayCaster *Qt3DRender::QAbstractRayCasterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster *ritual_ZN10Qt3DRender25QAbstractRayCasterPrivate6q_funcEv(
    Qt3DRender::QAbstractRayCasterPrivate *self) {
  return self->q_func();
}

//  const QAbstractRayCaster *Qt3DRender::QAbstractRayCasterPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractRayCaster *ritual_ZNK10Qt3DRender25QAbstractRayCasterPrivate6q_funcEv(
    const Qt3DRender::QAbstractRayCasterPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QAbstractRayCasterPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QAbstractRayCasterPrivate(
    Qt3DRender::QAbstractRayCasterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QAbstractRayCasterPrivate *>(self)->take(key, call);
}

//  a Qt3DRender::QAbstractRayCaster::Hits a ritual of
//      Qt3DRender::QAbstractRayCasterPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QAbstractRayCasterPrivate__Qt3DRender_QAbstractRayCaster_Hits(
    Qt3DRender::QAbstractRayCaster::Hits *self) {
  delete self;
}
