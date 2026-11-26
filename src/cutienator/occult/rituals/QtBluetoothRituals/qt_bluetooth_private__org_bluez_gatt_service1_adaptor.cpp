//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/gattservice1adaptor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/gattservice1adaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/gattservice1adaptor_p.h>
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

//  from ../qtconnectivity/src/bluetooth/bluez/gattservice1adaptor.cpp, line 38, as _ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor6deviceEv
namespace QtBluetoothPrivate {
inline QDBusObjectPath OrgBluezGattService1Adaptor::device() const
{
    // get the value of property Device
    return qvariant_cast< QDBusObjectPath >(parent()->property("Device"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattservice1adaptor.cpp, line 44, as _ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor8includesEv
namespace QtBluetoothPrivate {
inline QList<QDBusObjectPath> OrgBluezGattService1Adaptor::includes() const
{
    // get the value of property Includes
    return qvariant_cast< QList<QDBusObjectPath> >(parent()->property("Includes"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattservice1adaptor.cpp, line 50, as _ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor7primaryEv
namespace QtBluetoothPrivate {
inline bool OrgBluezGattService1Adaptor::primary() const
{
    // get the value of property Primary
    return qvariant_cast< bool >(parent()->property("Primary"));
}
}  // namespace QtBluetoothPrivate

//  from ../qtconnectivity/src/bluetooth/bluez/gattservice1adaptor.cpp, line 56, as _ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor4uUIDEv
namespace QtBluetoothPrivate {
inline QString OrgBluezGattService1Adaptor::uUID() const
{
    // get the value of property UUID
    return qvariant_cast< QString >(parent()->property("UUID"));
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezGattService1Adaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezGattService1Adaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezGattService1Adaptor : public QtBluetoothPrivate::OrgBluezGattService1Adaptor {
public:
  using QtBluetoothPrivate::OrgBluezGattService1Adaptor::OrgBluezGattService1Adaptor;
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattService1AdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezGattService1Adaptor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezGattService1Adaptor *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezGattService1Adaptor::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate27OrgBluezGattService1Adaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezGattService1Adaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezGattService1Adaptor::qt_metacall(QMetaObj
//      ect::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate27OrgBluezGattService1Adaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezGattService1Adaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtBluetoothPrivate::OrgBluezGattService1Adaptor::~OrgBluezGattService1Ada
//      ptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate27OrgBluezGattService1AdaptorD1Ev(
    QtBluetoothPrivate::OrgBluezGattService1Adaptor *self) {
  delete self;
}

//  QDBusObjectPath QtBluetoothPrivate::OrgBluezGattService1Adaptor::device()
//      const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor6deviceEv(
    const QtBluetoothPrivate::OrgBluezGattService1Adaptor *self) {
  return new QDBusObjectPath(self->device());
}

//  QList<QDBusObjectPath>
//      QtBluetoothPrivate::OrgBluezGattService1Adaptor::includes() const
extern "C" Q_DECL_EXPORT
QList<QDBusObjectPath> *ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor8includesEv(
    const QtBluetoothPrivate::OrgBluezGattService1Adaptor *self) {
  return new QList<QDBusObjectPath>(self->includes());
}

//  bool QtBluetoothPrivate::OrgBluezGattService1Adaptor::primary() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor7primaryEv(
    const QtBluetoothPrivate::OrgBluezGattService1Adaptor *self) {
  return self->primary();
}

//  QString QtBluetoothPrivate::OrgBluezGattService1Adaptor::uUID() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate27OrgBluezGattService1Adaptor4uUIDEv(
    const QtBluetoothPrivate::OrgBluezGattService1Adaptor *self) {
  return new QString(self->uUID());
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezGattService1Adaptor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezGattService1Adaptor(
    QtBluetoothPrivate::OrgBluezGattService1Adaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezGattService1Adaptor *>(self)->take(key, call);
}

#endif  // QT_CONFIG(bluez)
