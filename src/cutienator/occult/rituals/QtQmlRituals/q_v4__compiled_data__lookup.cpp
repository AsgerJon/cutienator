//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  quint32 QV4::CompiledData::Lookup::type() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData6Lookup4typeEv(
    const QV4::CompiledData::Lookup *self) {
  return self->type();
}

//  quint32 QV4::CompiledData::Lookup::nameIndex() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData6Lookup9nameIndexEv(
    const QV4::CompiledData::Lookup *self) {
  return self->nameIndex();
}

//  quint32 QV4::CompiledData::Lookup::mode() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData6Lookup4modeEv(
    const QV4::CompiledData::Lookup *self) {
  return self->mode();
}

//  QV4::CompiledData::Lookup::Lookup()
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Lookup *ritual_ZN3QV412CompiledData6LookupC1Ev() {
  return new QV4::CompiledData::Lookup();
}

//  QV4::CompiledData::Lookup::Lookup(Type type, Mode mode, quint32
//      nameIndex)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Lookup *ritual_ZN3QV412CompiledData6LookupC1ENS1_4TypeENS1_4ModeEj(
    QV4::CompiledData::Lookup::Type type,
    QV4::CompiledData::Lookup::Mode mode,
    quint32 nameIndex) {
  return new QV4::CompiledData::Lookup(type, mode, nameIndex);
}

//  QV4::CompiledData::Lookup::~Lookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData6LookupD1Ev(
    QV4::CompiledData::Lookup *self) {
  delete self;
}
