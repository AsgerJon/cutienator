//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qskeleton_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qskeleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QSkeletonPrivate that Python can take functions over in. Every Qt3DCore::QSkeletonPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QSkeletonPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QSkeletonPrivateCall1)(const void *, int *);
class CuteQt3DCore_QSkeletonPrivate : public Qt3DCore::QSkeletonPrivate {
public:
  using Qt3DCore::QSkeletonPrivate::QSkeletonPrivate;
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
      CuteQt3DCore_QSkeletonPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QSkeletonPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QSkeletonPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QSkeletonPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QSkeleton *Qt3DCore::QSkeletonPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeleton *ritual_ZN8Qt3DCore16QSkeletonPrivate6q_funcEv(
    Qt3DCore::QSkeletonPrivate *self) {
  return self->q_func();
}

//  const QSkeleton *Qt3DCore::QSkeletonPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QSkeleton *ritual_ZNK8Qt3DCore16QSkeletonPrivate6q_funcEv(
    const Qt3DCore::QSkeletonPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DCore_QSkeletonPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QSkeletonPrivate(
    Qt3DCore::QSkeletonPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QSkeletonPrivate *>(self)->take(key, call);
}
