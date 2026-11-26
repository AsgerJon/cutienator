//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 1.
//  Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  TypeReference &QV4::CompiledData::TypeReferenceMap::add(int nameIndex,
//      const Location &loc)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::TypeReference *ritual_ZN3QV412CompiledData16TypeReferenceMap3addEiRKNS0_8LocationE(
    QV4::CompiledData::TypeReferenceMap *self,
    int nameIndex,
    const QV4::CompiledData::Location *loc) {
  return &(self->add(nameIndex, *loc));
}

//  QV4::CompiledData::TypeReferenceMap::~TypeReferenceMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData16TypeReferenceMapD1Ev(
    QV4::CompiledData::TypeReferenceMap *self) {
  delete self;
}

//  void QV4::CompiledData::TypeReferenceMap::collectFromObject<
//      QV4::CompiledData::Object>(const QV4::CompiledData::Object *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData16TypeReferenceMap17collectFromObjectINS0_6ObjectEEEvPKT_(
    QV4::CompiledData::TypeReferenceMap *self,
    const QV4::CompiledData::Object *obj) {
  self->collectFromObject<QV4::CompiledData::Object>(obj);
}
