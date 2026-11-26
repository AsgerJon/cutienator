//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlcomponentattached_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlcomponentattached_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlComponentAttached that Python can take functions over in. Every QQmlComponentAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlComponentAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlComponentAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlComponentAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlComponentAttached : public QQmlComponentAttached {
public:
  using QQmlComponentAttached::QQmlComponentAttached;
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
      CuteQQmlComponentAttachedCall0 call = reinterpret_cast<CuteQQmlComponentAttachedCall0>(taken[0]);
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
      CuteQQmlComponentAttachedCall1 call = reinterpret_cast<CuteQQmlComponentAttachedCall1>(taken[1]);
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
      CuteQQmlComponentAttachedCall2 call = reinterpret_cast<CuteQQmlComponentAttachedCall2>(taken[2]);
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
      CuteQQmlComponentAttachedCall3 call = reinterpret_cast<CuteQQmlComponentAttachedCall3>(taken[3]);
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
      CuteQQmlComponentAttachedCall4 call = reinterpret_cast<CuteQQmlComponentAttachedCall4>(taken[4]);
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
      CuteQQmlComponentAttachedCall5 call = reinterpret_cast<CuteQQmlComponentAttachedCall5>(taken[5]);
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
      CuteQQmlComponentAttachedCall6 call = reinterpret_cast<CuteQQmlComponentAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlComponentAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQmlComponentAttached10metaObjectEv(
    const QQmlComponentAttached *self) {
  return self->metaObject();
}

//  void *QQmlComponentAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQmlComponentAttached11qt_metacastEPKc(
    QQmlComponentAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlComponentAttached::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQmlComponentAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlComponentAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlComponentAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQmlComponentAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlComponentAttached::tr(s, c, n));
}

//  QQmlComponentAttached::QQmlComponentAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlComponentAttached *ritual_ZN21QQmlComponentAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlComponentAttached(parent);
}

//  QQmlComponentAttached::~QQmlComponentAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlComponentAttachedD1Ev(QQmlComponentAttached *self) {
  delete self;
}

//  void QQmlComponentAttached::insertIntoList(QQmlComponentAttached
//      **listHead)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlComponentAttached14insertIntoListEPPS_(
    QQmlComponentAttached *self,
    QQmlComponentAttached **listHead) {
  self->insertIntoList(listHead);
}

//  void QQmlComponentAttached::removeFromList()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlComponentAttached14removeFromListEv(
    QQmlComponentAttached *self) {
  self->removeFromList();
}

//  QQmlComponentAttached *QQmlComponentAttached::next() const
extern "C" Q_DECL_EXPORT
QQmlComponentAttached *ritual_ZNK21QQmlComponentAttached4nextEv(
    const QQmlComponentAttached *self) {
  return self->next();
}

//  void QQmlComponentAttached::completed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlComponentAttached9completedEv(
    QQmlComponentAttached *self) {
  self->completed();
}

//  void QQmlComponentAttached::destruction()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlComponentAttached11destructionEv(
    QQmlComponentAttached *self) {
  self->destruction();
}

//  a Python function taken by a CuteQQmlComponentAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlComponentAttached(
    QQmlComponentAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlComponentAttached *>(self)->take(key, call);
}
