//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickScrollBarAttached that Python can take functions over in. Every QQuickScrollBarAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScrollBarAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScrollBarAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollBarAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollBarAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollBarAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollBarAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollBarAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickScrollBarAttached : public QQuickScrollBarAttached {
public:
  using QQuickScrollBarAttached::QQuickScrollBarAttached;
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
      CuteQQuickScrollBarAttachedCall0 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall0>(taken[0]);
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
      CuteQQuickScrollBarAttachedCall1 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall1>(taken[1]);
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
      CuteQQuickScrollBarAttachedCall2 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall2>(taken[2]);
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
      CuteQQuickScrollBarAttachedCall3 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall3>(taken[3]);
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
      CuteQQuickScrollBarAttachedCall4 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall4>(taken[4]);
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
      CuteQQuickScrollBarAttachedCall5 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall5>(taken[5]);
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
      CuteQQuickScrollBarAttachedCall6 call = reinterpret_cast<CuteQQuickScrollBarAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickScrollBarAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickScrollBarAttached10metaObjectEv(
    const QQuickScrollBarAttached *self) {
  return self->metaObject();
}

//  QString QQuickScrollBarAttached::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickScrollBarAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScrollBarAttached::tr(s, c, n));
}

//  QQuickScrollBarAttached::QQuickScrollBarAttached(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickScrollBarAttached *ritual_ZN23QQuickScrollBarAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickScrollBarAttached(parent);
}

//  QQuickScrollBarAttached::~QQuickScrollBarAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickScrollBarAttachedD1Ev(QQuickScrollBarAttached *self) {
  delete self;
}

//  QQuickScrollBar *QQuickScrollBarAttached::horizontal() const
extern "C" Q_DECL_EXPORT
QQuickScrollBar *ritual_ZNK23QQuickScrollBarAttached10horizontalEv(
    const QQuickScrollBarAttached *self) {
  return self->horizontal();
}

//  void QQuickScrollBarAttached::setHorizontal(QQuickScrollBar *horizontal)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickScrollBarAttached13setHorizontalEP15QQuickScrollBar(
    QQuickScrollBarAttached *self,
    QQuickScrollBar *horizontal) {
  self->setHorizontal(horizontal);
}

//  QQuickScrollBar *QQuickScrollBarAttached::vertical() const
extern "C" Q_DECL_EXPORT
QQuickScrollBar *ritual_ZNK23QQuickScrollBarAttached8verticalEv(
    const QQuickScrollBarAttached *self) {
  return self->vertical();
}

//  void QQuickScrollBarAttached::setVertical(QQuickScrollBar *vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickScrollBarAttached11setVerticalEP15QQuickScrollBar(
    QQuickScrollBarAttached *self,
    QQuickScrollBar *vertical) {
  self->setVertical(vertical);
}

//  QQuickScrollBarAttachedPrivate *QQuickScrollBarAttached::d_func()
extern "C" Q_DECL_EXPORT
QQuickScrollBarAttachedPrivate *ritual_ZN23QQuickScrollBarAttached6d_funcEv(
    QQuickScrollBarAttached *self) {
  return self->d_func();
}

//  const QQuickScrollBarAttachedPrivate *QQuickScrollBarAttached::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickScrollBarAttachedPrivate *ritual_ZNK23QQuickScrollBarAttached6d_funcEv(
    const QQuickScrollBarAttached *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickScrollBarAttached, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScrollBarAttached(
    QQuickScrollBarAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScrollBarAttached *>(self)->take(key, call);
}
