//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QGeoTiledMapTileContainerNode that Python can take functions over in. Every QGeoTiledMapTileContainerNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoTiledMapTileContainerNodeCall0)(const void *, int *);
typedef void (*CuteQGeoTiledMapTileContainerNodeCall1)(const void *, int *);
class CuteQGeoTiledMapTileContainerNode : public QGeoTiledMapTileContainerNode {
public:
  using QGeoTiledMapTileContainerNode::QGeoTiledMapTileContainerNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTiledMapTileContainerNodeCall0 call = reinterpret_cast<CuteQGeoTiledMapTileContainerNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMapTileContainerNodeCall1 call = reinterpret_cast<CuteQGeoTiledMapTileContainerNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  void QGeoTiledMapTileContainerNode::addChild(const QGeoTileSpec &spec,
//      QSGImageNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMapTileContainerNode8addChildERK12QGeoTileSpecP12QSGImageNode(
    QGeoTiledMapTileContainerNode *self,
    const QGeoTileSpec *spec,
    QSGImageNode *node) {
  self->addChild(*spec, node);
}

//  a Python function taken by a CuteQGeoTiledMapTileContainerNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMapTileContainerNode(
    QGeoTiledMapTileContainerNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMapTileContainerNode *>(self)->take(key, call);
}
