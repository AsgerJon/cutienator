//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/gattcharacteristic1adaptor_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor' is pasted in,
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
#include <QtBluetooth/6.12.0/QtBluetooth/private/gattcharacteristic1adaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtDBus/qdbusmessage.h>
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
#include <QtBluetooth/private/gattcharacteristic1adaptor_p.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtBluetooth__QtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor.cpp, line 1, as moc:QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t {};
} // unnamed namespace

template <> constexpr inline auto QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_create_metaobjectdata<qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor",
        "D-Bus Interface",
        "org.bluez.GattCharacteristic1",
        "D-Bus Introspection",
        "  <interface name=\"org.bluez.GattCharacteristic1\">\n    <method "
        "name=\"ReadValue\">\n      <arg direction=\"in\" type=\"a{sv}\" na"
        "me=\"options\"/>\n      <annotation value=\"QVariantMap\" name=\"o"
        "rg.qtproject.QtDBus.QtTypeName.In0\"/>\n      <arg direction=\"out"
        "\" type=\"ay\" name=\"value\"/>\n    </method>\n    <method name=\""
        "WriteValue\">\n      <arg direction=\"in\" type=\"ay\" name=\"valu"
        "e\"/>\n      <arg direction=\"in\" type=\"a{sv}\" name=\"options\""
        "/>\n      <annotation value=\"QVariantMap\" name=\"org.qtproject.Q"
        "tDBus.QtTypeName.In1\"/>\n    </method>\n    <method name=\"StartN"
        "otify\"/>\n    <method name=\"StopNotify\"/>\n    <property access"
        "=\"read\" type=\"s\" name=\"UUID\"/>\n    <property access=\"read\""
        " type=\"o\" name=\"Service\"/>\n    <property access=\"read\" type"
        "=\"ay\" name=\"Value\"/>\n    <property access=\"read\" type=\"b\""
        " name=\"Notifying\"/>\n    <property access=\"read\" type=\"as\" n"
        "ame=\"Flags\"/>\n  </interface>\n",
        "ReadValue",
        "",
        "QVariantMap",
        "options",
        "QDBusMessage",
        "msg",
        "StartNotify",
        "StopNotify",
        "WriteValue",
        "value",
        "Flags",
        "Notifying",
        "Service",
        "QDBusObjectPath",
        "UUID",
        "Value"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'ReadValue'
        QtMocHelpers::SlotData<QByteArray(const QVariantMap &, const QDBusMessage &)>(5, 6, QMC::AccessPublic, QMetaType::QByteArray, {{
            { 0x80000000 | 7, 8 }, { 0x80000000 | 9, 10 },
        }}),
        // Slot 'StartNotify'
        QtMocHelpers::SlotData<void()>(11, 6, QMC::AccessPublic, QMetaType::Void),
        // Slot 'StopNotify'
        QtMocHelpers::SlotData<void()>(12, 6, QMC::AccessPublic, QMetaType::Void),
        // Slot 'WriteValue'
        QtMocHelpers::SlotData<void(const QByteArray &, const QVariantMap &, const QDBusMessage &)>(13, 6, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::QByteArray, 14 }, { 0x80000000 | 7, 8 }, { 0x80000000 | 9, 10 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'Flags'
        QtMocHelpers::PropertyData<QStringList>(15, QMetaType::QStringList, QMC::DefaultPropertyFlags),
        // property 'Notifying'
        QtMocHelpers::PropertyData<bool>(16, QMetaType::Bool, QMC::DefaultPropertyFlags),
        // property 'Service'
        QtMocHelpers::PropertyData<QDBusObjectPath>(17, 0x80000000 | 18, QMC::DefaultPropertyFlags | QMC::EnumOrFlag),
        // property 'UUID'
        QtMocHelpers::PropertyData<QString>(19, QMetaType::QString, QMC::DefaultPropertyFlags),
        // property 'Value'
        QtMocHelpers::PropertyData<QByteArray>(20, QMetaType::QByteArray, QMC::DefaultPropertyFlags),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
    });
    return QtMocHelpers::metaObjectData<OrgBluezGattCharacteristic1Adaptor, qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT const QMetaObject QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::staticMetaObject = { {
    QMetaObject::SuperData::link<QDBusAbstractAdaptor::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t>.metaTypes,
    nullptr
} };

void QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<OrgBluezGattCharacteristic1Adaptor *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: { QByteArray _r = _t->ReadValue((*reinterpret_cast<std::add_pointer_t<QVariantMap>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QDBusMessage>>(_a[2])));
            if (_a[0]) *reinterpret_cast<QByteArray*>(_a[0]) = std::move(_r); }  break;
        case 1: _t->StartNotify(); break;
        case 2: _t->StopNotify(); break;
        case 3: _t->WriteValue((*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QVariantMap>>(_a[2])),(*reinterpret_cast<std::add_pointer_t<QDBusMessage>>(_a[3]))); break;
        default: ;
        }
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        switch (_id) {
        default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
        case 0:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 1:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusMessage >(); break;
            }
            break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 2:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QDBusMessage >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::RegisterPropertyMetaType) {
        switch (_id) {
        default: *reinterpret_cast<int*>(_a[0]) = -1; break;
        case 2:
            *reinterpret_cast<int*>(_a[0]) = qRegisterMetaType< QDBusObjectPath >(); break;
        }
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<QStringList*>(_v) = _t->flags(); break;
        case 1: *reinterpret_cast<bool*>(_v) = _t->notifying(); break;
        case 2: *reinterpret_cast<QDBusObjectPath*>(_v) = _t->service(); break;
        case 3: *reinterpret_cast<QString*>(_v) = _t->uUID(); break;
        case 4: *reinterpret_cast<QByteArray*>(_v) = _t->value(); break;
        default: break;
        }
    }
}

const QMetaObject *QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorE_t>.strings))
        return static_cast<void*>(this);
    return QDBusAbstractAdaptor::qt_metacast(_clname);
}

int QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
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
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 90, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10StopNotifyEv
namespace QtBluetoothPrivate {
inline void OrgBluezGattCharacteristic1Adaptor::StopNotify()
{
    // handle method call org.bluez.GattCharacteristic1.StopNotify
    QMetaObject::invokeMethod(parent(), "StopNotify");
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 96, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10WriteValueERK10QByteArrayRK4QMapI7QString8QVariantERK12QDBusMessage
namespace QtBluetoothPrivate {
inline void OrgBluezGattCharacteristic1Adaptor::WriteValue(const QByteArray &value,
                                                    const QVariantMap &options,
                                                    const QDBusMessage& msg)
{
    // handle method call org.bluez.GattCharacteristic1.WriteValue
    QString error;
    QMetaObject::invokeMethod(parent(), "WriteValue", Q_RETURN_ARG(QString, error),
                              Q_ARG(QByteArray, value), Q_ARG(QVariantMap, options));

    if (!error.isEmpty()) {
        // Reply with error if needed
        auto reply = msg.createErrorReply(error, {});
        QDBusConnection::systemBus().send(reply);
    }
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 84, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11StartNotifyEv
namespace QtBluetoothPrivate {
inline void OrgBluezGattCharacteristic1Adaptor::StartNotify()
{
    // handle method call org.bluez.GattCharacteristic1.StartNotify
    QMetaObject::invokeMethod(parent(), "StartNotify");
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 33, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorD0Ev
namespace QtBluetoothPrivate {
inline OrgBluezGattCharacteristic1Adaptor::~OrgBluezGattCharacteristic1Adaptor()
{
    // destructor
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 26, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorC1EP7QObject
namespace QtBluetoothPrivate {
inline OrgBluezGattCharacteristic1Adaptor::OrgBluezGattCharacteristic1Adaptor(QObject *parent)
    : QDBusAbstractAdaptor(parent)
{
    // constructor
    setAutoRelaySignals(true);
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 38, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5flagsEv
namespace QtBluetoothPrivate {
inline QStringList OrgBluezGattCharacteristic1Adaptor::flags() const
{
    // get the value of property Flags
    return qvariant_cast< QStringList >(parent()->property("Flags"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 44, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9notifyingEv
namespace QtBluetoothPrivate {
inline bool OrgBluezGattCharacteristic1Adaptor::notifying() const
{
    // get the value of property Notifying
    return qvariant_cast< bool >(parent()->property("Notifying"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 50, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor7serviceEv
namespace QtBluetoothPrivate {
inline QDBusObjectPath OrgBluezGattCharacteristic1Adaptor::service() const
{
    // get the value of property Service
    return qvariant_cast< QDBusObjectPath >(parent()->property("Service"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 56, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor4uUIDEv
namespace QtBluetoothPrivate {
inline QString OrgBluezGattCharacteristic1Adaptor::uUID() const
{
    // get the value of property UUID
    return qvariant_cast< QString >(parent()->property("UUID"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 62, as _ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5valueEv
namespace QtBluetoothPrivate {
inline QByteArray OrgBluezGattCharacteristic1Adaptor::value() const
{
    // get the value of property Value
    return qvariant_cast< QByteArray >(parent()->property("Value"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattcharacteristic1adaptor.cpp, line 68, as _ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9ReadValueERK4QMapI7QString8QVariantERK12QDBusMessage
namespace QtBluetoothPrivate {
inline QByteArray OrgBluezGattCharacteristic1Adaptor::ReadValue(const QVariantMap &options,
                                                         const QDBusMessage& msg)
{
    // handle method call org.bluez.GattCharacteristic1.ReadValue
    QByteArray value;
    QString error;
    QMetaObject::invokeMethod(parent(), "ReadValue", Q_RETURN_ARG(QByteArray, value),
                              Q_ARG(QVariantMap, options), Q_ARG(QString&, error));
    if (!error.isEmpty()) {
        // Reply with error if needed
        auto reply = msg.createErrorReply(error, {});
        QDBusConnection::systemBus().send(reply);
    }
    return value;
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor : public QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor {
public:
  using QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::OrgBluezGattCharacteristic1Adaptor;
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1AdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_metacast
//      (const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::qt_metacall(Q
//      MetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::tr(const
//      char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::tr(
          s,
          c,
          n));
}

//  QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::OrgBluezGattChara
//      cteristic1Adaptor(QObject *parent)
extern "C" Q_DECL_EXPORT
QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorC1EP7QObject(
    QObject *parent) {
  return new CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor(
      parent);
}

//  QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::~OrgBluezGattChar
//      acteristic1Adaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1AdaptorD1Ev(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  delete self;
}

//  QStringList
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::flags() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5flagsEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QList<QString>(self->flags());
}

//  bool QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::notifying()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9notifyingEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return self->notifying();
}

//  QDBusObjectPath
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::service()
//      const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor7serviceEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QDBusObjectPath(self->service());
}

//  QString QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::uUID()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor4uUIDEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QString(self->uUID());
}

//  QByteArray
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor5valueEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  return new QByteArray(self->value());
}

//  QByteArray
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::ReadValue(con
//      st QVariantMap &options, const QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor9ReadValueERK4QMapI7QString8QVariantERK12QDBusMessage(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const QMap<QString, QVariant> *options,
    const QDBusMessage *msg) {
  return new QByteArray(self->ReadValue(*options, *msg));
}

//  void
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::StartNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor11StartNotifyEv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "StartNotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "StartNotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::StopNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10StopNotifyEv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "StopNotify()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "StopNotify()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor::WriteValue(co
//      nst QByteArray &value, const QVariantMap &options, const QDBusMessage
//      &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate34OrgBluezGattCharacteristic1Adaptor10WriteValueERK10QByteArrayRK4QMapI7QString8QVariantERK12QDBusMessage(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const QByteArray *value,
    const QMap<QString, QVariant> *options,
    const QDBusMessage *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "WriteValue(const QByteArray &,const QVariantMap &,const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "WriteValue(const QByteArray &,const QVariantMap &,const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(value)),
      const_cast<void *>(static_cast<const void *>(options)),
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Adaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Adaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(bluez)
