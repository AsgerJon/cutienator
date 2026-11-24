//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/leadvertisingmanager1_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/leadvertisingmanager1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface that Python can take functions over in. Every QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface : public QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface {
public:
  using QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::OrgBluezLEAdvertisingManager1Interface;
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1InterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::metaObje
//      ct() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface10metaObjectEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return self->metaObject();
}

//  const char *QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::s
//      taticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::staticInterfaceName();
}

//  uchar QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::activeI
//      nstances() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface15activeInstancesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return self->activeInstances();
}

//  QStringList QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::s
//      upportedIncludes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface17supportedIncludesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return new QList<QString>(self->supportedIncludes());
}

//  uchar QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface::support
//      edInstances() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK18QtBluetoothPrivate38OrgBluezLEAdvertisingManager1Interface18supportedInstancesEv(
    const QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self) {
  return self->supportedInstances();
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface(
    QtBluetoothPrivate::OrgBluezLEAdvertisingManager1Interface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgBluezLEAdvertisingManager1Interface *>(self)->take(key, call);
}
