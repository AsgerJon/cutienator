//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiodecoder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiodecoder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtMultimedia/qaudiobuffer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformAudioDecoder that Python can take functions over in. Every QPlatformAudioDecoder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QUrl * (*CuteQPlatformAudioDecoderCall0)(const void *, int *);
typedef void (*CuteQPlatformAudioDecoderCall1)(const void *, const QUrl *, int *);
typedef void * (*CuteQPlatformAudioDecoderCall2)(const void *, int *);
typedef void (*CuteQPlatformAudioDecoderCall3)(const void *, QIODevice *, int *);
typedef void (*CuteQPlatformAudioDecoderCall4)(const void *, int *);
typedef void (*CuteQPlatformAudioDecoderCall5)(const void *, int *);
typedef const QAudioFormat * (*CuteQPlatformAudioDecoderCall6)(const void *, int *);
typedef void (*CuteQPlatformAudioDecoderCall7)(const void *, const QAudioFormat *, int *);
typedef const QAudioBuffer * (*CuteQPlatformAudioDecoderCall8)(const void *, int *);
typedef bool (*CuteQPlatformAudioDecoderCall9)(const void *, int *);
typedef bool (*CuteQPlatformAudioDecoderCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioDecoderCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformAudioDecoderCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDecoderCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDecoderCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDecoderCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDecoderCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformAudioDecoderCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformAudioDecoder : public QPlatformAudioDecoder {
public:
  using QPlatformAudioDecoder::QPlatformAudioDecoder;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDecoder6sourceEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDecoder9setSourceERK4QUrl")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDecoder12sourceDeviceEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDecoder15setSourceDeviceEP9QIODevice")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDecoder5startEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDecoder4stopEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDecoder11audioFormatEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDecoder14setAudioFormatERK12QAudioFormat")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformAudioDecoder4readEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDecoder15bufferAvailableEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformAudioDecoder10canReadQrcEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QUrl QPlatformAudioDecoder::source() const
  QUrl source() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall0 call = reinterpret_cast<CuteQPlatformAudioDecoderCall0>(taken[0]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QPlatformAudioDecoder::setSource(const QUrl &fileName)
  void setSource(const QUrl &fileName) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall1 call = reinterpret_cast<CuteQPlatformAudioDecoderCall1>(taken[1]);
      call(this, &fileName, &handled);
      if (handled) return;
    }
  }

  //  QIODevice *QPlatformAudioDecoder::sourceDevice() const
  QIODevice *sourceDevice() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall2 call = reinterpret_cast<CuteQPlatformAudioDecoderCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  void QPlatformAudioDecoder::setSourceDevice(QIODevice *device)
  void setSourceDevice(QIODevice *device) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall3 call = reinterpret_cast<CuteQPlatformAudioDecoderCall3>(taken[3]);
      call(this, device, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioDecoder::start()
  void start() override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall4 call = reinterpret_cast<CuteQPlatformAudioDecoderCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformAudioDecoder::stop()
  void stop() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall5 call = reinterpret_cast<CuteQPlatformAudioDecoderCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QAudioFormat QPlatformAudioDecoder::audioFormat() const
  QAudioFormat audioFormat() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall6 call = reinterpret_cast<CuteQPlatformAudioDecoderCall6>(taken[6]);
      const QAudioFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QPlatformAudioDecoder::setAudioFormat(const QAudioFormat
  //      &format)
  void setAudioFormat(const QAudioFormat &format) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall7 call = reinterpret_cast<CuteQPlatformAudioDecoderCall7>(taken[7]);
      call(this, &format, &handled);
      if (handled) return;
    }
  }

  //  QAudioBuffer QPlatformAudioDecoder::read()
  QAudioBuffer read() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall8 call = reinterpret_cast<CuteQPlatformAudioDecoderCall8>(taken[8]);
      const QAudioBuffer * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QPlatformAudioDecoder::bufferAvailable() const
  bool bufferAvailable() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall9 call = reinterpret_cast<CuteQPlatformAudioDecoderCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioDecoder::bufferAvailable();
  }

  //  bool QPlatformAudioDecoder::canReadQrc() const
  bool canReadQrc() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall10 call = reinterpret_cast<CuteQPlatformAudioDecoderCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformAudioDecoder::canReadQrc();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall11 call = reinterpret_cast<CuteQPlatformAudioDecoderCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall12 call = reinterpret_cast<CuteQPlatformAudioDecoderCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall13 call = reinterpret_cast<CuteQPlatformAudioDecoderCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall14 call = reinterpret_cast<CuteQPlatformAudioDecoderCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall15 call = reinterpret_cast<CuteQPlatformAudioDecoderCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall16 call = reinterpret_cast<CuteQPlatformAudioDecoderCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformAudioDecoderCall17 call = reinterpret_cast<CuteQPlatformAudioDecoderCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformAudioDecoder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QPlatformAudioDecoder10metaObjectEv(
    const QPlatformAudioDecoder *self) {
  return self->metaObject();
}

//  void *QPlatformAudioDecoder::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QPlatformAudioDecoder11qt_metacastEPKc(
    QPlatformAudioDecoder *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformAudioDecoder::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QPlatformAudioDecoder11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformAudioDecoder *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformAudioDecoder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QPlatformAudioDecoder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformAudioDecoder::tr(s, c, n));
}

//  QUrl QPlatformAudioDecoder::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK21QPlatformAudioDecoder6sourceEv(
    const QPlatformAudioDecoder *self) {
  return new QUrl(self->source());
}

//  void QPlatformAudioDecoder::setSource(const QUrl &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder9setSourceERK4QUrl(
    QPlatformAudioDecoder *self,
    const QUrl *fileName) {
  self->setSource(*fileName);
}

//  QIODevice *QPlatformAudioDecoder::sourceDevice() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK21QPlatformAudioDecoder12sourceDeviceEv(
    const QPlatformAudioDecoder *self) {
  return self->sourceDevice();
}

//  void QPlatformAudioDecoder::setSourceDevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder15setSourceDeviceEP9QIODevice(
    QPlatformAudioDecoder *self,
    QIODevice *device) {
  self->setSourceDevice(device);
}

//  void QPlatformAudioDecoder::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder5startEv(QPlatformAudioDecoder *self) {
  self->start();
}

//  void QPlatformAudioDecoder::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder4stopEv(QPlatformAudioDecoder *self) {
  self->stop();
}

//  QAudioFormat QPlatformAudioDecoder::audioFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK21QPlatformAudioDecoder11audioFormatEv(
    const QPlatformAudioDecoder *self) {
  return new QAudioFormat(self->audioFormat());
}

//  void QPlatformAudioDecoder::setAudioFormat(const QAudioFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder14setAudioFormatERK12QAudioFormat(
    QPlatformAudioDecoder *self,
    const QAudioFormat *format) {
  self->setAudioFormat(*format);
}

//  QAudioBuffer QPlatformAudioDecoder::read()
extern "C" Q_DECL_EXPORT
QAudioBuffer *ritual_ZN21QPlatformAudioDecoder4readEv(
    QPlatformAudioDecoder *self) {
  return new QAudioBuffer(self->read());
}

//  bool QPlatformAudioDecoder::bufferAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformAudioDecoder15bufferAvailableEv(
    const QPlatformAudioDecoder *self) {
  return self->bufferAvailable();
}

//  std::chrono::milliseconds QPlatformAudioDecoder::position() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK21QPlatformAudioDecoder8positionEv(
    const QPlatformAudioDecoder *self) {
  return static_cast<long long>(self->position().count());
}

//  std::chrono::milliseconds QPlatformAudioDecoder::duration() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK21QPlatformAudioDecoder8durationEv(
    const QPlatformAudioDecoder *self) {
  return static_cast<long long>(self->duration().count());
}

//  void QPlatformAudioDecoder::formatChanged(const QAudioFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder13formatChangedERK12QAudioFormat(
    QPlatformAudioDecoder *self,
    const QAudioFormat *format) {
  self->formatChanged(*format);
}

//  void QPlatformAudioDecoder::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder13sourceChangedEv(
    QPlatformAudioDecoder *self) {
  self->sourceChanged();
}

//  void QPlatformAudioDecoder::error(QAudioDecoder::Error error, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder5errorEN13QAudioDecoder5ErrorERK7QString(
    QPlatformAudioDecoder *self,
    QAudioDecoder::Error error,
    const QString *errorString) {
  self->error(error, *errorString);
}

//  void QPlatformAudioDecoder::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder10clearErrorEv(
    QPlatformAudioDecoder *self) {
  self->clearError();
}

//  void QPlatformAudioDecoder::bufferReady()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder11bufferReadyEv(
    QPlatformAudioDecoder *self) {
  self->bufferReady();
}

//  void QPlatformAudioDecoder::bufferAvailableChanged(bool available)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder22bufferAvailableChangedEb(
    QPlatformAudioDecoder *self,
    bool available) {
  self->bufferAvailableChanged(available);
}

//  void QPlatformAudioDecoder::setIsDecoding(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder13setIsDecodingEb(
    QPlatformAudioDecoder *self,
    bool running) {
  self->setIsDecoding(running);
}

//  void QPlatformAudioDecoder::finished()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder8finishedEv(
    QPlatformAudioDecoder *self) {
  self->finished();
}

//  bool QPlatformAudioDecoder::isDecoding() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformAudioDecoder10isDecodingEv(
    const QPlatformAudioDecoder *self) {
  return self->isDecoding();
}

//  void QPlatformAudioDecoder::positionChanged(std::chrono::milliseconds a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder15positionChangedENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QPlatformAudioDecoder *self,
    long long a0) {
  self->positionChanged(std::chrono::milliseconds(a0));
}

//  void QPlatformAudioDecoder::durationChanged(std::chrono::milliseconds a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoder15durationChangedENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QPlatformAudioDecoder *self,
    long long a0) {
  self->durationChanged(std::chrono::milliseconds(a0));
}

//  QAudioDecoder::Error QPlatformAudioDecoder::error() const
extern "C" Q_DECL_EXPORT
QAudioDecoder::Error ritual_ZNK21QPlatformAudioDecoder5errorEv(
    const QPlatformAudioDecoder *self) {
  return self->error();
}

//  QString QPlatformAudioDecoder::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QPlatformAudioDecoder11errorStringEv(
    const QPlatformAudioDecoder *self) {
  return new QString(self->errorString());
}

//  bool QPlatformAudioDecoder::canReadQrc() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlatformAudioDecoder10canReadQrcEv(
    const QPlatformAudioDecoder *self) {
  return self->canReadQrc();
}

//  QPlatformAudioDecoder::~QPlatformAudioDecoder()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformAudioDecoderD1Ev(QPlatformAudioDecoder *self) {
  delete self;
}

//  QPlatformAudioDecoder::QPlatformAudioDecoder(QAudioDecoder *parent)
extern "C" Q_DECL_EXPORT
QPlatformAudioDecoder *ritual_ZN21QPlatformAudioDecoderC1EP13QAudioDecoder(
    QAudioDecoder *parent) {
  return new CuteQPlatformAudioDecoder(parent);
}

//  a Python function taken by a CuteQPlatformAudioDecoder, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformAudioDecoder(
    QPlatformAudioDecoder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformAudioDecoder *>(self)->take(key, call);
}

//  bool QPlatformAudioDecoder::bufferAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformAudioDecoder15bufferAvailableEv(
    const QPlatformAudioDecoder *self) {
  return self->QPlatformAudioDecoder::bufferAvailable();
}

//  bool QPlatformAudioDecoder::canReadQrc() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK21QPlatformAudioDecoder10canReadQrcEv(
    const QPlatformAudioDecoder *self) {
  return self->QPlatformAudioDecoder::canReadQrc();
}
