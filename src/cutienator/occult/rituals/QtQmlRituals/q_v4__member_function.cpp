//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::MemberFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414MemberFunction10__dataTestEv(QV4::MemberFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::MemberFunction *QV4::MemberFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberFunction *ritual_ZNK3QV414MemberFunction11d_uncheckedEv(
    const QV4::MemberFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MemberFunction *QV4::MemberFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberFunction *ritual_ZNK3QV414MemberFunction1dEv(
    const QV4::MemberFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::MemberFunction::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV414MemberFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::MemberFunction::defaultInternalClass(e);
}
