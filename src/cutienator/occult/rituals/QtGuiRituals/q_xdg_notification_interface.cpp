//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qxdgnotificationproxy_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QXdgNotificationInterface' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(systemtrayicon) && 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qxdgnotificationproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtCore/QStringList>
#include <QtCore/QString>
#include <QtDBus/QDBusReply>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QVariant>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qxdgnotificationproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGui__QXdgNotificationInterface.cpp, line 1, as moc:QXdgNotificationInterface
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN25QXdgNotificationInterfaceE_t {};
} // unnamed namespace

template <> constexpr inline auto QXdgNotificationInterface::qt_create_metaobjectdata<qt_meta_tag_ZN25QXdgNotificationInterfaceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QXdgNotificationInterface",
        "ActionInvoked",
        "",
        "id",
        "action_key",
        "NotificationClosed",
        "reason",
        "closeNotification",
        "QDBusPendingReply<>",
        "getCapabilities",
        "QDBusPendingReply<QStringList>",
        "getServerInformation",
        "QDBusPendingReply<QString,QString,QString,QString>",
        "QDBusReply<QString>",
        "QString&",
        "vendor",
        "version",
        "specVersion",
        "notify",
        "QDBusPendingReply<uint>",
        "appName",
        "replacesId",
        "appIcon",
        "summary",
        "body",
        "actions",
        "QVariantMap",
        "hints",
        "timeout"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'ActionInvoked'
        QtMocHelpers::SignalData<void(uint, const QString &)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::UInt, 3 }, { QMetaType::QString, 4 },
        }}),
        // Signal 'NotificationClosed'
        QtMocHelpers::SignalData<void(uint, uint)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::UInt, 3 }, { QMetaType::UInt, 6 },
        }}),
        // Slot 'closeNotification'
        QtMocHelpers::SlotData<QDBusPendingReply<>(uint)>(7, 2, QMC::AccessPublic, 0x80000000 | 8, {{
            { QMetaType::UInt, 3 },
        }}),
        // Slot 'getCapabilities'
        QtMocHelpers::SlotData<QDBusPendingReply<QStringList>()>(9, 2, QMC::AccessPublic, 0x80000000 | 10),
        // Slot 'getServerInformation'
        QtMocHelpers::SlotData<QDBusPendingReply<QString,QString,QString,QString>()>(11, 2, QMC::AccessPublic, 0x80000000 | 12),
        // Slot 'getServerInformation'
        QtMocHelpers::SlotData<QDBusReply<QString>(QString &, QString &, QString &)>(11, 2, QMC::AccessPublic, 0x80000000 | 13, {{
            { 0x80000000 | 14, 15 }, { 0x80000000 | 14, 16 }, { 0x80000000 | 14, 17 },
        }}),
        // Slot 'notify'
        QtMocHelpers::SlotData<QDBusPendingReply<uint>(const QString &, uint, const QString &, const QString &, const QString &, const QStringList &, const QVariantMap &, int)>(18, 2, QMC::AccessPublic, 0x80000000 | 19, {{
            { QMetaType::QString, 20 }, { QMetaType::UInt, 21 }, { QMetaType::QString, 22 }, { QMetaType::QString, 23 },
            { QMetaType::QString, 24 }, { QMetaType::QStringList, 25 }, { 0x80000000 | 26, 27 }, { QMetaType::Int, 28 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QXdgNotificationInterface, qt_meta_tag_ZN25QXdgNotificationInterfaceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QXdgNotificationInterface::staticMetaObject = { {
    QMetaObject::SuperData::link<QDBusAbstractInterface::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QXdgNotificationInterfaceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QXdgNotificationInterfaceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN25QXdgNotificationInterfaceE_t>.metaTypes,
    nullptr
} };

void QXdgNotificationInterface::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QXdgNotificationInterface *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->ActionInvoked((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2]))); break;
        case 1: _t->NotificationClosed((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<uint>>(_a[2]))); break;
        case 2: { QDBusPendingReply<> _r = _t->closeNotification((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        case 3: { QDBusPendingReply<QStringList> _r = _t->getCapabilities();
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<QStringList>*>(_a[0]) = std::move(_r); }  break;
        case 4: { QDBusPendingReply<QString,QString,QString,QString> _r = _t->getServerInformation();
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<QString,QString,QString,QString>*>(_a[0]) = std::move(_r); }  break;
        case 5: { QDBusReply<QString> _r = _t->getServerInformation((*reinterpret_cast<std::add_pointer_t<QString&>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString&>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QString&>>(_a[3])));
            if (_a[0]) *reinterpret_cast<QDBusReply<QString>*>(_a[0]) = std::move(_r); }  break;
        case 6: { QDBusPendingReply<uint> _r = _t->notify((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<uint>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[3])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[4])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[5])),(*reinterpret_cast<std::add_pointer_t<QStringList>>(_a[6])),(*reinterpret_cast<std::add_pointer_t<QVariantMap>>(_a[7])),(*reinterpret_cast<std::add_pointer_t<int>>(_a[8])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<uint>*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QXdgNotificationInterface::*)(uint , const QString & )>(_a, &QXdgNotificationInterface::ActionInvoked, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QXdgNotificationInterface::*)(uint , uint )>(_a, &QXdgNotificationInterface::NotificationClosed, 1))
            return;
    }
}

const QMetaObject *QXdgNotificationInterface::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QXdgNotificationInterface::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN25QXdgNotificationInterfaceE_t>.strings))
        return static_cast<void*>(this);
    return QDBusAbstractInterface::qt_metacast(_clname);
}

int QXdgNotificationInterface::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDBusAbstractInterface::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 7;
    }
    return _id;
}

// SIGNAL 0
void QXdgNotificationInterface::ActionInvoked(uint _t1, const QString & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1, _t2);
}

// SIGNAL 1
void QXdgNotificationInterface::NotificationClosed(uint _t1, uint _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1, _t2);
}
QT_WARNING_POP

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 42, as _Z7qLcTrayv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline const QLoggingCategory &qLcTray()
{
    static const QLoggingCategory category("qt.qpa.tray");
    return category;
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qxdgnotificationproxy.cpp, line 9, as _ZN25QXdgNotificationInterfaceC1ERK7QStringS2_RK15QDBusConnectionP7QObject
inline QXdgNotificationInterface::QXdgNotificationInterface(const QString &service, const QString &path, const QDBusConnection &connection, QObject *parent)
    : QDBusAbstractInterface(service, path, staticInterfaceName(), connection, parent)
{
}

//  from src/gui/platform/unix/dbustray/qxdgnotificationproxy.cpp, line 14, as _ZN25QXdgNotificationInterfaceD1Ev
inline QXdgNotificationInterface::~QXdgNotificationInterface()
{
}
//  -----------------------------------------------------------------------

//  A QXdgNotificationInterface that Python can take functions over in. Every QXdgNotificationInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQXdgNotificationInterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQXdgNotificationInterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXdgNotificationInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQXdgNotificationInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXdgNotificationInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXdgNotificationInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQXdgNotificationInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQXdgNotificationInterface : public QXdgNotificationInterface {
public:
  using QXdgNotificationInterface::QXdgNotificationInterface;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
  //  void QDBusAbstractInterface::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[0]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall0 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall0>(taken[0]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QDBusAbstractInterface::connectNotify(signal);
  }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
  //  void QDBusAbstractInterface::disconnectNotify(const QMetaMethod
  //      &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[1]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall1 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall1>(taken[1]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QDBusAbstractInterface::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall2 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall3 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall4 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall5 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQXdgNotificationInterfaceCall6 call = reinterpret_cast<CuteQXdgNotificationInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QXdgNotificationInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QXdgNotificationInterface10metaObjectEv(
    const QXdgNotificationInterface *self) {
  return self->metaObject();
}

//  void *QXdgNotificationInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QXdgNotificationInterface11qt_metacastEPKc(
    QXdgNotificationInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QXdgNotificationInterface::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QXdgNotificationInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QXdgNotificationInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QString QXdgNotificationInterface::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QXdgNotificationInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QXdgNotificationInterface::tr(s, c, n));
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  const char *QXdgNotificationInterface::staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN25QXdgNotificationInterface19staticInterfaceNameEv() {
  return QXdgNotificationInterface::staticInterfaceName();
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QXdgNotificationInterface::QXdgNotificationInterface(const QString
//      &service, const QString &path, const QDBusConnection &connection,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QXdgNotificationInterface *ritual_ZN25QXdgNotificationInterfaceC1ERK7QStringS2_RK15QDBusConnectionP7QObject(
    const QString *service,
    const QString *path,
    const QDBusConnection *connection,
    QObject *parent) {
  return new CuteQXdgNotificationInterface(
      *service,
      *path,
      *connection,
      parent);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  QXdgNotificationInterface::~QXdgNotificationInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QXdgNotificationInterfaceD1Ev(
    QXdgNotificationInterface *self) {
  delete self;
}

//  QDBusPendingReply<> QXdgNotificationInterface::closeNotification(uint id)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN25QXdgNotificationInterface17closeNotificationEj(
    QXdgNotificationInterface *self,
    uint id) {
  return new QDBusPendingReply<>(self->closeNotification(id));
}

//  QDBusPendingReply<QStringList>
//      QXdgNotificationInterface::getCapabilities()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QStringList> *ritual_ZN25QXdgNotificationInterface15getCapabilitiesEv(
    QXdgNotificationInterface *self) {
  return new QDBusPendingReply<QStringList>(self->getCapabilities());
}

//  QDBusPendingReply<QString, QString, QString, QString>
//      QXdgNotificationInterface::getServerInformation()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QString, QString, QString, QString> *ritual_ZN25QXdgNotificationInterface20getServerInformationEv(
    QXdgNotificationInterface *self) {
  return new QDBusPendingReply<QString, QString, QString, QString>(
      self->getServerInformation());
}

//  QDBusReply<QString>
//      QXdgNotificationInterface::getServerInformation(QString &vendor,
//      QString &version, QString &specVersion)
extern "C" Q_DECL_EXPORT
QDBusReply<QString> *ritual_ZN25QXdgNotificationInterface20getServerInformationER7QStringS1_S1_(
    QXdgNotificationInterface *self,
    QString *vendor,
    QString *version,
    QString *specVersion) {
  return new QDBusReply<QString>(
      self->getServerInformation(
          *vendor,
          *version,
          *specVersion));
}

#if !defined(QT_NO_SYSTEMTRAYICON)
//  QDBusPendingReply<uint> QXdgNotificationInterface::notify(const QString
//      &appName, uint replacesId, const QString &appIcon, const QString
//      &summary, const QString &body, const QStringList &actions, const
//      QVariantMap &hints, int timeout)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<uint> *ritual_ZN25QXdgNotificationInterface6notifyERK7QStringjS2_S2_S2_RK5QListIS0_ERK4QMapIS0_8QVariantEi(
    QXdgNotificationInterface *self,
    const QString *appName,
    uint replacesId,
    const QString *appIcon,
    const QString *summary,
    const QString *body,
    const QList<QString> *actions,
    const QMap<QString, QVariant> *hints,
    int timeout) {
  return new QDBusPendingReply<uint>(
      self->notify(
          *appName,
          replacesId,
          *appIcon,
          *summary,
          *body,
          *actions,
          *hints,
          timeout));
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  void QXdgNotificationInterface::ActionInvoked(uint id, const QString
//      &action_key)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QXdgNotificationInterface13ActionInvokedEjRK7QString(
    QXdgNotificationInterface *self,
    uint id,
    const QString *action_key) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QXdgNotificationInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "ActionInvoked(uint,const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "ActionInvoked(uint,const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(action_key)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QXdgNotificationInterface::NotificationClosed(uint id, uint reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QXdgNotificationInterface18NotificationClosedEjj(
    QXdgNotificationInterface *self,
    uint id,
    uint reason) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QXdgNotificationInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "NotificationClosed(uint,uint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "NotificationClosed(uint,uint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(&reason)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQXdgNotificationInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXdgNotificationInterface(
    QXdgNotificationInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXdgNotificationInterface *>(self)->take(key, call);
}

//  a QDBusPendingReply<> a ritual of QXdgNotificationInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXdgNotificationInterface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

//  a QDBusPendingReply<QStringList> a ritual of QXdgNotificationInterface
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXdgNotificationInterface__QDBusPendingReply_QStringList(
    QDBusPendingReply<QStringList> *self) {
  delete self;
}

//  a QDBusPendingReply<QString, QString, QString, QString> a ritual of
//      QXdgNotificationInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXdgNotificationInterface__QDBusPendingReply_QString_QString_QString_QString(
    QDBusPendingReply<QString, QString, QString, QString> *self) {
  delete self;
}

//  a QDBusReply<QString> a ritual of QXdgNotificationInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXdgNotificationInterface__QDBusReply_QString(
    QDBusReply<QString> *self) {
  delete self;
}

//  a QDBusPendingReply<uint> a ritual of QXdgNotificationInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QXdgNotificationInterface__QDBusPendingReply_uint(
    QDBusPendingReply<uint> *self) {
  delete self;
}

#endif  // QT_CONFIG(systemtrayicon) && 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
