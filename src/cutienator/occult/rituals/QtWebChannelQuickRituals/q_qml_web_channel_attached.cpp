//  Written by dev_tooling.RitualGenerator from the records of QtWebChannelQu
//  ick/6.12.0/QtWebChannelQuick/private/qqmlwebchannelattached_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebChannelQuick/QtWebChannelQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebChannelQuick/6.12.0/QtWebChannelQuick/private/qqmlwebchannelattached_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlWebChannelAttached that Python can take functions over in. Every QQmlWebChannelAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlWebChannelAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlWebChannelAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlWebChannelAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlWebChannelAttached : public QQmlWebChannelAttached {
public:
  using QQmlWebChannelAttached::QQmlWebChannelAttached;
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
      CuteQQmlWebChannelAttachedCall0 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall0>(taken[0]);
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
      CuteQQmlWebChannelAttachedCall1 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall1>(taken[1]);
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
      CuteQQmlWebChannelAttachedCall2 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall2>(taken[2]);
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
      CuteQQmlWebChannelAttachedCall3 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall3>(taken[3]);
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
      CuteQQmlWebChannelAttachedCall4 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall4>(taken[4]);
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
      CuteQQmlWebChannelAttachedCall5 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall5>(taken[5]);
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
      CuteQQmlWebChannelAttachedCall6 call = reinterpret_cast<CuteQQmlWebChannelAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlWebChannelAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQmlWebChannelAttached10metaObjectEv(
    const QQmlWebChannelAttached *self) {
  return self->metaObject();
}

//  void *QQmlWebChannelAttached::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQmlWebChannelAttached11qt_metacastEPKc(
    QQmlWebChannelAttached *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlWebChannelAttached::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQmlWebChannelAttached11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlWebChannelAttached *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlWebChannelAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQmlWebChannelAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlWebChannelAttached::tr(s, c, n));
}

//  void QQmlWebChannelAttached::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlWebChannelAttached22qt_qmlMarker_anonymousEv(
    QQmlWebChannelAttached *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQmlWebChannelAttached::QQmlWebChannelAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlWebChannelAttached *ritual_ZN22QQmlWebChannelAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQmlWebChannelAttached(parent);
}

//  QQmlWebChannelAttached::~QQmlWebChannelAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlWebChannelAttachedD1Ev(QQmlWebChannelAttached *self) {
  delete self;
}

//  QString QQmlWebChannelAttached::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQmlWebChannelAttached2idEv(
    const QQmlWebChannelAttached *self) {
  return new QString(self->id());
}

//  void QQmlWebChannelAttached::setId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlWebChannelAttached5setIdERK7QString(
    QQmlWebChannelAttached *self,
    const QString *id) {
  self->setId(*id);
}

//  void QQmlWebChannelAttached::idChanged(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlWebChannelAttached9idChangedERK7QString(
    QQmlWebChannelAttached *self,
    const QString *id) {
  self->idChanged(*id);
}

//  a Python function taken by a CuteQQmlWebChannelAttached, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlWebChannelAttached(
    QQmlWebChannelAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlWebChannelAttached *>(self)->take(key, call);
}
