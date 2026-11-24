//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiodevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const AudioDeviceFormat &lhs, const AudioDeviceFormat
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN19QAudioDevicePrivate17AudioDeviceFormatES2_(
    const QAudioDevicePrivate::AudioDeviceFormat *lhs,
    const QAudioDevicePrivate::AudioDeviceFormat *rhs) {
  return operator==(*lhs, *rhs);
}

//  QAudioDevicePrivate::AudioDeviceFormat::~AudioDeviceFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAudioDevicePrivate17AudioDeviceFormatD1Ev(
    QAudioDevicePrivate::AudioDeviceFormat *self) {
  delete self;
}
