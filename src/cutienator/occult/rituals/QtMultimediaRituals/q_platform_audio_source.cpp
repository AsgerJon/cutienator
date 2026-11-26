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
#include <optional>

//  A QPlatformAudioSource that Python can take functions over in. Every QPlatformAudioSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformAudioSourceCall0)(const void *, QIODevice *, int *);
typedef void * (*CuteQPlatformAudioSourceCall1)(const void *, int *);
typedef void (*CuteQPlatformAudioSourceCall2)(const void *, int *);
typedef void (*CuteQPlatformAudioSourceCall3)(const void *, int *);
typedef void (*CuteQPlatformAudioSourceCall4)(const void *, int *);
typedef void (*CuteQPlatformAudioSourceCall5)(const void *, int *);
typedef qsizetype (*CuteQPlatformAudioSourceCall6)(const void *, int *);
typedef void (*CuteQPlatformAudioSourceCall7)(const void *, qsizetype, int *);
typedef qsizetype (*CuteQPlatformAudioSourceCall8)(const void *, int *);
typedef qint64 (*CuteQPlatformAudioSourceCall9)(const void *, int *);
typedef bool (*CuteQPlatformAudioSourceCall10)(const void *, int *);
typedef int (*CuteQPlatformAudioSourceCall11)(const void *, int *);
typedef void (*CuteQPlatformAudioSourceCall12)(const void *, int, int *);
typedef bool (*CuteQPlatformAudioSourceCall13)(const void *, const QAudioFormat *, int *);
typedef void (*CuteQPlatformAudioSourceCall14)(const void *, float, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioSourceCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioSourceCall16)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSourceCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSourceCall18)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSourceCall19)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSourceCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioSourceCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformAudioSource : public QPlatformAudioSource {
public:
  using QPlatformAudioSource::QPlatformAudioSource;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource5startEP9QIODevice")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource5startEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource4stopEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource5resetEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource7suspendEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource6resumeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformAudioSource10bytesReadyEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource13setBufferSizeEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformAudioSource10bufferSizeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformAudioSource14processedUSecsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformAudioSource14hasCallbackAPIEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase5stateEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase8setErrorEN6QAudio5ErrorE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK26QPlatformAudioEndpointBase17isFormatSupportedERK12QAudioFormat")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QPlatformAudioEndpointBase9setVolumeEf")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPlatformAudioSource::start(QIODevice *device)
  void start(QIODevice *device) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall0 call = reinterpret_cast<CuteQPlatformAudioSourceCall0>(taken[0]);
      call(this, device, &handled);
      if (handled) return;
    }
  }

  //  QIODevice *QPlatformAudioSource::start()
  QIODevice *start() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall1 call = reinterpret_cast<CuteQPlatformAudioSourceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  void QPlatformAudioSource::stop()
  void stop() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall2 call = reinterpret_cast<CuteQPlatformAudioSourceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioSource::reset()
  void reset() override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall3 call = reinterpret_cast<CuteQPlatformAudioSourceCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioSource::suspend()
  void suspend() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall4 call = reinterpret_cast<CuteQPlatformAudioSourceCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioSource::resume()
  void resume() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall5 call = reinterpret_cast<CuteQPlatformAudioSourceCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qsizetype QPlatformAudioSource::bytesReady() const
  qsizetype bytesReady() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall6 call = reinterpret_cast<CuteQPlatformAudioSourceCall6>(taken[6]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformAudioSource::setBufferSize(qsizetype value)
  void setBufferSize(qsizetype value) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall7 call = reinterpret_cast<CuteQPlatformAudioSourceCall7>(taken[7]);
      call(this, value, &handled);
      if (handled) return;
    }
  }

  //  qsizetype QPlatformAudioSource::bufferSize() const
  qsizetype bufferSize() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall8 call = reinterpret_cast<CuteQPlatformAudioSourceCall8>(taken[8]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QPlatformAudioSource::processedUSecs() const
  qint64 processedUSecs() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall9 call = reinterpret_cast<CuteQPlatformAudioSourceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPlatformAudioSource::hasCallbackAPI()
  bool hasCallbackAPI() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall10 call = reinterpret_cast<CuteQPlatformAudioSourceCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioSource::hasCallbackAPI();
  }

  //  QAudio::State QPlatformAudioEndpointBase::state() const
  QAudio::State state() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall11 call = reinterpret_cast<CuteQPlatformAudioSourceCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAudio::State>(given);
    }
    return QPlatformAudioEndpointBase::state();
  }

  //  void QPlatformAudioEndpointBase::setError(QAudio::Error a0)
  void setError(QAudio::Error a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall12 call = reinterpret_cast<CuteQPlatformAudioSourceCall12>(taken[12]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setError(a0);
  }

  //  bool QPlatformAudioEndpointBase::isFormatSupported(const QAudioFormat
  //      &format) const
  bool isFormatSupported(const QAudioFormat &format) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall13 call = reinterpret_cast<CuteQPlatformAudioSourceCall13>(taken[13]);
      bool given = call(this, &format, &handled);
      if (handled) return given;
    }
    return QPlatformAudioEndpointBase::isFormatSupported(format);
  }

  //  void QPlatformAudioEndpointBase::setVolume(float volume)
  void setVolume(float volume) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall14 call = reinterpret_cast<CuteQPlatformAudioSourceCall14>(taken[14]);
      call(this, volume, &handled);
      if (handled) return;
    }
    QPlatformAudioEndpointBase::setVolume(volume);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall15 call = reinterpret_cast<CuteQPlatformAudioSourceCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall16 call = reinterpret_cast<CuteQPlatformAudioSourceCall16>(taken[16]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall17 call = reinterpret_cast<CuteQPlatformAudioSourceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall18 call = reinterpret_cast<CuteQPlatformAudioSourceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall19 call = reinterpret_cast<CuteQPlatformAudioSourceCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall20 call = reinterpret_cast<CuteQPlatformAudioSourceCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformAudioSourceCall21 call = reinterpret_cast<CuteQPlatformAudioSourceCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformAudioSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QPlatformAudioSource10metaObjectEv(
    const QPlatformAudioSource *self) {
  return self->metaObject();
}

//  void *QPlatformAudioSource::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QPlatformAudioSource11qt_metacastEPKc(
    QPlatformAudioSource *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformAudioSource::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QPlatformAudioSource11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformAudioSource *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformAudioSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QPlatformAudioSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformAudioSource::tr(s, c, n));
}

//  QPlatformAudioSource::QPlatformAudioSource(QAudioDevice a0, const
//      QAudioFormat &a1, QObject *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN20QPlatformAudioSourceC1E12QAudioDeviceRK12QAudioFormatP7QObject(
    const QAudioDevice *a0,
    const QAudioFormat *a1,
    QObject *parent) {
  return new CuteQPlatformAudioSource(*a0, *a1, parent);
}

//  QPlatformAudioSource::~QPlatformAudioSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSourceD1Ev(QPlatformAudioSource *self) {
  delete self;
}

//  void QPlatformAudioSource::start(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource5startEP9QIODevice(
    QPlatformAudioSource *self,
    QIODevice *device) {
  self->start(device);
}

//  QIODevice *QPlatformAudioSource::start()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN20QPlatformAudioSource5startEv(
    QPlatformAudioSource *self) {
  return self->start();
}

//  void QPlatformAudioSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource4stopEv(QPlatformAudioSource *self) {
  self->stop();
}

//  void QPlatformAudioSource::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource5resetEv(QPlatformAudioSource *self) {
  self->reset();
}

//  void QPlatformAudioSource::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource7suspendEv(QPlatformAudioSource *self) {
  self->suspend();
}

//  void QPlatformAudioSource::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource6resumeEv(QPlatformAudioSource *self) {
  self->resume();
}

//  qsizetype QPlatformAudioSource::bytesReady() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QPlatformAudioSource10bytesReadyEv(
    const QPlatformAudioSource *self) {
  return self->bytesReady();
}

//  void QPlatformAudioSource::setBufferSize(qsizetype value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource13setBufferSizeEx(
    QPlatformAudioSource *self,
    qsizetype value) {
  self->setBufferSize(value);
}

//  void QPlatformAudioSource::setNativePeriodFrames(std::optional<NativePeri
//      odFrames> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource21setNativePeriodFramesESt8optionalIN19QtMultimediaPrivate18NativePeriodFramesEE(
    QPlatformAudioSource *self,
    const std::optional<QPlatformAudioEndpointBase::NativePeriodFrames> *a0) {
  self->setNativePeriodFrames(*a0);
}

//  std::optional<NativePeriodFrames>
//      QPlatformAudioSource::nativePeriodFrames()
extern "C" Q_DECL_EXPORT
std::optional<QPlatformAudioEndpointBase::NativePeriodFrames> *ritual_ZN20QPlatformAudioSource18nativePeriodFramesEv(
    QPlatformAudioSource *self) {
  return new std::optional<QPlatformAudioEndpointBase::NativePeriodFrames>(
      self->nativePeriodFrames());
}

//  qsizetype QPlatformAudioSource::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK20QPlatformAudioSource10bufferSizeEv(
    const QPlatformAudioSource *self) {
  return self->bufferSize();
}

//  qint64 QPlatformAudioSource::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QPlatformAudioSource14processedUSecsEv(
    const QPlatformAudioSource *self) {
  return self->processedUSecs();
}

//  void QPlatformAudioSource::start(AudioCallback &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformAudioSource5startEOSt7variantIJSt8functionIFv5QSpanIKfLm18446744073709551615EEEES1_IFvS2_IKhLm18446744073709551615EEEES1_IFvS2_IKsLm18446744073709551615EEEES1_IFvS2_IKiLm18446744073709551615EEEEEE(
    QPlatformAudioSource *self,
    QPlatformAudioSource::AudioCallback *a0) {
  self->start(std::move(*a0));
}

//  bool QPlatformAudioSource::hasCallbackAPI()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QPlatformAudioSource14hasCallbackAPIEv(
    QPlatformAudioSource *self) {
  return self->hasCallbackAPI();
}

//  QPlatformAudioSource *QPlatformAudioSource::get(const QAudioSource &a0)
extern "C" Q_DECL_EXPORT
QPlatformAudioSource *ritual_ZN20QPlatformAudioSource3getERK12QAudioSource(
    const QAudioSource *a0) {
  return QPlatformAudioSource::get(*a0);
}

//  a Python function taken by a CuteQPlatformAudioSource, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioSource(
    QPlatformAudioSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioSource *>(self)->take(key, call);
}

//  bool QPlatformAudioSource::hasCallbackAPI()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QPlatformAudioSource14hasCallbackAPIEv(
    QPlatformAudioSource *self) {
  return self->QPlatformAudioSource::hasCallbackAPI();
}

//  a std::optional<QPlatformAudioEndpointBase::NativePeriodFrames> a ritual
//      of QPlatformAudioSource gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QPlatformAudioSource__std_optional_QPlatformAudioEndpointBase_NativePeriodFrames(
    std::optional<QPlatformAudioEndpointBase::NativePeriodFrames> *self) {
  delete self;
}
