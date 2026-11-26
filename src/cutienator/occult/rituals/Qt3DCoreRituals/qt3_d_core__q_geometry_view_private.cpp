//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qgeometryview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qgeometryview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QGeometryViewPrivate that Python can take functions over in. Every Qt3DCore::QGeometryViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QGeometryViewPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QGeometryViewPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
class CuteQt3DCore_QGeometryViewPrivate : public Qt3DCore::QGeometryViewPrivate {
public:
  using Qt3DCore::QGeometryViewPrivate::QGeometryViewPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QGeometryViewPrivate::update()
  void update() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QGeometryViewPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QGeometryViewPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryViewPrivate::update();
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QGeometryViewPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QGeometryViewPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }
};

//  Qt3DCore::QGeometryViewPrivate::QGeometryViewPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryViewPrivate *ritual_ZN8Qt3DCore20QGeometryViewPrivateC1Ev() {
  return new CuteQt3DCore_QGeometryViewPrivate();
}

//  Qt3DCore::QGeometryViewPrivate::~QGeometryViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QGeometryViewPrivateD1Ev(
    Qt3DCore::QGeometryViewPrivate *self) {
  delete self;
}

//  QGeometryViewPrivate *Qt3DCore::QGeometryViewPrivate::get(QGeometryView
//      *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryViewPrivate *ritual_ZN8Qt3DCore20QGeometryViewPrivate3getEPNS_13QGeometryViewE(
    Qt3DCore::QGeometryView *q) {
  return Qt3DCore::QGeometryViewPrivate::get(q);
}

//  void Qt3DCore::QGeometryViewPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QGeometryViewPrivate6updateEv(
    Qt3DCore::QGeometryViewPrivate *self) {
  self->update();
}

//  QGeometryView *Qt3DCore::QGeometryViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryView *ritual_ZN8Qt3DCore20QGeometryViewPrivate6q_funcEv(
    Qt3DCore::QGeometryViewPrivate *self) {
  return self->q_func();
}

//  const QGeometryView *Qt3DCore::QGeometryViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QGeometryView *ritual_ZNK8Qt3DCore20QGeometryViewPrivate6q_funcEv(
    const Qt3DCore::QGeometryViewPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DCore_QGeometryViewPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QGeometryViewPrivate(
    Qt3DCore::QGeometryViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QGeometryViewPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QGeometryViewPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore20QGeometryViewPrivate6updateEv(
    Qt3DCore::QGeometryViewPrivate *self) {
  self->Qt3DCore::QGeometryViewPrivate::update();
}
