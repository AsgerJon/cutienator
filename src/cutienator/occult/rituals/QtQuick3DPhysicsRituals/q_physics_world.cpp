//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsworld_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsworld_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPhysicsWorld that Python can take functions over in. Every QPhysicsWorld
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPhysicsWorldCall0)(const void *, int *);
typedef void (*CuteQPhysicsWorldCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPhysicsWorldCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPhysicsWorldCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsWorldCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsWorldCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsWorldCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsWorldCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPhysicsWorldCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPhysicsWorld : public QPhysicsWorld {
public:
  using QPhysicsWorld::QPhysicsWorld;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
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

  //  void QPhysicsWorld::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPhysicsWorldCall0 call = reinterpret_cast<CuteQPhysicsWorldCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPhysicsWorld::classBegin();
  }

  //  void QPhysicsWorld::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPhysicsWorldCall1 call = reinterpret_cast<CuteQPhysicsWorldCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QPhysicsWorld::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPhysicsWorldCall2 call = reinterpret_cast<CuteQPhysicsWorldCall2>(taken[2]);
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
      CuteQPhysicsWorldCall3 call = reinterpret_cast<CuteQPhysicsWorldCall3>(taken[3]);
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
      CuteQPhysicsWorldCall4 call = reinterpret_cast<CuteQPhysicsWorldCall4>(taken[4]);
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
      CuteQPhysicsWorldCall5 call = reinterpret_cast<CuteQPhysicsWorldCall5>(taken[5]);
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
      CuteQPhysicsWorldCall6 call = reinterpret_cast<CuteQPhysicsWorldCall6>(taken[6]);
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
      CuteQPhysicsWorldCall7 call = reinterpret_cast<CuteQPhysicsWorldCall7>(taken[7]);
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
      CuteQPhysicsWorldCall8 call = reinterpret_cast<CuteQPhysicsWorldCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPhysicsWorld::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPhysicsWorld10metaObjectEv(
    const QPhysicsWorld *self) {
  return self->metaObject();
}

//  QString QPhysicsWorld::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPhysicsWorld2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPhysicsWorld::tr(s, c, n));
}

//  QPhysicsWorld::QPhysicsWorld(QObject *parent)
extern "C" Q_DECL_EXPORT
QPhysicsWorld *ritual_ZN13QPhysicsWorldC1EP7QObject(QObject *parent) {
  return new CuteQPhysicsWorld(parent);
}

//  QPhysicsWorld::~QPhysicsWorld()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorldD1Ev(QPhysicsWorld *self) {
  delete self;
}

//  void QPhysicsWorld::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld10classBeginEv(QPhysicsWorld *self) {
  self->classBegin();
}

//  void QPhysicsWorld::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld17componentCompleteEv(QPhysicsWorld *self) {
  self->componentComplete();
}

//  QVector3D QPhysicsWorld::gravity() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13QPhysicsWorld7gravityEv(const QPhysicsWorld *self) {
  return new QVector3D(self->gravity());
}

//  bool QPhysicsWorld::running() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPhysicsWorld7runningEv(const QPhysicsWorld *self) {
  return self->running();
}

//  bool QPhysicsWorld::forceDebugDraw() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPhysicsWorld14forceDebugDrawEv(const QPhysicsWorld *self) {
  return self->forceDebugDraw();
}

//  bool QPhysicsWorld::enableCCD() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPhysicsWorld9enableCCDEv(const QPhysicsWorld *self) {
  return self->enableCCD();
}

//  float QPhysicsWorld::typicalLength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QPhysicsWorld13typicalLengthEv(const QPhysicsWorld *self) {
  return self->typicalLength();
}

//  float QPhysicsWorld::typicalSpeed() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QPhysicsWorld12typicalSpeedEv(const QPhysicsWorld *self) {
  return self->typicalSpeed();
}

//  float QPhysicsWorld::defaultDensity() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QPhysicsWorld14defaultDensityEv(
    const QPhysicsWorld *self) {
  return self->defaultDensity();
}

//  float QPhysicsWorld::minimumTimestep() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QPhysicsWorld15minimumTimestepEv(
    const QPhysicsWorld *self) {
  return self->minimumTimestep();
}

//  float QPhysicsWorld::maximumTimestep() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13QPhysicsWorld15maximumTimestepEv(
    const QPhysicsWorld *self) {
  return self->maximumTimestep();
}

//  bool QPhysicsWorld::isNodeRemoved(QAbstractPhysicsNode *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QPhysicsWorld13isNodeRemovedEP20QAbstractPhysicsNode(
    QPhysicsWorld *self,
    QAbstractPhysicsNode *object) {
  return self->isNodeRemoved(object);
}

//  QPhysicsWorld *QPhysicsWorld::getWorld(QQuick3DNode *node)
extern "C" Q_DECL_EXPORT
QPhysicsWorld *ritual_ZN13QPhysicsWorld8getWorldEP12QQuick3DNode(
    QQuick3DNode *node) {
  return QPhysicsWorld::getWorld(node);
}

//  QPhysicsWorld *QPhysicsWorld::getWorld(QPhysicsJoint *joint)
extern "C" Q_DECL_EXPORT
QPhysicsWorld *ritual_ZN13QPhysicsWorld8getWorldEP13QPhysicsJoint(
    QPhysicsJoint *joint) {
  return QPhysicsWorld::getWorld(joint);
}

//  void QPhysicsWorld::registerNode(QAbstractPhysicsNode *physicsNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld12registerNodeEP20QAbstractPhysicsNode(
    QAbstractPhysicsNode *physicsNode) {
  QPhysicsWorld::registerNode(physicsNode);
}

//  void QPhysicsWorld::deregisterNode(QAbstractPhysicsNode *physicsNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld14deregisterNodeEP20QAbstractPhysicsNode(
    QAbstractPhysicsNode *physicsNode) {
  QPhysicsWorld::deregisterNode(physicsNode);
}

//  void QPhysicsWorld::registerJoint(QPhysicsJoint *joint)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld13registerJointEP13QPhysicsJoint(
    QPhysicsJoint *joint) {
  QPhysicsWorld::registerJoint(joint);
}

//  void QPhysicsWorld::deregisterJoint(QPhysicsJoint *joint)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld15deregisterJointEP13QPhysicsJoint(
    QPhysicsJoint *joint) {
  QPhysicsWorld::deregisterJoint(joint);
}

//  QQuick3DNode *QPhysicsWorld::viewport() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK13QPhysicsWorld8viewportEv(
    const QPhysicsWorld *self) {
  return self->viewport();
}

//  void QPhysicsWorld::setHasIndividualDebugDraw()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld25setHasIndividualDebugDrawEv(
    QPhysicsWorld *self) {
  self->setHasIndividualDebugDraw();
}

//  QQuick3DNode *QPhysicsWorld::scene() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK13QPhysicsWorld5sceneEv(const QPhysicsWorld *self) {
  return self->scene();
}

//  int QPhysicsWorld::numThreads() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPhysicsWorld10numThreadsEv(const QPhysicsWorld *self) {
  return self->numThreads();
}

//  bool QPhysicsWorld::reportKinematicKinematicCollisions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPhysicsWorld34reportKinematicKinematicCollisionsEv(
    const QPhysicsWorld *self) {
  return self->reportKinematicKinematicCollisions();
}

//  void QPhysicsWorld::setReportKinematicKinematicCollisions(bool
//      newReportKinematicKinematicCollisions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld37setReportKinematicKinematicCollisionsEb(
    QPhysicsWorld *self,
    bool newReportKinematicKinematicCollisions) {
  self->setReportKinematicKinematicCollisions(
      newReportKinematicKinematicCollisions);
}

//  bool QPhysicsWorld::reportStaticKinematicCollisions() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPhysicsWorld31reportStaticKinematicCollisionsEv(
    const QPhysicsWorld *self) {
  return self->reportStaticKinematicCollisions();
}

//  void QPhysicsWorld::setReportStaticKinematicCollisions(bool
//      newReportStaticKinematicCollisions)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld34setReportStaticKinematicCollisionsEb(
    QPhysicsWorld *self,
    bool newReportStaticKinematicCollisions) {
  self->setReportStaticKinematicCollisions(
      newReportStaticKinematicCollisions);
}

//  void QPhysicsWorld::cleanupRemovedJoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld20cleanupRemovedJointsEv(QPhysicsWorld *self) {
  self->cleanupRemovedJoints();
}

//  void QPhysicsWorld::setGravity(QVector3D gravity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld10setGravityE9QVector3D(
    QPhysicsWorld *self,
    const QVector3D *gravity) {
  self->setGravity(*gravity);
}

//  void QPhysicsWorld::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld10setRunningEb(
    QPhysicsWorld *self,
    bool running) {
  self->setRunning(running);
}

//  void QPhysicsWorld::setForceDebugDraw(bool forceDebugDraw)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld17setForceDebugDrawEb(
    QPhysicsWorld *self,
    bool forceDebugDraw) {
  self->setForceDebugDraw(forceDebugDraw);
}

//  void QPhysicsWorld::setEnableCCD(bool enableCCD)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld12setEnableCCDEb(
    QPhysicsWorld *self,
    bool enableCCD) {
  self->setEnableCCD(enableCCD);
}

//  void QPhysicsWorld::setTypicalLength(float typicalLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld16setTypicalLengthEf(
    QPhysicsWorld *self,
    float typicalLength) {
  self->setTypicalLength(typicalLength);
}

//  void QPhysicsWorld::setTypicalSpeed(float typicalSpeed)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld15setTypicalSpeedEf(
    QPhysicsWorld *self,
    float typicalSpeed) {
  self->setTypicalSpeed(typicalSpeed);
}

//  void QPhysicsWorld::setDefaultDensity(float defaultDensity)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld17setDefaultDensityEf(
    QPhysicsWorld *self,
    float defaultDensity) {
  self->setDefaultDensity(defaultDensity);
}

//  void QPhysicsWorld::setViewport(QQuick3DNode *viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld11setViewportEP12QQuick3DNode(
    QPhysicsWorld *self,
    QQuick3DNode *viewport) {
  self->setViewport(viewport);
}

//  void QPhysicsWorld::setMinimumTimestep(float minTimestep)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld18setMinimumTimestepEf(
    QPhysicsWorld *self,
    float minTimestep) {
  self->setMinimumTimestep(minTimestep);
}

//  void QPhysicsWorld::setMaximumTimestep(float maxTimestep)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld18setMaximumTimestepEf(
    QPhysicsWorld *self,
    float maxTimestep) {
  self->setMaximumTimestep(maxTimestep);
}

//  void QPhysicsWorld::setScene(QQuick3DNode *newScene)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld8setSceneEP12QQuick3DNode(
    QPhysicsWorld *self,
    QQuick3DNode *newScene) {
  self->setScene(newScene);
}

//  void QPhysicsWorld::setNumThreads(int newNumThreads)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld13setNumThreadsEi(
    QPhysicsWorld *self,
    int newNumThreads) {
  self->setNumThreads(newNumThreads);
}

//  void QPhysicsWorld::simulateFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld13simulateFrameEv(QPhysicsWorld *self) {
  self->simulateFrame();
}

//  void QPhysicsWorld::frameFinished(float deltaTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld13frameFinishedEf(
    QPhysicsWorld *self,
    float deltaTime) {
  self->frameFinished(deltaTime);
}

//  void QPhysicsWorld::frameFinishedDesignStudio()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld25frameFinishedDesignStudioEv(
    QPhysicsWorld *self) {
  self->frameFinishedDesignStudio();
}

//  void QPhysicsWorld::initPhysics()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld11initPhysicsEv(QPhysicsWorld *self) {
  self->initPhysics();
}

//  void QPhysicsWorld::cleanupRemovedNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld19cleanupRemovedNodesEv(QPhysicsWorld *self) {
  self->cleanupRemovedNodes();
}

//  void QPhysicsWorld::updateDebugDraw()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld15updateDebugDrawEv(QPhysicsWorld *self) {
  self->updateDebugDraw();
}

//  void QPhysicsWorld::updateDebugDrawDesignStudio()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld27updateDebugDrawDesignStudioEv(
    QPhysicsWorld *self) {
  self->updateDebugDrawDesignStudio();
}

//  void QPhysicsWorld::setupDebugMaterials(QQuick3DNode *sceneNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld19setupDebugMaterialsEP12QQuick3DNode(
    QPhysicsWorld *self,
    QQuick3DNode *sceneNode) {
  self->setupDebugMaterials(sceneNode);
}

//  void QPhysicsWorld::disableDebugDraw()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld16disableDebugDrawEv(QPhysicsWorld *self) {
  self->disableDebugDraw();
}

//  void QPhysicsWorld::matchOrphanNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld16matchOrphanNodesEv(QPhysicsWorld *self) {
  self->matchOrphanNodes();
}

//  void QPhysicsWorld::matchOrphanJoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld17matchOrphanJointsEv(QPhysicsWorld *self) {
  self->matchOrphanJoints();
}

//  void QPhysicsWorld::findPhysicsNodes()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld16findPhysicsNodesEv(QPhysicsWorld *self) {
  self->findPhysicsNodes();
}

//  void QPhysicsWorld::emitContactCallbacks()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPhysicsWorld20emitContactCallbacksEv(QPhysicsWorld *self) {
  self->emitContactCallbacks();
}

//  QPhysicsWorld as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QPhysicsWorld_QQmlParserStatus(
    QPhysicsWorld *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQPhysicsWorld, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPhysicsWorld(
    QPhysicsWorld *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPhysicsWorld *>(self)->take(key, call);
}

//  void QPhysicsWorld::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPhysicsWorld10classBeginEv(QPhysicsWorld *self) {
  self->QPhysicsWorld::classBegin();
}

//  void QPhysicsWorld::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPhysicsWorld17componentCompleteEv(QPhysicsWorld *self) {
  self->QPhysicsWorld::componentComplete();
}
