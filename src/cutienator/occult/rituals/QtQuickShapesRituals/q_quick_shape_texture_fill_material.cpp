//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#include <QtGui/private/qtriangulator_p.h>
#include <QtGui/private/qtriangulatingstroker_p.h>
#include <rhi/qrhi.h>
#include <QSGVertexColorMaterial>
#include <QSGTextureProvider>
#include <private/qsgplaintexture_p.h>
#include <QtQuick/private/qsggradientcache_p.h>
#if QT_CONFIG(thread)
#include <QtCore/QThreadPool>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1393, as _ZN30QQuickShapeTextureFillMaterialD2Ev
inline QQuickShapeTextureFillMaterial::~QQuickShapeTextureFillMaterial()
{
    delete m_dummyTexture;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1422, as _ZNK30QQuickShapeTextureFillMaterial12createShaderEN20QSGRendererInterface10RenderModeE
inline QSGMaterialShader *QQuickShapeTextureFillMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new QQuickShapeTextureFillRhiShader(viewCount());
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1398, as _ZNK30QQuickShapeTextureFillMaterial4typeEv
inline QSGMaterialType *QQuickShapeTextureFillMaterial::type() const
{
    static QSGMaterialType type;
    return &type;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1404, as _ZNK30QQuickShapeTextureFillMaterial7compareEPK11QSGMaterial
inline int QQuickShapeTextureFillMaterial::compare(const QSGMaterial *other) const
{
    Q_ASSERT(other && type() == other->type());
    const QQuickShapeTextureFillMaterial *m = static_cast<const QQuickShapeTextureFillMaterial *>(other);

    QQuickShapeGenericStrokeFillNode *a = node();
    QQuickShapeGenericStrokeFillNode *b = m->node();
    Q_ASSERT(a && b);
    if (a == b)
        return 0;

    if (int d = a->m_fillTransform.compareTo(b->m_fillTransform))
        return d;

    const qintptr diff = qintptr(a->m_fillTextureProvider) - qintptr(b->m_fillTextureProvider);
    return diff < 0 ? -1 : (diff > 0 ? 1 : 0);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1295, as _ZN31QQuickShapeTextureFillRhiShaderC1Ei
inline QQuickShapeTextureFillRhiShader::QQuickShapeTextureFillRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/texturefill.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/shapes/shaders_ng/texturefill.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1301, as _ZN31QQuickShapeTextureFillRhiShader17updateUniformDataERN17QSGMaterialShader11RenderStateEP11QSGMaterialS4_
inline bool QQuickShapeTextureFillRhiShader::updateUniformData(RenderState &state,
                                                        QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickShapeTextureFillMaterial *m = static_cast<QQuickShapeTextureFillMaterial *>(newMaterial);
    bool changed = false;
    QByteArray *buf = state.uniformData();
    const int shaderMatrixCount = newMaterial->viewCount();
    const int matrixCount = qMin(state.projectionMatrixCount(), shaderMatrixCount);
    Q_ASSERT(buf->size() >= 64 * shaderMatrixCount + 64 + 8 + 4);

    if (state.isMatrixDirty()) {
        for (int viewIndex = 0; viewIndex < matrixCount; ++viewIndex) {
            const QMatrix4x4 m = state.combinedMatrix();
            memcpy(buf->data() + 64 * viewIndex, m.constData(), 64);
            changed = true;
        }
    }

    QQuickShapeGenericStrokeFillNode *node = m->node();

    if (!oldMaterial || m_fillTransform != node->m_fillTransform) {
        memcpy(buf->data() + 64 * shaderMatrixCount, node->m_fillTransform.invertedData(), 64);
        m_fillTransform = node->m_fillTransform;
        changed = true;
    }

    const QSizeF boundsSize = node->m_fillTextureProvider != nullptr && node->m_fillTextureProvider->texture() != nullptr
        ? node->m_fillTextureProvider->texture()->textureSize()
        : QSizeF(0, 0);


    const QVector2D boundsVector(boundsSize.width() / state.devicePixelRatio(),
                                 boundsSize.height() / state.devicePixelRatio());
    if (!oldMaterial || m_boundsSize != boundsVector) {
        m_boundsSize = boundsVector;
        Q_ASSERT(sizeof(m_boundsSize) == 8);
        memcpy(buf->data() + 64 * shaderMatrixCount + 64, &m_boundsSize, 8);
        changed = true;
    }

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount + 64 + 8, &opacity, 4);
        changed = true;
    }

    return changed;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 1351, as _ZN31QQuickShapeTextureFillRhiShader18updateSampledImageERN17QSGMaterialShader11RenderStateEiPP10QSGTextureP11QSGMaterialS7_
inline void QQuickShapeTextureFillRhiShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                         QSGMaterial *newMaterial, QSGMaterial *)
{
    if (binding != 1)
        return;

    QQuickShapeTextureFillMaterial *m = static_cast<QQuickShapeTextureFillMaterial *>(newMaterial);
    QQuickShapeGenericStrokeFillNode *node = m->node();
    if (node->m_fillTextureProvider != nullptr) {
        QSGTexture *providedTexture = node->m_fillTextureProvider->texture();
        if (providedTexture != nullptr) {
            if (providedTexture->isAtlasTexture()) {
                // Create a non-atlas copy to make texture coordinate wrapping work. This
                // texture copy is owned by the QSGTexture so memory is managed with the original
                // texture provider.
                QSGTexture *newTexture = providedTexture->removedFromAtlas(state.resourceUpdateBatch());
                if (newTexture != nullptr)
                    providedTexture = newTexture;
            }

            providedTexture->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
            *texture = providedTexture;
            return;
        }
    }

    if (m->dummyTexture() == nullptr) {
        QSGPlainTexture *dummyTexture = new QSGPlainTexture;
        dummyTexture->setFiltering(QSGTexture::Nearest);
        dummyTexture->setHorizontalWrapMode(QSGTexture::Repeat);
        dummyTexture->setVerticalWrapMode(QSGTexture::Repeat);
        QImage img(128, 128, QImage::Format_ARGB32_Premultiplied);
        img.fill(0);
        dummyTexture->setImage(img);
        dummyTexture->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());

        m->setDummyTexture(dummyTexture);
    }

    *texture = m->dummyTexture();
}
//  -----------------------------------------------------------------------

//  A QQuickShapeTextureFillMaterial that Python can take functions over in. Every QQuickShapeTextureFillMaterial
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickShapeTextureFillMaterialCall0)(const void *, int *);
typedef int (*CuteQQuickShapeTextureFillMaterialCall1)(const void *, const QSGMaterial *, int *);
typedef void * (*CuteQQuickShapeTextureFillMaterialCall2)(const void *, int, int *);
class CuteQQuickShapeTextureFillMaterial : public QQuickShapeTextureFillMaterial {
public:
  using QQuickShapeTextureFillMaterial::QQuickShapeTextureFillMaterial;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QSGMaterial4typeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial7compareEPKS_")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGMaterial12createShaderEN20QSGRendererInterface10RenderModeE")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QSGMaterialType *QQuickShapeTextureFillMaterial::type() const
  QSGMaterialType *type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeTextureFillMaterialCall0 call = reinterpret_cast<CuteQQuickShapeTextureFillMaterialCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGMaterialType *>(given);
    }
    return QQuickShapeTextureFillMaterial::type();
  }

  //  int QQuickShapeTextureFillMaterial::compare(const QSGMaterial *other)
  //      const
  int compare(const QSGMaterial *other) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeTextureFillMaterialCall1 call = reinterpret_cast<CuteQQuickShapeTextureFillMaterialCall1>(taken[1]);
      int given = call(this, other, &handled);
      if (handled) return given;
    }
    return QQuickShapeTextureFillMaterial::compare(other);
  }

  //  QSGMaterialShader *QQuickShapeTextureFillMaterial::createShader(QSGRe
  //      ndererInterface::RenderMode renderMode) const
  QSGMaterialShader *createShader(
      QSGRendererInterface::RenderMode renderMode) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapeTextureFillMaterialCall2 call = reinterpret_cast<CuteQQuickShapeTextureFillMaterialCall2>(taken[2]);
      void * given = call(this, static_cast<int>(renderMode), &handled);
      if (handled) return static_cast<QSGMaterialShader *>(given);
    }
    return QQuickShapeTextureFillMaterial::createShader(renderMode);
  }
};

//  QQuickShapeTextureFillMaterial::QQuickShapeTextureFillMaterial(QQuickShap
//      eGenericStrokeFillNode *node)
extern "C" Q_DECL_EXPORT
QQuickShapeTextureFillMaterial *ritual_ZN30QQuickShapeTextureFillMaterialC1EP32QQuickShapeGenericStrokeFillNode(
    QQuickShapeGenericStrokeFillNode *node) {
  return new CuteQQuickShapeTextureFillMaterial(node);
}

//  QQuickShapeTextureFillMaterial::~QQuickShapeTextureFillMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickShapeTextureFillMaterialD1Ev(
    QQuickShapeTextureFillMaterial *self) {
  delete self;
}

//  QSGMaterialType *QQuickShapeTextureFillMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_ZNK30QQuickShapeTextureFillMaterial4typeEv(
    const QQuickShapeTextureFillMaterial *self) {
  return self->type();
}

//  int QQuickShapeTextureFillMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QQuickShapeTextureFillMaterial7compareEPK11QSGMaterial(
    const QQuickShapeTextureFillMaterial *self,
    const QSGMaterial *other) {
  return self->compare(other);
}

//  QSGMaterialShader *QQuickShapeTextureFillMaterial::createShader(QSGRender
//      erInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_ZNK30QQuickShapeTextureFillMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QQuickShapeTextureFillMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->createShader(renderMode);
}

//  QQuickShapeGenericStrokeFillNode *QQuickShapeTextureFillMaterial::node()
//      const
extern "C" Q_DECL_EXPORT
QQuickShapeGenericStrokeFillNode *ritual_ZNK30QQuickShapeTextureFillMaterial4nodeEv(
    const QQuickShapeTextureFillMaterial *self) {
  return self->node();
}

//  QSGPlainTexture *QQuickShapeTextureFillMaterial::dummyTexture() const
extern "C" Q_DECL_EXPORT
QSGPlainTexture *ritual_ZNK30QQuickShapeTextureFillMaterial12dummyTextureEv(
    const QQuickShapeTextureFillMaterial *self) {
  return self->dummyTexture();
}

//  void QQuickShapeTextureFillMaterial::setDummyTexture(QSGPlainTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickShapeTextureFillMaterial15setDummyTextureEP15QSGPlainTexture(
    QQuickShapeTextureFillMaterial *self,
    QSGPlainTexture *texture) {
  self->setDummyTexture(texture);
}

//  a Python function taken by a CuteQQuickShapeTextureFillMaterial, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeTextureFillMaterial(
    QQuickShapeTextureFillMaterial *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeTextureFillMaterial *>(self)->take(key, call);
}

//  QSGMaterialType *QQuickShapeTextureFillMaterial::type() const
extern "C" Q_DECL_EXPORT
QSGMaterialType *ritual_own_ZNK30QQuickShapeTextureFillMaterial4typeEv(
    const QQuickShapeTextureFillMaterial *self) {
  return self->QQuickShapeTextureFillMaterial::type();
}

//  int QQuickShapeTextureFillMaterial::compare(const QSGMaterial *other)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK30QQuickShapeTextureFillMaterial7compareEPK11QSGMaterial(
    const QQuickShapeTextureFillMaterial *self,
    const QSGMaterial *other) {
  return self->QQuickShapeTextureFillMaterial::compare(other);
}

//  QSGMaterialShader *QQuickShapeTextureFillMaterial::createShader(QSGRender
//      erInterface::RenderMode renderMode) const
extern "C" Q_DECL_EXPORT
QSGMaterialShader *ritual_own_ZNK30QQuickShapeTextureFillMaterial12createShaderEN20QSGRendererInterface10RenderModeE(
    const QQuickShapeTextureFillMaterial *self,
    QSGRendererInterface::RenderMode renderMode) {
  return self->QQuickShapeTextureFillMaterial::createShader(renderMode);
}
