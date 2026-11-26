//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/adapter1_bluez5_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtBluetoothPrivate::OrgBluezAdapter1Interface' is pasted in, cut from
//  what the moc of Qt 6.12.0 writes for its header: Qt's library keeps it to
//  itself; added are 2 rituals that lean on what moc writes for a class of
//  the part Qt keeps to itself, whose ritual file carries moc's output,
//  drafted by a copy of the generator that lets those names through. A copy
//  of a meta-object is a second one: 'qobject_cast' between it and Qt's own
//  does not match. Kept as it is when the generator runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/adapter1_bluez5_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusconnection.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtDBus/QDBusObjectPath>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QVariant>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtBluetooth/private/adapter1_bluez5_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtBluetooth__QtBluetoothPrivate_OrgBluezAdapter1Interface.cpp, line 1, as moc:QtBluetoothPrivate::OrgBluezAdapter1Interface
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t {};
} // unnamed namespace

template <> constexpr inline auto QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_create_metaobjectdata<qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtBluetoothPrivate::OrgBluezAdapter1Interface",
        "RemoveDevice",
        "QDBusPendingReply<>",
        "",
        "QDBusObjectPath",
        "device",
        "SetDiscoveryFilter",
        "QVariantMap",
        "properties",
        "StartDiscovery",
        "StopDiscovery",
        "Address",
        "Alias",
        "Class",
        "Discoverable",
        "DiscoverableTimeout",
        "Discovering",
        "Modalias",
        "Name",
        "Pairable",
        "PairableTimeout",
        "Powered",
        "UUIDs"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'RemoveDevice'
        QtMocHelpers::SlotData<QDBusPendingReply<>(const QDBusObjectPath &)>(1, 3, QMC::AccessPublic, 0x80000000 | 2, {{
            { 0x80000000 | 4, 5 },
        }}),
        // Slot 'SetDiscoveryFilter'
        QtMocHelpers::SlotData<QDBusPendingReply<>(const QVariantMap &)>(6, 3, QMC::AccessPublic, 0x80000000 | 2, {{
            { 0x80000000 | 7, 8 },
        }}),
        // Slot 'StartDiscovery'
        QtMocHelpers::SlotData<QDBusPendingReply<>()>(9, 3, QMC::AccessPublic, 0x80000000 | 2),
        // Slot 'StopDiscovery'
        QtMocHelpers::SlotData<QDBusPendingReply<>()>(10, 3, QMC::AccessPublic, 0x80000000 | 2),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'Address'
        QtMocHelpers::PropertyData<QString>(11, QMetaType::QString, QMC::DefaultPropertyFlags),
        // property 'Alias'
        QtMocHelpers::PropertyData<QString>(12, QMetaType::QString, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
        // property 'Class'
        QtMocHelpers::PropertyData<uint>(13, QMetaType::UInt, QMC::DefaultPropertyFlags),
        // property 'Discoverable'
        QtMocHelpers::PropertyData<bool>(14, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
        // property 'DiscoverableTimeout'
        QtMocHelpers::PropertyData<uint>(15, QMetaType::UInt, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
        // property 'Discovering'
        QtMocHelpers::PropertyData<bool>(16, QMetaType::Bool, QMC::DefaultPropertyFlags),
        // property 'Modalias'
        QtMocHelpers::PropertyData<QString>(17, QMetaType::QString, QMC::DefaultPropertyFlags),
        // property 'Name'
        QtMocHelpers::PropertyData<QString>(18, QMetaType::QString, QMC::DefaultPropertyFlags),
        // property 'Pairable'
        QtMocHelpers::PropertyData<bool>(19, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
        // property 'PairableTimeout'
        QtMocHelpers::PropertyData<uint>(20, QMetaType::UInt, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
        // property 'Powered'
        QtMocHelpers::PropertyData<bool>(21, QMetaType::Bool, QMC::DefaultPropertyFlags | QMC::Writable | QMC::StdCppSet),
        // property 'UUIDs'
        QtMocHelpers::PropertyData<QStringList>(22, QMetaType::QStringList, QMC::DefaultPropertyFlags),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<OrgBluezAdapter1Interface, qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtBluetoothPrivate::OrgBluezAdapter1Interface::staticMetaObject = { {
    QMetaObject::SuperData::link<QDBusAbstractInterface::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t>.metaTypes,
    nullptr
} };

void QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<OrgBluezAdapter1Interface *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: { QDBusPendingReply<> _r = _t->RemoveDevice((*reinterpret_cast<std::add_pointer_t<QDBusObjectPath>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        case 1: { QDBusPendingReply<> _r = _t->SetDiscoveryFilter((*reinterpret_cast<std::add_pointer_t<QVariantMap>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        case 2: { QDBusPendingReply<> _r = _t->StartDiscovery();
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        case 3: { QDBusPendingReply<> _r = _t->StopDiscovery();
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
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
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusObjectPath >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QString*>(_v) = _t->address(); break;
        case 1: *reinterpret_cast<QString*>(_v) = _t->alias(); break;
        case 2: *reinterpret_cast<uint*>(_v) = _t->classProperty(); break;
        case 3: *reinterpret_cast<bool*>(_v) = _t->discoverable(); break;
        case 4: *reinterpret_cast<uint*>(_v) = _t->discoverableTimeout(); break;
        case 5: *reinterpret_cast<bool*>(_v) = _t->discovering(); break;
        case 6: *reinterpret_cast<QString*>(_v) = _t->modalias(); break;
        case 7: *reinterpret_cast<QString*>(_v) = _t->name(); break;
        case 8: *reinterpret_cast<bool*>(_v) = _t->pairable(); break;
        case 9: *reinterpret_cast<uint*>(_v) = _t->pairableTimeout(); break;
        case 10: *reinterpret_cast<bool*>(_v) = _t->powered(); break;
        case 11: *reinterpret_cast<QStringList*>(_v) = _t->uUIDs(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setAlias(*reinterpret_cast<QString*>(_v)); break;
        case 3: _t->setDiscoverable(*reinterpret_cast<bool*>(_v)); break;
        case 4: _t->setDiscoverableTimeout(*reinterpret_cast<uint*>(_v)); break;
        case 8: _t->setPairable(*reinterpret_cast<bool*>(_v)); break;
        case 9: _t->setPairableTimeout(*reinterpret_cast<uint*>(_v)); break;
        case 10: _t->setPowered(*reinterpret_cast<bool*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QtBluetoothPrivate::OrgBluezAdapter1Interface::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceE_t>.strings))
        return static_cast<void*>(this);
    return QDBusAbstractInterface::qt_metacast(_clname);
}

int QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 12;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtconnectivity/src/bluetooth/bluez/adapter1_bluez5.cpp, line 20, as _ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceC1ERK7QStringS3_RK15QDBusConnectionP7QObject
namespace QtBluetoothPrivate {
inline OrgBluezAdapter1Interface::OrgBluezAdapter1Interface(const QString &service, const QString &path, const QDBusConnection &connection, QObject *parent)
    : QDBusAbstractInterface(service, path, staticInterfaceName(), connection, parent)
{
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/adapter1_bluez5.cpp, line 25, as _ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgBluezAdapter1Interface::~OrgBluezAdapter1Interface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezAdapter1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezAdapter1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezAdapter1Interface : public QtBluetoothPrivate::OrgBluezAdapter1Interface {
public:
  using QtBluetoothPrivate::OrgBluezAdapter1Interface::OrgBluezAdapter1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezAdapter1Interface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezAdapter1Interface::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::tr(const char *s,
//      const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtBluetoothPrivate::OrgBluezAdapter1Interface::tr(
          s,
          c,
          n));
}

//  const char
//      *QtBluetoothPrivate::OrgBluezAdapter1Interface::staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezAdapter1Interface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgBluezAdapter1Interface::OrgBluezAdapter1Interface(
//      const QString &service, const QString &path, const QDBusConnection
//      &connection, QObject *parent)
extern "C" Q_DECL_EXPORT
QtBluetoothPrivate::OrgBluezAdapter1Interface *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceC1ERK7QStringS3_RK15QDBusConnectionP7QObject(
    const QString *service,
    const QString *path,
    const QDBusConnection *connection,
    QObject *parent) {
  return new CuteQtBluetoothPrivate_OrgBluezAdapter1Interface(
      *service,
      *path,
      *connection,
      parent);
}

//  QtBluetoothPrivate::OrgBluezAdapter1Interface::~OrgBluezAdapter1Interface
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1InterfaceD1Ev(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  delete self;
}

//  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::address() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface7addressEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QString(self->address());
}

//  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::alias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface5aliasEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QString(self->alias());
}

//  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setAlias(const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface8setAliasERK7QString(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    const QString *value) {
  self->setAlias(*value);
}

//  uint QtBluetoothPrivate::OrgBluezAdapter1Interface::classProperty() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface13classPropertyEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->classProperty();
}

//  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::discoverable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface12discoverableEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->discoverable();
}

//  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setDiscoverable(bool
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface15setDiscoverableEb(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    bool value) {
  self->setDiscoverable(value);
}

//  uint QtBluetoothPrivate::OrgBluezAdapter1Interface::discoverableTimeout()
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface19discoverableTimeoutEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->discoverableTimeout();
}

//  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setDiscoverableTimeou
//      t(uint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface22setDiscoverableTimeoutEj(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    uint value) {
  self->setDiscoverableTimeout(value);
}

//  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::discovering() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface11discoveringEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->discovering();
}

//  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::modalias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface8modaliasEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QString(self->modalias());
}

//  QString QtBluetoothPrivate::OrgBluezAdapter1Interface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface4nameEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QString(self->name());
}

//  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::pairable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface8pairableEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->pairable();
}

//  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setPairable(bool
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface11setPairableEb(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    bool value) {
  self->setPairable(value);
}

//  uint QtBluetoothPrivate::OrgBluezAdapter1Interface::pairableTimeout()
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface15pairableTimeoutEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->pairableTimeout();
}

//  void
//      QtBluetoothPrivate::OrgBluezAdapter1Interface::setPairableTimeout(uin
//      t value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface18setPairableTimeoutEj(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    uint value) {
  self->setPairableTimeout(value);
}

//  bool QtBluetoothPrivate::OrgBluezAdapter1Interface::powered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface7poweredEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return self->powered();
}

//  void QtBluetoothPrivate::OrgBluezAdapter1Interface::setPowered(bool
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface10setPoweredEb(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    bool value) {
  self->setPowered(value);
}

//  QStringList QtBluetoothPrivate::OrgBluezAdapter1Interface::uUIDs() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate25OrgBluezAdapter1Interface5uUIDsEv(
    const QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QList<QString>(self->uUIDs());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezAdapter1Interface::RemoveDevice(const
//      QDBusObjectPath &device)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface12RemoveDeviceERK15QDBusObjectPath(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    const QDBusObjectPath *device) {
  return new QDBusPendingReply<>(self->RemoveDevice(*device));
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezAdapter1Interface::SetDiscoveryFilter(con
//      st QVariantMap &properties)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface18SetDiscoveryFilterERK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    const QMap<QString, QVariant> *properties) {
  return new QDBusPendingReply<>(self->SetDiscoveryFilter(*properties));
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezAdapter1Interface::StartDiscovery()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface14StartDiscoveryEv(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QDBusPendingReply<>(self->StartDiscovery());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezAdapter1Interface::StopDiscovery()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate25OrgBluezAdapter1Interface13StopDiscoveryEv(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self) {
  return new QDBusPendingReply<>(self->StopDiscovery());
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezAdapter1Interface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezAdapter1Interface(
    QtBluetoothPrivate::OrgBluezAdapter1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezAdapter1Interface *>(self)->take(key, call);
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgBluezAdapter1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezAdapter1Interface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
