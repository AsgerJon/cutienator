//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compileddata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::CompiledData::JSClassMember::JSClassMember()
extern "C" Q_DECL_EXPORT
QV4::CompiledData::JSClassMember *ritual_ZN3QV412CompiledData13JSClassMemberC1Ev() {
  return new QV4::CompiledData::JSClassMember();
}

//  void QV4::CompiledData::JSClassMember::set(quint32 nameOffset, bool
//      isAccessor)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData13JSClassMember3setEjb(
    QV4::CompiledData::JSClassMember *self,
    quint32 nameOffset,
    bool isAccessor) {
  self->set(nameOffset, isAccessor);
}

//  quint32 QV4::CompiledData::JSClassMember::nameOffset() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV412CompiledData13JSClassMember10nameOffsetEv(
    const QV4::CompiledData::JSClassMember *self) {
  return self->nameOffset();
}

//  bool QV4::CompiledData::JSClassMember::isAccessor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV412CompiledData13JSClassMember10isAccessorEv(
    const QV4::CompiledData::JSClassMember *self) {
  return self->isAccessor();
}

//  QV4::CompiledData::JSClassMember::~JSClassMember()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412CompiledData13JSClassMemberD1Ev(
    QV4::CompiledData::JSClassMember *self) {
  delete self;
}
