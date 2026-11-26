//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  uint64_t QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const
//      QRtAudioEngineVoice &arg)
extern "C" Q_DECL_EXPORT
uint64_t ritual_ZN19QtMultimediaPrivate26QRtAudioEngineVoiceCompare5getIdERKNS_19QRtAudioEngineVoiceE(
    const QtMultimediaPrivate::QRtAudioEngineVoice *arg) {
  return QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(*arg);
}

//  uint64_t QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(const
//      std::shared_ptr<QRtAudioEngineVoice> &arg)
extern "C" Q_DECL_EXPORT
uint64_t ritual_ZN19QtMultimediaPrivate26QRtAudioEngineVoiceCompare5getIdERKSt10shared_ptrINS_19QRtAudioEngineVoiceEE(
    const std::shared_ptr<QtMultimediaPrivate::QRtAudioEngineVoice> *arg) {
  return QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(*arg);
}

//  QtMultimediaPrivate::QRtAudioEngineVoiceCompare::~QRtAudioEngineVoiceComp
//      are()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QRtAudioEngineVoiceCompareD1Ev(
    QtMultimediaPrivate::QRtAudioEngineVoiceCompare *self) {
  delete self;
}
