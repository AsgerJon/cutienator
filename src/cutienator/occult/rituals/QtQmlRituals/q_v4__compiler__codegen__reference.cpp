//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4codegen_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4codegen_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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

//  from ../qtdeclarative/src/qml/compiler/qv4codegen.cpp, line 4443, as _ZNK3QV48Compiler7Codegen6RValue12storeOnStackEv
namespace QV4::Compiler {
using namespace Qt::StringLiterals;
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline Codegen::RValue Codegen::RValue::storeOnStack() const
{
    switch (type) {
    case Accumulator:
        return RValue::fromStackSlot(codegen, Reference::fromAccumulator(codegen).storeOnStack().stackSlot());
    case StackSlot:
        return *this;
    case Const:
        return RValue::fromStackSlot(codegen, Reference::storeConstOnStack(codegen, constant).stackSlot());
    default:
        Q_UNREACHABLE();
    }
}
}  // namespace QV4::Compiler

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

//  from ../qtdeclarative/src/qml/compiler/qv4codegen.cpp, line 4473, as _ZNK3QV48Compiler7Codegen9ReferenceeqERKS2_
namespace QV4::Compiler {
using namespace Qt::StringLiterals;
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool Codegen::Reference::operator==(const Codegen::Reference &other) const
{
    if (type != other.type)
        return false;
    switch (type) {
    case Invalid:
    case Accumulator:
        break;
    case Super:
        return true;
    case SuperProperty:
        return property == other.property;
    case StackSlot:
        return theStackSlot == other.theStackSlot;
    case ScopedLocal:
        return index == other.index && scope == other.scope;
    case Name:
        return nameAsIndex() == other.nameAsIndex();
    case Member:
        return propertyBase == other.propertyBase && propertyNameIndex == other.propertyNameIndex;
    case Subscript:
        return elementBase == other.elementBase && other.subscriptLoadedForCall
                ? (subscriptLoadedForCall && element == other.element)
                : (!subscriptLoadedForCall && elementSubscript == other.elementSubscript);
    case Import:
        return index == other.index;
    case Const:
        return constant == other.constant;
    }
    return true;
}
}  // namespace QV4::Compiler

//  from ../qtdeclarative/src/qml/compiler/qv4codegen.cpp, line 4651, as _ZNK3QV48Compiler7Codegen9Reference21storeWipesAccumulatorEv
namespace QV4::Compiler {
using namespace Qt::StringLiterals;
using namespace QV4;
using namespace QQmlJS;
using namespace QQmlJS::AST;
inline bool Codegen::Reference::storeWipesAccumulator() const
{
    switch (type) {
    default:
    case Invalid:
    case Const:
    case Accumulator:
        Q_UNREACHABLE();
        return false;
    case StackSlot:
    case ScopedLocal:
        return false;
    case Name:
    case Member:
    case Subscript:
        return true;
    }
}
}  // namespace QV4::Compiler
//  -----------------------------------------------------------------------

//  bool QV4::Compiler::Codegen::Reference::isLValue() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference8isLValueEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isLValue();
}

//  QV4::Compiler::Codegen::Reference::Reference(Codegen *cg, Type t)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9ReferenceC1EPS1_NS2_4TypeE(
    QV4::Compiler::Codegen *cg,
    QV4::Compiler::Codegen::Reference::Type t) {
  return new QV4::Compiler::Codegen::Reference(cg, t);
}

//  QV4::Compiler::Codegen::Reference::Reference(const QString &name)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9ReferenceC1ERK7QString(
    const QString *name) {
  return new QV4::Compiler::Codegen::Reference(*name);
}

//  QV4::Compiler::Codegen::Reference::Reference(const Reference &a0)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9ReferenceC1ERKS2_(
    const QV4::Compiler::Codegen::Reference *a0) {
  return new QV4::Compiler::Codegen::Reference(*a0);
}

//  QV4::Compiler::Codegen::Reference::Reference(Reference &&a0)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9ReferenceC1EOS2_(
    QV4::Compiler::Codegen::Reference *a0) {
  return new QV4::Compiler::Codegen::Reference(std::move(*a0));
}

//  Reference &QV4::Compiler::Codegen::Reference::operator=(const Reference
//      &a0)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9ReferenceaSERKS2_(
    QV4::Compiler::Codegen::Reference *self,
    const QV4::Compiler::Codegen::Reference *a0) {
  return &(self->operator=(*a0));
}

//  Reference &QV4::Compiler::Codegen::Reference::operator=(Reference &&a0)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9ReferenceaSEOS2_(
    QV4::Compiler::Codegen::Reference *self,
    QV4::Compiler::Codegen::Reference *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  bool QV4::Compiler::Codegen::Reference::operator==(const Reference
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9ReferenceeqERKS2_(
    const QV4::Compiler::Codegen::Reference *self,
    const QV4::Compiler::Codegen::Reference *other) {
  return self->operator==(*other);
}

//  bool QV4::Compiler::Codegen::Reference::operator!=(const Reference
//      &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9ReferenceneERKS2_(
    const QV4::Compiler::Codegen::Reference *self,
    const QV4::Compiler::Codegen::Reference *other) {
  return self->operator!=(*other);
}

//  bool QV4::Compiler::Codegen::Reference::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference7isValidEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isValid();
}

//  bool QV4::Compiler::Codegen::Reference::loadTriggersSideEffect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference22loadTriggersSideEffectEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->loadTriggersSideEffect();
}

//  bool QV4::Compiler::Codegen::Reference::isConstant() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference10isConstantEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isConstant();
}

//  bool QV4::Compiler::Codegen::Reference::isAccumulator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference13isAccumulatorEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isAccumulator();
}

//  bool QV4::Compiler::Codegen::Reference::isSuper() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference7isSuperEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isSuper();
}

//  bool QV4::Compiler::Codegen::Reference::isSuperProperty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference15isSuperPropertyEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isSuperProperty();
}

//  bool QV4::Compiler::Codegen::Reference::isStackSlot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference11isStackSlotEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isStackSlot();
}

//  bool QV4::Compiler::Codegen::Reference::isRegister() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference10isRegisterEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->isRegister();
}

//  Reference QV4::Compiler::Codegen::Reference::fromAccumulator(Codegen *cg)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference15fromAccumulatorEPS1_(
    QV4::Compiler::Codegen *cg) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromAccumulator(
          cg));
}

//  Reference QV4::Compiler::Codegen::Reference::fromSuper(Codegen *cg)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference9fromSuperEPS1_(
    QV4::Compiler::Codegen *cg) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromSuper(
          cg));
}

//  Reference QV4::Compiler::Codegen::Reference::fromScopedLocal(Codegen *cg,
//      int index, int scope)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference15fromScopedLocalEPS1_ii(
    QV4::Compiler::Codegen *cg,
    int index,
    int scope) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromScopedLocal(
          cg,
          index,
          scope));
}

//  Reference QV4::Compiler::Codegen::Reference::fromImport(Codegen *cg, int
//      index)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference10fromImportEPS1_i(
    QV4::Compiler::Codegen *cg,
    int index) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromImport(
          cg,
          index));
}

//  Reference QV4::Compiler::Codegen::Reference::fromName(Codegen *cg, const
//      QString &name)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference8fromNameEPS1_RK7QString(
    QV4::Compiler::Codegen *cg,
    const QString *name) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromName(
          cg,
          *name));
}

//  Reference QV4::Compiler::Codegen::Reference::fromSuperProperty(const
//      Reference &property)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference17fromSuperPropertyERKS2_(
    const QV4::Compiler::Codegen::Reference *property) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromSuperProperty(
          *property));
}

//  Reference QV4::Compiler::Codegen::Reference::fromConst(Codegen *cg,
//      QV4::ReturnedValue constant)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Codegen::Reference *ritual_ZN3QV48Compiler7Codegen9Reference9fromConstEPS1_y(
    QV4::Compiler::Codegen *cg,
    QV4::ReturnedValue constant) {
  return new QV4::Compiler::Codegen::Reference(
      QV4::Compiler::Codegen::Reference::fromConst(
          cg,
          constant));
}

//  bool QV4::Compiler::Codegen::Reference::storeWipesAccumulator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV48Compiler7Codegen9Reference21storeWipesAccumulatorEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->storeWipesAccumulator();
}

//  int QV4::Compiler::Codegen::Reference::nameAsIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48Compiler7Codegen9Reference11nameAsIndexEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return self->nameAsIndex();
}

//  Moth::StackSlot QV4::Compiler::Codegen::Reference::stackSlot() const
extern "C" Q_DECL_EXPORT
QV4::Moth::StackSlot *ritual_ZNK3QV48Compiler7Codegen9Reference9stackSlotEv(
    const QV4::Compiler::Codegen::Reference *self) {
  return new QV4::Moth::StackSlot(self->stackSlot());
}

//  QV4::Compiler::Codegen::Reference::~Reference()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Codegen9ReferenceD1Ev(
    QV4::Compiler::Codegen::Reference *self) {
  delete self;
}
