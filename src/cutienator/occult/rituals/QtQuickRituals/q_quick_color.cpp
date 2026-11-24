//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcolor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcolor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickColor that Python can take functions over in. Every QQuickColor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickColorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickColorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickColorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickColor : public QQuickColor {
public:
  using QQuickColor::QQuickColor;
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
      CuteQQuickColorCall0 call = reinterpret_cast<CuteQQuickColorCall0>(taken[0]);
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
      CuteQQuickColorCall1 call = reinterpret_cast<CuteQQuickColorCall1>(taken[1]);
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
      CuteQQuickColorCall2 call = reinterpret_cast<CuteQQuickColorCall2>(taken[2]);
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
      CuteQQuickColorCall3 call = reinterpret_cast<CuteQQuickColorCall3>(taken[3]);
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
      CuteQQuickColorCall4 call = reinterpret_cast<CuteQQuickColorCall4>(taken[4]);
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
      CuteQQuickColorCall5 call = reinterpret_cast<CuteQQuickColorCall5>(taken[5]);
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
      CuteQQuickColorCall6 call = reinterpret_cast<CuteQQuickColorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickColor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QQuickColor10metaObjectEv(
    const QQuickColor *self) {
  return self->metaObject();
}

//  QString QQuickColor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QQuickColor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickColor::tr(s, c, n));
}

//  void QQuickColor::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuickColor22qt_qmlMarker_singletonEv(QQuickColor *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuickColor::QQuickColor(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickColor *ritual_ZN11QQuickColorC1EP7QObject(QObject *parent) {
  return new CuteQQuickColor(parent);
}

//  QColor QQuickColor::rgba(double r, double g, double b, double a) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor4rgbaEdddd(
    const QQuickColor *self,
    double r,
    double g,
    double b,
    double a) {
  return new QColor(self->rgba(r, g, b, a));
}

//  QColor QQuickColor::hsla(double h, double s, double l, double a) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor4hslaEdddd(
    const QQuickColor *self,
    double h,
    double s,
    double l,
    double a) {
  return new QColor(self->hsla(h, s, l, a));
}

//  QColor QQuickColor::hsva(double h, double s, double v, double a) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor4hsvaEdddd(
    const QQuickColor *self,
    double h,
    double s,
    double v,
    double a) {
  return new QColor(self->hsva(h, s, v, a));
}

//  QColor QQuickColor::fromString(const QString &name) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor10fromStringERK7QString(
    const QQuickColor *self,
    const QString *name) {
  return new QColor(self->fromString(*name));
}

//  bool QQuickColor::equal(const QColor &lhs, const QColor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuickColor5equalERK6QColorS2_(
    const QQuickColor *self,
    const QColor *lhs,
    const QColor *rhs) {
  return self->equal(*lhs, *rhs);
}

//  QColor QQuickColor::transparent(const QColor &color, qreal opacity) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor11transparentERK6QColord(
    const QQuickColor *self,
    const QColor *color,
    qreal opacity) {
  return new QColor(self->transparent(*color, opacity));
}

//  QColor QQuickColor::blend(const QColor &a, const QColor &b, qreal factor)
//      const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor5blendERK6QColorS2_d(
    const QQuickColor *self,
    const QColor *a,
    const QColor *b,
    qreal factor) {
  return new QColor(self->blend(*a, *b, factor));
}

//  QColor QQuickColor::darker(const QColor &baseColor, double factor) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor6darkerERK6QColord(
    const QQuickColor *self,
    const QColor *baseColor,
    double factor) {
  return new QColor(self->darker(*baseColor, factor));
}

//  QColor QQuickColor::lighter(const QColor &baseColor, double factor) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor7lighterERK6QColord(
    const QQuickColor *self,
    const QColor *baseColor,
    double factor) {
  return new QColor(self->lighter(*baseColor, factor));
}

//  QColor QQuickColor::tint(const QColor &baseColor, const QColor
//      &tintColor) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK11QQuickColor4tintERK6QColorS2_(
    const QQuickColor *self,
    const QColor *baseColor,
    const QColor *tintColor) {
  return new QColor(self->tint(*baseColor, *tintColor));
}

//  a Python function taken by a CuteQQuickColor, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickColor(
    QQuickColor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickColor *>(self)->take(key, call);
}
