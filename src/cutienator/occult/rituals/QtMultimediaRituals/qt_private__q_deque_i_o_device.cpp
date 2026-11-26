//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudio_qiodevice_support_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudio_qiodevice_support_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtPrivate::QDequeIODevice::QDequeIODevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QtPrivate::QDequeIODevice *ritual_ZN9QtPrivate14QDequeIODeviceC1EP7QObject(
    QObject *parent) {
  return new QtPrivate::QDequeIODevice(parent);
}

//  qint64 QtPrivate::QDequeIODevice::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QtPrivate14QDequeIODevice14bytesAvailableEv(
    const QtPrivate::QDequeIODevice *self) {
  return self->bytesAvailable();
}

//  qint64 QtPrivate::QDequeIODevice::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QtPrivate14QDequeIODevice8readDataEPcx(
    QtPrivate::QDequeIODevice *self,
    char *data,
    qint64 maxlen) {
  return self->readData(data, maxlen);
}

//  qint64 QtPrivate::QDequeIODevice::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QtPrivate14QDequeIODevice9writeDataEPKcx(
    QtPrivate::QDequeIODevice *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}
