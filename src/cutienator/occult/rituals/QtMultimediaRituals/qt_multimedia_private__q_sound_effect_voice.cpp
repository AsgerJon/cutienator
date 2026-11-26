//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, rituals for
//  functions the generator leaves out: 1. Kept as it is when the generator
//  runs again.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudioformat.h>
#include <memory>
#include <optional>
#include <QtMultimedia/QAudioFormat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/private/qsoundeffectwithplayer_p.h>
#include <QtCore/q20map.h>
#include <QtCore/qmutex.h>
#include <utility>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtmultimedia/src/multimedia/audio/qsoundeffectwithplayer.cpp, line 214, as _ZNK19QtMultimediaPrivate17QSoundEffectVoice5cloneESt8optionalI12QAudioFormatE
namespace QtMultimediaPrivate {
inline std::shared_ptr<QSoundEffectVoice>
QSoundEffectVoice::clone(std::optional<QAudioFormat> newEngineFormat) const
{
    auto clone = std::make_shared<QSoundEffectVoice>(QRtAudioEngine::allocateVoiceId(), m_sample,
                                                     m_volume, m_muted, loopsRemaining(),
                                                     newEngineFormat.value_or(m_engineFormat));

    // caveat: reading frame is not atomic, so we may have a race here ... is is rare, though,
    // not sure if we really care
    clone->m_currentFrame = m_currentFrame;
    return clone;
}
}  // namespace QtMultimediaPrivate
//  -----------------------------------------------------------------------

//  QtMultimediaPrivate::QSoundEffectVoice::~QSoundEffectVoice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate17QSoundEffectVoiceD1Ev(
    QtMultimediaPrivate::QSoundEffectVoice *self) {
  delete self;
}

//  const QAudioFormat &QtMultimediaPrivate::QSoundEffectVoice::format()
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZN19QtMultimediaPrivate17QSoundEffectVoice6formatEv(
    QtMultimediaPrivate::QSoundEffectVoice *self) {
  return new QAudioFormat(self->format());
}

//  int QtMultimediaPrivate::QSoundEffectVoice::loopsRemaining() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QtMultimediaPrivate17QSoundEffectVoice14loopsRemainingEv(
    const QtMultimediaPrivate::QSoundEffectVoice *self) {
  return self->loopsRemaining();
}

//  std::shared_ptr<QSoundEffectVoice>
//      QtMultimediaPrivate::QSoundEffectVoice::clone(std::optional<QAudioFor
//      mat> newEngineFormat) const
extern "C" Q_DECL_EXPORT
std::shared_ptr<QtMultimediaPrivate::QSoundEffectVoice> *ritual_ZNK19QtMultimediaPrivate17QSoundEffectVoice5cloneESt8optionalI12QAudioFormatE(
    const QtMultimediaPrivate::QSoundEffectVoice *self,
    const std::optional<QAudioFormat> *newEngineFormat) {
  return new std::shared_ptr<QtMultimediaPrivate::QSoundEffectVoice>(
      self->clone(
          *newEngineFormat));
}

//  a std::shared_ptr<QtMultimediaPrivate::QSoundEffectVoice> a ritual of
//      QtMultimediaPrivate::QSoundEffectVoice gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMultimediaPrivate_QSoundEffectVoice__std_shared_ptr_QtMultimediaPrivate_QSoundEffectVoice(
    std::shared_ptr<QtMultimediaPrivate::QSoundEffectVoice> *self) {
  delete self;
}

//  QtMultimediaPrivate::QSoundEffectVoice::QSoundEffectVoice(VoiceId
//      voiceId, std::shared_ptr<const QSample> sample, float volume, bool
//      muted, int totalLoopCount, QAudioFormat engineFormat)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QSoundEffectVoice *ritual_ZN19QtMultimediaPrivate17QSoundEffectVoiceC1ENS_7VoiceIdESt10shared_ptrIK7QSampleEfbi12QAudioFormat(
    unsigned long long voiceId,
    const std::shared_ptr<const QSample> *sample,
    float volume,
    bool muted,
    int totalLoopCount,
    const QAudioFormat *engineFormat) {
  return new QtMultimediaPrivate::QSoundEffectVoice(
      static_cast<QtMultimediaPrivate::VoiceId>(voiceId), *sample, volume,
      muted, totalLoopCount, *engineFormat);
}
