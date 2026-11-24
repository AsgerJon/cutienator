//  Written by dev_tooling.RitualGenerator from the records of QtVirtualKeybo
//  ard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboard_global_p.h>
#include <QtVirtualKeyboard/QtVirtualKeyboard>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtVirtualKeyboard/6.12.0/QtVirtualKeyboard/private/qvirtualkeyboardinputcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVirtualKeyboardScopedState::QVirtualKeyboardScopedState(QVirtualKeyboard
//      InputContextPrivate *d, QVirtualKeyboardInputContextPrivate::State
//      state)
extern "C" Q_DECL_EXPORT
QVirtualKeyboardScopedState *ritual_ZN27QVirtualKeyboardScopedStateC1EP35QVirtualKeyboardInputContextPrivateNS0_5StateE(
    QVirtualKeyboardInputContextPrivate *d,
    QVirtualKeyboardInputContextPrivate::State state) {
  return new QVirtualKeyboardScopedState(d, state);
}

//  QVirtualKeyboardScopedState::~QVirtualKeyboardScopedState()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QVirtualKeyboardScopedStateD1Ev(
    QVirtualKeyboardScopedState *self) {
  delete self;
}
