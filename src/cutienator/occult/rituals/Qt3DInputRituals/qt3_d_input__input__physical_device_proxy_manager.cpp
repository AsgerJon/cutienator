//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/inputmanagers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/inputmanagers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  Qt3DInput::Input::PhysicalDeviceProxyManager::PhysicalDeviceProxyManager(
//      )
extern "C" Q_DECL_EXPORT
Qt3DInput::Input::PhysicalDeviceProxyManager *ritual_ZN9Qt3DInput5Input26PhysicalDeviceProxyManagerC1Ev() {
  return new Qt3DInput::Input::PhysicalDeviceProxyManager();
}

//  void Qt3DInput::Input::PhysicalDeviceProxyManager::addPendingProxyToLoad(
//      Qt3DCore::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput5Input26PhysicalDeviceProxyManager21addPendingProxyToLoadEN8Qt3DCore7QNodeIdE(
    Qt3DInput::Input::PhysicalDeviceProxyManager *self,
    const Qt3DCore::QNodeId *id) {
  self->addPendingProxyToLoad(*id);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DInput::Input::PhysicalDeviceProxyManager::takePendingProxiesToLoa
//      d()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN9Qt3DInput5Input26PhysicalDeviceProxyManager24takePendingProxiesToLoadEv(
    Qt3DInput::Input::PhysicalDeviceProxyManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->takePendingProxiesToLoad());
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DInput::Input::PhysicalDeviceProxyManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DInput_Input_PhysicalDeviceProxyManager__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
