//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Import *QV4::CompiledData::QmlUnit::importAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Import *ritual_ZNK3QV412CompiledData7QmlUnit8importAtEi(
    const QV4::CompiledData::QmlUnit *self,
    int idx) {
  return self->importAt(idx);
}

//  const Object *QV4::CompiledData::QmlUnit::objectAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::Object *ritual_ZNK3QV412CompiledData7QmlUnit8objectAtEi(
    const QV4::CompiledData::QmlUnit *self,
    int idx) {
  return self->objectAt(idx);
}

//  QV4::CompiledData::QmlUnit::~QmlUnit()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData7QmlUnitD1Ev(
    QV4::CompiledData::QmlUnit *self) {
  delete self;
}
