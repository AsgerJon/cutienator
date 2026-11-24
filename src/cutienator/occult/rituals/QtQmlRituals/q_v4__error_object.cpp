//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ErrorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ErrorObject10__dataTestEv(QV4::ErrorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ErrorObject *QV4::ErrorObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorObject *ritual_ZNK3QV411ErrorObject11d_uncheckedEv(
    const QV4::ErrorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ErrorObject *QV4::ErrorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorObject *ritual_ZNK3QV411ErrorObject1dEv(
    const QV4::ErrorObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ErrorObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411ErrorObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ErrorObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::ErrorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV411ErrorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ErrorObject::defaultPrototype(e);
}

//  void QV4::ErrorObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ErrorObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ErrorObject::virtualDestroy(b);
}

//  SyntaxErrorObject *QV4::ErrorObject::asSyntaxError()
extern "C" Q_DECL_EXPORT
QV4::SyntaxErrorObject *ritual_ZN3QV411ErrorObject13asSyntaxErrorEv(
    QV4::ErrorObject *self) {
  return self->asSyntaxError();
}
