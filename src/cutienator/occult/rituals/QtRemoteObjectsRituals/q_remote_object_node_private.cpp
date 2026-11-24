//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "private/qmetaobjectbuilder_p.h"
#include "qremoteobjectcontainers_p.h"
#include "qremoteobjectnode.h"
#include "qremoteobjectnode_p.h"
#include "qremoteobjectregistry.h"
#include "qremoteobjectdynamicreplica.h"
#include "qremoteobjectpacket_p.h"
#include "qremoteobjectregistrysource_p.h"
#include "qremoteobjectreplica_p.h"
#include "qremoteobjectsource_p.h"
#include "qremoteobjectabstractitemmodelreplica_p.h"
#include "qremoteobjectabstractitemmodeladapter_p.h"
#include <QtCore/qabstractitemmodel.h>
#include <memory>
#include <algorithm>
#include "qremoteobjectreplica.h"
#include "qremoteobjectreplica_p.h"
#include "qremoteobjectnode.h"
#include "qremoteobjectnode_p.h"
#include "qremoteobjectdynamicreplica.h"
#include "qremoteobjectpacket_p.h"
#include "qremoteobjectpendingcall_p.h"
#include "qconnectionfactories_p.h"
#include "qremoteobjectsource_p.h"
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 301, as _ZN24QRemoteObjectNodePrivateD1Ev
inline QRemoteObjectNodePrivate::~QRemoteObjectNodePrivate()
{
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 619, as _ZN24QRemoteObjectNodePrivate12setLastErrorEN17QRemoteObjectNode9ErrorCodeE
inline void QRemoteObjectNodePrivate::setLastError(QRemoteObjectNode::ErrorCode errorCode)
{
    Q_Q(QRemoteObjectNode);
    lastError = errorCode;
    emit q->error(lastError);
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1366, as _ZN24QRemoteObjectNodePrivate11hasInstanceERK7QString
inline bool QRemoteObjectNodePrivate::hasInstance(const QString &name)
{
    if (!replicas.contains(name))
        return false;

    QSharedPointer<QReplicaImplementationInterface> rep = replicas.value(name).toStrongRef();
    if (!rep) { //already deleted
        replicas.remove(name);
        return false;
    }

    return true;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1890, as _ZN24QRemoteObjectNodePrivate15checkSignaturesERK10QByteArrayS2_
inline bool QRemoteObjectNodePrivate::checkSignatures(const QByteArray &a, const QByteArray &b)
{
    // if any of a or b is empty it means it's a dynamic ojects or an item model
    if (a.isEmpty() || b.isEmpty())
        return true;
    return a == b;
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectNodePrivate that Python can take functions over in. Every QRemoteObjectNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRemoteObjectNodePrivateCall0)(const void *, const QMetaObject *, QRemoteObjectReplica *, const QString *, int *);
class CuteQRemoteObjectNodePrivate : public QRemoteObjectNodePrivate {
public:
  using QRemoteObjectNodePrivate::QRemoteObjectNodePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QReplicaImplementationInterface
  //      *QRemoteObjectNodePrivate::handleNewAcquire(const QMetaObject
  //      *meta, QRemoteObjectReplica *instance, const QString &name)
  QReplicaImplementationInterface *handleNewAcquire(
      const QMetaObject *meta,
      QRemoteObjectReplica *instance,
      const QString &name) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRemoteObjectNodePrivateCall0 call = reinterpret_cast<CuteQRemoteObjectNodePrivateCall0>(taken[0]);
      void * given = call(this, meta, instance, &name, &handled);
      if (handled) return static_cast<QReplicaImplementationInterface *>(given);
    }
    return QRemoteObjectNodePrivate::handleNewAcquire(meta, instance, name);
  }
};

//  QRemoteObjectNodePrivate::~QRemoteObjectNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectNodePrivateD1Ev(
    QRemoteObjectNodePrivate *self) {
  delete self;
}

//  QRemoteObjectSourceLocations
//      QRemoteObjectNodePrivate::remoteObjectAddresses() const
extern "C" Q_DECL_EXPORT
QHash<QString, QRemoteObjectSourceLocationInfo> *ritual_ZNK24QRemoteObjectNodePrivate21remoteObjectAddressesEv(
    const QRemoteObjectNodePrivate *self) {
  return new QHash<QString, QRemoteObjectSourceLocationInfo>(
      self->remoteObjectAddresses());
}

//  void QRemoteObjectNodePrivate::setLastError(QRemoteObjectNode::ErrorCode
//      errorCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectNodePrivate12setLastErrorEN17QRemoteObjectNode9ErrorCodeE(
    QRemoteObjectNodePrivate *self,
    QRemoteObjectNode::ErrorCode errorCode) {
  self->setLastError(errorCode);
}

//  bool QRemoteObjectNodePrivate::hasInstance(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QRemoteObjectNodePrivate11hasInstanceERK7QString(
    QRemoteObjectNodePrivate *self,
    const QString *name) {
  return self->hasInstance(*name);
}

//  QReplicaImplementationInterface
//      *QRemoteObjectNodePrivate::handleNewAcquire(const QMetaObject *meta,
//      QRemoteObjectReplica *instance, const QString &name)
extern "C" Q_DECL_EXPORT
QReplicaImplementationInterface *ritual_ZN24QRemoteObjectNodePrivate16handleNewAcquireEPK11QMetaObjectP20QRemoteObjectReplicaRK7QString(
    QRemoteObjectNodePrivate *self,
    const QMetaObject *meta,
    QRemoteObjectReplica *instance,
    const QString *name) {
  return self->handleNewAcquire(meta, instance, *name);
}

//  bool QRemoteObjectNodePrivate::checkSignatures(const QByteArray &a, const
//      QByteArray &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QRemoteObjectNodePrivate15checkSignaturesERK10QByteArrayS2_(
    QRemoteObjectNodePrivate *self,
    const QByteArray *a,
    const QByteArray *b) {
  return self->checkSignatures(*a, *b);
}

//  QRemoteObjectNode *QRemoteObjectNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectNode *ritual_ZN24QRemoteObjectNodePrivate6q_funcEv(
    QRemoteObjectNodePrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectNode *QRemoteObjectNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectNode *ritual_ZNK24QRemoteObjectNodePrivate6q_funcEv(
    const QRemoteObjectNodePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQRemoteObjectNodePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectNodePrivate(
    QRemoteObjectNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectNodePrivate *>(self)->take(key, call);
}
