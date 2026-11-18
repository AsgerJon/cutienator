//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectdefs.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectdefs.h>

//  const char *QMetaObject::className() const
extern "C" const char *ritual_ZNK11QMetaObject9classNameEv(
    const QMetaObject *self) {
  return self->className();
}

//  const QMetaObject *QMetaObject::superClass() const
extern "C" const QMetaObject *ritual_ZNK11QMetaObject10superClassEv(
    const QMetaObject *self) {
  return self->superClass();
}

//  bool QMetaObject::inherits(const QMetaObject *metaObject) const
extern "C" bool ritual_ZNK11QMetaObject8inheritsEPKS_(
    const QMetaObject *self,
    const QMetaObject *metaObject) {
  return self->inherits(metaObject);
}

//  QObject *QMetaObject::cast(QObject *obj) const
extern "C" QObject *ritual_ZNK11QMetaObject4castEP7QObject(
    const QMetaObject *self,
    QObject *obj) {
  return self->cast(obj);
}

//  const QObject *QMetaObject::cast(const QObject *obj) const
extern "C" const QObject *ritual_ZNK11QMetaObject4castEPK7QObject(
    const QMetaObject *self,
    const QObject *obj) {
  return self->cast(obj);
}

//  int QMetaObject::methodOffset() const
extern "C" int ritual_ZNK11QMetaObject12methodOffsetEv(
    const QMetaObject *self) {
  return self->methodOffset();
}

//  int QMetaObject::enumeratorOffset() const
extern "C" int ritual_ZNK11QMetaObject16enumeratorOffsetEv(
    const QMetaObject *self) {
  return self->enumeratorOffset();
}

//  int QMetaObject::propertyOffset() const
extern "C" int ritual_ZNK11QMetaObject14propertyOffsetEv(
    const QMetaObject *self) {
  return self->propertyOffset();
}

//  int QMetaObject::classInfoOffset() const
extern "C" int ritual_ZNK11QMetaObject15classInfoOffsetEv(
    const QMetaObject *self) {
  return self->classInfoOffset();
}

//  int QMetaObject::constructorCount() const
extern "C" int ritual_ZNK11QMetaObject16constructorCountEv(
    const QMetaObject *self) {
  return self->constructorCount();
}

//  int QMetaObject::methodCount() const
extern "C" int ritual_ZNK11QMetaObject11methodCountEv(
    const QMetaObject *self) {
  return self->methodCount();
}

//  int QMetaObject::enumeratorCount() const
extern "C" int ritual_ZNK11QMetaObject15enumeratorCountEv(
    const QMetaObject *self) {
  return self->enumeratorCount();
}

//  int QMetaObject::propertyCount() const
extern "C" int ritual_ZNK11QMetaObject13propertyCountEv(
    const QMetaObject *self) {
  return self->propertyCount();
}

//  int QMetaObject::classInfoCount() const
extern "C" int ritual_ZNK11QMetaObject14classInfoCountEv(
    const QMetaObject *self) {
  return self->classInfoCount();
}

//  int QMetaObject::indexOfConstructor(const char *constructor) const
extern "C" int ritual_ZNK11QMetaObject18indexOfConstructorEPKc(
    const QMetaObject *self,
    const char *constructor) {
  return self->indexOfConstructor(constructor);
}

//  int QMetaObject::indexOfMethod(const char *method) const
extern "C" int ritual_ZNK11QMetaObject13indexOfMethodEPKc(
    const QMetaObject *self,
    const char *method) {
  return self->indexOfMethod(method);
}

//  int QMetaObject::indexOfSignal(const char *signal) const
extern "C" int ritual_ZNK11QMetaObject13indexOfSignalEPKc(
    const QMetaObject *self,
    const char *signal) {
  return self->indexOfSignal(signal);
}

//  int QMetaObject::indexOfSlot(const char *slot) const
extern "C" int ritual_ZNK11QMetaObject11indexOfSlotEPKc(
    const QMetaObject *self,
    const char *slot) {
  return self->indexOfSlot(slot);
}

//  int QMetaObject::indexOfEnumerator(const char *name) const
extern "C" int ritual_ZNK11QMetaObject17indexOfEnumeratorEPKc(
    const QMetaObject *self,
    const char *name) {
  return self->indexOfEnumerator(name);
}

//  int QMetaObject::indexOfProperty(const char *name) const
extern "C" int ritual_ZNK11QMetaObject15indexOfPropertyEPKc(
    const QMetaObject *self,
    const char *name) {
  return self->indexOfProperty(name);
}

//  int QMetaObject::indexOfClassInfo(const char *name) const
extern "C" int ritual_ZNK11QMetaObject16indexOfClassInfoEPKc(
    const QMetaObject *self,
    const char *name) {
  return self->indexOfClassInfo(name);
}

//  bool QMetaObject::checkConnectArgs(const char *signal, const char
//      *method)
extern "C" bool ritual_ZN11QMetaObject16checkConnectArgsEPKcS1_(
    const char *signal,
    const char *method) {
  return QMetaObject::checkConnectArgs(signal, method);
}

//  bool QMetaObject::disconnect(const QObject *sender, int signal_index,
//      const QObject *receiver, int method_index)
extern "C" bool ritual_ZN11QMetaObject10disconnectEPK7QObjectiS2_i(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    int method_index) {
  return QMetaObject::disconnect(sender, signal_index, receiver, method_index);
}

//  bool QMetaObject::disconnectOne(const QObject *sender, int
//      signal_index, const QObject *receiver, int method_index)
extern "C" bool ritual_ZN11QMetaObject13disconnectOneEPK7QObjectiS2_i(
    const QObject *sender,
    int signal_index,
    const QObject *receiver,
    int method_index) {
  return QMetaObject::disconnectOne(sender, signal_index, receiver, method_index);
}

//  void QMetaObject::connectSlotsByName(QObject *o)
extern "C" void ritual_ZN11QMetaObject18connectSlotsByNameEP7QObject(
    QObject *o) {
  QMetaObject::connectSlotsByName(o);
}
