//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4internalclass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4internalclass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QV4::InternalClassEntry::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV418InternalClassEntry7isValidEv(
    const QV4::InternalClassEntry *self) {
  return self->isValid();
}

//  QV4::InternalClassEntry::~InternalClassEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418InternalClassEntryD1Ev(QV4::InternalClassEntry *self) {
  delete self;
}
