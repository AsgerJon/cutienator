//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::PropertyHash::PropertyHash(const PropertyHash &other)
extern "C" Q_DECL_EXPORT
QV4::PropertyHash *ritual_ZN3QV412PropertyHashC1ERKS0_(
    const QV4::PropertyHash *other) {
  return new QV4::PropertyHash(*other);
}

//  QV4::PropertyHash::~PropertyHash()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412PropertyHashD1Ev(QV4::PropertyHash *self) {
  delete self;
}

//  Entry *QV4::PropertyHash::lookup(PropertyKey identifier) const
extern "C" Q_DECL_EXPORT
QV4::PropertyHash::Entry *ritual_ZNK3QV412PropertyHash6lookupENS_11PropertyKeyE(
    const QV4::PropertyHash *self,
    const QV4::PropertyKey *identifier) {
  return self->lookup(*identifier);
}
