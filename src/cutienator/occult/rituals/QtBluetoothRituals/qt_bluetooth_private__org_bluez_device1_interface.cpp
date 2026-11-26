//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/device1_bluez5_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/device1_bluez5_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/device1_bluez5_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/device1_bluez5.cpp, line 25, as _ZN18QtBluetoothPrivate24OrgBluezDevice1InterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgBluezDevice1Interface::~OrgBluezDevice1Interface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgBluezDevice1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezDevice1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezDevice1Interface : public QtBluetoothPrivate::OrgBluezDevice1Interface {
public:
  using QtBluetoothPrivate::OrgBluezDevice1Interface::OrgBluezDevice1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezDevice1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezDevice1Interface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgBluezDevice1Interface::qt_metacast(const
//      char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgBluezDevice1Interface::qt_metacall(QMetaObject
//      ::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const char
//      *QtBluetoothPrivate::OrgBluezDevice1Interface::staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezDevice1Interface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgBluezDevice1Interface::~OrgBluezDevice1Interface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1InterfaceD1Ev(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  delete self;
}

//  QDBusObjectPath QtBluetoothPrivate::OrgBluezDevice1Interface::adapter()
//      const
extern "C" Q_DECL_EXPORT
QDBusObjectPath *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7adapterEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QDBusObjectPath(self->adapter());
}

//  QString QtBluetoothPrivate::OrgBluezDevice1Interface::address() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7addressEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QString(self->address());
}

//  QString QtBluetoothPrivate::OrgBluezDevice1Interface::alias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface5aliasEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QString(self->alias());
}

//  void QtBluetoothPrivate::OrgBluezDevice1Interface::setAlias(const QString
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface8setAliasERK7QString(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    const QString *value) {
  self->setAlias(*value);
}

//  ushort QtBluetoothPrivate::OrgBluezDevice1Interface::appearance() const
extern "C" Q_DECL_EXPORT
ushort ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface10appearanceEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->appearance();
}

//  bool QtBluetoothPrivate::OrgBluezDevice1Interface::blocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7blockedEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->blocked();
}

//  void QtBluetoothPrivate::OrgBluezDevice1Interface::setBlocked(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface10setBlockedEb(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    bool value) {
  self->setBlocked(value);
}

//  uint QtBluetoothPrivate::OrgBluezDevice1Interface::classProperty() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface13classPropertyEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->classProperty();
}

//  bool QtBluetoothPrivate::OrgBluezDevice1Interface::connected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface9connectedEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->connected();
}

//  QString QtBluetoothPrivate::OrgBluezDevice1Interface::icon() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface4iconEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QString(self->icon());
}

//  bool QtBluetoothPrivate::OrgBluezDevice1Interface::legacyPairing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface13legacyPairingEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->legacyPairing();
}

//  QString QtBluetoothPrivate::OrgBluezDevice1Interface::modalias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface8modaliasEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QString(self->modalias());
}

//  QString QtBluetoothPrivate::OrgBluezDevice1Interface::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface4nameEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QString(self->name());
}

//  bool QtBluetoothPrivate::OrgBluezDevice1Interface::paired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface6pairedEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->paired();
}

//  short QtBluetoothPrivate::OrgBluezDevice1Interface::rSSI() const
extern "C" Q_DECL_EXPORT
short ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface4rSSIEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->rSSI();
}

//  bool QtBluetoothPrivate::OrgBluezDevice1Interface::servicesResolved()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface16servicesResolvedEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->servicesResolved();
}

//  bool QtBluetoothPrivate::OrgBluezDevice1Interface::trusted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7trustedEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->trusted();
}

//  void QtBluetoothPrivate::OrgBluezDevice1Interface::setTrusted(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface10setTrustedEb(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    bool value) {
  self->setTrusted(value);
}

//  short QtBluetoothPrivate::OrgBluezDevice1Interface::txPower() const
extern "C" Q_DECL_EXPORT
short ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface7txPowerEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return self->txPower();
}

//  QStringList QtBluetoothPrivate::OrgBluezDevice1Interface::uUIDs() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate24OrgBluezDevice1Interface5uUIDsEv(
    const QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QList<QString>(self->uUIDs());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezDevice1Interface::CancelPairing()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface13CancelPairingEv(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QDBusPendingReply<>(self->CancelPairing());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezDevice1Interface::Connect()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface7ConnectEv(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QDBusPendingReply<>(self->Connect());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezDevice1Interface::ConnectProfile(const
//      QString &UUID)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface14ConnectProfileERK7QString(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    const QString *UUID) {
  return new QDBusPendingReply<>(self->ConnectProfile(*UUID));
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezDevice1Interface::Disconnect()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface10DisconnectEv(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QDBusPendingReply<>(self->Disconnect());
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgBluezDevice1Interface::DisconnectProfile(const
//      QString &UUID)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface17DisconnectProfileERK7QString(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    const QString *UUID) {
  return new QDBusPendingReply<>(self->DisconnectProfile(*UUID));
}

//  QDBusPendingReply<> QtBluetoothPrivate::OrgBluezDevice1Interface::Pair()
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate24OrgBluezDevice1Interface4PairEv(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self) {
  return new QDBusPendingReply<>(self->Pair());
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezDevice1Interface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezDevice1Interface(
    QtBluetoothPrivate::OrgBluezDevice1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezDevice1Interface *>(self)->take(key, call);
}

//  a ManufacturerDataList a ritual of
//      QtBluetoothPrivate::OrgBluezDevice1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezDevice1Interface__ManufacturerDataList(
    ManufacturerDataList *self) {
  delete self;
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgBluezDevice1Interface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgBluezDevice1Interface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
