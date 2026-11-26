//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/properties_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/properties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qvariant.h>
#include <QtDBus/qdbusmessage.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <cstring>
#include <QtDBus/QDBusPendingReply>
#include <QtDBus/QDBusVariant>
#include <QtCore/QString>
#include <QtCore/QVariantMap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/properties_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/properties.cpp, line 25, as _ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgFreedesktopDBusPropertiesInterface::~OrgFreedesktopDBusPropertiesInterface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface that Python can take functions over in. Every QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface : public QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface {
public:
  using QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::OrgFreedesktopDBusPropertiesInterface;
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::metaObjec
//      t() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface10metaObjectEv(
    const QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::qt_metac
//      ast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::qt_metacal
//      l(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const char *QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::st
//      aticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::~OrgFreedeskto
//      pDBusPropertiesInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterfaceD1Ev(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self) {
  delete self;
}

//  QDBusPendingReply<QDBusVariant>
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Get(const
//      QString &interface, const QString &name)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QDBusVariant> *ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface3GetERK7QStringS3_(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    const QString *interface,
    const QString *name) {
  return new QDBusPendingReply<QDBusVariant>(self->Get(*interface, *name));
}

//  QDBusPendingReply<QVariantMap>
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::GetAll(con
//      st QString &interface)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<QVariantMap> *ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface6GetAllERK7QString(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    const QString *interface) {
  return new QDBusPendingReply<QVariantMap>(self->GetAll(*interface));
}

//  QDBusPendingReply<>
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Set(const
//      QString &interface, const QString &name, const QDBusVariant &value)
extern "C" Q_DECL_EXPORT
QDBusPendingReply<> *ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface3SetERK7QStringS3_RK12QDBusVariant(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    const QString *interface,
    const QString *name,
    const QDBusVariant *value) {
  return new QDBusPendingReply<>(self->Set(*interface, *name, *value));
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface::Propertie
//      sChanged(const QString &interface, const QVariantMap
//      &changed_properties, const QStringList &invalidated_properties, const
//      QDBusMessage &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate37OrgFreedesktopDBusPropertiesInterface17PropertiesChangedERK7QStringRK4QMapIS1_8QVariantERK5QListIS1_ERK12QDBusMessage(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    const QString *interface,
    const QMap<QString, QVariant> *changed_properties,
    const QList<QString> *invalidated_properties,
    const QDBusMessage *msg) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "PropertiesChanged(const QString &,const QVariantMap &,const QStringList &,const QDBusMessage &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "PropertiesChanged(const QString &,const QVariantMap &,const QStringList &,const QDBusMessage &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(interface)),
      const_cast<void *>(static_cast<const void *>(changed_properties)),
      const_cast<void *>(static_cast<const void *>(invalidated_properties)),
      const_cast<void *>(static_cast<const void *>(msg)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface(
    QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface *>(self)->take(key, call);
}

//  a QDBusPendingReply<QDBusVariant> a ritual of
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface__QDBusPendingReply_QDBusVariant(
    QDBusPendingReply<QDBusVariant> *self) {
  delete self;
}

//  a QDBusPendingReply<QVariantMap> a ritual of
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface__QDBusPendingReply_QVariantMap(
    QDBusPendingReply<QVariantMap> *self) {
  delete self;
}

//  a QDBusPendingReply<> a ritual of
//      QtBluetoothPrivate::OrgFreedesktopDBusPropertiesInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgFreedesktopDBusPropertiesInterface__QDBusPendingReply(
    QDBusPendingReply<> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
