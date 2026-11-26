//  Written by dev_tooling.RitualGenerator from the records of
//  QtConcurrent/qtconcurrentthreadengine.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtConcurrent/qtconcurrent_global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtConcurrent/qtconcurrentthreadengine.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtConcurrent/qtconcurrentthreadengine.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/concurrent/qtconcurrentthreadengine.cpp, line 53, as _ZN12QtConcurrent19ThreadEngineBarrierC1Ev
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
namespace QtConcurrent {
inline ThreadEngineBarrier::ThreadEngineBarrier()
:count(0) { }
}  // namespace QtConcurrent
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

//  from src/concurrent/qtconcurrentthreadengine.cpp, line 56, as _ZN12QtConcurrent19ThreadEngineBarrier7acquireEv
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
namespace QtConcurrent {
inline void ThreadEngineBarrier::acquire()
{
    forever {
        int localCount = count.loadRelaxed();
        if (localCount < 0) {
            if (count.testAndSetOrdered(localCount, localCount -1))
                return;
        } else {
            if (count.testAndSetOrdered(localCount, localCount + 1))
                return;
        }
        qYieldCpu();
    }
}
}  // namespace QtConcurrent
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

//  from src/concurrent/qtconcurrentthreadengine.cpp, line 71, as _ZN12QtConcurrent19ThreadEngineBarrier7releaseEv
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
namespace QtConcurrent {
inline int ThreadEngineBarrier::release()
{
    forever {
        int localCount = count.loadRelaxed();
        if (localCount == -1) {
            if (count.testAndSetOrdered(-1, 0)) {
                semaphore.release();
                return 0;
            }
        } else if (localCount < 0) {
            if (count.testAndSetOrdered(localCount, localCount + 1))
                return qAbs(localCount + 1);
        } else {
            if (count.testAndSetOrdered(localCount, localCount - 1))
                return localCount - 1;
        }
        qYieldCpu();
    }
}
}  // namespace QtConcurrent
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

//  from src/concurrent/qtconcurrentthreadengine.cpp, line 92, as _ZN12QtConcurrent19ThreadEngineBarrier4waitEv
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
namespace QtConcurrent {
inline void ThreadEngineBarrier::wait()
{
    forever {
        int localCount = count.loadRelaxed();
        if (localCount == 0)
            return;

        Q_ASSERT(localCount > 0); // multiple waiters are not allowed.
        if (count.testAndSetOrdered(localCount, -localCount)) {
            semaphore.acquire();
            return;
        }
        qYieldCpu();
    }
}
}  // namespace QtConcurrent
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

//  from src/concurrent/qtconcurrentthreadengine.cpp, line 108, as _ZN12QtConcurrent19ThreadEngineBarrier12currentCountEv
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
namespace QtConcurrent {
inline int ThreadEngineBarrier::currentCount()
{
    return count.loadRelaxed();
}
}  // namespace QtConcurrent
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

//  from src/concurrent/qtconcurrentthreadengine.cpp, line 115, as _ZN12QtConcurrent19ThreadEngineBarrier17releaseUnlessLastEv
#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
namespace QtConcurrent {
inline bool ThreadEngineBarrier::releaseUnlessLast()
{
    forever {
        int localCount = count.loadRelaxed();
        if (qAbs(localCount) == 1) {
            return false;
        } else if (localCount < 0) {
            if (count.testAndSetOrdered(localCount, localCount + 1))
                return true;
        } else {
            if (count.testAndSetOrdered(localCount, localCount - 1))
                return true;
        }
        qYieldCpu();
    }
}
}  // namespace QtConcurrent
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
//  -----------------------------------------------------------------------

//  QtConcurrent::ThreadEngineBarrier::ThreadEngineBarrier()
extern "C" Q_DECL_EXPORT
QtConcurrent::ThreadEngineBarrier *ritual_ZN12QtConcurrent19ThreadEngineBarrierC1Ev() {
  return new QtConcurrent::ThreadEngineBarrier();
}

#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
//  void QtConcurrent::ThreadEngineBarrier::acquire()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent19ThreadEngineBarrier7acquireEv(
    QtConcurrent::ThreadEngineBarrier *self) {
  self->acquire();
}
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
//  int QtConcurrent::ThreadEngineBarrier::release()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QtConcurrent19ThreadEngineBarrier7releaseEv(
    QtConcurrent::ThreadEngineBarrier *self) {
  return self->release();
}
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
//  void QtConcurrent::ThreadEngineBarrier::wait()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent19ThreadEngineBarrier4waitEv(
    QtConcurrent::ThreadEngineBarrier *self) {
  self->wait();
}
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
//  int QtConcurrent::ThreadEngineBarrier::currentCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN12QtConcurrent19ThreadEngineBarrier12currentCountEv(
    QtConcurrent::ThreadEngineBarrier *self) {
  return self->currentCount();
}
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)
//  bool QtConcurrent::ThreadEngineBarrier::releaseUnlessLast()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QtConcurrent19ThreadEngineBarrier17releaseUnlessLastEv(
    QtConcurrent::ThreadEngineBarrier *self) {
  return self->releaseUnlessLast();
}
#endif  // !defined(QT_NO_CONCURRENT) || defined(Q_QDOC)

#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
