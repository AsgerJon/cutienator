//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputdevicemanager_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinputdevicemanager_p.h>
#include <QtGui/6.12.0/QtGui/private/qinputdevicemanager_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QInputDeviceManager *QInputDeviceManagerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QInputDeviceManager *ritual_ZN26QInputDeviceManagerPrivate6q_funcEv(
    QInputDeviceManagerPrivate *self) {
  return self->q_func();
}

//  const QInputDeviceManager *QInputDeviceManagerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QInputDeviceManager *ritual_ZNK26QInputDeviceManagerPrivate6q_funcEv(
    const QInputDeviceManagerPrivate *self) {
  return self->q_func();
}

//  QInputDeviceManagerPrivate
//      *QInputDeviceManagerPrivate::get(QInputDeviceManager *mgr)
extern "C" Q_DECL_EXPORT
QInputDeviceManagerPrivate *ritual_ZN26QInputDeviceManagerPrivate3getEP19QInputDeviceManager(
    QInputDeviceManager *mgr) {
  return QInputDeviceManagerPrivate::get(mgr);
}

//  int
//      QInputDeviceManagerPrivate::deviceCount(QInputDeviceManager::DeviceTy
//      pe type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QInputDeviceManagerPrivate11deviceCountEN19QInputDeviceManager10DeviceTypeE(
    const QInputDeviceManagerPrivate *self,
    QInputDeviceManager::DeviceType type) {
  return self->deviceCount(type);
}

//  void QInputDeviceManagerPrivate::setDeviceCount(QInputDeviceManager::Devi
//      ceType type, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QInputDeviceManagerPrivate14setDeviceCountEN19QInputDeviceManager10DeviceTypeEi(
    QInputDeviceManagerPrivate *self,
    QInputDeviceManager::DeviceType type,
    int count) {
  self->setDeviceCount(type, count);
}
