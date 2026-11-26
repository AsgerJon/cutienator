//  Written by hand on 2026-11-25 from
//  Qt3DCore/6.12.0/Qt3DCore/private/qscene_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again. Not written: 'lookupNodes'
//  and 'entitiesForComponent' (they take or give a QList).
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/6.12.0/Qt3DCore/private/qscene_p.h>
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DCore::QScene that Python can take functions over in. Every
//  Qt3DCore::QScene Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DCore_QSceneCall0)(const void *, const Qt3DCore::QNodeId *, int *);
class CuteQt3DCore_QScene : public Qt3DCore::QScene {
public:
  using Qt3DCore::QScene::QScene;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore28QAbstractFrontEndNodeManager10lookupNodeENS_7QNodeIdE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QNode *Qt3DCore::QAbstractFrontEndNodeManager::lookupNode(QNodeId id)
  //      const
  Qt3DCore::QNode *lookupNode(Qt3DCore::QNodeId id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QSceneCall0 call = reinterpret_cast<CuteQt3DCore_QSceneCall0>(taken[0]);
      void *given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QNode *>(given);
    }
    return Qt3DCore::QScene::lookupNode(id);
  }
};

//  QScene::QScene(QAspectEngine *engine)
extern "C" Q_DECL_EXPORT
Qt3DCore::QScene *ritual_ZN8Qt3DCore6QSceneC1EPNS_13QAspectEngineE(
    Qt3DCore::QAspectEngine *engine) {
  return new CuteQt3DCore_QScene(engine);
}

//  QScene::~QScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QSceneD1Ev(
    Qt3DCore::QScene *self) {
  delete self;
}

//  QAspectEngine *QScene::engine() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEngine *ritual_ZNK8Qt3DCore6QScene6engineEv(
    const Qt3DCore::QScene *self) {
  return self->engine();
}

//  void QScene::addObservable(QNode *observable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene13addObservableEPNS_5QNodeE(
    Qt3DCore::QScene *self,
    Qt3DCore::QNode *observable) {
  self->addObservable(observable);
}

//  void QScene::removeObservable(QNode *observable)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene16removeObservableEPNS_5QNodeE(
    Qt3DCore::QScene *self,
    Qt3DCore::QNode *observable) {
  self->removeObservable(observable);
}

//  QNode *QScene::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore6QScene10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QScene *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupNode(*id);
}

//  QNode *QScene::rootNode() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore6QScene8rootNodeEv(
    const Qt3DCore::QScene *self) {
  return self->rootNode();
}

//  void QScene::setArbiter(QChangeArbiter *arbiter)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene10setArbiterEPNS_14QChangeArbiterE(
    Qt3DCore::QScene *self,
    Qt3DCore::QChangeArbiter *arbiter) {
  self->setArbiter(arbiter);
}

//  QChangeArbiter *QScene::arbiter() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QChangeArbiter *ritual_ZNK8Qt3DCore6QScene7arbiterEv(
    const Qt3DCore::QScene *self) {
  return self->arbiter();
}

//  void QScene::addEntityForComponent(QNodeId componentUuid, QNodeId
//      entityUuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene21addEntityForComponentENS_7QNodeIdES1_(
    Qt3DCore::QScene *self,
    const Qt3DCore::QNodeId *componentUuid,
    const Qt3DCore::QNodeId *entityUuid) {
  self->addEntityForComponent(*componentUuid, *entityUuid);
}

//  void QScene::removeEntityForComponent(QNodeId componentUuid, QNodeId
//      entityUuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene24removeEntityForComponentENS_7QNodeIdES1_(
    Qt3DCore::QScene *self,
    const Qt3DCore::QNodeId *componentUuid,
    const Qt3DCore::QNodeId *entityUuid) {
  self->removeEntityForComponent(*componentUuid, *entityUuid);
}

//  bool QScene::hasEntityForComponent(QNodeId componentUuid, QNodeId
//      entityUuid)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8Qt3DCore6QScene21hasEntityForComponentENS_7QNodeIdES1_(
    Qt3DCore::QScene *self,
    const Qt3DCore::QNodeId *componentUuid,
    const Qt3DCore::QNodeId *entityUuid) {
  return self->hasEntityForComponent(*componentUuid, *entityUuid);
}

//  NodePostConstructorInit *QScene::postConstructorInit() const
extern "C" Q_DECL_EXPORT
Qt3DCore::NodePostConstructorInit *ritual_ZNK8Qt3DCore6QScene19postConstructorInitEv(
    const Qt3DCore::QScene *self) {
  return self->postConstructorInit();
}

//  void QScene::markDirty(DirtyNodeSet changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene9markDirtyE6QFlagsINS0_13DirtyNodeFlagEE(
    Qt3DCore::QScene *self,
    int changes) {
  self->markDirty(
      QFlags<Qt3DCore::QScene::DirtyNodeFlag>::fromInt(changes));
}

//  DirtyNodeSet QScene::dirtyBits()
extern "C" Q_DECL_EXPORT
int ritual_ZN8Qt3DCore6QScene9dirtyBitsEv(
    Qt3DCore::QScene *self) {
  return self->dirtyBits().toInt();
}

//  void QScene::clearDirtyBits()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene14clearDirtyBitsEv(
    Qt3DCore::QScene *self) {
  self->clearDirtyBits();
}

//  void QScene::setRootNode(QNode *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore6QScene11setRootNodeEPNS_5QNodeE(
    Qt3DCore::QScene *self,
    Qt3DCore::QNode *root) {
  self->setRootNode(root);
}

//  QScenePrivate *Qt3DCore::QScene::d_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QScenePrivate *ritual_ZN8Qt3DCore6QScene6d_funcEv(
    Qt3DCore::QScene *self) {
  return self->d_func();
}

//  const QScenePrivate *Qt3DCore::QScene::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QScenePrivate *ritual_ZNK8Qt3DCore6QScene6d_funcEv(
    const Qt3DCore::QScene *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DCore_QScene, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QScene(
    Qt3DCore::QScene *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QScene *>(self)->take(key, call);
}

//  QNode *QScene::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_own_ZNK8Qt3DCore6QScene10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QScene *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DCore::QScene::lookupNode(*id);
}
