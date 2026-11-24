//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsoundeffectwithplayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudioformat.h>

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
