//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qscheduler_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qscheduler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/private/qscheduler_p.h>
#include <Qt3DCore/qabstractaspect.h>
#include <Qt3DCore/private/qabstractaspect_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/qabstractaspectjobmanager_p.h>
#include <Qt3DCore/private/vector_helper_p.h>
#include <QtCore/QCoreApplication>
#include <QtCore/QDateTime>
#include <QtCore/QRegularExpression>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/core/qscheduler.cpp, line 64, as _ZN8Qt3DCore10QSchedulerD1Ev
namespace Qt3DCore {
inline QScheduler::~QScheduler()
{
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/qscheduler.cpp, line 68, as _ZN8Qt3DCore10QScheduler16setAspectManagerEPNS_14QAspectManagerE
namespace Qt3DCore {
inline void QScheduler::setAspectManager(QAspectManager *aspectManager)
{
    m_aspectManager = aspectManager;
}
}  // namespace Qt3DCore

//  from ../qt3d/src/core/qscheduler.cpp, line 73, as _ZNK8Qt3DCore10QScheduler13aspectManagerEv
namespace Qt3DCore {
inline QAspectManager *QScheduler::aspectManager() const
{
    return m_aspectManager;
}
}  // namespace Qt3DCore
//  -----------------------------------------------------------------------

//  A Qt3DCore::QScheduler that Python can take functions over in. Every Qt3DCore::QScheduler
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQt3DCore_QSchedulerCall0)(const void *, qint64, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QSchedulerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DCore_QSchedulerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSchedulerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSchedulerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSchedulerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSchedulerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DCore_QSchedulerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DCore_QScheduler : public Qt3DCore::QScheduler {
public:
  using Qt3DCore::QScheduler::QScheduler;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QScheduler33scheduleAndWaitForFrameAspectJobsExb")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int Qt3DCore::QScheduler::scheduleAndWaitForFrameAspectJobs(qint64
  //      time, bool dumpJobs)
  int scheduleAndWaitForFrameAspectJobs(
      qint64 time,
      bool dumpJobs) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall0 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall0>(taken[0]);
      int given = call(this, time, dumpJobs, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QScheduler::scheduleAndWaitForFrameAspectJobs(time, dumpJobs);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall1 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall2 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall3 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall4 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall5 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall6 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DCore_QSchedulerCall7 call = reinterpret_cast<CuteQt3DCore_QSchedulerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DCore::QScheduler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8Qt3DCore10QScheduler10metaObjectEv(
    const Qt3DCore::QScheduler *self) {
  return self->metaObject();
}

//  void *Qt3DCore::QScheduler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8Qt3DCore10QScheduler11qt_metacastEPKc(
    Qt3DCore::QScheduler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DCore::QScheduler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore10QScheduler11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DCore::QScheduler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DCore::QScheduler::~QScheduler()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QSchedulerD1Ev(Qt3DCore::QScheduler *self) {
  delete self;
}

//  void Qt3DCore::QScheduler::setAspectManager(QAspectManager
//      *aspectManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore10QScheduler16setAspectManagerEPNS_14QAspectManagerE(
    Qt3DCore::QScheduler *self,
    Qt3DCore::QAspectManager *aspectManager) {
  self->setAspectManager(aspectManager);
}

//  QAspectManager *Qt3DCore::QScheduler::aspectManager() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectManager *ritual_ZNK8Qt3DCore10QScheduler13aspectManagerEv(
    const Qt3DCore::QScheduler *self) {
  return self->aspectManager();
}

//  int Qt3DCore::QScheduler::scheduleAndWaitForFrameAspectJobs(qint64 time,
//      bool dumpJobs)
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore10QScheduler33scheduleAndWaitForFrameAspectJobsExb(
    Qt3DCore::QScheduler *self,
    qint64 time,
    bool dumpJobs) {
  return self->scheduleAndWaitForFrameAspectJobs(time, dumpJobs);
}

//  a Python function taken by a CuteQt3DCore_QScheduler, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QScheduler(
    Qt3DCore::QScheduler *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QScheduler *>(self)->take(key, call);
}
