//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(thread)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qthread.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qbindingstorage.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qeventloop.h>
#include <QtCore/qmutex.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qtools_p.h>
#if defined(Q_OS_WASM)
#  include <QtCore/private/qeventdispatcher_wasm_p.h>
#else
#  include <QtCore/private/qeventdispatcher_unix_p.h>
#  if defined(Q_OS_DARWIN)
#    include <QtCore/private/qeventdispatcher_cf_p.h>
#  elif !defined(QT_NO_GLIB)
#    include <QtCore/private/qeventdispatcher_glib_p.h>
#  endif
#endif
#include <sched.h>
#include <errno.h>
#if __has_include(<pthread_np.h>)
#  include <pthread_np.h>
#endif
#if defined(Q_OS_FREEBSD)
#  include <sys/cpuset.h>
#elif defined(Q_OS_BSD4)
#  include <sys/sysctl.h>
#endif
#ifdef Q_OS_VXWORKS
#  include <vxCpuLib.h>
#  include <cpuset.h>
#endif
#ifdef Q_OS_HPUX
#include <sys/pstat.h>
#endif
#if defined(Q_OS_LINUX) && !defined(QT_LINUXBASE)
#include <sys/prctl.h>
#endif
#if defined(Q_OS_QNX)
#include <sys/neutrino.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/thread/qthread_unix.cpp, line 100, as local:qthread_unix.cpp:UsingPThreadTimedJoin
#if QT_CONFIG(thread)
static constexpr bool UsingPThreadTimedJoin = QT_CONFIG(pthread_clockjoin)
        || (QT_CONFIG(pthread_timedjoin) && QWaitConditionClockId == CLOCK_REALTIME);
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread_unix.cpp, line 413, as local:qthread_unix.cpp:setCancellationEnabled
#if QT_CONFIG(thread)
static void setCancellationEnabled(bool enable)
{
#ifdef PTHREAD_CANCEL_DISABLE
    if (enable) {
        // may unwind the stack, see above
        pthread_setcancelstate(PTHREAD_CANCEL_ENABLE, nullptr);
        pthread_testcancel();
    } else {
        // this doesn't unwind the stack
        pthread_setcancelstate(PTHREAD_CANCEL_DISABLE, nullptr);
    }
#else
    Q_UNUSED(enable)
#endif
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread_unix.cpp, line 958, as local:qthread_unix.cpp:wakeAllInternal
#if QT_CONFIG(thread)
static void wakeAllInternal(QThreadPrivate *d)
{
    d->threadState = QThreadPrivate::Finished;
    if (d->waiters)
        d->thread_done.wakeAll();
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread.cpp, line 688, as _ZN9QtPrivate19BindingStatusOrList28addObjectUnlessAlreadyStatusEP7QObject
#if QT_CONFIG(thread)
inline QBindingStatus *QtPrivate::BindingStatusOrList::addObjectUnlessAlreadyStatus(QObject *object)
{
    if (auto status = bindingStatus())
        return status;
    List *objectList = list();
    if (!objectList) {
        objectList = new List();
        objectList->reserve(8);
        data.store(encodeList(objectList), std::memory_order_relaxed);
    }
    objectList->push_back(object);
    return nullptr;
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread.cpp, line 706, as _ZN9QtPrivate19BindingStatusOrList12removeObjectEP7QObject
#if QT_CONFIG(thread)
inline void QtPrivate::BindingStatusOrList::removeObject(QObject *object)
{
    List *objectList = list();
    if (!objectList)
        return;
    auto it = std::remove(objectList->begin(), objectList->end(), object);
    objectList->erase(it, objectList->end());
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread.cpp, line 1025, as _ZNK14QThreadPrivate8threadIdEv
#if QT_CONFIG(thread)
inline Qt::HANDLE QThreadPrivate::threadId() const noexcept
{
    return data->threadId.loadRelaxed();
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread_unix.cpp, line 965, as _ZN14QThreadPrivate7wakeAllEv
#if QT_CONFIG(thread)
inline void QThreadPrivate::wakeAll()
{
    if (data->isAdopted || !UsingPThreadTimedJoin)
        wakeAllInternal(this);
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread_unix.cpp, line 511, as _ZN14QThreadPrivate7cleanupEv
#if QT_CONFIG(thread)
inline void QThreadPrivate::cleanup()
{
    QThreadPrivate *d = this;

    // Disable cancellation again: we did it above, but some user code
    // running between finish() and cleanup() may have turned them back on.
    setCancellationEnabled(false);

    QMutexLocker locker(&d->mutex);
    d->priority = QThread::InheritPriority;

    QAbstractEventDispatcher *eventDispatcher = d->data->eventDispatcher.loadRelaxed();
    if (eventDispatcher) {
        d->data->eventDispatcher = nullptr;
        locker.unlock();
        eventDispatcher->closingDown();
        delete eventDispatcher;
        locker.relock();
    }

    d->interruptionRequested.store(false, std::memory_order_relaxed);

    d->wakeAll();
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread.cpp, line 715, as _ZN14QThreadPrivate39addObjectWithPendingBindingStatusChangeEP7QObject
#if QT_CONFIG(thread)
inline QBindingStatus *QThreadPrivate::addObjectWithPendingBindingStatusChange(QObject *obj)
{
    if (auto status = data->m_statusOrPendingObjects.bindingStatus())
        return status;
    QMutexLocker lock(&mutex);
    return data->m_statusOrPendingObjects.addObjectUnlessAlreadyStatus(obj);
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread.cpp, line 723, as _ZN14QThreadPrivate42removeObjectWithPendingBindingStatusChangeEP7QObject
#if QT_CONFIG(thread)
inline void QThreadPrivate::removeObjectWithPendingBindingStatusChange(QObject *obj)
{
    if (data->m_statusOrPendingObjects.bindingStatus())
        return;
    QMutexLocker lock(&mutex);
    data->m_statusOrPendingObjects.removeObject(obj);
}
#endif  // QT_CONFIG(thread)
//  -----------------------------------------------------------------------

//  QThread *QThreadPrivate::q_func()
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN14QThreadPrivate6q_funcEv(QThreadPrivate *self) {
  return self->q_func();
}

//  const QThread *QThreadPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QThread *ritual_ZNK14QThreadPrivate6q_funcEv(
    const QThreadPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(thread)
//  Qt::HANDLE QThreadPrivate::threadId() const
extern "C" Q_DECL_EXPORT
Qt::HANDLE ritual_ZNK14QThreadPrivate8threadIdEv(
    const QThreadPrivate *self) {
  return self->threadId();
}
#endif  // QT_CONFIG(thread)

#if defined(Q_OS_UNIX)
#if QT_CONFIG(thread)
//  void QThreadPrivate::wakeAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QThreadPrivate7wakeAllEv(QThreadPrivate *self) {
  self->wakeAll();
}
#endif  // QT_CONFIG(thread)
#endif  // defined(Q_OS_UNIX)

#if defined(Q_OS_UNIX)
#if QT_CONFIG(thread)
//  void QThreadPrivate::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QThreadPrivate7cleanupEv(QThreadPrivate *self) {
  self->cleanup();
}
#endif  // QT_CONFIG(thread)
#endif  // defined(Q_OS_UNIX)

//  void QThreadPrivate::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QThreadPrivate3refEv(QThreadPrivate *self) {
  self->ref();
}

//  void QThreadPrivate::deref()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QThreadPrivate5derefEv(QThreadPrivate *self) {
  self->deref();
}

//  QBindingStatus *QThreadPrivate::bindingStatus()
extern "C" Q_DECL_EXPORT
QBindingStatus *ritual_ZN14QThreadPrivate13bindingStatusEv(
    QThreadPrivate *self) {
  return self->bindingStatus();
}

#if QT_CONFIG(thread)
//  QBindingStatus
//      *QThreadPrivate::addObjectWithPendingBindingStatusChange(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
QBindingStatus *ritual_ZN14QThreadPrivate39addObjectWithPendingBindingStatusChangeEP7QObject(
    QThreadPrivate *self,
    QObject *obj) {
  return self->addObjectWithPendingBindingStatusChange(obj);
}
#endif  // QT_CONFIG(thread)

#if QT_CONFIG(thread)
//  void QThreadPrivate::removeObjectWithPendingBindingStatusChange(QObject
//      *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QThreadPrivate42removeObjectWithPendingBindingStatusChangeEP7QObject(
    QThreadPrivate *self,
    QObject *obj) {
  self->removeObjectWithPendingBindingStatusChange(obj);
}
#endif  // QT_CONFIG(thread)

#endif  // QT_CONFIG(thread)
