//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25, mended on 2026-11-26: added by hand,
//  instances of templates of the class: 4. Kept as it is when the generator
//  runs again. Also added by hand on 2026-11-25, rituals for functions the
//  generator leaves out: 1.
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

//  template <typename Lhs, typename Rhs>
//  bool QtMultimediaPrivate::QRtAudioEngineVoiceCompare::
//      operator()<QRtAudioEngineVoice, QRtAudioEngineVoice>(
//      const Lhs &lhs, const Rhs &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate26QRtAudioEngineVoiceCompareclINS_19QRtAudioEngineVoiceES2_EEbRKT_RKT0_(const QtMultimediaPrivate::QRtAudioEngineVoiceCompare *self,
    const QtMultimediaPrivate::QRtAudioEngineVoice *lhs,
    const QtMultimediaPrivate::QRtAudioEngineVoice *rhs) {
  using Voice = QtMultimediaPrivate::QRtAudioEngineVoice;
  return self->operator()<Voice, Voice>(*lhs, *rhs);
}

//  template <typename Lhs, typename Rhs>
//  bool QtMultimediaPrivate::QRtAudioEngineVoiceCompare::
//      operator()<std::shared_ptr<Voice>, std::shared_ptr<Voice>>(
//      const Lhs &lhs, const Rhs &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate26QRtAudioEngineVoiceCompareclISt10shared_ptrINS_19QRtAudioEngineVoiceEES4_EEbRKT_RKT0_(const QtMultimediaPrivate::QRtAudioEngineVoiceCompare *self,
    const std::shared_ptr<QtMultimediaPrivate::QRtAudioEngineVoice> *lhs, const std::shared_ptr<QtMultimediaPrivate::QRtAudioEngineVoice> *rhs) {
  using Voice = QtMultimediaPrivate::QRtAudioEngineVoice;
  using Shared = std::shared_ptr<Voice>;
  return self->operator()<Shared, Shared>(*lhs, *rhs);
}

//  template <typename Lhs, typename Rhs>
//  bool QtMultimediaPrivate::QRtAudioEngineVoiceCompare::
//      operator()<Voice, std::shared_ptr<Voice>>(
//      const Lhs &lhs, const Rhs &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate26QRtAudioEngineVoiceCompareclINS_19QRtAudioEngineVoiceESt10shared_ptrIS2_EEEbRKT_RKT0_(const QtMultimediaPrivate::QRtAudioEngineVoiceCompare *self,
    const QtMultimediaPrivate::QRtAudioEngineVoice *lhs, const std::shared_ptr<QtMultimediaPrivate::QRtAudioEngineVoice> *rhs) {
  using Voice = QtMultimediaPrivate::QRtAudioEngineVoice;
  using Shared = std::shared_ptr<Voice>;
  return self->operator()<Voice, Shared>(*lhs, *rhs);
}

//  template <typename Lhs, typename Rhs>
//  bool QtMultimediaPrivate::QRtAudioEngineVoiceCompare::
//      operator()<std::shared_ptr<Voice>, Voice>(
//      const Lhs &lhs, const Rhs &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate26QRtAudioEngineVoiceCompareclISt10shared_ptrINS_19QRtAudioEngineVoiceEES3_EEbRKT_RKT0_(const QtMultimediaPrivate::QRtAudioEngineVoiceCompare *self,
    const std::shared_ptr<QtMultimediaPrivate::QRtAudioEngineVoice> *lhs, const QtMultimediaPrivate::QRtAudioEngineVoice *rhs) {
  using Voice = QtMultimediaPrivate::QRtAudioEngineVoice;
  using Shared = std::shared_ptr<Voice>;
  return self->operator()<Shared, Voice>(*lhs, *rhs);
}

//  static uint64_t
//      QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(VoiceId arg)
extern "C" Q_DECL_EXPORT
unsigned long long ritual_ZN19QtMultimediaPrivate26QRtAudioEngineVoiceCompare5getIdENS_7VoiceIdE(
    unsigned long long arg) {
  return QtMultimediaPrivate::QRtAudioEngineVoiceCompare::getId(
      static_cast<QtMultimediaPrivate::VoiceId>(arg));
}
