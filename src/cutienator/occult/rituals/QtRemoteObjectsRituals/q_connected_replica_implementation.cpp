//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qobject_p.h>
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectpendingcall.cpp, line 37, as _ZN37QRemoteObjectPendingCallWatcherHelper11emitSignalsEv
inline void QRemoteObjectPendingCallWatcherHelper::emitSignals()
{
    emit finished();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 135, as _ZN34QRemoteObjectReplicaImplementation8setStateEN20QRemoteObjectReplica5StateE
inline void QRemoteObjectReplicaImplementation::setState(QRemoteObjectReplica::State state)
{
    if (m_state.loadAcquire() != QRemoteObjectReplica::Suspect && m_state.loadAcquire() >= state)
        return;

    int oldState = m_state.loadAcquire();
    m_state.storeRelease(state);

    // We should emit initialized before emitting any changed signals in case connections are made in a
    // Slot responding to initialized/validChanged.
    if (m_state.loadAcquire() == QRemoteObjectReplica::Valid) {
        // we're initialized now, emit signal
        emitInitialized();
    }

    const static int stateChangedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("stateChanged(State,State)");
    Q_ASSERT(stateChangedIndex != -1);
    void *args[] = {nullptr, &state, &oldState};
    QMetaObject::activate(this, metaObject(), stateChangedIndex, args);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 176, as _ZNK31QConnectedReplicaImplementation12childIndicesEv
inline QList<int> QConnectedReplicaImplementation::childIndices() const
{
    return m_childIndices;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 253, as _ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject
inline void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const QMetaObject *meta)
{
    Q_ASSERT(!m_metaObject);

    m_metaObject = meta;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 221, as _ZN34QRemoteObjectReplicaImplementation15emitInitializedEv
inline void QRemoteObjectReplicaImplementation::emitInitialized()
{
    const static int initializedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("initialized()");
    Q_ASSERT(initializedIndex != -1);
    void *noArgs[] = {nullptr};
    QMetaObject::activate(this, metaObject(), initializedIndex, noArgs);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 453, as _ZNK31QConnectedReplicaImplementation11getPropertyEi
inline const QVariant QConnectedReplicaImplementation::getProperty(int i) const
{
    Q_ASSERT_X(i >= 0 && i < m_propertyStorage.size(), __FUNCTION__, qPrintable(QString(QLatin1String("0 <= %1 < %2")).arg(i).arg(m_propertyStorage.size())));
    return m_propertyStorage[i];
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 466, as _ZN31QConnectedReplicaImplementation11setPropertyEiRK8QVariant
inline void QConnectedReplicaImplementation::setProperty(int i, const QVariant &prop)
{
    m_propertyStorage[i] = prop;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 308, as _ZNK31QConnectedReplicaImplementation13isInitializedEv
inline bool QConnectedReplicaImplementation::isInitialized() const
{
    return  m_state.loadAcquire() > QRemoteObjectReplica::Default && m_state.loadAcquire() != QRemoteObjectReplica::SignatureMismatch;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 313, as _ZN31QConnectedReplicaImplementation13waitForSourceEi
inline bool QConnectedReplicaImplementation::waitForSource(int timeout)
{
    switch (state()) {
    case QRemoteObjectReplica::State::Valid:
        return true;
    case QRemoteObjectReplica::State::SignatureMismatch:
        return false;
    default:
        break;
    }

    const static int stateChangedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("stateChanged(State,State)");
    Q_ASSERT(stateChangedIndex != -1);

    QEventLoop loop;
    QMetaObject::connect(this, stateChangedIndex,
                         &loop, QEventLoop::staticMetaObject.indexOfMethod("quit()"),
                         Qt::DirectConnection, nullptr);

    QTimer t; // NB: Related to QTBUG-94570 - don't use QTimer::singleShot here.
    if (timeout >= 0) {
        t.setSingleShot(true);
        connect(&t, &QTimer::timeout, &loop, &QEventLoop::quit);
        t.start(timeout);
    }

    // enter the event loop and wait for a reply
    loop.exec(QEventLoop::ExcludeUserInputEvents | QEventLoop::WaitForMoreEvents);

    return state() == QRemoteObjectReplica::State::Valid;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 480, as _ZN31QConnectedReplicaImplementation15setDisconnectedEv
inline void QConnectedReplicaImplementation::setDisconnected()
{
    Q_ASSERT(connectionToSource);
    connectionToSource.clear();
    setState(QRemoteObjectReplica::State::Suspect);
    const auto childIds = childIndices();
    for (const int index : childIds) {
        auto pointerToQObject = qvariant_cast<QObject *>(getProperty(index));
        auto child = qobject_cast<QRemoteObjectReplica *>(pointerToQObject);
        if (child) {
            QConnectedReplicaImplementation *childReplicaImplData
                    = static_cast<QConnectedReplicaImplementation *>(child->d_impl.data());
            if (childReplicaImplData && !childReplicaImplData->connectionToSource.isNull())
                childReplicaImplData->setDisconnected();
        }
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 260, as _ZN31QConnectedReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject
inline void QConnectedReplicaImplementation::setDynamicMetaObject(const QMetaObject *meta)
{
    QRemoteObjectReplicaImplementation::setDynamicMetaObject(meta);

    for (int index = m_metaObject->propertyOffset(); index < m_metaObject->propertyCount(); ++index) {
        const QMetaProperty property = m_metaObject->property(index);
        if (property.metaType().flags().testFlag(QMetaType::PointerToQObject))
            m_childIndices << index - m_metaObject->propertyOffset();
    }
}
//  -----------------------------------------------------------------------

//  const QVariant QConnectedReplicaImplementation::getProperty(int i) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK31QConnectedReplicaImplementation11getPropertyEi(
    const QConnectedReplicaImplementation *self,
    int i) {
  return new QVariant(self->getProperty(i));
}

//  void QConnectedReplicaImplementation::setProperty(int i, const QVariant
//      &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QConnectedReplicaImplementation11setPropertyEiRK8QVariant(
    QConnectedReplicaImplementation *self,
    int i,
    const QVariant *a1) {
  self->setProperty(i, *a1);
}

//  bool QConnectedReplicaImplementation::isShortCircuit() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QConnectedReplicaImplementation14isShortCircuitEv(
    const QConnectedReplicaImplementation *self) {
  return self->isShortCircuit();
}

//  bool QConnectedReplicaImplementation::isInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QConnectedReplicaImplementation13isInitializedEv(
    const QConnectedReplicaImplementation *self) {
  return self->isInitialized();
}

//  bool QConnectedReplicaImplementation::waitForSource(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QConnectedReplicaImplementation13waitForSourceEi(
    QConnectedReplicaImplementation *self,
    int timeout) {
  return self->waitForSource(timeout);
}

//  void QConnectedReplicaImplementation::setDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QConnectedReplicaImplementation15setDisconnectedEv(
    QConnectedReplicaImplementation *self) {
  self->setDisconnected();
}

//  void QConnectedReplicaImplementation::setDynamicMetaObject(const
//      QMetaObject *meta)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QConnectedReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject(
    QConnectedReplicaImplementation *self,
    const QMetaObject *meta) {
  self->setDynamicMetaObject(meta);
}
