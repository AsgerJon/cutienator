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
#include <QtRemoteObjects/private/qremoteobjectregistrysource_p.h>
#include <QtCore/qdatastream.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2818, as _ZN28QRemoteObjectHostBasePrivateC2Ev
inline QRemoteObjectHostBasePrivate::QRemoteObjectHostBasePrivate()
    : QRemoteObjectNodePrivate()
    , remoteObjectIo(nullptr)
{ }

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2838, as _ZN32QRemoteObjectRegistryHostPrivateD2Ev
inline QRemoteObjectRegistryHostPrivate::~QRemoteObjectRegistryHostPrivate()
{ }

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 312, as _ZNK32QRemoteObjectRegistryHostPrivate21remoteObjectAddressesEv
inline QRemoteObjectSourceLocations QRemoteObjectRegistryHostPrivate::remoteObjectAddresses() const
{
    if (registrySource)
        return registrySource->sourceLocations();
    return QRemoteObjectSourceLocations();
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 25, as _ZN15QRegistrySource12removeServerERK4QUrl
inline void QRegistrySource::removeServer(const QUrl &url)
{
    for (auto it = m_sourceLocations.begin(), end = m_sourceLocations.end(); it != end; /* erasing */) {
        if (it.value().hostUrl == url)
            it = m_sourceLocations.erase(it);
        else
            ++it;
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectregistrysource.cpp, line 52, as _ZN15QRegistrySource12removeSourceERKSt4pairI7QString31QRemoteObjectSourceLocationInfoE
inline void QRegistrySource::removeSource(const QRemoteObjectSourceLocation &entry)
{
    if (m_sourceLocations.contains(entry.first) && m_sourceLocations[entry.first].hostUrl == entry.second.hostUrl) {
        m_sourceLocations.remove(entry.first);
        emit remoteObjectRemoved(entry);
    }
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectRegistryHostPrivate that Python can take functions over in. Every QRemoteObjectRegistryHostPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRemoteObjectRegistryHostPrivateCall0)(const void *, const QMetaObject *, QRemoteObjectReplica *, const QString *, int *);
class CuteQRemoteObjectRegistryHostPrivate : public QRemoteObjectRegistryHostPrivate {
public:
  using QRemoteObjectRegistryHostPrivate::QRemoteObjectRegistryHostPrivate;
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
      CuteQRemoteObjectRegistryHostPrivateCall0 call = reinterpret_cast<CuteQRemoteObjectRegistryHostPrivateCall0>(taken[0]);
      void * given = call(this, meta, instance, &name, &handled);
      if (handled) return static_cast<QReplicaImplementationInterface *>(given);
    }
    return QRemoteObjectHostBasePrivate::handleNewAcquire(meta, instance, name);
  }
};

//  QRemoteObjectRegistryHostPrivate::~QRemoteObjectRegistryHostPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QRemoteObjectRegistryHostPrivateD1Ev(
    QRemoteObjectRegistryHostPrivate *self) {
  delete self;
}

//  QRemoteObjectSourceLocations
//      QRemoteObjectRegistryHostPrivate::remoteObjectAddresses() const
extern "C" Q_DECL_EXPORT
QHash<QString, QRemoteObjectSourceLocationInfo> *ritual_ZNK32QRemoteObjectRegistryHostPrivate21remoteObjectAddressesEv(
    const QRemoteObjectRegistryHostPrivate *self) {
  return new QHash<QString, QRemoteObjectSourceLocationInfo>(
      self->remoteObjectAddresses());
}

//  QRemoteObjectRegistryHost *QRemoteObjectRegistryHostPrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectRegistryHost *ritual_ZN32QRemoteObjectRegistryHostPrivate6q_funcEv(
    QRemoteObjectRegistryHostPrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectRegistryHost
//      *QRemoteObjectRegistryHostPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectRegistryHost *ritual_ZNK32QRemoteObjectRegistryHostPrivate6q_funcEv(
    const QRemoteObjectRegistryHostPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQRemoteObjectRegistryHostPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectRegistryHostPrivate(
    QRemoteObjectRegistryHostPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectRegistryHostPrivate *>(self)->take(key, call);
}
