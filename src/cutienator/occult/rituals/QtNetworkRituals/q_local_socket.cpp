//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qlocalsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalsocket.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLocalSocket may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLocalSocket : QLocalSocket {
  using QLocalSocket::skipData;
};

//  A QLocalSocket that Python can take functions over in. Every QLocalSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(localserver)
typedef bool (*CuteQLocalSocketCall0)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef qint64 (*CuteQLocalSocketCall1)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef qint64 (*CuteQLocalSocketCall2)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef bool (*CuteQLocalSocketCall3)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef bool (*CuteQLocalSocketCall4)(const void *, int, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef void (*CuteQLocalSocketCall5)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef bool (*CuteQLocalSocketCall6)(const void *, int, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef bool (*CuteQLocalSocketCall7)(const void *, int, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef qint64 (*CuteQLocalSocketCall8)(const void *, qint64, int *);
#endif  // QT_CONFIG(localserver)
typedef qint64 (*CuteQLocalSocketCall9)(const void *, int *);
typedef qint64 (*CuteQLocalSocketCall10)(const void *, int *);
typedef bool (*CuteQLocalSocketCall11)(const void *, qint64, int *);
typedef bool (*CuteQLocalSocketCall12)(const void *, int *);
typedef bool (*CuteQLocalSocketCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLocalSocketCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLocalSocketCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalSocketCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalSocketCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalSocketCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalSocketCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalSocketCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLocalSocket : public QLocalSocket {
public:
  using QLocalSocket::QLocalSocket;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(localserver)
  //  bool QLocalSocket::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLocalSocketCall0 call = reinterpret_cast<CuteQLocalSocketCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLocalSocket::isSequential();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  qint64 QLocalSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQLocalSocketCall1 call = reinterpret_cast<CuteQLocalSocketCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QLocalSocket::bytesAvailable();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  qint64 QLocalSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQLocalSocketCall2 call = reinterpret_cast<CuteQLocalSocketCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QLocalSocket::bytesToWrite();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  bool QLocalSocket::canReadLine() const
  bool canReadLine() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLocalSocketCall3 call = reinterpret_cast<CuteQLocalSocketCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLocalSocket::canReadLine();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  bool QLocalSocket::open(OpenMode openMode)
  bool open(QIODeviceBase::OpenMode openMode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLocalSocketCall4 call = reinterpret_cast<CuteQLocalSocketCall4>(taken[4]);
      bool given = call(this, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return QLocalSocket::open(openMode);
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  void QLocalSocket::close()
  void close() override {
    if (taken[5]) {
      int handled = 0;
      CuteQLocalSocketCall5 call = reinterpret_cast<CuteQLocalSocketCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QLocalSocket::close();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  bool QLocalSocket::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLocalSocketCall6 call = reinterpret_cast<CuteQLocalSocketCall6>(taken[6]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QLocalSocket::waitForBytesWritten(msecs);
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  bool QLocalSocket::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLocalSocketCall7 call = reinterpret_cast<CuteQLocalSocketCall7>(taken[7]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QLocalSocket::waitForReadyRead(msecs);
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  qint64 QLocalSocket::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLocalSocketCall8 call = reinterpret_cast<CuteQLocalSocketCall8>(taken[8]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QLocalSocket::skipData(maxSize);
  }
#endif  // QT_CONFIG(localserver)

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQLocalSocketCall9 call = reinterpret_cast<CuteQLocalSocketCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQLocalSocketCall10 call = reinterpret_cast<CuteQLocalSocketCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLocalSocketCall11 call = reinterpret_cast<CuteQLocalSocketCall11>(taken[11]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLocalSocketCall12 call = reinterpret_cast<CuteQLocalSocketCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[13]) {
      int handled = 0;
      CuteQLocalSocketCall13 call = reinterpret_cast<CuteQLocalSocketCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLocalSocketCall14 call = reinterpret_cast<CuteQLocalSocketCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLocalSocketCall15 call = reinterpret_cast<CuteQLocalSocketCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLocalSocketCall16 call = reinterpret_cast<CuteQLocalSocketCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLocalSocketCall17 call = reinterpret_cast<CuteQLocalSocketCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLocalSocketCall18 call = reinterpret_cast<CuteQLocalSocketCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLocalSocketCall19 call = reinterpret_cast<CuteQLocalSocketCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLocalSocketCall20 call = reinterpret_cast<CuteQLocalSocketCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLocalSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QLocalSocket10metaObjectEv(
    const QLocalSocket *self) {
  return self->metaObject();
}

//  QString QLocalSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QLocalSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLocalSocket::tr(s, c, n));
}

//  QLocalSocketPrivate *QLocalSocket::d_func()
extern "C" Q_DECL_EXPORT
QLocalSocketPrivate *ritual_ZN12QLocalSocket6d_funcEv(QLocalSocket *self) {
  return self->d_func();
}

//  const QLocalSocketPrivate *QLocalSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QLocalSocketPrivate *ritual_ZNK12QLocalSocket6d_funcEv(
    const QLocalSocket *self) {
  return self->d_func();
}

//  QLocalSocket::QLocalSocket(QObject *parent)
extern "C" Q_DECL_EXPORT
QLocalSocket *ritual_ZN12QLocalSocketC1EP7QObject(QObject *parent) {
  return new CuteQLocalSocket(parent);
}

//  QLocalSocket::~QLocalSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocketD1Ev(QLocalSocket *self) {
  delete self;
}

//  void QLocalSocket::connectToServer(OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket15connectToServerE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QLocalSocket *self,
    int openMode) {
  self->connectToServer(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QLocalSocket::connectToServer(const QString &name, OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket15connectToServerERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QLocalSocket *self,
    const QString *name,
    int openMode) {
  self->connectToServer(
      *name,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QLocalSocket::disconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket20disconnectFromServerEv(QLocalSocket *self) {
  self->disconnectFromServer();
}

//  void QLocalSocket::setServerName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket13setServerNameERK7QString(
    QLocalSocket *self,
    const QString *name) {
  self->setServerName(*name);
}

//  QString QLocalSocket::serverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QLocalSocket10serverNameEv(const QLocalSocket *self) {
  return new QString(self->serverName());
}

//  QString QLocalSocket::fullServerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QLocalSocket14fullServerNameEv(
    const QLocalSocket *self) {
  return new QString(self->fullServerName());
}

//  void QLocalSocket::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket5abortEv(QLocalSocket *self) {
  self->abort();
}

//  bool QLocalSocket::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLocalSocket12isSequentialEv(const QLocalSocket *self) {
  return self->isSequential();
}

//  qint64 QLocalSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QLocalSocket14bytesAvailableEv(const QLocalSocket *self) {
  return self->bytesAvailable();
}

//  qint64 QLocalSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QLocalSocket12bytesToWriteEv(const QLocalSocket *self) {
  return self->bytesToWrite();
}

//  bool QLocalSocket::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLocalSocket11canReadLineEv(const QLocalSocket *self) {
  return self->canReadLine();
}

//  bool QLocalSocket::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QLocalSocket *self,
    int openMode) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QLocalSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket5closeEv(QLocalSocket *self) {
  self->close();
}

//  LocalSocketError QLocalSocket::error() const
extern "C" Q_DECL_EXPORT
QLocalSocket::LocalSocketError ritual_ZNK12QLocalSocket5errorEv(
    const QLocalSocket *self) {
  return self->error();
}

//  bool QLocalSocket::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket5flushEv(QLocalSocket *self) {
  return self->flush();
}

//  bool QLocalSocket::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLocalSocket7isValidEv(const QLocalSocket *self) {
  return self->isValid();
}

//  qint64 QLocalSocket::readBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK12QLocalSocket14readBufferSizeEv(const QLocalSocket *self) {
  return self->readBufferSize();
}

//  void QLocalSocket::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket17setReadBufferSizeEx(
    QLocalSocket *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  bool QLocalSocket::setSocketDescriptor(qintptr socketDescriptor,
//      LocalSocketState socketState, OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket19setSocketDescriptorExNS_16LocalSocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QLocalSocket *self,
    qintptr socketDescriptor,
    QLocalSocket::LocalSocketState socketState,
    int openMode) {
  return self->setSocketDescriptor(
      socketDescriptor,
      socketState,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  qintptr QLocalSocket::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK12QLocalSocket16socketDescriptorEv(
    const QLocalSocket *self) {
  return self->socketDescriptor();
}

//  void QLocalSocket::setSocketOptions(SocketOptions option)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalSocket16setSocketOptionsE6QFlagsINS_12SocketOptionEE(
    QLocalSocket *self,
    int option) {
  self->setSocketOptions(
      QFlags<QLocalSocket::SocketOption>::fromInt(option));
}

//  SocketOptions QLocalSocket::socketOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLocalSocket13socketOptionsEv(const QLocalSocket *self) {
  return static_cast<int>(self->socketOptions().toInt());
}

//  LocalSocketState QLocalSocket::state() const
extern "C" Q_DECL_EXPORT
QLocalSocket::LocalSocketState ritual_ZNK12QLocalSocket5stateEv(
    const QLocalSocket *self) {
  return self->state();
}

//  bool QLocalSocket::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket19waitForBytesWrittenEi(
    QLocalSocket *self,
    int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QLocalSocket::waitForConnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket16waitForConnectedEi(
    QLocalSocket *self,
    int msecs) {
  return self->waitForConnected(msecs);
}

//  bool QLocalSocket::waitForDisconnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket19waitForDisconnectedEi(
    QLocalSocket *self,
    int msecs) {
  return self->waitForDisconnected(msecs);
}

//  bool QLocalSocket::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalSocket16waitForReadyReadEi(
    QLocalSocket *self,
    int msecs) {
  return self->waitForReadyRead(msecs);
}

//  qint64 QLocalSocket::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QLocalSocket8skipDataEx(
    QLocalSocket *self,
    qint64 maxSize) {
  return self->skipData(maxSize);
}

//  qint64 QLocalSocket::writeData(const char *a0, qint64 a1)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN12QLocalSocket9writeDataEPKcx(
    QLocalSocket *self,
    const char *a0,
    qint64 a1) {
  return self->writeData(a0, a1);
}

//  a Python function taken by a CuteQLocalSocket, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLocalSocket(
    QLocalSocket *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLocalSocket *>(self)->take(key, call);
}

//  bool QLocalSocket::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLocalSocket12isSequentialEv(const QLocalSocket *self) {
  return self->QLocalSocket::isSequential();
}

//  qint64 QLocalSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QLocalSocket14bytesAvailableEv(
    const QLocalSocket *self) {
  return self->QLocalSocket::bytesAvailable();
}

//  qint64 QLocalSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK12QLocalSocket12bytesToWriteEv(
    const QLocalSocket *self) {
  return self->QLocalSocket::bytesToWrite();
}

//  bool QLocalSocket::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLocalSocket11canReadLineEv(const QLocalSocket *self) {
  return self->QLocalSocket::canReadLine();
}

//  bool QLocalSocket::open(OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QLocalSocket4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QLocalSocket *self,
    int openMode) {
  return self->QLocalSocket::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QLocalSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLocalSocket5closeEv(QLocalSocket *self) {
  self->QLocalSocket::close();
}

//  bool QLocalSocket::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QLocalSocket19waitForBytesWrittenEi(
    QLocalSocket *self,
    int msecs) {
  return self->QLocalSocket::waitForBytesWritten(msecs);
}

//  bool QLocalSocket::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QLocalSocket16waitForReadyReadEi(
    QLocalSocket *self,
    int msecs) {
  return self->QLocalSocket::waitForReadyRead(msecs);
}

//  qint64 QLocalSocket::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN12QLocalSocket8skipDataEx(
    QLocalSocket *self,
    qint64 maxSize) {
  return static_cast<OwnQLocalSocket *>(self)->OwnQLocalSocket::skipData(
      maxSize);
}

#endif  // QT_CONFIG(localserver)
