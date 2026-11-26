//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/leadvertisingmanager1_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface' is pasted
//  in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/leadvertisingmanager1_p.h>
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
#include <QtBluetooth/private/leadvertisingmanager1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtBluetooth__QtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface.cpp, line 1, as moc:QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t {};
} // unnamed namespace

template <> constexpr inline auto QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_create_metaobjectdata<qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface",
        "RegisterAdvertisement",
        "QDBusPendingReply<>",
        "",
        "QDBusObjectPath",
        "advertisement",
        "QVariantMap",
        "options",
        "UnregisterAdvertisement",
        "ActiveInstances",
        "SupportedIncludes",
        "SupportedInstances"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'RegisterAdvertisement'
        QtMocHelpers::SlotData<QDBusPendingReply<>(const QDBusObjectPath &, const QVariantMap &)>(1, 3, QMC::AccessPublic, 0x80000000 | 2, {{
            { 0x80000000 | 4, 5 }, { 0x80000000 | 6, 7 },
        }}),
        // Slot 'UnregisterAdvertisement'
        QtMocHelpers::SlotData<QDBusPendingReply<>(const QDBusObjectPath &)>(8, 3, QMC::AccessPublic, 0x80000000 | 2, {{
            { 0x80000000 | 4, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'ActiveInstances'
        QtMocHelpers::PropertyData<uchar>(9, QMetaType::UChar, QMC::DefaultPropertyFlags),
        // property 'SupportedIncludes'
        QtMocHelpers::PropertyData<QStringList>(10, QMetaType::QStringList, QMC::DefaultPropertyFlags),
        // property 'SupportedInstances'
        QtMocHelpers::PropertyData<uchar>(11, QMetaType::UChar, QMC::DefaultPropertyFlags),
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<OrgBluezLEAdvertisingManager1Interface, qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::staticMetaObject = { {
    QMetaObject::SuperData::link<QDBusAbstractInterface::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t>.metaTypes,
    nullptr
} };

void QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<OrgBluezLEAdvertisingManager1Interface *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: { QDBusPendingReply<> _r = _t->RegisterAdvertisement((*reinterpret_cast<std::add_pointer_t<QDBusObjectPath>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QVariantMap>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QDBusPendingReply<>*>(_a[0]) = std::move(_r); }  break;
        case 1: { QDBusPendingReply<> _r = _t->UnregisterAdvertisement((*reinterpret_cast<std::add_pointer_t<QDBusObjectPath>>(_a[1])));
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
        case 1:
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
        case 0: *reinterpret_cast<uchar*>(_v) = _t->activeInstances(); break;
        case 1: *reinterpret_cast<QStringList*>(_v) = _t->supportedIncludes(); break;
        case 2: *reinterpret_cast<uchar*>(_v) = _t->supportedInstances(); break;
        default: break;
        }
    }
}

const QMetaObject *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceE_t>.strings))
        return static_cast<void*>(this);
    return QDBusAbstractInterface::qt_metacast(_clname);
}

int QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDBusAbstractInterface::qt_metacall(_c, _id, _a);
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
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisingmanager1.cpp, line 20, as _ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceC1ERK7QStringS3_RK15QDBusConnectionP7QObject
namespace QtBluetoothPrivate {
inline OrgBluezLEAdvertisingManager1Interface::OrgBluezLEAdvertisingManager1Interface(const QString &service, const QString &path, const QDBusConnection &connection, QObject *parent)
    : QDBusAbstractInterface(service, path, staticInterfaceName(), connection, parent)
{
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/leadvertisingmanager1.cpp, line 25, as _ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgBluezLEAdvertisingManager1Interface::~OrgBluezLEAdvertisingManager1Interface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface : public QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface {
public:
  using QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::OrgBluezLEAdvertisingManager1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::metaObje
//      ct() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_meta
//      cast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::qt_metaca
//      ll(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString
//      QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::tr(const
//      char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::tr(
          s,
          c,
          n));
}

//  const char *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::s
//      taticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::OrgBluezLEAdv
//      ertisingManager1Interface(const QString &service, const QString
//      &path, const QDBusConnection &connection, QObject *parent)
extern "C" Q_DECL_EXPORT
QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceC1ERK7QStringS3_RK15QDBusConnectionP7QObject(
    const QString *service,
    const QString *path,
    const QDBusConnection *connection,
    QObject *parent) {
  return new CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface(
      *service,
      *path,
      *connection,
      parent);
}

//  QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::~OrgBluezLEAd
//      vertisingManager1Interface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1InterfaceD1Ev(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  delete self;
}

//  uchar QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::activeI
//      nstances() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface15activeInstancesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return self->activeInstances();
}

//  QStringList QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::s
//      upportedIncludes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface17supportedIncludesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return new QList<QString>(self->supportedIncludes());
}

//  uchar QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::support
//      edInstances() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface18supportedInstancesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return self->supportedInstances();
}

//  QDBusPendingReply<> QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Inte
//      rface::RegisterAdvertisement(const QDBusObjectPath &advertisement,
//      const QVariantMap &options)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface21RegisterAdvertisementERK15QDBusObjectPathRK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self,
    const QDBusObjectPath *advertisement,
    const QMap<QString, QVariant> *options) {
  return new QDBusPendingReply<>(
      self->RegisterAdvertisement(
          *advertisement,
          *options));
}

//  QDBusPendingReply<> QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Inte
//      rface::UnregisterAdvertisement(const QDBusObjectPath &advertisement)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface23UnregisterAdvertisementERK15QDBusObjectPath(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self,
    const QDBusObjectPath *advertisement) {
  return new QDBusPendingReply<>(
      self->UnregisterAdvertisement(
          *advertisement));
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface *>(self)->take(key, call);
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
