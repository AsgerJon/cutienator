//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/keyboarddevice_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/keyboarddevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DCore::QNodeId Qt3DInput::Input::KeyboardDevice::currentFocusItem()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input14KeyboardDevice16currentFocusItemEv(
    const Qt3DInput::Input::KeyboardDevice *self) {
  return new Qt3DCore::QNodeId(self->currentFocusItem());
}

//  Qt3DCore::QNodeId
//      Qt3DInput::Input::KeyboardDevice::lastKeyboardInputRequester() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK9Qt3DInput5Input14KeyboardDevice26lastKeyboardInputRequesterEv(
    const Qt3DInput::Input::KeyboardDevice *self) {
  return new Qt3DCore::QNodeId(self->lastKeyboardInputRequester());
}
