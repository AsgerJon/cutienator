//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qabstractfrontendnodemanager_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qabstractfrontendnodemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>

//  A Qt3DCore::QAbstractFrontEndNodeManager that Python can take functions over in. Every Qt3DCore::QAbstractFrontEndNodeManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DCore_QAbstractFrontEndNodeManagerCall0)(const void *, const Qt3DCore::QNodeId *, int *);
class CuteQt3DCore_QAbstractFrontEndNodeManager : public Qt3DCore::QAbstractFrontEndNodeManager {
public:
  using Qt3DCore::QAbstractFrontEndNodeManager::QAbstractFrontEndNodeManager;
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
      CuteQt3DCore_QAbstractFrontEndNodeManagerCall0 call = reinterpret_cast<CuteQt3DCore_QAbstractFrontEndNodeManagerCall0>(taken[0]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QNode *>(given);
    }
    return {};
  }
};

//  Qt3DCore::QAbstractFrontEndNodeManager::~QAbstractFrontEndNodeManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore28QAbstractFrontEndNodeManagerD1Ev(
    Qt3DCore::QAbstractFrontEndNodeManager *self) {
  delete self;
}

//  QNode *Qt3DCore::QAbstractFrontEndNodeManager::lookupNode(QNodeId id)
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_ZNK8Qt3DCore28QAbstractFrontEndNodeManager10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QAbstractFrontEndNodeManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupNode(*id);
}

//  QList<QNode *> Qt3DCore::QAbstractFrontEndNodeManager::lookupNodes(const
//      QList<QNodeId> &ids) const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNode *> *ritual_ZNK8Qt3DCore28QAbstractFrontEndNodeManager11lookupNodesERK5QListINS_7QNodeIdEE(
    const Qt3DCore::QAbstractFrontEndNodeManager *self,
    const QList<Qt3DCore::QNodeId> *ids) {
  return new QList<Qt3DCore::QNode *>(self->lookupNodes(*ids));
}

//  a Python function taken by a CuteQt3DCore_QAbstractFrontEndNodeManager,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAbstractFrontEndNodeManager(
    Qt3DCore::QAbstractFrontEndNodeManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAbstractFrontEndNodeManager *>(self)->take(key, call);
}

//  a QList<Qt3DCore::QNode *> a ritual of
//      Qt3DCore::QAbstractFrontEndNodeManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DCore_QAbstractFrontEndNodeManager__QList_Qt3DCore_QNode(
    QList<Qt3DCore::QNode *> *self) {
  delete self;
}
