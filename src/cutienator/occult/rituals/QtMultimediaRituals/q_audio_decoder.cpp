//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qaudiodecoder.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qaudiodecoder.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioDecoder that Python can take functions over in. Every QAudioDecoder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioDecoderCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioDecoderCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioDecoderCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioDecoderCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioDecoderCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioDecoderCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioDecoderCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioDecoder : public QAudioDecoder {
public:
  using QAudioDecoder::QAudioDecoder;
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
      CuteQAudioDecoderCall0 call = reinterpret_cast<CuteQAudioDecoderCall0>(taken[0]);
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
      CuteQAudioDecoderCall1 call = reinterpret_cast<CuteQAudioDecoderCall1>(taken[1]);
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
      CuteQAudioDecoderCall2 call = reinterpret_cast<CuteQAudioDecoderCall2>(taken[2]);
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
      CuteQAudioDecoderCall3 call = reinterpret_cast<CuteQAudioDecoderCall3>(taken[3]);
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
      CuteQAudioDecoderCall4 call = reinterpret_cast<CuteQAudioDecoderCall4>(taken[4]);
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
      CuteQAudioDecoderCall5 call = reinterpret_cast<CuteQAudioDecoderCall5>(taken[5]);
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
      CuteQAudioDecoderCall6 call = reinterpret_cast<CuteQAudioDecoderCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioDecoder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QAudioDecoder10metaObjectEv(
    const QAudioDecoder *self) {
  return self->metaObject();
}

//  QString QAudioDecoder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QAudioDecoder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioDecoder::tr(s, c, n));
}

//  QAudioDecoder::QAudioDecoder(QObject *parent)
extern "C" Q_DECL_EXPORT
QAudioDecoder *ritual_ZN13QAudioDecoderC1EP7QObject(QObject *parent) {
  return new CuteQAudioDecoder(parent);
}

//  QAudioDecoder::~QAudioDecoder()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAudioDecoderD1Ev(QAudioDecoder *self) {
  delete self;
}

//  bool QAudioDecoder::isSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAudioDecoder11isSupportedEv(const QAudioDecoder *self) {
  return self->isSupported();
}

//  bool QAudioDecoder::isDecoding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAudioDecoder10isDecodingEv(const QAudioDecoder *self) {
  return self->isDecoding();
}

//  QUrl QAudioDecoder::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13QAudioDecoder6sourceEv(const QAudioDecoder *self) {
  return new QUrl(self->source());
}

//  void QAudioDecoder::setSource(const QUrl &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAudioDecoder9setSourceERK4QUrl(
    QAudioDecoder *self,
    const QUrl *fileName) {
  self->setSource(*fileName);
}

//  QIODevice *QAudioDecoder::sourceDevice() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK13QAudioDecoder12sourceDeviceEv(
    const QAudioDecoder *self) {
  return self->sourceDevice();
}

//  void QAudioDecoder::setSourceDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAudioDecoder15setSourceDeviceEP9QIODevice(
    QAudioDecoder *self,
    QIODevice *device) {
  self->setSourceDevice(device);
}

//  QAudioFormat QAudioDecoder::audioFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK13QAudioDecoder11audioFormatEv(
    const QAudioDecoder *self) {
  return new QAudioFormat(self->audioFormat());
}

//  void QAudioDecoder::setAudioFormat(const QAudioFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAudioDecoder14setAudioFormatERK12QAudioFormat(
    QAudioDecoder *self,
    const QAudioFormat *format) {
  self->setAudioFormat(*format);
}

//  QString QAudioDecoder::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QAudioDecoder11errorStringEv(
    const QAudioDecoder *self) {
  return new QString(self->errorString());
}

//  QAudioBuffer QAudioDecoder::read() const
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZNK13QAudioDecoder4readEv(const QAudioDecoder *self) {
  return new QAudioBuffer(self->read());
}

//  bool QAudioDecoder::bufferAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QAudioDecoder15bufferAvailableEv(
    const QAudioDecoder *self) {
  return self->bufferAvailable();
}

//  qint64 QAudioDecoder::position() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QAudioDecoder8positionEv(const QAudioDecoder *self) {
  return self->position();
}

//  qint64 QAudioDecoder::duration() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QAudioDecoder8durationEv(const QAudioDecoder *self) {
  return self->duration();
}

//  void QAudioDecoder::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAudioDecoder5startEv(QAudioDecoder *self) {
  self->start();
}

//  void QAudioDecoder::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAudioDecoder4stopEv(QAudioDecoder *self) {
  self->stop();
}

//  QAudioDecoderPrivate *QAudioDecoder::d_func()
extern "C" Q_DECL_EXPORT
QAudioDecoderPrivate *ritual_ZN13QAudioDecoder6d_funcEv(
    QAudioDecoder *self) {
  return self->d_func();
}

//  const QAudioDecoderPrivate *QAudioDecoder::d_func() const
extern "C" Q_DECL_EXPORT
const QAudioDecoderPrivate *ritual_ZNK13QAudioDecoder6d_funcEv(
    const QAudioDecoder *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAudioDecoder, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioDecoder(
    QAudioDecoder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAudioDecoder *>(self)->take(key, call);
}
