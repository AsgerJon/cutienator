//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>

//  QAudioDevicePrivate::QAudioDevicePrivate(const QByteArray &i,
//      QAudioDevice::Mode m, QString description, bool isDefault,
//      AudioDeviceFormat format)
extern "C" Q_DECL_EXPORT
QAudioDevicePrivate *ritual_ZN19QAudioDevicePrivateC1ERK10QByteArrayN12QAudioDevice4ModeE7QStringbNS_17AudioDeviceFormatE(
    const QByteArray *i,
    QAudioDevice::Mode m,
    const QString *description,
    bool isDefault,
    const QAudioDevicePrivate::AudioDeviceFormat *format) {
  return new QAudioDevicePrivate(*i, m, *description, isDefault, *format);
}

//  QAudioDevicePrivate::~QAudioDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioDevicePrivateD1Ev(QAudioDevicePrivate *self) {
  delete self;
}

//  const QAudioDevicePrivate *QAudioDevicePrivate::handle(const QAudioDevice
//      &device)
extern "C" Q_DECL_EXPORT
const QAudioDevicePrivate *ritual_ZN19QAudioDevicePrivate6handleERK12QAudioDevice(
    const QAudioDevice *device) {
  return QAudioDevicePrivate::handle(*device);
}
