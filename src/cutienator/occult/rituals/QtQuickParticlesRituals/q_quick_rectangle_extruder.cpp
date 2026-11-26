//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickrectangleextruder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickrectangleextruder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickRectangleExtruder that Python can take functions over in. Every QQuickRectangleExtruder
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QPointF * (*CuteQQuickRectangleExtruderCall0)(const void *, const QRectF *, int *);
typedef bool (*CuteQQuickRectangleExtruderCall1)(const void *, const QRectF *, const QPointF *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRectangleExtruderCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRectangleExtruderCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleExtruderCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleExtruderCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleExtruderCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleExtruderCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleExtruderCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRectangleExtruder : public QQuickRectangleExtruder {
public:
  using QQuickRectangleExtruder::QQuickRectangleExtruder;
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

  //  QPointF QQuickRectangleExtruder::extrude(const QRectF &a0)
  QPointF extrude(const QRectF &a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRectangleExtruderCall0 call = reinterpret_cast<CuteQQuickRectangleExtruderCall0>(taken[0]);
      const QPointF * given = call(this, &a0, &handled);
      if (handled && given) return *given;
    }
    return QQuickRectangleExtruder::extrude(a0);
  }

  //  bool QQuickRectangleExtruder::contains(const QRectF &bounds, const
  //      QPointF &point)
  bool contains(const QRectF &bounds, const QPointF &point) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRectangleExtruderCall1 call = reinterpret_cast<CuteQQuickRectangleExtruderCall1>(taken[1]);
      bool given = call(this, &bounds, &point, &handled);
      if (handled) return given;
    }
    return QQuickRectangleExtruder::contains(bounds, point);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRectangleExtruderCall2 call = reinterpret_cast<CuteQQuickRectangleExtruderCall2>(taken[2]);
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
      CuteQQuickRectangleExtruderCall3 call = reinterpret_cast<CuteQQuickRectangleExtruderCall3>(taken[3]);
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
      CuteQQuickRectangleExtruderCall4 call = reinterpret_cast<CuteQQuickRectangleExtruderCall4>(taken[4]);
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
      CuteQQuickRectangleExtruderCall5 call = reinterpret_cast<CuteQQuickRectangleExtruderCall5>(taken[5]);
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
      CuteQQuickRectangleExtruderCall6 call = reinterpret_cast<CuteQQuickRectangleExtruderCall6>(taken[6]);
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
      CuteQQuickRectangleExtruderCall7 call = reinterpret_cast<CuteQQuickRectangleExtruderCall7>(taken[7]);
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
      CuteQQuickRectangleExtruderCall8 call = reinterpret_cast<CuteQQuickRectangleExtruderCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRectangleExtruder::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickRectangleExtruder10metaObjectEv(
    const QQuickRectangleExtruder *self) {
  return self->metaObject();
}

//  void *QQuickRectangleExtruder::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QQuickRectangleExtruder11qt_metacastEPKc(
    QQuickRectangleExtruder *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRectangleExtruder::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QQuickRectangleExtruder11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRectangleExtruder *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRectangleExtruder::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickRectangleExtruder2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRectangleExtruder::tr(s, c, n));
}

//  QQuickRectangleExtruder::QQuickRectangleExtruder(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickRectangleExtruder *ritual_ZN23QQuickRectangleExtruderC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickRectangleExtruder(parent);
}

//  QPointF QQuickRectangleExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN23QQuickRectangleExtruder7extrudeERK6QRectF(
    QQuickRectangleExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->extrude(*a0));
}

//  bool QQuickRectangleExtruder::contains(const QRectF &bounds, const
//      QPointF &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickRectangleExtruder8containsERK6QRectFRK7QPointF(
    QQuickRectangleExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->contains(*bounds, *point);
}

//  bool QQuickRectangleExtruder::fill() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickRectangleExtruder4fillEv(
    const QQuickRectangleExtruder *self) {
  return self->fill();
}

//  void QQuickRectangleExtruder::fillChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangleExtruder11fillChangedEb(
    QQuickRectangleExtruder *self,
    bool arg) {
  self->fillChanged(arg);
}

//  void QQuickRectangleExtruder::setFill(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickRectangleExtruder7setFillEb(
    QQuickRectangleExtruder *self,
    bool arg) {
  self->setFill(arg);
}

//  a Python function taken by a CuteQQuickRectangleExtruder, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRectangleExtruder(
    QQuickRectangleExtruder *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRectangleExtruder *>(self)->take(key, call);
}

//  QPointF QQuickRectangleExtruder::extrude(const QRectF &a0)
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZN23QQuickRectangleExtruder7extrudeERK6QRectF(
    QQuickRectangleExtruder *self,
    const QRectF *a0) {
  return new QPointF(self->QQuickRectangleExtruder::extrude(*a0));
}

//  bool QQuickRectangleExtruder::contains(const QRectF &bounds, const
//      QPointF &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickRectangleExtruder8containsERK6QRectFRK7QPointF(
    QQuickRectangleExtruder *self,
    const QRectF *bounds,
    const QPointF *point) {
  return self->QQuickRectangleExtruder::contains(*bounds, *point);
}
