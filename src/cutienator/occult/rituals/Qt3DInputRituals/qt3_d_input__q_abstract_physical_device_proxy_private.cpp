//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldeviceproxy_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A Qt3DInput::QAbstractPhysicalDeviceProxyPrivate that Python can take functions over in. Every Qt3DInput::QAbstractPhysicalDeviceProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivateCall1)(const void *, int *);
class CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivate : public Qt3DInput::QAbstractPhysicalDeviceProxyPrivate {
public:
  using Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::QAbstractPhysicalDeviceProxyPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::QAbstractPhysicalDevicePr
//      oxyPrivate(const QString &deviceName)
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivateC1ERK7QString(
    const QString *deviceName) {
  return new CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivate(*deviceName);
}

//  Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::~QAbstractPhysicalDeviceP
//      roxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivateD1Ev(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self) {
  delete self;
}

//  QAbstractPhysicalDeviceProxy
//      *Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDeviceProxy *ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate6q_funcEv(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self) {
  return self->q_func();
}

//  const QAbstractPhysicalDeviceProxy
//      *Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractPhysicalDeviceProxy *ritual_ZNK9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate6q_funcEv(
    const Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self) {
  return self->q_func();
}

//  void Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::setDevice(QAbstractP
//      hysicalDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate9setDeviceEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self,
    Qt3DInput::QAbstractPhysicalDevice *device) {
  self->setDevice(device);
}

//  void Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::resetDevice(QAbstrac
//      tPhysicalDevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate11resetDeviceEPNS_23QAbstractPhysicalDeviceE(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self,
    Qt3DInput::QAbstractPhysicalDevice *device) {
  self->resetDevice(device);
}

//  void Qt3DInput::QAbstractPhysicalDeviceProxyPrivate::setStatus(QAbstractP
//      hysicalDeviceProxy::DeviceStatus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput35QAbstractPhysicalDeviceProxyPrivate9setStatusENS_28QAbstractPhysicalDeviceProxy12DeviceStatusE(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self,
    Qt3DInput::QAbstractPhysicalDeviceProxy::DeviceStatus status) {
  self->setStatus(status);
}

//  a Python function taken by a
//      CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAbstractPhysicalDeviceProxyPrivate(
    Qt3DInput::QAbstractPhysicalDeviceProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAbstractPhysicalDeviceProxyPrivate *>(self)->take(key, call);
}
