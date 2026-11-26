//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qaspectjobproviderinterface_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qaspectjobproviderinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <vector>

//  A Qt3DCore::QAspectJobProviderInterface that Python can take functions over in. Every Qt3DCore::QAspectJobProviderInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAspectJobProviderInterfaceCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAspectJobProviderInterfaceCall1)(const void *, int *);
class CuteQt3DCore_QAspectJobProviderInterface : public Qt3DCore::QAspectJobProviderInterface {
public:
  using Qt3DCore::QAspectJobProviderInterface::QAspectJobProviderInterface;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAspectJobProviderInterface::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobProviderInterfaceCall0 call = reinterpret_cast<CuteQt3DCore_QAspectJobProviderInterfaceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DCore::QAspectJobProviderInterface::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAspectJobProviderInterfaceCall1 call = reinterpret_cast<CuteQt3DCore_QAspectJobProviderInterfaceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  Qt3DCore::QAspectJobProviderInterface::~QAspectJobProviderInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore27QAspectJobProviderInterfaceD1Ev(
    Qt3DCore::QAspectJobProviderInterface *self) {
  delete self;
}

//  std::vector<QAspectJobPtr>
//      Qt3DCore::QAspectJobProviderInterface::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN8Qt3DCore27QAspectJobProviderInterface13jobsToExecuteEx(
    Qt3DCore::QAspectJobProviderInterface *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
}

//  void Qt3DCore::QAspectJobProviderInterface::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv(
    Qt3DCore::QAspectJobProviderInterface *self) {
  self->jobsDone();
}

//  void Qt3DCore::QAspectJobProviderInterface::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv(
    Qt3DCore::QAspectJobProviderInterface *self) {
  self->frameDone();
}

//  a Python function taken by a CuteQt3DCore_QAspectJobProviderInterface,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAspectJobProviderInterface(
    Qt3DCore::QAspectJobProviderInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAspectJobProviderInterface *>(self)->take(key, call);
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DCore::QAspectJobProviderInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAspectJobProviderInterface__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}
