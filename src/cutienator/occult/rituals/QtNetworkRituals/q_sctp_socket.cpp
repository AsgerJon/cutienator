//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsctpsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(sctp)
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
#include <QtNetwork/qsctpsocket.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkdatagram.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSctpSocket that Python can take functions over in. Every QSctpSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
typedef void (*CuteQSctpSocketCall0)(const void *, int *);
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
typedef void (*CuteQSctpSocketCall1)(const void *, int *);
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
typedef void (*CuteQSctpSocketCall2)(const void *, int *);
typedef bool (*CuteQSctpSocketCall3)(const void *, const QHostAddress *, quint16, int, int *);
typedef void (*CuteQSctpSocketCall4)(const void *, const QString *, quint16, int, int, int *);
typedef qint64 (*CuteQSctpSocketCall5)(const void *, int *);
typedef qint64 (*CuteQSctpSocketCall6)(const void *, int *);
typedef void (*CuteQSctpSocketCall7)(const void *, qint64, int *);
typedef qintptr (*CuteQSctpSocketCall8)(const void *, int *);
typedef bool (*CuteQSctpSocketCall9)(const void *, qintptr, int, int, int *);
typedef void (*CuteQSctpSocketCall10)(const void *, int, const QVariant *, int *);
typedef const QVariant * (*CuteQSctpSocketCall11)(const void *, int, int *);
typedef bool (*CuteQSctpSocketCall12)(const void *, int *);
typedef bool (*CuteQSctpSocketCall13)(const void *, int, int *);
typedef bool (*CuteQSctpSocketCall14)(const void *, int, int *);
typedef bool (*CuteQSctpSocketCall15)(const void *, int, int *);
typedef bool (*CuteQSctpSocketCall16)(const void *, int, int *);
typedef qint64 (*CuteQSctpSocketCall17)(const void *, qint64, int *);
typedef bool (*CuteQSctpSocketCall18)(const void *, int, int *);
typedef qint64 (*CuteQSctpSocketCall19)(const void *, int *);
typedef qint64 (*CuteQSctpSocketCall20)(const void *, int *);
typedef bool (*CuteQSctpSocketCall21)(const void *, qint64, int *);
typedef bool (*CuteQSctpSocketCall22)(const void *, int *);
typedef bool (*CuteQSctpSocketCall23)(const void *, int *);
typedef bool (*CuteQSctpSocketCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSctpSocketCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSctpSocketCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpSocketCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpSocketCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpSocketCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpSocketCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSctpSocketCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSctpSocket : public QSctpSocket {
public:
  using QSctpSocket::QSctpSocket;
  void *taken[32] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN15QAbstractSocket18disconnectFromHostEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN15QAbstractSocket6resumeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket4bindERK12QHostAddresst6QFlagsINS_8BindFlagEE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket13connectToHostERK7QStringt6QFlagsIN13QIODeviceBase12OpenModeFlagEENS_20NetworkLayerProtocolE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket17setReadBufferSizeEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QAbstractSocket16socketDescriptorEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket19setSocketDescriptorExNS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket15setSocketOptionENS_12SocketOptionERK8QVariant")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QAbstractSocket12socketOptionENS_12SocketOptionE")) {
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

#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
  //  void QSctpSocket::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSctpSocketCall0 call = reinterpret_cast<CuteQSctpSocketCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QSctpSocket::close();
  }
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)

#if !defined(QT_NO_SCTP) || defined(Q_QDOC)
  //  void QSctpSocket::disconnectFromHost()
  void disconnectFromHost() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSctpSocketCall1 call = reinterpret_cast<CuteQSctpSocketCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSctpSocket::disconnectFromHost();
  }
#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)

  //  void QAbstractSocket::resume()
  void resume() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSctpSocketCall2 call = reinterpret_cast<CuteQSctpSocketCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQSctpSocketCall3 call = reinterpret_cast<CuteQSctpSocketCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQSctpSocketCall4 call = reinterpret_cast<CuteQSctpSocketCall4>(taken[4]);
      call(this, &hostName, port, static_cast<int>(mode.toInt()), static_cast<int>(protocol), &handled);
      if (handled) return;
    }
    QAbstractSocket::connectToHost(hostName, port, mode, protocol);
  }

  //  qint64 QAbstractSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQSctpSocketCall5 call = reinterpret_cast<CuteQSctpSocketCall5>(taken[5]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesAvailable();
  }

  //  qint64 QAbstractSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSctpSocketCall6 call = reinterpret_cast<CuteQSctpSocketCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::bytesToWrite();
  }

  //  void QAbstractSocket::setReadBufferSize(qint64 size)
  void setReadBufferSize(qint64 size) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSctpSocketCall7 call = reinterpret_cast<CuteQSctpSocketCall7>(taken[7]);
      call(this, size, &handled);
      if (handled) return;
    }
    QAbstractSocket::setReadBufferSize(size);
  }

  //  qintptr QAbstractSocket::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSctpSocketCall8 call = reinterpret_cast<CuteQSctpSocketCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQSctpSocketCall9 call = reinterpret_cast<CuteQSctpSocketCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQSctpSocketCall10 call = reinterpret_cast<CuteQSctpSocketCall10>(taken[10]);
      call(this, static_cast<int>(option), &value, &handled);
      if (handled) return;
    }
    QAbstractSocket::setSocketOption(option, value);
  }

  //  QVariant QAbstractSocket::socketOption(QAbstractSocket::SocketOption
  //      option)
  QVariant socketOption(QAbstractSocket::SocketOption option) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSctpSocketCall11 call = reinterpret_cast<CuteQSctpSocketCall11>(taken[11]);
      const QVariant * given = call(this, static_cast<int>(option), &handled);
      if (handled && given) return *given;
    }
    return QAbstractSocket::socketOption(option);
  }

  //  bool QAbstractSocket::isSequential() const
  bool isSequential() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSctpSocketCall12 call = reinterpret_cast<CuteQSctpSocketCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::isSequential();
  }

  //  bool QAbstractSocket::waitForConnected(int msecs)
  bool waitForConnected(int msecs) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSctpSocketCall13 call = reinterpret_cast<CuteQSctpSocketCall13>(taken[13]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForConnected(msecs);
  }

  //  bool QAbstractSocket::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSctpSocketCall14 call = reinterpret_cast<CuteQSctpSocketCall14>(taken[14]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForReadyRead(msecs);
  }

  //  bool QAbstractSocket::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSctpSocketCall15 call = reinterpret_cast<CuteQSctpSocketCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForBytesWritten(msecs);
  }

  //  bool QAbstractSocket::waitForDisconnected(int msecs)
  bool waitForDisconnected(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSctpSocketCall16 call = reinterpret_cast<CuteQSctpSocketCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::waitForDisconnected(msecs);
  }

  //  qint64 QAbstractSocket::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSctpSocketCall17 call = reinterpret_cast<CuteQSctpSocketCall17>(taken[17]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QAbstractSocket::skipData(maxSize);
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSctpSocketCall18 call = reinterpret_cast<CuteQSctpSocketCall18>(taken[18]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSctpSocketCall19 call = reinterpret_cast<CuteQSctpSocketCall19>(taken[19]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSctpSocketCall20 call = reinterpret_cast<CuteQSctpSocketCall20>(taken[20]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSctpSocketCall21 call = reinterpret_cast<CuteQSctpSocketCall21>(taken[21]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSctpSocketCall22 call = reinterpret_cast<CuteQSctpSocketCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[23]) {
      int handled = 0;
      CuteQSctpSocketCall23 call = reinterpret_cast<CuteQSctpSocketCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSctpSocketCall24 call = reinterpret_cast<CuteQSctpSocketCall24>(taken[24]);
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
      CuteQSctpSocketCall25 call = reinterpret_cast<CuteQSctpSocketCall25>(taken[25]);
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
      CuteQSctpSocketCall26 call = reinterpret_cast<CuteQSctpSocketCall26>(taken[26]);
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
      CuteQSctpSocketCall27 call = reinterpret_cast<CuteQSctpSocketCall27>(taken[27]);
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
      CuteQSctpSocketCall28 call = reinterpret_cast<CuteQSctpSocketCall28>(taken[28]);
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
      CuteQSctpSocketCall29 call = reinterpret_cast<CuteQSctpSocketCall29>(taken[29]);
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
      CuteQSctpSocketCall30 call = reinterpret_cast<CuteQSctpSocketCall30>(taken[30]);
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
      CuteQSctpSocketCall31 call = reinterpret_cast<CuteQSctpSocketCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSctpSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QSctpSocket10metaObjectEv(
    const QSctpSocket *self) {
  return self->metaObject();
}

//  QString QSctpSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QSctpSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSctpSocket::tr(s, c, n));
}

//  QSctpSocket::QSctpSocket(QObject *parent)
extern "C" Q_DECL_EXPORT
QSctpSocket *ritual_ZN11QSctpSocketC1EP7QObject(QObject *parent) {
  return new CuteQSctpSocket(parent);
}

//  QSctpSocket::~QSctpSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpSocketD1Ev(QSctpSocket *self) {
  delete self;
}

//  void QSctpSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpSocket5closeEv(QSctpSocket *self) {
  self->close();
}

//  void QSctpSocket::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpSocket18disconnectFromHostEv(QSctpSocket *self) {
  self->disconnectFromHost();
}

//  void QSctpSocket::setMaximumChannelCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSctpSocket22setMaximumChannelCountEi(
    QSctpSocket *self,
    int count) {
  self->setMaximumChannelCount(count);
}

//  int QSctpSocket::maximumChannelCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QSctpSocket19maximumChannelCountEv(const QSctpSocket *self) {
  return self->maximumChannelCount();
}

//  bool QSctpSocket::isInDatagramMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QSctpSocket16isInDatagramModeEv(const QSctpSocket *self) {
  return self->isInDatagramMode();
}

//  QNetworkDatagram QSctpSocket::readDatagram()
extern "C" Q_DECL_EXPORT
QNetworkDatagram *ritual_ZN11QSctpSocket12readDatagramEv(QSctpSocket *self) {
  return new QNetworkDatagram(self->readDatagram());
}

//  bool QSctpSocket::writeDatagram(const QNetworkDatagram &datagram)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QSctpSocket13writeDatagramERK16QNetworkDatagram(
    QSctpSocket *self,
    const QNetworkDatagram *datagram) {
  return self->writeDatagram(*datagram);
}

//  QSctpSocketPrivate *QSctpSocket::d_func()
extern "C" Q_DECL_EXPORT
QSctpSocketPrivate *ritual_ZN11QSctpSocket6d_funcEv(QSctpSocket *self) {
  return self->d_func();
}

//  const QSctpSocketPrivate *QSctpSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QSctpSocketPrivate *ritual_ZNK11QSctpSocket6d_funcEv(
    const QSctpSocket *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSctpSocket, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSctpSocket(
    QSctpSocket *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSctpSocket *>(self)->take(key, call);
}

//  void QSctpSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSctpSocket5closeEv(QSctpSocket *self) {
  self->QSctpSocket::close();
}

//  void QSctpSocket::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QSctpSocket18disconnectFromHostEv(QSctpSocket *self) {
  self->QSctpSocket::disconnectFromHost();
}

#endif  // !defined(QT_NO_SCTP) || defined(Q_QDOC)
#endif  // QT_CONFIG(sctp)
