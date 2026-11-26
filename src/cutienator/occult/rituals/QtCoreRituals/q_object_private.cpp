//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qobject.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qobjectdefs.h>
#include <QtCore/qlist.h>
#include <string>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtconfigmacros.h>
#include <QtCore/qobject.h>
#include <QtCore/private/qobject_p.h>
#include <QtCore/private/qobject_p_p.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qtclasshelper_p.h>
#include <QtCore/qspan.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/private/qabstracteventdispatcher_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qcoreevent_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#if QT_CONFIG(regularexpression)
#  include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qset.h>
#if QT_CONFIG(thread)
#include <QtCore/private/qlatch_p.h>
#endif
#include <QtCore/private/qorderedmutexlocker_p.h>
#include <QtCore/private/qhooks_p.h>
#include <new>
#include <mutex>
#include <memory>
#include <optional>
#include <iterator>
#include <ctype.h>
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qobject.cpp, line 266, as _ZN14QObjectPrivate20ensureConnectionDataEv
inline void QObjectPrivate::ensureConnectionData()
{
    if (connections.loadRelaxed())
        return;
    ConnectionData *cd = new ConnectionData;
    cd->ref.ref();
    connections.storeRelease(cd);
}

//  from src/corelib/kernel/qobject.cpp, line 285, as _ZN14QObjectPrivate13addConnectionEiPNS_10ConnectionE
inline void QObjectPrivate::addConnection(int signal, Connection *c)
{
    Q_ASSERT(c->sender == q_ptr);
    ensureConnectionData();
    ConnectionData *cd = connections.loadRelaxed();
    cd->resizeSignalVector(signal + 1);

    ConnectionList &connectionList = cd->connectionsForSignal(signal);
    Connection *lastConnection = connectionList.last.loadRelaxed();
    if (lastConnection) {
        Q_ASSERT(lastConnection->receiver.loadRelaxed());
        lastConnection->nextConnectionList.storeRelease(c);
    } else {
        connectionList.first.storeRelease(c);
    }
    c->id.storeRelease(++cd->currentConnectionId);
    c->prevConnectionList = lastConnection;
    connectionList.last.storeRelaxed(c);

    QObjectPrivate *rd = QObjectPrivate::get(c->receiver.loadRelaxed());
    rd->ensureConnectionData();

    c->prev = &(rd->connections.loadRelaxed()->senders);
    c->next = *c->prev;
    *c->prev = c;
    if (c->next)
        c->next->prev = &c->next;
}
//  -----------------------------------------------------------------------

//  QObject *QObjectPrivate::q_func()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN14QObjectPrivate6q_funcEv(QObjectPrivate *self) {
  return self->q_func();
}

//  const QObject *QObjectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QObject *ritual_ZNK14QObjectPrivate6q_funcEv(
    const QObjectPrivate *self) {
  return self->q_func();
}

//  void QObjectPrivate::ensureExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate15ensureExtraDataEv(QObjectPrivate *self) {
  self->ensureExtraData();
}

//  void QObjectPrivate::setObjectNameWithoutBindings(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate28setObjectNameWithoutBindingsERK7QString(
    QObjectPrivate *self,
    const QString *name) {
  self->setObjectNameWithoutBindings(*name);
}

//  QObjectPrivate::QObjectPrivate(decltype(QObjectPrivateVersion) version)
extern "C" Q_DECL_EXPORT
QObjectPrivate *ritual_ZN14QObjectPrivateC1E16QtPrivate_6_12_0(
    decltype(QObjectPrivateVersion) version) {
  return new QObjectPrivate(version);
}

//  QObjectPrivate::~QObjectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivateD1Ev(QObjectPrivate *self) {
  delete self;
}

//  void QObjectPrivate::deleteChildren()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate14deleteChildrenEv(QObjectPrivate *self) {
  self->deleteChildren();
}

//  void QObjectPrivate::clearBindingStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate19clearBindingStorageEv(QObjectPrivate *self) {
  self->clearBindingStorage();
}

//  void QObjectPrivate::setParent_helper(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate16setParent_helperEP7QObject(
    QObjectPrivate *self,
    QObject *a0) {
  self->setParent_helper(a0);
}

//  void QObjectPrivate::moveToThread_helper()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate19moveToThread_helperEv(QObjectPrivate *self) {
  self->moveToThread_helper();
}

//  void QObjectPrivate::setThreadData_helper(QThreadData *currentData,
//      QThreadData *targetData, QBindingStatus *status)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate20setThreadData_helperEP11QThreadDataS1_P14QBindingStatus(
    QObjectPrivate *self,
    QThreadData *currentData,
    QThreadData *targetData,
    QBindingStatus *status) {
  self->setThreadData_helper(currentData, targetData, status);
}

//  QObjectList QObjectPrivate::receiverList(const char *signal) const
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZNK14QObjectPrivate12receiverListEPKc(
    const QObjectPrivate *self,
    const char *signal) {
  return new QList<QObject *>(self->receiverList(signal));
}

//  void QObjectPrivate::ensureConnectionData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate20ensureConnectionDataEv(
    QObjectPrivate *self) {
  self->ensureConnectionData();
}

//  void QObjectPrivate::addConnection(int signal, Connection *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate13addConnectionEiPNS_10ConnectionE(
    QObjectPrivate *self,
    int signal,
    QObjectPrivate::Connection *c) {
  self->addConnection(signal, c);
}

//  QObjectPrivate *QObjectPrivate::get(QObject *o)
extern "C" Q_DECL_EXPORT
QObjectPrivate *ritual_ZN14QObjectPrivate3getEP7QObject(QObject *o) {
  return QObjectPrivate::get(o);
}

//  const QObjectPrivate *QObjectPrivate::get(const QObject *o)
extern "C" Q_DECL_EXPORT
const QObjectPrivate *ritual_ZN14QObjectPrivate3getEPK7QObject(
    const QObject *o) {
  return QObjectPrivate::get(o);
}

//  void QObjectPrivate::deleteInOwnThread(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate17deleteInOwnThreadEP7QObject(
    QObject *object) {
  QObjectPrivate::deleteInOwnThread(object);
}

//  int QObjectPrivate::signalIndex(const char *signalName, const QMetaObject
//      **meta) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QObjectPrivate11signalIndexEPKcPPK11QMetaObject(
    const QObjectPrivate *self,
    const char *signalName,
    const QMetaObject **meta) {
  return self->signalIndex(signalName, meta);
}

//  bool QObjectPrivate::isSignalConnected(uint signalIdx, bool
//      checkDeclarative) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QObjectPrivate17isSignalConnectedEjb(
    const QObjectPrivate *self,
    uint signalIdx,
    bool checkDeclarative) {
  return self->isSignalConnected(signalIdx, checkDeclarative);
}

//  bool QObjectPrivate::maybeSignalConnected(uint signalIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QObjectPrivate20maybeSignalConnectedEj(
    const QObjectPrivate *self,
    uint signalIndex) {
  return self->maybeSignalConnected(signalIndex);
}

//  bool QObjectPrivate::isDeclarativeSignalConnected(uint signalIdx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QObjectPrivate28isDeclarativeSignalConnectedEj(
    const QObjectPrivate *self,
    uint signalIdx) {
  return self->isDeclarativeSignalConnected(signalIdx);
}

//  void QObjectPrivate::connectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate13connectNotifyERK11QMetaMethod(
    QObjectPrivate *self,
    const QMetaMethod *signal) {
  self->connectNotify(*signal);
}

//  void QObjectPrivate::disconnectNotify(const QMetaMethod &signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate16disconnectNotifyERK11QMetaMethod(
    QObjectPrivate *self,
    const QMetaMethod *signal) {
  self->disconnectNotify(*signal);
}

//  void QObjectPrivate::reinitBindingStorageAfterThreadMove()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QObjectPrivate35reinitBindingStorageAfterThreadMoveEv(
    QObjectPrivate *self) {
  self->reinitBindingStorageAfterThreadMove();
}

//  QMetaObject::Connection QObjectPrivate::connectImpl(const QObject
//      *sender, int signal_index, const QObject *receiver, void **slot,
//      QtPrivate::QSlotObjectBase *slotObj, int type, const int *types,
//      const QMetaObject *senderMetaObject)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN14QObjectPrivate11connectImplEPK7QObjectiS2_PPvPN9QtPrivate15QSlotObjectBaseEiPKiPK11QMetaObject(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    void **slot,
    QtPrivate::QSlotObjectBase *slotObj,
    int type,
    const int *types,
    const QMetaObject *senderMetaObject) {
  return new QMetaObject::Connection(
      QObjectPrivate::connectImpl(
          sender,
          signal_index,
          receiver,
          slot,
          slotObj,
          type,
          types,
          senderMetaObject));
}

//  QMetaObject::Connection QObjectPrivate::connect(const QObject *sender,
//      int signal_index, QtPrivate::QSlotObjectBase *slotObj,
//      Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN14QObjectPrivate7connectEPK7QObjectiPN9QtPrivate15QSlotObjectBaseEN2Qt14ConnectionTypeE(
    const QObject *sender,
    int signal_index,
    QtPrivate::QSlotObjectBase *slotObj,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      QObjectPrivate::connect(
          sender,
          signal_index,
          slotObj,
          type));
}

//  QMetaObject::Connection QObjectPrivate::connect(const QObject *sender,
//      int signal_index, const QObject *receiver, QtPrivate::QSlotObjectBase
//      *slotObj, Qt::ConnectionType type)
extern "C" Q_DECL_EXPORT
QMetaObject::Connection *ritual_ZN14QObjectPrivate7connectEPK7QObjectiS2_PN9QtPrivate15QSlotObjectBaseEN2Qt14ConnectionTypeE(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    QtPrivate::QSlotObjectBase *slotObj,
    Qt::ConnectionType type) {
  return new QMetaObject::Connection(
      QObjectPrivate::connect(
          sender,
          signal_index,
          receiver,
          slotObj,
          type));
}

//  bool QObjectPrivate::disconnect(const QObject *sender, int signal_index,
//      void **slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QObjectPrivate10disconnectEPK7QObjectiPPv(
    const QObject *sender,
    int signal_index,
    void **slot) {
  return QObjectPrivate::disconnect(sender, signal_index, slot);
}

//  bool QObjectPrivate::disconnect(const QObject *sender, int signal_index,
//      const QObject *receiver, void **slot)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QObjectPrivate10disconnectEPK7QObjectiS2_PPv(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    void **slot) {
  return QObjectPrivate::disconnect(sender, signal_index, receiver, slot);
}

//  std::string QObjectPrivate::flagsForDumping() const
extern "C" Q_DECL_EXPORT
std::string *ritual_ZNK14QObjectPrivate15flagsForDumpingB5cxx11Ev(
    const QObjectPrivate *self) {
  return new std::string(self->flagsForDumping());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  void QObjectPrivate::writeToDebugStream(QDebug &a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QObjectPrivate18writeToDebugStreamER6QDebug(
    const QObjectPrivate *self,
    QDebug *a0) {
  self->writeToDebugStream(*a0);
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QtPrivate::QPropertyAdaptorSlotObject
//      *QObjectPrivate::getPropertyAdaptorSlotObject(const QMetaProperty
//      &property)
extern "C" Q_DECL_EXPORT
QtPrivate::QPropertyAdaptorSlotObject *ritual_ZN14QObjectPrivate28getPropertyAdaptorSlotObjectERK13QMetaProperty(
    QObjectPrivate *self,
    const QMetaProperty *property) {
  return self->getPropertyAdaptorSlotObject(*property);
}

//  a std::string a ritual of QObjectPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QObjectPrivate__std_string(std::string *self) {
  delete self;
}
