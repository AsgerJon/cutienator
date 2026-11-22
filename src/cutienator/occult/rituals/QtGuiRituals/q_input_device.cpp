//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qinputdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qinputdevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QInputDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QInputDevice10metaObjectEv(
    const QInputDevice *self) {
  return self->metaObject();
}

//  QString QInputDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QInputDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QInputDevice::tr(s, c, n));
}

//  QInputDevice::QInputDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QInputDevice *ritual_ZN12QInputDeviceC1EP7QObject(QObject *parent) {
  return new QInputDevice(parent);
}

//  QInputDevice::~QInputDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QInputDeviceD1Ev(QInputDevice *self) {
  delete self;
}

//  QInputDevice::QInputDevice(const QString &name, qint64 systemId,
//      DeviceType type, const QString &seatName, QObject *parent)
extern "C" Q_DECL_EXPORT
QInputDevice *ritual_ZN12QInputDeviceC1ERK7QStringxNS_10DeviceTypeES2_P7QObject(
    const QString *name,
    qint64 systemId,
    QInputDevice::DeviceType type,
    const QString *seatName,
    QObject *parent) {
  return new QInputDevice(*name, systemId, type, *seatName, parent);
}

//  QString QInputDevice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDevice4nameEv(const QInputDevice *self) {
  return new QString(self->name());
}

//  DeviceType QInputDevice::type() const
extern "C" Q_DECL_EXPORT
QInputDevice::DeviceType ritual_ZNK12QInputDevice4typeEv(
    const QInputDevice *self) {
  return self->type();
}

//  Capabilities QInputDevice::capabilities() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QInputDevice12capabilitiesEv(const QInputDevice *self) {
  return static_cast<int>(self->capabilities().toInt());
}

//  bool QInputDevice::hasCapability(Capability cap) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QInputDevice13hasCapabilityENS_10CapabilityE(
    const QInputDevice *self,
    QInputDevice::Capability cap) {
  return self->hasCapability(cap);
}

//  qint64 QInputDevice::systemId() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QInputDevice8systemIdEv(const QInputDevice *self) {
  return self->systemId();
}

//  QString QInputDevice::seatName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QInputDevice8seatNameEv(const QInputDevice *self) {
  return new QString(self->seatName());
}

//  QRect QInputDevice::availableVirtualGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QInputDevice24availableVirtualGeometryEv(
    const QInputDevice *self) {
  return new QRect(self->availableVirtualGeometry());
}

//  const QInputDevice *QInputDevice::primaryKeyboard(const QString
//      &seatName)
extern "C" Q_DECL_EXPORT
const QInputDevice *ritual_ZN12QInputDevice15primaryKeyboardERK7QString(
    const QString *seatName) {
  return QInputDevice::primaryKeyboard(*seatName);
}
