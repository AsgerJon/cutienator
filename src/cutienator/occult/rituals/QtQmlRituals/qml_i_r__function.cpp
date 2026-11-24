//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlirbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const Parameter *QmlIR::Function::formalsBegin() const
extern "C" Q_DECL_EXPORT
const QmlIR::Parameter *ritual_ZNK5QmlIR8Function12formalsBeginEv(
    const QmlIR::Function *self) {
  return self->formalsBegin();
}

//  const Parameter *QmlIR::Function::formalsEnd() const
extern "C" Q_DECL_EXPORT
const QmlIR::Parameter *ritual_ZNK5QmlIR8Function10formalsEndEv(
    const QmlIR::Function *self) {
  return self->formalsEnd();
}

//  QmlIR::Function::~Function()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QmlIR8FunctionD1Ev(QmlIR::Function *self) {
  delete self;
}
