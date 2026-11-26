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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/private/scene3dsgmaterial_p.h>
#include <QtCore/qloggingcategory.h>
#include <Qt3DQuickScene3D/private/scene3dsgnode_p.h>
#include <QtCore/qthread.h>
#include <Qt3DQuickScene3D/private/scene3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgmaterial.cpp, line 24, as _ZN10Qt3DRender17Scene3DSGMaterialC1Ev
namespace Qt3DRender {
inline Scene3DSGMaterial::Scene3DSGMaterial()
    : QSGMaterial()
    , m_texture(nullptr)
    , m_visible(false)
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dlogging.cpp, line 10, as _ZN10Qt3DRender7Scene3DEv
namespace Qt3DRender {
inline const QLoggingCategory &Scene3D()
{
    static const QLoggingCategory category("Qt3D.Scene3D", QtWarningMsg);
    return category;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgnode.cpp, line 34, as _ZN10Qt3DRender13Scene3DSGNodeD1Ev
namespace Qt3DRender {
inline Scene3DSGNode::~Scene3DSGNode()
{
    qCDebug(Scene3D) << Q_FUNC_INFO << QThread::currentThread();
    // The Scene3DSGNode is deleted by the QSGRenderThread when the SceneGraph
    // is terminated.
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgnode.cpp, line 41, as _ZN10Qt3DRender13Scene3DSGNode7setRectERK6QRectFb
namespace Qt3DRender {
inline void Scene3DSGNode::setRect(const QRectF &rect, bool mirrorVertically)
{
    if (rect != m_rect) {
        m_rect = rect;
        // By default, map the item's bounding rect to normalized texture coordinates

        QRectF textureRect = QRectF(0.0f, 1.0f, 1.0f, -1.0f);
        if (mirrorVertically) {
            float tmp = textureRect.top();
            textureRect.setTop(textureRect.bottom());
            textureRect.setBottom(tmp);
        }

        QSGGeometry::updateTexturedRectGeometry(&m_geometry, m_rect, textureRect);
        markDirty(DirtyGeometry);
    }
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3dsgnode.cpp, line 59, as _ZN10Qt3DRender13Scene3DSGNode4showEv
namespace Qt3DRender {
inline void Scene3DSGNode::show()
{
    m_material.show();
    m_opaqueMaterial.show();
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

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

//  Qt3DRender::Scene3DSGNode::~Scene3DSGNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13Scene3DSGNodeD1Ev(
    Qt3DRender::Scene3DSGNode *self) {
  delete self;
}

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

//  void Qt3DRender::Scene3DSGNode::setRect(const QRectF &rect, bool
//      mirrorVertically)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13Scene3DSGNode7setRectERK6QRectFb(
    Qt3DRender::Scene3DSGNode *self,
    const QRectF *rect,
    bool mirrorVertically) {
  self->setRect(*rect, mirrorVertically);
}

//  QRectF Qt3DRender::Scene3DSGNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DRender13Scene3DSGNode4rectEv(
    const Qt3DRender::Scene3DSGNode *self) {
  return new QRectF(self->rect());
}

//  void Qt3DRender::Scene3DSGNode::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13Scene3DSGNode4showEv(
    Qt3DRender::Scene3DSGNode *self) {
  self->show();
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
