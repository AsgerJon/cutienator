//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  RValue QV4::Compiler::Codegen::RValue::fromStackSlot(Codegen *codegen,
//      Moth::StackSlot stackSlot)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::RValue *ritual_ZN3QV48Compiler7Codegen6RValue13fromStackSlotEPS1_NS_4Moth9StackSlotE(
    QV4::Compiler::Codegen *codegen,
    const QV4::Moth::StackSlot *stackSlot) {
  return new QV4::Compiler::Codegen::RValue(
      QV4::Compiler::Codegen::RValue::fromStackSlot(
          codegen,
          *stackSlot));
}

//  RValue QV4::Compiler::Codegen::RValue::fromAccumulator(Codegen *codegen)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::RValue *ritual_ZN3QV48Compiler7Codegen6RValue15fromAccumulatorEPS1_(
    QV4::Compiler::Codegen *codegen) {
  return new QV4::Compiler::Codegen::RValue(
      QV4::Compiler::Codegen::RValue::fromAccumulator(
          codegen));
}

//  RValue QV4::Compiler::Codegen::RValue::fromConst(Codegen *codegen,
//      QV4::ReturnedValue value)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::RValue *ritual_ZN3QV48Compiler7Codegen6RValue9fromConstEPS1_y(
    QV4::Compiler::Codegen *codegen,
    QV4::ReturnedValue value) {
  return new QV4::Compiler::Codegen::RValue(
      QV4::Compiler::Codegen::RValue::fromConst(
          codegen,
          value));
}

//  bool QV4::Compiler::Codegen::RValue::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen6RValue7isValidEv(
    const QV4::Compiler::Codegen::RValue *self) {
  return self->isValid();
}

//  bool QV4::Compiler::Codegen::RValue::isAccumulator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen6RValue13isAccumulatorEv(
    const QV4::Compiler::Codegen::RValue *self) {
  return self->isAccumulator();
}

//  bool QV4::Compiler::Codegen::RValue::isStackSlot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen6RValue11isStackSlotEv(
    const QV4::Compiler::Codegen::RValue *self) {
  return self->isStackSlot();
}

//  bool QV4::Compiler::Codegen::RValue::isConst() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen6RValue7isConstEv(
    const QV4::Compiler::Codegen::RValue *self) {
  return self->isConst();
}

//  Moth::StackSlot QV4::Compiler::Codegen::RValue::stackSlot() const
extern "C" Q_DECL_EXPORT
QV4::Moth::StackSlot *ritual_ZNK3QV48Compiler7Codegen6RValue9stackSlotEv(
    const QV4::Compiler::Codegen::RValue *self) {
  return new QV4::Moth::StackSlot(self->stackSlot());
}

//  QV4::ReturnedValue QV4::Compiler::Codegen::RValue::constantValue() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV48Compiler7Codegen6RValue13constantValueEv(
    const QV4::Compiler::Codegen::RValue *self) {
  return self->constantValue();
}

//  QV4::Compiler::Codegen::RValue::~RValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen6RValueD1Ev(
    QV4::Compiler::Codegen::RValue *self) {
  delete self;
}
