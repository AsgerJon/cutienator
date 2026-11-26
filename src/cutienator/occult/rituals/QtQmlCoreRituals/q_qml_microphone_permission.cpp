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

//  A QQmlMicrophonePermission that Python can take functions over in. Every QQmlMicrophonePermission
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlMicrophonePermissionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlMicrophonePermissionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlMicrophonePermissionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlMicrophonePermissionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlMicrophonePermissionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlMicrophonePermissionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlMicrophonePermissionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlMicrophonePermission : public QQmlMicrophonePermission {
public:
  using QQmlMicrophonePermission::QQmlMicrophonePermission;
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
      CuteQQmlMicrophonePermissionCall0 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall0>(taken[0]);
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
      CuteQQmlMicrophonePermissionCall1 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall1>(taken[1]);
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
      CuteQQmlMicrophonePermissionCall2 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall2>(taken[2]);
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
      CuteQQmlMicrophonePermissionCall3 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall3>(taken[3]);
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
      CuteQQmlMicrophonePermissionCall4 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall4>(taken[4]);
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
      CuteQQmlMicrophonePermissionCall5 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall5>(taken[5]);
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
      CuteQQmlMicrophonePermissionCall6 call = reinterpret_cast<CuteQQmlMicrophonePermissionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlMicrophonePermission::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQmlMicrophonePermission10metaObjectEv(
    const QQmlMicrophonePermission *self) {
  return self->metaObject();
}

//  void *QQmlMicrophonePermission::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQmlMicrophonePermission11qt_metacastEPKc(
    QQmlMicrophonePermission *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlMicrophonePermission::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQmlMicrophonePermission11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlMicrophonePermission *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt::PermissionStatus QQmlMicrophonePermission::status() const
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZNK24QQmlMicrophonePermission6statusEv(
    const QQmlMicrophonePermission *self) {
  return self->status();
}

//  a Python function taken by a CuteQQmlMicrophonePermission, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlMicrophonePermission(
    QQmlMicrophonePermission *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlMicrophonePermission *>(self)->take(key, call);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
