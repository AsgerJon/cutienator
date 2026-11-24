//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickscrollindicator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollindicator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickScrollIndicatorAttached that Python can take functions over in. Every QQuickScrollIndicatorAttached
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScrollIndicatorAttachedCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickScrollIndicatorAttachedCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollIndicatorAttachedCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollIndicatorAttachedCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollIndicatorAttachedCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollIndicatorAttachedCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickScrollIndicatorAttachedCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickScrollIndicatorAttached : public QQuickScrollIndicatorAttached {
public:
  using QQuickScrollIndicatorAttached::QQuickScrollIndicatorAttached;
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
      CuteQQuickScrollIndicatorAttachedCall0 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall0>(taken[0]);
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
      CuteQQuickScrollIndicatorAttachedCall1 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall1>(taken[1]);
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
      CuteQQuickScrollIndicatorAttachedCall2 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall2>(taken[2]);
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
      CuteQQuickScrollIndicatorAttachedCall3 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall3>(taken[3]);
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
      CuteQQuickScrollIndicatorAttachedCall4 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall4>(taken[4]);
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
      CuteQQuickScrollIndicatorAttachedCall5 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall5>(taken[5]);
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
      CuteQQuickScrollIndicatorAttachedCall6 call = reinterpret_cast<CuteQQuickScrollIndicatorAttachedCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickScrollIndicatorAttached::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickScrollIndicatorAttached10metaObjectEv(
    const QQuickScrollIndicatorAttached *self) {
  return self->metaObject();
}

//  QString QQuickScrollIndicatorAttached::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuickScrollIndicatorAttached2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickScrollIndicatorAttached::tr(s, c, n));
}

//  QQuickScrollIndicatorAttached::QQuickScrollIndicatorAttached(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickScrollIndicatorAttached *ritual_ZN29QQuickScrollIndicatorAttachedC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickScrollIndicatorAttached(parent);
}

//  QQuickScrollIndicatorAttached::~QQuickScrollIndicatorAttached()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickScrollIndicatorAttachedD1Ev(
    QQuickScrollIndicatorAttached *self) {
  delete self;
}

//  QQuickScrollIndicator *QQuickScrollIndicatorAttached::horizontal() const
extern "C" Q_DECL_EXPORT
QQuickScrollIndicator *ritual_ZNK29QQuickScrollIndicatorAttached10horizontalEv(
    const QQuickScrollIndicatorAttached *self) {
  return self->horizontal();
}

//  void QQuickScrollIndicatorAttached::setHorizontal(QQuickScrollIndicator
//      *horizontal)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickScrollIndicatorAttached13setHorizontalEP21QQuickScrollIndicator(
    QQuickScrollIndicatorAttached *self,
    QQuickScrollIndicator *horizontal) {
  self->setHorizontal(horizontal);
}

//  QQuickScrollIndicator *QQuickScrollIndicatorAttached::vertical() const
extern "C" Q_DECL_EXPORT
QQuickScrollIndicator *ritual_ZNK29QQuickScrollIndicatorAttached8verticalEv(
    const QQuickScrollIndicatorAttached *self) {
  return self->vertical();
}

//  void QQuickScrollIndicatorAttached::setVertical(QQuickScrollIndicator
//      *vertical)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickScrollIndicatorAttached11setVerticalEP21QQuickScrollIndicator(
    QQuickScrollIndicatorAttached *self,
    QQuickScrollIndicator *vertical) {
  self->setVertical(vertical);
}

//  a Python function taken by a CuteQQuickScrollIndicatorAttached, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScrollIndicatorAttached(
    QQuickScrollIndicatorAttached *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScrollIndicatorAttached *>(self)->take(key, call);
}
