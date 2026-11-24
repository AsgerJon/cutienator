//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qrtaudioengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudioformat.h>
#include <cstring>

//  A QtMultimediaPrivate::QRtAudioEngineVoice that Python can take functions over in. Every QtMultimediaPrivate::QRtAudioEngineVoice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QAudioFormat * (*CuteQtMultimediaPrivate_QRtAudioEngineVoiceCall0)(const void *, int *);
class CuteQtMultimediaPrivate_QRtAudioEngineVoice : public QtMultimediaPrivate::QRtAudioEngineVoice {
public:
  using QtMultimediaPrivate::QRtAudioEngineVoice::QRtAudioEngineVoice;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QtMultimediaPrivate19QRtAudioEngineVoice6formatEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  const QAudioFormat
  //      &QtMultimediaPrivate::QRtAudioEngineVoice::format()
  const QAudioFormat &format() noexcept override {
    if (taken[0]) {
      int handled = 0;
      CuteQtMultimediaPrivate_QRtAudioEngineVoiceCall0 call = reinterpret_cast<CuteQtMultimediaPrivate_QRtAudioEngineVoiceCall0>(taken[0]);
      const QAudioFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QtMultimediaPrivate::QRtAudioEngineVoice::~QRtAudioEngineVoice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate19QRtAudioEngineVoiceD1Ev(
    QtMultimediaPrivate::QRtAudioEngineVoice *self) {
  delete self;
}

//  const QAudioFormat &QtMultimediaPrivate::QRtAudioEngineVoice::format()
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZN19QtMultimediaPrivate19QRtAudioEngineVoice6formatEv(
    QtMultimediaPrivate::QRtAudioEngineVoice *self) {
  return new QAudioFormat(self->format());
}

//  a Python function taken by a CuteQtMultimediaPrivate_QRtAudioEngineVoice,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtMultimediaPrivate_QRtAudioEngineVoice(
    QtMultimediaPrivate::QRtAudioEngineVoice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtMultimediaPrivate_QRtAudioEngineVoice *>(self)->take(key, call);
}
