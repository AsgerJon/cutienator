//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrenderaspect_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrenderaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QRenderAspectPrivate that Python can take functions over in. Every Qt3DRender::QRenderAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall2)(const void *, int *);
typedef void (*CuteQt3DRender_QRenderAspectPrivateCall3)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
class CuteQt3DRender_QRenderAspectPrivate : public Qt3DRender::QRenderAspectPrivate {
public:
  using Qt3DRender::QRenderAspectPrivate::QRenderAspectPrivate;
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
    if (!std::strcmp(key, "_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::QRenderAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspectPrivate::jobsDone();
  }

  //  void Qt3DRender::QRenderAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspectPrivate::frameDone();
  }

  //  void Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QRenderAspectPrivateCall3 call = reinterpret_cast<CuteQt3DRender_QRenderAspectPrivateCall3>(taken[3]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }
};

//  QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspect *ritual_ZN10Qt3DRender20QRenderAspectPrivate6q_funcEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  return self->q_func();
}

//  const QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderAspect *ritual_ZNK10Qt3DRender20QRenderAspectPrivate6q_funcEv(
    const Qt3DRender::QRenderAspectPrivate *self) {
  return self->q_func();
}

//  QRenderAspectPrivate *Qt3DRender::QRenderAspectPrivate::get(QRenderAspect
//      *q)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspectPrivate *ritual_ZN10Qt3DRender20QRenderAspectPrivate3getEPNS_13QRenderAspectE(
    Qt3DRender::QRenderAspect *q) {
  return Qt3DRender::QRenderAspectPrivate::get(q);
}

//  a Python function taken by a CuteQt3DRender_QRenderAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderAspectPrivate(
    Qt3DRender::QRenderAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderAspectPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QRenderAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QRenderAspectPrivate8jobsDoneEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->Qt3DRender::QRenderAspectPrivate::jobsDone();
}

//  void Qt3DRender::QRenderAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QRenderAspectPrivate9frameDoneEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->Qt3DRender::QRenderAspectPrivate::frameDone();
}

//  void Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QRenderAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DRender::QRenderAspectPrivate *self) {
  self->Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown();
}
