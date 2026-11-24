//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticleextruder_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticleextruder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickParticleExtruder that Python can take functions over in. Every QQuickParticleExtruder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPointF * (*CuteQQuickParticleExtruderCall0)(const void *, const QRectF *, int *);
typedef bool (*CuteQQuickParticleExtruderCall1)(const void *, const QRectF *, const QPointF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticleExtruderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickParticleExtruderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleExtruderCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleExtruderCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleExtruderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleExtruderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickParticleExtruderCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickParticleExtruder : public QQuickParticleExtruder {
public:
  using QQuickParticleExtruder::QQuickParticleExtruder;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickParticleExtruder7extrudeERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QQuickParticleExtruder8containsERK6QRectFRK7QPointF")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QPointF QQuickParticleExtruder::extrude(const QRectF &a0)
  QPointF extrude(const QRectF &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall0 call = reinterpret_cast<CuteQQuickParticleExtruderCall0>(taken[0]);
      const QPointF * given = call(this, &a0, &handled);
      if (handled && given) return *given;
    }
    return QQuickParticleExtruder::extrude(a0);
  }

  //  bool QQuickParticleExtruder::contains(const QRectF &bounds, const
  //      QPointF &point)
  bool contains(const QRectF &bounds, const QPointF &point) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall1 call = reinterpret_cast<CuteQQuickParticleExtruderCall1>(taken[1]);
      bool given = call(this, &bounds, &point, &handled);
      if (handled) return given;
    }
    return QQuickParticleExtruder::contains(bounds, point);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall2 call = reinterpret_cast<CuteQQuickParticleExtruderCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall3 call = reinterpret_cast<CuteQQuickParticleExtruderCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall4 call = reinterpret_cast<CuteQQuickParticleExtruderCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall5 call = reinterpret_cast<CuteQQuickParticleExtruderCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall6 call = reinterpret_cast<CuteQQuickParticleExtruderCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall7 call = reinterpret_cast<CuteQQuickParticleExtruderCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickParticleExtruderCall8 call = reinterpret_cast<CuteQQuickParticleExtruderCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickParticleExtruder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickParticleExtruder10metaObjectEv(
    const QQuickParticleExtruder *self) {
  return self->metaObject();
}

//  QString QQuickParticleExtruder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickParticleExtruder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickParticleExtruder::tr(s, c, n));
}

//  void QQuickParticleExtruder::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickParticleExtruder24qt_qmlMarker_uncreatableEv(
    QQuickParticleExtruder *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickParticleExtruder::QQuickParticleExtruder(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickParticleExtruder *ritual_ZN22QQuickParticleExtruderC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickParticleExtruder(parent);
}

//  QPointF QQuickParticleExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN22QQuickParticleExtruder7extrudeERK6QRectF(
    QQuickParticleExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->extrude(*a0));
}

//  bool QQuickParticleExtruder::contains(const QRectF &bounds, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickParticleExtruder8containsERK6QRectFRK7QPointF(
    QQuickParticleExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->contains(*bounds, *point);
}

//  a Python function taken by a CuteQQuickParticleExtruder, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickParticleExtruder(
    QQuickParticleExtruder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickParticleExtruder *>(self)->take(key, call);
}

//  QPointF QQuickParticleExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN22QQuickParticleExtruder7extrudeERK6QRectF(
    QQuickParticleExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->QQuickParticleExtruder::extrude(*a0));
}

//  bool QQuickParticleExtruder::contains(const QRectF &bounds, const QPointF
//      &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickParticleExtruder8containsERK6QRectFRK7QPointF(
    QQuickParticleExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->QQuickParticleExtruder::contains(*bounds, *point);
}
