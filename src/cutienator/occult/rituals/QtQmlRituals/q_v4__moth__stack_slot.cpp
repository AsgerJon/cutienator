//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4instr_moth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  StackSlot QV4::Moth::StackSlot::createRegister(int index)
extern "C" Q_DECL_EXPORT
QV4::Moth::StackSlot *ritual_ZN3QV44Moth9StackSlot14createRegisterEi(
    int index) {
  return new QV4::Moth::StackSlot(
      QV4::Moth::StackSlot::createRegister(
          index));
}

//  int QV4::Moth::StackSlot::stackSlot() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Moth9StackSlot9stackSlotEv(
    const QV4::Moth::StackSlot *self) {
  return self->stackSlot();
}

//  int QV4::Moth::StackSlot::operator int() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Moth9StackSlotcviEv(const QV4::Moth::StackSlot *self) {
  return self->operator int();
}

//  QV4::Moth::StackSlot::~StackSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Moth9StackSlotD1Ev(QV4::Moth::StackSlot *self) {
  delete self;
}
