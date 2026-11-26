//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QAbstractSocketEngine' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkinterface.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>
#include <QtNetwork/qnetworkproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtNetwork__QAbstractSocketEngine.cpp, line 1, as moc:QAbstractSocketEngine
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN21QAbstractSocketEngineE_t {};
} // unnamed namespace

template <> constexpr inline auto QAbstractSocketEngine::qt_create_metaobjectdata<qt_meta_tag_ZN21QAbstractSocketEngineE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QAbstractSocketEngine",
        "readNotification",
        "",
        "writeNotification",
        "closeNotification",
        "exceptionNotification",
        "connectionNotification",
        "proxyAuthenticationRequired",
        "QNetworkProxy",
        "proxy",
        "QAuthenticator*",
        "authenticator"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'readNotification'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'writeNotification'
        QtMocHelpers::SlotData<void()>(3, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'closeNotification'
        QtMocHelpers::SlotData<void()>(4, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'exceptionNotification'
        QtMocHelpers::SlotData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'connectionNotification'
        QtMocHelpers::SlotData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'proxyAuthenticationRequired'
        QtMocHelpers::SlotData<void(const QNetworkProxy &, QAuthenticator *)>(7, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 8, 9 }, { 0x80000000 | 10, 11 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QAbstractSocketEngine, qt_meta_tag_ZN21QAbstractSocketEngineE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QAbstractSocketEngine::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QAbstractSocketEngineE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QAbstractSocketEngineE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN21QAbstractSocketEngineE_t>.metaTypes,
    nullptr
} };

void QAbstractSocketEngine::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QAbstractSocketEngine *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->readNotification(); break;
        case 1: _t->writeNotification(); break;
        case 2: _t->closeNotification(); break;
        case 3: _t->exceptionNotification(); break;
        case 4: _t->connectionNotification(); break;
        case 5: _t->proxyAuthenticationRequired((*reinterpret_cast<std::add_pointer_t<QNetworkProxy>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QAuthenticator*>>(_a[2]))); break;
        default: ;
        }
    }
}

const QMetaObject *QAbstractSocketEngine::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QAbstractSocketEngine::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN21QAbstractSocketEngineE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QAbstractSocketEngine::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 6)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 6;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 6)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 6;
    }
    return _id;
}
QT_WARNING_POP

//  from src/network/socket/qabstractsocketengine.cpp, line 120, as _ZN21QAbstractSocketEngine16readNotificationEv
inline void QAbstractSocketEngine::readNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->readNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 138, as _ZN21QAbstractSocketEngine17closeNotificationEv
inline void QAbstractSocketEngine::closeNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->closeNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 126, as _ZN21QAbstractSocketEngine17writeNotificationEv
inline void QAbstractSocketEngine::writeNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->writeNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 132, as _ZN21QAbstractSocketEngine21exceptionNotificationEv
inline void QAbstractSocketEngine::exceptionNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->exceptionNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 144, as _ZN21QAbstractSocketEngine22connectionNotificationEv
inline void QAbstractSocketEngine::connectionNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->connectionNotification();
}

//  from src/network/socket/qabstractsocketengine.cpp, line 151, as _ZN21QAbstractSocketEngine27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator
#if !defined(QT_NO_NETWORKPROXY)
inline void QAbstractSocketEngine::proxyAuthenticationRequired(const QNetworkProxy &proxy, QAuthenticator *authenticator)
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->proxyAuthenticationRequired(proxy, authenticator);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qabstractsocketengine.cpp, line 98, as _ZNK21QAbstractSocketEngine5errorEv
inline QAbstractSocket::SocketError QAbstractSocketEngine::error() const
{
    return d_func()->socketError;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 103, as _ZNK21QAbstractSocketEngine11errorStringEv
inline QString QAbstractSocketEngine::errorString() const
{
    return d_func()->socketErrorString;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 159, as _ZNK21QAbstractSocketEngine5stateEv
inline QAbstractSocket::SocketState QAbstractSocketEngine::state() const
{
    return d_func()->socketState;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 169, as _ZNK21QAbstractSocketEngine10socketTypeEv
inline QAbstractSocket::SocketType QAbstractSocketEngine::socketType() const
{
    return d_func()->socketType;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 179, as _ZNK21QAbstractSocketEngine8protocolEv
inline QAbstractSocket::NetworkLayerProtocol QAbstractSocketEngine::protocol() const
{
    return d_func()->socketProtocol;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 189, as _ZNK21QAbstractSocketEngine12localAddressEv
inline QHostAddress QAbstractSocketEngine::localAddress() const
{
    return d_func()->localAddress;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 199, as _ZNK21QAbstractSocketEngine9localPortEv
inline quint16 QAbstractSocketEngine::localPort() const
{
    return d_func()->localPort;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 209, as _ZNK21QAbstractSocketEngine11peerAddressEv
inline QHostAddress QAbstractSocketEngine::peerAddress() const
{
    return d_func()->peerAddress;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 219, as _ZNK21QAbstractSocketEngine8peerPortEv
inline quint16 QAbstractSocketEngine::peerPort() const
{
    return d_func()->peerPort;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 229, as _ZNK21QAbstractSocketEngine18inboundStreamCountEv
inline int QAbstractSocketEngine::inboundStreamCount() const
{
    return d_func()->inboundStreamCount;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 234, as _ZNK21QAbstractSocketEngine19outboundStreamCountEv
inline int QAbstractSocketEngine::outboundStreamCount() const
{
    return d_func()->outboundStreamCount;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 115, as _ZN21QAbstractSocketEngine11setReceiverEP29QAbstractSocketEngineReceiver
inline void QAbstractSocketEngine::setReceiver(QAbstractSocketEngineReceiver *receiver)
{
    d_func()->receiver = receiver;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 108, as _ZNK21QAbstractSocketEngine8setErrorEN15QAbstractSocket11SocketErrorERK7QString
inline void QAbstractSocketEngine::setError(QAbstractSocket::SocketError error, const QString &errorString) const
{
    Q_D(const QAbstractSocketEngine);
    d->socketError = error;
    d->socketErrorString = errorString;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 164, as _ZN21QAbstractSocketEngine8setStateEN15QAbstractSocket11SocketStateE
inline void QAbstractSocketEngine::setState(QAbstractSocket::SocketState state)
{
    d_func()->socketState = state;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 174, as _ZN21QAbstractSocketEngine13setSocketTypeEN15QAbstractSocket10SocketTypeE
inline void QAbstractSocketEngine::setSocketType(QAbstractSocket::SocketType socketType)
{
    d_func()->socketType = socketType;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 184, as _ZN21QAbstractSocketEngine11setProtocolEN15QAbstractSocket20NetworkLayerProtocolE
inline void QAbstractSocketEngine::setProtocol(QAbstractSocket::NetworkLayerProtocol protocol)
{
    d_func()->socketProtocol = protocol;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 194, as _ZN21QAbstractSocketEngine15setLocalAddressERK12QHostAddress
inline void QAbstractSocketEngine::setLocalAddress(const QHostAddress &address)
{
    d_func()->localAddress = address;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 204, as _ZN21QAbstractSocketEngine12setLocalPortEt
inline void QAbstractSocketEngine::setLocalPort(quint16 port)
{
    d_func()->localPort = port;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 214, as _ZN21QAbstractSocketEngine14setPeerAddressERK12QHostAddress
inline void QAbstractSocketEngine::setPeerAddress(const QHostAddress &address)
{
   d_func()->peerAddress = address;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 224, as _ZN21QAbstractSocketEngine11setPeerPortEt
inline void QAbstractSocketEngine::setPeerPort(quint16 port)
{
    d_func()->peerPort = port;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QAbstractSocketEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAbstractSocketEngine10metaObjectEv(
    const QAbstractSocketEngine *self) {
  return self->metaObject();
}

//  void *QAbstractSocketEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QAbstractSocketEngine11qt_metacastEPKc(
    QAbstractSocketEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractSocketEngine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QAbstractSocketEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractSocketEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if !defined(QT_NO_NETWORKPROXY)
//  QString QAbstractSocketEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractSocketEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractSocketEngine::tr(s, c, n));
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  bool QAbstractSocketEngine::initialize(QAbstractSocket::SocketType type,
//      QAbstractSocket::NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE(
    QAbstractSocketEngine *self,
    QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  return self->initialize(type, protocol);
}

//  bool QAbstractSocketEngine::initialize(qintptr socketDescriptor,
//      QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11SocketStateE(
    QAbstractSocketEngine *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState socketState) {
  return self->initialize(socketDescriptor, socketState);
}

//  qintptr QAbstractSocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK21QAbstractSocketEngine16socketDescriptorEv(
    const QAbstractSocketEngine *self) {
  return self->socketDescriptor();
}

//  bool QAbstractSocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractSocketEngine7isValidEv(
    const QAbstractSocketEngine *self) {
  return self->isValid();
}

//  bool QAbstractSocketEngine::connectToHost(const QHostAddress &address,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst(
    QAbstractSocketEngine *self,
    const QHostAddress *address,
    quint16 port) {
  return self->connectToHost(*address, port);
}

//  bool QAbstractSocketEngine::connectToHostByName(const QString &name,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt(
    QAbstractSocketEngine *self,
    const QString *name,
    quint16 port) {
  return self->connectToHostByName(*name, port);
}

//  bool QAbstractSocketEngine::bind(const QHostAddress &address, quint16
//      port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine4bindERK12QHostAddresst(
    QAbstractSocketEngine *self,
    const QHostAddress *address,
    quint16 port) {
  return self->bind(*address, port);
}

//  bool QAbstractSocketEngine::listen(int backlog)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine6listenEi(
    QAbstractSocketEngine *self,
    int backlog) {
  return self->listen(backlog);
}

//  qintptr QAbstractSocketEngine::accept()
extern "C" Q_DECL_EXPORT
qintptr ritual_ZN21QAbstractSocketEngine6acceptEv(
    QAbstractSocketEngine *self) {
  return self->accept();
}

//  void QAbstractSocketEngine::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine5closeEv(QAbstractSocketEngine *self) {
  self->close();
}

//  qint64 QAbstractSocketEngine::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QAbstractSocketEngine14bytesAvailableEv(
    const QAbstractSocketEngine *self) {
  return self->bytesAvailable();
}

//  qint64 QAbstractSocketEngine::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN21QAbstractSocketEngine4readEPcx(
    QAbstractSocketEngine *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  qint64 QAbstractSocketEngine::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN21QAbstractSocketEngine5writeEPKcx(
    QAbstractSocketEngine *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QAbstractSocketEngine::joinMulticastGroup(const QHostAddress
//      &groupAddress, const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface(
    QAbstractSocketEngine *self,
    const QHostAddress *groupAddress,
    const QNetworkInterface *iface) {
  return self->joinMulticastGroup(*groupAddress, *iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QAbstractSocketEngine::leaveMulticastGroup(const QHostAddress
//      &groupAddress, const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface(
    QAbstractSocketEngine *self,
    const QHostAddress *groupAddress,
    const QNetworkInterface *iface) {
  return self->leaveMulticastGroup(*groupAddress, *iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  QNetworkInterface QAbstractSocketEngine::multicastInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZNK21QAbstractSocketEngine18multicastInterfaceEv(
    const QAbstractSocketEngine *self) {
  return new QNetworkInterface(self->multicastInterface());
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QAbstractSocketEngine::setMulticastInterface(const QNetworkInterface
//      &iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkInterface(
    QAbstractSocketEngine *self,
    const QNetworkInterface *iface) {
  return self->setMulticastInterface(*iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
//  bool QAbstractSocketEngine::hasPendingDatagrams() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv(
    const QAbstractSocketEngine *self) {
  return self->hasPendingDatagrams();
}
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
//  qint64 QAbstractSocketEngine::pendingDatagramSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv(
    const QAbstractSocketEngine *self) {
  return self->pendingDatagramSize();
}
#endif  // !defined(QT_NO_UDPSOCKET)

//  qint64 QAbstractSocketEngine::readDatagram(char *data, qint64 maxlen,
//      QIpPacketHeader *header, PacketHeaderOptions a3)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN21QAbstractSocketEngine12readDatagramEPcxP15QIpPacketHeader6QFlagsINS_18PacketHeaderOptionEE(
    QAbstractSocketEngine *self,
    char *data,
    qint64 maxlen,
    QIpPacketHeader *header,
    int a3) {
  return self->readDatagram(
      data,
      maxlen,
      header,
      QFlags<QAbstractSocketEngine::PacketHeaderOption>::fromInt(a3));
}

//  qint64 QAbstractSocketEngine::writeDatagram(const char *data, qint64 len,
//      const QIpPacketHeader &header)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN21QAbstractSocketEngine13writeDatagramEPKcxRK15QIpPacketHeader(
    QAbstractSocketEngine *self,
    const char *data,
    qint64 len,
    const QIpPacketHeader *header) {
  return self->writeDatagram(data, len, *header);
}

//  qint64 QAbstractSocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QAbstractSocketEngine12bytesToWriteEv(
    const QAbstractSocketEngine *self) {
  return self->bytesToWrite();
}

//  int QAbstractSocketEngine::option(SocketOption option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE(
    const QAbstractSocketEngine *self,
    QAbstractSocketEngine::SocketOption option) {
  return self->option(option);
}

//  bool QAbstractSocketEngine::setOption(SocketOption option, int value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi(
    QAbstractSocketEngine *self,
    QAbstractSocketEngine::SocketOption option,
    int value) {
  return self->setOption(option, value);
}

//  bool QAbstractSocketEngine::waitForRead(QDeadlineTimer deadline, bool
//      *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine11waitForReadE14QDeadlineTimerPb(
    QAbstractSocketEngine *self,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForRead(*deadline, timedOut);
}

//  bool QAbstractSocketEngine::waitForWrite(QDeadlineTimer deadline, bool
//      *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine12waitForWriteE14QDeadlineTimerPb(
    QAbstractSocketEngine *self,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForWrite(*deadline, timedOut);
}

//  bool QAbstractSocketEngine::waitForReadOrWrite(bool *readyToRead, bool
//      *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer
//      deadline, bool *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractSocketEngine18waitForReadOrWriteEPbS0_bb14QDeadlineTimerS0_(
    QAbstractSocketEngine *self,
    bool *readyToRead,
    bool *readyToWrite,
    bool checkRead,
    bool checkWrite,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForReadOrWrite(
      readyToRead,
      readyToWrite,
      checkRead,
      checkWrite,
      *deadline,
      timedOut);
}

//  QAbstractSocket::SocketError QAbstractSocketEngine::error() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK21QAbstractSocketEngine5errorEv(
    const QAbstractSocketEngine *self) {
  return self->error();
}

//  QString QAbstractSocketEngine::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAbstractSocketEngine11errorStringEv(
    const QAbstractSocketEngine *self) {
  return new QString(self->errorString());
}

//  QAbstractSocket::SocketState QAbstractSocketEngine::state() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketState ritual_ZNK21QAbstractSocketEngine5stateEv(
    const QAbstractSocketEngine *self) {
  return self->state();
}

//  QAbstractSocket::SocketType QAbstractSocketEngine::socketType() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketType ritual_ZNK21QAbstractSocketEngine10socketTypeEv(
    const QAbstractSocketEngine *self) {
  return self->socketType();
}

//  QAbstractSocket::NetworkLayerProtocol QAbstractSocketEngine::protocol()
//      const
extern "C" Q_DECL_EXPORT
QAbstractSocket::NetworkLayerProtocol ritual_ZNK21QAbstractSocketEngine8protocolEv(
    const QAbstractSocketEngine *self) {
  return self->protocol();
}

//  QHostAddress QAbstractSocketEngine::localAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK21QAbstractSocketEngine12localAddressEv(
    const QAbstractSocketEngine *self) {
  return new QHostAddress(self->localAddress());
}

//  quint16 QAbstractSocketEngine::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QAbstractSocketEngine9localPortEv(
    const QAbstractSocketEngine *self) {
  return self->localPort();
}

//  QHostAddress QAbstractSocketEngine::peerAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK21QAbstractSocketEngine11peerAddressEv(
    const QAbstractSocketEngine *self) {
  return new QHostAddress(self->peerAddress());
}

//  quint16 QAbstractSocketEngine::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK21QAbstractSocketEngine8peerPortEv(
    const QAbstractSocketEngine *self) {
  return self->peerPort();
}

//  int QAbstractSocketEngine::inboundStreamCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractSocketEngine18inboundStreamCountEv(
    const QAbstractSocketEngine *self) {
  return self->inboundStreamCount();
}

//  int QAbstractSocketEngine::outboundStreamCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractSocketEngine19outboundStreamCountEv(
    const QAbstractSocketEngine *self) {
  return self->outboundStreamCount();
}

//  bool QAbstractSocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv(
    const QAbstractSocketEngine *self) {
  return self->isReadNotificationEnabled();
}

//  void QAbstractSocketEngine::setReadNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb(
    QAbstractSocketEngine *self,
    bool enable) {
  self->setReadNotificationEnabled(enable);
}

//  bool QAbstractSocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv(
    const QAbstractSocketEngine *self) {
  return self->isWriteNotificationEnabled();
}

//  void QAbstractSocketEngine::setWriteNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb(
    QAbstractSocketEngine *self,
    bool enable) {
  self->setWriteNotificationEnabled(enable);
}

//  bool QAbstractSocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv(
    const QAbstractSocketEngine *self) {
  return self->isExceptionNotificationEnabled();
}

//  void QAbstractSocketEngine::setExceptionNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb(
    QAbstractSocketEngine *self,
    bool enable) {
  self->setExceptionNotificationEnabled(enable);
}

//  void QAbstractSocketEngine::readNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine16readNotificationEv(
    QAbstractSocketEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractSocketEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "readNotification()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "readNotification()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractSocketEngine::writeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine17writeNotificationEv(
    QAbstractSocketEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractSocketEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "writeNotification()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "writeNotification()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractSocketEngine::closeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine17closeNotificationEv(
    QAbstractSocketEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractSocketEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "closeNotification()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "closeNotification()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractSocketEngine::exceptionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine21exceptionNotificationEv(
    QAbstractSocketEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractSocketEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "exceptionNotification()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "exceptionNotification()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QAbstractSocketEngine::connectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine22connectionNotificationEv(
    QAbstractSocketEngine *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractSocketEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "connectionNotification()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "connectionNotification()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocketEngine::proxyAuthenticationRequired(const
//      QNetworkProxy &proxy, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QAbstractSocketEngine *self,
    const QNetworkProxy *proxy,
    QAuthenticator *authenticator) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QAbstractSocketEngine")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "proxyAuthenticationRequired(const QNetworkProxy &,QAuthenticator *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "proxyAuthenticationRequired(const QNetworkProxy &,QAuthenticator *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(proxy)),
      const_cast<void *>(static_cast<const void *>(&authenticator)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QAbstractSocketEngine::setReceiver(QAbstractSocketEngineReceiver
//      *receiver)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine11setReceiverEP29QAbstractSocketEngineReceiver(
    QAbstractSocketEngine *self,
    QAbstractSocketEngineReceiver *receiver) {
  self->setReceiver(receiver);
}

//  void QAbstractSocketEngine::setError(QAbstractSocket::SocketError error,
//      const QString &errorString) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractSocketEngine8setErrorEN15QAbstractSocket11SocketErrorERK7QString(
    const QAbstractSocketEngine *self,
    QAbstractSocket::SocketError error,
    const QString *errorString) {
  self->setError(error, *errorString);
}

//  void QAbstractSocketEngine::setState(QAbstractSocket::SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine8setStateEN15QAbstractSocket11SocketStateE(
    QAbstractSocketEngine *self,
    QAbstractSocket::SocketState state) {
  self->setState(state);
}

//  void QAbstractSocketEngine::setSocketType(QAbstractSocket::SocketType
//      socketType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine13setSocketTypeEN15QAbstractSocket10SocketTypeE(
    QAbstractSocketEngine *self,
    QAbstractSocket::SocketType socketType) {
  self->setSocketType(socketType);
}

//  void
//      QAbstractSocketEngine::setProtocol(QAbstractSocket::NetworkLayerProto
//      col protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine11setProtocolEN15QAbstractSocket20NetworkLayerProtocolE(
    QAbstractSocketEngine *self,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->setProtocol(protocol);
}

//  void QAbstractSocketEngine::setLocalAddress(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine15setLocalAddressERK12QHostAddress(
    QAbstractSocketEngine *self,
    const QHostAddress *address) {
  self->setLocalAddress(*address);
}

//  void QAbstractSocketEngine::setLocalPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine12setLocalPortEt(
    QAbstractSocketEngine *self,
    quint16 port) {
  self->setLocalPort(port);
}

//  void QAbstractSocketEngine::setPeerAddress(const QHostAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine14setPeerAddressERK12QHostAddress(
    QAbstractSocketEngine *self,
    const QHostAddress *address) {
  self->setPeerAddress(*address);
}

//  void QAbstractSocketEngine::setPeerPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractSocketEngine11setPeerPortEt(
    QAbstractSocketEngine *self,
    quint16 port) {
  self->setPeerPort(port);
}

//  QAbstractSocketEnginePrivate *QAbstractSocketEngine::d_func()
extern "C" Q_DECL_EXPORT
QAbstractSocketEnginePrivate *ritual_ZN21QAbstractSocketEngine6d_funcEv(
    QAbstractSocketEngine *self) {
  return self->d_func();
}

//  const QAbstractSocketEnginePrivate *QAbstractSocketEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSocketEnginePrivate *ritual_ZNK21QAbstractSocketEngine6d_funcEv(
    const QAbstractSocketEngine *self) {
  return self->d_func();
}
