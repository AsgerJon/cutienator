//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/recursivemethodguard_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/recursivemethodguard_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtVirtualKeyboard::RecursiveMethodGuard::RecursiveMethodGuard(bool &flag)
extern "C" Q_DECL_EXPORT
QtVirtualKeyboard::RecursiveMethodGuard *ritual_ZN17QtVirtualKeyboard20RecursiveMethodGuardC1ERb(
    bool *flag) {
  return new QtVirtualKeyboard::RecursiveMethodGuard(*flag);
}

//  QtVirtualKeyboard::RecursiveMethodGuard::~RecursiveMethodGuard()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtVirtualKeyboard20RecursiveMethodGuardD1Ev(
    QtVirtualKeyboard::RecursiveMethodGuard *self) {
  delete self;
}

//  bool QtVirtualKeyboard::RecursiveMethodGuard::locked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtVirtualKeyboard20RecursiveMethodGuard6lockedEv(
    const QtVirtualKeyboard::RecursiveMethodGuard *self) {
  return self->locked();
}
