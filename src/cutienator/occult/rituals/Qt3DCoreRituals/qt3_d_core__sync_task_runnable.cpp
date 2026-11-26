//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/task_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/task_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/private/task_p.h>
#include <QtCore/QDebug>
#include <QtCore/QElapsedTimer>
#include <QtCore/QMutexLocker>
#include <Qt3DCore/private/qthreadpooler_p.h>
#include <Qt3DCore/private/qsysteminformationservice_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/jobs/task.cpp, line 77, as _ZN8Qt3DCore16SyncTaskRunnable3runEv
namespace Qt3DCore {
inline void SyncTaskRunnable::run()
{
    // Call the function
    m_func(m_arg);

    // Decrement the atomic counter to let others know we've done our bit
    m_atomicCount->deref();

    // Wait for the other worker threads to be done
    while (m_atomicCount->loadRelaxed() > 0)
        QThread::currentThread()->yieldCurrentThread();

    if (m_pooler)
        m_pooler->taskFinished(this);
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 17, as _ZN8Qt3DCore17RunnableInterfaceD2Ev
namespace Qt3DCore {
inline RunnableInterface::~RunnableInterface()
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 72, as _ZNK8Qt3DCore16SyncTaskRunnable10isRequiredEv
namespace Qt3DCore {
inline bool SyncTaskRunnable::isRequired() const
{
    return true;
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 68, as _ZN8Qt3DCore16SyncTaskRunnableD1Ev
namespace Qt3DCore {
inline SyncTaskRunnable::~SyncTaskRunnable()
{
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  A Qt3DCore::SyncTaskRunnable that Python can take functions over in. Every Qt3DCore::SyncTaskRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DCore_SyncTaskRunnableCall0)(const void *, int *);
typedef void (*CuteQt3DCore_SyncTaskRunnableCall1)(const void *, int *);
typedef void (*CuteQt3DCore_SyncTaskRunnableCall2)(const void *, Qt3DCore::QThreadPooler *, int *);
typedef void (*CuteQt3DCore_SyncTaskRunnableCall3)(const void *, bool, int *);
typedef bool (*CuteQt3DCore_SyncTaskRunnableCall4)(const void *, int *);
typedef int (*CuteQt3DCore_SyncTaskRunnableCall5)(const void *, int *);
typedef void (*CuteQt3DCore_SyncTaskRunnableCall6)(const void *, int, int *);
typedef int (*CuteQt3DCore_SyncTaskRunnableCall7)(const void *, int *);
class CuteQt3DCore_SyncTaskRunnable : public Qt3DCore::SyncTaskRunnable {
public:
  using Qt3DCore::SyncTaskRunnable::SyncTaskRunnable;
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
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface9setPoolerEPNS_13QThreadPoolerE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface11setReservedEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface8reservedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface2idEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore17RunnableInterface5setIdEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore17RunnableInterface4typeEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DCore::SyncTaskRunnable::isRequired() const
  bool isRequired() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall0 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::SyncTaskRunnable::isRequired();
  }

  //  void Qt3DCore::SyncTaskRunnable::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall1 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::SyncTaskRunnable::run();
  }

  //  void Qt3DCore::SyncTaskRunnable::setPooler(QThreadPooler *pooler)
  void setPooler(Qt3DCore::QThreadPooler *pooler) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall2 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall2>(taken[2]);
      call(this, pooler, &handled);
      if (handled) return;
    }
    Qt3DCore::SyncTaskRunnable::setPooler(pooler);
  }

  //  void Qt3DCore::SyncTaskRunnable::setReserved(bool reserved)
  void setReserved(bool reserved) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall3 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall3>(taken[3]);
      call(this, reserved, &handled);
      if (handled) return;
    }
    Qt3DCore::SyncTaskRunnable::setReserved(reserved);
  }

  //  bool Qt3DCore::SyncTaskRunnable::reserved()
  bool reserved() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall4 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::SyncTaskRunnable::reserved();
  }

  //  int Qt3DCore::SyncTaskRunnable::id()
  int id() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall5 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::SyncTaskRunnable::id();
  }

  //  void Qt3DCore::SyncTaskRunnable::setId(int id)
  void setId(int id) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall6 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall6>(taken[6]);
      call(this, id, &handled);
      if (handled) return;
    }
    Qt3DCore::SyncTaskRunnable::setId(id);
  }

  //  RunnableType Qt3DCore::SyncTaskRunnable::type() const
  Qt3DCore::RunnableInterface::RunnableType type() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_SyncTaskRunnableCall7 call = reinterpret_cast<CuteQt3DCore_SyncTaskRunnableCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DCore::RunnableInterface::RunnableType>(given);
    }
    return Qt3DCore::SyncTaskRunnable::type();
  }
};

//  Qt3DCore::SyncTaskRunnable::~SyncTaskRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16SyncTaskRunnableD1Ev(
    Qt3DCore::SyncTaskRunnable *self) {
  delete self;
}

//  bool Qt3DCore::SyncTaskRunnable::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore16SyncTaskRunnable10isRequiredEv(
    const Qt3DCore::SyncTaskRunnable *self) {
  return self->isRequired();
}

//  void Qt3DCore::SyncTaskRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16SyncTaskRunnable3runEv(
    Qt3DCore::SyncTaskRunnable *self) {
  self->run();
}

//  void Qt3DCore::SyncTaskRunnable::setPooler(QThreadPooler *pooler)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16SyncTaskRunnable9setPoolerEPNS_13QThreadPoolerE(
    Qt3DCore::SyncTaskRunnable *self,
    Qt3DCore::QThreadPooler *pooler) {
  self->setPooler(pooler);
}

//  void Qt3DCore::SyncTaskRunnable::setReserved(bool reserved)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16SyncTaskRunnable11setReservedEb(
    Qt3DCore::SyncTaskRunnable *self,
    bool reserved) {
  self->setReserved(reserved);
}

//  bool Qt3DCore::SyncTaskRunnable::reserved()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore16SyncTaskRunnable8reservedEv(
    Qt3DCore::SyncTaskRunnable *self) {
  return self->reserved();
}

//  int Qt3DCore::SyncTaskRunnable::id()
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore16SyncTaskRunnable2idEv(
    Qt3DCore::SyncTaskRunnable *self) {
  return self->id();
}

//  void Qt3DCore::SyncTaskRunnable::setId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore16SyncTaskRunnable5setIdEi(
    Qt3DCore::SyncTaskRunnable *self,
    int id) {
  self->setId(id);
}

//  RunnableType Qt3DCore::SyncTaskRunnable::type() const
extern "C" Q_DECL_EXPORT
Qt3DCore::RunnableInterface::RunnableType ritual_ZNK8Qt3DCore16SyncTaskRunnable4typeEv(
    const Qt3DCore::SyncTaskRunnable *self) {
  return self->type();
}

//  a Python function taken by a CuteQt3DCore_SyncTaskRunnable, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_SyncTaskRunnable(
    Qt3DCore::SyncTaskRunnable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_SyncTaskRunnable *>(self)->take(key, call);
}

//  bool Qt3DCore::SyncTaskRunnable::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8Qt3DCore16SyncTaskRunnable10isRequiredEv(
    const Qt3DCore::SyncTaskRunnable *self) {
  return self->Qt3DCore::SyncTaskRunnable::isRequired();
}

//  void Qt3DCore::SyncTaskRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16SyncTaskRunnable3runEv(
    Qt3DCore::SyncTaskRunnable *self) {
  self->Qt3DCore::SyncTaskRunnable::run();
}

//  void Qt3DCore::SyncTaskRunnable::setPooler(QThreadPooler *pooler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16SyncTaskRunnable9setPoolerEPNS_13QThreadPoolerE(
    Qt3DCore::SyncTaskRunnable *self,
    Qt3DCore::QThreadPooler *pooler) {
  self->Qt3DCore::SyncTaskRunnable::setPooler(pooler);
}

//  void Qt3DCore::SyncTaskRunnable::setReserved(bool reserved)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16SyncTaskRunnable11setReservedEb(
    Qt3DCore::SyncTaskRunnable *self,
    bool reserved) {
  self->Qt3DCore::SyncTaskRunnable::setReserved(reserved);
}

//  bool Qt3DCore::SyncTaskRunnable::reserved()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8Qt3DCore16SyncTaskRunnable8reservedEv(
    Qt3DCore::SyncTaskRunnable *self) {
  return self->Qt3DCore::SyncTaskRunnable::reserved();
}

//  int Qt3DCore::SyncTaskRunnable::id()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN8Qt3DCore16SyncTaskRunnable2idEv(
    Qt3DCore::SyncTaskRunnable *self) {
  return self->Qt3DCore::SyncTaskRunnable::id();
}

//  void Qt3DCore::SyncTaskRunnable::setId(int id)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore16SyncTaskRunnable5setIdEi(
    Qt3DCore::SyncTaskRunnable *self,
    int id) {
  self->Qt3DCore::SyncTaskRunnable::setId(id);
}

//  RunnableType Qt3DCore::SyncTaskRunnable::type() const
extern "C" Q_DECL_EXPORT
Qt3DCore::RunnableInterface::RunnableType ritual_own_ZNK8Qt3DCore16SyncTaskRunnable4typeEv(
    const Qt3DCore::SyncTaskRunnable *self) {
  return self->Qt3DCore::SyncTaskRunnable::type();
}
