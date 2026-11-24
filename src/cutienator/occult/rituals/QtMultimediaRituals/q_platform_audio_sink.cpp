//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformAudioSink that Python can take functions over in. Every QPlatformAudioSink
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformAudioSinkCall0)(const void *, QIODevice *, int *);
typedef void * (*CuteQPlatformAudioSinkCall1)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall2)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall3)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall4)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall5)(const void *, int *);
typedef qsizetype (*CuteQPlatformAudioSinkCall6)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall7)(const void *, qsizetype, int *);
typedef qsizetype (*CuteQPlatformAudioSinkCall8)(const void *, int *);
typedef qint64 (*CuteQPlatformAudioSinkCall9)(const void *, int *);
typedef bool (*CuteQPlatformAudioSinkCall10)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall11)(const void *, int, int *);
typedef int (*CuteQPlatformAudioSinkCall12)(const void *, int *);
typedef void (*CuteQPlatformAudioSinkCall13)(const void *, int, int *);
typedef bool (*CuteQPlatformAudioSinkCall14)(const void *, const QAudioFormat *, int *);
typedef void (*CuteQPlatformAudioSinkCall15)(const void *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioSinkCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioSinkCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSinkCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSinkCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSinkCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSinkCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSinkCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformAudioSink : public QPlatformAudioSink {
public:
  using QPlatformAudioSink::QPlatformAudioSink;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink5startEP9QIODevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink5startEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink4stopEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink5resetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink7suspendEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink6resumeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QPlatformAudioSink9bytesFreeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink13setBufferSizeEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QPlatformAudioSink10bufferSizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QPlatformAudioSink14processedUSecsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink14hasCallbackAPIEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate17AudioEndpointRoleE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase5stateEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase9setVolumeEf")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPlatformAudioSink::start(QIODevice *device)
  void start(QIODevice *device) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall0 call = reinterpret_cast<CuteQPlatformAudioSinkCall0>(taken[0]);
      call(this, device, &handled);
      if (handled) return;
    }
  }

  //  QIODevice *QPlatformAudioSink::start()
  QIODevice *start() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall1 call = reinterpret_cast<CuteQPlatformAudioSinkCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  void QPlatformAudioSink::stop()
  void stop() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall2 call = reinterpret_cast<CuteQPlatformAudioSinkCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioSink::reset()
  void reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall3 call = reinterpret_cast<CuteQPlatformAudioSinkCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioSink::suspend()
  void suspend() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall4 call = reinterpret_cast<CuteQPlatformAudioSinkCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioSink::resume()
  void resume() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall5 call = reinterpret_cast<CuteQPlatformAudioSinkCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qsizetype QPlatformAudioSink::bytesFree() const
  qsizetype bytesFree() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall6 call = reinterpret_cast<CuteQPlatformAudioSinkCall6>(taken[6]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformAudioSink::setBufferSize(qsizetype value)
  void setBufferSize(qsizetype value) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall7 call = reinterpret_cast<CuteQPlatformAudioSinkCall7>(taken[7]);
      call(this, value, &handled);
      if (handled) return;
    }
  }

  //  qsizetype QPlatformAudioSink::bufferSize() const
  qsizetype bufferSize() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall8 call = reinterpret_cast<CuteQPlatformAudioSinkCall8>(taken[8]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QPlatformAudioSink::processedUSecs() const
  qint64 processedUSecs() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall9 call = reinterpret_cast<CuteQPlatformAudioSinkCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPlatformAudioSink::hasCallbackAPI()
  bool hasCallbackAPI() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall10 call = reinterpret_cast<CuteQPlatformAudioSinkCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioSink::hasCallbackAPI();
  }

  //  void QPlatformAudioSink::setRole(AudioEndpointRole a0)
  void setRole(QPlatformAudioSink::AudioEndpointRole a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall11 call = reinterpret_cast<CuteQPlatformAudioSinkCall11>(taken[11]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioSink::setRole(a0);
  }

  //  QAudio::State QPlatformAudioEndpointBase::state() const
  QAudio::State state() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall12 call = reinterpret_cast<CuteQPlatformAudioSinkCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAudio::State>(given);
    }
    return QPlatformAudioEndpointBase::state();
  }

  //  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
  void setError(QAudio::Error a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall13 call = reinterpret_cast<CuteQPlatformAudioSinkCall13>(taken[13]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setError(a0);
  }

  //  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
  //      &format) const
  bool isFormatSupported(const QAudioFormat &format) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall14 call = reinterpret_cast<CuteQPlatformAudioSinkCall14>(taken[14]);
      bool given = call(this, &format, &handled);
      if (handled) return given;
    }
    return QPlatformAudioEndpointBase::isFormatSupported(format);
  }

  //  void QPlatformAudioEndpointBase::setVolume(float volume)
  void setVolume(float volume) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall15 call = reinterpret_cast<CuteQPlatformAudioSinkCall15>(taken[15]);
      call(this, volume, &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setVolume(volume);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall16 call = reinterpret_cast<CuteQPlatformAudioSinkCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall17 call = reinterpret_cast<CuteQPlatformAudioSinkCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall18 call = reinterpret_cast<CuteQPlatformAudioSinkCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall19 call = reinterpret_cast<CuteQPlatformAudioSinkCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall20 call = reinterpret_cast<CuteQPlatformAudioSinkCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall21 call = reinterpret_cast<CuteQPlatformAudioSinkCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformAudioSinkCall22 call = reinterpret_cast<CuteQPlatformAudioSinkCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformAudioSink::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QPlatformAudioSink10metaObjectEv(
    const QPlatformAudioSink *self) {
  return self->metaObject();
}

//  QString QPlatformAudioSink::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QPlatformAudioSink2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformAudioSink::tr(s, c, n));
}

//  QPlatformAudioSink::~QPlatformAudioSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSinkD1Ev(QPlatformAudioSink *self) {
  delete self;
}

//  void QPlatformAudioSink::start(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink5startEP9QIODevice(
    QPlatformAudioSink *self,
    QIODevice *device) {
  self->start(device);
}

//  QIODevice *QPlatformAudioSink::start()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN18QPlatformAudioSink5startEv(QPlatformAudioSink *self) {
  return self->start();
}

//  void QPlatformAudioSink::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink4stopEv(QPlatformAudioSink *self) {
  self->stop();
}

//  void QPlatformAudioSink::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink5resetEv(QPlatformAudioSink *self) {
  self->reset();
}

//  void QPlatformAudioSink::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink7suspendEv(QPlatformAudioSink *self) {
  self->suspend();
}

//  void QPlatformAudioSink::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink6resumeEv(QPlatformAudioSink *self) {
  self->resume();
}

//  qsizetype QPlatformAudioSink::bytesFree() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QPlatformAudioSink9bytesFreeEv(
    const QPlatformAudioSink *self) {
  return self->bytesFree();
}

//  void QPlatformAudioSink::setBufferSize(qsizetype value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink13setBufferSizeEx(
    QPlatformAudioSink *self,
    qsizetype value) {
  self->setBufferSize(value);
}

//  qsizetype QPlatformAudioSink::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QPlatformAudioSink10bufferSizeEv(
    const QPlatformAudioSink *self) {
  return self->bufferSize();
}

//  qint64 QPlatformAudioSink::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK18QPlatformAudioSink14processedUSecsEv(
    const QPlatformAudioSink *self) {
  return self->processedUSecs();
}

//  bool QPlatformAudioSink::hasCallbackAPI()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QPlatformAudioSink14hasCallbackAPIEv(
    QPlatformAudioSink *self) {
  return self->hasCallbackAPI();
}

//  void QPlatformAudioSink::setRole(AudioEndpointRole a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate17AudioEndpointRoleE(
    QPlatformAudioSink *self,
    QPlatformAudioSink::AudioEndpointRole a0) {
  self->setRole(a0);
}

//  a Python function taken by a CuteQPlatformAudioSink, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioSink(
    QPlatformAudioSink *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioSink *>(self)->take(key, call);
}

//  bool QPlatformAudioSink::hasCallbackAPI()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QPlatformAudioSink14hasCallbackAPIEv(
    QPlatformAudioSink *self) {
  return self->QPlatformAudioSink::hasCallbackAPI();
}

//  void QPlatformAudioSink::setRole(AudioEndpointRole a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate17AudioEndpointRoleE(
    QPlatformAudioSink *self,
    QPlatformAudioSink::AudioEndpointRole a0) {
  self->QPlatformAudioSink::setRole(a0);
}
