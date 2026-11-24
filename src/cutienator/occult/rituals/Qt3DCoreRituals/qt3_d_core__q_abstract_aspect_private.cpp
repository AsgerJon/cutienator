//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QAbstractAspectPrivate that Python can take functions over in. Every Qt3DCore::QAbstractAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall3)(const void *, int *);
class CuteQt3DCore_QAbstractAspectPrivate : public Qt3DCore::QAbstractAspectPrivate {
public:
  using Qt3DCore::QAbstractAspectPrivate::QAbstractAspectPrivate;
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
      CuteQt3DCore_QAbstractAspectPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall1>(taken[1]);
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
      CuteQt3DCore_QAbstractAspectPrivateCall2 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectPrivateCall3 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode *node,
//      QBackendNode *backend, bool firstTime) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb(
    const Qt3DCore::QAbstractAspectPrivate *self,
    Qt3DCore::QNode *node,
    Qt3DCore::QBackendNode *backend,
    bool firstTime) {
  self->syncDirtyFrontEndNode(node, backend, firstTime);
}

//  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->onEngineAboutToShutdown();
}

//  QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspect *ritual_ZN8Qt3DCore22QAbstractAspectPrivate6q_funcEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  return self->q_func();
}

//  const QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractAspect *ritual_ZNK8Qt3DCore22QAbstractAspectPrivate6q_funcEv(
    const Qt3DCore::QAbstractAspectPrivate *self) {
  return self->q_func();
}

//  Qt3DCore::QAbstractAspectPrivate as the
//      Qt3DCore::QAspectJobProviderInterface it is built on
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJobProviderInterface *ritual_cast_Qt3DCore_QAbstractAspectPrivate_Qt3DCore_QAspectJobProviderInterface(
    Qt3DCore::QAbstractAspectPrivate *self) {
  return static_cast<Qt3DCore::QAspectJobProviderInterface *>(self);
}

//  a Python function taken by a CuteQt3DCore_QAbstractAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractAspectPrivate(
    Qt3DCore::QAbstractAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractAspectPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate8jobsDoneEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->Qt3DCore::QAbstractAspectPrivate::jobsDone();
}

//  void Qt3DCore::QAbstractAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate9frameDoneEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->Qt3DCore::QAbstractAspectPrivate::frameDone();
}

//  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode *node,
//      QBackendNode *backend, bool firstTime) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb(
    const Qt3DCore::QAbstractAspectPrivate *self,
    Qt3DCore::QNode *node,
    Qt3DCore::QBackendNode *backend,
    bool firstTime) {
  self->Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(
      node,
      backend,
      firstTime);
}

//  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
}
