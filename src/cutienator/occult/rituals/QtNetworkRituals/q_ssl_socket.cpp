//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SSL)
#include <QtNetwork/qsslsocket.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qocspresponse.h>
#include <QtNetwork/qsslkey.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSslSocket may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSslSocket : QSslSocket {
  using QSslSocket::skipData;
};

//  A QSslSocket that Python can take functions over in. Every QSslSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SSL)
typedef void (*CuteQSslSocketCall0)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall1)(const void *, qintptr, int, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef void (*CuteQSslSocketCall2)(const void *, const QString *, quint16, int, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef void (*CuteQSslSocketCall3)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef void (*CuteQSslSocketCall4)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef const QVariant * (*CuteQSslSocketCall5)(const void *, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef qint64 (*CuteQSslSocketCall6)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef qint64 (*CuteQSslSocketCall7)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall8)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef void (*CuteQSslSocketCall9)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall10)(const void *, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef void (*CuteQSslSocketCall11)(const void *, qint64, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall12)(const void *, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall13)(const void *, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall14)(const void *, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall15)(const void *, int, int *);
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
typedef qint64 (*CuteQSslSocketCall16)(const void *, qint64, int *);
#endif  // !defined(QT_NO_SSL)
typedef bool (*CuteQSslSocketCall17)(const void *, const QHostAddress *, quint16, int, int *);
typedef qintptr (*CuteQSslSocketCall18)(const void *, int *);
typedef bool (*CuteQSslSocketCall19)(const void *, int *);
typedef bool (*CuteQSslSocketCall20)(const void *, int, int *);
typedef qint64 (*CuteQSslSocketCall21)(const void *, int *);
typedef qint64 (*CuteQSslSocketCall22)(const void *, int *);
typedef bool (*CuteQSslSocketCall23)(const void *, qint64, int *);
typedef bool (*CuteQSslSocketCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSslSocketCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSslSocketCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslSocketCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslSocketCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslSocketCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslSocketCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslSocketCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSslSocket : public QSslSocket {
public:
  using QSslSocket::QSslSocket;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket6resumeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket18disconnectFromHostEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket17setReadBufferSizeEx")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket16waitForConnectedEi")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket19waitForDisconnectedEi")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
#if !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_SSL)
    if (!std::strcmp(key, "_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindFlagEE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSocket16socketDescriptorEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
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

#if !defined(QT_NO_SSL)
  //  void QSslSocket::resume()
  void resume() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSslSocketCall0 call = reinterpret_cast<CuteQSslSocketCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSslSocket::resume();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::setSocketDescriptor(qintptr socketDescriptor,
  //      SocketState state, OpenMode openMode)
  bool setSocketDescriptor(
      qintptr socketDescriptor,
      QAbstractSocket::SocketState state,
      QIODeviceBase::OpenMode openMode) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSslSocketCall1 call = reinterpret_cast<CuteQSslSocketCall1>(taken[1]);
      bool given = call(this, socketDescriptor, static_cast<int>(state), static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return QSslSocket::setSocketDescriptor(socketDescriptor, state, openMode);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  void QSslSocket::connectToHost(const QString &hostName, quint16 port,
  //      OpenMode openMode, NetworkLayerProtocol protocol)
  void connectToHost(
      const QString &hostName,
      quint16 port,
      QIODeviceBase::OpenMode openMode,
      QAbstractSocket::NetworkLayerProtocol protocol) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSslSocketCall2 call = reinterpret_cast<CuteQSslSocketCall2>(taken[2]);
      call(this, &hostName, port, static_cast<int>(openMode.toInt()), static_cast<int>(protocol), &handled);
      if (handled) return;
    }
    QSslSocket::connectToHost(hostName, port, openMode, protocol);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  void QSslSocket::disconnectFromHost()
  void disconnectFromHost() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSslSocketCall3 call = reinterpret_cast<CuteQSslSocketCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QSslSocket::disconnectFromHost();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  void QSslSocket::setSocketOption(QAbstractSocket::SocketOption
  //      option, const QVariant &value)
  void setSocketOption(
      QAbstractSocket::SocketOption option,
      const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSslSocketCall4 call = reinterpret_cast<CuteQSslSocketCall4>(taken[4]);
      call(this, static_cast<int>(option), &value, &handled);
      if (handled) return;
    }
    QSslSocket::setSocketOption(option, value);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  QVariant QSslSocket::socketOption(QAbstractSocket::SocketOption
  //      option)
  QVariant socketOption(QAbstractSocket::SocketOption option) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSslSocketCall5 call = reinterpret_cast<CuteQSslSocketCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QSslSocket::socketOption(option);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  qint64 QSslSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSslSocketCall6 call = reinterpret_cast<CuteQSslSocketCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSslSocket::bytesAvailable();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  qint64 QSslSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSslSocketCall7 call = reinterpret_cast<CuteQSslSocketCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSslSocket::bytesToWrite();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::canReadLine() const
  bool canReadLine() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSslSocketCall8 call = reinterpret_cast<CuteQSslSocketCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSslSocket::canReadLine();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  void QSslSocket::close()
  void close() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSslSocketCall9 call = reinterpret_cast<CuteQSslSocketCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSslSocket::close();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::atEnd() const
  bool atEnd() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSslSocketCall10 call = reinterpret_cast<CuteQSslSocketCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSslSocket::atEnd();
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  void QSslSocket::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSslSocketCall11 call = reinterpret_cast<CuteQSslSocketCall11>(taken[11]);
      call(this, size, &handled);
      if (handled) return;
    }
    QSslSocket::setReadBufferSize(size);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::waitForConnected(int msecs)
  bool waitForConnected(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSslSocketCall12 call = reinterpret_cast<CuteQSslSocketCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QSslSocket::waitForConnected(msecs);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSslSocketCall13 call = reinterpret_cast<CuteQSslSocketCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QSslSocket::waitForReadyRead(msecs);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSslSocketCall14 call = reinterpret_cast<CuteQSslSocketCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QSslSocket::waitForBytesWritten(msecs);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  bool QSslSocket::waitForDisconnected(int msecs)
  bool waitForDisconnected(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSslSocketCall15 call = reinterpret_cast<CuteQSslSocketCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QSslSocket::waitForDisconnected(msecs);
  }
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
  //  qint64 QSslSocket::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSslSocketCall16 call = reinterpret_cast<CuteQSslSocketCall16>(taken[16]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QSslSocket::skipData(maxSize);
  }
#endif  // !defined(QT_NO_SSL)

  //  bool QAbstractSocket::bind(const QHostAddress &address, quint16 port,
  //      BindMode mode)
  bool bind(
      const QHostAddress &address,
      quint16 port,
      QAbstractSocket::BindMode mode) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSslSocketCall17 call = reinterpret_cast<CuteQSslSocketCall17>(taken[17]);
      bool given = call(this, &address, port, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bind(address, port, mode);
  }

  //  qintptr QAbstractSocket::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSslSocketCall18 call = reinterpret_cast<CuteQSslSocketCall18>(taken[18]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::socketDescriptor();
  }

  //  bool QAbstractSocket::isSequential() const
  bool isSequential() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSslSocketCall19 call = reinterpret_cast<CuteQSslSocketCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::isSequential();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[20]) {
      int handled = 0;
      CuteQSslSocketCall20 call = reinterpret_cast<CuteQSslSocketCall20>(taken[20]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQSslSocketCall21 call = reinterpret_cast<CuteQSslSocketCall21>(taken[21]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSslSocketCall22 call = reinterpret_cast<CuteQSslSocketCall22>(taken[22]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSslSocketCall23 call = reinterpret_cast<CuteQSslSocketCall23>(taken[23]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[24]) {
      int handled = 0;
      CuteQSslSocketCall24 call = reinterpret_cast<CuteQSslSocketCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSslSocketCall25 call = reinterpret_cast<CuteQSslSocketCall25>(taken[25]);
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
      CuteQSslSocketCall26 call = reinterpret_cast<CuteQSslSocketCall26>(taken[26]);
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
      CuteQSslSocketCall27 call = reinterpret_cast<CuteQSslSocketCall27>(taken[27]);
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
      CuteQSslSocketCall28 call = reinterpret_cast<CuteQSslSocketCall28>(taken[28]);
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
      CuteQSslSocketCall29 call = reinterpret_cast<CuteQSslSocketCall29>(taken[29]);
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
      CuteQSslSocketCall30 call = reinterpret_cast<CuteQSslSocketCall30>(taken[30]);
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
      CuteQSslSocketCall31 call = reinterpret_cast<CuteQSslSocketCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSslSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QSslSocket10metaObjectEv(
    const QSslSocket *self) {
  return self->metaObject();
}

//  QString QSslSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSslSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSslSocket::tr(s, c, n));
}

//  QSslSocket::QSslSocket(QObject *parent)
extern "C" Q_DECL_EXPORT
QSslSocket *ritual_ZN10QSslSocketC1EP7QObject(QObject *parent) {
  return new CuteQSslSocket(parent);
}

//  QSslSocket::~QSslSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocketD1Ev(QSslSocket *self) {
  delete self;
}

//  void QSslSocket::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket6resumeEv(QSslSocket *self) {
  self->resume();
}

//  void QSslSocket::connectToHostEncrypted(const QString &hostName, quint16
//      port, OpenMode mode, NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket22connectToHostEncryptedERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerProtocolE(
    QSslSocket *self,
    const QString *hostName,
    quint16 port,
    int mode,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->connectToHostEncrypted(
      *hostName,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode),
      protocol);
}

//  void QSslSocket::connectToHostEncrypted(const QString &hostName, quint16
//      port, const QString &sslPeerName, OpenMode mode, NetworkLayerProtocol
//      protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket22connectToHostEncryptedERK7QStringtS2_6QFlagsIN13QIODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerProtocolE(
    QSslSocket *self,
    const QString *hostName,
    quint16 port,
    const QString *sslPeerName,
    int mode,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->connectToHostEncrypted(
      *hostName,
      port,
      *sslPeerName,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode),
      protocol);
}

//  bool QSslSocket::setSocketDescriptor(qintptr socketDescriptor,
//      SocketState state, OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket19setSocketDescriptorExN15QAbstractSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSslSocket *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState state,
    int openMode) {
  return self->setSocketDescriptor(
      socketDescriptor,
      state,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QSslSocket::connectToHost(const QString &hostName, quint16 port,
//      OpenMode openMode, NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerProtocolE(
    QSslSocket *self,
    const QString *hostName,
    quint16 port,
    int openMode,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->connectToHost(
      *hostName,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode),
      protocol);
}

//  void QSslSocket::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket18disconnectFromHostEv(QSslSocket *self) {
  self->disconnectFromHost();
}

//  void QSslSocket::setSocketOption(QAbstractSocket::SocketOption option,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket15setSocketOptionEN15QAbstractSocket12SocketOptionERK8QVariant(
    QSslSocket *self,
    QAbstractSocket::SocketOption option,
    const QVariant *value) {
  self->setSocketOption(option, *value);
}

//  QVariant QSslSocket::socketOption(QAbstractSocket::SocketOption option)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN10QSslSocket12socketOptionEN15QAbstractSocket12SocketOptionE(
    QSslSocket *self,
    QAbstractSocket::SocketOption option) {
  return new QVariant(self->socketOption(option));
}

//  SslMode QSslSocket::mode() const
extern "C" Q_DECL_EXPORT
QSslSocket::SslMode ritual_ZNK10QSslSocket4modeEv(const QSslSocket *self) {
  return self->mode();
}

//  bool QSslSocket::isEncrypted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSslSocket11isEncryptedEv(const QSslSocket *self) {
  return self->isEncrypted();
}

//  QSsl::SslProtocol QSslSocket::protocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK10QSslSocket8protocolEv(const QSslSocket *self) {
  return self->protocol();
}

//  void QSslSocket::setProtocol(QSsl::SslProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket11setProtocolEN4QSsl11SslProtocolE(
    QSslSocket *self,
    QSsl::SslProtocol protocol) {
  self->setProtocol(protocol);
}

//  QSslSocket::PeerVerifyMode QSslSocket::peerVerifyMode() const
extern "C" Q_DECL_EXPORT
QSslSocket::PeerVerifyMode ritual_ZNK10QSslSocket14peerVerifyModeEv(
    const QSslSocket *self) {
  return self->peerVerifyMode();
}

//  void QSslSocket::setPeerVerifyMode(QSslSocket::PeerVerifyMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket17setPeerVerifyModeENS_14PeerVerifyModeE(
    QSslSocket *self,
    QSslSocket::PeerVerifyMode mode) {
  self->setPeerVerifyMode(mode);
}

//  int QSslSocket::peerVerifyDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSslSocket15peerVerifyDepthEv(const QSslSocket *self) {
  return self->peerVerifyDepth();
}

//  void QSslSocket::setPeerVerifyDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket18setPeerVerifyDepthEi(
    QSslSocket *self,
    int depth) {
  self->setPeerVerifyDepth(depth);
}

//  QString QSslSocket::peerVerifyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QSslSocket14peerVerifyNameEv(const QSslSocket *self) {
  return new QString(self->peerVerifyName());
}

//  void QSslSocket::setPeerVerifyName(const QString &hostName)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket17setPeerVerifyNameERK7QString(
    QSslSocket *self,
    const QString *hostName) {
  self->setPeerVerifyName(*hostName);
}

//  qint64 QSslSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QSslSocket14bytesAvailableEv(const QSslSocket *self) {
  return self->bytesAvailable();
}

//  qint64 QSslSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QSslSocket12bytesToWriteEv(const QSslSocket *self) {
  return self->bytesToWrite();
}

//  bool QSslSocket::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSslSocket11canReadLineEv(const QSslSocket *self) {
  return self->canReadLine();
}

//  void QSslSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket5closeEv(QSslSocket *self) {
  self->close();
}

//  bool QSslSocket::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QSslSocket5atEndEv(const QSslSocket *self) {
  return self->atEnd();
}

//  void QSslSocket::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket17setReadBufferSizeEx(
    QSslSocket *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  qint64 QSslSocket::encryptedBytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QSslSocket23encryptedBytesAvailableEv(
    const QSslSocket *self) {
  return self->encryptedBytesAvailable();
}

//  qint64 QSslSocket::encryptedBytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QSslSocket21encryptedBytesToWriteEv(
    const QSslSocket *self) {
  return self->encryptedBytesToWrite();
}

//  QSslConfiguration QSslSocket::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK10QSslSocket16sslConfigurationEv(
    const QSslSocket *self) {
  return new QSslConfiguration(self->sslConfiguration());
}

//  void QSslSocket::setSslConfiguration(const QSslConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket19setSslConfigurationERK17QSslConfiguration(
    QSslSocket *self,
    const QSslConfiguration *config) {
  self->setSslConfiguration(*config);
}

//  void QSslSocket::setLocalCertificateChain(const QList<QSslCertificate>
//      &localChain)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket24setLocalCertificateChainERK5QListI15QSslCertificateE(
    QSslSocket *self,
    const QList<QSslCertificate> *localChain) {
  self->setLocalCertificateChain(*localChain);
}

//  QList<QSslCertificate> QSslSocket::localCertificateChain() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK10QSslSocket21localCertificateChainEv(
    const QSslSocket *self) {
  return new QList<QSslCertificate>(self->localCertificateChain());
}

//  void QSslSocket::setLocalCertificate(const QSslCertificate &certificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket19setLocalCertificateERK15QSslCertificate(
    QSslSocket *self,
    const QSslCertificate *certificate) {
  self->setLocalCertificate(*certificate);
}

//  void QSslSocket::setLocalCertificate(const QString &fileName,
//      QSsl::EncodingFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket19setLocalCertificateERK7QStringN4QSsl14EncodingFormatE(
    QSslSocket *self,
    const QString *fileName,
    QSsl::EncodingFormat format) {
  self->setLocalCertificate(*fileName, format);
}

//  QSslCertificate QSslSocket::localCertificate() const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZNK10QSslSocket16localCertificateEv(
    const QSslSocket *self) {
  return new QSslCertificate(self->localCertificate());
}

//  QSslCertificate QSslSocket::peerCertificate() const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZNK10QSslSocket15peerCertificateEv(
    const QSslSocket *self) {
  return new QSslCertificate(self->peerCertificate());
}

//  QList<QSslCertificate> QSslSocket::peerCertificateChain() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK10QSslSocket20peerCertificateChainEv(
    const QSslSocket *self) {
  return new QList<QSslCertificate>(self->peerCertificateChain());
}

//  QSslCipher QSslSocket::sessionCipher() const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZNK10QSslSocket13sessionCipherEv(const QSslSocket *self) {
  return new QSslCipher(self->sessionCipher());
}

//  QSsl::SslProtocol QSslSocket::sessionProtocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK10QSslSocket15sessionProtocolEv(
    const QSslSocket *self) {
  return self->sessionProtocol();
}

//  QList<QOcspResponse> QSslSocket::ocspResponses() const
extern "C" Q_DECL_EXPORT
QList<QOcspResponse> *ritual_ZNK10QSslSocket13ocspResponsesEv(
    const QSslSocket *self) {
  return new QList<QOcspResponse>(self->ocspResponses());
}

//  void QSslSocket::setPrivateKey(const QSslKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket13setPrivateKeyERK7QSslKey(
    QSslSocket *self,
    const QSslKey *key) {
  self->setPrivateKey(*key);
}

//  void QSslSocket::setPrivateKey(const QString &fileName,
//      QSsl::KeyAlgorithm algorithm, QSsl::EncodingFormat format, const
//      QByteArray &passPhrase)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket13setPrivateKeyERK7QStringN4QSsl12KeyAlgorithmENS3_14EncodingFormatERK10QByteArray(
    QSslSocket *self,
    const QString *fileName,
    QSsl::KeyAlgorithm algorithm,
    QSsl::EncodingFormat format,
    const QByteArray *passPhrase) {
  self->setPrivateKey(*fileName, algorithm, format, *passPhrase);
}

//  QSslKey QSslSocket::privateKey() const
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZNK10QSslSocket10privateKeyEv(const QSslSocket *self) {
  return new QSslKey(self->privateKey());
}

//  bool QSslSocket::waitForConnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket16waitForConnectedEi(QSslSocket *self, int msecs) {
  return self->waitForConnected(msecs);
}

//  bool QSslSocket::waitForEncrypted(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket16waitForEncryptedEi(QSslSocket *self, int msecs) {
  return self->waitForEncrypted(msecs);
}

//  bool QSslSocket::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket16waitForReadyReadEi(QSslSocket *self, int msecs) {
  return self->waitForReadyRead(msecs);
}

//  bool QSslSocket::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket19waitForBytesWrittenEi(
    QSslSocket *self,
    int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QSslSocket::waitForDisconnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket19waitForDisconnectedEi(
    QSslSocket *self,
    int msecs) {
  return self->waitForDisconnected(msecs);
}

//  QList<QSslError> QSslSocket::sslHandshakeErrors() const
extern "C" Q_DECL_EXPORT
QList<QSslError> *ritual_ZNK10QSslSocket18sslHandshakeErrorsEv(
    const QSslSocket *self) {
  return new QList<QSslError>(self->sslHandshakeErrors());
}

//  bool QSslSocket::supportsSsl()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket11supportsSslEv() {
  return QSslSocket::supportsSsl();
}

//  long QSslSocket::sslLibraryVersionNumber()
extern "C" Q_DECL_EXPORT
long ritual_ZN10QSslSocket23sslLibraryVersionNumberEv() {
  return QSslSocket::sslLibraryVersionNumber();
}

//  QString QSslSocket::sslLibraryVersionString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSslSocket23sslLibraryVersionStringEv() {
  return new QString(QSslSocket::sslLibraryVersionString());
}

//  long QSslSocket::sslLibraryBuildVersionNumber()
extern "C" Q_DECL_EXPORT
long ritual_ZN10QSslSocket28sslLibraryBuildVersionNumberEv() {
  return QSslSocket::sslLibraryBuildVersionNumber();
}

//  QString QSslSocket::sslLibraryBuildVersionString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSslSocket28sslLibraryBuildVersionStringEv() {
  return new QString(QSslSocket::sslLibraryBuildVersionString());
}

//  QList<QString> QSslSocket::availableBackends()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN10QSslSocket17availableBackendsEv() {
  return new QList<QString>(QSslSocket::availableBackends());
}

//  QString QSslSocket::activeBackend()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSslSocket13activeBackendEv() {
  return new QString(QSslSocket::activeBackend());
}

//  bool QSslSocket::setActiveBackend(const QString &backendName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket16setActiveBackendERK7QString(
    const QString *backendName) {
  return QSslSocket::setActiveBackend(*backendName);
}

//  bool QSslSocket::isProtocolSupported(QSsl::SslProtocol protocol, const
//      QString &backendName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket19isProtocolSupportedEN4QSsl11SslProtocolERK7QString(
    QSsl::SslProtocol protocol,
    const QString *backendName) {
  return QSslSocket::isProtocolSupported(protocol, *backendName);
}

//  bool QSslSocket::isClassImplemented(QSsl::ImplementedClass cl, const
//      QString &backendName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket18isClassImplementedEN4QSsl16ImplementedClassERK7QString(
    QSsl::ImplementedClass cl,
    const QString *backendName) {
  return QSslSocket::isClassImplemented(cl, *backendName);
}

//  bool QSslSocket::isFeatureSupported(QSsl::SupportedFeature feat, const
//      QString &backendName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSslSocket18isFeatureSupportedEN4QSsl16SupportedFeatureERK7QString(
    QSsl::SupportedFeature feat,
    const QString *backendName) {
  return QSslSocket::isFeatureSupported(feat, *backendName);
}

//  void QSslSocket::ignoreSslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket15ignoreSslErrorsERK5QListI9QSslErrorE(
    QSslSocket *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}

//  void QSslSocket::continueInterruptedHandshake()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket28continueInterruptedHandshakeEv(
    QSslSocket *self) {
  self->continueInterruptedHandshake();
}

//  void QSslSocket::startClientEncryption()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket21startClientEncryptionEv(QSslSocket *self) {
  self->startClientEncryption();
}

//  void QSslSocket::startServerEncryption()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket21startServerEncryptionEv(QSslSocket *self) {
  self->startServerEncryption();
}

//  void QSslSocket::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslSocket15ignoreSslErrorsEv(QSslSocket *self) {
  self->ignoreSslErrors();
}

//  qint64 QSslSocket::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN10QSslSocket8skipDataEx(QSslSocket *self, qint64 maxSize) {
  return self->skipData(maxSize);
}

//  qint64 QSslSocket::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN10QSslSocket9writeDataEPKcx(
    QSslSocket *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  QSslSocketPrivate *QSslSocket::d_func()
extern "C" Q_DECL_EXPORT
QSslSocketPrivate *ritual_ZN10QSslSocket6d_funcEv(QSslSocket *self) {
  return self->d_func();
}

//  const QSslSocketPrivate *QSslSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QSslSocketPrivate *ritual_ZNK10QSslSocket6d_funcEv(
    const QSslSocket *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSslSocket, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSslSocket(QSslSocket *self, const char *key, void *call) {
  return static_cast<CuteQSslSocket *>(self)->take(key, call);
}

//  void QSslSocket::resume()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslSocket6resumeEv(QSslSocket *self) {
  self->QSslSocket::resume();
}

//  bool QSslSocket::setSocketDescriptor(qintptr socketDescriptor,
//      SocketState state, OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSslSocket19setSocketDescriptorExN15QAbstractSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSslSocket *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState state,
    int openMode) {
  return self->QSslSocket::setSocketDescriptor(
      socketDescriptor,
      state,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QSslSocket::connectToHost(const QString &hostName, quint16 port,
//      OpenMode openMode, NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEEN15QAbstractSocket20NetworkLayerProtocolE(
    QSslSocket *self,
    const QString *hostName,
    quint16 port,
    int openMode,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->QSslSocket::connectToHost(
      *hostName,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode),
      protocol);
}

//  void QSslSocket::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslSocket18disconnectFromHostEv(QSslSocket *self) {
  self->QSslSocket::disconnectFromHost();
}

//  void QSslSocket::setSocketOption(QAbstractSocket::SocketOption option,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslSocket15setSocketOptionEN15QAbstractSocket12SocketOptionERK8QVariant(
    QSslSocket *self,
    QAbstractSocket::SocketOption option,
    const QVariant *value) {
  self->QSslSocket::setSocketOption(option, *value);
}

//  QVariant QSslSocket::socketOption(QAbstractSocket::SocketOption option)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN10QSslSocket12socketOptionEN15QAbstractSocket12SocketOptionE(
    QSslSocket *self,
    QAbstractSocket::SocketOption option) {
  return new QVariant(self->QSslSocket::socketOption(option));
}

//  qint64 QSslSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK10QSslSocket14bytesAvailableEv(const QSslSocket *self) {
  return self->QSslSocket::bytesAvailable();
}

//  qint64 QSslSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK10QSslSocket12bytesToWriteEv(const QSslSocket *self) {
  return self->QSslSocket::bytesToWrite();
}

//  bool QSslSocket::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QSslSocket11canReadLineEv(const QSslSocket *self) {
  return self->QSslSocket::canReadLine();
}

//  void QSslSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslSocket5closeEv(QSslSocket *self) {
  self->QSslSocket::close();
}

//  bool QSslSocket::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QSslSocket5atEndEv(const QSslSocket *self) {
  return self->QSslSocket::atEnd();
}

//  void QSslSocket::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslSocket17setReadBufferSizeEx(
    QSslSocket *self,
    qint64 size) {
  self->QSslSocket::setReadBufferSize(size);
}

//  bool QSslSocket::waitForConnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSslSocket16waitForConnectedEi(
    QSslSocket *self,
    int msecs) {
  return self->QSslSocket::waitForConnected(msecs);
}

//  bool QSslSocket::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSslSocket16waitForReadyReadEi(
    QSslSocket *self,
    int msecs) {
  return self->QSslSocket::waitForReadyRead(msecs);
}

//  bool QSslSocket::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSslSocket19waitForBytesWrittenEi(
    QSslSocket *self,
    int msecs) {
  return self->QSslSocket::waitForBytesWritten(msecs);
}

//  bool QSslSocket::waitForDisconnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QSslSocket19waitForDisconnectedEi(
    QSslSocket *self,
    int msecs) {
  return self->QSslSocket::waitForDisconnected(msecs);
}

//  qint64 QSslSocket::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN10QSslSocket8skipDataEx(
    QSslSocket *self,
    qint64 maxSize) {
  return static_cast<OwnQSslSocket *>(self)->OwnQSslSocket::skipData(
      maxSize);
}

#endif  // !defined(QT_NO_SSL)
