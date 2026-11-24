//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiosource.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudiosource.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiodevice.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioSource that Python can take functions over in. Every QAudioSource
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioSourceCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioSourceCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSourceCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSourceCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSourceCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSourceCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioSourceCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioSource : public QAudioSource {
public:
  using QAudioSource::QAudioSource;
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
      CuteQAudioSourceCall0 call = reinterpret_cast<CuteQAudioSourceCall0>(taken[0]);
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
      CuteQAudioSourceCall1 call = reinterpret_cast<CuteQAudioSourceCall1>(taken[1]);
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
      CuteQAudioSourceCall2 call = reinterpret_cast<CuteQAudioSourceCall2>(taken[2]);
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
      CuteQAudioSourceCall3 call = reinterpret_cast<CuteQAudioSourceCall3>(taken[3]);
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
      CuteQAudioSourceCall4 call = reinterpret_cast<CuteQAudioSourceCall4>(taken[4]);
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
      CuteQAudioSourceCall5 call = reinterpret_cast<CuteQAudioSourceCall5>(taken[5]);
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
      CuteQAudioSourceCall6 call = reinterpret_cast<CuteQAudioSourceCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioSource::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QAudioSource10metaObjectEv(
    const QAudioSource *self) {
  return self->metaObject();
}

//  QString QAudioSource::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QAudioSource2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioSource::tr(s, c, n));
}

//  QAudioSource::QAudioSource(const QAudioFormat &format, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioSource *ritual_ZN12QAudioSourceC1ERK12QAudioFormatP7QObject(
    const QAudioFormat *format,
    QObject *parent) {
  return new CuteQAudioSource(*format, parent);
}

//  QAudioSource::QAudioSource(const QAudioDevice &audioDeviceInfo, const
//      QAudioFormat &format, QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioSource *ritual_ZN12QAudioSourceC1ERK12QAudioDeviceRK12QAudioFormatP7QObject(
    const QAudioDevice *audioDeviceInfo,
    const QAudioFormat *format,
    QObject *parent) {
  return new CuteQAudioSource(*audioDeviceInfo, *format, parent);
}

//  QAudioSource::~QAudioSource()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSourceD1Ev(QAudioSource *self) {
  delete self;
}

//  bool QAudioSource::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QAudioSource6isNullEv(const QAudioSource *self) {
  return self->isNull();
}

//  QAudioFormat QAudioSource::format() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK12QAudioSource6formatEv(const QAudioSource *self) {
  return new QAudioFormat(self->format());
}

//  void QAudioSource::start(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource5startEP9QIODevice(
    QAudioSource *self,
    QIODevice *device) {
  self->start(device);
}

//  QIODevice *QAudioSource::start()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN12QAudioSource5startEv(QAudioSource *self) {
  return self->start();
}

//  void QAudioSource::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource4stopEv(QAudioSource *self) {
  self->stop();
}

//  void QAudioSource::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource5resetEv(QAudioSource *self) {
  self->reset();
}

//  void QAudioSource::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource7suspendEv(QAudioSource *self) {
  self->suspend();
}

//  void QAudioSource::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource6resumeEv(QAudioSource *self) {
  self->resume();
}

//  void QAudioSource::setBufferSize(qsizetype bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource13setBufferSizeEx(
    QAudioSource *self,
    qsizetype bytes) {
  self->setBufferSize(bytes);
}

//  qsizetype QAudioSource::bufferSize() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioSource10bufferSizeEv(const QAudioSource *self) {
  return self->bufferSize();
}

//  void QAudioSource::setBufferFrameCount(qsizetype frames)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource19setBufferFrameCountEx(
    QAudioSource *self,
    qsizetype frames) {
  self->setBufferFrameCount(frames);
}

//  qsizetype QAudioSource::bufferFrameCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioSource16bufferFrameCountEv(
    const QAudioSource *self) {
  return self->bufferFrameCount();
}

//  void QAudioSource::setNativePeriodFrameCount(qsizetype frameCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource25setNativePeriodFrameCountEx(
    QAudioSource *self,
    qsizetype frameCount) {
  self->setNativePeriodFrameCount(frameCount);
}

//  qsizetype QAudioSource::nativePeriodFrameCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioSource22nativePeriodFrameCountEv(
    const QAudioSource *self) {
  return self->nativePeriodFrameCount();
}

//  qsizetype QAudioSource::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioSource14bytesAvailableEv(
    const QAudioSource *self) {
  return self->bytesAvailable();
}

//  qsizetype QAudioSource::framesAvailable() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK12QAudioSource15framesAvailableEv(
    const QAudioSource *self) {
  return self->framesAvailable();
}

//  void QAudioSource::setVolume(qreal volume)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QAudioSource9setVolumeEd(QAudioSource *self, qreal volume) {
  self->setVolume(volume);
}

//  qreal QAudioSource::volume() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QAudioSource6volumeEv(const QAudioSource *self) {
  return self->volume();
}

//  qint64 QAudioSource::processedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QAudioSource14processedUSecsEv(const QAudioSource *self) {
  return self->processedUSecs();
}

//  qint64 QAudioSource::elapsedUSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QAudioSource12elapsedUSecsEv(const QAudioSource *self) {
  return self->elapsedUSecs();
}

//  QtAudio::Error QAudioSource::error() const
extern "C" Q_DECL_EXPORT
QtAudio::Error ritual_ZNK12QAudioSource5errorEv(const QAudioSource *self) {
  return self->error();
}

//  QtAudio::State QAudioSource::state() const
extern "C" Q_DECL_EXPORT
QtAudio::State ritual_ZNK12QAudioSource5stateEv(const QAudioSource *self) {
  return self->state();
}

//  a Python function taken by a CuteQAudioSource, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioSource(
    QAudioSource *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioSource *>(self)->take(key, call);
}
