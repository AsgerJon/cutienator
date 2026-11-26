//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qtcpsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtcpsocket.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTcpSocket that Python can take functions over in. Every QTcpSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTcpSocketCall0)(const void *, int *);
typedef bool (*CuteQTcpSocketCall1)(const void *, const QHostAddress *, quint16, int, int *);
typedef void (*CuteQTcpSocketCall2)(const void *, const QString *, quint16, int, int, int *);
typedef void (*CuteQTcpSocketCall3)(const void *, int *);
typedef qint64 (*CuteQTcpSocketCall4)(const void *, int *);
typedef qint64 (*CuteQTcpSocketCall5)(const void *, int *);
typedef void (*CuteQTcpSocketCall6)(const void *, qint64, int *);
typedef qintptr (*CuteQTcpSocketCall7)(const void *, int *);
typedef bool (*CuteQTcpSocketCall8)(const void *, qintptr, int, int, int *);
typedef void (*CuteQTcpSocketCall9)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQTcpSocketCall10)(const void *, int, int *);
typedef void (*CuteQTcpSocketCall11)(const void *, int *);
typedef bool (*CuteQTcpSocketCall12)(const void *, int *);
typedef bool (*CuteQTcpSocketCall13)(const void *, int, int *);
typedef bool (*CuteQTcpSocketCall14)(const void *, int, int *);
typedef bool (*CuteQTcpSocketCall15)(const void *, int, int *);
typedef bool (*CuteQTcpSocketCall16)(const void *, int, int *);
typedef qint64 (*CuteQTcpSocketCall17)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQTcpSocketCall18)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQTcpSocketCall19)(const void *, qint64, int *);
typedef bool (*CuteQTcpSocketCall20)(const void *, int, int *);
typedef qint64 (*CuteQTcpSocketCall21)(const void *, int *);
typedef qint64 (*CuteQTcpSocketCall22)(const void *, int *);
typedef bool (*CuteQTcpSocketCall23)(const void *, qint64, int *);
typedef bool (*CuteQTcpSocketCall24)(const void *, int *);
typedef bool (*CuteQTcpSocketCall25)(const void *, int *);
typedef bool (*CuteQTcpSocketCall26)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTcpSocketCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTcpSocketCall28)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpSocketCall29)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpSocketCall30)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpSocketCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpSocketCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpSocketCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTcpSocket : public QTcpSocket {
public:
  using QTcpSocket::QTcpSocket;
  void *taken[34] = {};

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
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
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
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[26] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstractSocket::resume()
  void resume() override {
    if (taken[0]) {
      int handled = 0;
      CuteQTcpSocketCall0 call = reinterpret_cast<CuteQTcpSocketCall0>(taken[0]);
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
      CuteQTcpSocketCall1 call = reinterpret_cast<CuteQTcpSocketCall1>(taken[1]);
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
      CuteQTcpSocketCall2 call = reinterpret_cast<CuteQTcpSocketCall2>(taken[2]);
      call(this, &hostName, port, static_cast<int>(mode.toInt()), static_cast<int>(protocol), &handled);
      if (handled) return;
    }
    QAbstractSocket::connectToHost(hostName, port, mode, protocol);
  }

  //  void QAbstractSocket::disconnectFromHost()
  void disconnectFromHost() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTcpSocketCall3 call = reinterpret_cast<CuteQTcpSocketCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::disconnectFromHost();
  }

  //  qint64 QAbstractSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTcpSocketCall4 call = reinterpret_cast<CuteQTcpSocketCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesAvailable();
  }

  //  qint64 QAbstractSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTcpSocketCall5 call = reinterpret_cast<CuteQTcpSocketCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesToWrite();
  }

  //  void QAbstractSocket::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTcpSocketCall6 call = reinterpret_cast<CuteQTcpSocketCall6>(taken[6]);
      call(this, size, &handled);
      if (handled) return;
    }
    QAbstractSocket::setReadBufferSize(size);
  }

  //  qintptr QAbstractSocket::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTcpSocketCall7 call = reinterpret_cast<CuteQTcpSocketCall7>(taken[7]);
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
      CuteQTcpSocketCall8 call = reinterpret_cast<CuteQTcpSocketCall8>(taken[8]);
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
      CuteQTcpSocketCall9 call = reinterpret_cast<CuteQTcpSocketCall9>(taken[9]);
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
      CuteQTcpSocketCall10 call = reinterpret_cast<CuteQTcpSocketCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSocket::socketOption(option);
  }

  //  void QAbstractSocket::close()
  void close() override {
    if (taken[11]) {
      int handled = 0;
      CuteQTcpSocketCall11 call = reinterpret_cast<CuteQTcpSocketCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::close();
  }

  //  bool QAbstractSocket::isSequential() const
  bool isSequential() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTcpSocketCall12 call = reinterpret_cast<CuteQTcpSocketCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::isSequential();
  }

  //  bool QAbstractSocket::waitForConnected(int msecs)
  bool waitForConnected(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTcpSocketCall13 call = reinterpret_cast<CuteQTcpSocketCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForConnected(msecs);
  }

  //  bool QAbstractSocket::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTcpSocketCall14 call = reinterpret_cast<CuteQTcpSocketCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForReadyRead(msecs);
  }

  //  bool QAbstractSocket::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTcpSocketCall15 call = reinterpret_cast<CuteQTcpSocketCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForBytesWritten(msecs);
  }

  //  bool QAbstractSocket::waitForDisconnected(int msecs)
  bool waitForDisconnected(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTcpSocketCall16 call = reinterpret_cast<CuteQTcpSocketCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForDisconnected(msecs);
  }

  //  qint64 QAbstractSocket::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTcpSocketCall17 call = reinterpret_cast<CuteQTcpSocketCall17>(taken[17]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::readData(data, maxlen);
  }

  //  qint64 QAbstractSocket::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTcpSocketCall18 call = reinterpret_cast<CuteQTcpSocketCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::readLineData(data, maxlen);
  }

  //  qint64 QAbstractSocket::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTcpSocketCall19 call = reinterpret_cast<CuteQTcpSocketCall19>(taken[19]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::skipData(maxSize);
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTcpSocketCall20 call = reinterpret_cast<CuteQTcpSocketCall20>(taken[20]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTcpSocketCall21 call = reinterpret_cast<CuteQTcpSocketCall21>(taken[21]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTcpSocketCall22 call = reinterpret_cast<CuteQTcpSocketCall22>(taken[22]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTcpSocketCall23 call = reinterpret_cast<CuteQTcpSocketCall23>(taken[23]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTcpSocketCall24 call = reinterpret_cast<CuteQTcpSocketCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[25]) {
      int handled = 0;
      CuteQTcpSocketCall25 call = reinterpret_cast<CuteQTcpSocketCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQTcpSocketCall26 call = reinterpret_cast<CuteQTcpSocketCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQTcpSocketCall27 call = reinterpret_cast<CuteQTcpSocketCall27>(taken[27]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQTcpSocketCall28 call = reinterpret_cast<CuteQTcpSocketCall28>(taken[28]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQTcpSocketCall29 call = reinterpret_cast<CuteQTcpSocketCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQTcpSocketCall30 call = reinterpret_cast<CuteQTcpSocketCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQTcpSocketCall31 call = reinterpret_cast<CuteQTcpSocketCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQTcpSocketCall32 call = reinterpret_cast<CuteQTcpSocketCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQTcpSocketCall33 call = reinterpret_cast<CuteQTcpSocketCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTcpSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTcpSocket10metaObjectEv(
    const QTcpSocket *self) {
  return self->metaObject();
}

//  void *QTcpSocket::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QTcpSocket11qt_metacastEPKc(
    QTcpSocket *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTcpSocket::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QTcpSocket11qt_metacallEN11QMetaObject4CallEiPPv(
    QTcpSocket *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTcpSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTcpSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTcpSocket::tr(s, c, n));
}

//  QTcpSocket::QTcpSocket(QObject *parent)
extern "C" Q_DECL_EXPORT
QTcpSocket *ritual_ZN10QTcpSocketC1EP7QObject(QObject *parent) {
  return new CuteQTcpSocket(parent);
}

//  QTcpSocket::~QTcpSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpSocketD1Ev(QTcpSocket *self) {
  delete self;
}

#if QT_VERSION < QT_VERSION_CHECK(7,0,0) && !defined(Q_QDOC)
//  bool QTcpSocket::bind(QHostAddress::SpecialAddress addr, quint16 port,
//      BindMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTcpSocket4bindEN12QHostAddress14SpecialAddressEt6QFlagsIN15QAbstractSocket8BindFlagEE(
    QTcpSocket *self,
    QHostAddress::SpecialAddress addr,
    quint16 port,
    int mode) {
  return self->bind(
      addr,
      port,
      QFlags<QAbstractSocket::BindFlag>::fromInt(mode));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7,0,0) && !defined(Q_QDOC)

//  QTcpSocket::QTcpSocket(QTcpSocketPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QTcpSocket *ritual_ZN10QTcpSocketC1ER17QTcpSocketPrivateP7QObject(
    QTcpSocketPrivate *dd,
    QObject *parent) {
  return new CuteQTcpSocket(*dd, parent);
}

//  QTcpSocket::QTcpSocket(QAbstractSocket::SocketType socketType,
//      QTcpSocketPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QTcpSocket *ritual_ZN10QTcpSocketC1EN15QAbstractSocket10SocketTypeER17QTcpSocketPrivateP7QObject(
    QAbstractSocket::SocketType socketType,
    QTcpSocketPrivate *dd,
    QObject *parent) {
  return new CuteQTcpSocket(socketType, *dd, parent);
}

//  QTcpSocketPrivate *QTcpSocket::d_func()
extern "C" Q_DECL_EXPORT
QTcpSocketPrivate *ritual_ZN10QTcpSocket6d_funcEv(QTcpSocket *self) {
  return self->d_func();
}

//  const QTcpSocketPrivate *QTcpSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QTcpSocketPrivate *ritual_ZNK10QTcpSocket6d_funcEv(
    const QTcpSocket *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTcpSocket, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTcpSocket(QTcpSocket *self, const char *key, void *call) {
  return static_cast<CuteQTcpSocket *>(self)->take(key, call);
}
