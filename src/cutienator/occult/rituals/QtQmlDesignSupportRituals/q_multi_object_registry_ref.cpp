//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlDesignSupport/qmultiobjectregistryref.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQmlDesignSupport/QtQmlDesignSupport>
#include <QtQmlDesignSupport/qmultiobjectregistryref.h>
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  Only a class built on QMultiObjectRegistryRef may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMultiObjectRegistryRef : QMultiObjectRegistryRef {
  using QMultiObjectRegistryRef::event;
};

//  A QMultiObjectRegistryRef that Python can take functions over in. Every QMultiObjectRegistryRef
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMultiObjectRegistryRefCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMultiObjectRegistryRefCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMultiObjectRegistryRefCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMultiObjectRegistryRefCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMultiObjectRegistryRefCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMultiObjectRegistryRefCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMultiObjectRegistryRefCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMultiObjectRegistryRef : public QMultiObjectRegistryRef {
public:
  using QMultiObjectRegistryRef::QMultiObjectRegistryRef;
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
  //  bool QMultiObjectRegistryRef::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQMultiObjectRegistryRefCall0 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall0>(taken[0]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QMultiObjectRegistryRef::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQMultiObjectRegistryRefCall1 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall1>(taken[1]);
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
      CuteQMultiObjectRegistryRefCall2 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall2>(taken[2]);
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
      CuteQMultiObjectRegistryRefCall3 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall3>(taken[3]);
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
      CuteQMultiObjectRegistryRefCall4 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall4>(taken[4]);
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
      CuteQMultiObjectRegistryRefCall5 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall5>(taken[5]);
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
      CuteQMultiObjectRegistryRefCall6 call = reinterpret_cast<CuteQMultiObjectRegistryRefCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMultiObjectRegistryRef::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QMultiObjectRegistryRef10metaObjectEv(
    const QMultiObjectRegistryRef *self) {
  return self->metaObject();
}

//  void *QMultiObjectRegistryRef::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QMultiObjectRegistryRef11qt_metacastEPKc(
    QMultiObjectRegistryRef *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QMultiObjectRegistryRef::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QMultiObjectRegistryRef11qt_metacallEN11QMetaObject4CallEiPPv(
    QMultiObjectRegistryRef *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QMultiObjectRegistryRef::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QMultiObjectRegistryRef2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMultiObjectRegistryRef::tr(s, c, n));
}

//  QMultiObjectRegistryRefPrivate *QMultiObjectRegistryRef::d_func()
extern "C" Q_DECL_EXPORT
QMultiObjectRegistryRefPrivate *ritual_ZN23QMultiObjectRegistryRef6d_funcEv(
    QMultiObjectRegistryRef *self) {
  return self->d_func();
}

//  const QMultiObjectRegistryRefPrivate *QMultiObjectRegistryRef::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QMultiObjectRegistryRefPrivate *ritual_ZNK23QMultiObjectRegistryRef6d_funcEv(
    const QMultiObjectRegistryRef *self) {
  return self->d_func();
}

//  QMultiObjectRegistryRef::QMultiObjectRegistryRef(QObject *parent)
extern "C" Q_DECL_EXPORT
QMultiObjectRegistryRef *ritual_ZN23QMultiObjectRegistryRefC1EP7QObject(
    QObject *parent) {
  return new CuteQMultiObjectRegistryRef(parent);
}

//  QMultiObjectRegistryRef::QMultiObjectRegistryRef(QQmlEngine *engine,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QMultiObjectRegistryRef *ritual_ZN23QMultiObjectRegistryRefC1EP10QQmlEngineP7QObject(
    QQmlEngine *engine,
    QObject *parent) {
  return new CuteQMultiObjectRegistryRef(engine, parent);
}

//  QMultiObjectRegistryRef::QMultiObjectRegistryRef(QQmlEngine *engine,
//      const QString &key, QObject *parent)
extern "C" Q_DECL_EXPORT
QMultiObjectRegistryRef *ritual_ZN23QMultiObjectRegistryRefC1EP10QQmlEngineRK7QStringP7QObject(
    QQmlEngine *engine,
    const QString *key,
    QObject *parent) {
  return new CuteQMultiObjectRegistryRef(engine, *key, parent);
}

//  QMultiObjectRegistryRef::~QMultiObjectRegistryRef()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMultiObjectRegistryRefD1Ev(QMultiObjectRegistryRef *self) {
  delete self;
}

//  QQmlListProperty<QObject> QMultiObjectRegistryRef::objects()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN23QMultiObjectRegistryRef7objectsEv(
    QMultiObjectRegistryRef *self) {
  return new QQmlListProperty<QObject>(self->objects());
}

//  QList<QObject *> QMultiObjectRegistryRef::objectsList()
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZN23QMultiObjectRegistryRef11objectsListEv(
    QMultiObjectRegistryRef *self) {
  return new QList<QObject *>(self->objectsList());
}

//  bool QMultiObjectRegistryRef::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QMultiObjectRegistryRef5eventEP6QEvent(
    QMultiObjectRegistryRef *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QMultiObjectRegistryRef::objectsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMultiObjectRegistryRef14objectsChangedEv(
    QMultiObjectRegistryRef *self) {
  self->objectsChanged();
}

//  void QMultiObjectRegistryRef::objectAdded(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMultiObjectRegistryRef11objectAddedEP7QObject(
    QMultiObjectRegistryRef *self,
    QObject *obj) {
  self->objectAdded(obj);
}

//  void QMultiObjectRegistryRef::objectRemoved(QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QMultiObjectRegistryRef13objectRemovedEP7QObject(
    QMultiObjectRegistryRef *self,
    QObject *obj) {
  self->objectRemoved(obj);
}

//  a Python function taken by a CuteQMultiObjectRegistryRef, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMultiObjectRegistryRef(
    QMultiObjectRegistryRef *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMultiObjectRegistryRef *>(self)->take(key, call);
}

//  bool QMultiObjectRegistryRef::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QMultiObjectRegistryRef5eventEP6QEvent(
    QMultiObjectRegistryRef *self,
    QEvent *a0) {
  return static_cast<OwnQMultiObjectRegistryRef *>(self)->OwnQMultiObjectRegistryRef::event(
      a0);
}

//  a QQmlListProperty<QObject> a ritual of QMultiObjectRegistryRef gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMultiObjectRegistryRef__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
