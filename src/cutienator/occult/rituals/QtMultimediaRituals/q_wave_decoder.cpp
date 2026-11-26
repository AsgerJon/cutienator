//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qwavedecoder.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the function 'open' of QIODevice is
//  taken out of the Cute class, with its key. QWaveDecoder declares its
//  own 'open', which the class already has, and the compiler refused the
//  second as a redeclared member. The slot 'taken[8]' stays, unused.
//  Kept as it is when the generator runs again.
#include <QtMultimedia/qtmultimediaglobal.h>
#if QT_DEPRECATED_SINCE(6, 11)
#include <QtMultimedia/qwavedecoder.h>
#include <QtCore/qstring.h>
#include <QtMultimedia/qaudioformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QWaveDecoder that Python can take functions over in. Every QWaveDecoder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_DEPRECATED_SINCE(6, 11)
typedef bool (*CuteQWaveDecoderCall0)(const void *, int, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef void (*CuteQWaveDecoderCall1)(const void *, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef bool (*CuteQWaveDecoderCall2)(const void *, qint64, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef qint64 (*CuteQWaveDecoderCall3)(const void *, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef qint64 (*CuteQWaveDecoderCall4)(const void *, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef bool (*CuteQWaveDecoderCall5)(const void *, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef qint64 (*CuteQWaveDecoderCall6)(const void *, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
typedef qint64 (*CuteQWaveDecoderCall7)(const void *, char *, qint64, int *);
#endif  // QT_DEPRECATED_SINCE(6, 11)
typedef bool (*CuteQWaveDecoderCall8)(const void *, int, int *);
typedef bool (*CuteQWaveDecoderCall9)(const void *, int *);
typedef bool (*CuteQWaveDecoderCall10)(const void *, int *);
typedef qint64 (*CuteQWaveDecoderCall11)(const void *, int *);
typedef bool (*CuteQWaveDecoderCall12)(const void *, int *);
typedef bool (*CuteQWaveDecoderCall13)(const void *, int, int *);
typedef bool (*CuteQWaveDecoderCall14)(const void *, int, int *);
typedef qint64 (*CuteQWaveDecoderCall15)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQWaveDecoderCall16)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaveDecoderCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaveDecoderCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaveDecoderCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaveDecoderCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaveDecoderCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaveDecoderCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaveDecoderCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaveDecoder : public QWaveDecoder {
public:
  using QWaveDecoder::QWaveDecoder;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZN12QWaveDecoder4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
#if QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_DEPRECATED_SINCE(6, 11)
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_DEPRECATED_SINCE(6, 11)
  //  bool QWaveDecoder::open(QIODevice::OpenMode mode)
  bool open(QIODevice::OpenMode mode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaveDecoderCall0 call = reinterpret_cast<CuteQWaveDecoderCall0>(taken[0]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QWaveDecoder::open(mode);
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  void QWaveDecoder::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaveDecoderCall1 call = reinterpret_cast<CuteQWaveDecoderCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWaveDecoder::close();
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  bool QWaveDecoder::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaveDecoderCall2 call = reinterpret_cast<CuteQWaveDecoderCall2>(taken[2]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QWaveDecoder::seek(pos);
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  qint64 QWaveDecoder::pos() const
  qint64 pos() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaveDecoderCall3 call = reinterpret_cast<CuteQWaveDecoderCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QWaveDecoder::pos();
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  qint64 QWaveDecoder::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaveDecoderCall4 call = reinterpret_cast<CuteQWaveDecoderCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QWaveDecoder::size();
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  bool QWaveDecoder::isSequential() const
  bool isSequential() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaveDecoderCall5 call = reinterpret_cast<CuteQWaveDecoderCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWaveDecoder::isSequential();
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  qint64 QWaveDecoder::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaveDecoderCall6 call = reinterpret_cast<CuteQWaveDecoderCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QWaveDecoder::bytesAvailable();
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
  //  qint64 QWaveDecoder::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaveDecoderCall7 call = reinterpret_cast<CuteQWaveDecoderCall7>(taken[7]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QWaveDecoder::readData(data, maxlen);
  }
#endif  // QT_DEPRECATED_SINCE(6, 11)

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaveDecoderCall9 call = reinterpret_cast<CuteQWaveDecoderCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaveDecoderCall10 call = reinterpret_cast<CuteQWaveDecoderCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaveDecoderCall11 call = reinterpret_cast<CuteQWaveDecoderCall11>(taken[11]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQWaveDecoderCall12 call = reinterpret_cast<CuteQWaveDecoderCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWaveDecoderCall13 call = reinterpret_cast<CuteQWaveDecoderCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWaveDecoderCall14 call = reinterpret_cast<CuteQWaveDecoderCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWaveDecoderCall15 call = reinterpret_cast<CuteQWaveDecoderCall15>(taken[15]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWaveDecoderCall16 call = reinterpret_cast<CuteQWaveDecoderCall16>(taken[16]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWaveDecoderCall17 call = reinterpret_cast<CuteQWaveDecoderCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWaveDecoderCall18 call = reinterpret_cast<CuteQWaveDecoderCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWaveDecoderCall19 call = reinterpret_cast<CuteQWaveDecoderCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWaveDecoderCall20 call = reinterpret_cast<CuteQWaveDecoderCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWaveDecoderCall21 call = reinterpret_cast<CuteQWaveDecoderCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWaveDecoderCall22 call = reinterpret_cast<CuteQWaveDecoderCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWaveDecoderCall23 call = reinterpret_cast<CuteQWaveDecoderCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaveDecoder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QWaveDecoder10metaObjectEv(
    const QWaveDecoder *self) {
  return self->metaObject();
}

//  void *QWaveDecoder::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QWaveDecoder11qt_metacastEPKc(
    QWaveDecoder *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QWaveDecoder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QWaveDecoder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaveDecoder::tr(s, c, n));
}

//  QWaveDecoder::QWaveDecoder(QIODevice *device, QObject *parent)
extern "C" Q_DECL_EXPORT
QWaveDecoder *ritual_ZN12QWaveDecoderC1EP9QIODeviceP7QObject(
    QIODevice *device,
    QObject *parent) {
  return new CuteQWaveDecoder(device, parent);
}

//  QWaveDecoder::QWaveDecoder(QIODevice *device, const QAudioFormat &format,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QWaveDecoder *ritual_ZN12QWaveDecoderC1EP9QIODeviceRK12QAudioFormatP7QObject(
    QIODevice *device,
    const QAudioFormat *format,
    QObject *parent) {
  return new CuteQWaveDecoder(device, *format, parent);
}

//  QWaveDecoder::~QWaveDecoder()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaveDecoderD1Ev(QWaveDecoder *self) {
  delete self;
}

//  QAudioFormat QWaveDecoder::audioFormat() const
extern "C" Q_DECL_EXPORT
QAudioFormat *ritual_ZNK12QWaveDecoder11audioFormatEv(
    const QWaveDecoder *self) {
  return new QAudioFormat(self->audioFormat());
}

//  QIODevice *QWaveDecoder::getDevice()
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN12QWaveDecoder9getDeviceEv(QWaveDecoder *self) {
  return self->getDevice();
}

//  int QWaveDecoder::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QWaveDecoder8durationEv(const QWaveDecoder *self) {
  return self->duration();
}

//  qint64 QWaveDecoder::headerLength()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QWaveDecoder12headerLengthEv() {
  return QWaveDecoder::headerLength();
}

//  bool QWaveDecoder::open(QIODevice::OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QWaveDecoder4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QWaveDecoder *self,
    int mode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QWaveDecoder::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaveDecoder5closeEv(QWaveDecoder *self) {
  self->close();
}

//  bool QWaveDecoder::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QWaveDecoder4seekEx(QWaveDecoder *self, qint64 pos) {
  return self->seek(pos);
}

//  qint64 QWaveDecoder::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QWaveDecoder3posEv(const QWaveDecoder *self) {
  return self->pos();
}

//  void QWaveDecoder::setIODevice(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaveDecoder11setIODeviceEP9QIODevice(
    QWaveDecoder *self,
    QIODevice *device) {
  self->setIODevice(device);
}

//  qint64 QWaveDecoder::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QWaveDecoder4sizeEv(const QWaveDecoder *self) {
  return self->size();
}

//  bool QWaveDecoder::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaveDecoder12isSequentialEv(const QWaveDecoder *self) {
  return self->isSequential();
}

//  qint64 QWaveDecoder::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QWaveDecoder14bytesAvailableEv(const QWaveDecoder *self) {
  return self->bytesAvailable();
}

//  void QWaveDecoder::handleData()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaveDecoder10handleDataEv(QWaveDecoder *self) {
  self->handleData();
}

//  qint64 QWaveDecoder::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QWaveDecoder8readDataEPcx(
    QWaveDecoder *self,
    char *data,
    qint64 maxlen) {
  return self->readData(data, maxlen);
}

//  qint64 QWaveDecoder::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QWaveDecoder9writeDataEPKcx(
    QWaveDecoder *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  bool QWaveDecoder::writeHeader()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QWaveDecoder11writeHeaderEv(QWaveDecoder *self) {
  return self->writeHeader();
}

//  bool QWaveDecoder::writeDataLength()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QWaveDecoder15writeDataLengthEv(QWaveDecoder *self) {
  return self->writeDataLength();
}

//  void QWaveDecoder::parsingFailed()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaveDecoder13parsingFailedEv(QWaveDecoder *self) {
  self->parsingFailed();
}

//  a Python function taken by a CuteQWaveDecoder, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaveDecoder(
    QWaveDecoder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaveDecoder *>(self)->take(key, call);
}

//  bool QWaveDecoder::open(QIODevice::OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QWaveDecoder4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QWaveDecoder *self,
    int mode) {
  return self->QWaveDecoder::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QWaveDecoder::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QWaveDecoder5closeEv(QWaveDecoder *self) {
  self->QWaveDecoder::close();
}

//  bool QWaveDecoder::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QWaveDecoder4seekEx(QWaveDecoder *self, qint64 pos) {
  return self->QWaveDecoder::seek(pos);
}

//  qint64 QWaveDecoder::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QWaveDecoder3posEv(const QWaveDecoder *self) {
  return self->QWaveDecoder::pos();
}

//  qint64 QWaveDecoder::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QWaveDecoder4sizeEv(const QWaveDecoder *self) {
  return self->QWaveDecoder::size();
}

//  bool QWaveDecoder::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QWaveDecoder12isSequentialEv(const QWaveDecoder *self) {
  return self->QWaveDecoder::isSequential();
}

//  qint64 QWaveDecoder::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QWaveDecoder14bytesAvailableEv(
    const QWaveDecoder *self) {
  return self->QWaveDecoder::bytesAvailable();
}

//  qint64 QWaveDecoder::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN12QWaveDecoder8readDataEPcx(
    QWaveDecoder *self,
    char *data,
    qint64 maxlen) {
  return self->QWaveDecoder::readData(data, maxlen);
}

#endif  // QT_DEPRECATED_SINCE(6, 11)
