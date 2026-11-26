//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCore/6.12.0/QtQmlCore/private/qqmlpermissions_p.h, Qt 6.12.0.
//  Changes made here are lost.
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
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlContactsPermission that Python can take functions over in. Every QQmlContactsPermission
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlContactsPermissionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlContactsPermissionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContactsPermissionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContactsPermissionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContactsPermissionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContactsPermissionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlContactsPermissionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlContactsPermission : public QQmlContactsPermission {
public:
  using QQmlContactsPermission::QQmlContactsPermission;
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
      CuteQQmlContactsPermissionCall0 call = reinterpret_cast<CuteQQmlContactsPermissionCall0>(taken[0]);
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
      CuteQQmlContactsPermissionCall1 call = reinterpret_cast<CuteQQmlContactsPermissionCall1>(taken[1]);
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
      CuteQQmlContactsPermissionCall2 call = reinterpret_cast<CuteQQmlContactsPermissionCall2>(taken[2]);
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
      CuteQQmlContactsPermissionCall3 call = reinterpret_cast<CuteQQmlContactsPermissionCall3>(taken[3]);
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
      CuteQQmlContactsPermissionCall4 call = reinterpret_cast<CuteQQmlContactsPermissionCall4>(taken[4]);
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
      CuteQQmlContactsPermissionCall5 call = reinterpret_cast<CuteQQmlContactsPermissionCall5>(taken[5]);
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
      CuteQQmlContactsPermissionCall6 call = reinterpret_cast<CuteQQmlContactsPermissionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlContactsPermission::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlContactsPermission10metaObjectEv(
    const QQmlContactsPermission *self) {
  return self->metaObject();
}

//  void *QQmlContactsPermission::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQmlContactsPermission11qt_metacastEPKc(
    QQmlContactsPermission *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlContactsPermission::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlContactsPermission11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlContactsPermission *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt::PermissionStatus QQmlContactsPermission::status() const
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZNK22QQmlContactsPermission6statusEv(
    const QQmlContactsPermission *self) {
  return self->status();
}

//  const QMetaObject *QQmlContactsPermission::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN22QQmlContactsPermission20qmlExtendedNamespaceEv() {
  return QQmlContactsPermission::qmlExtendedNamespace();
}

//  void QQmlContactsPermission::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlContactsPermission30qt_qmlMarker_extendedNamespaceEv(
    QQmlContactsPermission *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QContactsPermission::AccessMode QQmlContactsPermission::accessMode()
//      const
extern "C" Q_DECL_EXPORT
QContactsPermission::AccessMode ritual_ZNK22QQmlContactsPermission10accessModeEv(
    const QQmlContactsPermission *self) {
  return self->accessMode();
}

//  a Python function taken by a CuteQQmlContactsPermission, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlContactsPermission(
    QQmlContactsPermission *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlContactsPermission *>(self)->take(key, call);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
