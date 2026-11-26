//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticleabstractshape_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticleabstractshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuick3DParticleAbstractShape may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleAbstractShape : QQuick3DParticleAbstractShape {
  using QQuick3DParticleAbstractShape::componentComplete;
  using QQuick3DParticleAbstractShape::classBegin;
};

//  A QQuick3DParticleAbstractShape that Python can take functions over in. Every QQuick3DParticleAbstractShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVector3D * (*CuteQQuick3DParticleAbstractShapeCall0)(const void *, int, int *);
typedef const QVector3D * (*CuteQQuick3DParticleAbstractShapeCall1)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleAbstractShapeCall2)(const void *, int *);
typedef void (*CuteQQuick3DParticleAbstractShapeCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleAbstractShapeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleAbstractShapeCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAbstractShapeCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAbstractShapeCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAbstractShapeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAbstractShapeCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleAbstractShapeCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleAbstractShape : public QQuick3DParticleAbstractShape {
public:
  using QQuick3DParticleAbstractShape::QQuick3DParticleAbstractShape;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN29QQuick3DParticleAbstractShape11getPositionEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QQuick3DParticleAbstractShape16getSurfaceNormalEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QVector3D QQuick3DParticleAbstractShape::getPosition(int
  //      particleIndex)
  QVector3D getPosition(int particleIndex) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall0 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall0>(taken[0]);
      const QVector3D * given = call(this, particleIndex, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QVector3D QQuick3DParticleAbstractShape::getSurfaceNormal(int
  //      particleIndex)
  QVector3D getSurfaceNormal(int particleIndex) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall1 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall1>(taken[1]);
      const QVector3D * given = call(this, particleIndex, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QQuick3DParticleAbstractShape::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall2 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleAbstractShape::componentComplete();
  }

  //  void QQuick3DParticleAbstractShape::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall3 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleAbstractShape::classBegin();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall4 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall5 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall6 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall7 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall8 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall9 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleAbstractShapeCall10 call = reinterpret_cast<CuteQQuick3DParticleAbstractShapeCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleAbstractShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuick3DParticleAbstractShape10metaObjectEv(
    const QQuick3DParticleAbstractShape *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleAbstractShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuick3DParticleAbstractShape11qt_metacastEPKc(
    QQuick3DParticleAbstractShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleAbstractShape::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuick3DParticleAbstractShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleAbstractShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleAbstractShape::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QQuick3DParticleAbstractShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleAbstractShape::tr(s, c, n));
}

//  void QQuick3DParticleAbstractShape::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleAbstractShape22qt_qmlMarker_anonymousEv(
    QQuick3DParticleAbstractShape *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuick3DParticleAbstractShape::QQuick3DParticleAbstractShape(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleAbstractShape *ritual_ZN29QQuick3DParticleAbstractShapeC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DParticleAbstractShape(parent);
}

//  QVector3D QQuick3DParticleAbstractShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN29QQuick3DParticleAbstractShape11getPositionEi(
    QQuick3DParticleAbstractShape *self,
    int particleIndex) {
  return new QVector3D(self->getPosition(particleIndex));
}

//  QVector3D QQuick3DParticleAbstractShape::getSurfaceNormal(int
//      particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN29QQuick3DParticleAbstractShape16getSurfaceNormalEi(
    QQuick3DParticleAbstractShape *self,
    int particleIndex) {
  return new QVector3D(self->getSurfaceNormal(particleIndex));
}

//  void QQuick3DParticleAbstractShape::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleAbstractShape17componentCompleteEv(
    QQuick3DParticleAbstractShape *self) {
  self->componentComplete();
}

//  void QQuick3DParticleAbstractShape::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuick3DParticleAbstractShape10classBeginEv(
    QQuick3DParticleAbstractShape *self) {
  self->classBegin();
}

//  QQuick3DNode *QQuick3DParticleAbstractShape::parentNode()
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZN29QQuick3DParticleAbstractShape10parentNodeEv(
    QQuick3DParticleAbstractShape *self) {
  return self->parentNode();
}

//  QQuick3DParticleAbstractShape as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuick3DParticleAbstractShape_QQmlParserStatus(
    QQuick3DParticleAbstractShape *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuick3DParticleAbstractShape, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleAbstractShape(
    QQuick3DParticleAbstractShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleAbstractShape *>(self)->take(key, call);
}

//  void QQuick3DParticleAbstractShape::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleAbstractShape17componentCompleteEv(
    QQuick3DParticleAbstractShape *self) {
  static_cast<OwnQQuick3DParticleAbstractShape *>(self)->OwnQQuick3DParticleAbstractShape::componentComplete();
}

//  void QQuick3DParticleAbstractShape::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuick3DParticleAbstractShape10classBeginEv(
    QQuick3DParticleAbstractShape *self) {
  static_cast<OwnQQuick3DParticleAbstractShape *>(self)->OwnQQuick3DParticleAbstractShape::classBegin();
}
