//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qiodevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qiodevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QIODevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQIODevice : QIODevice {
  using QIODevice::skipData;
};

//  A QIODevice that Python can take functions over in. Every QIODevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQIODeviceCall0)(const void *, int *);
typedef bool (*CuteQIODeviceCall1)(const void *, int, int *);
typedef void (*CuteQIODeviceCall2)(const void *, int *);
typedef qint64 (*CuteQIODeviceCall3)(const void *, int *);
typedef qint64 (*CuteQIODeviceCall4)(const void *, int *);
typedef bool (*CuteQIODeviceCall5)(const void *, qint64, int *);
typedef bool (*CuteQIODeviceCall6)(const void *, int *);
typedef bool (*CuteQIODeviceCall7)(const void *, int *);
typedef qint64 (*CuteQIODeviceCall8)(const void *, int *);
typedef qint64 (*CuteQIODeviceCall9)(const void *, int *);
typedef bool (*CuteQIODeviceCall10)(const void *, int *);
typedef bool (*CuteQIODeviceCall11)(const void *, int, int *);
typedef bool (*CuteQIODeviceCall12)(const void *, int, int *);
typedef qint64 (*CuteQIODeviceCall13)(const void *, qint64, int *);
typedef bool (*CuteQIODeviceCall14)(const void *, QEvent *, int *);
typedef bool (*CuteQIODeviceCall15)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQIODeviceCall16)(const void *, QTimerEvent *, int *);
typedef void (*CuteQIODeviceCall17)(const void *, QChildEvent *, int *);
typedef void (*CuteQIODeviceCall18)(const void *, QEvent *, int *);
typedef void (*CuteQIODeviceCall19)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQIODeviceCall20)(const void *, const QMetaMethod *, int *);
class CuteQIODevice : public QIODevice {
public:
  using QIODevice::QIODevice;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  bool QIODevice::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQIODeviceCall0 call = reinterpret_cast<CuteQIODeviceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::isSequential();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQIODeviceCall1 call = reinterpret_cast<CuteQIODeviceCall1>(taken[1]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  void QIODevice::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQIODeviceCall2 call = reinterpret_cast<CuteQIODeviceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QIODevice::close();
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQIODeviceCall3 call = reinterpret_cast<CuteQIODeviceCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQIODeviceCall4 call = reinterpret_cast<CuteQIODeviceCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[5]) {
      int handled = 0;
      CuteQIODeviceCall5 call = reinterpret_cast<CuteQIODeviceCall5>(taken[5]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQIODeviceCall6 call = reinterpret_cast<CuteQIODeviceCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[7]) {
      int handled = 0;
      CuteQIODeviceCall7 call = reinterpret_cast<CuteQIODeviceCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQIODeviceCall8 call = reinterpret_cast<CuteQIODeviceCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQIODeviceCall9 call = reinterpret_cast<CuteQIODeviceCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQIODeviceCall10 call = reinterpret_cast<CuteQIODeviceCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[11]) {
      int handled = 0;
      CuteQIODeviceCall11 call = reinterpret_cast<CuteQIODeviceCall11>(taken[11]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQIODeviceCall12 call = reinterpret_cast<CuteQIODeviceCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQIODeviceCall13 call = reinterpret_cast<CuteQIODeviceCall13>(taken[13]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQIODeviceCall14 call = reinterpret_cast<CuteQIODeviceCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQIODeviceCall15 call = reinterpret_cast<CuteQIODeviceCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQIODeviceCall16 call = reinterpret_cast<CuteQIODeviceCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQIODeviceCall17 call = reinterpret_cast<CuteQIODeviceCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQIODeviceCall18 call = reinterpret_cast<CuteQIODeviceCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQIODeviceCall19 call = reinterpret_cast<CuteQIODeviceCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQIODeviceCall20 call = reinterpret_cast<CuteQIODeviceCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QIODevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QIODevice10metaObjectEv(
    const QIODevice *self) {
  return self->metaObject();
}

//  QString QIODevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QIODevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIODevice::tr(s, c, n));
}

//  QIODevice::~QIODevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODeviceD1Ev(QIODevice *self) {
  delete self;
}

//  QIODeviceBase::OpenMode QIODevice::openMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice8openModeEv(const QIODevice *self) {
  return static_cast<int>(self->openMode().toInt());
}

//  void QIODevice::setTextModeEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice18setTextModeEnabledEb(
    QIODevice *self,
    bool enabled) {
  self->setTextModeEnabled(enabled);
}

//  bool QIODevice::isTextModeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice17isTextModeEnabledEv(const QIODevice *self) {
  return self->isTextModeEnabled();
}

//  bool QIODevice::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice6isOpenEv(const QIODevice *self) {
  return self->isOpen();
}

//  bool QIODevice::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice10isReadableEv(const QIODevice *self) {
  return self->isReadable();
}

//  bool QIODevice::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice10isWritableEv(const QIODevice *self) {
  return self->isWritable();
}

//  bool QIODevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice12isSequentialEv(const QIODevice *self) {
  return self->isSequential();
}

//  int QIODevice::readChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice16readChannelCountEv(const QIODevice *self) {
  return self->readChannelCount();
}

//  int QIODevice::writeChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice17writeChannelCountEv(const QIODevice *self) {
  return self->writeChannelCount();
}

//  int QIODevice::currentReadChannel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice18currentReadChannelEv(const QIODevice *self) {
  return self->currentReadChannel();
}

//  void QIODevice::setCurrentReadChannel(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice21setCurrentReadChannelEi(
    QIODevice *self,
    int channel) {
  self->setCurrentReadChannel(channel);
}

//  int QIODevice::currentWriteChannel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QIODevice19currentWriteChannelEv(const QIODevice *self) {
  return self->currentWriteChannel();
}

//  void QIODevice::setCurrentWriteChannel(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice22setCurrentWriteChannelEi(
    QIODevice *self,
    int channel) {
  self->setCurrentWriteChannel(channel);
}

//  bool QIODevice::open(QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QIODevice *self,
    int mode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QIODevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice5closeEv(QIODevice *self) {
  self->close();
}

//  qint64 QIODevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice3posEv(const QIODevice *self) {
  return self->pos();
}

//  qint64 QIODevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice4sizeEv(const QIODevice *self) {
  return self->size();
}

//  bool QIODevice::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice4seekEx(QIODevice *self, qint64 pos) {
  return self->seek(pos);
}

//  bool QIODevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice5atEndEv(const QIODevice *self) {
  return self->atEnd();
}

//  bool QIODevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice5resetEv(QIODevice *self) {
  return self->reset();
}

//  qint64 QIODevice::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice14bytesAvailableEv(const QIODevice *self) {
  return self->bytesAvailable();
}

//  qint64 QIODevice::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK9QIODevice12bytesToWriteEv(const QIODevice *self) {
  return self->bytesToWrite();
}

//  QByteArray QIODevice::read(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice4readEx(QIODevice *self, qint64 maxlen) {
  return new QByteArray(self->read(maxlen));
}

//  QByteArray QIODevice::readAll()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice7readAllEv(QIODevice *self) {
  return new QByteArray(self->readAll());
}

//  QByteArray QIODevice::readLine(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice8readLineEx(QIODevice *self, qint64 maxlen) {
  return new QByteArray(self->readLine(maxlen));
}

//  bool QIODevice::readLineInto(QByteArray *result, qint64 maxlen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice12readLineIntoEP10QByteArrayx(
    QIODevice *self,
    QByteArray *result,
    qint64 maxlen) {
  return self->readLineInto(result, maxlen);
}

//  bool QIODevice::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice11canReadLineEv(const QIODevice *self) {
  return self->canReadLine();
}

//  void QIODevice::startTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice16startTransactionEv(QIODevice *self) {
  self->startTransaction();
}

//  void QIODevice::commitTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice17commitTransactionEv(QIODevice *self) {
  self->commitTransaction();
}

//  void QIODevice::rollbackTransaction()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice19rollbackTransactionEv(QIODevice *self) {
  self->rollbackTransaction();
}

//  bool QIODevice::isTransactionStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QIODevice20isTransactionStartedEv(const QIODevice *self) {
  return self->isTransactionStarted();
}

//  qint64 QIODevice::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice5writeEPKcx(
    QIODevice *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

//  qint64 QIODevice::write(const char *data)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice5writeEPKc(QIODevice *self, const char *data) {
  return self->write(data);
}

//  qint64 QIODevice::write(const QByteArray &data)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice5writeERK10QByteArray(
    QIODevice *self,
    const QByteArray *data) {
  return self->write(*data);
}

//  QByteArray QIODevice::peek(qint64 maxlen)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN9QIODevice4peekEx(QIODevice *self, qint64 maxlen) {
  return new QByteArray(self->peek(maxlen));
}

//  qint64 QIODevice::skip(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice4skipEx(QIODevice *self, qint64 maxSize) {
  return self->skip(maxSize);
}

//  bool QIODevice::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice16waitForReadyReadEi(QIODevice *self, int msecs) {
  return self->waitForReadyRead(msecs);
}

//  bool QIODevice::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice19waitForBytesWrittenEi(QIODevice *self, int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  void QIODevice::ungetChar(char c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice9ungetCharEc(QIODevice *self, char c) {
  self->ungetChar(c);
}

//  bool QIODevice::putChar(char c)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QIODevice7putCharEc(QIODevice *self, char c) {
  return self->putChar(c);
}

//  QString QIODevice::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QIODevice11errorStringEv(const QIODevice *self) {
  return new QString(self->errorString());
}

//  qint64 QIODevice::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice8skipDataEx(QIODevice *self, qint64 maxSize) {
  return self->skipData(maxSize);
}

//  qint64 QIODevice::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QIODevice9writeDataEPKcx(
    QIODevice *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  void QIODevice::setOpenMode(QIODeviceBase::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice11setOpenModeE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QIODevice *self,
    int openMode) {
  self->setOpenMode(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QIODevice::setErrorString(const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIODevice14setErrorStringERK7QString(
    QIODevice *self,
    const QString *errorString) {
  self->setErrorString(*errorString);
}

//  QIODevice as the QIODeviceBase it is built on
extern "C" Q_DECL_EXPORT
QIODeviceBase *ritual_cast_QIODevice_QIODeviceBase(QIODevice *self) {
  return static_cast<QIODeviceBase *>(self);
}

//  a Python function taken by a CuteQIODevice, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QIODevice(QIODevice *self, const char *key, void *call) {
  return static_cast<CuteQIODevice *>(self)->take(key, call);
}

//  bool QIODevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QIODevice12isSequentialEv(const QIODevice *self) {
  return self->QIODevice::isSequential();
}

//  bool QIODevice::open(QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QIODevice *self,
    int mode) {
  return self->QIODevice::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QIODevice::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QIODevice5closeEv(QIODevice *self) {
  self->QIODevice::close();
}

//  qint64 QIODevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK9QIODevice3posEv(const QIODevice *self) {
  return self->QIODevice::pos();
}

//  qint64 QIODevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK9QIODevice4sizeEv(const QIODevice *self) {
  return self->QIODevice::size();
}

//  bool QIODevice::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QIODevice4seekEx(QIODevice *self, qint64 pos) {
  return self->QIODevice::seek(pos);
}

//  bool QIODevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QIODevice5atEndEv(const QIODevice *self) {
  return self->QIODevice::atEnd();
}

//  bool QIODevice::reset()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QIODevice5resetEv(QIODevice *self) {
  return self->QIODevice::reset();
}

//  qint64 QIODevice::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK9QIODevice14bytesAvailableEv(const QIODevice *self) {
  return self->QIODevice::bytesAvailable();
}

//  qint64 QIODevice::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK9QIODevice12bytesToWriteEv(const QIODevice *self) {
  return self->QIODevice::bytesToWrite();
}

//  bool QIODevice::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QIODevice11canReadLineEv(const QIODevice *self) {
  return self->QIODevice::canReadLine();
}

//  bool QIODevice::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QIODevice16waitForReadyReadEi(
    QIODevice *self,
    int msecs) {
  return self->QIODevice::waitForReadyRead(msecs);
}

//  bool QIODevice::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QIODevice19waitForBytesWrittenEi(
    QIODevice *self,
    int msecs) {
  return self->QIODevice::waitForBytesWritten(msecs);
}

//  qint64 QIODevice::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN9QIODevice8skipDataEx(QIODevice *self, qint64 maxSize) {
  return static_cast<OwnQIODevice *>(self)->OwnQIODevice::skipData(maxSize);
}
