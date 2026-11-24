//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtBluetooth/qbluetoothsocket.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBluetoothSocket that Python can take functions over in. Every QBluetoothSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBluetoothSocketCall0)(const void *, int *);
typedef bool (*CuteQBluetoothSocketCall1)(const void *, int *);
typedef qint64 (*CuteQBluetoothSocketCall2)(const void *, int *);
typedef qint64 (*CuteQBluetoothSocketCall3)(const void *, int *);
typedef bool (*CuteQBluetoothSocketCall4)(const void *, int *);
typedef bool (*CuteQBluetoothSocketCall5)(const void *, int, int *);
typedef qint64 (*CuteQBluetoothSocketCall6)(const void *, int *);
typedef qint64 (*CuteQBluetoothSocketCall7)(const void *, int *);
typedef bool (*CuteQBluetoothSocketCall8)(const void *, qint64, int *);
typedef bool (*CuteQBluetoothSocketCall9)(const void *, int *);
typedef bool (*CuteQBluetoothSocketCall10)(const void *, int *);
typedef bool (*CuteQBluetoothSocketCall11)(const void *, int, int *);
typedef bool (*CuteQBluetoothSocketCall12)(const void *, int, int *);
typedef qint64 (*CuteQBluetoothSocketCall13)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothSocketCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothSocketCall15)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketCall16)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketCall17)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketCall19)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothSocketCall20)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothSocket : public QBluetoothSocket {
public:
  using QBluetoothSocket::QBluetoothSocket;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
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

  //  void QBluetoothSocket::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQBluetoothSocketCall0 call = reinterpret_cast<CuteQBluetoothSocketCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QBluetoothSocket::close();
  }

  //  bool QBluetoothSocket::isSequential() const
  bool isSequential() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBluetoothSocketCall1 call = reinterpret_cast<CuteQBluetoothSocketCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBluetoothSocket::isSequential();
  }

  //  qint64 QBluetoothSocket::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQBluetoothSocketCall2 call = reinterpret_cast<CuteQBluetoothSocketCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QBluetoothSocket::bytesAvailable();
  }

  //  qint64 QBluetoothSocket::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQBluetoothSocketCall3 call = reinterpret_cast<CuteQBluetoothSocketCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QBluetoothSocket::bytesToWrite();
  }

  //  bool QBluetoothSocket::canReadLine() const
  bool canReadLine() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQBluetoothSocketCall4 call = reinterpret_cast<CuteQBluetoothSocketCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBluetoothSocket::canReadLine();
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[5]) {
      int handled = 0;
      CuteQBluetoothSocketCall5 call = reinterpret_cast<CuteQBluetoothSocketCall5>(taken[5]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  qint64 QIODevice::pos() const
  qint64 pos() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQBluetoothSocketCall6 call = reinterpret_cast<CuteQBluetoothSocketCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::pos();
  }

  //  qint64 QIODevice::size() const
  qint64 size() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQBluetoothSocketCall7 call = reinterpret_cast<CuteQBluetoothSocketCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::size();
  }

  //  bool QIODevice::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[8]) {
      int handled = 0;
      CuteQBluetoothSocketCall8 call = reinterpret_cast<CuteQBluetoothSocketCall8>(taken[8]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QIODevice::seek(pos);
  }

  //  bool QIODevice::atEnd() const
  bool atEnd() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQBluetoothSocketCall9 call = reinterpret_cast<CuteQBluetoothSocketCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[10]) {
      int handled = 0;
      CuteQBluetoothSocketCall10 call = reinterpret_cast<CuteQBluetoothSocketCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[11]) {
      int handled = 0;
      CuteQBluetoothSocketCall11 call = reinterpret_cast<CuteQBluetoothSocketCall11>(taken[11]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQBluetoothSocketCall12 call = reinterpret_cast<CuteQBluetoothSocketCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQBluetoothSocketCall13 call = reinterpret_cast<CuteQBluetoothSocketCall13>(taken[13]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQBluetoothSocketCall14 call = reinterpret_cast<CuteQBluetoothSocketCall14>(taken[14]);
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
      CuteQBluetoothSocketCall15 call = reinterpret_cast<CuteQBluetoothSocketCall15>(taken[15]);
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
      CuteQBluetoothSocketCall16 call = reinterpret_cast<CuteQBluetoothSocketCall16>(taken[16]);
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
      CuteQBluetoothSocketCall17 call = reinterpret_cast<CuteQBluetoothSocketCall17>(taken[17]);
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
      CuteQBluetoothSocketCall18 call = reinterpret_cast<CuteQBluetoothSocketCall18>(taken[18]);
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
      CuteQBluetoothSocketCall19 call = reinterpret_cast<CuteQBluetoothSocketCall19>(taken[19]);
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
      CuteQBluetoothSocketCall20 call = reinterpret_cast<CuteQBluetoothSocketCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QBluetoothSocket10metaObjectEv(
    const QBluetoothSocket *self) {
  return self->metaObject();
}

//  QString QBluetoothSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QBluetoothSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBluetoothSocket::tr(s, c, n));
}

//  QBluetoothSocketBasePrivate *QBluetoothSocket::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothSocketBasePrivate *ritual_ZN16QBluetoothSocket6d_funcEv(
    QBluetoothSocket *self) {
  return self->d_func();
}

//  const QBluetoothSocketBasePrivate *QBluetoothSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothSocketBasePrivate *ritual_ZNK16QBluetoothSocket6d_funcEv(
    const QBluetoothSocket *self) {
  return self->d_func();
}

//  QBluetoothSocket::QBluetoothSocket(QBluetoothServiceInfo::Protocol
//      socketType, QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothSocket *ritual_ZN16QBluetoothSocketC1EN21QBluetoothServiceInfo8ProtocolEP7QObject(
    QBluetoothServiceInfo::Protocol socketType,
    QObject *parent) {
  return new CuteQBluetoothSocket(socketType, parent);
}

//  QBluetoothSocket::QBluetoothSocket(QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothSocket *ritual_ZN16QBluetoothSocketC1EP7QObject(QObject *parent) {
  return new CuteQBluetoothSocket(parent);
}

//  QBluetoothSocket::~QBluetoothSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocketD1Ev(QBluetoothSocket *self) {
  delete self;
}

//  void QBluetoothSocket::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket5abortEv(QBluetoothSocket *self) {
  self->abort();
}

//  void QBluetoothSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket5closeEv(QBluetoothSocket *self) {
  self->close();
}

//  bool QBluetoothSocket::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QBluetoothSocket12isSequentialEv(
    const QBluetoothSocket *self) {
  return self->isSequential();
}

//  qint64 QBluetoothSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QBluetoothSocket14bytesAvailableEv(
    const QBluetoothSocket *self) {
  return self->bytesAvailable();
}

//  qint64 QBluetoothSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK16QBluetoothSocket12bytesToWriteEv(
    const QBluetoothSocket *self) {
  return self->bytesToWrite();
}

//  bool QBluetoothSocket::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QBluetoothSocket11canReadLineEv(
    const QBluetoothSocket *self) {
  return self->canReadLine();
}

//  void QBluetoothSocket::connectToService(const QBluetoothServiceInfo
//      &service, OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket16connectToServiceERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocket *self,
    const QBluetoothServiceInfo *service,
    int openMode) {
  self->connectToService(
      *service,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocket::connectToService(const QBluetoothAddress &address,
//      const QBluetoothUuid &uuid, OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket16connectToServiceERK17QBluetoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocket *self,
    const QBluetoothAddress *address,
    const QBluetoothUuid *uuid,
    int openMode) {
  self->connectToService(
      *address,
      *uuid,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocket::connectToService(const QBluetoothAddress &address,
//      quint16 port, OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket16connectToServiceERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocket *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToService(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocket::connectToService(const QBluetoothAddress &address,
//      QBluetoothUuid::ServiceClassUuid uuid, OpenMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket16connectToServiceERK17QBluetoothAddressN14QBluetoothUuid16ServiceClassUuidE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocket *self,
    const QBluetoothAddress *address,
    QBluetoothUuid::ServiceClassUuid uuid,
    int mode) {
  self->connectToService(
      *address,
      uuid,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  void QBluetoothSocket::disconnectFromService()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket21disconnectFromServiceEv(
    QBluetoothSocket *self) {
  self->disconnectFromService();
}

//  QString QBluetoothSocket::localName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBluetoothSocket9localNameEv(
    const QBluetoothSocket *self) {
  return new QString(self->localName());
}

//  QBluetoothAddress QBluetoothSocket::localAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK16QBluetoothSocket12localAddressEv(
    const QBluetoothSocket *self) {
  return new QBluetoothAddress(self->localAddress());
}

//  quint16 QBluetoothSocket::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK16QBluetoothSocket9localPortEv(
    const QBluetoothSocket *self) {
  return self->localPort();
}

//  QString QBluetoothSocket::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBluetoothSocket8peerNameEv(
    const QBluetoothSocket *self) {
  return new QString(self->peerName());
}

//  QBluetoothAddress QBluetoothSocket::peerAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK16QBluetoothSocket11peerAddressEv(
    const QBluetoothSocket *self) {
  return new QBluetoothAddress(self->peerAddress());
}

//  quint16 QBluetoothSocket::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK16QBluetoothSocket8peerPortEv(
    const QBluetoothSocket *self) {
  return self->peerPort();
}

//  bool QBluetoothSocket::setSocketDescriptor(int socketDescriptor,
//      QBluetoothServiceInfo::Protocol socketType, SocketState socketState,
//      OpenMode openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QBluetoothSocket19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolENS_11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocket *self,
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

//  int QBluetoothSocket::socketDescriptor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QBluetoothSocket16socketDescriptorEv(
    const QBluetoothSocket *self) {
  return self->socketDescriptor();
}

//  QBluetoothServiceInfo::Protocol QBluetoothSocket::socketType() const
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Protocol ritual_ZNK16QBluetoothSocket10socketTypeEv(
    const QBluetoothSocket *self) {
  return self->socketType();
}

//  SocketState QBluetoothSocket::state() const
extern "C" Q_DECL_EXPORT
QBluetoothSocket::SocketState ritual_ZNK16QBluetoothSocket5stateEv(
    const QBluetoothSocket *self) {
  return self->state();
}

//  SocketError QBluetoothSocket::error() const
extern "C" Q_DECL_EXPORT
QBluetoothSocket::SocketError ritual_ZNK16QBluetoothSocket5errorEv(
    const QBluetoothSocket *self) {
  return self->error();
}

//  QString QBluetoothSocket::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QBluetoothSocket11errorStringEv(
    const QBluetoothSocket *self) {
  return new QString(self->errorString());
}

//  void
//      QBluetoothSocket::setPreferredSecurityFlags(QBluetooth::SecurityFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket25setPreferredSecurityFlagsE6QFlagsIN10QBluetooth8SecurityEE(
    QBluetoothSocket *self,
    int flags) {
  self->setPreferredSecurityFlags(
      QFlags<QBluetooth::Security>::fromInt(flags));
}

//  QBluetooth::SecurityFlags QBluetoothSocket::preferredSecurityFlags()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QBluetoothSocket22preferredSecurityFlagsEv(
    const QBluetoothSocket *self) {
  return static_cast<int>(self->preferredSecurityFlags().toInt());
}

//  qint64 QBluetoothSocket::writeData(const char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN16QBluetoothSocket9writeDataEPKcx(
    QBluetoothSocket *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  void QBluetoothSocket::setSocketState(SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket14setSocketStateENS_11SocketStateE(
    QBluetoothSocket *self,
    QBluetoothSocket::SocketState state) {
  self->setSocketState(state);
}

//  void QBluetoothSocket::setSocketError(SocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket14setSocketErrorENS_11SocketErrorE(
    QBluetoothSocket *self,
    QBluetoothSocket::SocketError error) {
  self->setSocketError(error);
}

//  void QBluetoothSocket::doDeviceDiscovery(const QBluetoothServiceInfo
//      &service, OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket17doDeviceDiscoveryERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocket *self,
    const QBluetoothServiceInfo *service,
    int openMode) {
  self->doDeviceDiscovery(
      *service,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocket::serviceDiscovered(const QBluetoothServiceInfo
//      &service)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket17serviceDiscoveredERK21QBluetoothServiceInfo(
    QBluetoothSocket *self,
    const QBluetoothServiceInfo *service) {
  self->serviceDiscovered(*service);
}

//  void QBluetoothSocket::discoveryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothSocket17discoveryFinishedEv(
    QBluetoothSocket *self) {
  self->discoveryFinished();
}

#if QT_CONFIG(bluez)
//  QBluetoothSocket::QBluetoothSocket(QBluetoothSocketBasePrivate *d,
//      QBluetoothServiceInfo::Protocol socketType, QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothSocket *ritual_ZN16QBluetoothSocketC1EP27QBluetoothSocketBasePrivateN21QBluetoothServiceInfo8ProtocolEP7QObject(
    QBluetoothSocketBasePrivate *d,
    QBluetoothServiceInfo::Protocol socketType,
    QObject *parent) {
  return new CuteQBluetoothSocket(d, socketType, parent);
}
#endif  // QT_CONFIG(bluez)

//  a Python function taken by a CuteQBluetoothSocket, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothSocket(
    QBluetoothSocket *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothSocket *>(self)->take(key, call);
}

//  void QBluetoothSocket::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QBluetoothSocket5closeEv(QBluetoothSocket *self) {
  self->QBluetoothSocket::close();
}

//  bool QBluetoothSocket::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QBluetoothSocket12isSequentialEv(
    const QBluetoothSocket *self) {
  return self->QBluetoothSocket::isSequential();
}

//  qint64 QBluetoothSocket::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QBluetoothSocket14bytesAvailableEv(
    const QBluetoothSocket *self) {
  return self->QBluetoothSocket::bytesAvailable();
}

//  qint64 QBluetoothSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK16QBluetoothSocket12bytesToWriteEv(
    const QBluetoothSocket *self) {
  return self->QBluetoothSocket::bytesToWrite();
}

//  bool QBluetoothSocket::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QBluetoothSocket11canReadLineEv(
    const QBluetoothSocket *self) {
  return self->QBluetoothSocket::canReadLine();
}
