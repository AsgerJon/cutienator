//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, instances of templates of the
//  class: 3. Kept as it is when the generator runs again.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobjectdefs.h>
#include <cstring>
#include <vector>
#include <Qt3DCore/qbackendnode.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/qcomponent.h>

//  A Qt3DCore::QAbstractAspectPrivate that Python can take functions over in. Every Qt3DCore::QAbstractAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DCore_QAbstractAspectPrivateCall3)(const void *, int *);
class CuteQt3DCore_QAbstractAspectPrivate : public Qt3DCore::QAbstractAspectPrivate {
public:
  using Qt3DCore::QAbstractAspectPrivate::QAbstractAspectPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::frameDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectPrivateCall2 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DCore_QAbstractAspectPrivateCall3 call = reinterpret_cast<CuteQt3DCore_QAbstractAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  Qt3DCore::QAbstractAspectPrivate::QAbstractAspectPrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspectPrivate *ritual_ZN8Qt3DCore22QAbstractAspectPrivateC1Ev() {
  return new CuteQt3DCore_QAbstractAspectPrivate();
}

//  Qt3DCore::QAbstractAspectPrivate::~QAbstractAspectPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivateD1Ev(
    Qt3DCore::QAbstractAspectPrivate *self) {
  delete self;
}

//  void Qt3DCore::QAbstractAspectPrivate::setRootAndCreateNodes(QEntity
//      *rootObject, const QList<NodeTreeChange> &nodesTreeChanges)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate21setRootAndCreateNodesEPNS_7QEntityERK5QListINS_14NodeTreeChangeEE(
    Qt3DCore::QAbstractAspectPrivate *self,
    Qt3DCore::QEntity *rootObject,
    const QList<Qt3DCore::NodeTreeChange> *nodesTreeChanges) {
  self->setRootAndCreateNodes(rootObject, *nodesTreeChanges);
}

//  QServiceLocator *Qt3DCore::QAbstractAspectPrivate::services() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QServiceLocator *ritual_ZNK8Qt3DCore22QAbstractAspectPrivate8servicesEv(
    const Qt3DCore::QAbstractAspectPrivate *self) {
  return self->services();
}

//  QAbstractAspectJobManager *Qt3DCore::QAbstractAspectPrivate::jobManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspectJobManager *ritual_ZNK8Qt3DCore22QAbstractAspectPrivate10jobManagerEv(
    const Qt3DCore::QAbstractAspectPrivate *self) {
  return self->jobManager();
}

//  std::vector<QAspectJobPtr>
//      Qt3DCore::QAbstractAspectPrivate::jobsToExecute(qint64 time)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QAspectJobPtr> *ritual_ZN8Qt3DCore22QAbstractAspectPrivate13jobsToExecuteEx(
    Qt3DCore::QAbstractAspectPrivate *self,
    qint64 time) {
  return new std::vector<Qt3DCore::QAspectJobPtr>(self->jobsToExecute(time));
}

//  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate8jobsDoneEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->jobsDone();
}

//  void Qt3DCore::QAbstractAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate9frameDoneEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->frameDone();
}

//  QBackendNode *Qt3DCore::QAbstractAspectPrivate::createBackendNode(const
//      NodeTreeChange &change) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNode *ritual_ZNK8Qt3DCore22QAbstractAspectPrivate17createBackendNodeERKNS_14NodeTreeChangeE(
    const Qt3DCore::QAbstractAspectPrivate *self,
    const Qt3DCore::NodeTreeChange *change) {
  return self->createBackendNode(*change);
}

//  void Qt3DCore::QAbstractAspectPrivate::clearBackendNode(const
//      NodeTreeChange &change) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8Qt3DCore22QAbstractAspectPrivate16clearBackendNodeERKNS_14NodeTreeChangeE(
    const Qt3DCore::QAbstractAspectPrivate *self,
    const Qt3DCore::NodeTreeChange *change) {
  self->clearBackendNode(*change);
}

//  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNodes(const
//      QList<QNode *> &nodes)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate22syncDirtyFrontEndNodesERK5QListIPNS_5QNodeEE(
    Qt3DCore::QAbstractAspectPrivate *self,
    const QList<Qt3DCore::QNode *> *nodes) {
  self->syncDirtyFrontEndNodes(*nodes);
}

//  void
//      Qt3DCore::QAbstractAspectPrivate::syncDirtyEntityComponentNodes(const
//      QList<ComponentRelationshipChange> &nodes)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate29syncDirtyEntityComponentNodesERK5QListINS_27ComponentRelationshipChangeEE(
    Qt3DCore::QAbstractAspectPrivate *self,
    const QList<Qt3DCore::ComponentRelationshipChange> *nodes) {
  self->syncDirtyEntityComponentNodes(*nodes);
}

//  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode *node,
//      QBackendNode *backend, bool firstTime) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb(
    const Qt3DCore::QAbstractAspectPrivate *self,
    Qt3DCore::QNode *node,
    Qt3DCore::QBackendNode *backend,
    bool firstTime) {
  self->syncDirtyFrontEndNode(node, backend, firstTime);
}

//  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->onEngineAboutToShutdown();
}

//  void Qt3DCore::QAbstractAspectPrivate::unregisterBackendType(const
//      QMetaObject &mo)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate21unregisterBackendTypeERK11QMetaObject(
    Qt3DCore::QAbstractAspectPrivate *self,
    const QMetaObject *mo) {
  self->unregisterBackendType(*mo);
}

//  QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspect *ritual_ZN8Qt3DCore22QAbstractAspectPrivate6q_funcEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  return self->q_func();
}

//  const QAbstractAspect *Qt3DCore::QAbstractAspectPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAbstractAspect *ritual_ZNK8Qt3DCore22QAbstractAspectPrivate6q_funcEv(
    const Qt3DCore::QAbstractAspectPrivate *self) {
  return self->q_func();
}

//  QBackendNodeMapperPtr
//      Qt3DCore::QAbstractAspectPrivate::mapperForNode(const QMetaObject
//      *metaObj) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QBackendNodeMapperPtr *ritual_ZNK8Qt3DCore22QAbstractAspectPrivate13mapperForNodeEPK11QMetaObject(
    const Qt3DCore::QAbstractAspectPrivate *self,
    const QMetaObject *metaObj) {
  return new Qt3DCore::QBackendNodeMapperPtr(self->mapperForNode(metaObj));
}

//  QAbstractAspectPrivate
//      *Qt3DCore::QAbstractAspectPrivate::get(QAbstractAspect *aspect)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAbstractAspectPrivate *ritual_ZN8Qt3DCore22QAbstractAspectPrivate3getEPNS_15QAbstractAspectE(
    Qt3DCore::QAbstractAspect *aspect) {
  return Qt3DCore::QAbstractAspectPrivate::get(aspect);
}

//  Qt3DCore::QAbstractAspectPrivate as the
//      Qt3DCore::QAspectJobProviderInterface it is built on
extern "C" Q_DECL_EXPORT
Qt3DCore::QAspectJobProviderInterface *ritual_cast_Qt3DCore_QAbstractAspectPrivate_Qt3DCore_QAspectJobProviderInterface(
    Qt3DCore::QAbstractAspectPrivate *self) {
  return static_cast<Qt3DCore::QAspectJobProviderInterface *>(self);
}

//  a Python function taken by a CuteQt3DCore_QAbstractAspectPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractAspectPrivate(
    Qt3DCore::QAbstractAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractAspectPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate8jobsDoneEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->Qt3DCore::QAbstractAspectPrivate::jobsDone();
}

//  void Qt3DCore::QAbstractAspectPrivate::frameDone()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate9frameDoneEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->Qt3DCore::QAbstractAspectPrivate::frameDone();
}

//  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode *node,
//      QBackendNode *backend, bool firstTime) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb(
    const Qt3DCore::QAbstractAspectPrivate *self,
    Qt3DCore::QNode *node,
    Qt3DCore::QBackendNode *backend,
    bool firstTime) {
  self->Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(
      node,
      backend,
      firstTime);
}

//  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DCore::QAbstractAspectPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAbstractAspectPrivate__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}

//  a Qt3DCore::QBackendNodeMapperPtr a ritual of
//      Qt3DCore::QAbstractAspectPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAbstractAspectPrivate__Qt3DCore_QBackendNodeMapperPtr(
    Qt3DCore::QBackendNodeMapperPtr *self) {
  delete self;
}

//  void
//      Qt3DCore::QAbstractAspectPrivate::unregisterBackendType<Qt3DCore::QNode>()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate21unregisterBackendTypeINS_5QNodeEEEvv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->unregisterBackendType<Qt3DCore::QNode>();
}

//  void
//      Qt3DCore::QAbstractAspectPrivate::unregisterBackendType<Qt3DCore::QEntity>()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate21unregisterBackendTypeINS_7QEntityEEEvv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->unregisterBackendType<Qt3DCore::QEntity>();
}

//  void
//      Qt3DCore::QAbstractAspectPrivate::unregisterBackendType<Qt3DCore::QComponent>()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QAbstractAspectPrivate21unregisterBackendTypeINS_10QComponentEEEvv(
    Qt3DCore::QAbstractAspectPrivate *self) {
  self->unregisterBackendType<Qt3DCore::QComponent>();
}
