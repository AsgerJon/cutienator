//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/task_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/task_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::RunnableInterface that Python can take functions over in. Every Qt3DCore::RunnableInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DCore_RunnableInterfaceCall0)(const void *, int *);
typedef void (*CuteQt3DCore_RunnableInterfaceCall1)(const void *, int *);
typedef int (*CuteQt3DCore_RunnableInterfaceCall2)(const void *, int *);
typedef void (*CuteQt3DCore_RunnableInterfaceCall3)(const void *, int, int *);
typedef void (*CuteQt3DCore_RunnableInterfaceCall4)(const void *, bool, int *);
typedef bool (*CuteQt3DCore_RunnableInterfaceCall5)(const void *, int *);
typedef void (*CuteQt3DCore_RunnableInterfaceCall6)(const void *, Qt3DCore::QThreadPooler *, int *);
typedef int (*CuteQt3DCore_RunnableInterfaceCall7)(const void *, int *);
class CuteQt3DCore_RunnableInterface : public Qt3DCore::RunnableInterface {
public:
  using Qt3DCore::RunnableInterface::RunnableInterface;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore17RunnableInterface10isRequiredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface2idEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface5setIdEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface11setReservedEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface8reservedEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface9setPoolerEPNS_13QThreadPoolerE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore17RunnableInterface4typeEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DCore::RunnableInterface::isRequired() const
  bool isRequired() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall0 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DCore::RunnableInterface::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall1 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  int Qt3DCore::RunnableInterface::id()
  int id() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall2 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DCore::RunnableInterface::setId(int id)
  void setId(int id) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall3 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall3>(taken[3]);
      call(this, id, &handled);
      if (handled) return;
    }
  }

  //  void Qt3DCore::RunnableInterface::setReserved(bool reserved)
  void setReserved(bool reserved) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall4 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall4>(taken[4]);
      call(this, reserved, &handled);
      if (handled) return;
    }
  }

  //  bool Qt3DCore::RunnableInterface::reserved()
  bool reserved() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall5 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DCore::RunnableInterface::setPooler(QThreadPooler *pooler)
  void setPooler(Qt3DCore::QThreadPooler *pooler) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall6 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall6>(taken[6]);
      call(this, pooler, &handled);
      if (handled) return;
    }
  }

  //  RunnableType Qt3DCore::RunnableInterface::type() const
  Qt3DCore::RunnableInterface::RunnableType type() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_RunnableInterfaceCall7 call = reinterpret_cast<CuteQt3DCore_RunnableInterfaceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DCore::RunnableInterface::RunnableType>(given);
    }
    return {};
  }
};

//  Qt3DCore::RunnableInterface::~RunnableInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17RunnableInterfaceD1Ev(
    Qt3DCore::RunnableInterface *self) {
  delete self;
}

//  bool Qt3DCore::RunnableInterface::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore17RunnableInterface10isRequiredEv(
    const Qt3DCore::RunnableInterface *self) {
  return self->isRequired();
}

//  void Qt3DCore::RunnableInterface::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17RunnableInterface3runEv(
    Qt3DCore::RunnableInterface *self) {
  self->run();
}

//  int Qt3DCore::RunnableInterface::id()
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore17RunnableInterface2idEv(
    Qt3DCore::RunnableInterface *self) {
  return self->id();
}

//  void Qt3DCore::RunnableInterface::setId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17RunnableInterface5setIdEi(
    Qt3DCore::RunnableInterface *self,
    int id) {
  self->setId(id);
}

//  void Qt3DCore::RunnableInterface::setReserved(bool reserved)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17RunnableInterface11setReservedEb(
    Qt3DCore::RunnableInterface *self,
    bool reserved) {
  self->setReserved(reserved);
}

//  bool Qt3DCore::RunnableInterface::reserved()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore17RunnableInterface8reservedEv(
    Qt3DCore::RunnableInterface *self) {
  return self->reserved();
}

//  void Qt3DCore::RunnableInterface::setPooler(QThreadPooler *pooler)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17RunnableInterface9setPoolerEPNS_13QThreadPoolerE(
    Qt3DCore::RunnableInterface *self,
    Qt3DCore::QThreadPooler *pooler) {
  self->setPooler(pooler);
}

//  RunnableType Qt3DCore::RunnableInterface::type() const
extern "C" Q_DECL_EXPORT
Qt3DCore::RunnableInterface::RunnableType ritual_ZNK8Qt3DCore17RunnableInterface4typeEv(
    const Qt3DCore::RunnableInterface *self) {
  return self->type();
}

//  a Python function taken by a CuteQt3DCore_RunnableInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_RunnableInterface(
    Qt3DCore::RunnableInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_RunnableInterface *>(self)->take(key, call);
}
