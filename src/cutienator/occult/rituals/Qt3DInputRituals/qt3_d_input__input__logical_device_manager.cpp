//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputmanagers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputmanagers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>

//  Qt3DInput::Input::LogicalDeviceManager::LogicalDeviceManager()
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::LogicalDeviceManager *ritual_ZN9Qt3DInput5Input20LogicalDeviceManagerC1Ev() {
  return new Qt3DInput::Input::LogicalDeviceManager();
}

//  QList<HLogicalDevice>
//      Qt3DInput::Input::LogicalDeviceManager::activeDevices() const
extern "C" Q_DECL_EXPORT
QList<Qt3DInput::Input::HLogicalDevice> *ritual_ZNK9Qt3DInput5Input20LogicalDeviceManager13activeDevicesEv(
    const Qt3DInput::Input::LogicalDeviceManager *self) {
  return new QList<Qt3DInput::Input::HLogicalDevice>(self->activeDevices());
}

//  void
//      Qt3DInput::Input::LogicalDeviceManager::addActiveDevice(HLogicalDevic
//      e device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input20LogicalDeviceManager15addActiveDeviceEN8Qt3DCore7QHandleINS0_13LogicalDeviceEEE(
    Qt3DInput::Input::LogicalDeviceManager *self,
    const Qt3DInput::Input::HLogicalDevice *device) {
  self->addActiveDevice(*device);
}

//  void
//      Qt3DInput::Input::LogicalDeviceManager::removeActiveDevice(HLogicalDe
//      vice device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input20LogicalDeviceManager18removeActiveDeviceEN8Qt3DCore7QHandleINS0_13LogicalDeviceEEE(
    Qt3DInput::Input::LogicalDeviceManager *self,
    const Qt3DInput::Input::HLogicalDevice *device) {
  self->removeActiveDevice(*device);
}

//  a QList<Qt3DInput::Input::HLogicalDevice> a ritual of
//      Qt3DInput::Input::LogicalDeviceManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_LogicalDeviceManager__QList_Qt3DInput_Input_HLogicalDevice(
    QList<Qt3DInput::Input::HLogicalDevice> *self) {
  delete self;
}
