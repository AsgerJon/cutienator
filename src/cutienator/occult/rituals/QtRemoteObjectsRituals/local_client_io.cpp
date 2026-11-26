//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'LocalClientIo' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtRemoteObjects/private/qconnection_local_backend_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtRemoteObjects__LocalClientIo.cpp, line 1, as moc:LocalClientIo
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN13LocalClientIoE_t {};
} // unnamed namespace

template <> constexpr inline auto LocalClientIo::qt_create_metaobjectdata<qt_meta_tag_ZN13LocalClientIoE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "LocalClientIo",
        "onError",
        "",
        "QLocalSocket::LocalSocketError",
        "error",
        "onStateChanged",
        "QLocalSocket::LocalSocketState",
        "state"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'onError'
        QtMocHelpers::SlotData<void(QLocalSocket::LocalSocketError)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Slot 'onStateChanged'
        QtMocHelpers::SlotData<void(QLocalSocket::LocalSocketState)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<LocalClientIo, qt_meta_tag_ZN13LocalClientIoE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject LocalClientIo::staticMetaObject = { {
    QMetaObject::SuperData::link<QtROClientIoDevice::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13LocalClientIoE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13LocalClientIoE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN13LocalClientIoE_t>.metaTypes,
    nullptr
} };

void LocalClientIo::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<LocalClientIo *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->onError((*reinterpret_cast<std::add_pointer_t<QLocalSocket::LocalSocketError>>(_a[1]))); break;
        case 1: _t->onStateChanged((*reinterpret_cast<std::add_pointer_t<QLocalSocket::LocalSocketState>>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject *LocalClientIo::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *LocalClientIo::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN13LocalClientIoE_t>.strings))
        return static_cast<void*>(this);
    return QtROClientIoDevice::qt_metacast(_clname);
}

int LocalClientIo::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 85, as _ZN13LocalClientIo14onStateChangedEN12QLocalSocket16LocalSocketStateE
inline void LocalClientIo::onStateChanged(QLocalSocket::LocalSocketState state)
{
    if (state == QLocalSocket::ClosingState && !isClosing()) {
        m_socket->abort();
        emit shouldReconnect(this);
    }
    if (state == QLocalSocket::ConnectedState)
        initializeDataStream();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 43, as _ZN13LocalClientIo15connectToServerEv
#if defined(Q_OS_LINUX)
inline void LocalClientIo::connectToServer()
{
#ifdef Q_OS_ANDROID
    if (!m_socket->socketOptions().testFlag(QLocalSocket::AbstractNamespaceOption))
        qWarning() << "It is recommended to use 'localabstract' over 'local' on Android.";
#endif
    if (!isOpen())
        m_socket->connectToServer(url().path());
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 38, as _ZN13LocalClientIo22doDisconnectFromServerEv
inline void LocalClientIo::doDisconnectFromServer()
{
    m_socket->disconnectFromServer();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 28, as _ZN13LocalClientIo7doCloseEv
inline void LocalClientIo::doClose()
{
    if (m_socket->isOpen()) {
        connect(m_socket, &QLocalSocket::disconnected, this, &QObject::deleteLater);
        m_socket->disconnectFromServer();
    } else {
        this->deleteLater();
    }
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 59, as _ZN13LocalClientIo7onErrorEN12QLocalSocket16LocalSocketErrorE
#if defined(Q_OS_LINUX)
inline void LocalClientIo::onError(QLocalSocket::LocalSocketError error)
{
    qCDebug(QT_REMOTEOBJECT) << "onError" << error << m_socket->serverName();

    switch (error) {
    case QLocalSocket::ServerNotFoundError:
    case QLocalSocket::UnknownSocketError:
    case QLocalSocket::PeerClosedError:
        //Host not there, wait and try again
        emit shouldReconnect(this);
        break;
    case QLocalSocket::ConnectionError:
    case QLocalSocket::ConnectionRefusedError:
        //... TODO error reporting
#ifdef Q_OS_UNIX
        emit shouldReconnect(this);
#endif
        break;
    case QLocalSocket::SocketAccessError:
        emit setError(QRemoteObjectNode::SocketAccessError);
        break;
    default:
        break;
    }
}
#endif  // defined(Q_OS_LINUX)

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 18, as _ZN13LocalClientIoD0Ev
inline LocalClientIo::~LocalClientIo()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 23, as _ZNK13LocalClientIo10connectionEv
inline QIODevice *LocalClientIo::connection() const
{
    return m_socket;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 53, as _ZNK13LocalClientIo6isOpenEv
inline bool LocalClientIo::isOpen() const
{
    return !isClosing() && (m_socket->state() == QLocalSocket::ConnectedState
                            || m_socket->state() == QLocalSocket::ConnectingState);
}

//  from ../qtremoteobjects/src/remoteobjects/qtremoteobjectglobal.cpp, line 13, as _Z15QT_REMOTEOBJECTv
inline const QLoggingCategory &QT_REMOTEOBJECT()
{
    static const QLoggingCategory category("qt.remoteobjects", QtWarningMsg);
    return category;
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 9, as _ZN13LocalClientIoC1EP7QObject
inline LocalClientIo::LocalClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QLocalSocket(this))
{
    connect(m_socket, &QLocalSocket::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket, &QLocalSocket::errorOccurred, this, &LocalClientIo::onError);
    connect(m_socket, &QLocalSocket::stateChanged, this, &LocalClientIo::onStateChanged);
}
//  -----------------------------------------------------------------------

//  Only a class built on LocalClientIo may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnLocalClientIo : LocalClientIo {
  using LocalClientIo::doClose;
  using LocalClientIo::doDisconnectFromServer;
};

//  A LocalClientIo that Python can take functions over in. Every LocalClientIo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteLocalClientIoCall0)(const void *, int *);
typedef void (*CuteLocalClientIoCall1)(const void *, int *);
typedef bool (*CuteLocalClientIoCall2)(const void *, int *);
typedef void (*CuteLocalClientIoCall3)(const void *, int *);
typedef void (*CuteLocalClientIoCall4)(const void *, int *);
typedef QString * (*CuteLocalClientIoCall5)(const void *, int *);
typedef void (*CuteLocalClientIoCall6)(const void *, const QByteArray *, int *);
typedef void (*CuteLocalClientIoCall7)(const void *, const QByteArray *, qint64, int *);
typedef void (*CuteLocalClientIoCall8)(const void *, int *);
typedef qint64 (*CuteLocalClientIoCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLocalClientIoCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteLocalClientIoCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalClientIoCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalClientIoCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalClientIoCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalClientIoCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteLocalClientIoCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteLocalClientIo : public LocalClientIo {
public:
  using LocalClientIo::LocalClientIo;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10connectionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QtROClientIoDevice15connectToServerEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase6isOpenEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase7doCloseEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QtROClientIoDevice22doDisconnectFromServerEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase10deviceTypeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArray")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5writeERK10QByteArrayx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QtROIoDeviceBase5closeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QtROIoDeviceBase14bytesAvailableEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QIODevice *LocalClientIo::connection() const
  QIODevice *connection() const override {
    if (taken[0]) {
      int handled = 0;
      CuteLocalClientIoCall0 call = reinterpret_cast<CuteLocalClientIoCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return LocalClientIo::connection();
  }

  //  void LocalClientIo::connectToServer()
  void connectToServer() override {
    if (taken[1]) {
      int handled = 0;
      CuteLocalClientIoCall1 call = reinterpret_cast<CuteLocalClientIoCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    LocalClientIo::connectToServer();
  }

  //  bool LocalClientIo::isOpen() const
  bool isOpen() const override {
    if (taken[2]) {
      int handled = 0;
      CuteLocalClientIoCall2 call = reinterpret_cast<CuteLocalClientIoCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return LocalClientIo::isOpen();
  }

  //  void LocalClientIo::doClose()
  void doClose() override {
    if (taken[3]) {
      int handled = 0;
      CuteLocalClientIoCall3 call = reinterpret_cast<CuteLocalClientIoCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    LocalClientIo::doClose();
  }

  //  void LocalClientIo::doDisconnectFromServer()
  void doDisconnectFromServer() override {
    if (taken[4]) {
      int handled = 0;
      CuteLocalClientIoCall4 call = reinterpret_cast<CuteLocalClientIoCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    LocalClientIo::doDisconnectFromServer();
  }

  //  QString QtROClientIoDevice::deviceType() const
  QString deviceType() const override {
    if (taken[5]) {
      int handled = 0;
      CuteLocalClientIoCall5 call = reinterpret_cast<CuteLocalClientIoCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QtROClientIoDevice::deviceType();
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data)
  void write(const QByteArray &data) override {
    if (taken[6]) {
      int handled = 0;
      CuteLocalClientIoCall6 call = reinterpret_cast<CuteLocalClientIoCall6>(taken[6]);
      call(this, &data, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data);
  }

  //  void QtROIoDeviceBase::write(const QByteArray &data, qint64 a1)
  void write(const QByteArray &data, qint64 a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteLocalClientIoCall7 call = reinterpret_cast<CuteLocalClientIoCall7>(taken[7]);
      call(this, &data, a1, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::write(data, a1);
  }

  //  void QtROIoDeviceBase::close()
  void close() override {
    if (taken[8]) {
      int handled = 0;
      CuteLocalClientIoCall8 call = reinterpret_cast<CuteLocalClientIoCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QtROIoDeviceBase::close();
  }

  //  qint64 QtROIoDeviceBase::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[9]) {
      int handled = 0;
      CuteLocalClientIoCall9 call = reinterpret_cast<CuteLocalClientIoCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QtROIoDeviceBase::bytesAvailable();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteLocalClientIoCall10 call = reinterpret_cast<CuteLocalClientIoCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteLocalClientIoCall11 call = reinterpret_cast<CuteLocalClientIoCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteLocalClientIoCall12 call = reinterpret_cast<CuteLocalClientIoCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteLocalClientIoCall13 call = reinterpret_cast<CuteLocalClientIoCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteLocalClientIoCall14 call = reinterpret_cast<CuteLocalClientIoCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteLocalClientIoCall15 call = reinterpret_cast<CuteLocalClientIoCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteLocalClientIoCall16 call = reinterpret_cast<CuteLocalClientIoCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *LocalClientIo::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13LocalClientIo10metaObjectEv(
    const LocalClientIo *self) {
  return self->metaObject();
}

//  void *LocalClientIo::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13LocalClientIo11qt_metacastEPKc(
    LocalClientIo *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LocalClientIo::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13LocalClientIo11qt_metacallEN11QMetaObject4CallEiPPv(
    LocalClientIo *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if defined(Q_OS_LINUX)
//  QString LocalClientIo::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13LocalClientIo2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LocalClientIo::tr(s, c, n));
}
#endif  // defined(Q_OS_LINUX)

#if defined(Q_OS_LINUX)
//  LocalClientIo::LocalClientIo(QObject *parent)
extern "C" Q_DECL_EXPORT
LocalClientIo *ritual_ZN13LocalClientIoC1EP7QObject(QObject *parent) {
  return new CuteLocalClientIo(parent);
}
#endif  // defined(Q_OS_LINUX)

//  LocalClientIo::~LocalClientIo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalClientIoD1Ev(LocalClientIo *self) {
  delete self;
}

//  QIODevice *LocalClientIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK13LocalClientIo10connectionEv(
    const LocalClientIo *self) {
  return self->connection();
}

//  void LocalClientIo::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalClientIo15connectToServerEv(LocalClientIo *self) {
  self->connectToServer();
}

//  bool LocalClientIo::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13LocalClientIo6isOpenEv(const LocalClientIo *self) {
  return self->isOpen();
}

//  void LocalClientIo::onError(QLocalSocket::LocalSocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalClientIo7onErrorEN12QLocalSocket16LocalSocketErrorE(
    LocalClientIo *self,
    QLocalSocket::LocalSocketError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "LocalClientIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onError(QLocalSocket::LocalSocketError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onError(QLocalSocket::LocalSocketError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void LocalClientIo::onStateChanged(QLocalSocket::LocalSocketState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalClientIo14onStateChangedEN12QLocalSocket16LocalSocketStateE(
    LocalClientIo *self,
    QLocalSocket::LocalSocketState state) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "LocalClientIo")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "onStateChanged(QLocalSocket::LocalSocketState)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "onStateChanged(QLocalSocket::LocalSocketState)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&state)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void LocalClientIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalClientIo7doCloseEv(LocalClientIo *self) {
  self->doClose();
}

//  void LocalClientIo::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13LocalClientIo22doDisconnectFromServerEv(
    LocalClientIo *self) {
  self->doDisconnectFromServer();
}

//  a Python function taken by a CuteLocalClientIo, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_LocalClientIo(
    LocalClientIo *self,
    const char *key,
    void *call) {
  return static_cast<CuteLocalClientIo *>(self)->take(key, call);
}

//  QIODevice *LocalClientIo::connection() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZNK13LocalClientIo10connectionEv(
    const LocalClientIo *self) {
  return self->LocalClientIo::connection();
}

#if defined(Q_OS_LINUX)
//  void LocalClientIo::connectToServer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LocalClientIo15connectToServerEv(LocalClientIo *self) {
  self->LocalClientIo::connectToServer();
}
#endif  // defined(Q_OS_LINUX)

//  bool LocalClientIo::isOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13LocalClientIo6isOpenEv(const LocalClientIo *self) {
  return self->LocalClientIo::isOpen();
}

//  void LocalClientIo::doClose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LocalClientIo7doCloseEv(LocalClientIo *self) {
  static_cast<OwnLocalClientIo *>(self)->OwnLocalClientIo::doClose();
}

//  void LocalClientIo::doDisconnectFromServer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13LocalClientIo22doDisconnectFromServerEv(
    LocalClientIo *self) {
  static_cast<OwnLocalClientIo *>(self)->OwnLocalClientIo::doDisconnectFromServer();
}
