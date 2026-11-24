//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qinputaspect_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qinputaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QInputAspectPrivate that Python can take functions over in. Every Qt3DInput::QInputAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QInputAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DInput_QInputAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DInput_QInputAspectPrivateCall3)(const void *, int *);
class CuteQt3DInput_QInputAspectPrivate : public Qt3DInput::QInputAspectPrivate {
public:
  using Qt3DInput::QInputAspectPrivate::QInputAspectPrivate;
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
      CuteQt3DInput_QInputAspectPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall1>(taken[1]);
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
      CuteQt3DInput_QInputAspectPrivateCall2 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DInput_QInputAspectPrivateCall3 call = reinterpret_cast<CuteQt3DInput_QInputAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  QInputAspect *Qt3DInput::QInputAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QInputAspect *ritual_ZN9Qt3DInput19QInputAspectPrivate6q_funcEv(
    Qt3DInput::QInputAspectPrivate *self) {
  return self->q_func();
}

//  const QInputAspect *Qt3DInput::QInputAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QInputAspect *ritual_ZNK9Qt3DInput19QInputAspectPrivate6q_funcEv(
    const Qt3DInput::QInputAspectPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DInput_QInputAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QInputAspectPrivate(
    Qt3DInput::QInputAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QInputAspectPrivate *>(self)->take(key, call);
}
