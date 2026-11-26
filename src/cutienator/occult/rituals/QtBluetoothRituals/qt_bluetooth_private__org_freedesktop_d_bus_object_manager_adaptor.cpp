//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/objectmanageradaptor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/objectmanageradaptor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDBus/qdbusextratypes.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtDBus/QDBusObjectPath>

//  A QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor that Python can take functions over in. Every QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptor : public QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor {
public:
  using QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::OrgFreedesktopDBusObjectManagerAdaptor;
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall0 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall0>(taken[0]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall1 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall1>(taken[1]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall2 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall2>(taken[2]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall3 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall3>(taken[3]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall4 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall4>(taken[4]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall5 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall5>(taken[5]);
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
      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall6 call = reinterpret_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject
//      *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::metaObje
//      ct() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdaptor10metaObjectEv(
    const QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self) {
  return self->metaObject();
}

//  void *QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::qt_meta
//      cast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdaptor11qt_metacastEPKc(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::qt_metaca
//      ll(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdaptor11qt_metacallEN11QMetaObject4CallEiPPv(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::~OrgFreedeskt
//      opDBusObjectManagerAdaptor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdaptorD1Ev(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self) {
  delete self;
}

//  void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::Interfac
//      esAdded(const QDBusObjectPath &object_path, InterfaceList
//      interfaces_and_properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdaptor15InterfacesAddedERK15QDBusObjectPath4QMapI7QStringS4_IS5_8QVariantEE(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self,
    const QDBusObjectPath *object_path,
    const InterfaceList *interfaces_and_properties) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor")) {
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

//  void QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor::Interfac
//      esRemoved(const QDBusObjectPath &object_path, const QStringList
//      &interfaces)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QtBluetoothPrivate38OrgFreedesktopDBusObjectManagerAdaptor17InterfacesRemovedERK15QDBusObjectPathRK5QListI7QStringE(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self,
    const QDBusObjectPath *object_path,
    const QList<QString> *interfaces) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor")) {
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
//      CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptor, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptor(
    QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptor *>(self)->take(key, call);
}

//  a ManagedObjectList a ritual of
//      QtBluetoothPrivate::OrgFreedesktopDBusObjectManagerAdaptor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtBluetoothPrivate_OrgFreedesktopDBusObjectManagerAdaptor__ManagedObjectList(
    ManagedObjectList *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
