//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/propertiesadaptor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 2 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/propertiesadaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtBluetooth/private/propertiesadaptor_p.h>
#include <QtCore/QMetaObject>
#include <QtCore/QByteArray>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QStringList>
#include <QtCore/QVariant>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtBluetooth__QtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor.cpp, line 1, as moc:QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t {};
} // unnamed namespace

template <> constexpr inline auto QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_create_metaobjectdata<qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor",
        "D-Bus Interface",
        "org.freedesktop.DBus.Properties",
        "D-Bus Introspection",
        "  <interface name=\"org.freedesktop.DBus.Properties\">\n    <metho"
        "d name=\"Get\">\n      <arg direction=\"in\" type=\"s\" name=\"int"
        "erface\"/>\n      <arg direction=\"in\" type=\"s\" name=\"name\"/>"
        "\n      <arg direction=\"out\" type=\"v\" name=\"value\"/>\n    </"
        "method>\n    <method name=\"Set\">\n      <arg direction=\"in\" ty"
        "pe=\"s\" name=\"interface\"/>\n      <arg direction=\"in\" type=\""
        "s\" name=\"name\"/>\n      <arg direction=\"in\" type=\"v\" name=\""
        "value\"/>\n    </method>\n    <method name=\"GetAll\">\n      <arg"
        " direction=\"in\" type=\"s\" name=\"interface\"/>\n      <arg dire"
        "ction=\"out\" type=\"a{sv}\" name=\"properties\"/>\n      <annotat"
        "ion value=\"QVariantMap\" name=\"org.qtproject.QtDBus.QtTypeName.O"
        "ut0\"/>\n    </method>\n    <signal name=\"PropertiesChanged\">\n "
        "     <arg type=\"s\" name=\"interface\"/>\n      <arg type=\"a{sv}"
        "\" name=\"changed_properties\"/>\n      <annotation value=\"QVaria"
        "ntMap\" name=\"org.qtproject.QtDBus.QtTypeName.Out1\"/>\n      <ar"
        "g type=\"as\" name=\"invalidated_properties\"/>\n    </signal>\n  "
        "</interface>\n",
        "PropertiesChanged",
        "",
        "interface",
        "QVariantMap",
        "changed_properties",
        "invalidated_properties",
        "Get",
        "QDBusVariant",
        "name",
        "GetAll",
        "Set",
        "value"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'PropertiesChanged'
        QtMocHelpers::SignalData<void(const QString &, const QVariantMap &, const QStringList &)>(5, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 7 }, { 0x80000000 | 8, 9 }, { QMetaType::QStringList, 10 },
        }}),
        // Slot 'Get'
        QtMocHelpers::SlotData<QDBusVariant(const QString &, const QString &)>(11, 6, QMC::AccessPublic, 0x80000000 | 12, {{
            { QMetaType::QString, 7 }, { QMetaType::QString, 13 },
        }}),
        // Slot 'GetAll'
        QtMocHelpers::SlotData<QVariantMap(const QString &)>(14, 6, QMC::AccessPublic, 0x80000000 | 8, {{
            { QMetaType::QString, 7 },
        }}),
        // Slot 'Set'
        QtMocHelpers::SlotData<void(const QString &, const QString &, const QDBusVariant &)>(15, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QString, 7 }, { QMetaType::QString, 13 }, { 0x80000000 | 12, 16 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<OrgFreedesktopDBusPropertiesAdaptor, qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::staticMetaObject = { {
    QMetaObject::SuperData::link<QDBusAbstractAdaptor::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t>.metaTypes,
    nullptr
} };

void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<OrgFreedesktopDBusPropertiesAdaptor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->PropertiesChanged((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QVariantMap>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QStringList>>(_a[3]))); break;
        case 1: { QDBusVariant _r = _t->Get((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QDBusVariant*>(_a[0]) = std::move(_r); }  break;
        case 2: { QVariantMap _r = _t->GetAll((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])));
            if (_a[0]) *reinterpret_cast<QVariantMap*>(_a[0]) = std::move(_r); }  break;
        case 3: _t->Set((*reinterpret_cast<std::add_pointer_t<QString>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QString>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QDBusVariant>>(_a[3]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 2:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusVariant >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (OrgFreedesktopDBusPropertiesAdaptor::*)(const QString & , const QVariantMap & , const QStringList & )>(_a, &OrgFreedesktopDBusPropertiesAdaptor::PropertiesChanged, 0))
            return;
    }
}

const QMetaObject *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorE_t>.strings))
        return static_cast<void*>(this);
    return QDBusAbstractAdaptor::qt_metacast(_clname);
}

int QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QDBusAbstractAdaptor::qt_metacall(_c, _id, _a);
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

// SIGNAL 0
void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::PropertiesChanged(const QString & _t1, const QVariantMap & _t2, const QStringList & _t3)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1, _t2, _t3);
}
QT_WARNING_POP

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 54, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3SetERK7QStringS3_RK12QDBusVariant
namespace QtBluetoothPrivate {
inline void OrgFreedesktopDBusPropertiesAdaptor::Set(const QString &interface, const QString &name, const QDBusVariant &value)
{
    // handle method call org.freedesktop.DBus.Properties.Set
    QMetaObject::invokeMethod(parent(), "Set", Q_ARG(QString, interface), Q_ARG(QString, name), Q_ARG(QDBusVariant, value));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 33, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorD0Ev
namespace QtBluetoothPrivate {
inline OrgFreedesktopDBusPropertiesAdaptor::~OrgFreedesktopDBusPropertiesAdaptor()
{
    // destructor
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 26, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorC1EP7QObject
namespace QtBluetoothPrivate {
inline OrgFreedesktopDBusPropertiesAdaptor::OrgFreedesktopDBusPropertiesAdaptor(QObject *parent)
    : QDBusAbstractAdaptor(parent)
{
    // constructor
    setAutoRelaySignals(true);
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 38, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3GetERK7QStringS3_
namespace QtBluetoothPrivate {
inline QDBusVariant OrgFreedesktopDBusPropertiesAdaptor::Get(const QString &interface, const QString &name)
{
    // handle method call org.freedesktop.DBus.Properties.Get
    QDBusVariant value;
    QMetaObject::invokeMethod(parent(), "Get", Q_RETURN_ARG(QDBusVariant, value), Q_ARG(QString, interface), Q_ARG(QString, name));
    return value;
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/propertiesadaptor.cpp, line 46, as _ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor6GetAllERK7QString
namespace QtBluetoothPrivate {
inline QVariantMap OrgFreedesktopDBusPropertiesAdaptor::GetAll(const QString &interface)
{
    // handle method call org.freedesktop.DBus.Properties.GetAll
    QVariantMap properties;
    QMetaObject::invokeMethod(parent(), "GetAll", Q_RETURN_ARG(QVariantMap, properties), Q_ARG(QString, interface));
    return properties;
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor : public QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor {
public:
  using QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::OrgFreedesktopDBusPropertiesAdaptor;
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::metaObject(
//      ) const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacas
//      t(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::qt_metacall(
//      QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::tr(const
//      char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::tr(
          s,
          c,
          n));
}

//  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::OrgFreedesktopDB
//      usPropertiesAdaptor(QObject *parent)
extern "C" Q_DECL_EXPORT
QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorC1EP7QObject(
    QObject *parent) {
  return new CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor(
      parent);
}

//  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::~OrgFreedesktopD
//      BusPropertiesAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptorD1Ev(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self) {
  delete self;
}

//  QDBusVariant
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Get(const
//      QString &interface, const QString &name)
extern "C" Q_DECL_EXPORT
QDBusVariant *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3GetERK7QStringS3_(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface,
    const QString *name) {
  return new QDBusVariant(self->Get(*interface, *name));
}

//  QVariantMap
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::GetAll(const
//      QString &interface)
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor6GetAllERK7QString(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface) {
  return new QMap<QString, QVariant>(self->GetAll(*interface));
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::Set(const
//      QString &interface, const QString &name, const QDBusVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor3SetERK7QStringS3_RK12QDBusVariant(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface,
    const QString *name,
    const QDBusVariant *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "Set(const QString &,const QString &,const QDBusVariant &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "Set(const QString &,const QString &,const QDBusVariant &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(interface)),
      const_cast<void *>(static_cast<const void *>(name)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor::PropertiesC
//      hanged(const QString &interface, const QVariantMap
//      &changed_properties, const QStringList &invalidated_properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate35OrgFreedesktopDBusPropertiesAdaptor17PropertiesChangedERK7QStringRK4QMapIS1_8QVariantERK5QListIS1_E(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const QString *interface,
    const QMap<QString, QVariant> *changed_properties,
    const QList<QString> *invalidated_properties) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "PropertiesChanged(const QString &,const QVariantMap &,const QStringList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "PropertiesChanged(const QString &,const QVariantMap &,const QStringList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(interface)),
      const_cast<void *>(static_cast<const void *>(changed_properties)),
      const_cast<void *>(static_cast<const void *>(invalidated_properties)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesAdaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(bluez)
