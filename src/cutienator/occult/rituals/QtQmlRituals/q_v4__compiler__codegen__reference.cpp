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
