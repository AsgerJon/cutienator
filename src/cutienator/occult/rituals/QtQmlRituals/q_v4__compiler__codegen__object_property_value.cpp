//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Compiler::Codegen::ObjectPropertyValue::ObjectPropertyValue()
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::ObjectPropertyValue *ritual_ZN3QV48Compiler7Codegen19ObjectPropertyValueC1Ev() {
  return new QV4::Compiler::Codegen::ObjectPropertyValue();
}

//  bool QV4::Compiler::Codegen::ObjectPropertyValue::hasGetter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen19ObjectPropertyValue9hasGetterEv(
    const QV4::Compiler::Codegen::ObjectPropertyValue *self) {
  return self->hasGetter();
}

//  bool QV4::Compiler::Codegen::ObjectPropertyValue::hasSetter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen19ObjectPropertyValue9hasSetterEv(
    const QV4::Compiler::Codegen::ObjectPropertyValue *self) {
  return self->hasSetter();
}

//  QV4::Compiler::Codegen::ObjectPropertyValue::~ObjectPropertyValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen19ObjectPropertyValueD1Ev(
    QV4::Compiler::Codegen::ObjectPropertyValue *self) {
  delete self;
}
