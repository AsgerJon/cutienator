//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectreplica_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtRemoteObjects/private/qremoteobjectcontainers_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/private/qremoteobjectnode_p.h>
#include <QtRemoteObjects/qremoteobjectregistry.h>
#include <QtRemoteObjects/qremoteobjectdynamicreplica.h>
#include <QtRemoteObjects/private/qremoteobjectpacket_p.h>
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectsource_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodelreplica_p.h>
#include <QtRemoteObjects/private/qremoteobjectabstractitemmodeladapter_p.h>
#include <QtCore/qabstractitemmodel.h>
#include <memory>
#include <algorithm>
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
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtRemoteObjects/private/qremoteobjectpendingcall_p.h>
#include <QtRemoteObjects/private/qremoteobjectreplica_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 247, as _ZN15QtRemoteObjects37getTypeNameAndMetaobjectFromClassInfoERPK11QMetaObject
inline QString QtRemoteObjects::getTypeNameAndMetaobjectFromClassInfo(const QMetaObject *& meta) {
    QString typeName;
    const int ind = meta->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE);
    if (ind != -1) { //We have an object created from repc or at least with QCLASSINFO defined
        typeName = QString::fromLatin1(meta->classInfo(ind).value());
        while (true) {
            Q_ASSERT(meta->superClass());//This recurses to QObject, which doesn't have QCLASSINFO_REMOTEOBJECT_TYPE
            //At the point superclass doesn't have the same QCLASSINFO_REMOTEOBJECT_TYPE,
            //we have the metaobject we should work from
            if (ind != meta->superClass()->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE))
                break;
            meta = meta->superClass();
        }
    }
    return typeName;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 505, as _ZN34QRemoteObjectReplicaImplementation16configurePrivateEP20QRemoteObjectReplica
inline void QRemoteObjectReplicaImplementation::configurePrivate(QRemoteObjectReplica *rep)
{
    qCDebug(QT_REMOTEOBJECT) << "configurePrivate starting for" << this->m_objectName;
    //We need to connect the Replicant only signals too
    // Uncomment the following two lines if QRemoteObjectDynamicReplica gets a unique staticMetaObject (FIX #3)
    //const QMetaObject *m =  rep->inherits("QRemoteObjectDynamicReplica") ?
    //            &QRemoteObjectDynamicReplica::staticMetaObject : &QRemoteObjectReplica::staticMetaObject;
    const QMetaObject *m = &QRemoteObjectReplica::staticMetaObject;
    for (int i = m->methodOffset(); i < m->methodCount(); ++i)
    {
        const QMetaMethod mm = m->method(i);
        if (mm.methodType() == QMetaMethod::Signal) {
            const bool res = QMetaObject::connect(this, i, rep, i, Qt::DirectConnection, nullptr);
            qCDebug(QT_REMOTEOBJECT) << "  Rep connect"<<i<<res<<mm.name();
            Q_UNUSED(res)
        }
    }
    if (m_methodOffset == 0) //We haven't initialized the offsets yet
    {
        const int index = m_metaObject->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE);
        const QMetaObject *metaObject = m_metaObject;
        if (index != -1) { //We have an object created from repc or at least with QCLASSINFO defined
            while (true) {
                Q_ASSERT(metaObject->superClass()); //This recurses to QObject, which doesn't have QCLASSINFO_REMOTEOBJECT_TYPE
                if (index != metaObject->superClass()->indexOfClassInfo(QCLASSINFO_REMOTEOBJECT_TYPE)) //At the point we don't find the same QCLASSINFO_REMOTEOBJECT_TYPE,
                                //we have the metaobject we should work from
                    break;
                metaObject = metaObject->superClass();
            }
        }

        for (int i = m_signalOffset; i < metaObject->methodCount(); ++i) {
            const QMetaMethod mm = metaObject->method(i);
            if (mm.methodType() == QMetaMethod::Signal) {
                ++m_numSignals;
                const bool res = QMetaObject::connect(this, i, rep, i, Qt::DirectConnection, nullptr);
                qCDebug(QT_REMOTEOBJECT) << "  Connect"<<i<<res<<mm.name();
                Q_UNUSED(res)
            }
        }
        m_methodOffset = m_signalOffset + m_numSignals;
        qCDebug(QT_REMOTEOBJECT) << QStringLiteral("configurePrivate finished, signalOffset = %1, methodOffset = %2, #Signals = %3").arg(m_signalOffset).arg(m_methodOffset).arg(m_numSignals);
    } else { //We have initialized offsets, this is an additional Replica attaching
        for (int i = m_signalOffset; i < m_methodOffset; ++i) {
            const bool res = QMetaObject::connect(this, i, rep, i, Qt::DirectConnection, nullptr);
            qCDebug(QT_REMOTEOBJECT) << "  Connect"<<i<<res<<m_metaObject->method(i).name();
            Q_UNUSED(res)
        }
        if (isInitialized()) {
            qCDebug(QT_REMOTEOBJECT) << QStringLiteral("ReplicaImplementation initialized, emitting signal on replica");
            emit rep->initialized(); //Emit from new replica only
        }
        if (state() != QRemoteObjectReplica::Valid) {
            qCDebug(QT_REMOTEOBJECT) << QStringLiteral("ReplicaImplementation not currently valid, emitting signal on replica");
            emit rep->stateChanged(state(), m_metaObject ? QRemoteObjectReplica::Default : QRemoteObjectReplica::Uninitialized);
        }

        qCDebug(QT_REMOTEOBJECT) << QStringLiteral("configurePrivate finished, added replica to existing ReplicaImplementation");
    }
}

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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 253, as _ZN34QRemoteObjectReplicaImplementation20setDynamicMetaObjectEPK11QMetaObject
inline void QRemoteObjectReplicaImplementation::setDynamicMetaObject(const QMetaObject *meta)
{
    Q_ASSERT(!m_metaObject);

    m_metaObject = meta;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 156, as _ZN34QRemoteObjectReplicaImplementation12emitNotifiedEv
inline void QRemoteObjectReplicaImplementation::emitNotified()
{
    const static int notifiedIndex = QRemoteObjectReplica::staticMetaObject.indexOfMethod("notified()");
    Q_ASSERT(notifiedIndex != -1);
    void *args[] = {nullptr};
    QMetaObject::activate(this, metaObject(), notifiedIndex, args);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 271, as _ZN34QRemoteObjectReplicaImplementation20setDynamicPropertiesEO5QListI8QVariantE
inline void QRemoteObjectReplicaImplementation::setDynamicProperties(QVariantList &&values)
{
    const int offset = m_propertyOffset;
    int propertyIndex = -1;
    for (auto &prop : values) {
        propertyIndex++;
        const QMetaProperty property = m_metaObject->property(propertyIndex+offset);
        prop = QRemoteObjectPackets::decodeVariant(std::move(prop), property.metaType());
    }
    //rely on order of properties;
    setProperties(std::move(values));
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 459, as _ZN31QConnectedReplicaImplementation13setPropertiesEO5QListI8QVariantE
inline void QConnectedReplicaImplementation::setProperties(QVariantList &&properties)
{
    Q_ASSERT(m_propertyStorage.isEmpty());
    m_propertyStorage.reserve(properties.size());
    m_propertyStorage = std::move(properties);
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 176, as _ZNK31QConnectedReplicaImplementation12childIndicesEv
inline QList<int> QConnectedReplicaImplementation::childIndices() const
{
    return m_childIndices;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 566, as _ZN31QConnectedReplicaImplementation16configurePrivateEP20QRemoteObjectReplica
inline void QConnectedReplicaImplementation::configurePrivate(QRemoteObjectReplica *rep)
{
    if (m_metaObject) {
        // see QRemoteObjectReplicaImplementation::configurePrivate
        const bool firstReplicaInstance = (m_methodOffset == 0);

        QRemoteObjectReplicaImplementation::configurePrivate(rep);

        // ensure that notify signals are emitted for the new replica, when
        // we are initializing an nth replica of the same type
        if (!firstReplicaInstance) {
            const int offset = m_propertyOffset;
            const int nParam = int(m_propertyStorage.size());
            void *args[] = {nullptr, nullptr};
            for (int i = 0; i < nParam; ++i) {
                const int notifyIndex = m_metaObject->property(i+offset).notifySignalIndex();
                if (notifyIndex < 0)
                    continue;
                qCDebug(QT_REMOTEOBJECT) << " Before activate" << notifyIndex << m_metaObject->property(i+offset).name();
                args[1] = m_propertyStorage[i].data();
                // NOTE: this over-emits (assumes all values have changed)
                QMetaObject::activate(rep, rep->metaObject(), notifyIndex - m_signalOffset, args);
            }
        }
    } else
        m_parentsNeedingConnect.append(rep);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 427, as _ZN31QConnectedReplicaImplementation15waitForFinishedERK24QRemoteObjectPendingCalli
inline bool QConnectedReplicaImplementation::waitForFinished(const QRemoteObjectPendingCall& call, int timeout)
{
    if (!call.d->watcherHelper)
        call.d->watcherHelper.reset(new QRemoteObjectPendingCallWatcherHelper);

    call.d->mutex.unlock();

    QEventLoop loop;
    loop.connect(call.d->watcherHelper.data(), &QRemoteObjectPendingCallWatcherHelper::finished,
                 &loop, &QEventLoop::quit);

    QTimer t; // NB: Related to QTBUG-94570 - don't use QTimer::singleShot here.
    if (timeout >= 0) {
        t.setSingleShot(true);
        connect(&t, &QTimer::timeout, &loop, &QEventLoop::quit);
        t.start(timeout);
    }

    // enter the event loop and wait for a reply
    loop.exec(QEventLoop::ExcludeUserInputEvents | QEventLoop::WaitForMoreEvents);

    call.d->mutex.lock();

    return call.d->error != QRemoteObjectPendingCall::InvalidMessage;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 406, as _ZN31QConnectedReplicaImplementation16notifyAboutReplyEiRK8QVariant
inline void QConnectedReplicaImplementation::notifyAboutReply(int ackedSerialId, const QVariant &value)
{
    QRemoteObjectPendingCall call = m_pendingCalls.take(ackedSerialId);
    if (ackedSerialId == 0) {
        m_heartbeatTimer.stop();
        if (m_heartbeatTimer.interval())
            m_heartbeatTimer.start();
        return;
    }

    QMutexLocker mutex(&call.d->mutex);

    // clear error flag
    call.d->error = QRemoteObjectPendingCall::NoError;
    call.d->returnValue = value;

    // notify watchers if needed
    if (call.d->watcherHelper)
        call.d->watcherHelper->emitSignals();
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

//  void QConnectedReplicaImplementation::setProperties(QVariantList &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QConnectedReplicaImplementation13setPropertiesEO5QListI8QVariantE(
    QConnectedReplicaImplementation *self,
    QVariantList *a0) {
  self->setProperties(std::move(*a0));
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

//  QList<int> QConnectedReplicaImplementation::childIndices() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK31QConnectedReplicaImplementation12childIndicesEv(
    const QConnectedReplicaImplementation *self) {
  return new QList<int>(self->childIndices());
}

//  void
//      QConnectedReplicaImplementation::configurePrivate(QRemoteObjectReplic
//      a *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QConnectedReplicaImplementation16configurePrivateEP20QRemoteObjectReplica(
    QConnectedReplicaImplementation *self,
    QRemoteObjectReplica *a0) {
  self->configurePrivate(a0);
}

//  bool QConnectedReplicaImplementation::waitForFinished(const
//      QRemoteObjectPendingCall &call, int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN31QConnectedReplicaImplementation15waitForFinishedERK24QRemoteObjectPendingCalli(
    QConnectedReplicaImplementation *self,
    const QRemoteObjectPendingCall *call,
    int timeout) {
  return self->waitForFinished(*call, timeout);
}

//  void QConnectedReplicaImplementation::notifyAboutReply(int ackedSerialId,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QConnectedReplicaImplementation16notifyAboutReplyEiRK8QVariant(
    QConnectedReplicaImplementation *self,
    int ackedSerialId,
    const QVariant *value) {
  self->notifyAboutReply(ackedSerialId, *value);
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

//  a QList<int> a ritual of QConnectedReplicaImplementation gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QConnectedReplicaImplementation__QList_int(
    QList<int> *self) {
  delete self;
}
