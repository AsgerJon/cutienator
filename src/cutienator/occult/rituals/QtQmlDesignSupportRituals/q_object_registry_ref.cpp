//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlDesignSupport/qobjectregistryref.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#include <QtQmlDesignSupport/qobjectregistryref.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QObjectRegistryRef may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQObjectRegistryRef : QObjectRegistryRef {
  using QObjectRegistryRef::event;
};

//  A QObjectRegistryRef that Python can take functions over in. Every QObjectRegistryRef
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistryRefCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQObjectRegistryRefCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryRefCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryRefCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryRefCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryRefCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQObjectRegistryRefCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQObjectRegistryRef : public QObjectRegistryRef {
public:
  using QObjectRegistryRef::QObjectRegistryRef;
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
  //  bool QObjectRegistryRef::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQObjectRegistryRefCall0 call = reinterpret_cast<CuteQObjectRegistryRefCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QObjectRegistryRef::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQObjectRegistryRefCall1 call = reinterpret_cast<CuteQObjectRegistryRefCall1>(taken[1]);
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
      CuteQObjectRegistryRefCall2 call = reinterpret_cast<CuteQObjectRegistryRefCall2>(taken[2]);
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
      CuteQObjectRegistryRefCall3 call = reinterpret_cast<CuteQObjectRegistryRefCall3>(taken[3]);
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
      CuteQObjectRegistryRefCall4 call = reinterpret_cast<CuteQObjectRegistryRefCall4>(taken[4]);
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
      CuteQObjectRegistryRefCall5 call = reinterpret_cast<CuteQObjectRegistryRefCall5>(taken[5]);
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
      CuteQObjectRegistryRefCall6 call = reinterpret_cast<CuteQObjectRegistryRefCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QObjectRegistryRef::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QObjectRegistryRef10metaObjectEv(
    const QObjectRegistryRef *self) {
  return self->metaObject();
}

//  void *QObjectRegistryRef::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QObjectRegistryRef11qt_metacastEPKc(
    QObjectRegistryRef *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QObjectRegistryRef::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QObjectRegistryRef11qt_metacallEN11QMetaObject4CallEiPPv(
    QObjectRegistryRef *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QObjectRegistryRef::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QObjectRegistryRef2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QObjectRegistryRef::tr(s, c, n));
}

//  QObjectRegistryRefPrivate *QObjectRegistryRef::d_func()
extern "C" Q_DECL_EXPORT
QObjectRegistryRefPrivate *ritual_ZN18QObjectRegistryRef6d_funcEv(
    QObjectRegistryRef *self) {
  return self->d_func();
}

//  const QObjectRegistryRefPrivate *QObjectRegistryRef::d_func() const
extern "C" Q_DECL_EXPORT
const QObjectRegistryRefPrivate *ritual_ZNK18QObjectRegistryRef6d_funcEv(
    const QObjectRegistryRef *self) {
  return self->d_func();
}

//  QObjectRegistryRef::QObjectRegistryRef(QObject *parent)
extern "C" Q_DECL_EXPORT
QObjectRegistryRef *ritual_ZN18QObjectRegistryRefC1EP7QObject(
    QObject *parent) {
  return new CuteQObjectRegistryRef(parent);
}

//  QObjectRegistryRef::QObjectRegistryRef(QQmlEngine *engine, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QObjectRegistryRef *ritual_ZN18QObjectRegistryRefC1EP10QQmlEngineP7QObject(
    QQmlEngine *engine,
    QObject *parent) {
  return new CuteQObjectRegistryRef(engine, parent);
}

//  QObjectRegistryRef::QObjectRegistryRef(QQmlEngine *engine, const QString
//      &key, QObject *parent)
extern "C" Q_DECL_EXPORT
QObjectRegistryRef *ritual_ZN18QObjectRegistryRefC1EP10QQmlEngineRK7QStringP7QObject(
    QQmlEngine *engine,
    const QString *key,
    QObject *parent) {
  return new CuteQObjectRegistryRef(engine, *key, parent);
}

//  QObjectRegistryRef::~QObjectRegistryRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QObjectRegistryRefD1Ev(QObjectRegistryRef *self) {
  delete self;
}

//  QObject *QObjectRegistryRef::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK18QObjectRegistryRef6objectEv(
    const QObjectRegistryRef *self) {
  return self->object();
}

//  bool QObjectRegistryRef::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QObjectRegistryRef5eventEP6QEvent(
    QObjectRegistryRef *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QObjectRegistryRef::objectChanged(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QObjectRegistryRef13objectChangedEP7QObject(
    QObjectRegistryRef *self,
    QObject *object) {
  self->objectChanged(object);
}

//  a Python function taken by a CuteQObjectRegistryRef, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QObjectRegistryRef(
    QObjectRegistryRef *self,
    const char *key,
    void *call) {
  return static_cast<CuteQObjectRegistryRef *>(self)->take(key, call);
}

//  bool QObjectRegistryRef::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QObjectRegistryRef5eventEP6QEvent(
    QObjectRegistryRef *self,
    QEvent *a0) {
  return static_cast<OwnQObjectRegistryRef *>(self)->OwnQObjectRegistryRef::event(
      a0);
}
