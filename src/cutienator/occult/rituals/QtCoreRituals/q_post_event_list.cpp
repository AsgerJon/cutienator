//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qthread.h"
#include "qthread_p.h"
#include "qabstracteventdispatcher.h"
#include "qbindingstorage.h"
#include "private/qcoreapplication_p.h"
#include "qeventloop.h"
#include "qmutex.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/thread/qthread.cpp, line 23, as _ZN14QPostEventList8addEventERK10QPostEvent
inline void QPostEventList::addEvent(const QPostEvent &ev)
{
    int priority = ev.priority;
    if (isEmpty() ||
            constLast().priority >= priority ||
            insertionOffset >= size()) {
        // optimization: we can simply append if the last event in
        // the queue has higher or equal priority
        append(ev);
    } else {
        // insert event in descending priority order, using upper
        // bound for a given priority (to ensure proper ordering
        // of events with the same priority)
        QPostEventList::iterator at = std::upper_bound(begin() + insertionOffset, end(), ev);
        insert(at, ev);
    }
}
//  -----------------------------------------------------------------------

//  QPostEventList::QPostEventList()
extern "C" Q_DECL_EXPORT
QPostEventList *ritual_ZN14QPostEventListC1Ev() {
  return new QPostEventList();
}

//  void QPostEventList::addEvent(const QPostEvent &ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPostEventList8addEventERK10QPostEvent(
    QPostEventList *self,
    const QPostEvent *ev) {
  self->addEvent(*ev);
}
