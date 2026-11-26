//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlLocalStorage/6.12.0/QtQmlLocalStorage/private/qqmllocalstorage_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlLocalStorage/6.12.0/QtQmlLocalStorage/private/qqmllocalstorageglobal_p.h>
#include <QtQmlLocalStorage/QtQmlLocalStorage>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlLocalStorage/6.12.0/QtQmlLocalStorage/private/qqmllocalstorage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlLocalStorage that Python can take functions over in. Every QQmlLocalStorage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlLocalStorageCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlLocalStorageCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLocalStorageCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLocalStorageCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLocalStorageCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLocalStorageCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlLocalStorageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlLocalStorage : public QQmlLocalStorage {
public:
  using QQmlLocalStorage::QQmlLocalStorage;
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
      CuteQQmlLocalStorageCall0 call = reinterpret_cast<CuteQQmlLocalStorageCall0>(taken[0]);
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
      CuteQQmlLocalStorageCall1 call = reinterpret_cast<CuteQQmlLocalStorageCall1>(taken[1]);
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
      CuteQQmlLocalStorageCall2 call = reinterpret_cast<CuteQQmlLocalStorageCall2>(taken[2]);
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
      CuteQQmlLocalStorageCall3 call = reinterpret_cast<CuteQQmlLocalStorageCall3>(taken[3]);
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
      CuteQQmlLocalStorageCall4 call = reinterpret_cast<CuteQQmlLocalStorageCall4>(taken[4]);
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
      CuteQQmlLocalStorageCall5 call = reinterpret_cast<CuteQQmlLocalStorageCall5>(taken[5]);
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
      CuteQQmlLocalStorageCall6 call = reinterpret_cast<CuteQQmlLocalStorageCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlLocalStorage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQmlLocalStorage10metaObjectEv(
    const QQmlLocalStorage *self) {
  return self->metaObject();
}

//  void *QQmlLocalStorage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQmlLocalStorage11qt_metacastEPKc(
    QQmlLocalStorage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlLocalStorage::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQmlLocalStorage11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlLocalStorage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlLocalStorage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQmlLocalStorage2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlLocalStorage::tr(s, c, n));
}

//  void QQmlLocalStorage::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlLocalStorage22qt_qmlMarker_singletonEv(
    QQmlLocalStorage *self) {
  self->qt_qmlMarker_singleton();
}

//  QQmlLocalStorage::QQmlLocalStorage(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlLocalStorage *ritual_ZN16QQmlLocalStorageC1EP7QObject(QObject *parent) {
  return new CuteQQmlLocalStorage(parent);
}

//  QQmlLocalStorage::~QQmlLocalStorage()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlLocalStorageD1Ev(QQmlLocalStorage *self) {
  delete self;
}

//  void QQmlLocalStorage::openDatabaseSync(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQmlLocalStorage16openDatabaseSyncEP14QQmlV4Function(
    QQmlLocalStorage *self,
    QQmlV4FunctionPtr args) {
  self->openDatabaseSync(args);
}

//  a Python function taken by a CuteQQmlLocalStorage, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlLocalStorage(
    QQmlLocalStorage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlLocalStorage *>(self)->take(key, call);
}
