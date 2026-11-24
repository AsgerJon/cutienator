//  Written by dev_tooling.RitualGenerator from the records of QtMultimedia/6
//  .12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_platform_stream_support_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QtMultimediaPrivate::QPlatformAudioSourceStream that Python can take functions over in. Every QtMultimediaPrivate::QPlatformAudioSourceStream
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQtMultimediaPrivate_QPlatformAudioSourceStreamCall0)(const void *, bool, int *);
class CuteQtMultimediaPrivate_QPlatformAudioSourceStream : public QtMultimediaPrivate::QPlatformAudioSourceStream {
public:
  using QtMultimediaPrivate::QPlatformAudioSourceStream::QPlatformAudioSourceStream;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream16updateStreamIdleEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QtMultimediaPrivate::QPlatformAudioSourceStream::updateStreamIdl
  //      e(bool a0)
  void updateStreamIdle(bool a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQtMultimediaPrivate_QPlatformAudioSourceStreamCall0 call = reinterpret_cast<CuteQtMultimediaPrivate_QPlatformAudioSourceStreamCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
};

//  void
//      QtMultimediaPrivate::QPlatformAudioSourceStream::updateStreamIdle(boo
//      l a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate26QPlatformAudioSourceStream16updateStreamIdleEb(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    bool a0) {
  self->updateStreamIdle(a0);
}

//  a Python function taken by a
//      CuteQtMultimediaPrivate_QPlatformAudioSourceStream, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtMultimediaPrivate_QPlatformAudioSourceStream(
    QtMultimediaPrivate::QPlatformAudioSourceStream *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtMultimediaPrivate_QPlatformAudioSourceStream *>(self)->take(key, call);
}
