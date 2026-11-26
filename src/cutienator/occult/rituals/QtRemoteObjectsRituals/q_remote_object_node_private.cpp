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
#include <QtCore/qloggingcategory.h>
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

using namespace QRemoteObjectStringLiterals;

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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 305, as _ZNK24QRemoteObjectNodePrivate21remoteObjectAddressesEv
inline QRemoteObjectSourceLocations QRemoteObjectNodePrivate::remoteObjectAddresses() const
{
    if (registry)
        return registry->sourceLocations();
    return QRemoteObjectSourceLocations();
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 471, as _ZN31QConnectedReplicaImplementation13setConnectionEP16QtROIoDeviceBase
inline void QConnectedReplicaImplementation::setConnection(QtROIoDeviceBase *conn)
{
    if (connectionToSource.isNull()) {
        connectionToSource = conn;
        qCDebug(QT_REMOTEOBJECT) << "setConnection started" << conn << m_objectName;
    }
    requestRemoteObjectSource();
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 176, as _ZNK31QConnectedReplicaImplementation12childIndicesEv
inline QList<int> QConnectedReplicaImplementation::childIndices() const
{
    return m_childIndices;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 498, as _ZN31QConnectedReplicaImplementation25requestRemoteObjectSourceEv
inline void QConnectedReplicaImplementation::requestRemoteObjectSource()
{
    Q_ASSERT(connectionToSource);
    connectionToSource->d_func()->m_codec->serializeAddObjectPacket(m_objectName, needsDynamicInitialization());
    sendCommand();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 164, as _ZN31QConnectedReplicaImplementation11sendCommandEv
inline bool QConnectedReplicaImplementation::sendCommand()
{
    Q_ASSERT(connectionToSource);
    if (!connectionToSource->isOpen())
        return false;

    connectionToSource->d_func()->m_codec->send(connectionToSource);
    if (m_heartbeatTimer.interval())
        m_heartbeatTimer.start();
    return true;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectreplica.cpp, line 130, as _ZNK34QRemoteObjectReplicaImplementation26needsDynamicInitializationEv
inline bool QRemoteObjectReplicaImplementation::needsDynamicInitialization() const
{
    return m_metaObject == nullptr;
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 619, as _ZN24QRemoteObjectNodePrivate12setLastErrorEN17QRemoteObjectNode9ErrorCodeE
inline void QRemoteObjectNodePrivate::setLastError(QRemoteObjectNode::ErrorCode errorCode)
{
    Q_Q(QRemoteObjectNode);
    lastError = errorCode;
    emit q->error(lastError);
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1416, as _ZN24QRemoteObjectNodePrivate27onRemoteObjectSourceRemovedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE
inline void QRemoteObjectNodePrivate::onRemoteObjectSourceRemoved(const QRemoteObjectSourceLocation &entry)
{
    if (!entry.first.isEmpty()) {
        QRemoteObjectSourceLocations locs = registry->sourceLocations();
        locs.remove(entry.first);
        registry->d_impl->setProperty(0, QVariant::fromValue(locs));
        registry->notifySourceLocationsChanged();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 1445, as _ZN24QRemoteObjectNodePrivate17onShouldReconnectEP18QtROClientIoDevice
inline void QRemoteObjectNodePrivate::onShouldReconnect(QtROClientIoDevice *ioDevice)
{
    Q_Q(QRemoteObjectNode);

    const auto remoteObjects = ioDevice->remoteObjects();
    for (const QString &remoteObject : remoteObjects) {
        connectedSources.remove(remoteObject);
        ioDevice->removeSource(remoteObject);
        if (replicas.contains(remoteObject)) { //We have a replica waiting on this remoteObject
            QSharedPointer<QConnectedReplicaImplementation> rep = qSharedPointerCast<QConnectedReplicaImplementation>(replicas.value(remoteObject).toStrongRef());
            if (rep && !rep->connectionToSource.isNull()) {
                rep->setDisconnected();
            } else if (!rep) {
                replicas.remove(remoteObject);
            }
        }
    }
    if (requestedUrls.contains(ioDevice->url())) {
        // Only try to reconnect to URLs requested via connectToNode
        // If we connected via registry, wait for the registry to see the node/source again
        pendingReconnect.insert(ioDevice);
        if (!reconnectTimer.isActive()) {
            reconnectTimer.start(retryInterval, q);
            qROPrivDebug() << "Starting reconnect timer";
        }
    } else {
        qROPrivDebug() << "Url" << ioDevice->url().toDisplayString().toLatin1()
                       << "lost.  We will reconnect Replicas if they reappear on the Registry.";
    }
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

//  void QRemoteObjectNodePrivate::connectReplica(QObject *object,
//      QRemoteObjectReplica *instance)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectNodePrivate14connectReplicaEP7QObjectP20QRemoteObjectReplica(
    QRemoteObjectNodePrivate *self,
    QObject *object,
    QRemoteObjectReplica *instance) {
  self->connectReplica(object, instance);
}

//  bool QRemoteObjectNodePrivate::hasInstance(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QRemoteObjectNodePrivate11hasInstanceERK7QString(
    QRemoteObjectNodePrivate *self,
    const QString *name) {
  return self->hasInstance(*name);
}

//  void QRemoteObjectNodePrivate::onRemoteObjectSourceRemoved(const
//      QRemoteObjectSourceLocation &entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectNodePrivate27onRemoteObjectSourceRemovedERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE(
    QRemoteObjectNodePrivate *self,
    const QRemoteObjectSourceLocation *entry) {
  self->onRemoteObjectSourceRemoved(*entry);
}

//  void QRemoteObjectNodePrivate::onShouldReconnect(QtROClientIoDevice
//      *ioDevice)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectNodePrivate17onShouldReconnectEP18QtROClientIoDevice(
    QRemoteObjectNodePrivate *self,
    QtROClientIoDevice *ioDevice) {
  self->onShouldReconnect(ioDevice);
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
