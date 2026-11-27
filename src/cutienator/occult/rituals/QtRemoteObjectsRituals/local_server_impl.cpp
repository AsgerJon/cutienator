//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-26: moc's output for 'LocalServerImpl'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Edited by hand on 2026-11-27:
//  code taken from Qt's source no longer stands under defined(Q_OS_LINUX),
//  which Qt does not write there; its rituals no longer stand under
//  defined(Q_OS_LINUX), as the code taken from Qt they call no longer does.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__LocalServerImpl.cpp, line 1, as moc:LocalServerImpl
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15LocalServerImplE_t {};
} // unnamed namespace

template <> constexpr inline auto LocalServerImpl::qt_create_metaobjectdata<qt_meta_tag_ZN15LocalServerImplE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "LocalServerImpl"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<LocalServerImpl, qt_meta_tag_ZN15LocalServerImplE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject LocalServerImpl::staticMetaObject = { {
    QMetaObject::SuperData::link<QConnectionAbstractServer::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15LocalServerImplE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15LocalServerImplE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15LocalServerImplE_t>.metaTypes,
    nullptr
} };

void LocalServerImpl::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<LocalServerImpl *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *LocalServerImpl::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *LocalServerImpl::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15LocalServerImplE_t>.strings))
        return static_cast<void*>(this);
    return QConnectionAbstractServer::qt_metacast(_clname);
}

int LocalServerImpl::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QConnectionAbstractServer::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 124, as _ZN15LocalServerImpl22configureNewConnectionEv
inline QtROServerIoDevice *LocalServerImpl::configureNewConnection()
{
    if (!m_server.isListening())
        return nullptr;

    return new LocalServerIo(m_server.nextPendingConnection(), this);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 169, as _ZN15LocalServerImpl5closeEv
inline void LocalServerImpl::close()
{
    m_server.close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 146, as _ZN15LocalServerImpl6listenERK4QUrl
inline bool LocalServerImpl::listen(const QUrl &address)
{
#ifdef Q_OS_ANDROID
    if (!m_server.socketOptions().testFlag(QLocalServer::AbstractNamespaceOption))
        qWarning() << "It is recommended to use 'localabstract' over 'local' on Android.";
#endif
#ifdef Q_OS_UNIX
    bool res = m_server.listen(address.path());
    if (!res) {
        QLocalServer::removeServer(address.path());
        res = m_server.listen(address.path());
    }
    return res;
#else
    return m_server.listen(address.path());
#endif
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 119, as _ZN15LocalServerImplD0Ev
inline LocalServerImpl::~LocalServerImpl()
{
    m_server.close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 164, as _ZNK15LocalServerImpl11serverErrorEv
inline QAbstractSocket::SocketError LocalServerImpl::serverError() const
{
    return m_server.serverError();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 132, as _ZNK15LocalServerImpl21hasPendingConnectionsEv
inline bool LocalServerImpl::hasPendingConnections() const
{
    return m_server.hasPendingConnections();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 137, as _ZNK15LocalServerImpl7addressEv
inline QUrl LocalServerImpl::address() const
{
    QUrl result;
    result.setPath(m_server.serverName());
    result.setScheme(QRemoteObjectStringLiterals::local());

    return result;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 95, as _ZN13LocalServerIoC1EP12QLocalSocketP7QObject
inline LocalServerIo::LocalServerIo(QLocalSocket *conn, QObject *parent)
    : QtROServerIoDevice(parent), m_connection(conn)
{
    m_connection->setParent(this);
    connect(conn, &QIODevice::readyRead, this, &QtROServerIoDevice::readyRead);
    connect(conn, &QLocalSocket::disconnected, this, &QtROServerIoDevice::disconnected);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 113, as _ZN15LocalServerImplC1EP7QObject
inline LocalServerImpl::LocalServerImpl(QObject *parent)
    : QConnectionAbstractServer(parent)
{
    connect(&m_server, &QLocalServer::newConnection, this, &QConnectionAbstractServer::newConnection);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 174, as _ZN15LocalServerImpl16setSocketOptionsE6QFlagsIN12QLocalServer12SocketOptionEE
inline void LocalServerImpl::setSocketOptions(QLocalServer::SocketOptions options)
{
    m_server.setSocketOptions(options);
}
//  -----------------------------------------------------------------------

//  A LocalServerImpl that Python can take functions over in. Every LocalServerImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteLocalServerImplCall0)(const void *, int *);
typedef void * (*CuteLocalServerImplCall1)(const void *, int *);
typedef const QUrl * (*CuteLocalServerImplCall2)(const void *, int *);
typedef bool (*CuteLocalServerImplCall3)(const void *, const QUrl *, int *);
typedef int (*CuteLocalServerImplCall4)(const void *, int *);
typedef void (*CuteLocalServerImplCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLocalServerImplCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLocalServerImplCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalServerImplCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalServerImplCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalServerImplCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalServerImplCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalServerImplCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLocalServerImpl : public LocalServerImpl {
public:
  using LocalServerImpl::LocalServerImpl;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QConnectionAbstractServer21hasPendingConnectionsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QConnectionAbstractServer22configureNewConnectionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QConnectionAbstractServer7addressEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QConnectionAbstractServer6listenERK4QUrl")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QConnectionAbstractServer11serverErrorEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QConnectionAbstractServer5closeEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool LocalServerImpl::hasPendingConnections() const
  bool hasPendingConnections() const override {
    if (taken[0]) {
      int handled = 0;
      CuteLocalServerImplCall0 call = reinterpret_cast<CuteLocalServerImplCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return LocalServerImpl::hasPendingConnections();
  }

  //  QtROServerIoDevice *LocalServerImpl::configureNewConnection()
  QtROServerIoDevice *configureNewConnection() override {
    if (taken[1]) {
      int handled = 0;
      CuteLocalServerImplCall1 call = reinterpret_cast<CuteLocalServerImplCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QtROServerIoDevice *>(given);
    }
    return LocalServerImpl::configureNewConnection();
  }

  //  QUrl LocalServerImpl::address() const
  QUrl address() const override {
    if (taken[2]) {
      int handled = 0;
      CuteLocalServerImplCall2 call = reinterpret_cast<CuteLocalServerImplCall2>(taken[2]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return LocalServerImpl::address();
  }

  //  bool LocalServerImpl::listen(const QUrl &address)
  bool listen(const QUrl &address) override {
    if (taken[3]) {
      int handled = 0;
      CuteLocalServerImplCall3 call = reinterpret_cast<CuteLocalServerImplCall3>(taken[3]);
      bool given = call(this, &address, &handled);
      if (handled) return given;
    }
    return LocalServerImpl::listen(address);
  }

  //  QAbstractSocket::SocketError LocalServerImpl::serverError() const
  QAbstractSocket::SocketError serverError() const override {
    if (taken[4]) {
      int handled = 0;
      CuteLocalServerImplCall4 call = reinterpret_cast<CuteLocalServerImplCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSocket::SocketError>(given);
    }
    return LocalServerImpl::serverError();
  }

  //  void LocalServerImpl::close()
  void close() override {
    if (taken[5]) {
      int handled = 0;
      CuteLocalServerImplCall5 call = reinterpret_cast<CuteLocalServerImplCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    LocalServerImpl::close();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteLocalServerImplCall6 call = reinterpret_cast<CuteLocalServerImplCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteLocalServerImplCall7 call = reinterpret_cast<CuteLocalServerImplCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteLocalServerImplCall8 call = reinterpret_cast<CuteLocalServerImplCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteLocalServerImplCall9 call = reinterpret_cast<CuteLocalServerImplCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteLocalServerImplCall10 call = reinterpret_cast<CuteLocalServerImplCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteLocalServerImplCall11 call = reinterpret_cast<CuteLocalServerImplCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteLocalServerImplCall12 call = reinterpret_cast<CuteLocalServerImplCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LocalServerImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15LocalServerImpl10metaObjectEv(
    const LocalServerImpl *self) {
  return self->metaObject();
}

//  void *LocalServerImpl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15LocalServerImpl11qt_metacastEPKc(
    LocalServerImpl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LocalServerImpl::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15LocalServerImpl11qt_metacallEN11QMetaObject4CallEiPPv(
    LocalServerImpl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LocalServerImpl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15LocalServerImpl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LocalServerImpl::tr(s, c, n));
}

//  LocalServerImpl::LocalServerImpl(QObject *parent)
extern "C" Q_DECL_EXPORT
LocalServerImpl *ritual_ZN15LocalServerImplC1EP7QObject(QObject *parent) {
  return new CuteLocalServerImpl(parent);
}

//  LocalServerImpl::~LocalServerImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN15LocalServerImplD1Ev(LocalServerImpl *self) {
  delete self;
}

//  bool LocalServerImpl::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15LocalServerImpl21hasPendingConnectionsEv(
    const LocalServerImpl *self) {
  return self->hasPendingConnections();
}

//  QtROServerIoDevice *LocalServerImpl::configureNewConnection()
extern "C" Q_DECL_EXPORT
QtROServerIoDevice *ritual_ZN15LocalServerImpl22configureNewConnectionEv(
    LocalServerImpl *self) {
  return self->configureNewConnection();
}

//  QUrl LocalServerImpl::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15LocalServerImpl7addressEv(const LocalServerImpl *self) {
  return new QUrl(self->address());
}

//  bool LocalServerImpl::listen(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15LocalServerImpl6listenERK4QUrl(
    LocalServerImpl *self,
    const QUrl *address) {
  return self->listen(*address);
}

//  QAbstractSocket::SocketError LocalServerImpl::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK15LocalServerImpl11serverErrorEv(
    const LocalServerImpl *self) {
  return self->serverError();
}

//  void LocalServerImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN15LocalServerImpl5closeEv(LocalServerImpl *self) {
  self->close();
}

//  void LocalServerImpl::setSocketOptions(QLocalServer::SocketOptions
//      options)
extern "C" Q_DECL_EXPORT
void ritual_ZN15LocalServerImpl16setSocketOptionsE6QFlagsIN12QLocalServer12SocketOptionEE(
    LocalServerImpl *self,
    int options) {
  self->setSocketOptions(
      QFlags<QLocalServer::SocketOption>::fromInt(options));
}

//  a Python function taken by a CuteLocalServerImpl, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LocalServerImpl(
    LocalServerImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteLocalServerImpl *>(self)->take(key, call);
}

//  bool LocalServerImpl::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK15LocalServerImpl21hasPendingConnectionsEv(
    const LocalServerImpl *self) {
  return self->LocalServerImpl::hasPendingConnections();
}

//  QtROServerIoDevice *LocalServerImpl::configureNewConnection()
extern "C" Q_DECL_EXPORT
QtROServerIoDevice *ritual_own_ZN15LocalServerImpl22configureNewConnectionEv(
    LocalServerImpl *self) {
  return self->LocalServerImpl::configureNewConnection();
}

//  QUrl LocalServerImpl::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK15LocalServerImpl7addressEv(
    const LocalServerImpl *self) {
  return new QUrl(self->LocalServerImpl::address());
}

//  bool LocalServerImpl::listen(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15LocalServerImpl6listenERK4QUrl(
    LocalServerImpl *self,
    const QUrl *address) {
  return self->LocalServerImpl::listen(*address);
}

//  QAbstractSocket::SocketError LocalServerImpl::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_own_ZNK15LocalServerImpl11serverErrorEv(
    const LocalServerImpl *self) {
  return self->LocalServerImpl::serverError();
}

//  void LocalServerImpl::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15LocalServerImpl5closeEv(LocalServerImpl *self) {
  self->LocalServerImpl::close();
}
