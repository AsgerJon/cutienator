//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudioinput_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudioinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <cstring>

//  A QPlatformAudioInput that Python can take functions over in. Every QPlatformAudioInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformAudioInputCall0)(const void *, const QAudioDevice *, int *);
typedef void (*CuteQPlatformAudioInputCall1)(const void *, bool, int *);
typedef void (*CuteQPlatformAudioInputCall2)(const void *, float, int *);
class CuteQPlatformAudioInput : public QPlatformAudioInput {
public:
  using QPlatformAudioInput::QPlatformAudioInput;
  CuteQPlatformAudioInput(const QPlatformAudioInput & other) : QPlatformAudioInput(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPlatformAudioInput14setAudioDeviceERK12QAudioDevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlatformAudioInput8setMutedEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPlatformAudioInput9setVolumeEf")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QPlatformAudioInput::setAudioDevice(const QAudioDevice &a0)
  void setAudioDevice(const QAudioDevice &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioInputCall0 call = reinterpret_cast<CuteQPlatformAudioInputCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QPlatformAudioInput::setAudioDevice(a0);
  }

  //  void QPlatformAudioInput::setMuted(bool a0)
  void setMuted(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioInputCall1 call = reinterpret_cast<CuteQPlatformAudioInputCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformAudioInput::setMuted(a0);
  }

  //  void QPlatformAudioInput::setVolume(float a0)
  void setVolume(float a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioInputCall2 call = reinterpret_cast<CuteQPlatformAudioInputCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformAudioInput::setVolume(a0);
  }
};

//  QPlatformAudioInput::QPlatformAudioInput(QAudioInput *qq)
extern "C" Q_DECL_EXPORT
QPlatformAudioInput *ritual_ZN19QPlatformAudioInputC1EP11QAudioInput(
    QAudioInput *qq) {
  return new CuteQPlatformAudioInput(qq);
}

//  QPlatformAudioInput::~QPlatformAudioInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlatformAudioInputD1Ev(QPlatformAudioInput *self) {
  delete self;
}

//  void QPlatformAudioInput::setAudioDevice(const QAudioDevice &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlatformAudioInput14setAudioDeviceERK12QAudioDevice(
    QPlatformAudioInput *self,
    const QAudioDevice *a0) {
  self->setAudioDevice(*a0);
}

//  void QPlatformAudioInput::setMuted(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlatformAudioInput8setMutedEb(
    QPlatformAudioInput *self,
    bool a0) {
  self->setMuted(a0);
}

//  void QPlatformAudioInput::setVolume(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPlatformAudioInput9setVolumeEf(
    QPlatformAudioInput *self,
    float a0) {
  self->setVolume(a0);
}

//  a Python function taken by a CuteQPlatformAudioInput, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioInput(
    QPlatformAudioInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioInput *>(self)->take(key, call);
}

//  void QPlatformAudioInput::setAudioDevice(const QAudioDevice &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPlatformAudioInput14setAudioDeviceERK12QAudioDevice(
    QPlatformAudioInput *self,
    const QAudioDevice *a0) {
  self->QPlatformAudioInput::setAudioDevice(*a0);
}

//  void QPlatformAudioInput::setMuted(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPlatformAudioInput8setMutedEb(
    QPlatformAudioInput *self,
    bool a0) {
  self->QPlatformAudioInput::setMuted(a0);
}

//  void QPlatformAudioInput::setVolume(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPlatformAudioInput9setVolumeEf(
    QPlatformAudioInput *self,
    float a0) {
  self->QPlatformAudioInput::setVolume(a0);
}
