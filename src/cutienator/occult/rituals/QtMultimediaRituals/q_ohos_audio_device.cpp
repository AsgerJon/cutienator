//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qohosaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(ohaudio)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qohosaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qohosaudiodevice_p.h>
#include <QtMultimedia/private/qaudiodevice_p.h>
#include <QtMultimedia/private/qaudioformat_p.h>
#include <QtMultimedia/private/qohosaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/ohos/qohosaudiodevice.cpp, line 15, as local:qohosaudiodevice.cpp:createOhosAudioDeviceFormatFromPreferred
namespace {
inline QAudioDevicePrivate::AudioDeviceFormat
createOhosAudioDeviceFormatFromPreferred(const QAudioFormat &preferredFormat,
                                         int maximumChannelCount)
{
    QAudioDevicePrivate::AudioDeviceFormat format;

    format.preferredFormat = preferredFormat;

    // A mono stream is upmixed and the stream resamples, so only the maximum
    // channel count is taken from the device.
    format.minimumChannelCount = 1;
    format.maximumChannelCount = maximumChannelCount > 0 ? maximumChannelCount : 32;
    format.minimumSampleRate = QtMultimediaPrivate::allSupportedSampleRates.front();
    format.maximumSampleRate = QtMultimediaPrivate::allSupportedSampleRates.back();
    format.supportedSampleFormats = qAllSupportedSampleFormats();
    format.channelConfiguration = preferredFormat.channelConfig();

    return format;
}
}  // namespace

//  from ../qtmultimedia/src/multimedia/ohos/qohosaudiodevice.cpp, line 37, as _ZN16QOhosAudioDeviceC1E10QByteArray7QStringN12QAudioDevice4ModeE12QAudioFormatib
inline QOhosAudioDevice::QOhosAudioDevice(QByteArray id, QString description, QAudioDevice::Mode mode,
                                   QAudioFormat preferredFormat, int maximumChannelCount,
                                   bool isDefaultDevice)
    : QAudioDevicePrivate{ std::move(id), mode, std::move(description), isDefaultDevice,
                           createOhosAudioDeviceFormatFromPreferred(preferredFormat, maximumChannelCount) }
{
}
//  -----------------------------------------------------------------------

//  QOhosAudioDevice::QOhosAudioDevice(QByteArray id, QString description,
//      QAudioDevice::Mode mode, QAudioFormat preferredFormat, int
//      maximumChannelCount, bool isDefaultDevice)
extern "C" Q_DECL_EXPORT
QOhosAudioDevice *ritual_ZN16QOhosAudioDeviceC1E10QByteArray7QStringN12QAudioDevice4ModeE12QAudioFormatib(
    const QByteArray *id,
    const QString *description,
    QAudioDevice::Mode mode,
    const QAudioFormat *preferredFormat,
    int maximumChannelCount,
    bool isDefaultDevice) {
  return new QOhosAudioDevice(
      *id,
      *description,
      mode,
      *preferredFormat,
      maximumChannelCount,
      isDefaultDevice);
}

//  QOhosAudioDevice::~QOhosAudioDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOhosAudioDeviceD1Ev(QOhosAudioDevice *self) {
  delete self;
}

#endif  // QT_CONFIG(ohaudio)
