//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiooutput_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiooutput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qaudiodevice.h>
#include <cstring>

//  A QPlatformAudioOutput that Python can take functions over in. Every QPlatformAudioOutput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformAudioOutputCall0)(const void *, const QAudioDevice *, int *);
typedef void (*CuteQPlatformAudioOutputCall1)(const void *, bool, int *);
typedef void (*CuteQPlatformAudioOutputCall2)(const void *, float, int *);
class CuteQPlatformAudioOutput : public QPlatformAudioOutput {
public:
  using QPlatformAudioOutput::QPlatformAudioOutput;
  CuteQPlatformAudioOutput(const QPlatformAudioOutput & other) : QPlatformAudioOutput(other) {}
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QPlatformAudioOutput14setAudioDeviceERK12QAudioDevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioOutput8setMutedEb")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioOutput9setVolumeEf")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QPlatformAudioOutput::setAudioDevice(const QAudioDevice &a0)
  void setAudioDevice(const QAudioDevice &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioOutputCall0 call = reinterpret_cast<CuteQPlatformAudioOutputCall0>(taken[0]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QPlatformAudioOutput::setAudioDevice(a0);
  }

  //  void QPlatformAudioOutput::setMuted(bool a0)
  void setMuted(bool a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioOutputCall1 call = reinterpret_cast<CuteQPlatformAudioOutputCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformAudioOutput::setMuted(a0);
  }

  //  void QPlatformAudioOutput::setVolume(float a0)
  void setVolume(float a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioOutputCall2 call = reinterpret_cast<CuteQPlatformAudioOutputCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QPlatformAudioOutput::setVolume(a0);
  }
};

//  QPlatformAudioOutput::QPlatformAudioOutput(QAudioOutput *qq)
extern "C" Q_DECL_EXPORT
QPlatformAudioOutput *ritual_ZN20QPlatformAudioOutputC1EP12QAudioOutput(
    QAudioOutput *qq) {
  return new CuteQPlatformAudioOutput(qq);
}

//  QPlatformAudioOutput::~QPlatformAudioOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioOutputD1Ev(QPlatformAudioOutput *self) {
  delete self;
}

//  void QPlatformAudioOutput::setAudioDevice(const QAudioDevice &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioOutput14setAudioDeviceERK12QAudioDevice(
    QPlatformAudioOutput *self,
    const QAudioDevice *a0) {
  self->setAudioDevice(*a0);
}

//  void QPlatformAudioOutput::setMuted(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioOutput8setMutedEb(
    QPlatformAudioOutput *self,
    bool a0) {
  self->setMuted(a0);
}

//  void QPlatformAudioOutput::setVolume(float a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioOutput9setVolumeEf(
    QPlatformAudioOutput *self,
    float a0) {
  self->setVolume(a0);
}

//  a Python function taken by a CuteQPlatformAudioOutput, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioOutput(
    QPlatformAudioOutput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioOutput *>(self)->take(key, call);
}

//  void QPlatformAudioOutput::setAudioDevice(const QAudioDevice &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformAudioOutput14setAudioDeviceERK12QAudioDevice(
    QPlatformAudioOutput *self,
    const QAudioDevice *a0) {
  self->QPlatformAudioOutput::setAudioDevice(*a0);
}

//  void QPlatformAudioOutput::setMuted(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformAudioOutput8setMutedEb(
    QPlatformAudioOutput *self,
    bool a0) {
  self->QPlatformAudioOutput::setMuted(a0);
}

//  void QPlatformAudioOutput::setVolume(float a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformAudioOutput9setVolumeEf(
    QPlatformAudioOutput *self,
    float a0) {
  self->QPlatformAudioOutput::setVolume(a0);
}
