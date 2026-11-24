//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapscene_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A QGeoTiledMapRootNode that Python can take functions over in. Every QGeoTiledMapRootNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoTiledMapRootNodeCall0)(const void *, int *);
typedef void (*CuteQGeoTiledMapRootNodeCall1)(const void *, int *);
class CuteQGeoTiledMapRootNode : public QGeoTiledMapRootNode {
public:
  using QGeoTiledMapRootNode::QGeoTiledMapRootNode;
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
      CuteQGeoTiledMapRootNodeCall0 call = reinterpret_cast<CuteQGeoTiledMapRootNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMapRootNodeCall1 call = reinterpret_cast<CuteQGeoTiledMapRootNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QGeoTiledMapRootNode::QGeoTiledMapRootNode()
extern "C" Q_DECL_EXPORT
QGeoTiledMapRootNode *ritual_ZN20QGeoTiledMapRootNodeC1Ev() {
  return new CuteQGeoTiledMapRootNode();
}

//  QGeoTiledMapRootNode::~QGeoTiledMapRootNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoTiledMapRootNodeD1Ev(QGeoTiledMapRootNode *self) {
  delete self;
}

//  void QGeoTiledMapRootNode::setClipRect(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoTiledMapRootNode11setClipRectERK5QRect(
    QGeoTiledMapRootNode *self,
    const QRect *rect) {
  self->setClipRect(*rect);
}

//  void QGeoTiledMapRootNode::updateTiles(QGeoTiledMapTileContainerNode
//      *root, QGeoTiledMapScenePrivate *d, double camAdjust, QQuickWindow
//      *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QGeoTiledMapRootNode11updateTilesEP29QGeoTiledMapTileContainerNodeP24QGeoTiledMapScenePrivatedP12QQuickWindow(
    QGeoTiledMapRootNode *self,
    QGeoTiledMapTileContainerNode *root,
    QGeoTiledMapScenePrivate *d,
    double camAdjust,
    QQuickWindow *window) {
  self->updateTiles(root, d, camAdjust, window);
}

//  a Python function taken by a CuteQGeoTiledMapRootNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMapRootNode(
    QGeoTiledMapRootNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMapRootNode *>(self)->take(key, call);
}
