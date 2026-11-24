//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::CompiledData::InlineComponentData::InlineComponentData()
extern "C" Q_DECL_EXPORT
QV4::CompiledData::InlineComponentData *ritual_ZN3QV412CompiledData19InlineComponentDataC1Ev() {
  return new QV4::CompiledData::InlineComponentData();
}

//  QV4::CompiledData::InlineComponentData::InlineComponentData(const
//      QQmlType &qmlType, int objectIndex, int nameIndex)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::InlineComponentData *ritual_ZN3QV412CompiledData19InlineComponentDataC1ERK8QQmlTypeii(
    const QQmlType *qmlType,
    int objectIndex,
    int nameIndex) {
  return new QV4::CompiledData::InlineComponentData(
      *qmlType,
      objectIndex,
      nameIndex);
}

//  QV4::CompiledData::InlineComponentData::~InlineComponentData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData19InlineComponentDataD1Ev(
    QV4::CompiledData::InlineComponentData *self) {
  delete self;
}
