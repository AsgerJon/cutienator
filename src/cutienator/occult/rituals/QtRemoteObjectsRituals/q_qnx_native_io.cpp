//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnection_qnx_qiodevices.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#if defined(Q_OS_QNX)
#include <QtRemoteObjects/QtRemoteObjects>
#include <QtRemoteObjects/qconnection_qnx_qiodevices.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQnxNativeIo may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQnxNativeIo : QQnxNativeIo {
  using QQnxNativeIo::readData;
};

//  A QQnxNativeIo that Python can take functions over in. Every QQnxNativeIo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQnxNativeIoCall0)(const void *, int *);
typedef qint64 (*CuteQQnxNativeIoCall1)(const void *, int *);
typedef qint64 (*CuteQQnxNativeIoCall2)(const void *, int *);
typedef bool (*CuteQQnxNativeIoCall3)(const void *, int, int *);
typedef void (*CuteQQnxNativeIoCall4)(const void *, int *);
typedef bool (*CuteQQnxNativeIoCall5)(const void *, int, int *);
typedef bool (*CuteQQnxNativeIoCall6)(const void *, int, int *);
typedef qint64 (*CuteQQnxNativeIoCall7)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQQnxNativeIoCall8)(const void *, int *);
typedef qint64 (*CuteQQnxNativeIoCall9)(const void *, int *);
typedef bool (*CuteQQnxNativeIoCall10)(const void *, qint64, int *);
typedef bool (*CuteQQnxNativeIoCall11)(const void *, int *);
typedef bool (*CuteQQnxNativeIoCall12)(const void *, int *);
typedef bool (*CuteQQnxNativeIoCall13)(const void *, int *);
typedef qint64 (*CuteQQnxNativeIoCall14)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQQnxNativeIoCall15)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQnxNativeIoCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQnxNativeIoCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeIoCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeIoCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeIoCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeIoCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQnxNativeIoCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQnxNativeIo : public QQnxNativeIo {
public:
  using QQnxNativeIo::QQnxNativeIo;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
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

  //  bool QQnxNativeIo::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQnxNativeIoCall0 call = reinterpret_cast<CuteQQnxNativeIoCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::isSequential();
  }

  //  qint64 QQnxNativeIo::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQnxNativeIoCall1 call = reinterpret_cast<CuteQQnxNativeIoCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::bytesAvailable();
  }

  //  qint64 QQnxNativeIo::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQnxNativeIoCall2 call = reinterpret_cast<CuteQQnxNativeIoCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::bytesToWrite();
  }

  //  bool QQnxNativeIo::open(OpenMode openMode)
  bool open(QIODeviceBase::OpenMode openMode) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQnxNativeIoCall3 call = reinterpret_cast<CuteQQnxNativeIoCall3>(taken[3]);
      bool given = call(this, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::open(openMode);
  }

  //  void QQnxNativeIo::close()
  void close() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQnxNativeIoCall4 call = reinterpret_cast<CuteQQnxNativeIoCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQnxNativeIo::close();
  }

  //  bool QQnxNativeIo::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQnxNativeIoCall5 call = reinterpret_cast<CuteQQnxNativeIoCall5>(taken[5]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::waitForBytesWritten(msecs);
  }

  //  bool QQnxNativeIo::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQnxNativeIoCall6 call = reinterpret_cast<CuteQQnxNativeIoCall6>(taken[6]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::waitForReadyRead(msecs);
  }

  //  qint64 QQnxNativeIo::readData(char *a0, qint64 a1)
  qint64 readData(char *a0, qint64 a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQnxNativeIoCall7 call = reinterpret_cast<CuteQQnxNativeIoCall7>(taken[7]);
      qint64 given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQnxNativeIo::readData(a0, a1);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQnxNativeIoCall8 call = reinterpret_cast<CuteQQnxNativeIoCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQnxNativeIoCall9 call = reinterpret_cast<CuteQQnxNativeIoCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQnxNativeIoCall10 call = reinterpret_cast<CuteQQnxNativeIoCall10>(taken[10]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQnxNativeIoCall11 call = reinterpret_cast<CuteQQnxNativeIoCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQnxNativeIoCall12 call = reinterpret_cast<CuteQQnxNativeIoCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQnxNativeIoCall13 call = reinterpret_cast<CuteQQnxNativeIoCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  qint64 QIODevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQnxNativeIoCall14 call = reinterpret_cast<CuteQQnxNativeIoCall14>(taken[14]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QIODevice::readLineData(data, maxlen);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQnxNativeIoCall15 call = reinterpret_cast<CuteQQnxNativeIoCall15>(taken[15]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQnxNativeIoCall16 call = reinterpret_cast<CuteQQnxNativeIoCall16>(taken[16]);
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
      CuteQQnxNativeIoCall17 call = reinterpret_cast<CuteQQnxNativeIoCall17>(taken[17]);
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
      CuteQQnxNativeIoCall18 call = reinterpret_cast<CuteQQnxNativeIoCall18>(taken[18]);
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
      CuteQQnxNativeIoCall19 call = reinterpret_cast<CuteQQnxNativeIoCall19>(taken[19]);
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
      CuteQQnxNativeIoCall20 call = reinterpret_cast<CuteQQnxNativeIoCall20>(taken[20]);
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
      CuteQQnxNativeIoCall21 call = reinterpret_cast<CuteQQnxNativeIoCall21>(taken[21]);
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
      CuteQQnxNativeIoCall22 call = reinterpret_cast<CuteQQnxNativeIoCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQnxNativeIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QQnxNativeIo10metaObjectEv(
    const QQnxNativeIo *self) {
  return self->metaObject();
}

//  void *QQnxNativeIo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QQnxNativeIo11qt_metacastEPKc(
    QQnxNativeIo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQnxNativeIo::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QQnxNativeIo11qt_metacallEN11QMetaObject4CallEiPPv(
    QQnxNativeIo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQnxNativeIo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QQnxNativeIo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQnxNativeIo::tr(s, c, n));
}

//  QQnxNativeIoPrivate *QQnxNativeIo::d_func()
extern "C" Q_DECL_EXPORT
QQnxNativeIoPrivate *ritual_ZN12QQnxNativeIo6d_funcEv(QQnxNativeIo *self) {
  return self->d_func();
}

//  const QQnxNativeIoPrivate *QQnxNativeIo::d_func() const
extern "C" Q_DECL_EXPORT
const QQnxNativeIoPrivate *ritual_ZNK12QQnxNativeIo6d_funcEv(
    const QQnxNativeIo *self) {
  return self->d_func();
}

//  QQnxNativeIo::QQnxNativeIo(QObject *parent)
extern "C" Q_DECL_EXPORT
QQnxNativeIo *ritual_ZN12QQnxNativeIoC1EP7QObject(QObject *parent) {
  return new CuteQQnxNativeIo(parent);
}

//  QQnxNativeIo::~QQnxNativeIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIoD1Ev(QQnxNativeIo *self) {
  delete self;
}

//  bool QQnxNativeIo::connectToServer(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQnxNativeIo15connectToServerE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QQnxNativeIo *self,
    int openMode) {
  return self->connectToServer(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  bool QQnxNativeIo::connectToServer(const QString &name, OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQnxNativeIo15connectToServerERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QQnxNativeIo *self,
    const QString *name,
    int openMode) {
  return self->connectToServer(
      *name,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QQnxNativeIo::disconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo20disconnectFromServerEv(QQnxNativeIo *self) {
  self->disconnectFromServer();
}

//  void QQnxNativeIo::setServerName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo13setServerNameERK7QString(
    QQnxNativeIo *self,
    const QString *name) {
  self->setServerName(*name);
}

//  QString QQnxNativeIo::serverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QQnxNativeIo10serverNameEv(const QQnxNativeIo *self) {
  return new QString(self->serverName());
}

//  void QQnxNativeIo::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo5abortEv(QQnxNativeIo *self) {
  self->abort();
}

//  bool QQnxNativeIo::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QQnxNativeIo12isSequentialEv(const QQnxNativeIo *self) {
  return self->isSequential();
}

//  qint64 QQnxNativeIo::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QQnxNativeIo14bytesAvailableEv(const QQnxNativeIo *self) {
  return self->bytesAvailable();
}

//  qint64 QQnxNativeIo::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QQnxNativeIo12bytesToWriteEv(const QQnxNativeIo *self) {
  return self->bytesToWrite();
}

//  bool QQnxNativeIo::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQnxNativeIo4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QQnxNativeIo *self,
    int openMode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QQnxNativeIo::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo5closeEv(QQnxNativeIo *self) {
  self->close();
}

//  QAbstractSocket::SocketState QQnxNativeIo::state() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketState ritual_ZNK12QQnxNativeIo5stateEv(
    const QQnxNativeIo *self) {
  return self->state();
}

//  bool QQnxNativeIo::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQnxNativeIo19waitForBytesWrittenEi(
    QQnxNativeIo *self,
    int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QQnxNativeIo::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QQnxNativeIo16waitForReadyReadEi(
    QQnxNativeIo *self,
    int msecs) {
  return self->waitForReadyRead(msecs);
}

//  void QQnxNativeIo::connected()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo9connectedEv(QQnxNativeIo *self) {
  self->connected();
}

//  void QQnxNativeIo::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo12disconnectedEv(QQnxNativeIo *self) {
  self->disconnected();
}

//  void QQnxNativeIo::error(QAbstractSocket::SocketError socketError)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo5errorEN15QAbstractSocket11SocketErrorE(
    QQnxNativeIo *self,
    QAbstractSocket::SocketError socketError) {
  self->error(socketError);
}

//  void QQnxNativeIo::stateChanged(QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQnxNativeIo12stateChangedEN15QAbstractSocket11SocketStateE(
    QQnxNativeIo *self,
    QAbstractSocket::SocketState socketState) {
  self->stateChanged(socketState);
}

//  qint64 QQnxNativeIo::readData(char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QQnxNativeIo8readDataEPcx(
    QQnxNativeIo *self,
    char *a0,
    qint64 a1) {
  return self->readData(a0, a1);
}

//  qint64 QQnxNativeIo::writeData(const char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QQnxNativeIo9writeDataEPKcx(
    QQnxNativeIo *self,
    const char *a0,
    qint64 a1) {
  return self->writeData(a0, a1);
}

//  a Python function taken by a CuteQQnxNativeIo, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQnxNativeIo(
    QQnxNativeIo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQnxNativeIo *>(self)->take(key, call);
}

//  bool QQnxNativeIo::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QQnxNativeIo12isSequentialEv(const QQnxNativeIo *self) {
  return self->QQnxNativeIo::isSequential();
}

//  qint64 QQnxNativeIo::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QQnxNativeIo14bytesAvailableEv(
    const QQnxNativeIo *self) {
  return self->QQnxNativeIo::bytesAvailable();
}

//  qint64 QQnxNativeIo::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QQnxNativeIo12bytesToWriteEv(
    const QQnxNativeIo *self) {
  return self->QQnxNativeIo::bytesToWrite();
}

//  bool QQnxNativeIo::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQnxNativeIo4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QQnxNativeIo *self,
    int openMode) {
  return self->QQnxNativeIo::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QQnxNativeIo::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QQnxNativeIo5closeEv(QQnxNativeIo *self) {
  self->QQnxNativeIo::close();
}

//  bool QQnxNativeIo::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQnxNativeIo19waitForBytesWrittenEi(
    QQnxNativeIo *self,
    int msecs) {
  return self->QQnxNativeIo::waitForBytesWritten(msecs);
}

//  bool QQnxNativeIo::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QQnxNativeIo16waitForReadyReadEi(
    QQnxNativeIo *self,
    int msecs) {
  return self->QQnxNativeIo::waitForReadyRead(msecs);
}

//  qint64 QQnxNativeIo::readData(char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN12QQnxNativeIo8readDataEPcx(
    QQnxNativeIo *self,
    char *a0,
    qint64 a1) {
  return static_cast<OwnQQnxNativeIo *>(self)->OwnQQnxNativeIo::readData(
      a0,
      a1);
}

#endif  // defined(Q_OS_QNX)
