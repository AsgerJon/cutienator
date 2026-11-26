//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/qaudioengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/qaudioengine.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioEngine that Python can take functions over in. Every QAudioEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioEngine : public QAudioEngine {
public:
  using QAudioEngine::QAudioEngine;
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
      CuteQAudioEngineCall0 call = reinterpret_cast<CuteQAudioEngineCall0>(taken[0]);
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
      CuteQAudioEngineCall1 call = reinterpret_cast<CuteQAudioEngineCall1>(taken[1]);
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
      CuteQAudioEngineCall2 call = reinterpret_cast<CuteQAudioEngineCall2>(taken[2]);
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
      CuteQAudioEngineCall3 call = reinterpret_cast<CuteQAudioEngineCall3>(taken[3]);
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
      CuteQAudioEngineCall4 call = reinterpret_cast<CuteQAudioEngineCall4>(taken[4]);
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
      CuteQAudioEngineCall5 call = reinterpret_cast<CuteQAudioEngineCall5>(taken[5]);
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
      CuteQAudioEngineCall6 call = reinterpret_cast<CuteQAudioEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QAudioEngine10metaObjectEv(
    const QAudioEngine *self) {
  return self->metaObject();
}

//  void *QAudioEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QAudioEngine11qt_metacastEPKc(
    QAudioEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAudioEngine::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QAudioEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QAudioEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAudioEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QAudioEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioEngine::tr(s, c, n));
}

//  QAudioEngine::QAudioEngine()
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZN12QAudioEngineC1Ev() {
  return new CuteQAudioEngine();
}

//  QAudioEngine::QAudioEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZN12QAudioEngineC1EP7QObject(QObject *parent) {
  return new CuteQAudioEngine(parent);
}

//  QAudioEngine::QAudioEngine(int sampleRate, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioEngine *ritual_ZN12QAudioEngineC1EiP7QObject(
    int sampleRate,
    QObject *parent) {
  return new CuteQAudioEngine(sampleRate, parent);
}

//  QAudioEngine::~QAudioEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngineD1Ev(QAudioEngine *self) {
  delete self;
}

//  void QAudioEngine::setOutputMode(OutputMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine13setOutputModeENS_10OutputModeE(
    QAudioEngine *self,
    QAudioEngine::OutputMode mode) {
  self->setOutputMode(mode);
}

//  OutputMode QAudioEngine::outputMode() const
extern "C" Q_DECL_EXPORT
QAudioEngine::OutputMode ritual_ZNK12QAudioEngine10outputModeEv(
    const QAudioEngine *self) {
  return self->outputMode();
}

//  int QAudioEngine::sampleRate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QAudioEngine10sampleRateEv(const QAudioEngine *self) {
  return self->sampleRate();
}

//  void QAudioEngine::setOutputDevice(const QAudioDevice &device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine15setOutputDeviceERK12QAudioDevice(
    QAudioEngine *self,
    const QAudioDevice *device) {
  self->setOutputDevice(*device);
}

//  QAudioDevice QAudioEngine::outputDevice() const
extern "C" Q_DECL_EXPORT
QAudioDevice *ritual_ZNK12QAudioEngine12outputDeviceEv(
    const QAudioEngine *self) {
  return new QAudioDevice(self->outputDevice());
}

//  void QAudioEngine::setMasterVolume(float volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine15setMasterVolumeEf(
    QAudioEngine *self,
    float volume) {
  self->setMasterVolume(volume);
}

//  float QAudioEngine::masterVolume() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QAudioEngine12masterVolumeEv(const QAudioEngine *self) {
  return self->masterVolume();
}

//  void QAudioEngine::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine9setPausedEb(QAudioEngine *self, bool paused) {
  self->setPaused(paused);
}

//  bool QAudioEngine::paused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioEngine6pausedEv(const QAudioEngine *self) {
  return self->paused();
}

//  void QAudioEngine::setRoomEffectsEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine21setRoomEffectsEnabledEb(
    QAudioEngine *self,
    bool enabled) {
  self->setRoomEffectsEnabled(enabled);
}

//  bool QAudioEngine::roomEffectsEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioEngine18roomEffectsEnabledEv(
    const QAudioEngine *self) {
  return self->roomEffectsEnabled();
}

//  void QAudioEngine::setDistanceScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine16setDistanceScaleEf(
    QAudioEngine *self,
    float scale) {
  self->setDistanceScale(scale);
}

//  float QAudioEngine::distanceScale() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QAudioEngine13distanceScaleEv(const QAudioEngine *self) {
  return self->distanceScale();
}

//  void QAudioEngine::outputModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine17outputModeChangedEv(QAudioEngine *self) {
  self->outputModeChanged();
}

//  void QAudioEngine::outputDeviceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine19outputDeviceChangedEv(QAudioEngine *self) {
  self->outputDeviceChanged();
}

//  void QAudioEngine::masterVolumeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine19masterVolumeChangedEv(QAudioEngine *self) {
  self->masterVolumeChanged();
}

//  void QAudioEngine::pausedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine13pausedChangedEv(QAudioEngine *self) {
  self->pausedChanged();
}

//  void QAudioEngine::distanceScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine20distanceScaleChangedEv(QAudioEngine *self) {
  self->distanceScaleChanged();
}

//  void QAudioEngine::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine5startEv(QAudioEngine *self) {
  self->start();
}

//  void QAudioEngine::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine4stopEv(QAudioEngine *self) {
  self->stop();
}

//  void QAudioEngine::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine5pauseEv(QAudioEngine *self) {
  self->pause();
}

//  void QAudioEngine::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioEngine6resumeEv(QAudioEngine *self) {
  self->resume();
}

//  QAudioEnginePrivate *QAudioEngine::d_func()
extern "C" Q_DECL_EXPORT
QAudioEnginePrivate *ritual_ZN12QAudioEngine6d_funcEv(QAudioEngine *self) {
  return self->d_func();
}

//  const QAudioEnginePrivate *QAudioEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QAudioEnginePrivate *ritual_ZNK12QAudioEngine6d_funcEv(
    const QAudioEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAudioEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioEngine(
    QAudioEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioEngine *>(self)->take(key, call);
}
