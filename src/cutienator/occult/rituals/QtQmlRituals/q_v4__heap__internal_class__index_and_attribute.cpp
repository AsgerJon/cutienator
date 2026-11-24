//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::Heap::InternalClass::IndexAndAttribute::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13InternalClass17IndexAndAttribute7isValidEv(
    const QV4::Heap::InternalClass::IndexAndAttribute *self) {
  return self->isValid();
}

//  QV4::Heap::InternalClass::IndexAndAttribute::~IndexAndAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13InternalClass17IndexAndAttributeD1Ev(
    QV4::Heap::InternalClass::IndexAndAttribute *self) {
  delete self;
}
