//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qinputdevice_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qinputdevice.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qinputdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  QInputDevice *QInputDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QInputDevice *ritual_ZN19QInputDevicePrivate6q_funcEv(
    QInputDevicePrivate *self) {
  return self->q_func();
}

//  const QInputDevice *QInputDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QInputDevice *ritual_ZNK19QInputDevicePrivate6q_funcEv(
    const QInputDevicePrivate *self) {
  return self->q_func();
}

//  QInputDevicePrivate::QInputDevicePrivate(const QString &name, qint64
//      winSysId, QInputDevice::DeviceType type, QInputDevice::Capabilities
//      caps, const QString &seatName)
extern "C" Q_DECL_EXPORT
QInputDevicePrivate *ritual_ZN19QInputDevicePrivateC1ERK7QStringxN12QInputDevice10DeviceTypeE6QFlagsINS3_10CapabilityEES2_(
    const QString *name,
    qint64 winSysId,
    QInputDevice::DeviceType type,
    int caps,
    const QString *seatName) {
  return new QInputDevicePrivate(
      *name,
      winSysId,
      type,
      QFlags<QInputDevice::Capability>::fromInt(caps),
      *seatName);
}

//  QInputDevicePrivate::~QInputDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDevicePrivateD1Ev(QInputDevicePrivate *self) {
  delete self;
}

//  void QInputDevicePrivate::registerDevice(const QInputDevice *dev)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDevicePrivate14registerDeviceEPK12QInputDevice(
    const QInputDevice *dev) {
  QInputDevicePrivate::registerDevice(dev);
}

//  void QInputDevicePrivate::unregisterDevice(const QInputDevice *dev)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDevicePrivate16unregisterDeviceEPK12QInputDevice(
    const QInputDevice *dev) {
  QInputDevicePrivate::unregisterDevice(dev);
}

//  bool QInputDevicePrivate::isRegistered(const QInputDevice *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QInputDevicePrivate12isRegisteredEPK12QInputDevice(
    const QInputDevice *dev) {
  return QInputDevicePrivate::isRegistered(dev);
}

//  const QInputDevice *QInputDevicePrivate::fromId(qint64 systemId)
extern "C" Q_DECL_EXPORT
const QInputDevice *ritual_ZN19QInputDevicePrivate6fromIdEx(
    qint64 systemId) {
  return QInputDevicePrivate::fromId(systemId);
}

//  void QInputDevicePrivate::setAvailableVirtualGeometry(QRect a)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDevicePrivate27setAvailableVirtualGeometryE5QRect(
    QInputDevicePrivate *self,
    const QRect *a) {
  self->setAvailableVirtualGeometry(*a);
}

//  void QInputDevicePrivate::setCapabilities(QInputDevice::Capabilities c)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QInputDevicePrivate15setCapabilitiesE6QFlagsIN12QInputDevice10CapabilityEE(
    QInputDevicePrivate *self,
    int c) {
  self->setCapabilities(QFlags<QInputDevice::Capability>::fromInt(c));
}

//  QInputDevicePrivate *QInputDevicePrivate::get(QInputDevice *q)
extern "C" Q_DECL_EXPORT
QInputDevicePrivate *ritual_ZN19QInputDevicePrivate3getEP12QInputDevice(
    QInputDevice *q) {
  return QInputDevicePrivate::get(q);
}

//  const QInputDevicePrivate *QInputDevicePrivate::get(const QInputDevice
//      *q)
extern "C" Q_DECL_EXPORT
const QInputDevicePrivate *ritual_ZN19QInputDevicePrivate3getEPK12QInputDevice(
    const QInputDevice *q) {
  return QInputDevicePrivate::get(q);
}
