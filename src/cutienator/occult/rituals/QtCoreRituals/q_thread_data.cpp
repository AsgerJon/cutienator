//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  QThreadData::QThreadData(int initialRefCount)
extern "C" Q_DECL_EXPORT
QThreadData *ritual_ZN11QThreadDataC1Ei(int initialRefCount) {
  return new QThreadData(initialRefCount);
}

//  QThreadData *QThreadData::get2(QThread *thread)
extern "C" Q_DECL_EXPORT
QThreadData *ritual_ZN11QThreadData4get2EP7QThread(QThread *thread) {
  return QThreadData::get2(thread);
}

#if QT_CONFIG(thread)
//  void QThreadData::ref()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadData3refEv(QThreadData *self) {
  self->ref();
}
#endif  // QT_CONFIG(thread)

//  bool QThreadData::hasEventDispatcher() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QThreadData18hasEventDispatcherEv(const QThreadData *self) {
  return self->hasEventDispatcher();
}

//  bool QThreadData::canWaitLocked()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadData13canWaitLockedEv(QThreadData *self) {
  return self->canWaitLocked();
}

//  void QThreadData::clearEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadData11clearEventsEv(QThreadData *self) {
  self->clearEvents();
}
