//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qaspectengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qaspectengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DCore::QAspectEnginePrivate that Python can take functions over in. Every Qt3DCore::QAspectEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DCore_QAspectEnginePrivateCall0)(const void *, const Qt3DCore::QNodeId *, int *);
class CuteQt3DCore_QAspectEnginePrivate : public Qt3DCore::QAspectEnginePrivate {
public:
  using Qt3DCore::QAspectEnginePrivate::QAspectEnginePrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK8Qt3DCore28QAbstractFrontEndNodeManager10lookupNodeENS_7QNodeIdE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QNode *Qt3DCore::QAspectEnginePrivate::lookupNode(QNodeId id) const
  Qt3DCore::QNode *lookupNode(Qt3DCore::QNodeId id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAspectEnginePrivateCall0 call = reinterpret_cast<CuteQt3DCore_QAspectEnginePrivateCall0>(taken[0]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QNode *>(given);
    }
    return Qt3DCore::QAspectEnginePrivate::lookupNode(id);
  }
};

//  Qt3DCore::QAspectEnginePrivate::QAspectEnginePrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEnginePrivate *ritual_ZN8Qt3DCore20QAspectEnginePrivateC1Ev() {
  return new CuteQt3DCore_QAspectEnginePrivate();
}

//  Qt3DCore::QAspectEnginePrivate::~QAspectEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivateD1Ev(
    Qt3DCore::QAspectEnginePrivate *self) {
  delete self;
}

//  QAspectEngine *Qt3DCore::QAspectEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEngine *ritual_ZN8Qt3DCore20QAspectEnginePrivate6q_funcEv(
    Qt3DCore::QAspectEnginePrivate *self) {
  return self->q_func();
}

//  const QAspectEngine *Qt3DCore::QAspectEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAspectEngine *ritual_ZNK8Qt3DCore20QAspectEnginePrivate6q_funcEv(
    const Qt3DCore::QAspectEnginePrivate *self) {
  return self->q_func();
}

//  void Qt3DCore::QAspectEnginePrivate::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate10initializeEv(
    Qt3DCore::QAspectEnginePrivate *self) {
  self->initialize();
}

//  void Qt3DCore::QAspectEnginePrivate::shutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate8shutdownEv(
    Qt3DCore::QAspectEnginePrivate *self) {
  self->shutdown();
}

//  void Qt3DCore::QAspectEnginePrivate::exitSimulationLoop()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate18exitSimulationLoopEv(
    Qt3DCore::QAspectEnginePrivate *self) {
  self->exitSimulationLoop();
}

//  void Qt3DCore::QAspectEnginePrivate::initNodeTree(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate12initNodeTreeEPNS_5QNodeE(
    Qt3DCore::QAspectEnginePrivate *self,
    Qt3DCore::QNode *node) {
  self->initNodeTree(node);
}

//  void Qt3DCore::QAspectEnginePrivate::initNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate8initNodeEPNS_5QNodeE(
    Qt3DCore::QAspectEnginePrivate *self,
    Qt3DCore::QNode *node) {
  self->initNode(node);
}

//  void Qt3DCore::QAspectEnginePrivate::initEntity(QEntity *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate10initEntityEPNS_7QEntityE(
    Qt3DCore::QAspectEnginePrivate *self,
    Qt3DCore::QEntity *entity) {
  self->initEntity(entity);
}

//  void Qt3DCore::QAspectEnginePrivate::addNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate7addNodeEPNS_5QNodeE(
    Qt3DCore::QAspectEnginePrivate *self,
    Qt3DCore::QNode *node) {
  self->addNode(node);
}

//  void Qt3DCore::QAspectEnginePrivate::removeNode(QNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore20QAspectEnginePrivate10removeNodeEPNS_5QNodeE(
    Qt3DCore::QAspectEnginePrivate *self,
    Qt3DCore::QNode *node) {
  self->removeNode(node);
}

//  QNode *Qt3DCore::QAspectEnginePrivate::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore20QAspectEnginePrivate10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QAspectEnginePrivate *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupNode(*id);
}

//  QList<QNode *> Qt3DCore::QAspectEnginePrivate::lookupNodes(const
//      QList<QNodeId> &ids) const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNode *> *ritual_ZNK8Qt3DCore20QAspectEnginePrivate11lookupNodesERK5QListINS_7QNodeIdEE(
    const Qt3DCore::QAspectEnginePrivate *self,
    const QList<Qt3DCore::QNodeId> *ids) {
  return new QList<Qt3DCore::QNode *>(self->lookupNodes(*ids));
}

//  QAspectEnginePrivate *Qt3DCore::QAspectEnginePrivate::get(QAspectEngine
//      *engine)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectEnginePrivate *ritual_ZN8Qt3DCore20QAspectEnginePrivate3getEPNS_13QAspectEngineE(
    Qt3DCore::QAspectEngine *engine) {
  return Qt3DCore::QAspectEnginePrivate::get(engine);
}

//  Qt3DCore::QAspectEnginePrivate as the
//      Qt3DCore::QAbstractFrontEndNodeManager it is built on
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractFrontEndNodeManager *ritual_cast_Qt3DCore_QAspectEnginePrivate_Qt3DCore_QAbstractFrontEndNodeManager(
    Qt3DCore::QAspectEnginePrivate *self) {
  return static_cast<Qt3DCore::QAbstractFrontEndNodeManager *>(self);
}

//  a Python function taken by a CuteQt3DCore_QAspectEnginePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAspectEnginePrivate(
    Qt3DCore::QAspectEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAspectEnginePrivate *>(self)->take(key, call);
}

//  QNode *Qt3DCore::QAspectEnginePrivate::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_own_ZNK8Qt3DCore20QAspectEnginePrivate10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QAspectEnginePrivate *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DCore::QAspectEnginePrivate::lookupNode(*id);
}

//  a QList<Qt3DCore::QNode *> a ritual of Qt3DCore::QAspectEnginePrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAspectEnginePrivate__QList_Qt3DCore_QNode(
    QList<Qt3DCore::QNode *> *self) {
  delete self;
}
