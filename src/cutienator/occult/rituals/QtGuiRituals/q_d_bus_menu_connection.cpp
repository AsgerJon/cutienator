//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenuconnection_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QDBusMenuConnection' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenuconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbuserror.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGui/qtgui-config.h>
#include <QDBusMessage>
#include <QDBusInterface>
#include <QDBusServiceWatcher>
#include <QDBusConnectionInterface>
#include <QtCore/QDebug>
#include <QtCore/QCoreApplication>
#ifndef QT_NO_SYSTEMTRAYICON
#include <QtGui/private/qdbustrayicon_p.h>
#endif
#include <QtGui/private/qdbusmenuconnection_p.h>
#include <QtGui/private/qdbusmenuadaptor_p.h>
#include <QtGui/private/qdbusplatformmenu_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/platform/unix/dbusmenu/qdbusmenuconnection.cpp, line 25, as local:qdbusmenuconnection.cpp:StatusNotifierWatcherService
const QString StatusNotifierWatcherService = "org.kde.StatusNotifierWatcher"_L1;

//  from src/gui/platform/unix/dbusmenu/qdbusmenuconnection.cpp, line 27, as local:qdbusmenuconnection.cpp:StatusNotifierItemPath
const QString StatusNotifierItemPath = "/StatusNotifierItem"_L1;

//  from src/gui/platform/unix/dbusmenu/qdbusmenuconnection.cpp, line 28, as local:qdbusmenuconnection.cpp:MenuBarPath
const QString MenuBarPath = "/MenuBar"_L1;

//  from QtGui__QDBusMenuConnection.cpp, line 1, as moc:QDBusMenuConnection
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN19QDBusMenuConnectionE_t {};
} // unnamed namespace

template <> constexpr inline auto QDBusMenuConnection::qt_create_metaobjectdata<qt_meta_tag_ZN19QDBusMenuConnectionE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QDBusMenuConnection",
        "trayIconRegistered",
        "",
        "dbusError",
        "QDBusError",
        "error"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'trayIconRegistered'
        QtMocHelpers::SignalData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'dbusError'
        QtMocHelpers::SlotData<void(const QDBusError &)>(3, 2, QMC::AccessPrivate, QMetaType::Void, {{
            { 0x80000000 | 4, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QDBusMenuConnection, qt_meta_tag_ZN19QDBusMenuConnectionE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QDBusMenuConnection::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QDBusMenuConnectionE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QDBusMenuConnectionE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN19QDBusMenuConnectionE_t>.metaTypes,
    nullptr
} };

void QDBusMenuConnection::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QDBusMenuConnection *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->trayIconRegistered(); break;
        case 1: _t->dbusError((*reinterpret_cast<std::add_pointer_t<QDBusError>>(_a[1]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QDBusMenuConnection::*)()>(_a, &QDBusMenuConnection::trayIconRegistered, 0))
            return;
    }
}

const QMetaObject *QDBusMenuConnection::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QDBusMenuConnection::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN19QDBusMenuConnectionE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QDBusMenuConnection::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QDBusMenuConnection::trayIconRegistered()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}
QT_WARNING_POP

//  from src/gui/platform/unix/dbusmenu/qdbusmenuconnection.cpp, line 59, as _ZN19QDBusMenuConnection9dbusErrorERK10QDBusError
inline void QDBusMenuConnection::dbusError(const QDBusError &error)
{
    qWarning() << "QDBusTrayIcon encountered a D-Bus error:" << error;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuconnection.cpp, line 36, as _ZN19QDBusMenuConnectionC1EP7QObjectRK7QString
inline QDBusMenuConnection::QDBusMenuConnection(QObject *parent, const QString &serviceName)
    : QObject(parent)
    , m_serviceName(serviceName)
    , m_connection(serviceName.isNull() ? QDBusConnection::sessionBus()
                                        : QDBusConnection::connectToBus(QDBusConnection::SessionBus, serviceName))
    , m_dbusWatcher(new QDBusServiceWatcher(StatusNotifierWatcherService, m_connection, QDBusServiceWatcher::WatchForRegistration, this))
    , m_watcherRegistered(false)
{
#ifndef QT_NO_SYSTEMTRAYICON
    // Start monitoring if any known tray-related services are registered.
    if (m_connection.interface()->isServiceRegistered(StatusNotifierWatcherService))
        m_watcherRegistered = true;
    else
        qCDebug(qLcMenu) << "failed to find service" << StatusNotifierWatcherService;
#endif
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 13, as _Z7qLcMenuv
inline const QLoggingCategory &qLcMenu()
{
    static const QLoggingCategory category("qt.qpa.menu");
    return category;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuconnection.cpp, line 53, as _ZN19QDBusMenuConnectionD1Ev
inline QDBusMenuConnection::~QDBusMenuConnection()
{
  if (!m_serviceName.isEmpty() && m_connection.isConnected())
      QDBusConnection::disconnectFromBus(m_serviceName);
}
//  -----------------------------------------------------------------------

//  A QDBusMenuConnection that Python can take functions over in. Every QDBusMenuConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuConnectionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuConnectionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuConnectionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuConnectionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuConnectionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuConnectionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuConnectionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusMenuConnection : public QDBusMenuConnection {
public:
  using QDBusMenuConnection::QDBusMenuConnection;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall0 call = reinterpret_cast<CuteQDBusMenuConnectionCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall1 call = reinterpret_cast<CuteQDBusMenuConnectionCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall2 call = reinterpret_cast<CuteQDBusMenuConnectionCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall3 call = reinterpret_cast<CuteQDBusMenuConnectionCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall4 call = reinterpret_cast<CuteQDBusMenuConnectionCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall5 call = reinterpret_cast<CuteQDBusMenuConnectionCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDBusMenuConnectionCall6 call = reinterpret_cast<CuteQDBusMenuConnectionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusMenuConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QDBusMenuConnection10metaObjectEv(
    const QDBusMenuConnection *self) {
  return self->metaObject();
}

//  void *QDBusMenuConnection::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QDBusMenuConnection11qt_metacastEPKc(
    QDBusMenuConnection *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusMenuConnection::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QDBusMenuConnection11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusMenuConnection *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDBusMenuConnection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QDBusMenuConnection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusMenuConnection::tr(s, c, n));
}

//  QDBusMenuConnection::~QDBusMenuConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMenuConnectionD1Ev(QDBusMenuConnection *self) {
  delete self;
}

//  QDBusConnection QDBusMenuConnection::connection() const
extern "C" Q_DECL_EXPORT
QDBusConnection *ritual_ZNK19QDBusMenuConnection10connectionEv(
    const QDBusMenuConnection *self) {
  return new QDBusConnection(self->connection());
}

//  QDBusServiceWatcher *QDBusMenuConnection::dbusWatcher() const
extern "C" Q_DECL_EXPORT
QDBusServiceWatcher *ritual_ZNK19QDBusMenuConnection11dbusWatcherEv(
    const QDBusMenuConnection *self) {
  return self->dbusWatcher();
}

//  bool QDBusMenuConnection::isWatcherRegistered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDBusMenuConnection19isWatcherRegisteredEv(
    const QDBusMenuConnection *self) {
  return self->isWatcherRegistered();
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  void QDBusMenuConnection::trayIconRegistered()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMenuConnection18trayIconRegisteredEv(
    QDBusMenuConnection *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusMenuConnection")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "trayIconRegistered()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "trayIconRegistered()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  void QDBusMenuConnection::dbusError(const QDBusError &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDBusMenuConnection9dbusErrorERK10QDBusError(
    QDBusMenuConnection *self,
    const QDBusError *error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusMenuConnection")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "dbusError(const QDBusError &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "dbusError(const QDBusError &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQDBusMenuConnection, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusMenuConnection(
    QDBusMenuConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusMenuConnection *>(self)->take(key, call);
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
