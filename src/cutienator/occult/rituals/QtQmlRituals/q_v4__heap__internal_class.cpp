//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::Heap::InternalClass::isExtensible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass12isExtensibleEv(
    const QV4::Heap::InternalClass *self) {
  return self->isExtensible();
}

//  bool QV4::Heap::InternalClass::isSealed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass8isSealedEv(
    const QV4::Heap::InternalClass *self) {
  return self->isSealed();
}

//  bool QV4::Heap::InternalClass::isFrozen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass8isFrozenEv(
    const QV4::Heap::InternalClass *self) {
  return self->isFrozen();
}

//  bool QV4::Heap::InternalClass::isUsedAsProto() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass13isUsedAsProtoEv(
    const QV4::Heap::InternalClass *self) {
  return self->isUsedAsProto();
}

//  bool QV4::Heap::InternalClass::isLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass8isLockedEv(
    const QV4::Heap::InternalClass *self) {
  return self->isLocked();
}

//  PropertyHash::Entry *QV4::Heap::InternalClass::findEntry(const
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::PropertyHash::Entry *ritual_ZN3QV44Heap13InternalClass9findEntryENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return self->findEntry(*id);
}

//  InternalClassEntry QV4::Heap::InternalClass::find(const PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::InternalClassEntry *ritual_ZN3QV44Heap13InternalClass4findENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return new QV4::InternalClassEntry(self->find(*id));
}

//  IndexAndAttribute QV4::Heap::InternalClass::findValueOrGetter(const
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass::IndexAndAttribute *ritual_ZN3QV44Heap13InternalClass17findValueOrGetterENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return new QV4::Heap::InternalClass::IndexAndAttribute(
      self->findValueOrGetter(
          *id));
}

//  IndexAndAttribute QV4::Heap::InternalClass::findValueOrSetter(const
//      PropertyKey id)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass::IndexAndAttribute *ritual_ZN3QV44Heap13InternalClass17findValueOrSetterENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return new QV4::Heap::InternalClass::IndexAndAttribute(
      self->findValueOrSetter(
          *id));
}

//  uint QV4::Heap::InternalClass::indexOfValueOrGetter(const PropertyKey id)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV44Heap13InternalClass20indexOfValueOrGetterENS_11PropertyKeyE(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id) {
  return self->indexOfValueOrGetter(*id);
}

//  bool QV4::Heap::InternalClass::verifyIndex(const PropertyKey id, uint
//      index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap13InternalClass11verifyIndexENS_11PropertyKeyEj(
    QV4::Heap::InternalClass *self,
    const QV4::PropertyKey *id,
    uint index) {
  return self->verifyIndex(*id, index);
}

//  InternalClass *QV4::Heap::InternalClass::changeVTable(const VTable *vt)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass12changeVTableEPKNS_6VTableE(
    QV4::Heap::InternalClass *self,
    const QV4::VTable *vt) {
  return self->changeVTable(vt);
}

//  InternalClass *QV4::Heap::InternalClass::changePrototype(Heap::Object
//      *proto)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV44Heap13InternalClass15changePrototypeEPNS0_6ObjectE(
    QV4::Heap::InternalClass *self,
    QV4::Heap::Object *proto) {
  return self->changePrototype(proto);
}
