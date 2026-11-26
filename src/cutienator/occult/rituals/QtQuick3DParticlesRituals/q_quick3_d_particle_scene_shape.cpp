//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesceneshape_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesceneshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuick3DParticleSceneShape that Python can take functions over in. Every QQuick3DParticleSceneShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVector3D * (*CuteQQuick3DParticleSceneShapeCall0)(const void *, int, int *);
typedef const QVector3D * (*CuteQQuick3DParticleSceneShapeCall1)(const void *, int, int *);
typedef void (*CuteQQuick3DParticleSceneShapeCall2)(const void *, int *);
typedef void (*CuteQQuick3DParticleSceneShapeCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSceneShapeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSceneShapeCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSceneShapeCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSceneShapeCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSceneShapeCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSceneShapeCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSceneShapeCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleSceneShape : public QQuick3DParticleSceneShape {
public:
  using QQuick3DParticleSceneShape::QQuick3DParticleSceneShape;
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

  //  QVector3D QQuick3DParticleSceneShape::getPosition(int particleIndex)
  QVector3D getPosition(int particleIndex) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleSceneShapeCall0 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall0>(taken[0]);
      const QVector3D * given = call(this, particleIndex, &handled);
      if (handled && given) return *given;
    }
    return QQuick3DParticleSceneShape::getPosition(particleIndex);
  }

  //  QVector3D QQuick3DParticleSceneShape::getSurfaceNormal(int
  //      particleIndex)
  QVector3D getSurfaceNormal(int particleIndex) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleSceneShapeCall1 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall1>(taken[1]);
      const QVector3D * given = call(this, particleIndex, &handled);
      if (handled && given) return *given;
    }
    return QQuick3DParticleSceneShape::getSurfaceNormal(particleIndex);
  }

  //  void QQuick3DParticleAbstractShape::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleSceneShapeCall2 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleAbstractShape::componentComplete();
  }

  //  void QQuick3DParticleAbstractShape::classBegin()
  void classBegin() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleSceneShapeCall3 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall3>(taken[3]);
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
      CuteQQuick3DParticleSceneShapeCall4 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall4>(taken[4]);
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
      CuteQQuick3DParticleSceneShapeCall5 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall5>(taken[5]);
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
      CuteQQuick3DParticleSceneShapeCall6 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall6>(taken[6]);
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
      CuteQQuick3DParticleSceneShapeCall7 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall7>(taken[7]);
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
      CuteQQuick3DParticleSceneShapeCall8 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall8>(taken[8]);
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
      CuteQQuick3DParticleSceneShapeCall9 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall9>(taken[9]);
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
      CuteQQuick3DParticleSceneShapeCall10 call = reinterpret_cast<CuteQQuick3DParticleSceneShapeCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleSceneShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuick3DParticleSceneShape10metaObjectEv(
    const QQuick3DParticleSceneShape *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleSceneShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuick3DParticleSceneShape11qt_metacastEPKc(
    QQuick3DParticleSceneShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleSceneShape::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQuick3DParticleSceneShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleSceneShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleSceneShape::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QQuick3DParticleSceneShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleSceneShape::tr(s, c, n));
}

//  QQuick3DParticleSceneShape::QQuick3DParticleSceneShape(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSceneShape *ritual_ZN26QQuick3DParticleSceneShapeC1EP7QObject(
    QObject *parent) {
  return new CuteQQuick3DParticleSceneShape(parent);
}

//  QQuick3DParticleSceneShape::~QQuick3DParticleSceneShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShapeD1Ev(
    QQuick3DParticleSceneShape *self) {
  delete self;
}

//  QQuick3DNode *QQuick3DParticleSceneShape::scene() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK26QQuick3DParticleSceneShape5sceneEv(
    const QQuick3DParticleSceneShape *self) {
  return self->scene();
}

//  QVector3D QQuick3DParticleSceneShape::sceneCenter() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK26QQuick3DParticleSceneShape11sceneCenterEv(
    const QQuick3DParticleSceneShape *self) {
  return new QVector3D(self->sceneCenter());
}

//  QVector3D QQuick3DParticleSceneShape::sceneExtents() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK26QQuick3DParticleSceneShape12sceneExtentsEv(
    const QQuick3DParticleSceneShape *self) {
  return new QVector3D(self->sceneExtents());
}

//  float QQuick3DParticleSceneShape::shapeResolution() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK26QQuick3DParticleSceneShape15shapeResolutionEv(
    const QQuick3DParticleSceneShape *self) {
  return self->shapeResolution();
}

//  QQuick3DGeometry *QQuick3DParticleSceneShape::geometry() const
extern "C" Q_DECL_EXPORT
QQuick3DGeometry *ritual_ZNK26QQuick3DParticleSceneShape8geometryEv(
    const QQuick3DParticleSceneShape *self) {
  return self->geometry();
}

//  QList<QQuick3DNode *> QQuick3DParticleSceneShape::excludedNodes() const
extern "C" Q_DECL_EXPORT
QList<QQuick3DNode *> *ritual_ZNK26QQuick3DParticleSceneShape13excludedNodesEv(
    const QQuick3DParticleSceneShape *self) {
  return new QList<QQuick3DNode *>(self->excludedNodes());
}

//  void QQuick3DParticleSceneShape::setScene(QQuick3DNode *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape8setSceneEP12QQuick3DNode(
    QQuick3DParticleSceneShape *self,
    QQuick3DNode *scene) {
  self->setScene(scene);
}

//  void QQuick3DParticleSceneShape::setSceneCenter(const QVector3D &extents)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape14setSceneCenterERK9QVector3D(
    QQuick3DParticleSceneShape *self,
    const QVector3D *extents) {
  self->setSceneCenter(*extents);
}

//  void QQuick3DParticleSceneShape::setSceneExtents(const QVector3D
//      &extents)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape15setSceneExtentsERK9QVector3D(
    QQuick3DParticleSceneShape *self,
    const QVector3D *extents) {
  self->setSceneExtents(*extents);
}

//  void QQuick3DParticleSceneShape::setShapeResolution(float resolution)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape18setShapeResolutionEf(
    QQuick3DParticleSceneShape *self,
    float resolution) {
  self->setShapeResolution(resolution);
}

//  void QQuick3DParticleSceneShape::setExcludedNodes(const
//      QList<QQuick3DNode *> &nodes)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape16setExcludedNodesERK5QListIP12QQuick3DNodeE(
    QQuick3DParticleSceneShape *self,
    const QList<QQuick3DNode *> *nodes) {
  self->setExcludedNodes(*nodes);
}

//  QVector3D QQuick3DParticleSceneShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN26QQuick3DParticleSceneShape11getPositionEi(
    QQuick3DParticleSceneShape *self,
    int particleIndex) {
  return new QVector3D(self->getPosition(particleIndex));
}

//  QVector3D QQuick3DParticleSceneShape::getSurfaceNormal(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN26QQuick3DParticleSceneShape16getSurfaceNormalEi(
    QQuick3DParticleSceneShape *self,
    int particleIndex) {
  return new QVector3D(self->getSurfaceNormal(particleIndex));
}

//  void QQuick3DParticleSceneShape::sceneChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape12sceneChangedEv(
    QQuick3DParticleSceneShape *self) {
  self->sceneChanged();
}

//  void QQuick3DParticleSceneShape::sceneCenterChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape18sceneCenterChangedEv(
    QQuick3DParticleSceneShape *self) {
  self->sceneCenterChanged();
}

//  void QQuick3DParticleSceneShape::sceneExtentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape19sceneExtentsChangedEv(
    QQuick3DParticleSceneShape *self) {
  self->sceneExtentsChanged();
}

//  void QQuick3DParticleSceneShape::shapeResolutionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape22shapeResolutionChangedEv(
    QQuick3DParticleSceneShape *self) {
  self->shapeResolutionChanged();
}

//  void QQuick3DParticleSceneShape::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape15geometryChangedEv(
    QQuick3DParticleSceneShape *self) {
  self->geometryChanged();
}

//  void QQuick3DParticleSceneShape::excludedNodesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape20excludedNodesChangedEv(
    QQuick3DParticleSceneShape *self) {
  self->excludedNodesChanged();
}

//  QVector3D QQuick3DParticleSceneShape::randomPositionModel(int
//      particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN26QQuick3DParticleSceneShape19randomPositionModelEi(
    QQuick3DParticleSceneShape *self,
    int particleIndex) {
  return new QVector3D(self->randomPositionModel(particleIndex));
}

//  void QQuick3DParticleSceneShape::createShapeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape15createShapeDataEv(
    QQuick3DParticleSceneShape *self) {
  self->createShapeData();
}

//  void QQuick3DParticleSceneShape::clearModelVertexPositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape25clearModelVertexPositionsEv(
    QQuick3DParticleSceneShape *self) {
  self->clearModelVertexPositions();
}

//  void QQuick3DParticleSceneShape::calculateModelVertexPositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape29calculateModelVertexPositionsEv(
    QQuick3DParticleSceneShape *self) {
  self->calculateModelVertexPositions();
}

//  QList<QVector3D> QQuick3DParticleSceneShape::excludeTriangles(const
//      QList<QVector3D> &list)
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZN26QQuick3DParticleSceneShape16excludeTrianglesERK5QListI9QVector3DE(
    QQuick3DParticleSceneShape *self,
    const QList<QVector3D> *list) {
  return new QList<QVector3D>(self->excludeTriangles(*list));
}

//  void QQuick3DParticleSceneShape::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape14updateGeometryEv(
    QQuick3DParticleSceneShape *self) {
  self->updateGeometry();
}

//  bool QQuick3DParticleSceneShape::isVisibleRecursive(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuick3DParticleSceneShape18isVisibleRecursiveEP12QQuick3DNode(
    QQuick3DParticleSceneShape *self,
    QQuick3DNode *node) {
  return self->isVisibleRecursive(node);
}

//  bool QQuick3DParticleSceneShape::isExcluded(QQuick3DModel *model)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuick3DParticleSceneShape10isExcludedEP13QQuick3DModel(
    QQuick3DParticleSceneShape *self,
    QQuick3DModel *model) {
  return self->isExcluded(model);
}

//  void QQuick3DParticleSceneShape::markDirty(bool dirty, bool excludeDirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuick3DParticleSceneShape9markDirtyEbb(
    QQuick3DParticleSceneShape *self,
    bool dirty,
    bool excludeDirty) {
  self->markDirty(dirty, excludeDirty);
}

//  a Python function taken by a CuteQQuick3DParticleSceneShape, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleSceneShape(
    QQuick3DParticleSceneShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleSceneShape *>(self)->take(key, call);
}

//  QVector3D QQuick3DParticleSceneShape::getPosition(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN26QQuick3DParticleSceneShape11getPositionEi(
    QQuick3DParticleSceneShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleSceneShape::getPosition(
          particleIndex));
}

//  QVector3D QQuick3DParticleSceneShape::getSurfaceNormal(int particleIndex)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZN26QQuick3DParticleSceneShape16getSurfaceNormalEi(
    QQuick3DParticleSceneShape *self,
    int particleIndex) {
  return new QVector3D(
      self->QQuick3DParticleSceneShape::getSurfaceNormal(
          particleIndex));
}
