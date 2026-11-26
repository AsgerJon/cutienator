//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qcoreaspect_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qcoreaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QCoreAspectPrivate that Python can take functions over in. Every Qt3DCore::QCoreAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QCoreAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DCore_QCoreAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DCore_QCoreAspectPrivateCall3)(const void *, int *);
class CuteQt3DCore_QCoreAspectPrivate : public Qt3DCore::QCoreAspectPrivate {
public:
  using Qt3DCore::QCoreAspectPrivate::QCoreAspectPrivate;
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

  //  void Qt3DCore::QCoreAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QCoreAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QCoreAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QCoreAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QCoreAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QCoreAspectPrivate::frameDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectPrivateCall2 call = reinterpret_cast<CuteQt3DCore_QCoreAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QCoreAspectPrivateCall3 call = reinterpret_cast<CuteQt3DCore_QCoreAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  Qt3DCore::QCoreAspectPrivate::QCoreAspectPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QCoreAspectPrivate *ritual_ZN8Qt3DCore18QCoreAspectPrivateC1Ev() {
  return new CuteQt3DCore_QCoreAspectPrivate();
}

//  Qt3DCore::QCoreAspectPrivate::~QCoreAspectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18QCoreAspectPrivateD1Ev(
    Qt3DCore::QCoreAspectPrivate *self) {
  delete self;
}

//  QCoreAspect *Qt3DCore::QCoreAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QCoreAspect *ritual_ZN8Qt3DCore18QCoreAspectPrivate6q_funcEv(
    Qt3DCore::QCoreAspectPrivate *self) {
  return self->q_func();
}

//  const QCoreAspect *Qt3DCore::QCoreAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QCoreAspect *ritual_ZNK8Qt3DCore18QCoreAspectPrivate6q_funcEv(
    const Qt3DCore::QCoreAspectPrivate *self) {
  return self->q_func();
}

//  QCoreAspectPrivate *Qt3DCore::QCoreAspectPrivate::get(QCoreAspect
//      *aspect)
extern "C" Q_DECL_EXPORT
Qt3DCore::QCoreAspectPrivate *ritual_ZN8Qt3DCore18QCoreAspectPrivate3getEPNS_11QCoreAspectE(
    Qt3DCore::QCoreAspect *aspect) {
  return Qt3DCore::QCoreAspectPrivate::get(aspect);
}

//  void Qt3DCore::QCoreAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18QCoreAspectPrivate8jobsDoneEv(
    Qt3DCore::QCoreAspectPrivate *self) {
  self->jobsDone();
}

//  void Qt3DCore::QCoreAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18QCoreAspectPrivate9frameDoneEv(
    Qt3DCore::QCoreAspectPrivate *self) {
  self->frameDone();
}

//  a Python function taken by a CuteQt3DCore_QCoreAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QCoreAspectPrivate(
    Qt3DCore::QCoreAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QCoreAspectPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QCoreAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore18QCoreAspectPrivate8jobsDoneEv(
    Qt3DCore::QCoreAspectPrivate *self) {
  self->Qt3DCore::QCoreAspectPrivate::jobsDone();
}

//  void Qt3DCore::QCoreAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore18QCoreAspectPrivate9frameDoneEv(
    Qt3DCore::QCoreAspectPrivate *self) {
  self->Qt3DCore::QCoreAspectPrivate::frameDone();
}
