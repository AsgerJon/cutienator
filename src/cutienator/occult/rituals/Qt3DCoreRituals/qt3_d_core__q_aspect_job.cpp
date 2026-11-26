//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/qaspectjob.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DCore/qaspectjob.h>
#include <cstring>
#include <QtCore/QWeakPointer>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DCore::QAspectJob that Python can take functions over in. Every Qt3DCore::QAspectJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAspectJobCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAspectJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DCore_QAspectJobCall2)(const void *, int *);
class CuteQt3DCore_QAspectJob : public Qt3DCore::QAspectJob {
public:
  using Qt3DCore::QAspectJob::QAspectJob;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob3runEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAspectJob::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobCall0 call = reinterpret_cast<CuteQt3DCore_QAspectJobCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobCall1 call = reinterpret_cast<CuteQt3DCore_QAspectJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobCall2 call = reinterpret_cast<CuteQt3DCore_QAspectJobCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  Qt3DCore::QAspectJob::QAspectJob()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJob *ritual_ZN8Qt3DCore10QAspectJobC1Ev() {
  return new CuteQt3DCore_QAspectJob();
}

//  Qt3DCore::QAspectJob::~QAspectJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAspectJobD1Ev(Qt3DCore::QAspectJob *self) {
  delete self;
}

//  void Qt3DCore::QAspectJob::addDependency(QWeakPointer<QAspectJob>
//      dependency)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAspectJob13addDependencyE12QWeakPointerIS0_E(
    Qt3DCore::QAspectJob *self,
    const QWeakPointer<Qt3DCore::QAspectJob> *dependency) {
  self->addDependency(*dependency);
}

//  void Qt3DCore::QAspectJob::removeDependency(QWeakPointer<QAspectJob>
//      dependency)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAspectJob16removeDependencyE12QWeakPointerIS0_E(
    Qt3DCore::QAspectJob *self,
    const QWeakPointer<Qt3DCore::QAspectJob> *dependency) {
  self->removeDependency(*dependency);
}

//  const std::vector<QWeakPointer<QAspectJob>>
//      &Qt3DCore::QAspectJob::dependencies() const
extern "C" Q_DECL_EXPORT
const std::vector<QWeakPointer<Qt3DCore::QAspectJob>> *ritual_ZNK8Qt3DCore10QAspectJob12dependenciesEv(
    const Qt3DCore::QAspectJob *self) {
  return &(self->dependencies());
}

//  void Qt3DCore::QAspectJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAspectJob3runEv(Qt3DCore::QAspectJob *self) {
  self->run();
}

//  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE(
    Qt3DCore::QAspectJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->postFrame(aspectEngine);
}

//  bool Qt3DCore::QAspectJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore10QAspectJob10isRequiredEv(
    Qt3DCore::QAspectJob *self) {
  return self->isRequired();
}

//  Qt3DCore::QAspectJob::QAspectJob(QAspectJobPrivate &dd)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJob *ritual_ZN8Qt3DCore10QAspectJobC1ERNS_17QAspectJobPrivateE(
    Qt3DCore::QAspectJobPrivate *dd) {
  return new CuteQt3DCore_QAspectJob(*dd);
}

//  QAspectJobPrivate *Qt3DCore::QAspectJob::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJobPrivate *ritual_ZN8Qt3DCore10QAspectJob6d_funcEv(
    Qt3DCore::QAspectJob *self) {
  return self->d_func();
}

//  const QAspectJobPrivate *Qt3DCore::QAspectJob::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAspectJobPrivate *ritual_ZNK8Qt3DCore10QAspectJob6d_funcEv(
    const Qt3DCore::QAspectJob *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QAspectJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAspectJob(
    Qt3DCore::QAspectJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAspectJob *>(self)->take(key, call);
}

//  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE(
    Qt3DCore::QAspectJob *self,
    Qt3DCore::QAspectEngine *aspectEngine) {
  self->Qt3DCore::QAspectJob::postFrame(aspectEngine);
}

//  bool Qt3DCore::QAspectJob::isRequired()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8Qt3DCore10QAspectJob10isRequiredEv(
    Qt3DCore::QAspectJob *self) {
  return self->Qt3DCore::QAspectJob::isRequired();
}
