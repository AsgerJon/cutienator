//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4codegen_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljsdiagnosticmessage_p.h>
#include <QtQml/private/qv4bytecodegenerator_p.h>
#include <QtQml/private/qv4compilercontext_p.h>
#include <QtQml/private/qv4compilercontrolflow_p.h>
#include <QtQml/private/qv4compilerscanfunctions_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4staticvalue_p.h>
#include <QtQml/private/qv4stringtoarrayindex_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qstack.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qurl.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtdeclarative/src/qml/compiler/qv4codegen.cpp, line 4578, as _ZNK3QV48Compiler7Codegen9Reference12storeOnStackEv
namespace QV4::Compiler {
using namespace Qt::StringLiterals;
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline Codegen::Reference Codegen::Reference::storeOnStack() const
{ return doStoreOnStack(-1); }
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4codegen.cpp, line 4584, as _ZNK3QV48Compiler7Codegen9Reference14doStoreOnStackEi
namespace QV4::Compiler {
using namespace Qt::StringLiterals;
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline Codegen::Reference Codegen::Reference::doStoreOnStack(int slotIndex) const
{
    Q_ASSERT(isValid());

    if (isStackSlot() && slotIndex == -1 && !(stackSlotIsLocalOrArgument && isVolatile) && !requiresTDZCheck)
        return *this;

    if (isStackSlot() && !requiresTDZCheck) { // temp-to-temp move
        Reference dest = Reference::fromStackSlot(codegen, slotIndex);
        Instruction::MoveReg move;
        move.srcReg = stackSlot();
        move.destReg = dest.stackSlot();
        codegen->bytecodeGenerator->addInstruction(move);
        return dest;
    }

    Reference slot = Reference::fromStackSlot(codegen, slotIndex);
    if (isConstant()) {
        Instruction::MoveConst move;
        move.constIndex = codegen->registerConstant(constant);
        move.destTemp = slot.stackSlot();
        codegen->bytecodeGenerator->addInstruction(move);
    } else {
        loadInAccumulator();
        slot.storeConsumeAccumulator();
    }
    return slot;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4codegen.cpp, line 4429, as _ZNK3QV48Compiler7Codegen6RValueeqERKS2_
namespace QV4::Compiler {
using namespace Qt::StringLiterals;
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool Codegen::RValue::operator==(const RValue &other) const
{
    switch (type) {
    case Accumulator:
        return other.isAccumulator();
    case StackSlot:
        return other.isStackSlot() && theStackSlot == other.theStackSlot;
    case Const:
        return other.isConst() && constant == other.constant;
    default:
        return false;
    }
}
}  // namespace QV4::Compiler
//  -----------------------------------------------------------------------

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

//  bool QV4::Compiler::Codegen::RValue::operator==(const RValue &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen6RValueeqERKS2_(
    const QV4::Compiler::Codegen::RValue *self,
    const QV4::Compiler::Codegen::RValue *other) {
  return self->operator==(*other);
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
