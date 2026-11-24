//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4writebarrier_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4writebarrier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::WriteBarrier::write(EngineBase *engine, Heap::Base *base,
//      ReturnedValue *slot, ReturnedValue value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412WriteBarrier5writeEPNS_10EngineBaseEPNS_4Heap4BaseEPyy(
    QV4::EngineBase *engine,
    QV4::Heap::Base *base,
    QV4::ReturnedValue *slot,
    QV4::ReturnedValue value) {
  QV4::WriteBarrier::write(engine, base, slot, value);
}

//  QV4::WriteBarrier::~WriteBarrier()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412WriteBarrierD1Ev(QV4::WriteBarrier *self) {
  delete self;
}
