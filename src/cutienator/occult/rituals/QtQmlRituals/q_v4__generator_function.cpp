//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4generatorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::GeneratorFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417GeneratorFunction10__dataTestEv(
    QV4::GeneratorFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::GeneratorFunction *QV4::GeneratorFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::GeneratorFunction *ritual_ZNK3QV417GeneratorFunction11d_uncheckedEv(
    const QV4::GeneratorFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::GeneratorFunction *QV4::GeneratorFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::GeneratorFunction *ritual_ZNK3QV417GeneratorFunction1dEv(
    const QV4::GeneratorFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::GeneratorFunction::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV417GeneratorFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::GeneratorFunction::defaultInternalClass(e);
}

//  Heap::FunctionObject *QV4::GeneratorFunction::create(ExecutionContext
//      *scope, Function *function)
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZN3QV417GeneratorFunction6createEPNS_16ExecutionContextEPNS_8FunctionE(
    QV4::ExecutionContext *scope,
    QV4::Function *function) {
  return QV4::GeneratorFunction::create(scope, function);
}
