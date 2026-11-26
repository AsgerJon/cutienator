//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenuregistrarproxy_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QDBusMenuRegistrarInterface' is pasted in, cut from what the moc of Qt
//  6.12.0 writes for its header: Qt's library keeps it to itself; added are
//  2 rituals that lean on what moc writes for a class of the part Qt keeps
//  to itself, whose ritual file carries moc's output, drafted by a copy of
//  the generator that lets those names through. A copy of a meta-object is a
//  second one: 'qobject_cast' between it and Qt's own does not match. Kept
//  as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenuregistrarproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtCore/QString>
#include <QtDBus/QDBusObjectPath>
#include <QtDBus/QDBusReply>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtGui/private/qdbusmenuregistrarproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtGui__QDBusMenuRegistrarInterface.cpp, line 1, as moc:QDBusMenuRegistrarInterface
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t {};
} // unnamed namespace

template <> constexpr inline auto QDBusMenuRegistrarInterface::qt_create_metaobjectdata<qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QDBusMenuRegistrarInterface",
        "GetMenuForWindow",
        "QDBusPendingReply<QString,QDBusObjectPath>",
        "",
        "windowId",
        "QDBusReply<QString>",
        "QDBusObjectPath&",
        "menuObjectPath",
        "RegisterWindow",
        "QDBusPendingReply<>",
        "QDBusObjectPath",
        "UnregisterWindow"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'GetMenuForWindow'
        QtMocHelpers::SlotData<QDBusPendingReply<QString,QDBusObjectPath>(uint)>(1, 3, QMC::AccessPublic, 0x80000000 | 2, {{
            { QMetaType::UInt, 4 },
        }}),
        // Slot 'GetMenuForWindow'
        QtMocHelpers::SlotData<QDBusReply<QString>(uint, QDBusObjectPath &)>(1, 3, QMC::AccessPublic, 0x80000000 | 5, {{
            { QMetaType::UInt, 4 }, { 0x80000000 | 6, 7 },
        }}),
        // Slot 'RegisterWindow'
        QtMocHelpers::SlotData<QDBusPendingReply<>(uint, const QDBusObjectPath &)>(8, 3, QMC::AccessPublic, 0x80000000 | 9, {{
            { QMetaType::UInt, 4 }, { 0x80000000 | 10, 7 },
        }}),
        // Slot 'UnregisterWindow'
        QtMocHelpers::SlotData<QDBusPendingReply<>(uint)>(11, 3, QMC::AccessPublic, 0x80000000 | 9, {{
            { QMetaType::UInt, 4 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QDBusMenuRegistrarInterface, qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QDBusMenuRegistrarInterface::staticMetaObject = { {
    QMetaObject::SuperData::link<QDBusAbstractInterface::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t>.metaTypes,
    nullptr
} };

void QDBusMenuRegistrarInterface::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QDBusMenuRegistrarInterface *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: { QDBusPendingReply<QString,QDBusObjectPath> _r = _t->GetMenuForWindow((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<QString,QDBusObjectPath>*>(_a[0]) = std::move(_r); }  break;
        case 1: { QDBusReply<QString> _r = _t->GetMenuForWindow((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QDBusObjectPath&>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QDBusReply<QString>*>(_a[0]) = std::move(_r); }  break;
        case 2: { QDBusPendingReply<> _r = _t->RegisterWindow((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QDBusObjectPath>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        case 3: { QDBusPendingReply<> _r = _t->UnregisterWindow((*reinterpret_cast<std::add_pointer_t<uint>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 2:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 1:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusObjectPath >(); break;
            }
            break;
        }
    }
}

const QMetaObject *QDBusMenuRegistrarInterface::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QDBusMenuRegistrarInterface::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN27QDBusMenuRegistrarInterfaceE_t>.strings))
        return static_cast<void*>(this);
    return QDBusAbstractInterface::qt_metacast(_clname);
}

int QDBusMenuRegistrarInterface::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDBusAbstractInterface::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    return _id;
}
QT_WARNING_POP

//  from src/gui/platform/unix/dbusmenu/qdbusmenuregistrarproxy.cpp, line 20, as _ZN27QDBusMenuRegistrarInterfaceC1ERK7QStringS2_RK15QDBusConnectionP7QObject
inline QDBusMenuRegistrarInterface::QDBusMenuRegistrarInterface(const QString &service, const QString &path, const QDBusConnection &connection, QObject *parent)
    : QDBusAbstractInterface(service, path, staticInterfaceName(), connection, parent)
{
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenuregistrarproxy.cpp, line 25, as _ZN27QDBusMenuRegistrarInterfaceD1Ev
inline QDBusMenuRegistrarInterface::~QDBusMenuRegistrarInterface()
{
}
//  -----------------------------------------------------------------------

//  A QDBusMenuRegistrarInterface that Python can take functions over in. Every QDBusMenuRegistrarInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusMenuRegistrarInterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQDBusMenuRegistrarInterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuRegistrarInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuRegistrarInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuRegistrarInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuRegistrarInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuRegistrarInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusMenuRegistrarInterface : public QDBusMenuRegistrarInterface {
public:
  using QDBusMenuRegistrarInterface::QDBusMenuRegistrarInterface;
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
      CuteQDBusMenuRegistrarInterfaceCall0 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall0>(taken[0]);
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
      CuteQDBusMenuRegistrarInterfaceCall1 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall1>(taken[1]);
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
      CuteQDBusMenuRegistrarInterfaceCall2 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall2>(taken[2]);
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
      CuteQDBusMenuRegistrarInterfaceCall3 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall3>(taken[3]);
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
      CuteQDBusMenuRegistrarInterfaceCall4 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall4>(taken[4]);
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
      CuteQDBusMenuRegistrarInterfaceCall5 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall5>(taken[5]);
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
      CuteQDBusMenuRegistrarInterfaceCall6 call = reinterpret_cast<CuteQDBusMenuRegistrarInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusMenuRegistrarInterface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QDBusMenuRegistrarInterface10metaObjectEv(
    const QDBusMenuRegistrarInterface *self) {
  return self->metaObject();
}

//  void *QDBusMenuRegistrarInterface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QDBusMenuRegistrarInterface11qt_metacastEPKc(
    QDBusMenuRegistrarInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusMenuRegistrarInterface::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QDBusMenuRegistrarInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusMenuRegistrarInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDBusMenuRegistrarInterface::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QDBusMenuRegistrarInterface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusMenuRegistrarInterface::tr(s, c, n));
}

//  const char *QDBusMenuRegistrarInterface::staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN27QDBusMenuRegistrarInterface19staticInterfaceNameEv() {
  return QDBusMenuRegistrarInterface::staticInterfaceName();
}

//  QDBusMenuRegistrarInterface::QDBusMenuRegistrarInterface(const QString
//      &service, const QString &path, const QDBusConnection &connection,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusMenuRegistrarInterface *ritual_ZN27QDBusMenuRegistrarInterfaceC1ERK7QStringS2_RK15QDBusConnectionP7QObject(
    const QString *service,
    const QString *path,
    const QDBusConnection *connection,
    QObject *parent) {
  return new CuteQDBusMenuRegistrarInterface(
      *service,
      *path,
      *connection,
      parent);
}

//  QDBusMenuRegistrarInterface::~QDBusMenuRegistrarInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDBusMenuRegistrarInterfaceD1Ev(
    QDBusMenuRegistrarInterface *self) {
  delete self;
}

//  QDBusPendingReply<QString, QDBusObjectPath>
//      QDBusMenuRegistrarInterface::GetMenuForWindow(uint windowId)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QString, QDBusObjectPath> *ritual_ZN27QDBusMenuRegistrarInterface16GetMenuForWindowEj(
    QDBusMenuRegistrarInterface *self,
    uint windowId) {
  return new QDBusPendingReply<QString, QDBusObjectPath>(
      self->GetMenuForWindow(
          windowId));
}

//  QDBusReply<QString> QDBusMenuRegistrarInterface::GetMenuForWindow(uint
//      windowId, QDBusObjectPath &menuObjectPath)
extern "C" Q_DECL_EXPORT
QDBusReply<QString> *ritual_ZN27QDBusMenuRegistrarInterface16GetMenuForWindowEjR15QDBusObjectPath(
    QDBusMenuRegistrarInterface *self,
    uint windowId,
    QDBusObjectPath *menuObjectPath) {
  return new QDBusReply<QString>(
      self->GetMenuForWindow(
          windowId,
          *menuObjectPath));
}

//  QDBusPendingReply<> QDBusMenuRegistrarInterface::RegisterWindow(uint
//      windowId, const QDBusObjectPath &menuObjectPath)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN27QDBusMenuRegistrarInterface14RegisterWindowEjRK15QDBusObjectPath(
    QDBusMenuRegistrarInterface *self,
    uint windowId,
    const QDBusObjectPath *menuObjectPath) {
  return new QDBusPendingReply<>(
      self->RegisterWindow(
          windowId,
          *menuObjectPath));
}

//  QDBusPendingReply<> QDBusMenuRegistrarInterface::UnregisterWindow(uint
//      windowId)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN27QDBusMenuRegistrarInterface16UnregisterWindowEj(
    QDBusMenuRegistrarInterface *self,
    uint windowId) {
  return new QDBusPendingReply<>(self->UnregisterWindow(windowId));
}

//  a Python function taken by a CuteQDBusMenuRegistrarInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusMenuRegistrarInterface(
    QDBusMenuRegistrarInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusMenuRegistrarInterface *>(self)->take(key, call);
}

//  a QDBusPendingReply<QString, QDBusObjectPath> a ritual of
//      QDBusMenuRegistrarInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusMenuRegistrarInterface__QDBusPendingReply_QString_QDBusObjectPath(
    QDBusPendingReply<QString, QDBusObjectPath> *self) {
  delete self;
}

//  a QDBusReply<QString> a ritual of QDBusMenuRegistrarInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusMenuRegistrarInterface__QDBusReply_QString(
    QDBusReply<QString> *self) {
  delete self;
}

//  a QDBusPendingReply<> a ritual of QDBusMenuRegistrarInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusMenuRegistrarInterface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
