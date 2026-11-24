//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qbackendnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qbackendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QBackendNodePrivate that Python can take functions over in. Every Qt3DCore::QBackendNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QBackendNodePrivateCall0)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DCore_QBackendNodePrivateCall1)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DCore_QBackendNodePrivateCall2)(const void *, Qt3DCore::QNode *, int *);
typedef void (*CuteQt3DCore_QBackendNodePrivateCall3)(const void *, Qt3DCore::QNode *, int *);
class CuteQt3DCore_QBackendNodePrivate : public Qt3DCore::QBackendNodePrivate {
public:
  using Qt3DCore::QBackendNodePrivate::QBackendNodePrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QNodeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNodeE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNodeE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode *frontend)
  void addedToEntity(Qt3DCore::QNode *frontend) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodePrivateCall0 call = reinterpret_cast<CuteQt3DCore_QBackendNodePrivateCall0>(taken[0]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::addedToEntity(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode
  //      *frontend)
  void removedFromEntity(Qt3DCore::QNode *frontend) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodePrivateCall1 call = reinterpret_cast<CuteQt3DCore_QBackendNodePrivateCall1>(taken[1]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::removedFromEntity(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::componentAdded(QNode *frontend)
  void componentAdded(Qt3DCore::QNode *frontend) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodePrivateCall2 call = reinterpret_cast<CuteQt3DCore_QBackendNodePrivateCall2>(taken[2]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::componentAdded(frontend);
  }

  //  void Qt3DCore::QBackendNodePrivate::componentRemoved(QNode *frontend)
  void componentRemoved(Qt3DCore::QNode *frontend) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QBackendNodePrivateCall3 call = reinterpret_cast<CuteQt3DCore_QBackendNodePrivateCall3>(taken[3]);
      call(this, frontend, &handled);
      if (handled) return;
    }
    Qt3DCore::QBackendNodePrivate::componentRemoved(frontend);
  }
};

//  Qt3DCore::QBackendNodePrivate::~QBackendNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QBackendNodePrivateD1Ev(
    Qt3DCore::QBackendNodePrivate *self) {
  delete self;
}

//  QBackendNode *Qt3DCore::QBackendNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZN8Qt3DCore19QBackendNodePrivate6q_funcEv(
    Qt3DCore::QBackendNodePrivate *self) {
  return self->q_func();
}

//  const QBackendNode *Qt3DCore::QBackendNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QBackendNode *ritual_ZNK8Qt3DCore19QBackendNodePrivate6q_funcEv(
    const Qt3DCore::QBackendNodePrivate *self) {
  return self->q_func();
}

//  void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->addedToEntity(frontend);
}

//  void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->removedFromEntity(frontend);
}

//  void Qt3DCore::QBackendNodePrivate::componentAdded(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->componentAdded(frontend);
}

//  void Qt3DCore::QBackendNodePrivate::componentRemoved(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->componentRemoved(frontend);
}

//  a Python function taken by a CuteQt3DCore_QBackendNodePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QBackendNodePrivate(
    Qt3DCore::QBackendNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QBackendNodePrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QBackendNodePrivate::addedToEntity(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore19QBackendNodePrivate13addedToEntityEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->Qt3DCore::QBackendNodePrivate::addedToEntity(frontend);
}

//  void Qt3DCore::QBackendNodePrivate::removedFromEntity(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore19QBackendNodePrivate17removedFromEntityEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->Qt3DCore::QBackendNodePrivate::removedFromEntity(frontend);
}

//  void Qt3DCore::QBackendNodePrivate::componentAdded(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore19QBackendNodePrivate14componentAddedEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->Qt3DCore::QBackendNodePrivate::componentAdded(frontend);
}

//  void Qt3DCore::QBackendNodePrivate::componentRemoved(QNode *frontend)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore19QBackendNodePrivate16componentRemovedEPNS_5QNodeE(
    Qt3DCore::QBackendNodePrivate *self,
    Qt3DCore::QNode *frontend) {
  self->Qt3DCore::QBackendNodePrivate::componentRemoved(frontend);
}
