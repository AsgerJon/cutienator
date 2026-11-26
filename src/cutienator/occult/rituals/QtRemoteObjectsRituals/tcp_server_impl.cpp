//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'TcpServerImpl' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 6 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qloggingcategory.h>
#include <QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#include <QtNetwork/qhostinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__TcpServerImpl.cpp, line 1, as moc:TcpServerImpl
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN13TcpServerImplE_t {};
} // unnamed namespace

template <> constexpr inline auto TcpServerImpl::qt_create_metaobjectdata<qt_meta_tag_ZN13TcpServerImplE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "TcpServerImpl"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<TcpServerImpl, qt_meta_tag_ZN13TcpServerImplE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject TcpServerImpl::staticMetaObject = { {
    QMetaObject::SuperData::link<QConnectionAbstractServer::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13TcpServerImplE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13TcpServerImplE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN13TcpServerImplE_t>.metaTypes,
    nullptr
} };

void TcpServerImpl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<TcpServerImpl *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *TcpServerImpl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *TcpServerImpl::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13TcpServerImplE_t>.strings))
        return static_cast<void*>(this);
    return QConnectionAbstractServer::qt_metacast(_clname);
}

int TcpServerImpl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QConnectionAbstractServer::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 95, as _ZN11TcpServerIoC1EP10QTcpSocketP7QObject
inline TcpServerIo::TcpServerIo(QTcpSocket *conn, QObject *parent)
    : QtROServerIoDevice(parent), m_connection(conn)
{
    m_connection->setParent(this);
    connect(conn, &QIODevice::readyRead, this, &QtROServerIoDevice::readyRead);
    connect(conn, &QAbstractSocket::disconnected, this, &QtROServerIoDevice::disconnected);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 115, as _ZN13TcpServerImplC1EP7QObject
inline TcpServerImpl::TcpServerImpl(QObject *parent)
    : QConnectionAbstractServer(parent)
{
    connect(&m_server, &QTcpServer::newConnection, this, &QConnectionAbstractServer::newConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 121, as _ZN13TcpServerImplD1Ev
inline TcpServerImpl::~TcpServerImpl()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 134, as _ZNK13TcpServerImpl21hasPendingConnectionsEv
inline bool TcpServerImpl::hasPendingConnections() const
{
    return m_server.hasPendingConnections();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 126, as _ZN13TcpServerImpl22configureNewConnectionEv
inline QtROServerIoDevice *TcpServerImpl::configureNewConnection()
{
    if (!m_server.isListening())
        return nullptr;

    return new TcpServerIo(m_server.nextPendingConnection(), this);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 139, as _ZNK13TcpServerImpl7addressEv
inline QUrl TcpServerImpl::address() const
{
    return m_originalUrl;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 144, as _ZN13TcpServerImpl6listenERK4QUrl
inline bool TcpServerImpl::listen(const QUrl &address)
{
    QHostAddress host(address.host());
    if (host.isNull()) {
        if (address.host().isEmpty()) {
            host = QHostAddress::Any;
        } else {
            qCWarning(QT_REMOTEOBJECT) << address.host() << " is not an IP address, trying to resolve it";
            QHostInfo info = QHostInfo::fromName(address.host());
            if (info.addresses().isEmpty())
                host = QHostAddress::Any;
            else
                host = info.addresses().constFirst();
        }
    }

    bool ret = m_server.listen(host, quint16(address.port()));
    if (ret) {
        m_originalUrl.setScheme(QLatin1String("tcp"));
        m_originalUrl.setHost(m_server.serverAddress().toString());
        m_originalUrl.setPort(m_server.serverPort());
    }
    return ret;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 169, as _ZNK13TcpServerImpl11serverErrorEv
inline QAbstractSocket::SocketError TcpServerImpl::serverError() const
{
    return m_server.serverError();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 174, as _ZN13TcpServerImpl5closeEv
inline void TcpServerImpl::close()
{
    m_server.close();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *TcpServerImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13TcpServerImpl10metaObjectEv(
    const TcpServerImpl *self) {
  return self->metaObject();
}

//  void *TcpServerImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13TcpServerImpl11qt_metacastEPKc(
    TcpServerImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int TcpServerImpl::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13TcpServerImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    TcpServerImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString TcpServerImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13TcpServerImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(TcpServerImpl::tr(s, c, n));
}

//  TcpServerImpl::TcpServerImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
TcpServerImpl *ritual_ZN13TcpServerImplC1EP7QObject(QObject *parent) {
  return new TcpServerImpl(parent);
}

//  TcpServerImpl::~TcpServerImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TcpServerImplD1Ev(TcpServerImpl *self) {
  delete self;
}

//  bool TcpServerImpl::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13TcpServerImpl21hasPendingConnectionsEv(
    const TcpServerImpl *self) {
  return self->hasPendingConnections();
}

//  QtROServerIoDevice *TcpServerImpl::configureNewConnection()
extern "C" Q_DECL_EXPORT
QtROServerIoDevice *ritual_ZN13TcpServerImpl22configureNewConnectionEv(
    TcpServerImpl *self) {
  return self->configureNewConnection();
}

//  QUrl TcpServerImpl::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13TcpServerImpl7addressEv(const TcpServerImpl *self) {
  return new QUrl(self->address());
}

//  bool TcpServerImpl::listen(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13TcpServerImpl6listenERK4QUrl(
    TcpServerImpl *self,
    const QUrl *address) {
  return self->listen(*address);
}

//  QAbstractSocket::SocketError TcpServerImpl::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK13TcpServerImpl11serverErrorEv(
    const TcpServerImpl *self) {
  return self->serverError();
}

//  void TcpServerImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN13TcpServerImpl5closeEv(TcpServerImpl *self) {
  self->close();
}
