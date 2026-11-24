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

//  from src/corelib/thread/qthread.cpp, line 631, as _ZN9QtPrivate19BindingStatusOrList21setStatusAndClearListEP14QBindingStatus
inline void QtPrivate::BindingStatusOrList::setStatusAndClearList(QBindingStatus *status) noexcept
{
    if (auto pendingObjects = list()) {
        for (auto obj: *pendingObjects)
            QObjectPrivate::get(obj)->reinitBindingStorageAfterThreadMove();
        delete pendingObjects;
    }
    // synchronizes-with the load-acquire in bindingStatus():
    data.store(encodeBindingStatus(status), std::memory_order_release);
}
//  -----------------------------------------------------------------------

//  QtPrivate::BindingStatusOrList::BindingStatusOrList()
extern "C" Q_DECL_EXPORT
QtPrivate::BindingStatusOrList *ritual_ZN9QtPrivate19BindingStatusOrListC1Ev() {
  return new QtPrivate::BindingStatusOrList();
}

//  QtPrivate::BindingStatusOrList::BindingStatusOrList(QBindingStatus
//      *status)
extern "C" Q_DECL_EXPORT
QtPrivate::BindingStatusOrList *ritual_ZN9QtPrivate19BindingStatusOrListC1EP14QBindingStatus(
    QBindingStatus *status) {
  return new QtPrivate::BindingStatusOrList(status);
}

//  QtPrivate::BindingStatusOrList::~BindingStatusOrList()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19BindingStatusOrListD1Ev(
    QtPrivate::BindingStatusOrList *self) {
  delete self;
}

#if QT_CONFIG(thread)
//  QBindingStatus
//      *QtPrivate::BindingStatusOrList::addObjectUnlessAlreadyStatus(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QBindingStatus *ritual_ZN9QtPrivate19BindingStatusOrList28addObjectUnlessAlreadyStatusEP7QObject(
    QtPrivate::BindingStatusOrList *self,
    QObject *object) {
  return self->addObjectUnlessAlreadyStatus(object);
}
#endif  // QT_CONFIG(thread)

#if QT_CONFIG(thread)
//  void QtPrivate::BindingStatusOrList::removeObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19BindingStatusOrList12removeObjectEP7QObject(
    QtPrivate::BindingStatusOrList *self,
    QObject *object) {
  self->removeObject(object);
}
#endif  // QT_CONFIG(thread)

//  void QtPrivate::BindingStatusOrList::setStatusAndClearList(QBindingStatus
//      *status)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate19BindingStatusOrList21setStatusAndClearListEP14QBindingStatus(
    QtPrivate::BindingStatusOrList *self,
    QBindingStatus *status) {
  self->setStatusAndClearList(status);
}

//  bool QtPrivate::BindingStatusOrList::isBindingStatus(quintptr data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate19BindingStatusOrList15isBindingStatusEy(
    quintptr data) {
  return QtPrivate::BindingStatusOrList::isBindingStatus(data);
}

//  bool QtPrivate::BindingStatusOrList::isList(quintptr data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate19BindingStatusOrList6isListEy(quintptr data) {
  return QtPrivate::BindingStatusOrList::isList(data);
}

//  bool QtPrivate::BindingStatusOrList::isNull(quintptr data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QtPrivate19BindingStatusOrList6isNullEy(quintptr data) {
  return QtPrivate::BindingStatusOrList::isNull(data);
}

//  QBindingStatus *QtPrivate::BindingStatusOrList::bindingStatus() const
extern "C" Q_DECL_EXPORT
QBindingStatus *ritual_ZNK9QtPrivate19BindingStatusOrList13bindingStatusEv(
    const QtPrivate::BindingStatusOrList *self) {
  return self->bindingStatus();
}

//  quintptr
//      QtPrivate::BindingStatusOrList::encodeBindingStatus(QBindingStatus
//      *status)
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN9QtPrivate19BindingStatusOrList19encodeBindingStatusEP14QBindingStatus(
    QBindingStatus *status) {
  return QtPrivate::BindingStatusOrList::encodeBindingStatus(status);
}
