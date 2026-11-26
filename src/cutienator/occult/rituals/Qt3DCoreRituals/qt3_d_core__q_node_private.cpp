//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A Qt3DCore::QNodePrivate that Python can take functions over in. Every Qt3DCore::QNodePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QNodePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QNodePrivateCall1)(const void *, int *);
class CuteQt3DCore_QNodePrivate : public Qt3DCore::QNodePrivate {
public:
  using Qt3DCore::QNodePrivate::QNodePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QNodePrivateCall0 call = reinterpret_cast<CuteQt3DCore_QNodePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QNodePrivateCall1 call = reinterpret_cast<CuteQt3DCore_QNodePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DCore::QNodePrivate::QNodePrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodePrivate *ritual_ZN8Qt3DCore12QNodePrivateC1Ev() {
  return new CuteQt3DCore_QNodePrivate();
}

//  Qt3DCore::QNodePrivate::~QNodePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivateD1Ev(Qt3DCore::QNodePrivate *self) {
  delete self;
}

//  void Qt3DCore::QNodePrivate::init(QNode *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate4initEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *parent) {
  self->init(parent);
}

//  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  QScene *Qt3DCore::QNodePrivate::scene() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QScene *ritual_ZNK8Qt3DCore12QNodePrivate5sceneEv(
    const Qt3DCore::QNodePrivate *self) {
  return self->scene();
}

//  void Qt3DCore::QNodePrivate::setArbiter(QChangeArbiter *arbiter)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate10setArbiterEPNS_14QChangeArbiterE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QChangeArbiter *arbiter) {
  self->setArbiter(arbiter);
}

//  void Qt3DCore::QNodePrivate::notifyPropertyChange(const char *name, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate20notifyPropertyChangeEPKcRK8QVariant(
    Qt3DCore::QNodePrivate *self,
    const char *name,
    const QVariant *value) {
  self->notifyPropertyChange(name, *value);
}

//  void Qt3DCore::QNodePrivate::notifyDynamicPropertyChange(const QByteArray
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate27notifyDynamicPropertyChangeERK10QByteArrayRK8QVariant(
    Qt3DCore::QNodePrivate *self,
    const QByteArray *name,
    const QVariant *value) {
  self->notifyDynamicPropertyChange(*name, *value);
}

//  void Qt3DCore::QNodePrivate::insertTree(QNode *treeRoot, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate10insertTreeEPNS_5QNodeEi(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *treeRoot,
    int depth) {
  self->insertTree(treeRoot, depth);
}

//  void Qt3DCore::QNodePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate6updateEv(
    Qt3DCore::QNodePrivate *self) {
  self->update();
}

//  void Qt3DCore::QNodePrivate::markDirty(QScene::DirtyNodeSet changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate9markDirtyE6QFlagsINS_6QScene13DirtyNodeFlagEE(
    Qt3DCore::QNodePrivate *self,
    int changes) {
  self->markDirty(QFlags<Qt3DCore::QScene::DirtyNodeFlag>::fromInt(changes));
}

//  QNode *Qt3DCore::QNodePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZN8Qt3DCore12QNodePrivate6q_funcEv(
    Qt3DCore::QNodePrivate *self) {
  return self->q_func();
}

//  const QNode *Qt3DCore::QNodePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QNode *ritual_ZNK8Qt3DCore12QNodePrivate6q_funcEv(
    const Qt3DCore::QNodePrivate *self) {
  return self->q_func();
}

//  QNodePrivate *Qt3DCore::QNodePrivate::get(QNode *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodePrivate *ritual_ZN8Qt3DCore12QNodePrivate3getEPNS_5QNodeE(
    Qt3DCore::QNode *q) {
  return Qt3DCore::QNodePrivate::get(q);
}

//  const QNodePrivate *Qt3DCore::QNodePrivate::get(const QNode *q)
extern "C" Q_DECL_EXPORT
const Qt3DCore::QNodePrivate *ritual_ZN8Qt3DCore12QNodePrivate3getEPKNS_5QNodeE(
    const Qt3DCore::QNode *q) {
  return Qt3DCore::QNodePrivate::get(q);
}

//  void Qt3DCore::QNodePrivate::nodePtrDeleter(QNode *q)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate14nodePtrDeleterEPNS_5QNodeE(
    Qt3DCore::QNode *q) {
  Qt3DCore::QNodePrivate::nodePtrDeleter(q);
}

//  void Qt3DCore::QNodePrivate::unregisterDestructionHelper(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate27unregisterDestructionHelperEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *node) {
  self->unregisterDestructionHelper(node);
}

//  const QMetaObject *Qt3DCore::QNodePrivate::findStaticMetaObject(const
//      QMetaObject *metaObject)
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN8Qt3DCore12QNodePrivate20findStaticMetaObjectEPK11QMetaObject(
    const QMetaObject *metaObject) {
  return Qt3DCore::QNodePrivate::findStaticMetaObject(metaObject);
}

//  void Qt3DCore::QNodePrivate::_q_postConstructorInit()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate22_q_postConstructorInitEv(
    Qt3DCore::QNodePrivate *self) {
  self->_q_postConstructorInit();
}

//  void Qt3DCore::QNodePrivate::_q_ensureBackendNodeCreated()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate27_q_ensureBackendNodeCreatedEv(
    Qt3DCore::QNodePrivate *self) {
  self->_q_ensureBackendNodeCreated();
}

//  void Qt3DCore::QNodePrivate::createBackendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate17createBackendNodeEv(
    Qt3DCore::QNodePrivate *self) {
  self->createBackendNode();
}

//  void Qt3DCore::QNodePrivate::notifyDestructionChangesAndRemoveFromScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate42notifyDestructionChangesAndRemoveFromSceneEv(
    Qt3DCore::QNodePrivate *self) {
  self->notifyDestructionChangesAndRemoveFromScene();
}

//  void Qt3DCore::QNodePrivate::_q_addChild(QNode *childNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate11_q_addChildEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *childNode) {
  self->_q_addChild(childNode);
}

//  void Qt3DCore::QNodePrivate::_q_removeChild(QNode *childNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate14_q_removeChildEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *childNode) {
  self->_q_removeChild(childNode);
}

//  void Qt3DCore::QNodePrivate::_q_setParentHelper(QNode *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate18_q_setParentHelperEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *parent) {
  self->_q_setParentHelper(parent);
}

//  void Qt3DCore::QNodePrivate::registerNotifiedProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate26registerNotifiedPropertiesEv(
    Qt3DCore::QNodePrivate *self) {
  self->registerNotifiedProperties();
}

//  void Qt3DCore::QNodePrivate::unregisterNotifiedProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate28unregisterNotifiedPropertiesEv(
    Qt3DCore::QNodePrivate *self) {
  self->unregisterNotifiedProperties();
}

//  void Qt3DCore::QNodePrivate::propertyChanged(int propertyIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate15propertyChangedEi(
    Qt3DCore::QNodePrivate *self,
    int propertyIndex) {
  self->propertyChanged(propertyIndex);
}

//  void Qt3DCore::QNodePrivate::setSceneHelper(QNode *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate14setSceneHelperEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *root) {
  self->setSceneHelper(root);
}

//  void Qt3DCore::QNodePrivate::unsetSceneHelper(QNode *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate16unsetSceneHelperEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *root) {
  self->unsetSceneHelper(root);
}

//  void Qt3DCore::QNodePrivate::addEntityComponentToScene(QNode *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore12QNodePrivate25addEntityComponentToSceneEPNS_5QNodeE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QNode *root) {
  self->addEntityComponentToScene(root);
}

//  a Python function taken by a CuteQt3DCore_QNodePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QNodePrivate(
    Qt3DCore::QNodePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QNodePrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE(
    Qt3DCore::QNodePrivate *self,
    Qt3DCore::QScene *scene) {
  self->Qt3DCore::QNodePrivate::setScene(scene);
}

//  void Qt3DCore::QNodePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore12QNodePrivate6updateEv(
    Qt3DCore::QNodePrivate *self) {
  self->Qt3DCore::QNodePrivate::update();
}
