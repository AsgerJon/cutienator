//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCore/6.12.0/QtQmlCore/private/qqmlpermissions_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QQmlBluetoothPermission'
//  is pasted in, cut from what the moc of Qt 6.12.0 writes for its header:
//  Qt's library keeps it to itself; added are 3 rituals that lean on what
//  moc writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#include <QtQmlCore/qtqmlcoreexports.h>
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlcoreglobal_p.h>
#if QT_CONFIG(permissions)
#if QT_CONFIG(permissions)
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlcoreglobal_p.h>
#include <QtQmlCore/QtQmlCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCore/6.12.0/QtQmlCore/private/qqmlpermissions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtQmlCore__QQmlBluetoothPermission.cpp, line 1, as moc:QQmlBluetoothPermission
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN23QQmlBluetoothPermissionE_t {};
} // unnamed namespace

template <> constexpr inline auto QQmlBluetoothPermission::qt_create_metaobjectdata<qt_meta_tag_ZN23QQmlBluetoothPermissionE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QQmlBluetoothPermission",
        "QML.Element",
        "BluetoothPermission",
        "QML.AddedInVersion",
        "1542",
        "QML.Extended",
        "QBluetoothPermission",
        "QML.ExtensionIsNamespace",
        "true",
        "statusChanged",
        "",
        "communicationModesChanged",
        "request",
        "status",
        "Qt::PermissionStatus",
        "communicationModes",
        "QBluetoothPermission::CommunicationModes"
    };

    QtMocHelpers::UintData qt_methods {
        // Signal 'statusChanged'
        QtMocHelpers::SignalData<void()>(9, 10, QMC::AccessPublic, QMetaType::Void),
        // Signal 'communicationModesChanged'
        QtMocHelpers::SignalData<void()>(11, 10, QMC::AccessPublic, QMetaType::Void),
        // Method 'request'
        QtMocHelpers::MethodData<void()>(12, 10, QMC::AccessPublic, QMetaType::Void),
    };
    QtMocHelpers::UintData qt_properties {
        // property 'status'
        QtMocHelpers::PropertyData<Qt::PermissionStatus>(13, 0x80000000 | 14, QMC::DefaultPropertyFlags | QMC::EnumOrFlag, 0),
        // property 'communicationModes'
        QtMocHelpers::PropertyData<QBluetoothPermission::CommunicationModes>(15, 0x80000000 | 16, QMC::DefaultPropertyFlags | QMC::Writable | QMC::EnumOrFlag | QMC::StdCppSet, 1),
    };
    QtMocHelpers::UintData qt_enums {
    };
    QtMocHelpers::UintData qt_constructors {};
    QtMocHelpers::ClassInfos qt_classinfo({
            {    1,    2 },
            {    3,    4 },
            {    5,    6 },
            {    7,    8 },
    });
    return QtMocHelpers::metaObjectData<QQmlBluetoothPermission, void>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums, qt_constructors, qt_classinfo);
}
Q_CONSTINIT static const QMetaObject::SuperData qt_meta_extradata_ZN23QQmlBluetoothPermissionE[] = {
    QMetaObject::SuperData::link<QBluetoothPermission::staticMetaObject>(),
    nullptr
};

Q_CONSTINIT const QMetaObject QQmlBluetoothPermission::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQmlBluetoothPermissionE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQmlBluetoothPermissionE_t>.data,
    qt_static_metacall,
    qt_meta_extradata_ZN23QQmlBluetoothPermissionE,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN23QQmlBluetoothPermissionE_t>.metaTypes,
    nullptr
} };

void QQmlBluetoothPermission::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QQmlBluetoothPermission *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->statusChanged(); break;
        case 1: _t->communicationModesChanged(); break;
        case 2: _t->request(); break;
        default: ;
        }
    }
    if (_c == QMetaObject::IndexOfMethod) {
        if (QtMocHelpers::indexOfMethod<void (QQmlBluetoothPermission::*)()>(_a, &QQmlBluetoothPermission::statusChanged, 0))
            return;
        if (QtMocHelpers::indexOfMethod<void (QQmlBluetoothPermission::*)()>(_a, &QQmlBluetoothPermission::communicationModesChanged, 1))
            return;
    }
    if (_c == QMetaObject::ReadProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 0: *reinterpret_cast<Qt::PermissionStatus*>(_v) = _t->status(); break;
        case 1: *reinterpret_cast<QBluetoothPermission::CommunicationModes*>(_v) = _t->communicationModes(); break;
        default: break;
        }
    }
    if (_c == QMetaObject::WriteProperty) {
        void *_v = _a[0];
        switch (_id) {
        case 1: _t->setCommunicationModes(*reinterpret_cast<QBluetoothPermission::CommunicationModes*>(_v)); break;
        default: break;
        }
    }
}

const QMetaObject *QQmlBluetoothPermission::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QQmlBluetoothPermission::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN23QQmlBluetoothPermissionE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QQmlBluetoothPermission::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 3)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 3;
    }
    if (_c == QMetaObject::ReadProperty || _c == QMetaObject::WriteProperty
            || _c == QMetaObject::ResetProperty || _c == QMetaObject::BindableProperty
            || _c == QMetaObject::RegisterPropertyMetaType) {
        qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    return _id;
}

// SIGNAL 0
void QQmlBluetoothPermission::statusChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 0, nullptr);
}

// SIGNAL 1
void QQmlBluetoothPermission::communicationModesChanged()
{
    QMetaObject::activate(this, &staticMetaObject, 1, nullptr);
}
QT_WARNING_POP
//  -----------------------------------------------------------------------

//  A QQmlBluetoothPermission that Python can take functions over in. Every QQmlBluetoothPermission
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlBluetoothPermissionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlBluetoothPermissionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBluetoothPermissionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBluetoothPermissionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBluetoothPermissionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBluetoothPermissionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlBluetoothPermissionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlBluetoothPermission : public QQmlBluetoothPermission {
public:
  using QQmlBluetoothPermission::QQmlBluetoothPermission;
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
      CuteQQmlBluetoothPermissionCall0 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall0>(taken[0]);
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
      CuteQQmlBluetoothPermissionCall1 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall1>(taken[1]);
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
      CuteQQmlBluetoothPermissionCall2 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall2>(taken[2]);
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
      CuteQQmlBluetoothPermissionCall3 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall3>(taken[3]);
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
      CuteQQmlBluetoothPermissionCall4 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall4>(taken[4]);
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
      CuteQQmlBluetoothPermissionCall5 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall5>(taken[5]);
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
      CuteQQmlBluetoothPermissionCall6 call = reinterpret_cast<CuteQQmlBluetoothPermissionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlBluetoothPermission::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQmlBluetoothPermission10metaObjectEv(
    const QQmlBluetoothPermission *self) {
  return self->metaObject();
}

//  void *QQmlBluetoothPermission::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQmlBluetoothPermission11qt_metacastEPKc(
    QQmlBluetoothPermission *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlBluetoothPermission::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQmlBluetoothPermission11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlBluetoothPermission *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlBluetoothPermission::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQmlBluetoothPermission2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlBluetoothPermission::tr(s, c, n));
}

//  Qt::PermissionStatus QQmlBluetoothPermission::status() const
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZNK23QQmlBluetoothPermission6statusEv(
    const QQmlBluetoothPermission *self) {
  return self->status();
}

//  void QQmlBluetoothPermission::request()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlBluetoothPermission7requestEv(
    QQmlBluetoothPermission *self) {
  self->request();
}

//  const QMetaObject *QQmlBluetoothPermission::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN23QQmlBluetoothPermission20qmlExtendedNamespaceEv() {
  return QQmlBluetoothPermission::qmlExtendedNamespace();
}

//  void QQmlBluetoothPermission::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlBluetoothPermission30qt_qmlMarker_extendedNamespaceEv(
    QQmlBluetoothPermission *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QBluetoothPermission::CommunicationModes
//      QQmlBluetoothPermission::communicationModes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QQmlBluetoothPermission18communicationModesEv(
    const QQmlBluetoothPermission *self) {
  return static_cast<int>(self->communicationModes().toInt());
}

//  void QQmlBluetoothPermission::setCommunicationModes(const
//      QBluetoothPermission::CommunicationModes &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQmlBluetoothPermission21setCommunicationModesERK6QFlagsIN20QBluetoothPermission17CommunicationModeEE(
    QQmlBluetoothPermission *self,
    const QBluetoothPermission::CommunicationModes *value) {
  self->setCommunicationModes(*value);
}

//  a Python function taken by a CuteQQmlBluetoothPermission, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlBluetoothPermission(
    QQmlBluetoothPermission *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlBluetoothPermission *>(self)->take(key, call);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
