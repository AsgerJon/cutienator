//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::SymbolObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412SymbolObject10__dataTestEv(QV4::SymbolObject *self) {
  self->__dataTest();
}

//  QV4::Heap::SymbolObject *QV4::SymbolObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SymbolObject *ritual_ZNK3QV412SymbolObject11d_uncheckedEv(
    const QV4::SymbolObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SymbolObject *QV4::SymbolObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SymbolObject *ritual_ZNK3QV412SymbolObject1dEv(
    const QV4::SymbolObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::SymbolObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV412SymbolObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::SymbolObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::SymbolObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV412SymbolObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::SymbolObject::defaultPrototype(e);
}
