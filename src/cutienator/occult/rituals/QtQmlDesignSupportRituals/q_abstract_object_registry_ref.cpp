//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlDesignSupport/qabstractobjectregistryref.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#include <QtQmlDesignSupport/qabstractobjectregistryref.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QAbstractObjectRegistryRef may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAbstractObjectRegistryRef : QAbstractObjectRegistryRef {
  using QAbstractObjectRegistryRef::event;
};

//  A QAbstractObjectRegistryRef that Python can take functions over in. Every QAbstractObjectRegistryRef
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractObjectRegistryRefCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractObjectRegistryRefCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractObjectRegistryRefCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractObjectRegistryRefCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractObjectRegistryRefCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractObjectRegistryRefCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractObjectRegistryRefCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractObjectRegistryRef : public QAbstractObjectRegistryRef {
public:
  using QAbstractObjectRegistryRef::QAbstractObjectRegistryRef;
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
  //  bool QAbstractObjectRegistryRef::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractObjectRegistryRefCall0 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QAbstractObjectRegistryRef::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractObjectRegistryRefCall1 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall1>(taken[1]);
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
      CuteQAbstractObjectRegistryRefCall2 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall2>(taken[2]);
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
      CuteQAbstractObjectRegistryRefCall3 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall3>(taken[3]);
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
      CuteQAbstractObjectRegistryRefCall4 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall4>(taken[4]);
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
      CuteQAbstractObjectRegistryRefCall5 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall5>(taken[5]);
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
      CuteQAbstractObjectRegistryRefCall6 call = reinterpret_cast<CuteQAbstractObjectRegistryRefCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractObjectRegistryRef::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QAbstractObjectRegistryRef10metaObjectEv(
    const QAbstractObjectRegistryRef *self) {
  return self->metaObject();
}

//  QString QAbstractObjectRegistryRef::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAbstractObjectRegistryRef2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractObjectRegistryRef::tr(s, c, n));
}

//  QAbstractObjectRegistryRefPrivate *QAbstractObjectRegistryRef::d_func()
extern "C" Q_DECL_EXPORT
QAbstractObjectRegistryRefPrivate *ritual_ZN26QAbstractObjectRegistryRef6d_funcEv(
    QAbstractObjectRegistryRef *self) {
  return self->d_func();
}

//  const QAbstractObjectRegistryRefPrivate
//      *QAbstractObjectRegistryRef::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractObjectRegistryRefPrivate *ritual_ZNK26QAbstractObjectRegistryRef6d_funcEv(
    const QAbstractObjectRegistryRef *self) {
  return self->d_func();
}

//  void QAbstractObjectRegistryRef::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractObjectRegistryRef24qt_qmlMarker_uncreatableEv(
    QAbstractObjectRegistryRef *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QAbstractObjectRegistryRef::~QAbstractObjectRegistryRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractObjectRegistryRefD1Ev(
    QAbstractObjectRegistryRef *self) {
  delete self;
}

//  QString QAbstractObjectRegistryRef::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAbstractObjectRegistryRef3keyEv(
    const QAbstractObjectRegistryRef *self) {
  return new QString(self->key());
}

//  void QAbstractObjectRegistryRef::setKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractObjectRegistryRef6setKeyERK7QString(
    QAbstractObjectRegistryRef *self,
    const QString *key) {
  self->setKey(*key);
}

//  bool QAbstractObjectRegistryRef::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractObjectRegistryRef5eventEP6QEvent(
    QAbstractObjectRegistryRef *self,
    QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQAbstractObjectRegistryRef, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractObjectRegistryRef(
    QAbstractObjectRegistryRef *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractObjectRegistryRef *>(self)->take(key, call);
}

//  bool QAbstractObjectRegistryRef::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QAbstractObjectRegistryRef5eventEP6QEvent(
    QAbstractObjectRegistryRef *self,
    QEvent *a0) {
  return static_cast<OwnQAbstractObjectRegistryRef *>(self)->OwnQAbstractObjectRegistryRef::event(
      a0);
}
