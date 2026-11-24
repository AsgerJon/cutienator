//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::CompiledData::RegExp::RegExp()
extern "C" Q_DECL_EXPORT
QV4::CompiledData::RegExp *ritual_ZN3QV412CompiledData6RegExpC1Ev() {
  return new QV4::CompiledData::RegExp();
}

//  QV4::CompiledData::RegExp::RegExp(quint32 flags, quint32 stringIndex)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::RegExp *ritual_ZN3QV412CompiledData6RegExpC1Ejj(
    quint32 flags,
    quint32 stringIndex) {
  return new QV4::CompiledData::RegExp(flags, stringIndex);
}

//  quint32 QV4::CompiledData::RegExp::flags() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData6RegExp5flagsEv(
    const QV4::CompiledData::RegExp *self) {
  return self->flags();
}

//  quint32 QV4::CompiledData::RegExp::stringIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData6RegExp11stringIndexEv(
    const QV4::CompiledData::RegExp *self) {
  return self->stringIndex();
}

//  QV4::CompiledData::RegExp::~RegExp()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6RegExpD1Ev(
    QV4::CompiledData::RegExp *self) {
  delete self;
}
