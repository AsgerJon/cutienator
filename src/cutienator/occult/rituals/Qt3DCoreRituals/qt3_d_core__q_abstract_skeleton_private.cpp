//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractskeleton_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractskeleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QAbstractSkeletonPrivate that Python can take functions over in. Every Qt3DCore::QAbstractSkeletonPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAbstractSkeletonPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QAbstractSkeletonPrivateCall1)(const void *, int *);
class CuteQt3DCore_QAbstractSkeletonPrivate : public Qt3DCore::QAbstractSkeletonPrivate {
public:
  using Qt3DCore::QAbstractSkeletonPrivate::QAbstractSkeletonPrivate;
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
      CuteQt3DCore_QAbstractSkeletonPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAbstractSkeletonPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QAbstractSkeletonPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DCore::QAbstractSkeletonPrivate::QAbstractSkeletonPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractSkeletonPrivate *ritual_ZN8Qt3DCore24QAbstractSkeletonPrivateC1Ev() {
  return new CuteQt3DCore_QAbstractSkeletonPrivate();
}

//  void Qt3DCore::QAbstractSkeletonPrivate::setJointCount(int jointCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate13setJointCountEi(
    Qt3DCore::QAbstractSkeletonPrivate *self,
    int jointCount) {
  self->setJointCount(jointCount);
}

//  QAbstractSkeleton *Qt3DCore::QAbstractSkeletonPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractSkeleton *ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate6q_funcEv(
    Qt3DCore::QAbstractSkeletonPrivate *self) {
  return self->q_func();
}

//  const QAbstractSkeleton *Qt3DCore::QAbstractSkeletonPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractSkeleton *ritual_ZNK8Qt3DCore24QAbstractSkeletonPrivate6q_funcEv(
    const Qt3DCore::QAbstractSkeletonPrivate *self) {
  return self->q_func();
}

//  const QAbstractSkeletonPrivate
//      *Qt3DCore::QAbstractSkeletonPrivate::get(const QAbstractSkeleton *q)
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractSkeletonPrivate *ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate3getEPKNS_17QAbstractSkeletonE(
    const Qt3DCore::QAbstractSkeleton *q) {
  return Qt3DCore::QAbstractSkeletonPrivate::get(q);
}

//  QAbstractSkeletonPrivate
//      *Qt3DCore::QAbstractSkeletonPrivate::get(QAbstractSkeleton *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractSkeletonPrivate *ritual_ZN8Qt3DCore24QAbstractSkeletonPrivate3getEPNS_17QAbstractSkeletonE(
    Qt3DCore::QAbstractSkeleton *q) {
  return Qt3DCore::QAbstractSkeletonPrivate::get(q);
}

//  a Python function taken by a CuteQt3DCore_QAbstractSkeletonPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractSkeletonPrivate(
    Qt3DCore::QAbstractSkeletonPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractSkeletonPrivate *>(self)->take(key, call);
}
