//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ConstructorFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ConstructorFunction10__dataTestEv(
    QV4::ConstructorFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::ConstructorFunction *QV4::ConstructorFunction::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ConstructorFunction *ritual_ZNK3QV419ConstructorFunction11d_uncheckedEv(
    const QV4::ConstructorFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ConstructorFunction *QV4::ConstructorFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ConstructorFunction *ritual_ZNK3QV419ConstructorFunction1dEv(
    const QV4::ConstructorFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ConstructorFunction::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV419ConstructorFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ConstructorFunction::defaultInternalClass(e);
}
