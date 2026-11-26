//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QLowEnergyServicePrivate'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 5 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtBluetooth/qlowenergycharacteristic.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergydescriptor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtBluetooth/private/qlowenergyserviceprivate_p.h>
#include <QtBluetooth/private/qlowenergycontrollerbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtBluetooth__QLowEnergyServicePrivate.cpp, line 1, as moc:QLowEnergyServicePrivate
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN24QLowEnergyServicePrivateE_t {};
} // unnamed namespace

template <> constexpr inline auto QLowEnergyServicePrivate::qt_create_metaobjectdata<qt_meta_tag_ZN24QLowEnergyServicePrivateE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QLowEnergyServicePrivate",
        "stateChanged",
        "",
        "QLowEnergyService::ServiceState",
        "newState",
        "errorOccurred",
        "QLowEnergyService::ServiceError",
        "error",
        "characteristicChanged",
        "QLowEnergyCharacteristic",
        "characteristic",
        "newValue",
        "characteristicRead",
        "info",
        "value",
        "characteristicWritten",
        "descriptorRead",
        "QLowEnergyDescriptor",
        "descriptorWritten",
        "descriptor"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'stateChanged'
        QtMocHelpers::SignalData<void(QLowEnergyService::ServiceState)>(1, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 3, 4 },
        }}),
        // Signal 'errorOccurred'
        QtMocHelpers::SignalData<void(QLowEnergyService::ServiceError)>(5, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 6, 7 },
        }}),
        // Signal 'characteristicChanged'
        QtMocHelpers::SignalData<void(const QLowEnergyCharacteristic &, const QByteArray &)>(8, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 9, 10 }, { QMetaType::QByteArray, 11 },
        }}),
        // Signal 'characteristicRead'
        QtMocHelpers::SignalData<void(const QLowEnergyCharacteristic &, const QByteArray &)>(12, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 9, 13 }, { QMetaType::QByteArray, 14 },
        }}),
        // Signal 'characteristicWritten'
        QtMocHelpers::SignalData<void(const QLowEnergyCharacteristic &, const QByteArray &)>(15, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 9, 10 }, { QMetaType::QByteArray, 11 },
        }}),
        // Signal 'descriptorRead'
        QtMocHelpers::SignalData<void(const QLowEnergyDescriptor &, const QByteArray &)>(16, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 17, 13 }, { QMetaType::QByteArray, 14 },
        }}),
        // Signal 'descriptorWritten'
        QtMocHelpers::SignalData<void(const QLowEnergyDescriptor &, const QByteArray &)>(18, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 17, 19 }, { QMetaType::QByteArray, 11 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<QLowEnergyServicePrivate, qt_meta_tag_ZN24QLowEnergyServicePrivateE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QLowEnergyServicePrivate::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QLowEnergyServicePrivateE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QLowEnergyServicePrivateE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN24QLowEnergyServicePrivateE_t>.metaTypes,
    nullptr
} };

void QLowEnergyServicePrivate::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QLowEnergyServicePrivate *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->stateChanged((*reinterpret_cast<std::add_pointer_t<QLowEnergyService::ServiceState>>(_a[1]))); break;
        case 1: _t->errorOccurred((*reinterpret_cast<std::add_pointer_t<QLowEnergyService::ServiceError>>(_a[1]))); break;
        case 2: _t->characteristicChanged((*reinterpret_cast<std::add_pointer_t<QLowEnergyCharacteristic>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 3: _t->characteristicRead((*reinterpret_cast<std::add_pointer_t<QLowEnergyCharacteristic>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 4: _t->characteristicWritten((*reinterpret_cast<std::add_pointer_t<QLowEnergyCharacteristic>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 5: _t->descriptorRead((*reinterpret_cast<std::add_pointer_t<QLowEnergyDescriptor>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
        case 6: _t->descriptorWritten((*reinterpret_cast<std::add_pointer_t<QLowEnergyDescriptor>>(_a[1])),(*reinterpret_cast<std::add_pointer_t<QByteArray>>(_a[2]))); break;
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
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyService::ServiceState >(); break;
            }
            break;
        case 1:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyService::ServiceError >(); break;
            }
            break;
        case 2:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyCharacteristic >(); break;
            }
            break;
        case 3:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyCharacteristic >(); break;
            }
            break;
        case 4:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyCharacteristic >(); break;
            }
            break;
        case 5:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyDescriptor >(); break;
            }
            break;
        case 6:
            switch (*reinterpret_cast<int*>(_a[1])) {
            default: *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType(); break;
            case 0:
                *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType::fromType< QLowEnergyDescriptor >(); break;
            }
            break;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(QLowEnergyService::ServiceState )>(_a, &QLowEnergyServicePrivate::stateChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(QLowEnergyService::ServiceError )>(_a, &QLowEnergyServicePrivate::errorOccurred, 1))
            return;
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(const QLowEnergyCharacteristic & , const QByteArray & )>(_a, &QLowEnergyServicePrivate::characteristicChanged, 2))
            return;
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(const QLowEnergyCharacteristic & , const QByteArray & )>(_a, &QLowEnergyServicePrivate::characteristicRead, 3))
            return;
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(const QLowEnergyCharacteristic & , const QByteArray & )>(_a, &QLowEnergyServicePrivate::characteristicWritten, 4))
            return;
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(const QLowEnergyDescriptor & , const QByteArray & )>(_a, &QLowEnergyServicePrivate::descriptorRead, 5))
            return;
        if (QtMocHelpers::indexOfMethod<void (QLowEnergyServicePrivate::*)(const QLowEnergyDescriptor & , const QByteArray & )>(_a, &QLowEnergyServicePrivate::descriptorWritten, 6))
            return;
    }
}

const QMetaObject *QLowEnergyServicePrivate::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QLowEnergyServicePrivate::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN24QLowEnergyServicePrivateE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QLowEnergyServicePrivate::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    }
    return _id;
}

// SIGNAL 0
void QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceState _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 0, nullptr, _t1);
}

// SIGNAL 1
void QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::ServiceError _t1)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 1, nullptr, _t1);
}

// SIGNAL 2
void QLowEnergyServicePrivate::characteristicChanged(const QLowEnergyCharacteristic & _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 2, nullptr, _t1, _t2);
}

// SIGNAL 3
void QLowEnergyServicePrivate::characteristicRead(const QLowEnergyCharacteristic & _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 3, nullptr, _t1, _t2);
}

// SIGNAL 4
void QLowEnergyServicePrivate::characteristicWritten(const QLowEnergyCharacteristic & _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 4, nullptr, _t1, _t2);
}

// SIGNAL 5
void QLowEnergyServicePrivate::descriptorRead(const QLowEnergyDescriptor & _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 5, nullptr, _t1, _t2);
}

// SIGNAL 6
void QLowEnergyServicePrivate::descriptorWritten(const QLowEnergyDescriptor & _t1, const QByteArray & _t2)
{
    QMetaObject::activate<void>(this, &staticMetaObject, 6, nullptr, _t1, _t2);
}
QT_WARNING_POP

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 13, as _ZN24QLowEnergyServicePrivateC1EP7QObject
inline QLowEnergyServicePrivate::QLowEnergyServicePrivate(QObject *parent) : QObject(parent) { }

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 15, as _ZN24QLowEnergyServicePrivateD1Ev
inline QLowEnergyServicePrivate::~QLowEnergyServicePrivate()
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 19, as _ZN24QLowEnergyServicePrivate13setControllerEP27QLowEnergyControllerPrivate
inline void QLowEnergyServicePrivate::setController(QLowEnergyControllerPrivate *control)
{
    controller = control;

    if (control)
        setState(QLowEnergyService::RemoteService);
    else
        setState(QLowEnergyService::InvalidService);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 29, as _ZN24QLowEnergyServicePrivate8setErrorEN17QLowEnergyService12ServiceErrorE
inline void QLowEnergyServicePrivate::setError(QLowEnergyService::ServiceError newError)
{
    lastError = newError;
    emit errorOccurred(newError);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergyserviceprivate.cpp, line 35, as _ZN24QLowEnergyServicePrivate8setStateEN17QLowEnergyService12ServiceStateE
inline void QLowEnergyServicePrivate::setState(QLowEnergyService::ServiceState newState)
{
    if (state == newState)
        return;

    state = newState;
    emit stateChanged(newState);
}
//  -----------------------------------------------------------------------

//  A QLowEnergyServicePrivate that Python can take functions over in. Every QLowEnergyServicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyServicePrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLowEnergyServicePrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLowEnergyServicePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLowEnergyServicePrivate : public QLowEnergyServicePrivate {
public:
  using QLowEnergyServicePrivate::QLowEnergyServicePrivate;
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
      CuteQLowEnergyServicePrivateCall0 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall0>(taken[0]);
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
      CuteQLowEnergyServicePrivateCall1 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall1>(taken[1]);
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
      CuteQLowEnergyServicePrivateCall2 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall2>(taken[2]);
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
      CuteQLowEnergyServicePrivateCall3 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall3>(taken[3]);
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
      CuteQLowEnergyServicePrivateCall4 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall4>(taken[4]);
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
      CuteQLowEnergyServicePrivateCall5 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall5>(taken[5]);
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
      CuteQLowEnergyServicePrivateCall6 call = reinterpret_cast<CuteQLowEnergyServicePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLowEnergyServicePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QLowEnergyServicePrivate10metaObjectEv(
    const QLowEnergyServicePrivate *self) {
  return self->metaObject();
}

//  void *QLowEnergyServicePrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QLowEnergyServicePrivate11qt_metacastEPKc(
    QLowEnergyServicePrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QLowEnergyServicePrivate::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QLowEnergyServicePrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    QLowEnergyServicePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QLowEnergyServicePrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QLowEnergyServicePrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLowEnergyServicePrivate::tr(s, c, n));
}

//  QLowEnergyServicePrivate::QLowEnergyServicePrivate(QObject *parent)
extern "C" Q_DECL_EXPORT
QLowEnergyServicePrivate *ritual_ZN24QLowEnergyServicePrivateC1EP7QObject(
    QObject *parent) {
  return new CuteQLowEnergyServicePrivate(parent);
}

//  QLowEnergyServicePrivate::~QLowEnergyServicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivateD1Ev(
    QLowEnergyServicePrivate *self) {
  delete self;
}

//  void QLowEnergyServicePrivate::setController(QLowEnergyControllerPrivate
//      *control)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate13setControllerEP27QLowEnergyControllerPrivate(
    QLowEnergyServicePrivate *self,
    QLowEnergyControllerPrivate *control) {
  self->setController(control);
}

//  void QLowEnergyServicePrivate::setError(QLowEnergyService::ServiceError
//      newError)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate8setErrorEN17QLowEnergyService12ServiceErrorE(
    QLowEnergyServicePrivate *self,
    QLowEnergyService::ServiceError newError) {
  self->setError(newError);
}

//  void QLowEnergyServicePrivate::setState(QLowEnergyService::ServiceState
//      newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate8setStateEN17QLowEnergyService12ServiceStateE(
    QLowEnergyServicePrivate *self,
    QLowEnergyService::ServiceState newState) {
  self->setState(newState);
}

//  void
//      QLowEnergyServicePrivate::stateChanged(QLowEnergyService::ServiceStat
//      e newState)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate12stateChangedEN17QLowEnergyService12ServiceStateE(
    QLowEnergyServicePrivate *self,
    QLowEnergyService::ServiceState newState) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "stateChanged(QLowEnergyService::ServiceState)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "stateChanged(QLowEnergyService::ServiceState)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&newState)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      QLowEnergyServicePrivate::errorOccurred(QLowEnergyService::ServiceErr
//      or error)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate13errorOccurredEN17QLowEnergyService12ServiceErrorE(
    QLowEnergyServicePrivate *self,
    QLowEnergyService::ServiceError error) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "errorOccurred(QLowEnergyService::ServiceError)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "errorOccurred(QLowEnergyService::ServiceError)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&error)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::characteristicChanged(const
//      QLowEnergyCharacteristic &characteristic, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate21characteristicChangedERK24QLowEnergyCharacteristicRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyCharacteristic *characteristic,
    const QByteArray *newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicChanged(const QLowEnergyCharacteristic &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicChanged(const QLowEnergyCharacteristic &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(characteristic)),
      const_cast<void *>(static_cast<const void *>(newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::characteristicRead(const
//      QLowEnergyCharacteristic &info, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate18characteristicReadERK24QLowEnergyCharacteristicRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyCharacteristic *info,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicRead(const QLowEnergyCharacteristic &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicRead(const QLowEnergyCharacteristic &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(info)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::characteristicWritten(const
//      QLowEnergyCharacteristic &characteristic, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate21characteristicWrittenERK24QLowEnergyCharacteristicRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyCharacteristic *characteristic,
    const QByteArray *newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "characteristicWritten(const QLowEnergyCharacteristic &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "characteristicWritten(const QLowEnergyCharacteristic &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(characteristic)),
      const_cast<void *>(static_cast<const void *>(newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::descriptorRead(const QLowEnergyDescriptor
//      &info, const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate14descriptorReadERK20QLowEnergyDescriptorRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyDescriptor *info,
    const QByteArray *value) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorRead(const QLowEnergyDescriptor &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorRead(const QLowEnergyDescriptor &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(info)),
      const_cast<void *>(static_cast<const void *>(value)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QLowEnergyServicePrivate::descriptorWritten(const
//      QLowEnergyDescriptor &descriptor, const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate17descriptorWrittenERK20QLowEnergyDescriptorRK10QByteArray(
    QLowEnergyServicePrivate *self,
    const QLowEnergyDescriptor *descriptor,
    const QByteArray *newValue) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QLowEnergyServicePrivate")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "descriptorWritten(const QLowEnergyDescriptor &,const QByteArray &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "descriptorWritten(const QLowEnergyDescriptor &,const QByteArray &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(descriptor)),
      const_cast<void *>(static_cast<const void *>(newValue)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQLowEnergyServicePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLowEnergyServicePrivate(
    QLowEnergyServicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLowEnergyServicePrivate *>(self)->take(key, call);
}
