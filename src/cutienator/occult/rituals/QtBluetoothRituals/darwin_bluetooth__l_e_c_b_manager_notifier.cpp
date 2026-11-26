//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'DarwinBluetooth::LECBManagerNotifier' is pasted in, cut from what the
//  moc of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 1 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtBluetooth__DarwinBluetooth_LECBManagerNotifier.cpp, line 1, as moc:DarwinBluetooth::LECBManagerNotifier
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t {};
} // unnamed namespace

template <> constexpr inline auto DarwinBluetooth::LECBManagerNotifier::qt_create_metaobjectdata<qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "DarwinBluetooth::LECBManagerNotifier",
        "deviceDiscovered",
        "",
        "QBluetoothDeviceInfo",
        "deviceInfo",
        "discoveryFinished",
        "connected",
        "disconnected",
        "mtuChanged",
        "newValue",
        "serviceDiscoveryFinished",
        "serviceDetailsDiscoveryFinished",
        "QSharedPointer<QLowEnergyServicePrivate>",
        "service",
        "characteristicRead",
        "QLowEnergyHandle",
        "charHandle",
        "value",
        "characteristicWritten",
        "characteristicUpdated",
        "descriptorRead",
        "descHandle",
        "descriptorWritten",
        "notificationEnabled",
        "enabled",
        "servicesWereModified",
        "rssiUpdated",
        "LEnotSupported",
        "CBManagerError",
        "QBluetoothDeviceDiscoveryAgent::Error",
        "error",
        "QLowEnergyController::Error",
        "QBluetoothUuid",
        "serviceUuid",
        "QLowEnergyService::ServiceError"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'deviceDiscovered'
        QtMocHelpers::SignalData<void(QBluetoothDeviceInfo)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Signal 'discoveryFinished'
        QtMocHelpers::SignalData<void()>(5, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'connected'
        QtMocHelpers::SignalData<void()>(6, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'disconnected'
        QtMocHelpers::SignalData<void()>(7, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'mtuChanged'
        QtMocHelpers::SignalData<void(int)>(8, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Int, 9 },
        }}),
        // Signal 'serviceDiscoveryFinished'
        QtMocHelpers::SignalData<void()>(10, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'serviceDetailsDiscoveryFinished'
        QtMocHelpers::SignalData<void(QSharedPointer<QLowEnergyServicePrivate>)>(11, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 12, 13 },
        }}),
        // Signal 'characteristicRead'
        QtMocHelpers::SignalData<void(QLowEnergyHandle, const QByteArray &)>(14, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 16 }, { QMetaType::QByteArray, 17 },
        }}),
        // Signal 'characteristicWritten'
        QtMocHelpers::SignalData<void(QLowEnergyHandle, const QByteArray &)>(18, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 16 }, { QMetaType::QByteArray, 17 },
        }}),
        // Signal 'characteristicUpdated'
        QtMocHelpers::SignalData<void(QLowEnergyHandle, const QByteArray &)>(19, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 16 }, { QMetaType::QByteArray, 17 },
        }}),
        // Signal 'descriptorRead'
        QtMocHelpers::SignalData<void(QLowEnergyHandle, const QByteArray &)>(20, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 21 }, { QMetaType::QByteArray, 17 },
        }}),
        // Signal 'descriptorWritten'
        QtMocHelpers::SignalData<void(QLowEnergyHandle, const QByteArray &)>(22, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 21 }, { QMetaType::QByteArray, 17 },
        }}),
        // Signal 'notificationEnabled'
        QtMocHelpers::SignalData<void(QLowEnergyHandle, bool)>(23, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 15, 16 }, { QMetaType::Bool, 24 },
        }}),
        // Signal 'servicesWereModified'
        QtMocHelpers::SignalData<void()>(25, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'rssiUpdated'
        QtMocHelpers::SignalData<void(qint16)>(26, 2, QMC::AccessPublic, QMetaType::Void, {{
            { QMetaType::Short, 9 },
        }}),
        // Signal 'LEnotSupported'
        QtMocHelpers::SignalData<void()>(27, 2, QMC::AccessPublic, QMetaType::Void),
        // Signal 'CBManagerError'
        QtMocHelpers::SignalData<void(QBluetoothDeviceDiscoveryAgent::Error)>(28, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 29, 30 },
        }}),
        // Signal 'CBManagerError'
        QtMocHelpers::SignalData<void(QLowEnergyController::Error)>(28, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 31, 30 },
        }}),
        // Signal 'CBManagerError'
        QtMocHelpers::SignalData<void(const QBluetoothUuid &, QLowEnergyController::Error)>(28, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 32, 33 }, { 0x80000000 | 31, 30 },
        }}),
        // Signal 'CBManagerError'
        QtMocHelpers::SignalData<void(const QBluetoothUuid &, QLowEnergyService::ServiceError)>(28, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 32, 33 }, { 0x80000000 | 34, 30 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<LECBManagerNotifier, qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject DarwinBluetooth::LECBManagerNotifier::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t>.metaTypes,
    nullptr
} };

void DarwinBluetooth::LECBManagerNotifier::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<LECBManagerNotifier *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->deviceDiscovered((*reinterpret_cast<std::add_pointer_t<QBluetoothDeviceInfo>>(_a[1]))); break;
        case 1: _t->discoveryFinished(); break;
        case 2: _t->connected(); break;
        case 3: _t->disconnected(); break;
        case 4: _t->mtuChanged((*reinterpret_cast<std::add_pointer_t<int>>(_a[1]))); break;
        case 5: _t->serviceDiscoveryFinished(); break;
        case 6: _t->serviceDetailsDiscoveryFinished((*reinterpret_cast<std::add_pointer_t<QSharedPointer<QLowEnergyServicePrivate>>>(_a[1]))); break;
        case 7: _t->characteristicRead((*reinterpret_cast<std::add_pointer_t<QLowEnergyHandle>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 8: _t->characteristicWritten((*reinterpret_cast<std::add_pointer_t<QLowEnergyHandle>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 9: _t->characteristicUpdated((*reinterpret_cast<std::add_pointer_t<QLowEnergyHandle>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 10: _t->descriptorRead((*reinterpret_cast<std::add_pointer_t<QLowEnergyHandle>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 11: _t->descriptorWritten((*reinterpret_cast<std::add_pointer_t<QLowEnergyHandle>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 12: _t->notificationEnabled((*reinterpret_cast<std::add_pointer_t<QLowEnergyHandle>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<bool>>(_a[2]))); break;
        case 13: _t->servicesWereModified(); break;
        case 14: _t->rssiUpdated((*reinterpret_cast<std::add_pointer_t<qint16>>(_a[1]))); break;
        case 15: _t->LEnotSupported(); break;
        case 16: _t->CBManagerError((*reinterpret_cast<std::add_pointer_t<QBluetoothDeviceDiscoveryAgent::Error>>(_a[1]))); break;
        case 17: _t->CBManagerError((*reinterpret_cast<std::add_pointer_t<QLowEnergyController::Error>>(_a[1]))); break;
        case 18: _t->CBManagerError((*reinterpret_cast<std::add_pointer_t<QBluetoothUuid>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QLowEnergyController::Error>>(_a[2]))); break;
        case 19: _t->CBManagerError((*reinterpret_cast<std::add_pointer_t<QBluetoothUuid>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QLowEnergyService::ServiceError>>(_a[2]))); break;
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
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QBluetoothDeviceInfo >(); break;
            }
            break;
        case 17:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyController::Error >(); break;
            }
            break;
        case 18:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QBluetoothUuid >(); break;
            case 1:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyController::Error >(); break;
            }
            break;
        case 19:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QBluetoothUuid >(); break;
            case 1:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyService::ServiceError >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QBluetoothDeviceInfo )>(_a, &LECBManagerNotifier::deviceDiscovered, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)()>(_a, &LECBManagerNotifier::discoveryFinished, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)()>(_a, &LECBManagerNotifier::connected, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)()>(_a, &LECBManagerNotifier::disconnected, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(int )>(_a, &LECBManagerNotifier::mtuChanged, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)()>(_a, &LECBManagerNotifier::serviceDiscoveryFinished, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QSharedPointer<QLowEnergyServicePrivate> )>(_a, &LECBManagerNotifier::serviceDetailsDiscoveryFinished, 6))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyHandle , const QByteArray & )>(_a, &LECBManagerNotifier::characteristicRead, 7))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyHandle , const QByteArray & )>(_a, &LECBManagerNotifier::characteristicWritten, 8))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyHandle , const QByteArray & )>(_a, &LECBManagerNotifier::characteristicUpdated, 9))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyHandle , const QByteArray & )>(_a, &LECBManagerNotifier::descriptorRead, 10))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyHandle , const QByteArray & )>(_a, &LECBManagerNotifier::descriptorWritten, 11))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyHandle , bool )>(_a, &LECBManagerNotifier::notificationEnabled, 12))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)()>(_a, &LECBManagerNotifier::servicesWereModified, 13))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(qint16 )>(_a, &LECBManagerNotifier::rssiUpdated, 14))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)()>(_a, &LECBManagerNotifier::LEnotSupported, 15))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QBluetoothDeviceDiscoveryAgent::Error )>(_a, &LECBManagerNotifier::CBManagerError, 16))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(QLowEnergyController::Error )>(_a, &LECBManagerNotifier::CBManagerError, 17))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(const QBluetoothUuid & , QLowEnergyController::Error )>(_a, &LECBManagerNotifier::CBManagerError, 18))
            return;
        if (QtMocHelpers::indexOfMethod<void (LECBManagerNotifier::*)(const QBluetoothUuid & , QLowEnergyService::ServiceError )>(_a, &LECBManagerNotifier::CBManagerError, 19))
            return;
    }
}

const QMetaObject *DarwinBluetooth::LECBManagerNotifier::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *DarwinBluetooth::LECBManagerNotifier::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15DarwinBluetooth19LECBManagerNotifierE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int DarwinBluetooth::LECBManagerNotifier::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 20)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 20;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 20)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 20;
    }
    return _id;
}

// SIGNAL 0
void DarwinBluetooth::LECBManagerNotifier::deviceDiscovered(QBluetoothDeviceInfo _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void DarwinBluetooth::LECBManagerNotifier::discoveryFinished()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}

// SIGNAL 2
void DarwinBluetooth::LECBManagerNotifier::connected()
{
    QMetaObject::activate(this, &staticMetaObject, 2, nullptr);
}

// SIGNAL 3
void DarwinBluetooth::LECBManagerNotifier::disconnected()
{
    QMetaObject::activate(this, &staticMetaObject, 3, nullptr);
}

// SIGNAL 4
void DarwinBluetooth::LECBManagerNotifier::mtuChanged(int _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 4, nullptr, _t1);
}

// SIGNAL 5
void DarwinBluetooth::LECBManagerNotifier::serviceDiscoveryFinished()
{
    QMetaObject::activate(this, &staticMetaObject, 5, nullptr);
}

// SIGNAL 6
void DarwinBluetooth::LECBManagerNotifier::serviceDetailsDiscoveryFinished(QSharedPointer<QLowEnergyServicePrivate> _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 6, nullptr, _t1);
}

// SIGNAL 7
void DarwinBluetooth::LECBManagerNotifier::characteristicRead(QLowEnergyHandle _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 7, nullptr, _t1, _t2);
}

// SIGNAL 8
void DarwinBluetooth::LECBManagerNotifier::characteristicWritten(QLowEnergyHandle _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 8, nullptr, _t1, _t2);
}

// SIGNAL 9
void DarwinBluetooth::LECBManagerNotifier::characteristicUpdated(QLowEnergyHandle _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 9, nullptr, _t1, _t2);
}

// SIGNAL 10
void DarwinBluetooth::LECBManagerNotifier::descriptorRead(QLowEnergyHandle _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 10, nullptr, _t1, _t2);
}

// SIGNAL 11
void DarwinBluetooth::LECBManagerNotifier::descriptorWritten(QLowEnergyHandle _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 11, nullptr, _t1, _t2);
}

// SIGNAL 12
void DarwinBluetooth::LECBManagerNotifier::notificationEnabled(QLowEnergyHandle _t1, bool _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 12, nullptr, _t1, _t2);
}

// SIGNAL 13
void DarwinBluetooth::LECBManagerNotifier::servicesWereModified()
{
    QMetaObject::activate(this, &staticMetaObject, 13, nullptr);
}

// SIGNAL 14
void DarwinBluetooth::LECBManagerNotifier::rssiUpdated(qint16 _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 14, nullptr, _t1);
}

// SIGNAL 15
void DarwinBluetooth::LECBManagerNotifier::LEnotSupported()
{
    QMetaObject::activate(this, &staticMetaObject, 15, nullptr);
}

// SIGNAL 16
void DarwinBluetooth::LECBManagerNotifier::CBManagerError(QBluetoothDeviceDiscoveryAgent::Error _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 16, nullptr, _t1);
}

// SIGNAL 17
void DarwinBluetooth::LECBManagerNotifier::CBManagerError(QLowEnergyController::Error _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 17, nullptr, _t1);
}

// SIGNAL 18
void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const QBluetoothUuid & _t1, QLowEnergyController::Error _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 18, nullptr, _t1, _t2);
}

// SIGNAL 19
void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const QBluetoothUuid & _t1, QLowEnergyService::ServiceError _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 19, nullptr, _t1, _t2);
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  A DarwinBluetooth::LECBManagerNotifier that Python can take functions over in. Every DarwinBluetooth::LECBManagerNotifier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDarwinBluetooth_LECBManagerNotifierCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDarwinBluetooth_LECBManagerNotifierCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDarwinBluetooth_LECBManagerNotifierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDarwinBluetooth_LECBManagerNotifier : public DarwinBluetooth::LECBManagerNotifier {
public:
  using DarwinBluetooth::LECBManagerNotifier::LECBManagerNotifier;
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
      CuteDarwinBluetooth_LECBManagerNotifierCall0 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall0>(taken[0]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall1 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall1>(taken[1]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall2 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall2>(taken[2]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall3 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall3>(taken[3]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall4 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall4>(taken[4]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall5 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall5>(taken[5]);
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
      CuteDarwinBluetooth_LECBManagerNotifierCall6 call = reinterpret_cast<CuteDarwinBluetooth_LECBManagerNotifierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DarwinBluetooth::LECBManagerNotifier::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15DarwinBluetooth19LECBManagerNotifier10metaObjectEv(
    const DarwinBluetooth::LECBManagerNotifier *self) {
  return self->metaObject();
}

//  void *DarwinBluetooth::LECBManagerNotifier::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15DarwinBluetooth19LECBManagerNotifier11qt_metacastEPKc(
    DarwinBluetooth::LECBManagerNotifier *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int DarwinBluetooth::LECBManagerNotifier::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15DarwinBluetooth19LECBManagerNotifier11qt_metacallEN11QMetaObject4CallEiPPv(
    DarwinBluetooth::LECBManagerNotifier *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString DarwinBluetooth::LECBManagerNotifier::tr(const char *s, const
//      char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15DarwinBluetooth19LECBManagerNotifier2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(DarwinBluetooth::LECBManagerNotifier::tr(s, c, n));
}

//  void DarwinBluetooth::LECBManagerNotifier::deviceDiscovered(QBluetoothDev
//      iceInfo deviceInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier16deviceDiscoveredE20QBluetoothDeviceInfo(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QBluetoothDeviceInfo *deviceInfo) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "deviceDiscovered(QBluetoothDeviceInfo)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "deviceDiscovered(QBluetoothDeviceInfo)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(deviceInfo)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::discoveryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier17discoveryFinishedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "discoveryFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "discoveryFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::connected()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier9connectedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "connected()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "connected()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier12disconnectedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "disconnected()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "disconnected()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::mtuChanged(int newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier10mtuChangedEi(
    DarwinBluetooth::LECBManagerNotifier *self,
    int newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "mtuChanged(int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "mtuChanged(int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::serviceDiscoveryFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier24serviceDiscoveryFinishedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serviceDiscoveryFinished()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serviceDiscoveryFinished()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::serviceDetailsDiscoveryFinishe
//      d(QSharedPointer<QLowEnergyServicePrivate> service)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier31serviceDetailsDiscoveryFinishedE14QSharedPointerI24QLowEnergyServicePrivateE(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "serviceDetailsDiscoveryFinished(QSharedPointer<QLowEnergyServicePrivate>)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "serviceDetailsDiscoveryFinished(QSharedPointer<QLowEnergyServicePrivate>)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(service)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      DarwinBluetooth::LECBManagerNotifier::characteristicRead(QLowEnergyHa
//      ndle charHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier18characteristicReadEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicRead(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicRead(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::characteristicWritten(QLowEner
//      gyHandle charHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier21characteristicWrittenEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicWritten(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicWritten(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::characteristicUpdated(QLowEner
//      gyHandle charHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier21characteristicUpdatedEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicUpdated(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicUpdated(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      DarwinBluetooth::LECBManagerNotifier::descriptorRead(QLowEnergyHandle
//      descHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14descriptorReadEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle descHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorRead(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorRead(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&descHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      DarwinBluetooth::LECBManagerNotifier::descriptorWritten(QLowEnergyHan
//      dle descHandle, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier17descriptorWrittenEtRK10QByteArray(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle descHandle,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorWritten(QLowEnergyHandle,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorWritten(QLowEnergyHandle,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&descHandle)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::notificationEnabled(QLowEnergy
//      Handle charHandle, bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier19notificationEnabledEtb(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyHandle charHandle,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "notificationEnabled(QLowEnergyHandle,bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "notificationEnabled(QLowEnergyHandle,bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&charHandle)),
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::servicesWereModified()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier20servicesWereModifiedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "servicesWereModified()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "servicesWereModified()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::rssiUpdated(qint16 newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier11rssiUpdatedEs(
    DarwinBluetooth::LECBManagerNotifier *self,
    qint16 newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "rssiUpdated(qint16)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "rssiUpdated(qint16)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::LEnotSupported()
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14LEnotSupportedEv(
    DarwinBluetooth::LECBManagerNotifier *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "LEnotSupported()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "LEnotSupported()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(QBluetoothDevic
//      eDiscoveryAgent::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorEN30QBluetoothDeviceDiscoveryAgent5ErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    QBluetoothDeviceDiscoveryAgent::Error error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(QBluetoothDeviceDiscoveryAgent::Error)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(QBluetoothDeviceDiscoveryAgent::Error)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(QLowEnergyContr
//      oller::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorEN20QLowEnergyController5ErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    QLowEnergyController::Error error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(QLowEnergyController::Error)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(QLowEnergyController::Error)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const
//      QBluetoothUuid &serviceUuid, QLowEnergyController::Error error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorERK14QBluetoothUuidN20QLowEnergyController5ErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QBluetoothUuid *serviceUuid,
    QLowEnergyController::Error error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(const QBluetoothUuid &,QLowEnergyController::Error)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(const QBluetoothUuid &,QLowEnergyController::Error)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(serviceUuid)),
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void DarwinBluetooth::LECBManagerNotifier::CBManagerError(const
//      QBluetoothUuid &serviceUuid, QLowEnergyService::ServiceError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN15DarwinBluetooth19LECBManagerNotifier14CBManagerErrorERK14QBluetoothUuidN17QLowEnergyService12ServiceErrorE(
    DarwinBluetooth::LECBManagerNotifier *self,
    const QBluetoothUuid *serviceUuid,
    QLowEnergyService::ServiceError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "DarwinBluetooth::LECBManagerNotifier")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "CBManagerError(const QBluetoothUuid &,QLowEnergyService::ServiceError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "CBManagerError(const QBluetoothUuid &,QLowEnergyService::ServiceError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(serviceUuid)),
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteDarwinBluetooth_LECBManagerNotifier, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DarwinBluetooth_LECBManagerNotifier(
    DarwinBluetooth::LECBManagerNotifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteDarwinBluetooth_LECBManagerNotifier *>(self)->take(key, call);
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/btnotifier_p.h>)
