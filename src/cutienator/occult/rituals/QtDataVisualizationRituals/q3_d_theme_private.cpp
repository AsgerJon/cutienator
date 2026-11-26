//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dtheme_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/q3dtheme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Q3DThemePrivate that Python can take functions over in. Every Q3DThemePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DThemePrivateCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DThemePrivateCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemePrivateCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemePrivateCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemePrivateCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemePrivateCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DThemePrivateCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DThemePrivate : public Q3DThemePrivate {
public:
  using Q3DThemePrivate::Q3DThemePrivate;
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
      CuteQ3DThemePrivateCall0 call = reinterpret_cast<CuteQ3DThemePrivateCall0>(taken[0]);
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
      CuteQ3DThemePrivateCall1 call = reinterpret_cast<CuteQ3DThemePrivateCall1>(taken[1]);
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
      CuteQ3DThemePrivateCall2 call = reinterpret_cast<CuteQ3DThemePrivateCall2>(taken[2]);
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
      CuteQ3DThemePrivateCall3 call = reinterpret_cast<CuteQ3DThemePrivateCall3>(taken[3]);
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
      CuteQ3DThemePrivateCall4 call = reinterpret_cast<CuteQ3DThemePrivateCall4>(taken[4]);
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
      CuteQ3DThemePrivateCall5 call = reinterpret_cast<CuteQ3DThemePrivateCall5>(taken[5]);
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
      CuteQ3DThemePrivateCall6 call = reinterpret_cast<CuteQ3DThemePrivateCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DThemePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15Q3DThemePrivate10metaObjectEv(
    const Q3DThemePrivate *self) {
  return self->metaObject();
}

//  void *Q3DThemePrivate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15Q3DThemePrivate11qt_metacastEPKc(
    Q3DThemePrivate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Q3DThemePrivate::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15Q3DThemePrivate11qt_metacallEN11QMetaObject4CallEiPPv(
    Q3DThemePrivate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Q3DThemePrivate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15Q3DThemePrivate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DThemePrivate::tr(s, c, n));
}

//  Q3DThemePrivate::Q3DThemePrivate(Q3DTheme *q)
extern "C" Q_DECL_EXPORT
Q3DThemePrivate *ritual_ZN15Q3DThemePrivateC1EP8Q3DTheme(Q3DTheme *q) {
  return new CuteQ3DThemePrivate(q);
}

//  Q3DThemePrivate::~Q3DThemePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DThemePrivateD1Ev(Q3DThemePrivate *self) {
  delete self;
}

//  void Q3DThemePrivate::resetDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DThemePrivate14resetDirtyBitsEv(Q3DThemePrivate *self) {
  self->resetDirtyBits();
}

//  bool Q3DThemePrivate::sync(Q3DThemePrivate &other)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15Q3DThemePrivate4syncERS_(
    Q3DThemePrivate *self,
    Q3DThemePrivate *other) {
  return self->sync(*other);
}

//  bool Q3DThemePrivate::isDefaultTheme()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15Q3DThemePrivate14isDefaultThemeEv(Q3DThemePrivate *self) {
  return self->isDefaultTheme();
}

//  void Q3DThemePrivate::setDefaultTheme(bool isDefault)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DThemePrivate15setDefaultThemeEb(
    Q3DThemePrivate *self,
    bool isDefault) {
  self->setDefaultTheme(isDefault);
}

//  bool Q3DThemePrivate::isForcePredefinedType()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15Q3DThemePrivate21isForcePredefinedTypeEv(
    Q3DThemePrivate *self) {
  return self->isForcePredefinedType();
}

//  void Q3DThemePrivate::setForcePredefinedType(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DThemePrivate22setForcePredefinedTypeEb(
    Q3DThemePrivate *self,
    bool enable) {
  self->setForcePredefinedType(enable);
}

//  void Q3DThemePrivate::needRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN15Q3DThemePrivate10needRenderEv(Q3DThemePrivate *self) {
  self->needRender();
}

//  a Python function taken by a CuteQ3DThemePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DThemePrivate(
    Q3DThemePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQ3DThemePrivate *>(self)->take(key, call);
}
