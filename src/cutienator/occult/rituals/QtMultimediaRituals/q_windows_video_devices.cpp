//  Written by hand on 2026-11-25 from
//  QtMultimedia/6.12.0/QtMultimedia/private/qwindowsvideodevices_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Of this class Qt's library offers by name only the constructor and the
//  destructor; its virtual function is called through the object. No Cute
//  class is built on it: one would need the function Qt's library offers
//  not.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qwindowsvideodevices_p.h>
#include <QtCore/qlist.h>
#include <QtMultimedia/qcameradevice.h>

//  QWindowsVideoDevices::QWindowsVideoDevices(QPlatformMediaIntegration
//      *integration)
extern "C" Q_DECL_EXPORT
QWindowsVideoDevices *ritual_ZN20QWindowsVideoDevicesC1EP25QPlatformMediaIntegration(
    QPlatformMediaIntegration *integration) {
  return new QWindowsVideoDevices(integration);
}

//  QWindowsVideoDevices::~QWindowsVideoDevices()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QWindowsVideoDevicesD1Ev(QWindowsVideoDevices *self) {
  delete self;
}

//  QList<QCameraDevice> QWindowsVideoDevices::findVideoInputs() const
extern "C" Q_DECL_EXPORT
QList<QCameraDevice> *ritual_ZNK20QWindowsVideoDevices15findVideoInputsEv(
    const QWindowsVideoDevices *self) {
  return new QList<QCameraDevice>(self->findVideoInputs());
}

#endif  // defined(Q_OS_WIN)
