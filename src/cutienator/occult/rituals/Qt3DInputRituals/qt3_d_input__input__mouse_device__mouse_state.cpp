//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/mousedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DInput::Input::MouseDevice::MouseState::MouseState()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::MouseDevice::MouseState *ritual_ZN9Qt3DInput5Input11MouseDevice10MouseStateC1Ev() {
  return new Qt3DInput::Input::MouseDevice::MouseState();
}

//  Qt3DInput::Input::MouseDevice::MouseState::~MouseState()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input11MouseDevice10MouseStateD1Ev(
    Qt3DInput::Input::MouseDevice::MouseState *self) {
  delete self;
}
