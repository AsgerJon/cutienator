//  Written by hand on 2026-11-25 from
//  Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again. Not
//  written: 'addWatcher' and 'removeWatcher' (they take a QWeakPointer, a
//  template).
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/calcboundingvolumejob_p.h>
#include <cstring>

//  A Qt3DCore::CalculateBoundingVolumeJob that Python can take functions over
//  in. Every Qt3DCore::CalculateBoundingVolumeJob Python makes is one.
//  Each function below asks the Python function handed over for it, and
//  runs Qt's own without one.
typedef bool (*CuteQt3DCore_CalculateBoundingVolumeJobCall0)(const void *, int *);
typedef void (*CuteQt3DCore_CalculateBoundingVolumeJobCall1)(const void *, int *);
typedef void (*CuteQt3DCore_CalculateBoundingVolumeJobCall2)(const void *, Qt3DCore::QAspectEngine *, int *);
class CuteQt3DCore_CalculateBoundingVolumeJob : public Qt3DCore::CalculateBoundingVolumeJob {
public:
  using Qt3DCore::CalculateBoundingVolumeJob::CalculateBoundingVolumeJob;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob3runEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_CalculateBoundingVolumeJobCall0 call = reinterpret_cast<CuteQt3DCore_CalculateBoundingVolumeJobCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::CalculateBoundingVolumeJob::isRequired();
  }

  //  void Qt3DCore::QAspectJob::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_CalculateBoundingVolumeJobCall1 call = reinterpret_cast<CuteQt3DCore_CalculateBoundingVolumeJobCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::CalculateBoundingVolumeJob::run();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_CalculateBoundingVolumeJobCall2 call = reinterpret_cast<CuteQt3DCore_CalculateBoundingVolumeJobCall2>(taken[2]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::CalculateBoundingVolumeJob::postFrame(aspectEngine);
  }
};

//  Qt3DCore::CalculateBoundingVolumeJob::CalculateBoundingVolumeJob(QCoreAspect
//      *aspect)
extern "C" Q_DECL_EXPORT
Qt3DCore::CalculateBoundingVolumeJob *ritual_ZN8Qt3DCore26CalculateBoundingVolumeJobC1EPNS_11QCoreAspectE(
    Qt3DCore::QCoreAspect *aspect) {
  return new CuteQt3DCore_CalculateBoundingVolumeJob(aspect);
}

//  Qt3DCore::CalculateBoundingVolumeJob::~CalculateBoundingVolumeJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore26CalculateBoundingVolumeJobD1Ev(
    Qt3DCore::CalculateBoundingVolumeJob *self) {
  delete self;
}

//  void Qt3DCore::CalculateBoundingVolumeJob::setRoot(QEntity *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob7setRootEPNS_7QEntityE(
    Qt3DCore::CalculateBoundingVolumeJob *self,
    Qt3DCore::QEntity *root) {
  self->setRoot(root);
}

//  bool Qt3DCore::CalculateBoundingVolumeJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob10isRequiredEv(
    Qt3DCore::CalculateBoundingVolumeJob *self) {
  return self->isRequired();
}

//  void Qt3DCore::CalculateBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob3runEv(
    Qt3DCore::CalculateBoundingVolumeJob *self) {
  self->run();
}

//  void Qt3DCore::CalculateBoundingVolumeJob::postFrame(QAspectEngine
//      *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob9postFrameEPNS_13QAspectEngineE(
    Qt3DCore::CalculateBoundingVolumeJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->postFrame(aspectEngine);
}

//  CalculateBoundingVolumeJobPrivate
//      *Qt3DCore::CalculateBoundingVolumeJob::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::CalculateBoundingVolumeJobPrivate *ritual_ZN8Qt3DCore26CalculateBoundingVolumeJob6d_funcEv(
    Qt3DCore::CalculateBoundingVolumeJob *self) {
  return self->d_func();
}

//  const CalculateBoundingVolumeJobPrivate
//      *Qt3DCore::CalculateBoundingVolumeJob::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::CalculateBoundingVolumeJobPrivate *ritual_ZNK8Qt3DCore26CalculateBoundingVolumeJob6d_funcEv(
    const Qt3DCore::CalculateBoundingVolumeJob *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_CalculateBoundingVolumeJob, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_CalculateBoundingVolumeJob(
    Qt3DCore::CalculateBoundingVolumeJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_CalculateBoundingVolumeJob *>(self)->take(key, call);
}

//  bool Qt3DCore::CalculateBoundingVolumeJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8Qt3DCore26CalculateBoundingVolumeJob10isRequiredEv(
    Qt3DCore::CalculateBoundingVolumeJob *self) {
  return self->Qt3DCore::CalculateBoundingVolumeJob::isRequired();
}

//  void Qt3DCore::CalculateBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore26CalculateBoundingVolumeJob3runEv(
    Qt3DCore::CalculateBoundingVolumeJob *self) {
  self->Qt3DCore::CalculateBoundingVolumeJob::run();
}

//  void Qt3DCore::CalculateBoundingVolumeJob::postFrame(QAspectEngine
//      *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore26CalculateBoundingVolumeJob9postFrameEPNS_13QAspectEngineE(
    Qt3DCore::CalculateBoundingVolumeJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->Qt3DCore::CalculateBoundingVolumeJob::postFrame(aspectEngine);
}
