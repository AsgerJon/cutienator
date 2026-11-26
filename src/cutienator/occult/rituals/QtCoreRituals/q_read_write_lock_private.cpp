//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qreadwritelock_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(thread)
#if QT_CONFIG(thread)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qreadwritelock_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qreadwritelock.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qreadwritelock_p.h>
#include <QtCore/private/qfreelist_p.h>
#include <QtCore/private/qlocking_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/thread/qreadwritelock.cpp, line 496, as local:qreadwritelock.cpp:handleEquals
static auto handleEquals(Qt::HANDLE handle)
{
    return [handle](QReadWriteLockPrivate::Reader reader) { return reader.handle == handle; };
}

//  from src/corelib/thread/qreadwritelock.cpp, line 457, as _ZN21QReadWriteLockPrivate12lockForWriteERSt11unique_lockISt5mutexE14QDeadlineTimer
inline bool QReadWriteLockPrivate::lockForWrite(std::unique_lock<std::mutex> &lock, QDeadlineTimer timeout)
{
    using std::chrono::steady_clock;
    Q_ASSERT(!mutex.try_lock()); // mutex must be locked when entering this function

    while (readerCount || writerCount) {
        if (timeout.hasExpired()) {
            if (waitingReaders && !waitingWriters && !writerCount) {
                // We timed out and now there is no more writers or waiting writers, but some
                // readers were queued (probably because of us). Wake the waiting readers.
                readerCond.notify_all();
            }
            return false;
        }
        if (!timeout.isForever()) {
            waitingWriters++;
            writerCond.wait_until(lock, timeout.deadline<steady_clock>());
        } else {
            waitingWriters++;
            writerCond.wait(lock);
        }
        waitingWriters--;
    }

    Q_ASSERT(writerCount == 0);
    Q_ASSERT(readerCount == 0);
    writerCount = 1;
    return true;
}

//  from src/corelib/thread/qreadwritelock.cpp, line 435, as _ZN21QReadWriteLockPrivate11lockForReadERSt11unique_lockISt5mutexE14QDeadlineTimer
inline bool QReadWriteLockPrivate::lockForRead(std::unique_lock<std::mutex> &lock, QDeadlineTimer timeout)
{
    using std::chrono::steady_clock;
    Q_ASSERT(!mutex.try_lock()); // mutex must be locked when entering this function

    while (waitingWriters || writerCount) {
        if (timeout.hasExpired())
            return false;
        if (!timeout.isForever()) {
            waitingReaders++;
            readerCond.wait_until(lock, timeout.deadline<steady_clock>());
        } else {
            waitingReaders++;
            readerCond.wait(lock);
        }
        waitingReaders--;
    }
    readerCount++;
    Q_ASSERT(writerCount == 0);
    return true;
}

//  from src/corelib/thread/qreadwritelock.cpp, line 487, as _ZN21QReadWriteLockPrivate6unlockEv
inline void QReadWriteLockPrivate::unlock()
{
    Q_ASSERT(!mutex.try_lock()); // mutex must be locked when entering this function
    if (waitingWriters)
        writerCond.notify_one();
    else if (waitingReaders)
        readerCond.notify_all();
}

//  from src/corelib/thread/qreadwritelock.cpp, line 523, as _ZN21QReadWriteLockPrivate21recursiveLockForWriteE14QDeadlineTimer
inline bool QReadWriteLockPrivate::recursiveLockForWrite(QDeadlineTimer timeout)
{
    Q_ASSERT(recursive);
    auto lock = qt_unique_lock(mutex);

    Qt::HANDLE self = QThread::currentThreadId();
    if (currentWriter == self) {
        writerCount++;
        return true;
    }

    if (!lockForWrite(lock, timeout))
        return false;

    currentWriter = self;
    return true;
}

//  from src/corelib/thread/qreadwritelock.cpp, line 501, as _ZN21QReadWriteLockPrivate20recursiveLockForReadE14QDeadlineTimer
inline bool QReadWriteLockPrivate::recursiveLockForRead(QDeadlineTimer timeout)
{
    Q_ASSERT(recursive);
    auto lock = qt_unique_lock(mutex);

    Qt::HANDLE self = QThread::currentThreadId();

    auto it = std::find_if(currentReaders.begin(), currentReaders.end(),
                           handleEquals(self));
    if (it != currentReaders.end()) {
        ++it->recursionLevel;
        return true;
    }

    if (!lockForRead(lock, timeout))
        return false;

    Reader r = {self, 1};
    currentReaders.append(std::move(r));
    return true;
}
//  -----------------------------------------------------------------------

//  QReadWriteLockPrivate::QReadWriteLockPrivate(bool isRecursive)
extern "C" Q_DECL_EXPORT
QReadWriteLockPrivate *ritual_ZN21QReadWriteLockPrivateC1Eb(
    bool isRecursive) {
  return new QReadWriteLockPrivate(isRecursive);
}

//  bool QReadWriteLockPrivate::lockForWrite(std::unique_lock<std::mutex>
//      &lock, QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QReadWriteLockPrivate12lockForWriteERSt11unique_lockISt5mutexE14QDeadlineTimer(
    QReadWriteLockPrivate *self,
    std::unique_lock<std::mutex> *lock,
    const QDeadlineTimer *timeout) {
  return self->lockForWrite(*lock, *timeout);
}

//  bool QReadWriteLockPrivate::lockForRead(std::unique_lock<std::mutex>
//      &lock, QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QReadWriteLockPrivate11lockForReadERSt11unique_lockISt5mutexE14QDeadlineTimer(
    QReadWriteLockPrivate *self,
    std::unique_lock<std::mutex> *lock,
    const QDeadlineTimer *timeout) {
  return self->lockForRead(*lock, *timeout);
}

//  void QReadWriteLockPrivate::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QReadWriteLockPrivate6unlockEv(QReadWriteLockPrivate *self) {
  self->unlock();
}

//  bool QReadWriteLockPrivate::recursiveLockForWrite(QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QReadWriteLockPrivate21recursiveLockForWriteE14QDeadlineTimer(
    QReadWriteLockPrivate *self,
    const QDeadlineTimer *timeout) {
  return self->recursiveLockForWrite(*timeout);
}

//  bool QReadWriteLockPrivate::recursiveLockForRead(QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QReadWriteLockPrivate20recursiveLockForReadE14QDeadlineTimer(
    QReadWriteLockPrivate *self,
    const QDeadlineTimer *timeout) {
  return self->recursiveLockForRead(*timeout);
}

//  quintptr QReadWriteLockPrivate::describeState(void *dd)
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN21QReadWriteLockPrivate13describeStateEPv(void *dd) {
  return QReadWriteLockPrivate::describeState(dd);
}

#endif  // QT_CONFIG(thread)
#endif  // QT_CONFIG(thread)
