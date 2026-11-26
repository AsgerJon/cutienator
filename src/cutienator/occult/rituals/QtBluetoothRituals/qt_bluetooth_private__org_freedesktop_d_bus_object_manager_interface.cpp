//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/objectmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/objectmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtDBus/QDBusObjectPath>
#include <QtDBus/QDBusPendingReply>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/objectmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/bluez/objectmanager.cpp, line 25, as _ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterfaceD1Ev
namespace QtBluetoothPrivate {
inline OrgFreedesktopDBusObjectManagerInterface::~OrgFreedesktopDBusObjectManagerInterface()
{
}
}  // namespace QtBluetoothPrivate
//  -----------------------------------------------------------------------

//  A QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface that Python can take functions over in. Every QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall0)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_DBUS)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall1)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_DBUS)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterface : public QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface {
public:
  using QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::OrgFreedesktopDBusObjectManagerInterface;
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterfaceCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInt
//      erface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterface10metaObjectEv(
    const QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::qt_me
//      tacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterface11qt_metacastEPKc(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::qt_meta
//      call(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterface11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const char *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface:
//      :staticInterfaceName()
extern "C" Q_DECL_EXPORT
const char *ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterface19staticInterfaceNameEv() {
  return QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::staticInterfaceName();
}

//  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::~OrgFreedes
//      ktopDBusObjectManagerInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterfaceD1Ev(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self) {
  delete self;
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::Interf
//      acesAdded(const QDBusObjectPath &object_path, InterfaceList
//      interfaces_and_properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterface15InterfacesAddedERK15QDBusObjectPath4QMapI7QStringS4_IS5_8QVariantEE(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self,
    const QDBusObjectPath *object_path,
    const InterfaceList *interfaces_and_properties) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "InterfacesAdded(const QDBusObjectPath &,InterfaceList)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "InterfacesAdded(const QDBusObjectPath &,InterfaceList)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(object_path)),
      const_cast<void *>(static_cast<const void *>(interfaces_and_properties)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface::Interf
//      acesRemoved(const QDBusObjectPath &object_path, const QStringList
//      &interfaces)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate40OrgFreedesktopDBusObjectManagerInterface17InterfacesRemovedERK15QDBusObjectPathRK5QListI7QStringE(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self,
    const QDBusObjectPath *object_path,
    const QList<QString> *interfaces) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "InterfacesRemoved(const QDBusObjectPath &,const QStringList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "InterfacesRemoved(const QDBusObjectPath &,const QStringList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(object_path)),
      const_cast<void *>(static_cast<const void *>(interfaces)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a
//      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterface(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterface *>(self)->take(key, call);
}

//  a QDBusPendingReply<ManagedObjectList> a ritual of
//      QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerInterface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgFreedesktopDBusObjectManagerInterface__QDBusPendingReply_ManagedObjectList(
    QDBusPendingReply<ManagedObjectList> *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
