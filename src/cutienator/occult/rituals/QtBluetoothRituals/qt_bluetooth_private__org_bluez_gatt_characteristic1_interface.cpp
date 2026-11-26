//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/gattchar1_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/gattchar1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
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
#include <QtBluetooth/private/gattchar1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/gattchar1.cpp, line 25, as _ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1InterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgBluezGattCharacteristic1Interface::~OrgBluezGattCharacteristic1Interface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Interface : public QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface {
public:
  using QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::OrgBluezGattCharacteristic1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::metaObject
//      () const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::qt_metaca
//      st(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::qt_metacall
//      (QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const char *QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::sta
//      ticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::~OrgBluezGattCh
//      aracteristic1Interface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1InterfaceD1Ev(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  delete self;
}

//  QStringList
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::flags()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface5flagsEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return new QList<QString>(self->flags());
}

//  bool
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::notifying()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface9notifyingEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return self->notifying();
}

//  QDBusObjectPath
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::service()
//      const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface7serviceEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return new QDBusObjectPath(self->service());
}

//  QString QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::uUID()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface4uUIDEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return new QString(self->uUID());
}

//  QByteArray
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::value()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface5valueEv(
    const QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return new QByteArray(self->value());
}

//  QDBusPendingReply<QByteArray>
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::ReadValue(c
//      onst QVariantMap &options)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QByteArray> *ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface9ReadValueERK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self,
    const QMap<QString, QVariant> *options) {
  return new QDBusPendingReply<QByteArray>(self->ReadValue(*options));
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StartNotify
//      ()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface11StartNotifyEv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return new QDBusPendingReply<>(self->StartNotify());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface::StopNotify(
//      )
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface10StopNotifyEv(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self) {
  return new QDBusPendingReply<>(self->StopNotify());
}

//  QDBusPendingReply<> QtBluetoothPrivate::OrgBluezGattCharacteristic1Interf
//      ace::WriteValue(const QByteArray &value, const QVariantMap &options)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate36OrgBluezGattCharacteristic1Interface10WriteValueERK10QByteArrayRK4QMapI7QString8QVariantE(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self,
    const QByteArray *value,
    const QMap<QString, QVariant> *options) {
  return new QDBusPendingReply<>(self->WriteValue(*value, *options));
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Interface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezGattCharacteristic1Interface(
    QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezGattCharacteristic1Interface *>(self)->take(key, call);
}

//  a QDBusPendingReply<QByteArray> a ritual of
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezGattCharacteristic1Interface__QDBusPendingReply_QByteArray(
    QDBusPendingReply<QByteArray> *self) {
  delete self;
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgBluezGattCharacteristic1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezGattCharacteristic1Interface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
