//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::CompiledData::ParameterType::set(Flags flags, quint32
//      typeNameIndexOrCommonType)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData13ParameterType3setE6QFlagsINS1_4FlagEEj(
    QV4::CompiledData::ParameterType *self,
    int flags,
    quint32 typeNameIndexOrCommonType) {
  self->set(
      QFlags<QV4::CompiledData::ParameterType::Flag>::fromInt(flags),
      typeNameIndexOrCommonType);
}

//  bool QV4::CompiledData::ParameterType::indexIsCommonType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData13ParameterType17indexIsCommonTypeEv(
    const QV4::CompiledData::ParameterType *self) {
  return self->indexIsCommonType();
}

//  bool QV4::CompiledData::ParameterType::isList() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData13ParameterType6isListEv(
    const QV4::CompiledData::ParameterType *self) {
  return self->isList();
}

//  quint32 QV4::CompiledData::ParameterType::typeNameIndexOrCommonType()
//      const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData13ParameterType25typeNameIndexOrCommonTypeEv(
    const QV4::CompiledData::ParameterType *self) {
  return self->typeNameIndexOrCommonType();
}

//  QV4::CompiledData::ParameterType::~ParameterType()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData13ParameterTypeD1Ev(
    QV4::CompiledData::ParameterType *self) {
  delete self;
}
