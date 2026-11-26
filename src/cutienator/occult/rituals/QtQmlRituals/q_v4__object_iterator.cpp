//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectiterator_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ObjectIterator::ObjectIterator(Scope &scope, const Object *o, uint
//      flags)
extern "C" Q_DECL_EXPORT
QV4::ObjectIterator *ritual_ZN3QV414ObjectIteratorC1ERNS_5ScopeEPKNS_6ObjectEj(
    QV4::Scope *scope,
    const QV4::Object *o,
    uint flags) {
  return new QV4::ObjectIterator(*scope, o, flags);
}

//  QV4::ObjectIterator::~ObjectIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414ObjectIteratorD1Ev(QV4::ObjectIterator *self) {
  delete self;
}

//  PropertyKey QV4::ObjectIterator::next(Property *pd, PropertyAttributes
//      *attributes)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV414ObjectIterator4nextEPNS_8PropertyEPNS_18PropertyAttributesE(
    QV4::ObjectIterator *self,
    QV4::Property *pd,
    QV4::PropertyAttributes *attributes) {
  return new QV4::PropertyKey(self->next(pd, attributes));
}

//  ReturnedValue QV4::ObjectIterator::nextPropertyName(Value *value)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414ObjectIterator16nextPropertyNameEPNS_5ValueE(
    QV4::ObjectIterator *self,
    QV4::Value *value) {
  return self->nextPropertyName(value);
}

//  ReturnedValue QV4::ObjectIterator::nextPropertyNameAsString(Value *value)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414ObjectIterator24nextPropertyNameAsStringEPNS_5ValueE(
    QV4::ObjectIterator *self,
    QV4::Value *value) {
  return self->nextPropertyNameAsString(value);
}

//  ReturnedValue QV4::ObjectIterator::nextPropertyNameAsString()
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414ObjectIterator24nextPropertyNameAsStringEv(
    QV4::ObjectIterator *self) {
  return self->nextPropertyNameAsString();
}
