//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::CompiledData::TypeReference::TypeReference(const Location &loc)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::TypeReference *ritual_ZN3QV412CompiledData13TypeReferenceC1ERKNS0_8LocationE(
    const QV4::CompiledData::Location *loc) {
  return new QV4::CompiledData::TypeReference(*loc);
}

//  QV4::CompiledData::TypeReference::~TypeReference()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData13TypeReferenceD1Ev(
    QV4::CompiledData::TypeReference *self) {
  delete self;
}
