//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpointingdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpointingdevice.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QPointingDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QPointingDevice10metaObjectEv(
    const QPointingDevice *self) {
  return self->metaObject();
}

//  QString QPointingDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QPointingDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPointingDevice::tr(s, c, n));
}

//  QPointingDevice::QPointingDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZN15QPointingDeviceC1EP7QObject(QObject *parent) {
  return new QPointingDevice(parent);
}

//  QPointingDevice::~QPointingDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDeviceD1Ev(QPointingDevice *self) {
  delete self;
}

//  QPointingDevice::QPointingDevice(const QString &name, qint64 systemId,
//      QInputDevice::DeviceType devType, PointerType pType, Capabilities
//      caps, int maxPoints, int buttonCount, const QString &seatName,
//      QPointingDeviceUniqueId uniqueId, QObject *parent)
extern "C" Q_DECL_EXPORT
QPointingDevice *ritual_ZN15QPointingDeviceC1ERK7QStringxN12QInputDevice10DeviceTypeENS_11PointerTypeE6QFlagsINS3_10CapabilityEEiiS2_23QPointingDeviceUniqueIdP7QObject(
    const QString *name,
    qint64 systemId,
    QInputDevice::DeviceType devType,
    QPointingDevice::PointerType pType,
    int caps,
    int maxPoints,
    int buttonCount,
    const QString *seatName,
    const QPointingDeviceUniqueId *uniqueId,
    QObject *parent) {
  return new QPointingDevice(
      *name,
      systemId,
      devType,
      pType,
      QFlags<QInputDevice::Capability>::fromInt(caps),
      maxPoints,
      buttonCount,
      *seatName,
      *uniqueId,
      parent);
}

//  void QPointingDevice::setType(DeviceType devType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDevice7setTypeEN12QInputDevice10DeviceTypeE(
    QPointingDevice *self,
    QInputDevice::DeviceType devType) {
  self->setType(devType);
}

//  void QPointingDevice::setCapabilities(QInputDevice::Capabilities caps)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDevice15setCapabilitiesE6QFlagsIN12QInputDevice10CapabilityEE(
    QPointingDevice *self,
    int caps) {
  self->setCapabilities(QFlags<QInputDevice::Capability>::fromInt(caps));
}

//  void QPointingDevice::setMaximumTouchPoints(int c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QPointingDevice21setMaximumTouchPointsEi(
    QPointingDevice *self,
    int c) {
  self->setMaximumTouchPoints(c);
}

//  PointerType QPointingDevice::pointerType() const
extern "C" Q_DECL_EXPORT
QPointingDevice::PointerType ritual_ZNK15QPointingDevice11pointerTypeEv(
    const QPointingDevice *self) {
  return self->pointerType();
}

//  int QPointingDevice::maximumPoints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPointingDevice13maximumPointsEv(
    const QPointingDevice *self) {
  return self->maximumPoints();
}

//  int QPointingDevice::buttonCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QPointingDevice11buttonCountEv(const QPointingDevice *self) {
  return self->buttonCount();
}

//  QPointingDeviceUniqueId QPointingDevice::uniqueId() const
extern "C" Q_DECL_EXPORT
QPointingDeviceUniqueId *ritual_ZNK15QPointingDevice8uniqueIdEv(
    const QPointingDevice *self) {
  return new QPointingDeviceUniqueId(self->uniqueId());
}

//  const QPointingDevice *QPointingDevice::primaryPointingDevice(const
//      QString &seatName)
extern "C" Q_DECL_EXPORT
const QPointingDevice *ritual_ZN15QPointingDevice21primaryPointingDeviceERK7QString(
    const QString *seatName) {
  return QPointingDevice::primaryPointingDevice(*seatName);
}
