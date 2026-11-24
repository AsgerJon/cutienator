//  Written by dev_tooling.RitualGenerator from the records of QtQmlDesignSup
//  port/6.12.0/QtQmlDesignSupport/private/qobjectregistryref_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#include <QtQmlDesignSupport/qobjectregistryref.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistryref_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QObjectRegistryRef *QObjectRegistryRefPrivate::q_func()
extern "C" Q_DECL_EXPORT
QObjectRegistryRef *ritual_ZN25QObjectRegistryRefPrivate6q_funcEv(
    QObjectRegistryRefPrivate *self) {
  return self->q_func();
}

//  const QObjectRegistryRef *QObjectRegistryRefPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QObjectRegistryRef *ritual_ZNK25QObjectRegistryRefPrivate6q_funcEv(
    const QObjectRegistryRefPrivate *self) {
  return self->q_func();
}

//  QObjectRegistryRefPrivate::QObjectRegistryRefPrivate(QQmlEngine *engine)
extern "C" Q_DECL_EXPORT
QObjectRegistryRefPrivate *ritual_ZN25QObjectRegistryRefPrivateC1EP10QQmlEngine(
    QQmlEngine *engine) {
  return new QObjectRegistryRefPrivate(engine);
}

//  void QObjectRegistryRefPrivate::setObject(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QObjectRegistryRefPrivate9setObjectEP7QObject(
    QObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->setObject(obj);
}

//  void QObjectRegistryRefPrivate::printMultiWarning() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QObjectRegistryRefPrivate17printMultiWarningEv(
    const QObjectRegistryRefPrivate *self) {
  self->printMultiWarning();
}

//  void QObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QObjectRegistryRefPrivate17handleObjectAddedEP7QObject(
    QObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->handleObjectAdded(obj);
}

//  void QObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QObjectRegistryRefPrivate19handleObjectRemovedEP7QObject(
    QObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->handleObjectRemoved(obj);
}

//  void QObjectRegistryRefPrivate::handleInitialObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QObjectRegistryRefPrivate20handleInitialObjectsEv(
    QObjectRegistryRefPrivate *self) {
  self->handleInitialObjects();
}

//  void QObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QObjectRegistryRefPrivate17handleObjectAddedEP7QObject(
    QObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->QObjectRegistryRefPrivate::handleObjectAdded(obj);
}

//  void QObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QObjectRegistryRefPrivate19handleObjectRemovedEP7QObject(
    QObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->QObjectRegistryRefPrivate::handleObjectRemoved(obj);
}

//  void QObjectRegistryRefPrivate::handleInitialObjects()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QObjectRegistryRefPrivate20handleInitialObjectsEv(
    QObjectRegistryRefPrivate *self) {
  self->QObjectRegistryRefPrivate::handleInitialObjects();
}
