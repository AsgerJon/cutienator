//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::JavaScriptFunctionObject::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap24JavaScriptFunctionObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::JavaScriptFunctionObject::markObjects(b, stack);
}

//  unsigned int QV4::Heap::JavaScriptFunctionObject::formalParameterCount()
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN3QV44Heap24JavaScriptFunctionObject20formalParameterCountEv(
    QV4::Heap::JavaScriptFunctionObject *self) {
  return self->formalParameterCount();
}

//  unsigned int QV4::Heap::JavaScriptFunctionObject::varCount()
extern "C" Q_DECL_EXPORT
unsigned int ritual_ZN3QV44Heap24JavaScriptFunctionObject8varCountEv(
    QV4::Heap::JavaScriptFunctionObject *self) {
  return self->varCount();
}

//  QV4::Heap::JavaScriptFunctionObject as the
//      QV4::Heap::JavaScriptFunctionObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::JavaScriptFunctionObjectData *ritual_cast_QV4_Heap_JavaScriptFunctionObject_QV4_Heap_JavaScriptFunctionObjectData(
    QV4::Heap::JavaScriptFunctionObject *self) {
  return static_cast<QV4::Heap::JavaScriptFunctionObjectData *>(self);
}
