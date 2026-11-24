//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::JavaScriptFunctionObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV424JavaScriptFunctionObject12staticVTableEv() {
  return QV4::JavaScriptFunctionObject::staticVTable();
}

//  void QV4::JavaScriptFunctionObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV424JavaScriptFunctionObject10__dataTestEv(
    QV4::JavaScriptFunctionObject *self) {
  self->__dataTest();
}

//  QV4::Heap::JavaScriptFunctionObject
//      *QV4::JavaScriptFunctionObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::JavaScriptFunctionObject *ritual_ZNK3QV424JavaScriptFunctionObject11d_uncheckedEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::JavaScriptFunctionObject *QV4::JavaScriptFunctionObject::d()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::JavaScriptFunctionObject *ritual_ZNK3QV424JavaScriptFunctionObject1dEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->d();
}

//  void QV4::JavaScriptFunctionObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV424JavaScriptFunctionObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::JavaScriptFunctionObject::virtualDestroy(b);
}

//  Heap::ExecutionContext *QV4::JavaScriptFunctionObject::scope() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV424JavaScriptFunctionObject5scopeEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->scope();
}

//  Function *QV4::JavaScriptFunctionObject::function() const
extern "C" Q_DECL_EXPORT
QV4::Function *ritual_ZNK3QV424JavaScriptFunctionObject8functionEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->function();
}

//  unsigned int QV4::JavaScriptFunctionObject::formalParameterCount() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK3QV424JavaScriptFunctionObject20formalParameterCountEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->formalParameterCount();
}

//  unsigned int QV4::JavaScriptFunctionObject::varCount() const
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZNK3QV424JavaScriptFunctionObject8varCountEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->varCount();
}

//  bool QV4::JavaScriptFunctionObject::strictMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV424JavaScriptFunctionObject10strictModeEv(
    const QV4::JavaScriptFunctionObject *self) {
  return self->strictMode();
}
