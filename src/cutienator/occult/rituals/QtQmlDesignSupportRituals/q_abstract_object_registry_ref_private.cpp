//  Written by dev_tooling.RitualGenerator from the records of QtQmlDesignSup
//  port/6.12.0/QtQmlDesignSupport/private/qabstractobjectregistryref_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#include <QtQmlDesignSupport/qabstractobjectregistryref.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qabstractobjectregistryref_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QAbstractObjectRegistryRef *QAbstractObjectRegistryRefPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractObjectRegistryRef *ritual_ZN33QAbstractObjectRegistryRefPrivate6q_funcEv(
    QAbstractObjectRegistryRefPrivate *self) {
  return self->q_func();
}

//  const QAbstractObjectRegistryRef
//      *QAbstractObjectRegistryRefPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractObjectRegistryRef *ritual_ZNK33QAbstractObjectRegistryRefPrivate6q_funcEv(
    const QAbstractObjectRegistryRefPrivate *self) {
  return self->q_func();
}

//  void QAbstractObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate17handleObjectAddedEP7QObject(
    QAbstractObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->handleObjectAdded(obj);
}

//  void QAbstractObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate19handleObjectRemovedEP7QObject(
    QAbstractObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->handleObjectRemoved(obj);
}

//  QString QAbstractObjectRegistryRefPrivate::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK33QAbstractObjectRegistryRefPrivate3keyEv(
    const QAbstractObjectRegistryRefPrivate *self) {
  return new QString(self->key());
}

//  void QAbstractObjectRegistryRefPrivate::handleInitialObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate20handleInitialObjectsEv(
    QAbstractObjectRegistryRefPrivate *self) {
  self->handleInitialObjects();
}

//  QObjectRegistrySingleton *QAbstractObjectRegistryRefPrivate::registry()
//      const
extern "C" Q_DECL_EXPORT
QObjectRegistrySingleton *ritual_ZNK33QAbstractObjectRegistryRefPrivate8registryEv(
    const QAbstractObjectRegistryRefPrivate *self) {
  return self->registry();
}
