//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtQuick3D/qquick3dobject.h>
#include <cstring>

//  Only a class built on QQuick3DParticleSystem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleSystem : QQuick3DParticleSystem {
  using QQuick3DParticleSystem::componentComplete;
};

//  A QQuick3DParticleSystem that Python can take functions over in. Every QQuick3DParticleSystem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuick3DParticleSystemCall0)(const void *, int *);
typedef void (*CuteQQuick3DParticleSystemCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSystemCall2)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSystemCall3)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuick3DParticleSystemCall4)(const void *, QSSGRenderGraphObject *, int *);
typedef void (*CuteQQuick3DParticleSystemCall5)(const void *, int, const QQuick3DObject::ItemChangeData *, int *);
typedef void (*CuteQQuick3DParticleSystemCall6)(const void *, int *);
typedef void (*CuteQQuick3DParticleSystemCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSystemCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DParticleSystemCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSystemCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSystemCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DParticleSystemCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DParticleSystem : public QQuick3DParticleSystem {
public:
  using QQuick3DParticleSystem::QQuick3DParticleSystem;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject12markAllDirtyEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuick3DObject7preSyncEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuick3DParticleSystem::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall0 call = reinterpret_cast<CuteQQuick3DParticleSystemCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DParticleSystem::componentComplete();
  }

  //  void QQuick3DNode::markAllDirty()
  void markAllDirty() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall1 call = reinterpret_cast<CuteQQuick3DParticleSystemCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DNode::markAllDirty();
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall2 call = reinterpret_cast<CuteQQuick3DParticleSystemCall2>(taken[2]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QQuick3DNode::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall3 call = reinterpret_cast<CuteQQuick3DParticleSystemCall3>(taken[3]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QQuick3DNode::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSSGRenderGraphObject
  //      *QQuick3DNode::updateSpatialNode(QSSGRenderGraphObject *node)
  QSSGRenderGraphObject *updateSpatialNode(
      QSSGRenderGraphObject *node) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall4 call = reinterpret_cast<CuteQQuick3DParticleSystemCall4>(taken[4]);
      void * given = call(this, node, &handled);
      if (handled) return static_cast<QSSGRenderGraphObject *>(given);
    }
    return QQuick3DNode::updateSpatialNode(node);
  }

  //  void QQuick3DNode::itemChange(ItemChange a0, const ItemChangeData
  //      &a1)
  void itemChange(
      QQuick3DObject::ItemChange a0,
      const QQuick3DObject::ItemChangeData &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall5 call = reinterpret_cast<CuteQQuick3DParticleSystemCall5>(taken[5]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuick3DNode::itemChange(a0, a1);
  }

  //  void QQuick3DObject::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall6 call = reinterpret_cast<CuteQQuick3DParticleSystemCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::classBegin();
  }

  //  void QQuick3DObject::preSync()
  void preSync() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall7 call = reinterpret_cast<CuteQQuick3DParticleSystemCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DObject::preSync();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall8 call = reinterpret_cast<CuteQQuick3DParticleSystemCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall9 call = reinterpret_cast<CuteQQuick3DParticleSystemCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall10 call = reinterpret_cast<CuteQQuick3DParticleSystemCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall11 call = reinterpret_cast<CuteQQuick3DParticleSystemCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DParticleSystemCall12 call = reinterpret_cast<CuteQQuick3DParticleSystemCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DParticleSystem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuick3DParticleSystem10metaObjectEv(
    const QQuick3DParticleSystem *self) {
  return self->metaObject();
}

//  void *QQuick3DParticleSystem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuick3DParticleSystem11qt_metacastEPKc(
    QQuick3DParticleSystem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DParticleSystem::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuick3DParticleSystem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DParticleSystem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DParticleSystem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuick3DParticleSystem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleSystem::tr(s, c, n));
}

//  QQuick3DParticleSystem::QQuick3DParticleSystem(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystem *ritual_ZN22QQuick3DParticleSystemC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new CuteQQuick3DParticleSystem(parent);
}

//  QQuick3DParticleSystem::~QQuick3DParticleSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystemD1Ev(QQuick3DParticleSystem *self) {
  delete self;
}

//  bool QQuick3DParticleSystem::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DParticleSystem9isRunningEv(
    const QQuick3DParticleSystem *self) {
  return self->isRunning();
}

//  bool QQuick3DParticleSystem::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DParticleSystem8isPausedEv(
    const QQuick3DParticleSystem *self) {
  return self->isPaused();
}

//  int QQuick3DParticleSystem::startTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleSystem9startTimeEv(
    const QQuick3DParticleSystem *self) {
  return self->startTime();
}

//  int QQuick3DParticleSystem::time() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleSystem4timeEv(
    const QQuick3DParticleSystem *self) {
  return self->time();
}

//  bool QQuick3DParticleSystem::useRandomSeed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DParticleSystem13useRandomSeedEv(
    const QQuick3DParticleSystem *self) {
  return self->useRandomSeed();
}

//  int QQuick3DParticleSystem::seed() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleSystem4seedEv(
    const QQuick3DParticleSystem *self) {
  return self->seed();
}

//  int QQuick3DParticleSystem::particleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleSystem13particleCountEv(
    const QQuick3DParticleSystem *self) {
  return self->particleCount();
}

//  bool QQuick3DParticleSystem::logging() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DParticleSystem7loggingEv(
    const QQuick3DParticleSystem *self) {
  return self->logging();
}

//  QQuick3DParticleSystemLogging *QQuick3DParticleSystem::loggingData()
//      const
extern "C" Q_DECL_EXPORT
QQuick3DParticleSystemLogging *ritual_ZNK22QQuick3DParticleSystem11loggingDataEv(
    const QQuick3DParticleSystem *self) {
  return self->loggingData();
}

//  void QQuick3DParticleSystem::registerParticle(QQuick3DParticle *particle)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem16registerParticleEP16QQuick3DParticle(
    QQuick3DParticleSystem *self,
    QQuick3DParticle *particle) {
  self->registerParticle(particle);
}

//  void QQuick3DParticleSystem::unRegisterParticle(QQuick3DParticle
//      *particle)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem18unRegisterParticleEP16QQuick3DParticle(
    QQuick3DParticleSystem *self,
    QQuick3DParticle *particle) {
  self->unRegisterParticle(particle);
}

//  void
//      QQuick3DParticleSystem::registerParticleEmitter(QQuick3DParticleEmitt
//      er *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem23registerParticleEmitterEP23QQuick3DParticleEmitter(
    QQuick3DParticleSystem *self,
    QQuick3DParticleEmitter *e) {
  self->registerParticleEmitter(e);
}

//  void
//      QQuick3DParticleSystem::unRegisterParticleEmitter(QQuick3DParticleEmi
//      tter *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem25unRegisterParticleEmitterEP23QQuick3DParticleEmitter(
    QQuick3DParticleSystem *self,
    QQuick3DParticleEmitter *e) {
  self->unRegisterParticleEmitter(e);
}

//  void
//      QQuick3DParticleSystem::registerParticleAffector(QQuick3DParticleAffe
//      ctor *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem24registerParticleAffectorEP24QQuick3DParticleAffector(
    QQuick3DParticleSystem *self,
    QQuick3DParticleAffector *a) {
  self->registerParticleAffector(a);
}

//  void QQuick3DParticleSystem::unRegisterParticleAffector(QQuick3DParticleA
//      ffector *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem26unRegisterParticleAffectorEP24QQuick3DParticleAffector(
    QQuick3DParticleSystem *self,
    QQuick3DParticleAffector *a) {
  self->unRegisterParticleAffector(a);
}

//  void QQuick3DParticleSystem::updateCurrentTime(int currentTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem17updateCurrentTimeEi(
    QQuick3DParticleSystem *self,
    int currentTime) {
  self->updateCurrentTime(currentTime);
}

//  QPRand *QQuick3DParticleSystem::rand()
extern "C" Q_DECL_EXPORT
QPRand *ritual_ZN22QQuick3DParticleSystem4randEv(
    QQuick3DParticleSystem *self) {
  return self->rand();
}

//  bool QQuick3DParticleSystem::isShared(const QQuick3DParticle *particle)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuick3DParticleSystem8isSharedEPK16QQuick3DParticle(
    const QQuick3DParticleSystem *self,
    const QQuick3DParticle *particle) {
  return self->isShared(particle);
}

//  int QQuick3DParticleSystem::currentTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuick3DParticleSystem11currentTimeEv(
    const QQuick3DParticleSystem *self) {
  return self->currentTime();
}

//  void QQuick3DParticleSystem::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem5resetEv(
    QQuick3DParticleSystem *self) {
  self->reset();
}

//  void QQuick3DParticleSystem::setRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem10setRunningEb(
    QQuick3DParticleSystem *self,
    bool running) {
  self->setRunning(running);
}

//  void QQuick3DParticleSystem::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem9setPausedEb(
    QQuick3DParticleSystem *self,
    bool paused) {
  self->setPaused(paused);
}

//  void QQuick3DParticleSystem::setStartTime(int startTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem12setStartTimeEi(
    QQuick3DParticleSystem *self,
    int startTime) {
  self->setStartTime(startTime);
}

//  void QQuick3DParticleSystem::setTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem7setTimeEi(
    QQuick3DParticleSystem *self,
    int time) {
  self->setTime(time);
}

//  void QQuick3DParticleSystem::setUseRandomSeed(bool randomize)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem16setUseRandomSeedEb(
    QQuick3DParticleSystem *self,
    bool randomize) {
  self->setUseRandomSeed(randomize);
}

//  void QQuick3DParticleSystem::setSeed(int seed)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem7setSeedEi(
    QQuick3DParticleSystem *self,
    int seed) {
  self->setSeed(seed);
}

//  void QQuick3DParticleSystem::setLogging(bool logging)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem10setLoggingEb(
    QQuick3DParticleSystem *self,
    bool logging) {
  self->setLogging(logging);
}

//  void QQuick3DParticleSystem::setEditorTime(int time)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem13setEditorTimeEi(
    QQuick3DParticleSystem *self,
    int time) {
  self->setEditorTime(time);
}

//  void QQuick3DParticleSystem::runningChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem14runningChangedEv(
    QQuick3DParticleSystem *self) {
  self->runningChanged();
}

//  void QQuick3DParticleSystem::pausedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem13pausedChangedEv(
    QQuick3DParticleSystem *self) {
  self->pausedChanged();
}

//  void QQuick3DParticleSystem::timeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem11timeChangedEv(
    QQuick3DParticleSystem *self) {
  self->timeChanged();
}

//  void QQuick3DParticleSystem::startTimeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem16startTimeChangedEv(
    QQuick3DParticleSystem *self) {
  self->startTimeChanged();
}

//  void QQuick3DParticleSystem::useRandomSeedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem20useRandomSeedChangedEv(
    QQuick3DParticleSystem *self) {
  self->useRandomSeedChanged();
}

//  void QQuick3DParticleSystem::seedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem11seedChangedEv(
    QQuick3DParticleSystem *self) {
  self->seedChanged();
}

//  void QQuick3DParticleSystem::loggingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem14loggingChangedEv(
    QQuick3DParticleSystem *self) {
  self->loggingChanged();
}

//  void QQuick3DParticleSystem::loggingDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem18loggingDataChangedEv(
    QQuick3DParticleSystem *self) {
  self->loggingDataChanged();
}

//  void QQuick3DParticleSystem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem17componentCompleteEv(
    QQuick3DParticleSystem *self) {
  self->componentComplete();
}

//  void QQuick3DParticleSystem::updateLoggingData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem17updateLoggingDataEv(
    QQuick3DParticleSystem *self) {
  self->updateLoggingData();
}

//  void QQuick3DParticleSystem::resetLoggingVariables()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem21resetLoggingVariablesEv(
    QQuick3DParticleSystem *self) {
  self->resetLoggingVariables();
}

//  void QQuick3DParticleSystem::doSeedRandomization()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem19doSeedRandomizationEv(
    QQuick3DParticleSystem *self) {
  self->doSeedRandomization();
}

//  void QQuick3DParticleSystem::refresh()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem7refreshEv(
    QQuick3DParticleSystem *self) {
  self->refresh();
}

//  void QQuick3DParticleSystem::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem9markDirtyEv(
    QQuick3DParticleSystem *self) {
  self->markDirty();
}

//  void QQuick3DParticleSystem::processModelParticle(QQuick3DParticleModelPa
//      rticle *modelParticle, const QVector<TrailEmits> &trailEmits, float
//      timeS)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem20processModelParticleEP29QQuick3DParticleModelParticleRK5QListINS_10TrailEmitsEEf(
    QQuick3DParticleSystem *self,
    QQuick3DParticleModelParticle *modelParticle,
    const QVector<QQuick3DParticleSystem::TrailEmits> *trailEmits,
    float timeS) {
  self->processModelParticle(modelParticle, *trailEmits, timeS);
}

//  void QQuick3DParticleSystem::processSpriteParticle(QQuick3DParticleSprite
//      Particle *spriteParticle, const QVector<TrailEmits> &trailEmits,
//      float timeS)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem21processSpriteParticleEP30QQuick3DParticleSpriteParticleRK5QListINS_10TrailEmitsEEf(
    QQuick3DParticleSystem *self,
    QQuick3DParticleSpriteParticle *spriteParticle,
    const QVector<QQuick3DParticleSystem::TrailEmits> *trailEmits,
    float timeS) {
  self->processSpriteParticle(spriteParticle, *trailEmits, timeS);
}

//  void QQuick3DParticleSystem::processModelBlendParticle(QQuick3DParticleMo
//      delBlendParticle *particle, const QVector<TrailEmits> &trailEmits,
//      float timeS)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem25processModelBlendParticleEP34QQuick3DParticleModelBlendParticleRK5QListINS_10TrailEmitsEEf(
    QQuick3DParticleSystem *self,
    QQuick3DParticleModelBlendParticle *particle,
    const QVector<QQuick3DParticleSystem::TrailEmits> *trailEmits,
    float timeS) {
  self->processModelBlendParticle(particle, *trailEmits, timeS);
}

//  void
//      QQuick3DParticleSystem::processParticleCommon(QQuick3DParticleDataCur
//      rent &currentData, const QQuick3DParticleData *d, float
//      particleTimeS)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem21processParticleCommonER27QQuick3DParticleDataCurrentPK20QQuick3DParticleDataf(
    QQuick3DParticleSystem *self,
    QQuick3DParticleDataCurrent *currentData,
    const QQuick3DParticleData *d,
    float particleTimeS) {
  self->processParticleCommon(*currentData, d, particleTimeS);
}

//  void QQuick3DParticleSystem::processParticleFadeInOut(QQuick3DParticleDat
//      aCurrent &currentData, const QQuick3DParticle *particle, float
//      particleTimeS, float particleTimeLeftS)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem24processParticleFadeInOutER27QQuick3DParticleDataCurrentPK16QQuick3DParticleff(
    QQuick3DParticleSystem *self,
    QQuick3DParticleDataCurrent *currentData,
    const QQuick3DParticle *particle,
    float particleTimeS,
    float particleTimeLeftS) {
  self->processParticleFadeInOut(
      *currentData,
      particle,
      particleTimeS,
      particleTimeLeftS);
}

//  void QQuick3DParticleSystem::processParticleAlignment(QQuick3DParticleDat
//      aCurrent &currentData, const QQuick3DParticle *particle, const
//      QQuick3DParticleData *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuick3DParticleSystem24processParticleAlignmentER27QQuick3DParticleDataCurrentPK16QQuick3DParticlePK20QQuick3DParticleData(
    QQuick3DParticleSystem *self,
    QQuick3DParticleDataCurrent *currentData,
    const QQuick3DParticle *particle,
    const QQuick3DParticleData *d) {
  self->processParticleAlignment(*currentData, particle, d);
}

//  bool QQuick3DParticleSystem::isGloballyDisabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuick3DParticleSystem18isGloballyDisabledEv() {
  return QQuick3DParticleSystem::isGloballyDisabled();
}

//  bool QQuick3DParticleSystem::isEditorModeOn()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuick3DParticleSystem14isEditorModeOnEv() {
  return QQuick3DParticleSystem::isEditorModeOn();
}

//  a Python function taken by a CuteQQuick3DParticleSystem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DParticleSystem(
    QQuick3DParticleSystem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DParticleSystem *>(self)->take(key, call);
}

//  void QQuick3DParticleSystem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuick3DParticleSystem17componentCompleteEv(
    QQuick3DParticleSystem *self) {
  static_cast<OwnQQuick3DParticleSystem *>(self)->OwnQQuick3DParticleSystem::componentComplete();
}
