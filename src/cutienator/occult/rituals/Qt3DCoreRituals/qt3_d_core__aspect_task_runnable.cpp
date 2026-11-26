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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/jobs/task.cpp, line 17, as _ZN8Qt3DCore17RunnableInterfaceD2Ev
namespace Qt3DCore {
inline RunnableInterface::~RunnableInterface()
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 40, as _ZN8Qt3DCore18AspectTaskRunnable3runEv
namespace Qt3DCore {
inline void AspectTaskRunnable::run()
{
    if (m_job) {
        QAspectJobPrivate *jobD = QAspectJobPrivate::get(m_job.data());
        QTaskLogger logger(m_pooler ? m_service : nullptr, jobD->m_jobId, QTaskLogger::AspectJob);
        m_job->run();
    }

    // We could have an append sub task or something in here
    // So that a job can post sub jobs ?

    if (m_pooler)
        m_pooler->taskFinished(this);
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 35, as _ZNK8Qt3DCore18AspectTaskRunnable10isRequiredEv
namespace Qt3DCore {
inline bool AspectTaskRunnable::isRequired() const
{
    return m_job ? QAspectJobPrivate::get(m_job.data())->isRequired() : false;
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 23, as _ZN8Qt3DCore18AspectTaskRunnableC1EPNS_25QSystemInformationServiceE
namespace Qt3DCore {
inline AspectTaskRunnable::AspectTaskRunnable(QSystemInformationService *service)
    : m_service(service)
    , m_pooler(nullptr)
    , m_id(0)
    , m_reserved(false)
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/jobs/task.cpp, line 31, as _ZN8Qt3DCore18AspectTaskRunnableD1Ev
namespace Qt3DCore {
inline AspectTaskRunnable::~AspectTaskRunnable()
{
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  A Qt3DCore::AspectTaskRunnable that Python can take functions over in. Every Qt3DCore::AspectTaskRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DCore_AspectTaskRunnableCall0)(const void *, int *);
typedef void (*CuteQt3DCore_AspectTaskRunnableCall1)(const void *, int *);
typedef void (*CuteQt3DCore_AspectTaskRunnableCall2)(const void *, Qt3DCore::QThreadPooler *, int *);
typedef void (*CuteQt3DCore_AspectTaskRunnableCall3)(const void *, bool, int *);
typedef bool (*CuteQt3DCore_AspectTaskRunnableCall4)(const void *, int *);
typedef int (*CuteQt3DCore_AspectTaskRunnableCall5)(const void *, int *);
typedef void (*CuteQt3DCore_AspectTaskRunnableCall6)(const void *, int, int *);
typedef int (*CuteQt3DCore_AspectTaskRunnableCall7)(const void *, int *);
class CuteQt3DCore_AspectTaskRunnable : public Qt3DCore::AspectTaskRunnable {
public:
  using Qt3DCore::AspectTaskRunnable::AspectTaskRunnable;
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

  //  bool Qt3DCore::AspectTaskRunnable::isRequired() const
  bool isRequired() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall0 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::AspectTaskRunnable::isRequired();
  }

  //  void Qt3DCore::AspectTaskRunnable::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall1 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::AspectTaskRunnable::run();
  }

  //  void Qt3DCore::AspectTaskRunnable::setPooler(QThreadPooler *pooler)
  void setPooler(Qt3DCore::QThreadPooler *pooler) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall2 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall2>(taken[2]);
      call(this, pooler, &handled);
      if (handled) return;
    }
    Qt3DCore::AspectTaskRunnable::setPooler(pooler);
  }

  //  void Qt3DCore::AspectTaskRunnable::setReserved(bool reserved)
  void setReserved(bool reserved) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall3 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall3>(taken[3]);
      call(this, reserved, &handled);
      if (handled) return;
    }
    Qt3DCore::AspectTaskRunnable::setReserved(reserved);
  }

  //  bool Qt3DCore::AspectTaskRunnable::reserved()
  bool reserved() override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall4 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::AspectTaskRunnable::reserved();
  }

  //  int Qt3DCore::AspectTaskRunnable::id()
  int id() override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall5 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::AspectTaskRunnable::id();
  }

  //  void Qt3DCore::AspectTaskRunnable::setId(int id)
  void setId(int id) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall6 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall6>(taken[6]);
      call(this, id, &handled);
      if (handled) return;
    }
    Qt3DCore::AspectTaskRunnable::setId(id);
  }

  //  RunnableType Qt3DCore::AspectTaskRunnable::type() const
  Qt3DCore::RunnableInterface::RunnableType type() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_AspectTaskRunnableCall7 call = reinterpret_cast<CuteQt3DCore_AspectTaskRunnableCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DCore::RunnableInterface::RunnableType>(given);
    }
    return Qt3DCore::AspectTaskRunnable::type();
  }
};

//  Qt3DCore::AspectTaskRunnable::AspectTaskRunnable(QSystemInformationServic
//      e *service)
extern "C" Q_DECL_EXPORT
Qt3DCore::AspectTaskRunnable *ritual_ZN8Qt3DCore18AspectTaskRunnableC1EPNS_25QSystemInformationServiceE(
    Qt3DCore::QSystemInformationService *service) {
  return new CuteQt3DCore_AspectTaskRunnable(service);
}

//  Qt3DCore::AspectTaskRunnable::~AspectTaskRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18AspectTaskRunnableD1Ev(
    Qt3DCore::AspectTaskRunnable *self) {
  delete self;
}

//  bool Qt3DCore::AspectTaskRunnable::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore18AspectTaskRunnable10isRequiredEv(
    const Qt3DCore::AspectTaskRunnable *self) {
  return self->isRequired();
}

//  void Qt3DCore::AspectTaskRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18AspectTaskRunnable3runEv(
    Qt3DCore::AspectTaskRunnable *self) {
  self->run();
}

//  void Qt3DCore::AspectTaskRunnable::setPooler(QThreadPooler *pooler)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18AspectTaskRunnable9setPoolerEPNS_13QThreadPoolerE(
    Qt3DCore::AspectTaskRunnable *self,
    Qt3DCore::QThreadPooler *pooler) {
  self->setPooler(pooler);
}

//  void Qt3DCore::AspectTaskRunnable::setReserved(bool reserved)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18AspectTaskRunnable11setReservedEb(
    Qt3DCore::AspectTaskRunnable *self,
    bool reserved) {
  self->setReserved(reserved);
}

//  bool Qt3DCore::AspectTaskRunnable::reserved()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore18AspectTaskRunnable8reservedEv(
    Qt3DCore::AspectTaskRunnable *self) {
  return self->reserved();
}

//  int Qt3DCore::AspectTaskRunnable::id()
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore18AspectTaskRunnable2idEv(
    Qt3DCore::AspectTaskRunnable *self) {
  return self->id();
}

//  void Qt3DCore::AspectTaskRunnable::setId(int id)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore18AspectTaskRunnable5setIdEi(
    Qt3DCore::AspectTaskRunnable *self,
    int id) {
  self->setId(id);
}

//  RunnableType Qt3DCore::AspectTaskRunnable::type() const
extern "C" Q_DECL_EXPORT
Qt3DCore::RunnableInterface::RunnableType ritual_ZNK8Qt3DCore18AspectTaskRunnable4typeEv(
    const Qt3DCore::AspectTaskRunnable *self) {
  return self->type();
}

//  a Python function taken by a CuteQt3DCore_AspectTaskRunnable, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_AspectTaskRunnable(
    Qt3DCore::AspectTaskRunnable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_AspectTaskRunnable *>(self)->take(key, call);
}

//  bool Qt3DCore::AspectTaskRunnable::isRequired() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK8Qt3DCore18AspectTaskRunnable10isRequiredEv(
    const Qt3DCore::AspectTaskRunnable *self) {
  return self->Qt3DCore::AspectTaskRunnable::isRequired();
}

//  void Qt3DCore::AspectTaskRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore18AspectTaskRunnable3runEv(
    Qt3DCore::AspectTaskRunnable *self) {
  self->Qt3DCore::AspectTaskRunnable::run();
}

//  void Qt3DCore::AspectTaskRunnable::setPooler(QThreadPooler *pooler)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore18AspectTaskRunnable9setPoolerEPNS_13QThreadPoolerE(
    Qt3DCore::AspectTaskRunnable *self,
    Qt3DCore::QThreadPooler *pooler) {
  self->Qt3DCore::AspectTaskRunnable::setPooler(pooler);
}

//  void Qt3DCore::AspectTaskRunnable::setReserved(bool reserved)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore18AspectTaskRunnable11setReservedEb(
    Qt3DCore::AspectTaskRunnable *self,
    bool reserved) {
  self->Qt3DCore::AspectTaskRunnable::setReserved(reserved);
}

//  bool Qt3DCore::AspectTaskRunnable::reserved()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN8Qt3DCore18AspectTaskRunnable8reservedEv(
    Qt3DCore::AspectTaskRunnable *self) {
  return self->Qt3DCore::AspectTaskRunnable::reserved();
}

//  int Qt3DCore::AspectTaskRunnable::id()
extern "C" Q_DECL_EXPORT
int ritual_own_ZN8Qt3DCore18AspectTaskRunnable2idEv(
    Qt3DCore::AspectTaskRunnable *self) {
  return self->Qt3DCore::AspectTaskRunnable::id();
}

//  void Qt3DCore::AspectTaskRunnable::setId(int id)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore18AspectTaskRunnable5setIdEi(
    Qt3DCore::AspectTaskRunnable *self,
    int id) {
  self->Qt3DCore::AspectTaskRunnable::setId(id);
}

//  RunnableType Qt3DCore::AspectTaskRunnable::type() const
extern "C" Q_DECL_EXPORT
Qt3DCore::RunnableInterface::RunnableType ritual_own_ZNK8Qt3DCore18AspectTaskRunnable4typeEv(
    const Qt3DCore::AspectTaskRunnable *self) {
  return self->Qt3DCore::AspectTaskRunnable::type();
}
