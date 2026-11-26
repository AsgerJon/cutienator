//  Written by dev_tooling.RitualGenerator from the records of QtQmlDesignSup
//  port/6.12.0/QtQmlDesignSupport/private/qmultiobjectregistryref_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#include <QtQmlDesignSupport/qmultiobjectregistryref.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qmultiobjectregistryref_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QMultiObjectRegistryRef *QMultiObjectRegistryRefPrivate::q_func()
extern "C" Q_DECL_EXPORT
QMultiObjectRegistryRef *ritual_ZN30QMultiObjectRegistryRefPrivate6q_funcEv(
    QMultiObjectRegistryRefPrivate *self) {
  return self->q_func();
}

//  const QMultiObjectRegistryRef *QMultiObjectRegistryRefPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QMultiObjectRegistryRef *ritual_ZNK30QMultiObjectRegistryRefPrivate6q_funcEv(
    const QMultiObjectRegistryRefPrivate *self) {
  return self->q_func();
}

//  QMultiObjectRegistryRefPrivate::QMultiObjectRegistryRefPrivate(QQmlEngine
//      *engine)
extern "C" Q_DECL_EXPORT
QMultiObjectRegistryRefPrivate *ritual_ZN30QMultiObjectRegistryRefPrivateC1EP10QQmlEngine(
    QQmlEngine *engine) {
  return new QMultiObjectRegistryRefPrivate(engine);
}

//  void QMultiObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QMultiObjectRegistryRefPrivate17handleObjectAddedEP7QObject(
    QMultiObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->handleObjectAdded(obj);
}

//  void QMultiObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QMultiObjectRegistryRefPrivate19handleObjectRemovedEP7QObject(
    QMultiObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->handleObjectRemoved(obj);
}

//  void QMultiObjectRegistryRefPrivate::handleInitialObjects()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QMultiObjectRegistryRefPrivate20handleInitialObjectsEv(
    QMultiObjectRegistryRefPrivate *self) {
  self->handleInitialObjects();
}

//  qsizetype
//      QMultiObjectRegistryRefPrivate::objectsCount(QQmlListProperty<QObject
//      > *l)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN30QMultiObjectRegistryRefPrivate12objectsCountEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *l) {
  return QMultiObjectRegistryRefPrivate::objectsCount(l);
}

//  QObject
//      *QMultiObjectRegistryRefPrivate::objectsAt(QQmlListProperty<QObject>
//      *l, qsizetype i)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN30QMultiObjectRegistryRefPrivate9objectsAtEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *l,
    qsizetype i) {
  return QMultiObjectRegistryRefPrivate::objectsAt(l, i);
}

//  void QMultiObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QMultiObjectRegistryRefPrivate17handleObjectAddedEP7QObject(
    QMultiObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->QMultiObjectRegistryRefPrivate::handleObjectAdded(obj);
}

//  void QMultiObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QMultiObjectRegistryRefPrivate19handleObjectRemovedEP7QObject(
    QMultiObjectRegistryRefPrivate *self,
    QObject *obj) {
  self->QMultiObjectRegistryRefPrivate::handleObjectRemoved(obj);
}

//  void QMultiObjectRegistryRefPrivate::handleInitialObjects()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QMultiObjectRegistryRefPrivate20handleInitialObjectsEv(
    QMultiObjectRegistryRefPrivate *self) {
  self->QMultiObjectRegistryRefPrivate::handleInitialObjects();
}
