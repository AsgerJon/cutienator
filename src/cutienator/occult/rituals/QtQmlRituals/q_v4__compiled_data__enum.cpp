//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const EnumValue *QV4::CompiledData::Enum::enumValueAt(int idx) const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::EnumValue *ritual_ZNK3QV412CompiledData4Enum11enumValueAtEi(
    const QV4::CompiledData::Enum *self,
    int idx) {
  return self->enumValueAt(idx);
}

//  int QV4::CompiledData::Enum::calculateSize(int nEnumValues)
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV412CompiledData4Enum13calculateSizeEi(int nEnumValues) {
  return QV4::CompiledData::Enum::calculateSize(nEnumValues);
}

//  const EnumValue *QV4::CompiledData::Enum::enumValuesBegin() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::EnumValue *ritual_ZNK3QV412CompiledData4Enum15enumValuesBeginEv(
    const QV4::CompiledData::Enum *self) {
  return self->enumValuesBegin();
}

//  const EnumValue *QV4::CompiledData::Enum::enumValuesEnd() const
extern "C" Q_DECL_EXPORT
const QV4::CompiledData::EnumValue *ritual_ZNK3QV412CompiledData4Enum13enumValuesEndEv(
    const QV4::CompiledData::Enum *self) {
  return self->enumValuesEnd();
}

//  int QV4::CompiledData::Enum::enumValueCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412CompiledData4Enum14enumValueCountEv(
    const QV4::CompiledData::Enum *self) {
  return self->enumValueCount();
}

//  QV4::CompiledData::Enum::~Enum()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData4EnumD1Ev(QV4::CompiledData::Enum *self) {
  delete self;
}
