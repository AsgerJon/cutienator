//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiosink.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudiosink.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioSink that Python can take functions over in. Every QAudioSink
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioSinkCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioSinkCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSinkCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSinkCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSinkCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSinkCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSinkCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioSink : public QAudioSink {
public:
  using QAudioSink::QAudioSink;
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
      CuteQAudioSinkCall0 call = reinterpret_cast<CuteQAudioSinkCall0>(taken[0]);
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
      CuteQAudioSinkCall1 call = reinterpret_cast<CuteQAudioSinkCall1>(taken[1]);
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
      CuteQAudioSinkCall2 call = reinterpret_cast<CuteQAudioSinkCall2>(taken[2]);
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
      CuteQAudioSinkCall3 call = reinterpret_cast<CuteQAudioSinkCall3>(taken[3]);
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
      CuteQAudioSinkCall4 call = reinterpret_cast<CuteQAudioSinkCall4>(taken[4]);
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
      CuteQAudioSinkCall5 call = reinterpret_cast<CuteQAudioSinkCall5>(taken[5]);
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
      CuteQAudioSinkCall6 call = reinterpret_cast<CuteQAudioSinkCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioSink::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QAudioSink10metaObjectEv(
    const QAudioSink *self) {
  return self->metaObject();
}

//  void *QAudioSink::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QAudioSink11qt_metacastEPKc(
    QAudioSink *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAudioSink::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QAudioSink11qt_metacallEN11QMetaObject4CallEiPPv(
    QAudioSink *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAudioSink::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QAudioSink2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioSink::tr(s, c, n));
}

//  QAudioSink::QAudioSink(const QAudioFormat &format, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioSink *ritual_ZN10QAudioSinkC1ERK12QAudioFormatP7QObject(
    const QAudioFormat *format,
    QObject *parent) {
  return new CuteQAudioSink(*format, parent);
}

//  QAudioSink::QAudioSink(const QAudioDevice &audioDeviceInfo, const
//      QAudioFormat &format, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioSink *ritual_ZN10QAudioSinkC1ERK12QAudioDeviceRK12QAudioFormatP7QObject(
    const QAudioDevice *audioDeviceInfo,
    const QAudioFormat *format,
    QObject *parent) {
  return new CuteQAudioSink(*audioDeviceInfo, *format, parent);
}

//  QAudioSink::~QAudioSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSinkD1Ev(QAudioSink *self) {
  delete self;
}

//  bool QAudioSink::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QAudioSink6isNullEv(const QAudioSink *self) {
  return self->isNull();
}

//  QAudioFormat QAudioSink::format() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK10QAudioSink6formatEv(const QAudioSink *self) {
  return new QAudioFormat(self->format());
}

//  void QAudioSink::start(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink5startEP9QIODevice(
    QAudioSink *self,
    QIODevice *device) {
  self->start(device);
}

//  QIODevice *QAudioSink::start()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN10QAudioSink5startEv(QAudioSink *self) {
  return self->start();
}

//  void QAudioSink::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink4stopEv(QAudioSink *self) {
  self->stop();
}

//  void QAudioSink::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink5resetEv(QAudioSink *self) {
  self->reset();
}

//  void QAudioSink::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink7suspendEv(QAudioSink *self) {
  self->suspend();
}

//  void QAudioSink::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink6resumeEv(QAudioSink *self) {
  self->resume();
}

//  void QAudioSink::setBufferSize(qsizetype bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink13setBufferSizeEx(
    QAudioSink *self,
    qsizetype bytes) {
  self->setBufferSize(bytes);
}

//  qsizetype QAudioSink::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QAudioSink10bufferSizeEv(const QAudioSink *self) {
  return self->bufferSize();
}

//  void QAudioSink::setBufferFrameCount(qsizetype framesCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink19setBufferFrameCountEx(
    QAudioSink *self,
    qsizetype framesCount) {
  self->setBufferFrameCount(framesCount);
}

//  qsizetype QAudioSink::bufferFrameCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QAudioSink16bufferFrameCountEv(
    const QAudioSink *self) {
  return self->bufferFrameCount();
}

//  void QAudioSink::setNativePeriodFrameCount(qsizetype frameCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink25setNativePeriodFrameCountEx(
    QAudioSink *self,
    qsizetype frameCount) {
  self->setNativePeriodFrameCount(frameCount);
}

//  qsizetype QAudioSink::nativePeriodFrameCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QAudioSink22nativePeriodFrameCountEv(
    const QAudioSink *self) {
  return self->nativePeriodFrameCount();
}

//  qsizetype QAudioSink::bytesFree() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QAudioSink9bytesFreeEv(const QAudioSink *self) {
  return self->bytesFree();
}

//  qsizetype QAudioSink::framesFree() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10QAudioSink10framesFreeEv(const QAudioSink *self) {
  return self->framesFree();
}

//  qint64 QAudioSink::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QAudioSink14processedUSecsEv(const QAudioSink *self) {
  return self->processedUSecs();
}

//  qint64 QAudioSink::elapsedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QAudioSink12elapsedUSecsEv(const QAudioSink *self) {
  return self->elapsedUSecs();
}

//  QtAudio::Error QAudioSink::error() const
extern "C" Q_DECL_EXPORT
QtAudio::Error ritual_ZNK10QAudioSink5errorEv(const QAudioSink *self) {
  return self->error();
}

//  QtAudio::State QAudioSink::state() const
extern "C" Q_DECL_EXPORT
QtAudio::State ritual_ZNK10QAudioSink5stateEv(const QAudioSink *self) {
  return self->state();
}

//  void QAudioSink::setVolume(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink9setVolumeEd(QAudioSink *self, qreal a0) {
  self->setVolume(a0);
}

//  qreal QAudioSink::volume() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QAudioSink6volumeEv(const QAudioSink *self) {
  return self->volume();
}

#if !(defined(Q_QDOC))
//  void QAudioSink::stateChanged(QAudio::State state)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink12stateChangedEN6QAudio5StateE(
    QAudioSink *self,
    QAudio::State state) {
  self->stateChanged(state);
}
#endif  // !(defined(Q_QDOC))

//  void QAudioSink::startABIImpl(QtAudioPrivate::AudioSinkCallback &&a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioSink12startABIImplEOSt7variantIJSt8functionIFv5QSpanIfLm18446744073709551615EEEES1_IFvS2_IhLm18446744073709551615EEEES1_IFvS2_IsLm18446744073709551615EEEES1_IFvS2_IiLm18446744073709551615EEEEEE(
    QAudioSink *self,
    QtAudioPrivate::AudioSinkCallback *a0) {
  self->startABIImpl(std::move(*a0));
}

//  a Python function taken by a CuteQAudioSink, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioSink(QAudioSink *self, const char *key, void *call) {
  return static_cast<CuteQAudioSink *>(self)->take(key, call);
}
