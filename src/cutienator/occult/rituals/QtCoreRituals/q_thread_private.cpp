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
