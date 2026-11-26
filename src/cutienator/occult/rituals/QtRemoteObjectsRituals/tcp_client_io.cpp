//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_tcpip_backend_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'TcpClientIo' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 7 rituals that lean on what moc
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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtRemoteObjects/private/qconnection_tcpip_backend_p.h>
#include <QtNetwork/qhostinfo.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__TcpClientIo.cpp, line 1, as moc:TcpClientIo
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN11TcpClientIoE_t {};
} // unnamed namespace

template <> constexpr inline auto TcpClientIo::qt_create_metaobjectdata<qt_meta_tag_ZN11TcpClientIoE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "TcpClientIo",
        "onError",
        "",
        "QAbstractSocket::SocketError",
        "error",
        "onStateChanged",
        "QAbstractSocket::SocketState",
        "state"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'onError'
        QtMocHelpers::SlotData<void(QAbstractSocket::SocketError)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'onStateChanged'
        QtMocHelpers::SlotData<void(QAbstractSocket::SocketState)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<TcpClientIo, qt_meta_tag_ZN11TcpClientIoE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject TcpClientIo::staticMetaObject = { {
    QMetaObject::SuperData::link<QtROClientIoDevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN11TcpClientIoE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN11TcpClientIoE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN11TcpClientIoE_t>.metaTypes,
    nullptr
} };

void TcpClientIo::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<TcpClientIo *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->onError((*reinterpret_cast<std::add_pointer_t<QAbstractSocket::SocketError>>(_a[1]))); break;
        case 1: _t->onStateChanged((*reinterpret_cast<std::add_pointer_t<QAbstractSocket::SocketState>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 0:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QAbstractSocket::SocketError >(); break;
            }
            break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QAbstractSocket::SocketState >(); break;
            }
            break;
        }
    }
}

const QMetaObject *TcpClientIo::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *TcpClientIo::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN11TcpClientIoE_t>.strings))
        return static_cast<void*>(this);
    return QtROClientIoDevice::qt_metacast(_clname);
}

int TcpClientIo::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QtROClientIoDevice::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 84, as _ZN11TcpClientIo14onStateChangedEN15QAbstractSocket11SocketStateE
inline void TcpClientIo::onStateChanged(QAbstractSocket::SocketState state)
{
    if (state == QAbstractSocket::ClosingState && !isClosing()) {
        m_socket->abort();
        emit shouldReconnect(this);
    }
    if (state == QAbstractSocket::ConnectedState)
        initializeDataStream();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 66, as _ZN11TcpClientIo7onErrorEN15QAbstractSocket11SocketErrorE
inline void TcpClientIo::onError(QAbstractSocket::SocketError error)
{
    qCDebug(QT_REMOTEOBJECT) << "onError" << error;

    switch (error) {
    case QAbstractSocket::HostNotFoundError:     //Host not there, wait and try again
    case QAbstractSocket::ConnectionRefusedError:
    case QAbstractSocket::NetworkError:
        emit shouldReconnect(this);
        break;
    case QAbstractSocket::AddressInUseError:
        //... TODO error reporting
        break;
    default:
        break;
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 11, as _ZN11TcpClientIoC1EP7QObject
inline TcpClientIo::TcpClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QTcpSocket(this))
{
    connect(m_socket, &QTcpSocket::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket, &QAbstractSocket::errorOccurred, this, &TcpClientIo::onError);
    connect(m_socket, &QTcpSocket::stateChanged, this, &TcpClientIo::onStateChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 20, as _ZN11TcpClientIoD1Ev
inline TcpClientIo::~TcpClientIo()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 25, as _ZNK11TcpClientIo10connectionEv
inline QIODevice *TcpClientIo::connection() const
{
    return m_socket;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 45, as _ZN11TcpClientIo15connectToServerEv
inline void TcpClientIo::connectToServer()
{
    if (isOpen())
        return;
    const QString &host = url().host();
    QHostAddress address(host);
    if (address.isNull())
        address = QHostInfo::fromName(host).addresses().value(0);

    if (address.isNull())
        qWarning("connectToServer(): Failed to resolve host %s", qUtf8Printable(host));
    else
        m_socket->connectToHost(address, url().port());
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 60, as _ZNK11TcpClientIo6isOpenEv
inline bool TcpClientIo::isOpen() const
{
    return (!isClosing() && (m_socket->state() == QAbstractSocket::ConnectedState
                             || m_socket->state() == QAbstractSocket::ConnectingState));
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 30, as _ZN11TcpClientIo7doCloseEv
inline void TcpClientIo::doClose()
{
    if (m_socket->isOpen()) {
        connect(m_socket, &QTcpSocket::disconnected, this, &QObject::deleteLater);
        m_socket->disconnectFromHost();
    } else {
        this->deleteLater();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_tcpip_backend.cpp, line 40, as _ZN11TcpClientIo22doDisconnectFromServerEv
inline void TcpClientIo::doDisconnectFromServer()
{
    m_socket->disconnectFromHost();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *TcpClientIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11TcpClientIo10metaObjectEv(
    const TcpClientIo *self) {
  return self->metaObject();
}

//  void *TcpClientIo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11TcpClientIo11qt_metacastEPKc(
    TcpClientIo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int TcpClientIo::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11TcpClientIo11qt_metacallEN11QMetaObject4CallEiPPv(
    TcpClientIo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString TcpClientIo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11TcpClientIo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(TcpClientIo::tr(s, c, n));
}

//  TcpClientIo::TcpClientIo(QObject *parent)
extern "C" Q_DECL_EXPORT
TcpClientIo *ritual_ZN11TcpClientIoC1EP7QObject(QObject *parent) {
  return new TcpClientIo(parent);
}

//  TcpClientIo::~TcpClientIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIoD1Ev(TcpClientIo *self) {
  delete self;
}

//  QIODevice *TcpClientIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11TcpClientIo10connectionEv(const TcpClientIo *self) {
  return self->connection();
}

//  void TcpClientIo::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo15connectToServerEv(TcpClientIo *self) {
  self->connectToServer();
}

//  bool TcpClientIo::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11TcpClientIo6isOpenEv(const TcpClientIo *self) {
  return self->isOpen();
}

//  void TcpClientIo::onError(QAbstractSocket::SocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo7onErrorEN15QAbstractSocket11SocketErrorE(
    TcpClientIo *self,
    QAbstractSocket::SocketError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "TcpClientIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onError(QAbstractSocket::SocketError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onError(QAbstractSocket::SocketError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void TcpClientIo::onStateChanged(QAbstractSocket::SocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo14onStateChangedEN15QAbstractSocket11SocketStateE(
    TcpClientIo *self,
    QAbstractSocket::SocketState state) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "TcpClientIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onStateChanged(QAbstractSocket::SocketState)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onStateChanged(QAbstractSocket::SocketState)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&state)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void TcpClientIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo7doCloseEv(TcpClientIo *self) {
  self->doClose();
}

//  void TcpClientIo::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11TcpClientIo22doDisconnectFromServerEv(TcpClientIo *self) {
  self->doDisconnectFromServer();
}
