//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qclipanimator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qclipanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DAnimation::QClipAnimatorPrivate that Python can take functions over in. Every Qt3DAnimation::QClipAnimatorPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DAnimation_QClipAnimatorPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DAnimation_QClipAnimatorPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DAnimation_QClipAnimatorPrivateCall2)(const void *, int *);
class CuteQt3DAnimation_QClipAnimatorPrivate : public Qt3DAnimation::QClipAnimatorPrivate {
public:
  using Qt3DAnimation::QClipAnimatorPrivate::QClipAnimatorPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation28QAbstractClipAnimatorPrivate7canPlayEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DAnimation::QClipAnimatorPrivate::canPlay() const
  bool canPlay() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QClipAnimatorPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QClipAnimatorPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::QClipAnimatorPrivate::canPlay();
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QClipAnimatorPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QClipAnimatorPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_QClipAnimatorPrivateCall2 call = reinterpret_cast<CuteQt3DAnimation_QClipAnimatorPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QClipAnimator *Qt3DAnimation::QClipAnimatorPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClipAnimator *ritual_ZN13Qt3DAnimation20QClipAnimatorPrivate6q_funcEv(
    Qt3DAnimation::QClipAnimatorPrivate *self) {
  return self->q_func();
}

//  const QClipAnimator *Qt3DAnimation::QClipAnimatorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QClipAnimator *ritual_ZNK13Qt3DAnimation20QClipAnimatorPrivate6q_funcEv(
    const Qt3DAnimation::QClipAnimatorPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DAnimation_QClipAnimatorPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QClipAnimatorPrivate(
    Qt3DAnimation::QClipAnimatorPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QClipAnimatorPrivate *>(self)->take(key, call);
}
