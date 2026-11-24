//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlemodelshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuick3DParticleModelShape that Python can take functions over in. Every QQuick3DParticleModelShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVector3D * (*CuteQQuick3DParticleModelShapeCall0)(const void *, int, int *);
typedef const QVector3D * (*CuteQQuick3DParticleModelShapeCall1)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleModelShapeCall2)(const void *, int *);
typedef void (*CuteQQuick3DParticleModelShapeCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleModelShapeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleModelShapeCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelShapeCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelShapeCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelShapeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelShapeCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleModelShapeCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleModelShape : public QQuick3DParticleModelShape {
public:
  using QQuick3DParticleModelShape::QQuick3DParticleModelShape;
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

  //  QVector3D QQuick3DParticleModelShape::getPosition(int particleIndex)
  QVector3D getPosition(int particleIndex) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleModelShapeCall0 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall0>(taken[0]);
      const QVector3D * given = call(this, particleIndex, &handled);
      if (handled && given) return *given;
    }
    return QQuick3DParticleModelShape::getPosition(particleIndex);
  }

  //  QVector3D QQuick3DParticleModelShape::getSurfaceNormal(int
  //      particleIndex)
  QVector3D getSurfaceNormal(int particleIndex) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleModelShapeCall1 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall1>(taken[1]);
      const QVector3D * given = call(this, particleIndex, &handled);
      if (handled && given) return *given;
    }
    return QQuick3DParticleModelShape::getSurfaceNormal(particleIndex);
  }

  //  void QQuick3DParticleAbstractShape::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleModelShapeCall2 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleAbstractShape::componentComplete();
  }

  //  void QQuick3DParticleAbstractShape::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleModelShapeCall3 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall3>(taken[3]);
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
      CuteQQuick3DParticleModelShapeCall4 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall4>(taken[4]);
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
      CuteQQuick3DParticleModelShapeCall5 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall5>(taken[5]);
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
      CuteQQuick3DParticleModelShapeCall6 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall6>(taken[6]);
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
      CuteQQuick3DParticleModelShapeCall7 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall7>(taken[7]);
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
      CuteQQuick3DParticleModelShapeCall8 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall8>(taken[8]);
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
      CuteQQuick3DParticleModelShapeCall9 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall9>(taken[9]);
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
      CuteQQuick3DParticleModelShapeCall10 call = reinterpret_cast<CuteQQuick3DParticleModelShapeCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleModelShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuick3DParticleModelShape10metaObjectEv(
    const QQuick3DParticleModelShape *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleModelShape::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuick3DParticleModelShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleModelShape::tr(s, c, n));
}

//  QQuick3DParticleModelShape::QQuick3DParticleModelShape(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleModelShape *ritual_ZN26QQuick3DParticleModelShapeC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DParticleModelShape(parent);
}

//  QQuick3DParticleModelShape::~QQuick3DParticleModelShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleModelShapeD1Ev(
    QQuick3DParticleModelShape *self) {
  delete self;
}

//  bool QQuick3DParticleModelShape::fill() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuick3DParticleModelShape4fillEv(
    const QQuick3DParticleModelShape *self) {
  return self->fill();
}

//  QQmlComponent *QQuick3DParticleModelShape::delegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK26QQuick3DParticleModelShape8delegateEv(
    const QQuick3DParticleModelShape *self) {
  return self->delegate();
}

//  void QQuick3DParticleModelShape::setFill(bool fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleModelShape7setFillEb(
    QQuick3DParticleModelShape *self,
    bool fill) {
  self->setFill(fill);
}

//  void QQuick3DParticleModelShape::setDelegate(QQmlComponent *delegate)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleModelShape11setDelegateEP13QQmlComponent(
    QQuick3DParticleModelShape *self,
    QQmlComponent *delegate) {
  self->setDelegate(delegate);
}

//  QVector3D QQuick3DParticleModelShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN26QQuick3DParticleModelShape11getPositionEi(
    QQuick3DParticleModelShape *self,
    int particleIndex) {
  return new QVector3D(self->getPosition(particleIndex));
}

//  QVector3D QQuick3DParticleModelShape::getSurfaceNormal(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN26QQuick3DParticleModelShape16getSurfaceNormalEi(
    QQuick3DParticleModelShape *self,
    int particleIndex) {
  return new QVector3D(self->getSurfaceNormal(particleIndex));
}

//  QVector3D QQuick3DParticleModelShape::randomPositionModel(int
//      particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN26QQuick3DParticleModelShape19randomPositionModelEi(
    QQuick3DParticleModelShape *self,
    int particleIndex) {
  return new QVector3D(self->randomPositionModel(particleIndex));
}

//  void QQuick3DParticleModelShape::createModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleModelShape11createModelEv(
    QQuick3DParticleModelShape *self) {
  self->createModel();
}

//  void QQuick3DParticleModelShape::clearModelVertexPositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleModelShape25clearModelVertexPositionsEv(
    QQuick3DParticleModelShape *self) {
  self->clearModelVertexPositions();
}

//  void QQuick3DParticleModelShape::calculateModelVertexPositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleModelShape29calculateModelVertexPositionsEv(
    QQuick3DParticleModelShape *self) {
  self->calculateModelVertexPositions();
}

//  a Python function taken by a CuteQQuick3DParticleModelShape, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleModelShape(
    QQuick3DParticleModelShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleModelShape *>(self)->take(key, call);
}

//  QVector3D QQuick3DParticleModelShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN26QQuick3DParticleModelShape11getPositionEi(
    QQuick3DParticleModelShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleModelShape::getPosition(
          particleIndex));
}

//  QVector3D QQuick3DParticleModelShape::getSurfaceNormal(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN26QQuick3DParticleModelShape16getSurfaceNormalEi(
    QQuick3DParticleModelShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleModelShape::getSurfaceNormal(
          particleIndex));
}
