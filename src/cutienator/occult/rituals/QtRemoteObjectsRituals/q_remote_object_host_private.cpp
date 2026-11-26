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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2830, as _ZN24QRemoteObjectHostPrivateD2Ev
inline QRemoteObjectHostPrivate::~QRemoteObjectHostPrivate()
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

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 2818, as _ZN28QRemoteObjectHostBasePrivateC2Ev
inline QRemoteObjectHostBasePrivate::QRemoteObjectHostBasePrivate()
    : QRemoteObjectNodePrivate()
    , remoteObjectIo(nullptr)
{ }

//  from ../qtremoteobjects/src/remoteobjects/qremoteobjectnode.cpp, line 305, as _ZNK24QRemoteObjectNodePrivate21remoteObjectAddressesEv
inline QRemoteObjectSourceLocations QRemoteObjectNodePrivate::remoteObjectAddresses() const
{
    if (registry)
        return registry->sourceLocations();
    return QRemoteObjectSourceLocations();
}
//  -----------------------------------------------------------------------

//  A QRemoteObjectHostPrivate that Python can take functions over in. Every QRemoteObjectHostPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQRemoteObjectHostPrivateCall0)(const void *, const QMetaObject *, QRemoteObjectReplica *, const QString *, int *);
class CuteQRemoteObjectHostPrivate : public QRemoteObjectHostPrivate {
public:
  using QRemoteObjectHostPrivate::QRemoteObjectHostPrivate;
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
      CuteQRemoteObjectHostPrivateCall0 call = reinterpret_cast<CuteQRemoteObjectHostPrivateCall0>(taken[0]);
      void * given = call(this, meta, instance, &name, &handled);
      if (handled) return static_cast<QReplicaImplementationInterface *>(given);
    }
    return QRemoteObjectHostBasePrivate::handleNewAcquire(meta, instance, name);
  }
};

//  QRemoteObjectHostPrivate::~QRemoteObjectHostPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRemoteObjectHostPrivateD1Ev(
    QRemoteObjectHostPrivate *self) {
  delete self;
}

//  QRemoteObjectHost *QRemoteObjectHostPrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectHost *ritual_ZN24QRemoteObjectHostPrivate6q_funcEv(
    QRemoteObjectHostPrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectHost *QRemoteObjectHostPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectHost *ritual_ZNK24QRemoteObjectHostPrivate6q_funcEv(
    const QRemoteObjectHostPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQRemoteObjectHostPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectHostPrivate(
    QRemoteObjectHostPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectHostPrivate *>(self)->take(key, call);
}
