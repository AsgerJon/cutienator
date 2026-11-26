//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qaspectjob_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qaspectjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QAspectJobPrivate that Python can take functions over in. Every Qt3DCore::QAspectJobPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DCore_QAspectJobPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAspectJobPrivateCall1)(const void *, Qt3DCore::QAspectManager *, int *);
class CuteQt3DCore_QAspectJobPrivate : public Qt3DCore::QAspectJobPrivate {
public:
  using Qt3DCore::QAspectJobPrivate::QAspectJobPrivate;
  CuteQt3DCore_QAspectJobPrivate(const Qt3DCore::QAspectJobPrivate & other) : Qt3DCore::QAspectJobPrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManagerE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DCore::QAspectJobPrivate::isRequired() const
  bool isRequired() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QAspectJobPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJobPrivate::isRequired();
  }

  //  void Qt3DCore::QAspectJobPrivate::postFrame(QAspectManager
  //      *aspectManager)
  void postFrame(Qt3DCore::QAspectManager *aspectManager) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QAspectJobPrivateCall1>(taken[1]);
      call(this, aspectManager, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJobPrivate::postFrame(aspectManager);
  }
};

//  Qt3DCore::QAspectJobPrivate::QAspectJobPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJobPrivate *ritual_ZN8Qt3DCore17QAspectJobPrivateC1Ev() {
  return new CuteQt3DCore_QAspectJobPrivate();
}

//  Qt3DCore::QAspectJobPrivate::~QAspectJobPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QAspectJobPrivateD1Ev(
    Qt3DCore::QAspectJobPrivate *self) {
  delete self;
}

//  QAspectJobPrivate *Qt3DCore::QAspectJobPrivate::get(QAspectJob *job)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJobPrivate *ritual_ZN8Qt3DCore17QAspectJobPrivate3getEPNS_10QAspectJobE(
    Qt3DCore::QAspectJob *job) {
  return Qt3DCore::QAspectJobPrivate::get(job);
}

//  bool Qt3DCore::QAspectJobPrivate::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv(
    const Qt3DCore::QAspectJobPrivate *self) {
  return self->isRequired();
}

//  void Qt3DCore::QAspectJobPrivate::postFrame(QAspectManager
//      *aspectManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManagerE(
    Qt3DCore::QAspectJobPrivate *self,
    Qt3DCore::QAspectManager *aspectManager) {
  self->postFrame(aspectManager);
}

//  void Qt3DCore::QAspectJobPrivate::clearDependencies()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QAspectJobPrivate17clearDependenciesEv(
    Qt3DCore::QAspectJobPrivate *self) {
  self->clearDependencies();
}

//  a Python function taken by a CuteQt3DCore_QAspectJobPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAspectJobPrivate(
    Qt3DCore::QAspectJobPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAspectJobPrivate *>(self)->take(key, call);
}

//  bool Qt3DCore::QAspectJobPrivate::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv(
    const Qt3DCore::QAspectJobPrivate *self) {
  return self->Qt3DCore::QAspectJobPrivate::isRequired();
}

//  void Qt3DCore::QAspectJobPrivate::postFrame(QAspectManager
//      *aspectManager)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManagerE(
    Qt3DCore::QAspectJobPrivate *self,
    Qt3DCore::QAspectManager *aspectManager) {
  self->Qt3DCore::QAspectJobPrivate::postFrame(aspectManager);
}
