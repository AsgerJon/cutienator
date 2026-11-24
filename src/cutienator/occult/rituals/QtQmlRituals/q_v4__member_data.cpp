//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4memberdata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4memberdata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::MemberData::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410MemberData10__dataTestEv(QV4::MemberData *self) {
  self->__dataTest();
}

//  QV4::Heap::MemberData *QV4::MemberData::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberData *ritual_ZNK3QV410MemberData11d_uncheckedEv(
    const QV4::MemberData *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MemberData *QV4::MemberData::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberData *ritual_ZNK3QV410MemberData1dEv(
    const QV4::MemberData *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::MemberData::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV410MemberData20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::MemberData::defaultInternalClass(e);
}

//  const Value &QV4::MemberData::operator[](uint idx) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV410MemberDataixEj(
    const QV4::MemberData *self,
    uint idx) {
  return new QV4::Value(self->operator[](idx));
}

//  const Value *QV4::MemberData::data() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV410MemberData4dataEv(
    const QV4::MemberData *self) {
  return self->data();
}

//  void QV4::MemberData::set(EngineBase *e, uint index, Value v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410MemberData3setEPNS_10EngineBaseEjNS_5ValueE(
    QV4::MemberData *self,
    QV4::EngineBase *e,
    uint index,
    const QV4::Value *v) {
  self->set(e, index, *v);
}

//  void QV4::MemberData::set(EngineBase *e, uint index, Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410MemberData3setEPNS_10EngineBaseEjPNS_4Heap4BaseE(
    QV4::MemberData *self,
    QV4::EngineBase *e,
    uint index,
    QV4::Heap::Base *b) {
  self->set(e, index, b);
}

//  uint QV4::MemberData::size() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV410MemberData4sizeEv(const QV4::MemberData *self) {
  return self->size();
}
