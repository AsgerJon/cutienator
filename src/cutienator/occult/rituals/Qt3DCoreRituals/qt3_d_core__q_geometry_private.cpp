//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qgeometry_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qgeometry_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>

//  A Qt3DCore::QGeometryPrivate that Python can take functions over in. Every Qt3DCore::QGeometryPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QGeometryPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QGeometryPrivateCall1)(const void *, int *);
class CuteQt3DCore_QGeometryPrivate : public Qt3DCore::QGeometryPrivate {
public:
  using Qt3DCore::QGeometryPrivate::QGeometryPrivate;
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

  //  void Qt3DCore::QGeometryPrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QGeometryPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QGeometryPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::setScene(scene);
  }

  //  void Qt3DCore::QGeometryPrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QGeometryPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QGeometryPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QGeometryPrivate::update();
  }
};

//  QGeometry *Qt3DCore::QGeometryPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometry *ritual_ZN8Qt3DCore16QGeometryPrivate6q_funcEv(
    Qt3DCore::QGeometryPrivate *self) {
  return self->q_func();
}

//  const QGeometry *Qt3DCore::QGeometryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QGeometry *ritual_ZNK8Qt3DCore16QGeometryPrivate6q_funcEv(
    const Qt3DCore::QGeometryPrivate *self) {
  return self->q_func();
}

//  Qt3DCore::QGeometryPrivate::QGeometryPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryPrivate *ritual_ZN8Qt3DCore16QGeometryPrivateC1Ev() {
  return new CuteQt3DCore_QGeometryPrivate();
}

//  Qt3DCore::QGeometryPrivate::~QGeometryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QGeometryPrivateD1Ev(
    Qt3DCore::QGeometryPrivate *self) {
  delete self;
}

//  void Qt3DCore::QGeometryPrivate::setScene(QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QGeometryPrivate8setSceneEPNS_6QSceneE(
    Qt3DCore::QGeometryPrivate *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  void Qt3DCore::QGeometryPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QGeometryPrivate6updateEv(
    Qt3DCore::QGeometryPrivate *self) {
  self->update();
}

//  void Qt3DCore::QGeometryPrivate::setExtent(const QVector3D &minExtent,
//      const QVector3D &maxExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16QGeometryPrivate9setExtentERK9QVector3DS3_(
    Qt3DCore::QGeometryPrivate *self,
    const QVector3D *minExtent,
    const QVector3D *maxExtent) {
  self->setExtent(*minExtent, *maxExtent);
}

//  QGeometryPrivate *Qt3DCore::QGeometryPrivate::get(QGeometry *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryPrivate *ritual_ZN8Qt3DCore16QGeometryPrivate3getEPNS_9QGeometryE(
    Qt3DCore::QGeometry *q) {
  return Qt3DCore::QGeometryPrivate::get(q);
}

//  a Python function taken by a CuteQt3DCore_QGeometryPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QGeometryPrivate(
    Qt3DCore::QGeometryPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QGeometryPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QGeometryPrivate::setScene(QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16QGeometryPrivate8setSceneEPNS_6QSceneE(
    Qt3DCore::QGeometryPrivate *self,
    Qt3DCore::QScene *scene) {
  self->Qt3DCore::QGeometryPrivate::setScene(scene);
}

//  void Qt3DCore::QGeometryPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16QGeometryPrivate6updateEv(
    Qt3DCore::QGeometryPrivate *self) {
  self->Qt3DCore::QGeometryPrivate::update();
}
