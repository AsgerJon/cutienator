//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocketbase_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/qbluetoothsocket.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocketbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBluetoothSocketBasePrivate that Python can take functions over in. Every QBluetoothSocketBasePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQBluetoothSocketBasePrivateCall0)(const void *, int, int *);
typedef QString * (*CuteQBluetoothSocketBasePrivateCall1)(const void *, int *);
typedef const QBluetoothAddress * (*CuteQBluetoothSocketBasePrivateCall2)(const void *, int *);
typedef quint16 (*CuteQBluetoothSocketBasePrivateCall3)(const void *, int *);
typedef QString * (*CuteQBluetoothSocketBasePrivateCall4)(const void *, int *);
typedef const QBluetoothAddress * (*CuteQBluetoothSocketBasePrivateCall5)(const void *, int *);
typedef quint16 (*CuteQBluetoothSocketBasePrivateCall6)(const void *, int *);
typedef void (*CuteQBluetoothSocketBasePrivateCall7)(const void *, int *);
typedef void (*CuteQBluetoothSocketBasePrivateCall8)(const void *, int *);
typedef qint64 (*CuteQBluetoothSocketBasePrivateCall9)(const void *, int *);
typedef bool (*CuteQBluetoothSocketBasePrivateCall10)(const void *, int *);
typedef qint64 (*CuteQBluetoothSocketBasePrivateCall11)(const void *, int *);
typedef bool (*CuteQBluetoothSocketBasePrivateCall12)(const void *, int, int, int, int, int *);
#if !(defined(QT_ANDROID_BLUETOOTH))
typedef void (*CuteQBluetoothSocketBasePrivateCall13)(const void *, const QBluetoothAddress *, quint16, int, int *);
#endif  // !(defined(QT_ANDROID_BLUETOOTH))
typedef void (*CuteQBluetoothSocketBasePrivateCall14)(const void *, const QBluetoothServiceInfo *, int, int *);
typedef void (*CuteQBluetoothSocketBasePrivateCall15)(const void *, const QBluetoothAddress *, const QBluetoothUuid *, int, int *);
typedef void (*CuteQBluetoothSocketBasePrivateCall16)(const void *, const QBluetoothAddress *, quint16, int, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothSocketBasePrivateCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothSocketBasePrivateCall18)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketBasePrivateCall19)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketBasePrivateCall20)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketBasePrivateCall21)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketBasePrivateCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketBasePrivateCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothSocketBasePrivate : public QBluetoothSocketBasePrivate {
public:
  using QBluetoothSocketBasePrivate::QBluetoothSocketBasePrivate;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate9localNameEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate12localAddressEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate9localPortEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate8peerNameEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate11peerAddressEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate8peerPortEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate5abortEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate5closeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate14bytesAvailableEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate11canReadLineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK27QBluetoothSocketBasePrivate12bytesToWriteEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[12] = call;
      return true;
    }
#if !(defined(QT_ANDROID_BLUETOOTH))
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[13] = call;
      return true;
    }
#endif  // !(defined(QT_ANDROID_BLUETOOTH))
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate16connectToServiceERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBluetoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QBluetoothSocketBasePrivate::ensureNativeSocket(QBluetoothServic
  //      eInfo::Protocol type)
  bool ensureNativeSocket(QBluetoothServiceInfo::Protocol type) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall0 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall0>(taken[0]);
      bool given = call(this, static_cast<int>(type), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QBluetoothSocketBasePrivate::localName() const
  QString localName() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall1 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QBluetoothAddress QBluetoothSocketBasePrivate::localAddress() const
  QBluetoothAddress localAddress() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall2 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall2>(taken[2]);
      const QBluetoothAddress * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  quint16 QBluetoothSocketBasePrivate::localPort() const
  quint16 localPort() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall3 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall3>(taken[3]);
      quint16 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QString QBluetoothSocketBasePrivate::peerName() const
  QString peerName() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall4 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall4>(taken[4]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QBluetoothAddress QBluetoothSocketBasePrivate::peerAddress() const
  QBluetoothAddress peerAddress() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall5 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall5>(taken[5]);
      const QBluetoothAddress * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  quint16 QBluetoothSocketBasePrivate::peerPort() const
  quint16 peerPort() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall6 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall6>(taken[6]);
      quint16 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QBluetoothSocketBasePrivate::abort()
  void abort() override {
    if (taken[7]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall7 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QBluetoothSocketBasePrivate::close()
  void close() override {
    if (taken[8]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall8 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qint64 QBluetoothSocketBasePrivate::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall9 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QBluetoothSocketBasePrivate::canReadLine() const
  bool canReadLine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall10 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QBluetoothSocketBasePrivate::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall11 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall11>(taken[11]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QBluetoothSocketBasePrivate::setSocketDescriptor(int
  //      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
  //      QBluetoothSocket::SocketState socketState,
  //      QBluetoothSocket::OpenMode openMode)
  bool setSocketDescriptor(
      int socketDescriptor,
      QBluetoothServiceInfo::Protocol socketType,
      QBluetoothSocket::SocketState socketState,
      QBluetoothSocket::OpenMode openMode) override {
    if (taken[12]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall12 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall12>(taken[12]);
      bool given = call(this, socketDescriptor, static_cast<int>(socketType), static_cast<int>(socketState), static_cast<int>(openMode.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

#if !(defined(QT_ANDROID_BLUETOOTH))
  //  void QBluetoothSocketBasePrivate::connectToServiceHelper(const
  //      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
  //      openMode)
  void connectToServiceHelper(
      const QBluetoothAddress &address,
      quint16 port,
      QIODevice::OpenMode openMode) override {
    if (taken[13]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall13 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall13>(taken[13]);
      call(this, &address, port, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return;
    }
  }
#endif  // !(defined(QT_ANDROID_BLUETOOTH))

  //  void QBluetoothSocketBasePrivate::connectToService(const
  //      QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
  void connectToService(
      const QBluetoothServiceInfo &service,
      QIODevice::OpenMode openMode) override {
    if (taken[14]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall14 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall14>(taken[14]);
      call(this, &service, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QBluetoothSocketBasePrivate::connectToService(const
  //      QBluetoothAddress &address, const QBluetoothUuid &uuid,
  //      QIODevice::OpenMode openMode)
  void connectToService(
      const QBluetoothAddress &address,
      const QBluetoothUuid &uuid,
      QIODevice::OpenMode openMode) override {
    if (taken[15]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall15 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall15>(taken[15]);
      call(this, &address, &uuid, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QBluetoothSocketBasePrivate::connectToService(const
  //      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
  //      openMode)
  void connectToService(
      const QBluetoothAddress &address,
      quint16 port,
      QIODevice::OpenMode openMode) override {
    if (taken[16]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall16 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall16>(taken[16]);
      call(this, &address, port, static_cast<int>(openMode.toInt()), &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall17 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall17>(taken[17]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall18 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall18>(taken[18]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall19 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall20 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall21 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall22 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQBluetoothSocketBasePrivateCall23 call = reinterpret_cast<CuteQBluetoothSocketBasePrivateCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothSocketBasePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QBluetoothSocketBasePrivate10metaObjectEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->metaObject();
}

//  QBluetoothSocketBasePrivate::~QBluetoothSocketBasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivateD1Ev(
    QBluetoothSocketBasePrivate *self) {
  delete self;
}

//  bool QBluetoothSocketBasePrivate::ensureNativeSocket(QBluetoothServiceInf
//      o::Protocol type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QBluetoothSocketBasePrivate18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE(
    QBluetoothSocketBasePrivate *self,
    QBluetoothServiceInfo::Protocol type) {
  return self->ensureNativeSocket(type);
}

//  QString QBluetoothSocketBasePrivate::localName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QBluetoothSocketBasePrivate9localNameEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QString(self->localName());
}

//  QBluetoothAddress QBluetoothSocketBasePrivate::localAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK27QBluetoothSocketBasePrivate12localAddressEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QBluetoothAddress(self->localAddress());
}

//  quint16 QBluetoothSocketBasePrivate::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK27QBluetoothSocketBasePrivate9localPortEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->localPort();
}

//  QString QBluetoothSocketBasePrivate::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK27QBluetoothSocketBasePrivate8peerNameEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QString(self->peerName());
}

//  QBluetoothAddress QBluetoothSocketBasePrivate::peerAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK27QBluetoothSocketBasePrivate11peerAddressEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QBluetoothAddress(self->peerAddress());
}

//  quint16 QBluetoothSocketBasePrivate::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK27QBluetoothSocketBasePrivate8peerPortEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->peerPort();
}

//  void QBluetoothSocketBasePrivate::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivate5abortEv(
    QBluetoothSocketBasePrivate *self) {
  self->abort();
}

//  void QBluetoothSocketBasePrivate::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivate5closeEv(
    QBluetoothSocketBasePrivate *self) {
  self->close();
}

//  qint64 QBluetoothSocketBasePrivate::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN27QBluetoothSocketBasePrivate9writeDataEPKcx(
    QBluetoothSocketBasePrivate *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  qint64 QBluetoothSocketBasePrivate::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK27QBluetoothSocketBasePrivate14bytesAvailableEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->bytesAvailable();
}

//  bool QBluetoothSocketBasePrivate::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QBluetoothSocketBasePrivate11canReadLineEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->canReadLine();
}

//  qint64 QBluetoothSocketBasePrivate::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK27QBluetoothSocketBasePrivate12bytesToWriteEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->bytesToWrite();
}

//  bool QBluetoothSocketBasePrivate::setSocketDescriptor(int
//      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
//      QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QBluetoothSocketBasePrivate19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    int socketDescriptor,
    QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState,
    int openMode) {
  return self->setSocketDescriptor(
      socketDescriptor,
      socketType,
      socketState,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

#if !(defined(QT_ANDROID_BLUETOOTH))
//  void QBluetoothSocketBasePrivate::connectToServiceHelper(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivate22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToServiceHelper(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}
#endif  // !(defined(QT_ANDROID_BLUETOOTH))

//  void QBluetoothSocketBasePrivate::connectToService(const
//      QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivate16connectToServiceERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothServiceInfo *service,
    int openMode) {
  self->connectToService(
      *service,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketBasePrivate::connectToService(const
//      QBluetoothAddress &address, const QBluetoothUuid &uuid,
//      QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBluetoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothAddress *address,
    const QBluetoothUuid *uuid,
    int openMode) {
  self->connectToService(
      *address,
      *uuid,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketBasePrivate::connectToService(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothSocketBasePrivate16connectToServiceERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToService(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  QBluetoothSocket *QBluetoothSocketBasePrivate::q_func()
extern "C" Q_DECL_EXPORT
QBluetoothSocket *ritual_ZN27QBluetoothSocketBasePrivate6q_funcEv(
    QBluetoothSocketBasePrivate *self) {
  return self->q_func();
}

//  const QBluetoothSocket *QBluetoothSocketBasePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothSocket *ritual_ZNK27QBluetoothSocketBasePrivate6q_funcEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQBluetoothSocketBasePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothSocketBasePrivate(
    QBluetoothSocketBasePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothSocketBasePrivate *>(self)->take(key, call);
}
