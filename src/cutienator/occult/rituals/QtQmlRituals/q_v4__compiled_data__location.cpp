//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::CompiledData::Location::Location()
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Location *ritual_ZN3QV412CompiledData8LocationC1Ev() {
  return new QV4::CompiledData::Location();
}

//  QV4::CompiledData::Location::Location(quint32 l, quint32 c)
extern "C" Q_DECL_EXPORT
QV4::CompiledData::Location *ritual_ZN3QV412CompiledData8LocationC1Ejj(
    quint32 l,
    quint32 c) {
  return new QV4::CompiledData::Location(l, c);
}

//  bool QV4::CompiledData::Location::operator<(const Location &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData8LocationltERKS1_(
    const QV4::CompiledData::Location *self,
    const QV4::CompiledData::Location *other) {
  return self->operator<(*other);
}

//  bool operator==(const Location &lhs, const Location &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV412CompiledDataeqERKNS0_8LocationES3_(
    const QV4::CompiledData::Location *lhs,
    const QV4::CompiledData::Location *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const Location &lhs, const Location &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV412CompiledDataneERKNS0_8LocationES3_(
    const QV4::CompiledData::Location *lhs,
    const QV4::CompiledData::Location *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QV4::CompiledData::Location::set(quint32 line, quint32 column)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData8Location3setEjj(
    QV4::CompiledData::Location *self,
    quint32 line,
    quint32 column) {
  self->set(line, column);
}

//  quint32 QV4::CompiledData::Location::line() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData8Location4lineEv(
    const QV4::CompiledData::Location *self) {
  return self->line();
}

//  quint32 QV4::CompiledData::Location::column() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData8Location6columnEv(
    const QV4::CompiledData::Location *self) {
  return self->column();
}

//  QV4::CompiledData::Location::~Location()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData8LocationD1Ev(
    QV4::CompiledData::Location *self) {
  delete self;
}
