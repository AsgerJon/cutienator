//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformAudioEndpointBase that Python can take functions over in. Every QPlatformAudioEndpointBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPlatformAudioEndpointBaseCall0)(const void *, int *);
typedef void (*CuteQPlatformAudioEndpointBaseCall1)(const void *, int, int *);
typedef bool (*CuteQPlatformAudioEndpointBaseCall2)(const void *, const QAudioFormat *, int *);
typedef void (*CuteQPlatformAudioEndpointBaseCall3)(const void *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioEndpointBaseCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioEndpointBaseCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioEndpointBaseCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioEndpointBaseCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioEndpointBaseCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioEndpointBaseCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioEndpointBaseCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformAudioEndpointBase : public QPlatformAudioEndpointBase {
public:
  using QPlatformAudioEndpointBase::QPlatformAudioEndpointBase;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase5stateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase9setVolumeEf")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QAudio::State QPlatformAudioEndpointBase::state() const
  QAudio::State state() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall0 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAudio::State>(given);
    }
    return QPlatformAudioEndpointBase::state();
  }

  //  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
  void setError(QAudio::Error a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall1 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall1>(taken[1]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setError(a0);
  }

  //  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
  //      &format) const
  bool isFormatSupported(const QAudioFormat &format) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall2 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall2>(taken[2]);
      bool given = call(this, &format, &handled);
      if (handled) return given;
    }
    return QPlatformAudioEndpointBase::isFormatSupported(format);
  }

  //  void QPlatformAudioEndpointBase::setVolume(float volume)
  void setVolume(float volume) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall3 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall3>(taken[3]);
      call(this, volume, &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setVolume(volume);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall4 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall5 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall6 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall7 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall8 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall9 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformAudioEndpointBaseCall10 call = reinterpret_cast<CuteQPlatformAudioEndpointBaseCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformAudioEndpointBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QPlatformAudioEndpointBase10metaObjectEv(
    const QPlatformAudioEndpointBase *self) {
  return self->metaObject();
}

//  QString QPlatformAudioEndpointBase::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QPlatformAudioEndpointBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformAudioEndpointBase::tr(s, c, n));
}

//  QPlatformAudioEndpointBase::QPlatformAudioEndpointBase(QAudioDevice a0,
//      const QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioEndpointBase *ritual_ZN26QPlatformAudioEndpointBaseC1E12QAudioDeviceRK12QAudioFormatP7QObject(
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return new CuteQPlatformAudioEndpointBase(*a0, *a1, parent);
}

//  QPlatformAudioEndpointBase::~QPlatformAudioEndpointBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformAudioEndpointBaseD1Ev(
    QPlatformAudioEndpointBase *self) {
  delete self;
}

//  QAudio::Error QPlatformAudioEndpointBase::error() const
extern "C" Q_DECL_EXPORT
QAudio::Error ritual_ZNK26QPlatformAudioEndpointBase5errorEv(
    const QPlatformAudioEndpointBase *self) {
  return self->error();
}

//  QAudio::State QPlatformAudioEndpointBase::state() const
extern "C" Q_DECL_EXPORT
QAudio::State ritual_ZNK26QPlatformAudioEndpointBase5stateEv(
    const QPlatformAudioEndpointBase *self) {
  return self->state();
}

//  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE(
    QPlatformAudioEndpointBase *self,
    QAudio::Error a0) {
  self->setError(a0);
}

//  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
//      &format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat(
    const QPlatformAudioEndpointBase *self,
    const QAudioFormat *format) {
  return self->isFormatSupported(*format);
}

//  QAudioFormat QPlatformAudioEndpointBase::format() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK26QPlatformAudioEndpointBase6formatEv(
    const QPlatformAudioEndpointBase *self) {
  return new QAudioFormat(self->format());
}

//  void QPlatformAudioEndpointBase::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformAudioEndpointBase9setVolumeEf(
    QPlatformAudioEndpointBase *self,
    float volume) {
  self->setVolume(volume);
}

//  float QPlatformAudioEndpointBase::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QPlatformAudioEndpointBase6volumeEv(
    const QPlatformAudioEndpointBase *self) {
  return self->volume();
}

//  void QPlatformAudioEndpointBase::updateStreamState(QAudio::State a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformAudioEndpointBase17updateStreamStateEN6QAudio5StateE(
    QPlatformAudioEndpointBase *self,
    QAudio::State a0) {
  self->updateStreamState(a0);
}

//  void QPlatformAudioEndpointBase::updateStreamIdle(bool idle,
//      EmitStateSignal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformAudioEndpointBase16updateStreamIdleEbNS_15EmitStateSignalE(
    QPlatformAudioEndpointBase *self,
    bool idle,
    QPlatformAudioEndpointBase::EmitStateSignal a1) {
  self->updateStreamIdle(idle, a1);
}

//  void QPlatformAudioEndpointBase::inferState()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QPlatformAudioEndpointBase10inferStateEv(
    QPlatformAudioEndpointBase *self) {
  self->inferState();
}

//  a Python function taken by a CuteQPlatformAudioEndpointBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioEndpointBase(
    QPlatformAudioEndpointBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioEndpointBase *>(self)->take(key, call);
}

//  QAudio::State QPlatformAudioEndpointBase::state() const
extern "C" Q_DECL_EXPORT
QAudio::State ritual_own_ZNK26QPlatformAudioEndpointBase5stateEv(
    const QPlatformAudioEndpointBase *self) {
  return self->QPlatformAudioEndpointBase::state();
}

//  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE(
    QPlatformAudioEndpointBase *self,
    QAudio::Error a0) {
  self->QPlatformAudioEndpointBase::setError(a0);
}

//  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
//      &format) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat(
    const QPlatformAudioEndpointBase *self,
    const QAudioFormat *format) {
  return self->QPlatformAudioEndpointBase::isFormatSupported(*format);
}

//  void QPlatformAudioEndpointBase::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QPlatformAudioEndpointBase9setVolumeEf(
    QPlatformAudioEndpointBase *self,
    float volume) {
  self->QPlatformAudioEndpointBase::setVolume(volume);
}
