//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/qremoteobjectnode.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qremoteobjectnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRemoteObjectAbstractPersistedStorePrivate::~QRemoteObjectAbstractPersist
//      edStorePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN42QRemoteObjectAbstractPersistedStorePrivateD1Ev(
    QRemoteObjectAbstractPersistedStorePrivate *self) {
  delete self;
}

//  QRemoteObjectAbstractPersistedStore
//      *QRemoteObjectAbstractPersistedStorePrivate::q_func()
extern "C" Q_DECL_EXPORT
QRemoteObjectAbstractPersistedStore *ritual_ZN42QRemoteObjectAbstractPersistedStorePrivate6q_funcEv(
    QRemoteObjectAbstractPersistedStorePrivate *self) {
  return self->q_func();
}

//  const QRemoteObjectAbstractPersistedStore
//      *QRemoteObjectAbstractPersistedStorePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QRemoteObjectAbstractPersistedStore *ritual_ZNK42QRemoteObjectAbstractPersistedStorePrivate6q_funcEv(
    const QRemoteObjectAbstractPersistedStorePrivate *self) {
  return self->q_func();
}
