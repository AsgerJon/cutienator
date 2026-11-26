//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPlanarTransform that Python can take functions over in. Every QQuickPlanarTransform
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlanarTransformCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPlanarTransformCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlanarTransformCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlanarTransformCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlanarTransformCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlanarTransformCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPlanarTransformCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPlanarTransform : public QQuickPlanarTransform {
public:
  using QQuickPlanarTransform::QQuickPlanarTransform;
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
      CuteQQuickPlanarTransformCall0 call = reinterpret_cast<CuteQQuickPlanarTransformCall0>(taken[0]);
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
      CuteQQuickPlanarTransformCall1 call = reinterpret_cast<CuteQQuickPlanarTransformCall1>(taken[1]);
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
      CuteQQuickPlanarTransformCall2 call = reinterpret_cast<CuteQQuickPlanarTransformCall2>(taken[2]);
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
      CuteQQuickPlanarTransformCall3 call = reinterpret_cast<CuteQQuickPlanarTransformCall3>(taken[3]);
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
      CuteQQuickPlanarTransformCall4 call = reinterpret_cast<CuteQQuickPlanarTransformCall4>(taken[4]);
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
      CuteQQuickPlanarTransformCall5 call = reinterpret_cast<CuteQQuickPlanarTransformCall5>(taken[5]);
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
      CuteQQuickPlanarTransformCall6 call = reinterpret_cast<CuteQQuickPlanarTransformCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPlanarTransform::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickPlanarTransform10metaObjectEv(
    const QQuickPlanarTransform *self) {
  return self->metaObject();
}

//  void *QQuickPlanarTransform::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QQuickPlanarTransform11qt_metacastEPKc(
    QQuickPlanarTransform *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPlanarTransform::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickPlanarTransform11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPlanarTransform *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPlanarTransform::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickPlanarTransform2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPlanarTransform::tr(s, c, n));
}

//  void QQuickPlanarTransform::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPlanarTransform22qt_qmlMarker_singletonEv(
    QQuickPlanarTransform *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuickPlanarTransform::QQuickPlanarTransform(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickPlanarTransform *ritual_ZN21QQuickPlanarTransformC1EP7QObject(
    QObject *parent) {
  return new CuteQQuickPlanarTransform(parent);
}

//  QMatrix4x4 QQuickPlanarTransform::identity()
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QQuickPlanarTransform8identityEv() {
  return new QMatrix4x4(QQuickPlanarTransform::identity());
}

//  QMatrix4x4 QQuickPlanarTransform::fromAffineMatrix(float scaleX, float
//      shearY, float shearX, float scaleY, float translateX, float
//      translateY)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QQuickPlanarTransform16fromAffineMatrixEffffff(
    float scaleX,
    float shearY,
    float shearX,
    float scaleY,
    float translateX,
    float translateY) {
  return new QMatrix4x4(
      QQuickPlanarTransform::fromAffineMatrix(
          scaleX,
          shearY,
          shearX,
          scaleY,
          translateX,
          translateY));
}

//  QMatrix4x4 QQuickPlanarTransform::fromTranslate(float translateX, float
//      translateY)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QQuickPlanarTransform13fromTranslateEff(
    float translateX,
    float translateY) {
  return new QMatrix4x4(
      QQuickPlanarTransform::fromTranslate(
          translateX,
          translateY));
}

//  QMatrix4x4 QQuickPlanarTransform::fromScale(float scaleX, float scaleY,
//      float originX, float originY)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QQuickPlanarTransform9fromScaleEffff(
    float scaleX,
    float scaleY,
    float originX,
    float originY) {
  return new QMatrix4x4(
      QQuickPlanarTransform::fromScale(
          scaleX,
          scaleY,
          originX,
          originY));
}

//  QMatrix4x4 QQuickPlanarTransform::fromRotate(float angle, float originX,
//      float originY)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QQuickPlanarTransform10fromRotateEfff(
    float angle,
    float originX,
    float originY) {
  return new QMatrix4x4(
      QQuickPlanarTransform::fromRotate(
          angle,
          originX,
          originY));
}

//  QMatrix4x4 QQuickPlanarTransform::fromShear(float shearX, float shearY,
//      float originX, float originY)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN21QQuickPlanarTransform9fromShearEffff(
    float shearX,
    float shearY,
    float originX,
    float originY) {
  return new QMatrix4x4(
      QQuickPlanarTransform::fromShear(
          shearX,
          shearY,
          originX,
          originY));
}

//  a Python function taken by a CuteQQuickPlanarTransform, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPlanarTransform(
    QQuickPlanarTransform *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPlanarTransform *>(self)->take(key, call);
}
