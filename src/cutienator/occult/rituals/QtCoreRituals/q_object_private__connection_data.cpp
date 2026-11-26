//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qbindingstorage.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qeventloop.h>
#include <QtCore/qmutex.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/thread/qthread.cpp, line 46, as _ZN11QThreadDataD1Ev
inline QThreadData::~QThreadData()
{
#if QT_CONFIG(thread)
    Q_ASSERT(_ref.loadRelaxed() == 0);
#endif

    if (threadId.loadAcquire() == QCoreApplicationPrivate::theMainThreadId.loadAcquire()) {
        QCoreApplicationPrivate::theMainThread.storeRelease(nullptr);
        QCoreApplicationPrivate::theMainThreadId.storeRelaxed(nullptr);
        QThreadData::clearCurrentThreadData();
    }

    // ~QThread() sets thread to nullptr, so if it isn't null here, it's
    // because we're being run before the main object itself. This can only
    // happen for QAdoptedThread. Note that both ~QThreadPrivate() and
    // ~QObjectPrivate() will deref this object again, but that is acceptable
    // because this destructor is still running (the _ref sub-object has not
    // been destroyed) and there's no reentrancy. The refcount will become
    // negative, but that's acceptable.
    QThread *t = thread.loadAcquire();
    thread.storeRelease(nullptr);
    delete t;

    clearEvents();

    // fprintf(stderr, "QThreadData %p destroyed\n", this);
}

//  from src/corelib/thread/qthread.cpp, line 74, as _ZN11QThreadData11clearEventsEv
inline void QThreadData::clearEvents()
{
    for (const auto &pe : std::as_const(postEventList)) {
        if (pe.event) {
            pe.receiver->d_func()->postedEvents.fetchAndSubRelaxed(1);
            pe.event->m_posted = false;
            delete pe.event;
        }
    }
    postEventList.clear();
}
//  -----------------------------------------------------------------------

//  ConnectionList &QObjectPrivate::ConnectionData::connectionsForSignal(int
//      signal)
extern "C" Q_DECL_EXPORT
QObjectPrivate::ConnectionList *ritual_ZN14QObjectPrivate14ConnectionData20connectionsForSignalEi(
    QObjectPrivate::ConnectionData *self,
    int signal) {
  return &(self->connectionsForSignal(signal));
}

//  void QObjectPrivate::ConnectionData::resizeSignalVector(size_t size)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate14ConnectionData18resizeSignalVectorEm(
    QObjectPrivate::ConnectionData *self,
    size_t size) {
  self->resizeSignalVector(size);
}

//  int QObjectPrivate::ConnectionData::signalVectorCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QObjectPrivate14ConnectionData17signalVectorCountEv(
    const QObjectPrivate::ConnectionData *self) {
  return self->signalVectorCount();
}
