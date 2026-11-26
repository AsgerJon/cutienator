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
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/QAudioFormat>
#include <QtCore/QList>

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

//  QAudioDeviceExpected<AudioDeviceFormat> QAudioDevicePrivate::format()
//      const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<QAudioDevicePrivate::AudioDeviceFormat> *ritual_ZNK19QAudioDevicePrivate6formatEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<QAudioDevicePrivate::AudioDeviceFormat>(
      self->format());
}

//  QAudioDeviceExpected<QAudioFormat> QAudioDevicePrivate::preferredFormat()
//      const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<QAudioFormat> *ritual_ZNK19QAudioDevicePrivate15preferredFormatEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<QAudioFormat>(self->preferredFormat());
}

//  QAudioDeviceExpected<int> QAudioDevicePrivate::minimumSampleRate() const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<int> *ritual_ZNK19QAudioDevicePrivate17minimumSampleRateEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<int>(self->minimumSampleRate());
}

//  QAudioDeviceExpected<int> QAudioDevicePrivate::maximumSampleRate() const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<int> *ritual_ZNK19QAudioDevicePrivate17maximumSampleRateEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<int>(self->maximumSampleRate());
}

//  QAudioDeviceExpected<int> QAudioDevicePrivate::minimumChannelCount()
//      const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<int> *ritual_ZNK19QAudioDevicePrivate19minimumChannelCountEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<int>(self->minimumChannelCount());
}

//  QAudioDeviceExpected<int> QAudioDevicePrivate::maximumChannelCount()
//      const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<int> *ritual_ZNK19QAudioDevicePrivate19maximumChannelCountEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<int>(self->maximumChannelCount());
}

//  QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>>
//      QAudioDevicePrivate::supportedSampleFormats() const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>> *ritual_ZNK19QAudioDevicePrivate22supportedSampleFormatsEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>>(
      self->supportedSampleFormats());
}

//  QAudioDeviceExpected<QAudioFormat::ChannelConfig>
//      QAudioDevicePrivate::channelConfiguration() const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<QAudioFormat::ChannelConfig> *ritual_ZNK19QAudioDevicePrivate20channelConfigurationEv(
    const QAudioDevicePrivate *self) {
  return new QAudioDeviceExpected<QAudioFormat::ChannelConfig>(
      self->channelConfiguration());
}

//  QAudioDeviceExpected<bool> QAudioDevicePrivate::isFormatSupported(const
//      QAudioFormat &format) const
extern "C" Q_DECL_EXPORT
QAudioDeviceExpected<bool> *ritual_ZNK19QAudioDevicePrivate17isFormatSupportedERK12QAudioFormat(
    const QAudioDevicePrivate *self,
    const QAudioFormat *format) {
  return new QAudioDeviceExpected<bool>(self->isFormatSupported(*format));
}

//  const QAudioDevicePrivate *QAudioDevicePrivate::handle(const QAudioDevice
//      &device)
extern "C" Q_DECL_EXPORT
const QAudioDevicePrivate *ritual_ZN19QAudioDevicePrivate6handleERK12QAudioDevice(
    const QAudioDevice *device) {
  return QAudioDevicePrivate::handle(*device);
}

//  QAudioDevicePrivate *QAudioDevicePrivate::handle(QAudioDevice &device)
extern "C" Q_DECL_EXPORT
QAudioDevicePrivate *ritual_ZN19QAudioDevicePrivate6handleER12QAudioDevice(
    QAudioDevice *device) {
  return QAudioDevicePrivate::handle(*device);
}

//  QAudioDevicePrivate::QAudioDevicePrivate(const QAudioDevicePrivate &a0)
extern "C" Q_DECL_EXPORT
QAudioDevicePrivate *ritual_ZN19QAudioDevicePrivateC1ERKS_(
    const QAudioDevicePrivate *a0) {
  return new QAudioDevicePrivate(*a0);
}

//  a QAudioDeviceExpected<QAudioDevicePrivate::AudioDeviceFormat> a ritual
//      of QAudioDevicePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioDevicePrivate__QAudioDeviceExpected_QAudioDevicePrivate_AudioDeviceFormat(
    QAudioDeviceExpected<QAudioDevicePrivate::AudioDeviceFormat> *self) {
  delete self;
}

//  a QAudioDeviceExpected<QAudioFormat> a ritual of QAudioDevicePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioDevicePrivate__QAudioDeviceExpected_QAudioFormat(
    QAudioDeviceExpected<QAudioFormat> *self) {
  delete self;
}

//  a QAudioDeviceExpected<int> a ritual of QAudioDevicePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioDevicePrivate__QAudioDeviceExpected_int(
    QAudioDeviceExpected<int> *self) {
  delete self;
}

//  a QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>> a ritual of
//      QAudioDevicePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioDevicePrivate__QAudioDeviceExpected_QList_QAudioFormat_SampleFormat(
    QAudioDeviceExpected<QList<QAudioFormat::SampleFormat>> *self) {
  delete self;
}

//  a QAudioDeviceExpected<QAudioFormat::ChannelConfig> a ritual of
//      QAudioDevicePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioDevicePrivate__QAudioDeviceExpected_QAudioFormat_ChannelConfig(
    QAudioDeviceExpected<QAudioFormat::ChannelConfig> *self) {
  delete self;
}

//  a QAudioDeviceExpected<bool> a ritual of QAudioDevicePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAudioDevicePrivate__QAudioDeviceExpected_bool(
    QAudioDeviceExpected<bool> *self) {
  delete self;
}
