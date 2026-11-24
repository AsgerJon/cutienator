//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dquaternionutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dquaternionutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DQuaternionUtils that Python can take functions over in. Every QQuick3DQuaternionUtils
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DQuaternionUtilsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DQuaternionUtilsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionUtilsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionUtilsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionUtilsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionUtilsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DQuaternionUtilsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DQuaternionUtils : public QQuick3DQuaternionUtils {
public:
  using QQuick3DQuaternionUtils::QQuick3DQuaternionUtils;
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
      CuteQQuick3DQuaternionUtilsCall0 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall0>(taken[0]);
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
      CuteQQuick3DQuaternionUtilsCall1 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall1>(taken[1]);
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
      CuteQQuick3DQuaternionUtilsCall2 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall2>(taken[2]);
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
      CuteQQuick3DQuaternionUtilsCall3 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall3>(taken[3]);
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
      CuteQQuick3DQuaternionUtilsCall4 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall4>(taken[4]);
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
      CuteQQuick3DQuaternionUtilsCall5 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall5>(taken[5]);
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
      CuteQQuick3DQuaternionUtilsCall6 call = reinterpret_cast<CuteQQuick3DQuaternionUtilsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DQuaternionUtils::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuick3DQuaternionUtils10metaObjectEv(
    const QQuick3DQuaternionUtils *self) {
  return self->metaObject();
}

//  QString QQuick3DQuaternionUtils::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuick3DQuaternionUtils2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DQuaternionUtils::tr(s, c, n));
}

//  void QQuick3DQuaternionUtils::qt_qmlMarker_singleton()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuick3DQuaternionUtils22qt_qmlMarker_singletonEv(
    QQuick3DQuaternionUtils *self) {
  self->qt_qmlMarker_singleton();
}

//  QQuick3DQuaternionUtils::QQuick3DQuaternionUtils(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DQuaternionUtils *ritual_ZN23QQuick3DQuaternionUtilsC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DQuaternionUtils(parent);
}

//  QQuaternion QQuick3DQuaternionUtils::fromAxesAndAngles(const QVector3D
//      &axis1, float angle1, const QVector3D &axis2, float angle2, const
//      QVector3D &axis3, float angle3)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils17fromAxesAndAnglesERK9QVector3DfS2_fS2_f(
    const QVector3D *axis1,
    float angle1,
    const QVector3D *axis2,
    float angle2,
    const QVector3D *axis3,
    float angle3) {
  return new QQuaternion(
      QQuick3DQuaternionUtils::fromAxesAndAngles(
          *axis1,
          angle1,
          *axis2,
          angle2,
          *axis3,
          angle3));
}

//  QQuaternion QQuick3DQuaternionUtils::fromAxesAndAngles(const QVector3D
//      &axis1, float angle1, const QVector3D &axis2, float angle2)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils17fromAxesAndAnglesERK9QVector3DfS2_f(
    const QVector3D *axis1,
    float angle1,
    const QVector3D *axis2,
    float angle2) {
  return new QQuaternion(
      QQuick3DQuaternionUtils::fromAxesAndAngles(
          *axis1,
          angle1,
          *axis2,
          angle2));
}

//  QQuaternion QQuick3DQuaternionUtils::fromAxisAndAngle(float x, float y,
//      float z, float angle)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils16fromAxisAndAngleEffff(
    float x,
    float y,
    float z,
    float angle) {
  return new QQuaternion(
      QQuick3DQuaternionUtils::fromAxisAndAngle(
          x,
          y,
          z,
          angle));
}

//  QQuaternion QQuick3DQuaternionUtils::fromAxisAndAngle(const QVector3D
//      &axis, float angle)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils16fromAxisAndAngleERK9QVector3Df(
    const QVector3D *axis,
    float angle) {
  return new QQuaternion(
      QQuick3DQuaternionUtils::fromAxisAndAngle(
          *axis,
          angle));
}

//  QQuaternion QQuick3DQuaternionUtils::fromEulerAngles(float x, float y,
//      float z)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils15fromEulerAnglesEfff(
    float x,
    float y,
    float z) {
  return new QQuaternion(QQuick3DQuaternionUtils::fromEulerAngles(x, y, z));
}

//  QQuaternion QQuick3DQuaternionUtils::fromEulerAngles(const QVector3D
//      &eulerAngles)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils15fromEulerAnglesERK9QVector3D(
    const QVector3D *eulerAngles) {
  return new QQuaternion(
      QQuick3DQuaternionUtils::fromEulerAngles(
          *eulerAngles));
}

//  QQuaternion QQuick3DQuaternionUtils::lookAt(const QVector3D
//      &sourcePosition, const QVector3D &targetPosition, const QVector3D
//      &forwardDirection, const QVector3D &upDirection)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN23QQuick3DQuaternionUtils6lookAtERK9QVector3DS2_S2_S2_(
    const QVector3D *sourcePosition,
    const QVector3D *targetPosition,
    const QVector3D *forwardDirection,
    const QVector3D *upDirection) {
  return new QQuaternion(
      QQuick3DQuaternionUtils::lookAt(
          *sourcePosition,
          *targetPosition,
          *forwardDirection,
          *upDirection));
}

//  a Python function taken by a CuteQQuick3DQuaternionUtils, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DQuaternionUtils(
    QQuick3DQuaternionUtils *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DQuaternionUtils *>(self)->take(key, call);
}
