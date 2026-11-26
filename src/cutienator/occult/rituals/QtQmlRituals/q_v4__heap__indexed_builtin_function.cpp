//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::IndexedBuiltinFunction::init(QV4::ExecutionEngine
//      *engine, qsizetype index, VTable::Call call)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap22IndexedBuiltinFunction4initEPNS_15ExecutionEngineExPFyPKNS_14FunctionObjectEPKNS_5ValueES9_iE(
    QV4::Heap::IndexedBuiltinFunction *self,
    QV4::ExecutionEngine *engine,
    qsizetype index,
    void *call) {
  self->init(engine, index, reinterpret_cast<QV4::VTable::Call>(call));
}
