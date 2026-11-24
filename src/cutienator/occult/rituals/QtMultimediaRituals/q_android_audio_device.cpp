//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qandroidaudiodevice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if defined(Q_OS_ANDROID)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qandroidaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qandroidaudiodevice_p.h>
#include <QtMultimedia/private/qaudioformat_p.h>
#include <QtMultimedia/private/qaudiodevice_p.h>
#include <QtCore/qjniobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevice.cpp, line 36, as _ZN19QAndroidAudioDeviceC1E10QByteArray7QStringN12QAudioDevice4ModeE12QAudioFormatbb
inline QAndroidAudioDevice::QAndroidAudioDevice(QByteArray device, QString desc, QAudioDevice::Mode mode,
                                         QAudioFormat format, bool isBluetoothDevice,
                                         bool isDefaultDevice)
    : QAudioDevicePrivate{ std::move(device), mode, std::move(desc), isDefaultDevice,
                           createAndroidAudioDeviceFormatFromPreferred(format) },
      m_isBluetoothDevice(isBluetoothDevice)
{
}

//  from ../qtmultimedia/src/multimedia/android/qandroidaudiodevice.cpp, line 45, as _ZNK19QAndroidAudioDevice17isBluetoothDeviceEv
inline bool QAndroidAudioDevice::isBluetoothDevice() const
{
    return m_isBluetoothDevice;
}
//  -----------------------------------------------------------------------

//  QAndroidAudioDevice::QAndroidAudioDevice(QByteArray device, QString desc,
//      QAudioDevice::Mode mode, QAudioFormat preferredFormat, bool
//      isBluetoothDevice, bool isDefaultDevice)
extern "C" Q_DECL_EXPORT
QAndroidAudioDevice *ritual_ZN19QAndroidAudioDeviceC1E10QByteArray7QStringN12QAudioDevice4ModeE12QAudioFormatbb(
    const QByteArray *device,
    const QString *desc,
    QAudioDevice::Mode mode,
    const QAudioFormat *preferredFormat,
    bool isBluetoothDevice,
    bool isDefaultDevice) {
  return new QAndroidAudioDevice(
      *device,
      *desc,
      mode,
      *preferredFormat,
      isBluetoothDevice,
      isDefaultDevice);
}

//  bool QAndroidAudioDevice::isBluetoothDevice() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAndroidAudioDevice17isBluetoothDeviceEv(
    const QAndroidAudioDevice *self) {
  return self->isBluetoothDevice();
}

//  QAndroidAudioDevice::~QAndroidAudioDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAndroidAudioDeviceD1Ev(QAndroidAudioDevice *self) {
  delete self;
}

#endif  // defined(Q_OS_ANDROID)
