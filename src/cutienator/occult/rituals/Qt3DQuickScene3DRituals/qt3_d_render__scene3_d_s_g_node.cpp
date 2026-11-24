//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DQuickScene3D/Qt3DQuickScene3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3dsgnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>

//  A Qt3DRender::Scene3DSGNode that Python can take functions over in. Every Qt3DRender::Scene3DSGNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DRender_Scene3DSGNodeCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Scene3DSGNodeCall1)(const void *, int *);
class CuteQt3DRender_Scene3DSGNode : public Qt3DRender::Scene3DSGNode {
public:
  using Qt3DRender::Scene3DSGNode::Scene3DSGNode;
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
      CuteQt3DRender_Scene3DSGNodeCall0 call = reinterpret_cast<CuteQt3DRender_Scene3DSGNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Scene3DSGNodeCall1 call = reinterpret_cast<CuteQt3DRender_Scene3DSGNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  void Qt3DRender::Scene3DSGNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13Scene3DSGNode10setTextureEP10QSGTexture(
    Qt3DRender::Scene3DSGNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  QSGTexture *Qt3DRender::Scene3DSGNode::texture() const
extern "C" Q_DECL_EXPORT
QSGTexture *ritual_ZNK10Qt3DRender13Scene3DSGNode7textureEv(
    const Qt3DRender::Scene3DSGNode *self) {
  return self->texture();
}

//  QRectF Qt3DRender::Scene3DSGNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DRender13Scene3DSGNode4rectEv(
    const Qt3DRender::Scene3DSGNode *self) {
  return new QRectF(self->rect());
}

//  a Python function taken by a CuteQt3DRender_Scene3DSGNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Scene3DSGNode(
    Qt3DRender::Scene3DSGNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Scene3DSGNode *>(self)->take(key, call);
}
