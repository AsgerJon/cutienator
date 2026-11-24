//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4globalobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4globalobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::EvalFunction::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV412EvalFunction12staticVTableEv() {
  return QV4::EvalFunction::staticVTable();
}

//  void QV4::EvalFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412EvalFunction10__dataTestEv(QV4::EvalFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::EvalFunction *QV4::EvalFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::EvalFunction *ritual_ZNK3QV412EvalFunction11d_uncheckedEv(
    const QV4::EvalFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::EvalFunction *QV4::EvalFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::EvalFunction *ritual_ZNK3QV412EvalFunction1dEv(
    const QV4::EvalFunction *self) {
  return self->d();
}
