//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace QRemoteObjectStringLiterals;

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 264, as local:qremoteobjectnode.cpp:map_contains
inline template <typename K, typename V, typename Query>
bool map_contains(const QMap<K,V> &map, const Query &key, typename QMap<K,V>::const_iterator &result)
{
    const typename QMap<K,V>::const_iterator it = map.find(key);
    if (it == map.end())
        return false;
    result = it;
    return true;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 293, as _ZN24QRemoteObjectNodePrivateC2Ev
inline QRemoteObjectNodePrivate::QRemoteObjectNodePrivate()
    : QObjectPrivate()
    , registry(nullptr)
    , retryInterval(250)
    , lastError(QRemoteObjectNode::NoError)
    , persistedStore(nullptr)
{ }

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1527, as _ZN28QRemoteObjectHostBasePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString
inline QReplicaImplementationInterface *QRemoteObjectHostBasePrivate::handleNewAcquire(const QMetaObject *meta, QRemoteObjectReplica *instance, const QString &name)
{
    QMap<QString, QRemoteObjectSourceBase*>::const_iterator mapIt;
    if (remoteObjectIo && map_contains(remoteObjectIo->m_sourceObjects, name, mapIt)) {
        Q_Q(QRemoteObjectHostBase);
        QInProcessReplicaImplementation *rp = new QInProcessReplicaImplementation(name, meta, q);
        rp->configurePrivate(instance);
        connectReplica(mapIt.value()->m_object, instance);
        rp->connectionToSource = mapIt.value();
        return rp;
    }
    return QRemoteObjectNodePrivate::handleNewAcquire(meta, instance, name);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2823, as _ZN28QRemoteObjectHostBasePrivateD2Ev
inline QRemoteObjectHostBasePrivate::~QRemoteObjectHostBasePrivate()
{ }

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 305, as _ZNK24QRemoteObjectNodePrivate21remoteObjectAddressesEv
inline QRemoteObjectSourceLocations QRemoteObjectNodePrivate::remoteObjectAddresses() const
{
    if (registry)
        return registry->sourceLocations();
    return QRemoteObjectSourceLocations();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1287, as _ZN24QRemoteObjectNodePrivate14connectReplicaEP7QObjectP20QRemoteObjectReplica
inline void QRemoteObjectNodePrivate::connectReplica(QObject *object, QRemoteObjectReplica *instance)
{
    int nConnections = 0;
    const QMetaObject *us = instance->metaObject();
    const QMetaObject *them = object->metaObject();

    static const int memberOffset = QRemoteObjectReplica::staticMetaObject.methodCount();
    for (int idx = memberOffset; idx < us->methodCount(); ++idx) {
        const QMetaMethod mm = us->method(idx);

        qROPrivDebug() << idx << mm.name();
        if (mm.methodType() != QMetaMethod::Signal)
            continue;

        // try to connect to a signal on the parent that has the same method signature
        QByteArray sig = QMetaObject::normalizedSignature(mm.methodSignature().constData());
        qROPrivDebug() << sig;
        if (them->indexOfSignal(sig.constData()) == -1)
            continue;

        sig.prepend(QSIGNAL_CODE + '0');
        const char * const csig = sig.constData();
        const bool res = QObject::connect(object, csig, instance, csig);
        Q_UNUSED(res)
        ++nConnections;

        qROPrivDebug() << sig << res;
    }

    qROPrivDebug() << "# connections =" << nConnections;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1478, as _ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString
inline QReplicaImplementationInterface *QRemoteObjectNodePrivate::handleNewAcquire(const QMetaObject *meta, QRemoteObjectReplica *instance, const QString &name)
{
    Q_Q(QRemoteObjectNode);
    QConnectedReplicaImplementation *rp = new QConnectedReplicaImplementation(name, meta, q);
    rp->configurePrivate(instance);
    if (connectedSources.contains(name)) { //Either we have a peer connections, or existing connection via registry
        handleReplicaConnection(connectedSources[name].objectSignature, rp, connectedSources[name].device);
    } else {
        //No existing connection, but we know we can connect via registry
        const auto &sourceLocations = remoteObjectAddresses();
        const auto it = sourceLocations.constFind(name);
        // This will try the connection, and if successful, the remoteObjects will be sent
        // The link to the replica will be handled then
        if (it != sourceLocations.constEnd())
            initConnection(it.value().hostUrl);
    }
    return rp;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 301, as _ZN24QRemoteObjectNodePrivateD2Ev
inline QRemoteObjectNodePrivate::~QRemoteObjectNodePrivate()
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 842, as _ZN31QInProcessReplicaImplementationC1ERK7QStringPK11QMetaObjectP17QRemoteObjectNode
inline QInProcessReplicaImplementation::QInProcessReplicaImplementation(const QString &name, const QMetaObject *meta, QRemoteObjectNode * node)
    : QRemoteObjectReplicaImplementation(name, meta, node)
{
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

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1331, as _ZN24QRemoteObjectNodePrivate14initConnectionERK4QUrl
inline bool QRemoteObjectNodePrivate::initConnection(const QUrl &address)
{
    Q_Q(QRemoteObjectNode);
    if (requestedUrls.contains(address)) {
        qROPrivDebug() << "Connection already requested for " << address.toString();
        return true;
    }

    requestedUrls.insert(address);

    if (schemaHandlers.contains(address.scheme())) {
        schemaHandlers[address.scheme()](address);
        return true;
    }

    QtROClientIoDevice *connection = QtROClientFactory::instance()->create(address, q);
    if (!connection) {
        qROPrivWarning() << "Could not create QtROClientIoDevice for client. Invalid url/scheme provided?" << address;
        return false;
    }
    qROPrivDebug() << "Opening connection to" << address.toString();
    qROPrivDebug() << "Replica Connection isValid" << connection->isOpen();
    QObject::connect(connection, &QtROClientIoDevice::shouldReconnect, q, [this, connection]() {
        onShouldReconnect(connection);
    });
    QObject::connect(connection, &QtROIoDeviceBase::readyRead, q, [this, connection]() {
        onClientRead(connection);
    });
    connect(connection, &QtROClientIoDevice::setError, this,
            &QRemoteObjectNodePrivate::setLastError);
    connection->connectToServer();

    return true;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1515, as _ZN24QRemoteObjectNodePrivate23handleReplicaConnectionERK10QByteArrayP31QConnectedReplicaImplementationP16QtROIoDeviceBase
inline void QRemoteObjectNodePrivate::handleReplicaConnection(const QByteArray &sourceSignature, QConnectedReplicaImplementation *rep, QtROIoDeviceBase *connection)
{
    if (!checkSignatures(rep->m_objectSignature, sourceSignature)) {
        qROPrivWarning() << "Signature mismatch for" << rep->m_metaObject->className() << (rep->m_objectName.isEmpty() ? QLatin1String("(unnamed)") : rep->m_objectName);
        rep->setState(QRemoteObjectReplica::SignatureMismatch);
        return;
    }
    rep->setConnection(connection);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 771, as _ZN30QRemoteObjectMetaObjectManagerD1Ev
inline QRemoteObjectMetaObjectManager::~QRemoteObjectMetaObjectManager()
{
    for (QMetaObject *mo : std::as_const(dynamicTypes)) {
        for (auto metaType : std::as_const(enumTypes[mo]))
            QMetaType::unregisterMetaType(metaType);
        enumTypes.remove(mo);
        free(mo); //QMetaObjectBuilder uses malloc, not new
    }
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 59, as _ZN31QConnectedReplicaImplementationC1ERK7QStringPK11QMetaObjectP17QRemoteObjectNode
inline QConnectedReplicaImplementation::QConnectedReplicaImplementation(const QString &name, const QMetaObject *meta, QRemoteObjectNode *node)
    : QRemoteObjectReplicaImplementation(name, meta, node), connectionToSource(nullptr)
{
    m_heartbeatTimer.setTimerType(Qt::CoarseTimer);
    m_heartbeatTimer.setSingleShot(true);
    m_heartbeatTimer.setInterval(node->heartbeatInterval());

    connect(node, &QRemoteObjectNode::heartbeatIntervalChanged, this, [this](int interval) {
        m_heartbeatTimer.stop();
        m_heartbeatTimer.setInterval(interval);
        if (interval)
            m_heartbeatTimer.start();
    });
    connect(&m_heartbeatTimer, &QTimer::timeout, this, [this] {
        // TODO: Revisit if a baseclass method can be used to avoid specialized cast
        // conditional logic.

        if (m_pendingCalls.contains(0)) {
            m_pendingCalls.take(0);
            // The source didn't respond in time, disconnect the connection
            if (connectionToSource) {
                auto clientIo = qobject_cast<QtROClientIoDevice *>(connectionToSource);
                if (clientIo)
                    clientIo->disconnectFromServer();
                else
                    connectionToSource->close();
            }
        } else {
            if (connectionToSource.isNull()) {
                qCDebug(QT_REMOTEOBJECT) << "Ignoring heartbeat as there is no source connected.";
                return;
            }
            connectionToSource->d_func()->m_codec->serializePingPacket(m_objectName);
            if (sendCommandWithReply(0).d->serialId == -1) {
                m_heartbeatTimer.stop();
                auto clientIo = qobject_cast<QtROClientIoDevice *>(connectionToSource);
                if (clientIo)
                    clientIo->disconnectFromServer();
                else
                    connectionToSource->close();
            }
        }
    });

    if (!meta)
        return;

    auto offsetMeta = m_metaObject;
    QtRemoteObjects::getTypeNameAndMetaobjectFromClassInfo(offsetMeta);
    for (int index = offsetMeta->propertyOffset(); index < offsetMeta->propertyCount(); ++index) {
        const QMetaProperty property = offsetMeta->property(index);
        if (property.metaType().flags().testFlag(QMetaType::PointerToQObject))
            m_childIndices << index - offsetMeta->propertyOffset();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 42, as _ZN34QRemoteObjectReplicaImplementationC2ERK7QStringPK11QMetaObjectP17QRemoteObjectNode
inline QRemoteObjectReplicaImplementation::QRemoteObjectReplicaImplementation(const QString &name, const QMetaObject *meta, QRemoteObjectNode *_node)
    : QObject(nullptr), m_objectName(name), m_metaObject(meta), m_numSignals(0), m_methodOffset(0)
    // Uncomment the following two lines if QRemoteObjectDynamicReplica gets a unique staticMetaObject (FIX #1, #2)
    //, m_signalOffset(meta ? QRemoteObjectReplica::staticMetaObject.methodCount() : QRemoteObjectDynamicReplica::staticMetaObject.methodCount())
    //, m_propertyOffset(meta ? QRemoteObjectReplica::staticMetaObject.propertyCount() : QRemoteObjectDynamicReplica::staticMetaObject.propertyCount())
    , m_signalOffset(QRemoteObjectReplica::staticMetaObject.methodCount())
    , m_propertyOffset(QRemoteObjectReplica::staticMetaObject.propertyCount())
    , m_node(_node)
    , m_objectSignature(QtPrivate::qtro_classinfo_signature(m_metaObject))
    , m_state(meta ? QRemoteObjectReplica::Default : QRemoteObjectReplica::Uninitialized)
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 847, as _ZN31QInProcessReplicaImplementationD1Ev
inline QInProcessReplicaImplementation::~QInProcessReplicaImplementation()
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 851, as _ZNK31QInProcessReplicaImplementation11getPropertyEi
inline const QVariant QInProcessReplicaImplementation::getProperty(int i) const
{
    Q_ASSERT(connectionToSource);
    Q_ASSERT(connectionToSource->m_object);
    const int index = i + QRemoteObjectSource::qobjectPropertyOffset;
    Q_ASSERT(index >= 0 && index < connectionToSource->m_object->metaObject()->propertyCount());
    return connectionToSource->m_object->metaObject()->property(index).read(connectionToSource->m_object);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 860, as _ZN31QInProcessReplicaImplementation13setPropertiesEO5QListI8QVariantE
inline void QInProcessReplicaImplementation::setProperties(QVariantList &&)
{
    //TODO some verification here maybe?
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 865, as _ZN31QInProcessReplicaImplementation11setPropertyEiRK8QVariant
inline void QInProcessReplicaImplementation::setProperty(int i, const QVariant &property)
{
    Q_ASSERT(connectionToSource);
    Q_ASSERT(connectionToSource->m_object);
    const int index = i + QRemoteObjectSource::qobjectPropertyOffset;
    Q_ASSERT(index >= 0 && index < connectionToSource->m_object->metaObject()->propertyCount());
    connectionToSource->m_object->metaObject()->property(index).write(connectionToSource->m_object, property);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 874, as _ZN31QInProcessReplicaImplementation7_q_sendEN11QMetaObject4CallEiRK5QListI8QVariantE
inline void QInProcessReplicaImplementation::_q_send(QMetaObject::Call call, int index, const QVariantList &args)
{
    Q_ASSERT(call == QMetaObject::InvokeMetaMethod || call == QMetaObject::WriteProperty);

    const SourceApiMap *api = connectionToSource->m_api;
    if (call == QMetaObject::InvokeMetaMethod) {
        const int resolvedIndex = api->sourceMethodIndex(index - m_methodOffset);
        if (resolvedIndex < 0)
            qCWarning(QT_REMOTEOBJECT) << "Skipping invalid invocation.  Index not found:" << index - m_methodOffset;
        else
            connectionToSource->invoke(call, index - m_methodOffset, args);
    } else {
        const int resolvedIndex = connectionToSource->m_api->sourcePropertyIndex(index - m_propertyOffset);
        if (resolvedIndex < 0)
            qCWarning(QT_REMOTEOBJECT) << "Skipping invalid property setter.  Index not found:" << index - m_propertyOffset;
        else
            connectionToSource->invoke(call, index - m_propertyOffset, args);
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 894, as _ZN31QInProcessReplicaImplementation16_q_sendWithReplyEN11QMetaObject4CallEiRK5QListI8QVariantE
inline QRemoteObjectPendingCall QInProcessReplicaImplementation::_q_sendWithReply(QMetaObject::Call call, int index, const QVariantList &args)
{
    Q_ASSERT(call == QMetaObject::InvokeMetaMethod);

    const int ReplicaIndex = index - m_methodOffset;
    auto metaType = QMetaType::fromName(connectionToSource->m_api->typeName(ReplicaIndex).constData());
    if (!metaType.sizeOf())
        metaType = QMetaType(QMetaType::UnknownType);
    QVariant returnValue(metaType, nullptr);

    const int resolvedIndex = connectionToSource->m_api->sourceMethodIndex(ReplicaIndex);
    if (resolvedIndex < 0) {
        qCWarning(QT_REMOTEOBJECT) << "Skipping invalid invocation.  Index not found:" << ReplicaIndex;
        return QRemoteObjectPendingCall();
    }

    connectionToSource->invoke(call, ReplicaIndex, args, &returnValue);
    return QRemoteObjectPendingCall::fromCompletedCall(returnValue);
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
//  -----------------------------------------------------------------------

//  A QRemoteObjectHostBasePrivate that Python can take functions over in. Every QRemoteObjectHostBasePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRemoteObjectHostBasePrivateCall0)(const void *, const QMetaObject *, QRemoteObjectReplica *, const QString *, int *);
class CuteQRemoteObjectHostBasePrivate : public QRemoteObjectHostBasePrivate {
public:
  using QRemoteObjectHostBasePrivate::QRemoteObjectHostBasePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QReplicaImplementationInterface
  //      *QRemoteObjectHostBasePrivate::handleNewAcquire(const QMetaObject
  //      *meta, QRemoteObjectReplica *instance, const QString &name)
  QReplicaImplementationInterface *handleNewAcquire(
      const QMetaObject *meta,
      QRemoteObjectReplica *instance,
      const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectHostBasePrivateCall0 call = reinterpret_cast<CuteQRemoteObjectHostBasePrivateCall0>(taken[0]);
      void * given = call(this, meta, instance, &name, &handled);
      if (handled) return static_cast<QReplicaImplementationInterface *>(given);
    }
    return QRemoteObjectHostBasePrivate::handleNewAcquire(meta, instance, name);
  }
};

//  QRemoteObjectHostBasePrivate::~QRemoteObjectHostBasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QRemoteObjectHostBasePrivateD1Ev(
    QRemoteObjectHostBasePrivate *self) {
  delete self;
}

//  QReplicaImplementationInterface
//      *QRemoteObjectHostBasePrivate::handleNewAcquire(const QMetaObject
//      *meta, QRemoteObjectReplica *instance, const QString &name)
extern "C" Q_DECL_EXPORT
QReplicaImplementationInterface *ritual_ZN28QRemoteObjectHostBasePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString(
    QRemoteObjectHostBasePrivate *self,
    const QMetaObject *meta,
    QRemoteObjectReplica *instance,
    const QString *name) {
  return self->handleNewAcquire(meta, instance, *name);
}

//  QRemoteObjectHostBase *QRemoteObjectHostBasePrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectHostBase *ritual_ZN28QRemoteObjectHostBasePrivate6q_funcEv(
    QRemoteObjectHostBasePrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectHostBase *QRemoteObjectHostBasePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectHostBase *ritual_ZNK28QRemoteObjectHostBasePrivate6q_funcEv(
    const QRemoteObjectHostBasePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQRemoteObjectHostBasePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectHostBasePrivate(
    QRemoteObjectHostBasePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectHostBasePrivate *>(self)->take(key, call);
}
