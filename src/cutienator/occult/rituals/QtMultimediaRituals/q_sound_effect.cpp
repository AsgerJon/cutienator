//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qsoundeffect.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qsoundeffect.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSoundEffect that Python can take functions over in. Every QSoundEffect
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSoundEffectCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSoundEffectCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSoundEffectCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSoundEffect : public QSoundEffect {
public:
  using QSoundEffect::QSoundEffect;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSoundEffectCall0 call = reinterpret_cast<CuteQSoundEffectCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSoundEffectCall1 call = reinterpret_cast<CuteQSoundEffectCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSoundEffectCall2 call = reinterpret_cast<CuteQSoundEffectCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSoundEffectCall3 call = reinterpret_cast<CuteQSoundEffectCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSoundEffectCall4 call = reinterpret_cast<CuteQSoundEffectCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSoundEffectCall5 call = reinterpret_cast<CuteQSoundEffectCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSoundEffectCall6 call = reinterpret_cast<CuteQSoundEffectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSoundEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QSoundEffect10metaObjectEv(
    const QSoundEffect *self) {
  return self->metaObject();
}

//  QString QSoundEffect::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QSoundEffect2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSoundEffect::tr(s, c, n));
}

//  QSoundEffect::QSoundEffect(QObject *parent)
extern "C" Q_DECL_EXPORT
QSoundEffect *ritual_ZN12QSoundEffectC1EP7QObject(QObject *parent) {
  return new CuteQSoundEffect(parent);
}

//  QSoundEffect::QSoundEffect(const QAudioDevice &audioDevice, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QSoundEffect *ritual_ZN12QSoundEffectC1ERK12QAudioDeviceP7QObject(
    const QAudioDevice *audioDevice,
    QObject *parent) {
  return new CuteQSoundEffect(*audioDevice, parent);
}

//  QSoundEffect::~QSoundEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffectD1Ev(QSoundEffect *self) {
  delete self;
}

//  QStringList QSoundEffect::supportedMimeTypes()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN12QSoundEffect18supportedMimeTypesEv() {
  return new QList<QString>(QSoundEffect::supportedMimeTypes());
}

//  QUrl QSoundEffect::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK12QSoundEffect6sourceEv(const QSoundEffect *self) {
  return new QUrl(self->source());
}

//  void QSoundEffect::setSource(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect9setSourceERK4QUrl(
    QSoundEffect *self,
    const QUrl *url) {
  self->setSource(*url);
}

//  int QSoundEffect::loopCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSoundEffect9loopCountEv(const QSoundEffect *self) {
  return self->loopCount();
}

//  int QSoundEffect::loopsRemaining() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QSoundEffect14loopsRemainingEv(const QSoundEffect *self) {
  return self->loopsRemaining();
}

//  void QSoundEffect::setLoopCount(int loopCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect12setLoopCountEi(
    QSoundEffect *self,
    int loopCount) {
  self->setLoopCount(loopCount);
}

//  QAudioDevice QSoundEffect::audioDevice()
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZN12QSoundEffect11audioDeviceEv(QSoundEffect *self) {
  return new QAudioDevice(self->audioDevice());
}

//  void QSoundEffect::setAudioDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect14setAudioDeviceERK12QAudioDevice(
    QSoundEffect *self,
    const QAudioDevice *device) {
  self->setAudioDevice(*device);
}

//  float QSoundEffect::volume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QSoundEffect6volumeEv(const QSoundEffect *self) {
  return self->volume();
}

//  void QSoundEffect::setVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect9setVolumeEf(QSoundEffect *self, float volume) {
  self->setVolume(volume);
}

//  bool QSoundEffect::isMuted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSoundEffect7isMutedEv(const QSoundEffect *self) {
  return self->isMuted();
}

//  void QSoundEffect::setMuted(bool muted)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect8setMutedEb(QSoundEffect *self, bool muted) {
  self->setMuted(muted);
}

//  bool QSoundEffect::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSoundEffect8isLoadedEv(const QSoundEffect *self) {
  return self->isLoaded();
}

//  bool QSoundEffect::isPlaying() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSoundEffect9isPlayingEv(const QSoundEffect *self) {
  return self->isPlaying();
}

//  Status QSoundEffect::status() const
extern "C" Q_DECL_EXPORT
QSoundEffect::Status ritual_ZNK12QSoundEffect6statusEv(
    const QSoundEffect *self) {
  return self->status();
}

//  void QSoundEffect::play()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect4playEv(QSoundEffect *self) {
  self->play();
}

//  void QSoundEffect::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSoundEffect4stopEv(QSoundEffect *self) {
  self->stop();
}

//  QSoundEffectPrivate *QSoundEffect::d_func()
extern "C" Q_DECL_EXPORT
QSoundEffectPrivate *ritual_ZN12QSoundEffect6d_funcEv(QSoundEffect *self) {
  return self->d_func();
}

//  const QSoundEffectPrivate *QSoundEffect::d_func() const
extern "C" Q_DECL_EXPORT
const QSoundEffectPrivate *ritual_ZNK12QSoundEffect6d_funcEv(
    const QSoundEffect *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSoundEffect, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSoundEffect(
    QSoundEffect *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSoundEffect *>(self)->take(key, call);
}
