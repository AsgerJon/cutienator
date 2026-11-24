//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qscene_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qscene_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DCore::QScene that Python can take functions over in. Every Qt3DCore::QScene
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
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

  //  QNode *Qt3DCore::QScene::lookupNode(QNodeId id) const
  Qt3DCore::QNode *lookupNode(Qt3DCore::QNodeId id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QSceneCall0 call = reinterpret_cast<CuteQt3DCore_QSceneCall0>(taken[0]);
      void * given = call(this, &id, &handled);
      if (handled) return static_cast<Qt3DCore::QNode *>(given);
    }
    return Qt3DCore::QScene::lookupNode(id);
  }
};

//  a Python function taken by a CuteQt3DCore_QScene, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QScene(
    Qt3DCore::QScene *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QScene *>(self)->take(key, call);
}

//  QNode *Qt3DCore::QScene::lookupNode(QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNode *ritual_own_ZNK8Qt3DCore6QScene10lookupNodeENS_7QNodeIdE(
    const Qt3DCore::QScene *self,
    const Qt3DCore::QNodeId *id) {
  return self->Qt3DCore::QScene::lookupNode(*id);
}
