//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4identifiertable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4identifiertable_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  PropertyKey QV4::IdentifierTable::asPropertyKey(const Heap::String *str)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV415IdentifierTable13asPropertyKeyEPKNS_4Heap6StringE(
    QV4::IdentifierTable *self,
    const QV4::Heap::String *str) {
  return new QV4::PropertyKey(self->asPropertyKey(str));
}

//  PropertyKey QV4::IdentifierTable::asPropertyKey(const QV4::String *str)
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZN3QV415IdentifierTable13asPropertyKeyEPKNS_6StringE(
    QV4::IdentifierTable *self,
    const QV4::String *str) {
  return new QV4::PropertyKey(self->asPropertyKey(str));
}

//  void QV4::IdentifierTable::addIdentifierHash(IdentifierHashData *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTable17addIdentifierHashEPNS_18IdentifierHashDataE(
    QV4::IdentifierTable *self,
    QV4::IdentifierHashData *h) {
  self->addIdentifierHash(h);
}

//  void QV4::IdentifierTable::removeIdentifierHash(IdentifierHashData *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415IdentifierTable20removeIdentifierHashEPNS_18IdentifierHashDataE(
    QV4::IdentifierTable *self,
    QV4::IdentifierHashData *h) {
  self->removeIdentifierHash(h);
}
