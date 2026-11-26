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

//  void
//      QAbstractObjectRegistryRefPrivate::dataAppend(QQmlListProperty<QObjec
//      t> *l, QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate10dataAppendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *l,
    QObject *o) {
  QAbstractObjectRegistryRefPrivate::dataAppend(l, o);
}

//  qsizetype
//      QAbstractObjectRegistryRefPrivate::dataCount(QQmlListProperty<QObject
//      > *l)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN33QAbstractObjectRegistryRefPrivate9dataCountEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *l) {
  return QAbstractObjectRegistryRefPrivate::dataCount(l);
}

//  QObject
//      *QAbstractObjectRegistryRefPrivate::dataAt(QQmlListProperty<QObject>
//      *l, qsizetype i)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN33QAbstractObjectRegistryRefPrivate6dataAtEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *l,
    qsizetype i) {
  return QAbstractObjectRegistryRefPrivate::dataAt(l, i);
}

//  void
//      QAbstractObjectRegistryRefPrivate::dataClear(QQmlListProperty<QObject
//      > *l)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate9dataClearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *l) {
  QAbstractObjectRegistryRefPrivate::dataClear(l);
}

//  void
//      QAbstractObjectRegistryRefPrivate::dataReplace(QQmlListProperty<QObje
//      ct> *l, qsizetype i, QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate11dataReplaceEP16QQmlListPropertyI7QObjectExPS1_(
    QQmlListProperty<QObject> *l,
    qsizetype i,
    QObject *o) {
  QAbstractObjectRegistryRefPrivate::dataReplace(l, i, o);
}

//  void QAbstractObjectRegistryRefPrivate::dataRemoveLast(QQmlListProperty<Q
//      Object> *l)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QAbstractObjectRegistryRefPrivate14dataRemoveLastEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *l) {
  QAbstractObjectRegistryRefPrivate::dataRemoveLast(l);
}
