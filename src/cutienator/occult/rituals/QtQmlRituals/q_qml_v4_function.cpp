//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4engine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4engine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QQmlV4Function::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQmlV4Function6lengthEv(const QQmlV4Function *self) {
  return self->length();
}

//  QV4::ReturnedValue QQmlV4Function::operator[](int idx) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK14QQmlV4FunctionixEi(
    const QQmlV4Function *self,
    int idx) {
  return self->operator[](idx);
}

//  void QQmlV4Function::setReturnValue(QV4::ReturnedValue rv)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlV4Function14setReturnValueEy(
    QQmlV4Function *self,
    QV4::ReturnedValue rv) {
  self->setReturnValue(rv);
}

//  QV4::ExecutionEngine *QQmlV4Function::v4engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK14QQmlV4Function8v4engineEv(
    const QQmlV4Function *self) {
  return self->v4engine();
}

//  QQmlV4Function::QQmlV4Function(QV4::CallData *callData, QV4::Value
//      *retVal, QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QQmlV4Function *ritual_ZN14QQmlV4FunctionC1EPN3QV48CallDataEPNS0_5ValueEPNS0_15ExecutionEngineE(
    QV4::CallData *callData,
    QV4::Value *retVal,
    QV4::ExecutionEngine *e) {
  return new QQmlV4Function(callData, retVal, e);
}
