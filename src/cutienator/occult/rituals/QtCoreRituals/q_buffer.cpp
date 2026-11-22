//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qbuffer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qbuffer.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QBuffer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQBuffer : QBuffer {
  using QBuffer::connectNotify;
  using QBuffer::disconnectNotify;
};

//  A QBuffer that Python can take functions over in. Every QBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQBufferCall0)(const void *, int, int *);
typedef void (*CuteQBufferCall1)(const void *, int *);
typedef qint64 (*CuteQBufferCall2)(const void *, int *);
typedef qint64 (*CuteQBufferCall3)(const void *, int *);
typedef bool (*CuteQBufferCall4)(const void *, qint64, int *);
typedef bool (*CuteQBufferCall5)(const void *, int *);
typedef bool (*CuteQBufferCall6)(const void *, int *);
typedef void (*CuteQBufferCall7)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQBufferCall8)(const void *, const QMetaMethod *, int *);
typedef bool (*CuteQBufferCall9)(const void *, int *);
typedef bool (*CuteQBufferCall10)(const void *, int *);
typedef qint64 (*CuteQBufferCall11)(const void *, int *);
typedef qint64 (*CuteQBufferCall12)(const void *, int *);
typedef bool (*CuteQBufferCall13)(const void *, int, int *);
typedef bool (*CuteQBufferCall14)(const void *, int, int *);
typedef qint64 (*CuteQBufferCall15)(const void *, qint64, int *);
typedef bool (*CuteQBufferCall16)(const void *, QEvent *, int *);
typedef bool (*CuteQBufferCall17)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQBufferCall18)(const void *, QTimerEvent *, int *);
typedef void (*CuteQBufferCall19)(const void *, QChildEvent *, int *);
typedef void (*CuteQBufferCall20)(const void *, QEvent *, int *);
class CuteQBuffer : public QBuffer {
public:
  using QBuffer::QBuffer;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
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
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  bool QBuffer::open(OpenMode openMode)
  bool open(QIODeviceBase::OpenMode openMode) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBufferCall0 call = reinterpret_cast<CuteQBufferCall0>(taken[0]);
      bool given = call(this, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return QBuffer::open(openMode);
  }

  //  void QBuffer::close()
  void close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQBufferCall1 call = reinterpret_cast<CuteQBufferCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QBuffer::close();
  }

  //  qint64 QBuffer::size() const
  qint64 size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQBufferCall2 call = reinterpret_cast<CuteQBufferCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QBuffer::size();
  }

  //  qint64 QBuffer::pos() const
  qint64 pos() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQBufferCall3 call = reinterpret_cast<CuteQBufferCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QBuffer::pos();
  }

  //  bool QBuffer::seek(qint64 off)
  bool seek(qint64 off) override {
    if (taken[4]) {
      int handled = 0;
      CuteQBufferCall4 call = reinterpret_cast<CuteQBufferCall4>(taken[4]);
      bool given = call(this, off, &handled);
      if (handled) return given;
    }
    return QBuffer::seek(off);
  }

  //  bool QBuffer::atEnd() const
  bool atEnd() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQBufferCall5 call = reinterpret_cast<CuteQBufferCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBuffer::atEnd();
  }

  //  bool QBuffer::canReadLine() const
  bool canReadLine() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQBufferCall6 call = reinterpret_cast<CuteQBufferCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBuffer::canReadLine();
  }

  //  void QBuffer::connectNotify(const QMetaMethod &a0)
  void connectNotify(const QMetaMethod &a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQBufferCall7 call = reinterpret_cast<CuteQBufferCall7>(taken[7]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QBuffer::connectNotify(a0);
  }

  //  void QBuffer::disconnectNotify(const QMetaMethod &a0)
  void disconnectNotify(const QMetaMethod &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQBufferCall8 call = reinterpret_cast<CuteQBufferCall8>(taken[8]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QBuffer::disconnectNotify(a0);
  }

  //  bool QIODevice::isSequential() const
  bool isSequential() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQBufferCall9 call = reinterpret_cast<CuteQBufferCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::isSequential();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[10]) {
      int handled = 0;
      CuteQBufferCall10 call = reinterpret_cast<CuteQBufferCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQBufferCall11 call = reinterpret_cast<CuteQBufferCall11>(taken[11]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQBufferCall12 call = reinterpret_cast<CuteQBufferCall12>(taken[12]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQBufferCall13 call = reinterpret_cast<CuteQBufferCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQBufferCall14 call = reinterpret_cast<CuteQBufferCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[15]) {
      int handled = 0;
      CuteQBufferCall15 call = reinterpret_cast<CuteQBufferCall15>(taken[15]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQBufferCall16 call = reinterpret_cast<CuteQBufferCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQBufferCall17 call = reinterpret_cast<CuteQBufferCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQBufferCall18 call = reinterpret_cast<CuteQBufferCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQBufferCall19 call = reinterpret_cast<CuteQBufferCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQBufferCall20 call = reinterpret_cast<CuteQBufferCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
};

//  const QMetaObject *QBuffer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QBuffer10metaObjectEv(const QBuffer *self) {
  return self->metaObject();
}

//  QString QBuffer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QBuffer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QBuffer::tr(s, c, n));
}

//  QBuffer::QBuffer(QObject *parent)
extern "C" Q_DECL_EXPORT
QBuffer *ritual_ZN7QBufferC1EP7QObject(QObject *parent) {
  return new CuteQBuffer(parent);
}

//  QBuffer::QBuffer(QByteArray *buf, QObject *parent)
extern "C" Q_DECL_EXPORT
QBuffer *ritual_ZN7QBufferC1EP10QByteArrayP7QObject(
    QByteArray *buf,
    QObject *parent) {
  return new CuteQBuffer(buf, parent);
}

//  QBuffer::~QBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBufferD1Ev(QBuffer *self) {
  delete self;
}

//  const QByteArray &QBuffer::buffer() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QBuffer6bufferEv(const QBuffer *self) {
  return new QByteArray(self->buffer());
}

//  void QBuffer::setBuffer(QByteArray *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer9setBufferEP10QByteArray(
    QBuffer *self,
    QByteArray *a) {
  self->setBuffer(a);
}

//  void QBuffer::setData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer7setDataERK10QByteArray(
    QBuffer *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  void QBuffer::setData(const char *data, qsizetype len)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer7setDataEPKcx(
    QBuffer *self,
    const char *data,
    qsizetype len) {
  self->setData(data, len);
}

//  const QByteArray &QBuffer::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK7QBuffer4dataEv(const QBuffer *self) {
  return new QByteArray(self->data());
}

//  bool QBuffer::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QBuffer4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBuffer *self,
    int openMode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBuffer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBuffer5closeEv(QBuffer *self) {
  self->close();
}

//  qint64 QBuffer::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK7QBuffer4sizeEv(const QBuffer *self) {
  return self->size();
}

//  qint64 QBuffer::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK7QBuffer3posEv(const QBuffer *self) {
  return self->pos();
}

//  bool QBuffer::seek(qint64 off)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QBuffer4seekEx(QBuffer *self, qint64 off) {
  return self->seek(off);
}

//  bool QBuffer::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBuffer5atEndEv(const QBuffer *self) {
  return self->atEnd();
}

//  bool QBuffer::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QBuffer11canReadLineEv(const QBuffer *self) {
  return self->canReadLine();
}

//  a Python function taken by a CuteQBuffer, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBuffer(QBuffer *self, const char *key, void *call) {
  return static_cast<CuteQBuffer *>(self)->take(key, call);
}

//  bool QBuffer::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QBuffer4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBuffer *self,
    int openMode) {
  return self->QBuffer::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBuffer::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QBuffer5closeEv(QBuffer *self) {
  self->QBuffer::close();
}

//  qint64 QBuffer::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK7QBuffer4sizeEv(const QBuffer *self) {
  return self->QBuffer::size();
}

//  qint64 QBuffer::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK7QBuffer3posEv(const QBuffer *self) {
  return self->QBuffer::pos();
}

//  bool QBuffer::seek(qint64 off)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN7QBuffer4seekEx(QBuffer *self, qint64 off) {
  return self->QBuffer::seek(off);
}

//  bool QBuffer::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK7QBuffer5atEndEv(const QBuffer *self) {
  return self->QBuffer::atEnd();
}

//  bool QBuffer::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK7QBuffer11canReadLineEv(const QBuffer *self) {
  return self->QBuffer::canReadLine();
}

//  void QBuffer::connectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QBuffer13connectNotifyERK11QMetaMethod(
    QBuffer *self,
    const QMetaMethod *a0) {
  static_cast<OwnQBuffer *>(self)->OwnQBuffer::connectNotify(*a0);
}

//  void QBuffer::disconnectNotify(const QMetaMethod &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN7QBuffer16disconnectNotifyERK11QMetaMethod(
    QBuffer *self,
    const QMetaMethod *a0) {
  static_cast<OwnQBuffer *>(self)->OwnQBuffer::disconnectNotify(*a0);
}
