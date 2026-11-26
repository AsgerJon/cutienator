//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNativeSocketEngine that Python can take functions over in. Every QNativeSocketEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNativeSocketEngineCall0)(const void *, int, int, int *);
typedef bool (*CuteQNativeSocketEngineCall1)(const void *, qintptr, int, int *);
typedef qintptr (*CuteQNativeSocketEngineCall2)(const void *, int *);
typedef bool (*CuteQNativeSocketEngineCall3)(const void *, int *);
typedef bool (*CuteQNativeSocketEngineCall4)(const void *, const QHostAddress *, quint16, int *);
typedef bool (*CuteQNativeSocketEngineCall5)(const void *, const QString *, quint16, int *);
typedef bool (*CuteQNativeSocketEngineCall6)(const void *, const QHostAddress *, quint16, int *);
typedef bool (*CuteQNativeSocketEngineCall7)(const void *, int, int *);
typedef qintptr (*CuteQNativeSocketEngineCall8)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall9)(const void *, int *);
typedef qint64 (*CuteQNativeSocketEngineCall10)(const void *, int *);
typedef qint64 (*CuteQNativeSocketEngineCall11)(const void *, char *, qint64, int *);
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef bool (*CuteQNativeSocketEngineCall12)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef bool (*CuteQNativeSocketEngineCall13)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef const QNetworkInterface * (*CuteQNativeSocketEngineCall14)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef bool (*CuteQNativeSocketEngineCall15)(const void *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
typedef bool (*CuteQNativeSocketEngineCall16)(const void *, int *);
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
typedef qint64 (*CuteQNativeSocketEngineCall17)(const void *, int *);
#endif  // !defined(QT_NO_UDPSOCKET)
typedef qint64 (*CuteQNativeSocketEngineCall18)(const void *, char *, qint64, QIpPacketHeader *, int, int *);
typedef qint64 (*CuteQNativeSocketEngineCall19)(const void *, int *);
typedef int (*CuteQNativeSocketEngineCall20)(const void *, int, int *);
typedef bool (*CuteQNativeSocketEngineCall21)(const void *, int, int, int *);
typedef bool (*CuteQNativeSocketEngineCall22)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall23)(const void *, bool, int *);
typedef bool (*CuteQNativeSocketEngineCall24)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall25)(const void *, bool, int *);
typedef bool (*CuteQNativeSocketEngineCall26)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall27)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNativeSocketEngineCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNativeSocketEngineCall29)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall30)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall31)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall32)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall34)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNativeSocketEngine : public QNativeSocketEngine {
public:
  using QNativeSocketEngine::QNativeSocketEngine;
  void *taken[35] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11SocketStateE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine16socketDescriptorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine7isValidEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine4bindERK12QHostAddresst")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6listenEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6acceptEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine5closeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine14bytesAvailableEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine4readEPcx")) {
      taken[11] = call;
      return true;
    }
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine18multicastInterfaceEv")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkInterface")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_UDPSOCKET)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine12readDatagramEPcxP15QIpPacketHeader6QFlagsINS_18PacketHeaderOptionEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine12bytesToWriteEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb")) {
      taken[27] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QNativeSocketEngine::initialize(QAbstractSocket::SocketType
  //      type, QAbstractSocket::NetworkLayerProtocol protocol)
  bool initialize(
      QAbstractSocket::SocketType type,
      QAbstractSocket::NetworkLayerProtocol protocol) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeSocketEngineCall0 call = reinterpret_cast<CuteQNativeSocketEngineCall0>(taken[0]);
      bool given = call(this, static_cast<int>(type), static_cast<int>(protocol), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::initialize(type, protocol);
  }

  //  bool QNativeSocketEngine::initialize(qintptr socketDescriptor,
  //      QAbstractSocket::SocketState socketState)
  bool initialize(
      qintptr socketDescriptor,
      QAbstractSocket::SocketState socketState) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeSocketEngineCall1 call = reinterpret_cast<CuteQNativeSocketEngineCall1>(taken[1]);
      bool given = call(this, socketDescriptor, static_cast<int>(socketState), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::initialize(socketDescriptor, socketState);
  }

  //  qintptr QNativeSocketEngine::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeSocketEngineCall2 call = reinterpret_cast<CuteQNativeSocketEngineCall2>(taken[2]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::socketDescriptor();
  }

  //  bool QNativeSocketEngine::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeSocketEngineCall3 call = reinterpret_cast<CuteQNativeSocketEngineCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isValid();
  }

  //  bool QNativeSocketEngine::connectToHost(const QHostAddress &address,
  //      quint16 port)
  bool connectToHost(const QHostAddress &address, quint16 port) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNativeSocketEngineCall4 call = reinterpret_cast<CuteQNativeSocketEngineCall4>(taken[4]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::connectToHost(address, port);
  }

  //  bool QNativeSocketEngine::connectToHostByName(const QString &name,
  //      quint16 port)
  bool connectToHostByName(const QString &name, quint16 port) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNativeSocketEngineCall5 call = reinterpret_cast<CuteQNativeSocketEngineCall5>(taken[5]);
      bool given = call(this, &name, port, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::connectToHostByName(name, port);
  }

  //  bool QNativeSocketEngine::bind(const QHostAddress &address, quint16
  //      port)
  bool bind(const QHostAddress &address, quint16 port) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNativeSocketEngineCall6 call = reinterpret_cast<CuteQNativeSocketEngineCall6>(taken[6]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::bind(address, port);
  }

  //  bool QNativeSocketEngine::listen(int backlog)
  bool listen(int backlog) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNativeSocketEngineCall7 call = reinterpret_cast<CuteQNativeSocketEngineCall7>(taken[7]);
      bool given = call(this, backlog, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::listen(backlog);
  }

  //  qintptr QNativeSocketEngine::accept()
  qintptr accept() override {
    if (taken[8]) {
      int handled = 0;
      CuteQNativeSocketEngineCall8 call = reinterpret_cast<CuteQNativeSocketEngineCall8>(taken[8]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::accept();
  }

  //  void QNativeSocketEngine::close()
  void close() override {
    if (taken[9]) {
      int handled = 0;
      CuteQNativeSocketEngineCall9 call = reinterpret_cast<CuteQNativeSocketEngineCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::close();
  }

  //  qint64 QNativeSocketEngine::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNativeSocketEngineCall10 call = reinterpret_cast<CuteQNativeSocketEngineCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::bytesAvailable();
  }

  //  qint64 QNativeSocketEngine::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNativeSocketEngineCall11 call = reinterpret_cast<CuteQNativeSocketEngineCall11>(taken[11]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::read(data, maxlen);
  }

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  bool QNativeSocketEngine::joinMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool joinMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNativeSocketEngineCall12 call = reinterpret_cast<CuteQNativeSocketEngineCall12>(taken[12]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::joinMulticastGroup(groupAddress, iface);
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  bool QNativeSocketEngine::leaveMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool leaveMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNativeSocketEngineCall13 call = reinterpret_cast<CuteQNativeSocketEngineCall13>(taken[13]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::leaveMulticastGroup(groupAddress, iface);
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  QNetworkInterface QNativeSocketEngine::multicastInterface() const
  QNetworkInterface multicastInterface() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQNativeSocketEngineCall14 call = reinterpret_cast<CuteQNativeSocketEngineCall14>(taken[14]);
      const QNetworkInterface * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNativeSocketEngine::multicastInterface();
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  bool QNativeSocketEngine::setMulticastInterface(const
  //      QNetworkInterface &iface)
  bool setMulticastInterface(const QNetworkInterface &iface) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNativeSocketEngineCall15 call = reinterpret_cast<CuteQNativeSocketEngineCall15>(taken[15]);
      bool given = call(this, &iface, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::setMulticastInterface(iface);
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
  //  bool QNativeSocketEngine::hasPendingDatagrams() const
  bool hasPendingDatagrams() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQNativeSocketEngineCall16 call = reinterpret_cast<CuteQNativeSocketEngineCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::hasPendingDatagrams();
  }
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
  //  qint64 QNativeSocketEngine::pendingDatagramSize() const
  qint64 pendingDatagramSize() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQNativeSocketEngineCall17 call = reinterpret_cast<CuteQNativeSocketEngineCall17>(taken[17]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::pendingDatagramSize();
  }
#endif  // !defined(QT_NO_UDPSOCKET)

  //  qint64 QNativeSocketEngine::readDatagram(char *data, qint64 maxlen,
  //      QIpPacketHeader *a2, PacketHeaderOptions a3)
  qint64 readDatagram(
      char *data,
      qint64 maxlen,
      QIpPacketHeader *a2,
      QAbstractSocketEngine::PacketHeaderOptions a3) override {
    if (taken[18]) {
      int handled = 0;
      CuteQNativeSocketEngineCall18 call = reinterpret_cast<CuteQNativeSocketEngineCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, a2, static_cast<int>(a3.toInt()), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::readDatagram(data, maxlen, a2, a3);
  }

  //  qint64 QNativeSocketEngine::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQNativeSocketEngineCall19 call = reinterpret_cast<CuteQNativeSocketEngineCall19>(taken[19]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::bytesToWrite();
  }

  //  int QNativeSocketEngine::option(SocketOption option) const
  int option(QAbstractSocketEngine::SocketOption option) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQNativeSocketEngineCall20 call = reinterpret_cast<CuteQNativeSocketEngineCall20>(taken[20]);
      int given = call(this, static_cast<int>(option), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::option(option);
  }

  //  bool QNativeSocketEngine::setOption(SocketOption option, int value)
  bool setOption(
      QAbstractSocketEngine::SocketOption option,
      int value) override {
    if (taken[21]) {
      int handled = 0;
      CuteQNativeSocketEngineCall21 call = reinterpret_cast<CuteQNativeSocketEngineCall21>(taken[21]);
      bool given = call(this, static_cast<int>(option), value, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::setOption(option, value);
  }

  //  bool QNativeSocketEngine::isReadNotificationEnabled() const
  bool isReadNotificationEnabled() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQNativeSocketEngineCall22 call = reinterpret_cast<CuteQNativeSocketEngineCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isReadNotificationEnabled();
  }

  //  void QNativeSocketEngine::setReadNotificationEnabled(bool enable)
  void setReadNotificationEnabled(bool enable) override {
    if (taken[23]) {
      int handled = 0;
      CuteQNativeSocketEngineCall23 call = reinterpret_cast<CuteQNativeSocketEngineCall23>(taken[23]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::setReadNotificationEnabled(enable);
  }

  //  bool QNativeSocketEngine::isWriteNotificationEnabled() const
  bool isWriteNotificationEnabled() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQNativeSocketEngineCall24 call = reinterpret_cast<CuteQNativeSocketEngineCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isWriteNotificationEnabled();
  }

  //  void QNativeSocketEngine::setWriteNotificationEnabled(bool enable)
  void setWriteNotificationEnabled(bool enable) override {
    if (taken[25]) {
      int handled = 0;
      CuteQNativeSocketEngineCall25 call = reinterpret_cast<CuteQNativeSocketEngineCall25>(taken[25]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::setWriteNotificationEnabled(enable);
  }

  //  bool QNativeSocketEngine::isExceptionNotificationEnabled() const
  bool isExceptionNotificationEnabled() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQNativeSocketEngineCall26 call = reinterpret_cast<CuteQNativeSocketEngineCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isExceptionNotificationEnabled();
  }

  //  void QNativeSocketEngine::setExceptionNotificationEnabled(bool
  //      enable)
  void setExceptionNotificationEnabled(bool enable) override {
    if (taken[27]) {
      int handled = 0;
      CuteQNativeSocketEngineCall27 call = reinterpret_cast<CuteQNativeSocketEngineCall27>(taken[27]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::setExceptionNotificationEnabled(enable);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQNativeSocketEngineCall28 call = reinterpret_cast<CuteQNativeSocketEngineCall28>(taken[28]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQNativeSocketEngineCall29 call = reinterpret_cast<CuteQNativeSocketEngineCall29>(taken[29]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQNativeSocketEngineCall30 call = reinterpret_cast<CuteQNativeSocketEngineCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQNativeSocketEngineCall31 call = reinterpret_cast<CuteQNativeSocketEngineCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQNativeSocketEngineCall32 call = reinterpret_cast<CuteQNativeSocketEngineCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQNativeSocketEngineCall33 call = reinterpret_cast<CuteQNativeSocketEngineCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[34]) {
      int handled = 0;
      CuteQNativeSocketEngineCall34 call = reinterpret_cast<CuteQNativeSocketEngineCall34>(taken[34]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};
