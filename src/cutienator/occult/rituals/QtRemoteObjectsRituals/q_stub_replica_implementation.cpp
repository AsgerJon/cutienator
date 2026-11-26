//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectreplica.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#include <QtRemoteObjects/private/qconnectionfactories_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qvariant.h>
#include <QtCore/qthread.h>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 914, as _ZN26QStubReplicaImplementationC1Ev
inline QStubReplicaImplementation::QStubReplicaImplementation() {}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 916, as _ZN26QStubReplicaImplementationD1Ev
inline QStubReplicaImplementation::~QStubReplicaImplementation() {}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 918, as _ZNK26QStubReplicaImplementation11getPropertyEi
inline const QVariant QStubReplicaImplementation::getProperty(int i) const
{
    Q_ASSERT_X(i >= 0 && i < m_propertyStorage.size(), __FUNCTION__, qPrintable(QString(QLatin1String("0 <= %1 < %2")).arg(i).arg(m_propertyStorage.size())));
    return m_propertyStorage[i];
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 924, as _ZN26QStubReplicaImplementation13setPropertiesEO5QListI8QVariantE
inline void QStubReplicaImplementation::setProperties(QVariantList &&properties)
{
    Q_ASSERT(m_propertyStorage.isEmpty());
    m_propertyStorage.reserve(properties.size());
    m_propertyStorage = std::move(properties);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 931, as _ZN26QStubReplicaImplementation11setPropertyEiRK8QVariant
inline void QStubReplicaImplementation::setProperty(int i, const QVariant &prop)
{
    m_propertyStorage[i] = prop;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 936, as _ZN26QStubReplicaImplementation7_q_sendEN11QMetaObject4CallEiRK5QListI8QVariantE
inline void QStubReplicaImplementation::_q_send(QMetaObject::Call call, int index, const QVariantList &args)
{
    Q_UNUSED(call)
    Q_UNUSED(index)
    Q_UNUSED(args)
    qWarning("Tried calling a slot or setting a property on a replica that hasn't been initialized with a node");
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 944, as _ZN26QStubReplicaImplementation16_q_sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE
inline QRemoteObjectPendingCall QStubReplicaImplementation::_q_sendWithReply(QMetaObject::Call call, int index, const QVariantList &args)
{
    Q_UNUSED(call)
    Q_UNUSED(index)
    Q_UNUSED(args)
    qWarning("Tried calling a slot or setting a property on a replica that hasn't been initialized with a node");
    return QRemoteObjectPendingCall(); //Invalid
}
//  -----------------------------------------------------------------------

//  QStubReplicaImplementation::QStubReplicaImplementation()
extern "C" Q_DECL_EXPORT
QStubReplicaImplementation *ritual_ZN26QStubReplicaImplementationC1Ev() {
  return new QStubReplicaImplementation();
}

//  QStubReplicaImplementation::~QStubReplicaImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStubReplicaImplementationD1Ev(
    QStubReplicaImplementation *self) {
  delete self;
}

//  const QVariant QStubReplicaImplementation::getProperty(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QStubReplicaImplementation11getPropertyEi(
    const QStubReplicaImplementation *self,
    int i) {
  return new QVariant(self->getProperty(i));
}

//  void QStubReplicaImplementation::setProperties(QVariantList &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStubReplicaImplementation13setPropertiesEO5QListI8QVariantE(
    QStubReplicaImplementation *self,
    QVariantList *a0) {
  self->setProperties(std::move(*a0));
}

//  void QStubReplicaImplementation::setProperty(int i, const QVariant &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStubReplicaImplementation11setPropertyEiRK8QVariant(
    QStubReplicaImplementation *self,
    int i,
    const QVariant *a1) {
  self->setProperty(i, *a1);
}

//  bool QStubReplicaImplementation::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QStubReplicaImplementation13isInitializedEv(
    const QStubReplicaImplementation *self) {
  return self->isInitialized();
}

//  QRemoteObjectReplica::State QStubReplicaImplementation::state() const
extern "C" Q_DECL_EXPORT
QRemoteObjectReplica::State ritual_ZNK26QStubReplicaImplementation5stateEv(
    const QStubReplicaImplementation *self) {
  return self->state();
}

//  bool QStubReplicaImplementation::waitForSource(int a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QStubReplicaImplementation13waitForSourceEi(
    QStubReplicaImplementation *self,
    int a0) {
  return self->waitForSource(a0);
}

//  QRemoteObjectNode *QStubReplicaImplementation::node() const
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZNK26QStubReplicaImplementation4nodeEv(
    const QStubReplicaImplementation *self) {
  return self->node();
}

//  void QStubReplicaImplementation::_q_send(QMetaObject::Call call, int
//      index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QStubReplicaImplementation7_q_sendEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QStubReplicaImplementation *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  self->_q_send(call, index, *args);
}

//  QRemoteObjectPendingCall
//      QStubReplicaImplementation::_q_sendWithReply(QMetaObject::Call call,
//      int index, const QVariantList &args)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_ZN26QStubReplicaImplementation16_q_sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE(
    QStubReplicaImplementation *self,
    QMetaObject::Call call,
    int index,
    const QList<QVariant> *args) {
  return new QRemoteObjectPendingCall(
      self->_q_sendWithReply(
          call,
          index,
          *args));
}
