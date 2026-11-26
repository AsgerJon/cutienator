//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qabstractsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qabstractsocket.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qvariant.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAbstractSocket may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractSocket : QAbstractSocket {
  using QAbstractSocket::readData;
  using QAbstractSocket::readLineData;
  using QAbstractSocket::skipData;
};

//  A QAbstractSocket that Python can take functions over in. Every QAbstractSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractSocketCall0)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall1)(const void *, const QHostAddress *, quint16, int, int *);
typedef void (*CuteQAbstractSocketCall2)(const void *, const QString *, quint16, int, int, int *);
typedef void (*CuteQAbstractSocketCall3)(const void *, int *);
typedef qint64 (*CuteQAbstractSocketCall4)(const void *, int *);
typedef qint64 (*CuteQAbstractSocketCall5)(const void *, int *);
typedef void (*CuteQAbstractSocketCall6)(const void *, qint64, int *);
typedef qintptr (*CuteQAbstractSocketCall7)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall8)(const void *, qintptr, int, int, int *);
typedef void (*CuteQAbstractSocketCall9)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQAbstractSocketCall10)(const void *, int, int *);
typedef void (*CuteQAbstractSocketCall11)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall12)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall13)(const void *, int, int *);
typedef bool (*CuteQAbstractSocketCall14)(const void *, int, int *);
typedef bool (*CuteQAbstractSocketCall15)(const void *, int, int *);
typedef bool (*CuteQAbstractSocketCall16)(const void *, int, int *);
typedef qint64 (*CuteQAbstractSocketCall17)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQAbstractSocketCall18)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQAbstractSocketCall19)(const void *, qint64, int *);
typedef bool (*CuteQAbstractSocketCall20)(const void *, int, int *);
typedef qint64 (*CuteQAbstractSocketCall21)(const void *, int *);
typedef qint64 (*CuteQAbstractSocketCall22)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall23)(const void *, qint64, int *);
typedef bool (*CuteQAbstractSocketCall24)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall25)(const void *, int *);
typedef bool (*CuteQAbstractSocketCall26)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSocketCall27)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractSocketCall28)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSocketCall29)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSocketCall30)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSocketCall31)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSocketCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractSocketCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractSocket : public QAbstractSocket {
public:
  using QAbstractSocket::QAbstractSocket;
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
      CuteQAbstractSocketCall0 call = reinterpret_cast<CuteQAbstractSocketCall0>(taken[0]);
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
      CuteQAbstractSocketCall1 call = reinterpret_cast<CuteQAbstractSocketCall1>(taken[1]);
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
      CuteQAbstractSocketCall2 call = reinterpret_cast<CuteQAbstractSocketCall2>(taken[2]);
      call(this, &hostName, port, static_cast<int>(mode.toInt()), static_cast<int>(protocol), &handled);
      if (handled) return;
    }
    QAbstractSocket::connectToHost(hostName, port, mode, protocol);
  }

  //  void QAbstractSocket::disconnectFromHost()
  void disconnectFromHost() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSocketCall3 call = reinterpret_cast<CuteQAbstractSocketCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::disconnectFromHost();
  }

  //  qint64 QAbstractSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSocketCall4 call = reinterpret_cast<CuteQAbstractSocketCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesAvailable();
  }

  //  qint64 QAbstractSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSocketCall5 call = reinterpret_cast<CuteQAbstractSocketCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesToWrite();
  }

  //  void QAbstractSocket::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSocketCall6 call = reinterpret_cast<CuteQAbstractSocketCall6>(taken[6]);
      call(this, size, &handled);
      if (handled) return;
    }
    QAbstractSocket::setReadBufferSize(size);
  }

  //  qintptr QAbstractSocket::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSocketCall7 call = reinterpret_cast<CuteQAbstractSocketCall7>(taken[7]);
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
      CuteQAbstractSocketCall8 call = reinterpret_cast<CuteQAbstractSocketCall8>(taken[8]);
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
      CuteQAbstractSocketCall9 call = reinterpret_cast<CuteQAbstractSocketCall9>(taken[9]);
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
      CuteQAbstractSocketCall10 call = reinterpret_cast<CuteQAbstractSocketCall10>(taken[10]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSocket::socketOption(option);
  }

  //  void QAbstractSocket::close()
  void close() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSocketCall11 call = reinterpret_cast<CuteQAbstractSocketCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocket::close();
  }

  //  bool QAbstractSocket::isSequential() const
  bool isSequential() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSocketCall12 call = reinterpret_cast<CuteQAbstractSocketCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::isSequential();
  }

  //  bool QAbstractSocket::waitForConnected(int msecs)
  bool waitForConnected(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractSocketCall13 call = reinterpret_cast<CuteQAbstractSocketCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForConnected(msecs);
  }

  //  bool QAbstractSocket::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractSocketCall14 call = reinterpret_cast<CuteQAbstractSocketCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForReadyRead(msecs);
  }

  //  bool QAbstractSocket::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractSocketCall15 call = reinterpret_cast<CuteQAbstractSocketCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForBytesWritten(msecs);
  }

  //  bool QAbstractSocket::waitForDisconnected(int msecs)
  bool waitForDisconnected(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractSocketCall16 call = reinterpret_cast<CuteQAbstractSocketCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForDisconnected(msecs);
  }

  //  qint64 QAbstractSocket::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractSocketCall17 call = reinterpret_cast<CuteQAbstractSocketCall17>(taken[17]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::readData(data, maxlen);
  }

  //  qint64 QAbstractSocket::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractSocketCall18 call = reinterpret_cast<CuteQAbstractSocketCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::readLineData(data, maxlen);
  }

  //  qint64 QAbstractSocket::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractSocketCall19 call = reinterpret_cast<CuteQAbstractSocketCall19>(taken[19]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::skipData(maxSize);
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractSocketCall20 call = reinterpret_cast<CuteQAbstractSocketCall20>(taken[20]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractSocketCall21 call = reinterpret_cast<CuteQAbstractSocketCall21>(taken[21]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractSocketCall22 call = reinterpret_cast<CuteQAbstractSocketCall22>(taken[22]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractSocketCall23 call = reinterpret_cast<CuteQAbstractSocketCall23>(taken[23]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractSocketCall24 call = reinterpret_cast<CuteQAbstractSocketCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractSocketCall25 call = reinterpret_cast<CuteQAbstractSocketCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractSocketCall26 call = reinterpret_cast<CuteQAbstractSocketCall26>(taken[26]);
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
      CuteQAbstractSocketCall27 call = reinterpret_cast<CuteQAbstractSocketCall27>(taken[27]);
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
      CuteQAbstractSocketCall28 call = reinterpret_cast<CuteQAbstractSocketCall28>(taken[28]);
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
      CuteQAbstractSocketCall29 call = reinterpret_cast<CuteQAbstractSocketCall29>(taken[29]);
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
      CuteQAbstractSocketCall30 call = reinterpret_cast<CuteQAbstractSocketCall30>(taken[30]);
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
      CuteQAbstractSocketCall31 call = reinterpret_cast<CuteQAbstractSocketCall31>(taken[31]);
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
      CuteQAbstractSocketCall32 call = reinterpret_cast<CuteQAbstractSocketCall32>(taken[32]);
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
      CuteQAbstractSocketCall33 call = reinterpret_cast<CuteQAbstractSocketCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QAbstractSocket10metaObjectEv(
    const QAbstractSocket *self) {
  return self->metaObject();
}

//  void *QAbstractSocket::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QAbstractSocket11qt_metacastEPKc(
    QAbstractSocket *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractSocket::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QAbstractSocket11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractSocket *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QAbstractSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSocket::tr(s, c, n));
}

//  QAbstractSocket::QAbstractSocket(SocketType socketType, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocket *ritual_ZN15QAbstractSocketC1ENS_10SocketTypeEP7QObject(
    QAbstractSocket::SocketType socketType,
    QObject *parent) {
  return new CuteQAbstractSocket(socketType, parent);
}

//  QAbstractSocket::~QAbstractSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocketD1Ev(QAbstractSocket *self) {
  delete self;
}

//  void QAbstractSocket::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket6resumeEv(QAbstractSocket *self) {
  self->resume();
}

//  PauseModes QAbstractSocket::pauseMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAbstractSocket9pauseModeEv(const QAbstractSocket *self) {
  return static_cast<int>(self->pauseMode().toInt());
}

//  void QAbstractSocket::setPauseMode(PauseModes pauseMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket12setPauseModeE6QFlagsINS_9PauseModeEE(
    QAbstractSocket *self,
    int pauseMode) {
  self->setPauseMode(QFlags<QAbstractSocket::PauseMode>::fromInt(pauseMode));
}

//  bool QAbstractSocket::bind(const QHostAddress &address, quint16 port,
//      BindMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindFlagEE(
    QAbstractSocket *self,
    const QHostAddress *address,
    quint16 port,
    int mode) {
  return self->bind(
      *address,
      port,
      QFlags<QAbstractSocket::BindFlag>::fromInt(mode));
}

#if !(QT_VERSION >= QT_VERSION_CHECK(7,0,0) || defined(Q_QDOC))
//  bool QAbstractSocket::bind(quint16 port, BindMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket4bindEt6QFlagsINS_8BindFlagEE(
    QAbstractSocket *self,
    quint16 port,
    int mode) {
  return self->bind(port, QFlags<QAbstractSocket::BindFlag>::fromInt(mode));
}
#endif  // !(QT_VERSION >= QT_VERSION_CHECK(7,0,0) || defined(Q_QDOC))

//  void QAbstractSocket::connectToHost(const QString &hostName, quint16
//      port, OpenMode mode, NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE(
    QAbstractSocket *self,
    const QString *hostName,
    quint16 port,
    int mode,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->connectToHost(
      *hostName,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode),
      protocol);
}

//  void QAbstractSocket::connectToHost(const QHostAddress &address, quint16
//      port, OpenMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket13connectToHostERK12QHostAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QAbstractSocket *self,
    const QHostAddress *address,
    quint16 port,
    int mode) {
  self->connectToHost(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QAbstractSocket::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket18disconnectFromHostEv(
    QAbstractSocket *self) {
  self->disconnectFromHost();
}

//  bool QAbstractSocket::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSocket7isValidEv(const QAbstractSocket *self) {
  return self->isValid();
}

//  qint64 QAbstractSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QAbstractSocket14bytesAvailableEv(
    const QAbstractSocket *self) {
  return self->bytesAvailable();
}

//  qint64 QAbstractSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QAbstractSocket12bytesToWriteEv(
    const QAbstractSocket *self) {
  return self->bytesToWrite();
}

//  quint16 QAbstractSocket::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QAbstractSocket9localPortEv(
    const QAbstractSocket *self) {
  return self->localPort();
}

//  QHostAddress QAbstractSocket::localAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK15QAbstractSocket12localAddressEv(
    const QAbstractSocket *self) {
  return new QHostAddress(self->localAddress());
}

//  quint16 QAbstractSocket::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK15QAbstractSocket8peerPortEv(const QAbstractSocket *self) {
  return self->peerPort();
}

//  QHostAddress QAbstractSocket::peerAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK15QAbstractSocket11peerAddressEv(
    const QAbstractSocket *self) {
  return new QHostAddress(self->peerAddress());
}

//  QString QAbstractSocket::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractSocket8peerNameEv(
    const QAbstractSocket *self) {
  return new QString(self->peerName());
}

//  qint64 QAbstractSocket::readBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QAbstractSocket14readBufferSizeEv(
    const QAbstractSocket *self) {
  return self->readBufferSize();
}

//  void QAbstractSocket::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket17setReadBufferSizeEx(
    QAbstractSocket *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  void QAbstractSocket::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket5abortEv(QAbstractSocket *self) {
  self->abort();
}

//  qintptr QAbstractSocket::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK15QAbstractSocket16socketDescriptorEv(
    const QAbstractSocket *self) {
  return self->socketDescriptor();
}

//  bool QAbstractSocket::setSocketDescriptor(qintptr socketDescriptor,
//      SocketState state, OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QAbstractSocket *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState state,
    int openMode) {
  return self->setSocketDescriptor(
      socketDescriptor,
      state,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QAbstractSocket::setSocketOption(QAbstractSocket::SocketOption
//      option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8QVariant(
    QAbstractSocket *self,
    QAbstractSocket::SocketOption option,
    const QVariant *value) {
  self->setSocketOption(option, *value);
}

//  QVariant QAbstractSocket::socketOption(QAbstractSocket::SocketOption
//      option)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE(
    QAbstractSocket *self,
    QAbstractSocket::SocketOption option) {
  return new QVariant(self->socketOption(option));
}

//  SocketType QAbstractSocket::socketType() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketType ritual_ZNK15QAbstractSocket10socketTypeEv(
    const QAbstractSocket *self) {
  return self->socketType();
}

//  SocketState QAbstractSocket::state() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketState ritual_ZNK15QAbstractSocket5stateEv(
    const QAbstractSocket *self) {
  return self->state();
}

//  SocketError QAbstractSocket::error() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK15QAbstractSocket5errorEv(
    const QAbstractSocket *self) {
  return self->error();
}

//  void QAbstractSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket5closeEv(QAbstractSocket *self) {
  self->close();
}

//  bool QAbstractSocket::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QAbstractSocket12isSequentialEv(
    const QAbstractSocket *self) {
  return self->isSequential();
}

//  bool QAbstractSocket::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket5flushEv(QAbstractSocket *self) {
  return self->flush();
}

//  bool QAbstractSocket::waitForConnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket16waitForConnectedEi(
    QAbstractSocket *self,
    int msecs) {
  return self->waitForConnected(msecs);
}

//  bool QAbstractSocket::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket16waitForReadyReadEi(
    QAbstractSocket *self,
    int msecs) {
  return self->waitForReadyRead(msecs);
}

//  bool QAbstractSocket::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket19waitForBytesWrittenEi(
    QAbstractSocket *self,
    int msecs) {
  return self->waitForBytesWritten(msecs);
}

//  bool QAbstractSocket::waitForDisconnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QAbstractSocket19waitForDisconnectedEi(
    QAbstractSocket *self,
    int msecs) {
  return self->waitForDisconnected(msecs);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocket::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket8setProxyERK13QNetworkProxy(
    QAbstractSocket *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QAbstractSocket::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK15QAbstractSocket5proxyEv(
    const QAbstractSocket *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QString QAbstractSocket::protocolTag() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAbstractSocket11protocolTagEv(
    const QAbstractSocket *self) {
  return new QString(self->protocolTag());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocket::setProtocolTag(const QString &tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket14setProtocolTagERK7QString(
    QAbstractSocket *self,
    const QString *tag) {
  self->setProtocolTag(*tag);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QAbstractSocket::hostFound()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket9hostFoundEv(QAbstractSocket *self) {
  self->hostFound();
}

//  void QAbstractSocket::connected()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket9connectedEv(QAbstractSocket *self) {
  self->connected();
}

//  void QAbstractSocket::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket12disconnectedEv(QAbstractSocket *self) {
  self->disconnected();
}

//  void QAbstractSocket::stateChanged(QAbstractSocket::SocketState a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket12stateChangedENS_11SocketStateE(
    QAbstractSocket *self,
    QAbstractSocket::SocketState a0) {
  self->stateChanged(a0);
}

//  void QAbstractSocket::errorOccurred(QAbstractSocket::SocketError a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket13errorOccurredENS_11SocketErrorE(
    QAbstractSocket *self,
    QAbstractSocket::SocketError a0) {
  self->errorOccurred(a0);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocket::proxyAuthenticationRequired(const QNetworkProxy
//      &proxy, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QAbstractSocket *self,
    const QNetworkProxy *proxy,
    QAuthenticator *authenticator) {
  self->proxyAuthenticationRequired(*proxy, authenticator);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  qint64 QAbstractSocket::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN15QAbstractSocket8readDataEPcx(
    QAbstractSocket *self,
    char *data,
    qint64 maxlen) {
  return self->readData(data, maxlen);
}

//  qint64 QAbstractSocket::readLineData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN15QAbstractSocket12readLineDataEPcx(
    QAbstractSocket *self,
    char *data,
    qint64 maxlen) {
  return self->readLineData(data, maxlen);
}

//  qint64 QAbstractSocket::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN15QAbstractSocket8skipDataEx(
    QAbstractSocket *self,
    qint64 maxSize) {
  return self->skipData(maxSize);
}

//  qint64 QAbstractSocket::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN15QAbstractSocket9writeDataEPKcx(
    QAbstractSocket *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  void QAbstractSocket::setSocketState(SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket14setSocketStateENS_11SocketStateE(
    QAbstractSocket *self,
    QAbstractSocket::SocketState state) {
  self->setSocketState(state);
}

//  void QAbstractSocket::setSocketError(SocketError socketError)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket14setSocketErrorENS_11SocketErrorE(
    QAbstractSocket *self,
    QAbstractSocket::SocketError socketError) {
  self->setSocketError(socketError);
}

//  void QAbstractSocket::setLocalPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket12setLocalPortEt(
    QAbstractSocket *self,
    quint16 port) {
  self->setLocalPort(port);
}

//  void QAbstractSocket::setLocalAddress(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket15setLocalAddressERK12QHostAddress(
    QAbstractSocket *self,
    const QHostAddress *address) {
  self->setLocalAddress(*address);
}

//  void QAbstractSocket::setPeerPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket11setPeerPortEt(
    QAbstractSocket *self,
    quint16 port) {
  self->setPeerPort(port);
}

//  void QAbstractSocket::setPeerAddress(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket14setPeerAddressERK12QHostAddress(
    QAbstractSocket *self,
    const QHostAddress *address) {
  self->setPeerAddress(*address);
}

//  void QAbstractSocket::setPeerName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QAbstractSocket11setPeerNameERK7QString(
    QAbstractSocket *self,
    const QString *name) {
  self->setPeerName(*name);
}

//  QAbstractSocket::QAbstractSocket(SocketType socketType,
//      QAbstractSocketPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractSocket *ritual_ZN15QAbstractSocketC1ENS_10SocketTypeER22QAbstractSocketPrivateP7QObject(
    QAbstractSocket::SocketType socketType,
    QAbstractSocketPrivate *dd,
    QObject *parent) {
  return new CuteQAbstractSocket(socketType, *dd, parent);
}

//  QAbstractSocketPrivate *QAbstractSocket::d_func()
extern "C" Q_DECL_EXPORT
QAbstractSocketPrivate *ritual_ZN15QAbstractSocket6d_funcEv(
    QAbstractSocket *self) {
  return self->d_func();
}

//  const QAbstractSocketPrivate *QAbstractSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSocketPrivate *ritual_ZNK15QAbstractSocket6d_funcEv(
    const QAbstractSocket *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractSocket, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSocket(
    QAbstractSocket *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSocket *>(self)->take(key, call);
}

//  void QAbstractSocket::resume()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSocket6resumeEv(QAbstractSocket *self) {
  self->QAbstractSocket::resume();
}

//  bool QAbstractSocket::bind(const QHostAddress &address, quint16 port,
//      BindMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindFlagEE(
    QAbstractSocket *self,
    const QHostAddress *address,
    quint16 port,
    int mode) {
  return self->QAbstractSocket::bind(
      *address,
      port,
      QFlags<QAbstractSocket::BindFlag>::fromInt(mode));
}

//  void QAbstractSocket::connectToHost(const QString &hostName, quint16
//      port, OpenMode mode, NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE(
    QAbstractSocket *self,
    const QString *hostName,
    quint16 port,
    int mode,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->QAbstractSocket::connectToHost(
      *hostName,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode),
      protocol);
}

//  void QAbstractSocket::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSocket18disconnectFromHostEv(
    QAbstractSocket *self) {
  self->QAbstractSocket::disconnectFromHost();
}

//  qint64 QAbstractSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK15QAbstractSocket14bytesAvailableEv(
    const QAbstractSocket *self) {
  return self->QAbstractSocket::bytesAvailable();
}

//  qint64 QAbstractSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK15QAbstractSocket12bytesToWriteEv(
    const QAbstractSocket *self) {
  return self->QAbstractSocket::bytesToWrite();
}

//  void QAbstractSocket::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSocket17setReadBufferSizeEx(
    QAbstractSocket *self,
    qint64 size) {
  self->QAbstractSocket::setReadBufferSize(size);
}

//  qintptr QAbstractSocket::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK15QAbstractSocket16socketDescriptorEv(
    const QAbstractSocket *self) {
  return self->QAbstractSocket::socketDescriptor();
}

//  bool QAbstractSocket::setSocketDescriptor(qintptr socketDescriptor,
//      SocketState state, OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QAbstractSocket *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState state,
    int openMode) {
  return self->QAbstractSocket::setSocketDescriptor(
      socketDescriptor,
      state,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QAbstractSocket::setSocketOption(QAbstractSocket::SocketOption
//      option, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8QVariant(
    QAbstractSocket *self,
    QAbstractSocket::SocketOption option,
    const QVariant *value) {
  self->QAbstractSocket::setSocketOption(option, *value);
}

//  QVariant QAbstractSocket::socketOption(QAbstractSocket::SocketOption
//      option)
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE(
    QAbstractSocket *self,
    QAbstractSocket::SocketOption option) {
  return new QVariant(self->QAbstractSocket::socketOption(option));
}

//  void QAbstractSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QAbstractSocket5closeEv(QAbstractSocket *self) {
  self->QAbstractSocket::close();
}

//  bool QAbstractSocket::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15QAbstractSocket12isSequentialEv(
    const QAbstractSocket *self) {
  return self->QAbstractSocket::isSequential();
}

//  bool QAbstractSocket::waitForConnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSocket16waitForConnectedEi(
    QAbstractSocket *self,
    int msecs) {
  return self->QAbstractSocket::waitForConnected(msecs);
}

//  bool QAbstractSocket::waitForReadyRead(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSocket16waitForReadyReadEi(
    QAbstractSocket *self,
    int msecs) {
  return self->QAbstractSocket::waitForReadyRead(msecs);
}

//  bool QAbstractSocket::waitForBytesWritten(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSocket19waitForBytesWrittenEi(
    QAbstractSocket *self,
    int msecs) {
  return self->QAbstractSocket::waitForBytesWritten(msecs);
}

//  bool QAbstractSocket::waitForDisconnected(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QAbstractSocket19waitForDisconnectedEi(
    QAbstractSocket *self,
    int msecs) {
  return self->QAbstractSocket::waitForDisconnected(msecs);
}

//  qint64 QAbstractSocket::readData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN15QAbstractSocket8readDataEPcx(
    QAbstractSocket *self,
    char *data,
    qint64 maxlen) {
  return static_cast<OwnQAbstractSocket *>(self)->OwnQAbstractSocket::readData(
      data,
      maxlen);
}

//  qint64 QAbstractSocket::readLineData(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN15QAbstractSocket12readLineDataEPcx(
    QAbstractSocket *self,
    char *data,
    qint64 maxlen) {
  return static_cast<OwnQAbstractSocket *>(self)->OwnQAbstractSocket::readLineData(
      data,
      maxlen);
}

//  qint64 QAbstractSocket::skipData(qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN15QAbstractSocket8skipDataEx(
    QAbstractSocket *self,
    qint64 maxSize) {
  return static_cast<OwnQAbstractSocket *>(self)->OwnQAbstractSocket::skipData(
      maxSize);
}
