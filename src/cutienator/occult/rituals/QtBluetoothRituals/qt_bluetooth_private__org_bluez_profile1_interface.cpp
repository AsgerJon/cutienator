//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/profile1_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/profile1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusextratypes.h>
#include <QtDBus/qdbusunixfiledescriptor.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtDBus/QDBusObjectPath>
#include <QtDBus/QDBusUnixFileDescriptor>
#include <QtCore/QMap>
#include <QtCore/QString>
#include <QtCore/QVariant>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/profile1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/profile1.cpp, line 25, as _ZN18QtBluetoothPrivate25OrgBluezProfile1InterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgBluezProfile1Interface::~OrgBluezProfile1Interface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezProfile1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezProfile1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezProfile1Interface : public QtBluetoothPrivate::OrgBluezProfile1Interface {
public:
  using QtBluetoothPrivate::OrgBluezProfile1Interface::OrgBluezProfile1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezProfile1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezProfile1Interface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate25OrgBluezProfile1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezProfile1Interface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezProfile1Interface::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezProfile1Interface::qt_metacall(QMetaObjec
//      t::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const char
//      *QtBluetoothPrivate::OrgBluezProfile1Interface::staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezProfile1Interface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgBluezProfile1Interface::~OrgBluezProfile1Interface
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1InterfaceD1Ev(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self) {
  delete self;
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezProfile1Interface::NewConnection(const
//      QDBusObjectPath &in0, const QDBusUnixFileDescriptor &in1, const
//      QVariantMap &in2)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface13NewConnectionERK15QDBusObjectPathRK23QDBusUnixFileDescriptorRK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self,
    const QDBusObjectPath *in0,
    const QDBusUnixFileDescriptor *in1,
    const QMap<QString, QVariant> *in2) {
  return new QDBusPendingReply<>(self->NewConnection(*in0, *in1, *in2));
}

//  void QtBluetoothPrivate::OrgBluezProfile1Interface::Release()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface7ReleaseEv(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self) {
  self->Release();
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezProfile1Interface::RequestDisconnection(c
//      onst QDBusObjectPath &in0)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate25OrgBluezProfile1Interface20RequestDisconnectionERK15QDBusObjectPath(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self,
    const QDBusObjectPath *in0) {
  return new QDBusPendingReply<>(self->RequestDisconnection(*in0));
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezProfile1Interface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezProfile1Interface(
    QtBluetoothPrivate::OrgBluezProfile1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezProfile1Interface *>(self)->take(key, call);
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgBluezProfile1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezProfile1Interface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
