//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/gattdesc1_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/gattdesc1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtCore/QByteArray>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QVariant>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/gattdesc1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/gattdesc1.cpp, line 25, as _ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1InterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgBluezGattDescriptor1Interface::~OrgBluezGattDescriptor1Interface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezGattDescriptor1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezGattDescriptor1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezGattDescriptor1Interface : public QtBluetoothPrivate::OrgBluezGattDescriptor1Interface {
public:
  using QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::OrgBluezGattDescriptor1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self) {
  return self->metaObject();
}

//  void
//      *QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::qt_metacast(co
//      nst char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::qt_metacall(QMe
//      taObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const char *QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::staticI
//      nterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::~OrgBluezGattDescri
//      ptor1Interface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1InterfaceD1Ev(
    QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self) {
  delete self;
}

//  QDBusObjectPath
//      QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::characteristic(
//      ) const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface14characteristicEv(
    const QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self) {
  return new QDBusObjectPath(self->characteristic());
}

//  QString QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::uUID()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface4uUIDEv(
    const QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self) {
  return new QString(self->uUID());
}

//  QByteArray QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::value()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface5valueEv(
    const QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self) {
  return new QByteArray(self->value());
}

//  QDBusPendingReply<QByteArray>
//      QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::ReadValue(const
//      QVariantMap &options)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QByteArray> *ritual_ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface9ReadValueERK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self,
    const QMap<QString, QVariant> *options) {
  return new QDBusPendingReply<QByteArray>(self->ReadValue(*options));
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezGattDescriptor1Interface::WriteValue(cons
//      t QByteArray &value, const QVariantMap &options)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate32OrgBluezGattDescriptor1Interface10WriteValueERK10QByteArrayRK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self,
    const QByteArray *value,
    const QMap<QString, QVariant> *options) {
  return new QDBusPendingReply<>(self->WriteValue(*value, *options));
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezGattDescriptor1Interface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezGattDescriptor1Interface(
    QtBluetoothPrivate::OrgBluezGattDescriptor1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezGattDescriptor1Interface *>(self)->take(key, call);
}

//  a QDBusPendingReply<QByteArray> a ritual of
//      QtBluetoothPrivate::OrgBluezGattDescriptor1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezGattDescriptor1Interface__QDBusPendingReply_QByteArray(
    QDBusPendingReply<QByteArray> *self) {
  delete self;
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgBluezGattDescriptor1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezGattDescriptor1Interface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
