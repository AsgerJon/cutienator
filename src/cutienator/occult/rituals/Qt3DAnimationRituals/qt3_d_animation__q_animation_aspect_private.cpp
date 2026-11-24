//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationaspect_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DAnimation::QAnimationAspectPrivate that Python can take functions over in. Every Qt3DAnimation::QAnimationAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall3)(const void *, int *);
class CuteQt3DAnimation_QAnimationAspectPrivate : public Qt3DAnimation::QAnimationAspectPrivate {
public:
  using Qt3DAnimation::QAnimationAspectPrivate::QAnimationAspectPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::frameDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall2 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall3 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  QAnimationAspect *Qt3DAnimation::QAnimationAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationAspect *ritual_ZN13Qt3DAnimation23QAnimationAspectPrivate6q_funcEv(
    Qt3DAnimation::QAnimationAspectPrivate *self) {
  return self->q_func();
}

//  const QAnimationAspect *Qt3DAnimation::QAnimationAspectPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationAspect *ritual_ZNK13Qt3DAnimation23QAnimationAspectPrivate6q_funcEv(
    const Qt3DAnimation::QAnimationAspectPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DAnimation_QAnimationAspectPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAnimationAspectPrivate(
    Qt3DAnimation::QAnimationAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAnimationAspectPrivate *>(self)->take(key, call);
}
