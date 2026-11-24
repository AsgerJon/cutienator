//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qlocalsocket_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(localserver)
#if !defined(Q_OS_WIN) || defined(QT_LOCALSOCKET_TCP)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qlocalsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QLocalUnixSocket that Python can take functions over in. Every QLocalUnixSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLocalUnixSocketCall0)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall1)(const void *, const QHostAddress *, quint16, int, int *);
typedef void (*CuteQLocalUnixSocketCall2)(const void *, const QString *, quint16, int, int, int *);
typedef void (*CuteQLocalUnixSocketCall3)(const void *, int *);
typedef qint64 (*CuteQLocalUnixSocketCall4)(const void *, int *);
typedef qint64 (*CuteQLocalUnixSocketCall5)(const void *, int *);
typedef void (*CuteQLocalUnixSocketCall6)(const void *, qint64, int *);
typedef qintptr (*CuteQLocalUnixSocketCall7)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall8)(const void *, qintptr, int, int, int *);
typedef void (*CuteQLocalUnixSocketCall9)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQLocalUnixSocketCall10)(const void *, int, int *);
typedef void (*CuteQLocalUnixSocketCall11)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall12)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall13)(const void *, int, int *);
typedef bool (*CuteQLocalUnixSocketCall14)(const void *, int, int *);
typedef bool (*CuteQLocalUnixSocketCall15)(const void *, int, int *);
typedef bool (*CuteQLocalUnixSocketCall16)(const void *, int, int *);
typedef qint64 (*CuteQLocalUnixSocketCall17)(const void *, qint64, int *);
typedef bool (*CuteQLocalUnixSocketCall18)(const void *, int, int *);
typedef qint64 (*CuteQLocalUnixSocketCall19)(const void *, int *);
typedef qint64 (*CuteQLocalUnixSocketCall20)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall21)(const void *, qint64, int *);
typedef bool (*CuteQLocalUnixSocketCall22)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall23)(const void *, int *);
typedef bool (*CuteQLocalUnixSocketCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLocalUnixSocketCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLocalUnixSocketCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalUnixSocketCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalUnixSocketCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalUnixSocketCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalUnixSocketCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalUnixSocketCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLocalUnixSocket : public QLocalUnixSocket {
public:
  using QLocalUnixSocket::QLocalUnixSocket;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QAbstractSocket6resumeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket18disconnectFromHostEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket17setReadBufferSizeEx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSocket16socketDescriptorEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8QVariant")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket16waitForConnectedEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket19waitForDisconnectedEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstractSocket::resume()
  void resume() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLocalUnixSocketCall0 call = reinterpret_cast<CuteQLocalUnixSocketCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::resume();
  }

  //  bool QAbstractSocket::bind(const QHostAddress &address, quint16 port,
  //      BindMode mode)
  bool bind(
      const QHostAddress &address,
      quint16 port,
      QAbstractSocket::BindMode mode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQLocalUnixSocketCall1 call = reinterpret_cast<CuteQLocalUnixSocketCall1>(taken[1]);
      bool given = call(this, &address, port, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bind(address, port, mode);
  }

  //  void QAbstractSocket::connectToHost(const QString &hostName, quint16
  //      port, OpenMode mode, NetworkLayerProtocol protocol)
  void connectToHost(
      const QString &hostName,
      quint16 port,
      QIODeviceBase::OpenMode mode,
      QAbstractSocket::NetworkLayerProtocol protocol) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLocalUnixSocketCall2 call = reinterpret_cast<CuteQLocalUnixSocketCall2>(taken[2]);
      call(this, &hostName, port, static_cast<int>(mode.toInt()), static_cast<int>(protocol), &handled);
      if (handled) return;
    }
    QAbstractSocket::connectToHost(hostName, port, mode, protocol);
  }

  //  void QAbstractSocket::disconnectFromHost()
  void disconnectFromHost() override {
    if (taken[3]) {
      int handled = 0;
      CuteQLocalUnixSocketCall3 call = reinterpret_cast<CuteQLocalUnixSocketCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::disconnectFromHost();
  }

  //  qint64 QAbstractSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQLocalUnixSocketCall4 call = reinterpret_cast<CuteQLocalUnixSocketCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesAvailable();
  }

  //  qint64 QAbstractSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQLocalUnixSocketCall5 call = reinterpret_cast<CuteQLocalUnixSocketCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesToWrite();
  }

  //  void QAbstractSocket::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLocalUnixSocketCall6 call = reinterpret_cast<CuteQLocalUnixSocketCall6>(taken[6]);
      call(this, size, &handled);
      if (handled) return;
    }
    QAbstractSocket::setReadBufferSize(size);
  }

  //  qintptr QAbstractSocket::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQLocalUnixSocketCall7 call = reinterpret_cast<CuteQLocalUnixSocketCall7>(taken[7]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::socketDescriptor();
  }

  //  bool QAbstractSocket::setSocketDescriptor(qintptr socketDescriptor,
  //      SocketState state, OpenMode openMode)
  bool setSocketDescriptor(
      qintptr socketDescriptor,
      QAbstractSocket::SocketState state,
      QIODeviceBase::OpenMode openMode) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLocalUnixSocketCall8 call = reinterpret_cast<CuteQLocalUnixSocketCall8>(taken[8]);
      bool given = call(this, socketDescriptor, static_cast<int>(state), static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return QAbstractSocket::setSocketDescriptor(socketDescriptor, state, openMode);
  }

  //  void QAbstractSocket::setSocketOption(QAbstractSocket::SocketOption
  //      option, const QVariant &value)
  void setSocketOption(
      QAbstractSocket::SocketOption option,
      const QVariant &value) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLocalUnixSocketCall9 call = reinterpret_cast<CuteQLocalUnixSocketCall9>(taken[9]);
      call(this, static_cast<int>(option), &value, &handled);
      if (handled) return;
    }
    QAbstractSocket::setSocketOption(option, value);
  }

  //  QVariant QAbstractSocket::socketOption(QAbstractSocket::SocketOption
  //      option)
  QVariant socketOption(QAbstractSocket::SocketOption option) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLocalUnixSocketCall10 call = reinterpret_cast<CuteQLocalUnixSocketCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSocket::socketOption(option);
  }

  //  void QAbstractSocket::close()
  void close() override {
    if (taken[11]) {
      int handled = 0;
      CuteQLocalUnixSocketCall11 call = reinterpret_cast<CuteQLocalUnixSocketCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::close();
  }

  //  bool QAbstractSocket::isSequential() const
  bool isSequential() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQLocalUnixSocketCall12 call = reinterpret_cast<CuteQLocalUnixSocketCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::isSequential();
  }

  //  bool QAbstractSocket::waitForConnected(int msecs)
  bool waitForConnected(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLocalUnixSocketCall13 call = reinterpret_cast<CuteQLocalUnixSocketCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForConnected(msecs);
  }

  //  bool QAbstractSocket::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLocalUnixSocketCall14 call = reinterpret_cast<CuteQLocalUnixSocketCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForReadyRead(msecs);
  }

  //  bool QAbstractSocket::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLocalUnixSocketCall15 call = reinterpret_cast<CuteQLocalUnixSocketCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForBytesWritten(msecs);
  }

  //  bool QAbstractSocket::waitForDisconnected(int msecs)
  bool waitForDisconnected(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLocalUnixSocketCall16 call = reinterpret_cast<CuteQLocalUnixSocketCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForDisconnected(msecs);
  }

  //  qint64 QAbstractSocket::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLocalUnixSocketCall17 call = reinterpret_cast<CuteQLocalUnixSocketCall17>(taken[17]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::skipData(maxSize);
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLocalUnixSocketCall18 call = reinterpret_cast<CuteQLocalUnixSocketCall18>(taken[18]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQLocalUnixSocketCall19 call = reinterpret_cast<CuteQLocalUnixSocketCall19>(taken[19]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQLocalUnixSocketCall20 call = reinterpret_cast<CuteQLocalUnixSocketCall20>(taken[20]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLocalUnixSocketCall21 call = reinterpret_cast<CuteQLocalUnixSocketCall21>(taken[21]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQLocalUnixSocketCall22 call = reinterpret_cast<CuteQLocalUnixSocketCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[23]) {
      int handled = 0;
      CuteQLocalUnixSocketCall23 call = reinterpret_cast<CuteQLocalUnixSocketCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQLocalUnixSocketCall24 call = reinterpret_cast<CuteQLocalUnixSocketCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQLocalUnixSocketCall25 call = reinterpret_cast<CuteQLocalUnixSocketCall25>(taken[25]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQLocalUnixSocketCall26 call = reinterpret_cast<CuteQLocalUnixSocketCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQLocalUnixSocketCall27 call = reinterpret_cast<CuteQLocalUnixSocketCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQLocalUnixSocketCall28 call = reinterpret_cast<CuteQLocalUnixSocketCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQLocalUnixSocketCall29 call = reinterpret_cast<CuteQLocalUnixSocketCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQLocalUnixSocketCall30 call = reinterpret_cast<CuteQLocalUnixSocketCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQLocalUnixSocketCall31 call = reinterpret_cast<CuteQLocalUnixSocketCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QLocalUnixSocket::QLocalUnixSocket()
extern "C" Q_DECL_EXPORT
QLocalUnixSocket *ritual_ZN16QLocalUnixSocketC1Ev() {
  return new CuteQLocalUnixSocket();
}

//  void QLocalUnixSocket::setSocketState(QAbstractSocket::SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLocalUnixSocket14setSocketStateEN15QAbstractSocket11SocketStateE(
    QLocalUnixSocket *self,
    QAbstractSocket::SocketState state) {
  self->setSocketState(state);
}

//  void QLocalUnixSocket::setErrorString(const QString &string)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLocalUnixSocket14setErrorStringERK7QString(
    QLocalUnixSocket *self,
    const QString *string) {
  self->setErrorString(*string);
}

//  void QLocalUnixSocket::setSocketError(QAbstractSocket::SocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QLocalUnixSocket14setSocketErrorEN15QAbstractSocket11SocketErrorE(
    QLocalUnixSocket *self,
    QAbstractSocket::SocketError error) {
  self->setSocketError(error);
}

//  qint64 QLocalUnixSocket::writeData(const char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QLocalUnixSocket9writeDataEPKcx(
    QLocalUnixSocket *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  a Python function taken by a CuteQLocalUnixSocket, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLocalUnixSocket(
    QLocalUnixSocket *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLocalUnixSocket *>(self)->take(key, call);
}

#endif  // !defined(Q_OS_WIN) || defined(QT_LOCALSOCKET_TCP)
#endif  // QT_CONFIG(localserver)
