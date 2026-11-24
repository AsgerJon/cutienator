//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4writebarrier_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4writebarrier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::WriteBarrier::HeapObjectWrapperBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412WriteBarrier21HeapObjectWrapperBase5clearEv(
    QV4::WriteBarrier::HeapObjectWrapperBase *self) {
  self->clear();
}

//  QV4::WriteBarrier::HeapObjectWrapperBase::~HeapObjectWrapperBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412WriteBarrier21HeapObjectWrapperBaseD1Ev(
    QV4::WriteBarrier::HeapObjectWrapperBase *self) {
  delete self;
}
