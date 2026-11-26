//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgdefaultspritenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgdefaultspritenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgdefaultspritenode_p.h>
#include <QtQuick/QSGMaterial>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 11, as local:qsgdefaultspritenode.cpp:SpriteVertex
struct SpriteVertex {
    float x;
    float y;
    float tx;
    float ty;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 25, as local:qsgdefaultspritenode.cpp:QQuickSpriteMaterial
class QQuickSpriteMaterial : public QSGMaterial
{
public:
    QQuickSpriteMaterial();
    ~QQuickSpriteMaterial();
    QSGMaterialType *type() const  override { static QSGMaterialType type; return &type; }
    QSGMaterialShader *createShader(QSGRendererInterface::RenderMode renderMode) const override;

    QSGTexture *texture = nullptr;

    float animT = 0.0f;
    float animX1 = 0.0f;
    float animY1 = 0.0f;
    float animX2 = 0.0f;
    float animY2 = 0.0f;
    float animW = 1.0f;
    float animH = 1.0f;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 44, as local:qsgdefaultspritenode.cpp:QQuickSpriteMaterial::QQuickSpriteMaterial
inline QQuickSpriteMaterial::QQuickSpriteMaterial()
{
    setFlag(Blending, true);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 49, as local:qsgdefaultspritenode.cpp:QQuickSpriteMaterial::~QQuickSpriteMaterial
inline QQuickSpriteMaterial::~QQuickSpriteMaterial()
{
    delete texture;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 54, as local:qsgdefaultspritenode.cpp:SpriteMaterialRhiShader
class SpriteMaterialRhiShader : public QSGMaterialShader
{
public:
     SpriteMaterialRhiShader(int viewCount);

     bool updateUniformData(RenderState &state,
                            QSGMaterial *newMaterial, QSGMaterial *oldMaterial) override;
     void updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                             QSGMaterial *newMaterial, QSGMaterial *oldMaterial) override;
};

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 65, as local:qsgdefaultspritenode.cpp:SpriteMaterialRhiShader::SpriteMaterialRhiShader
inline SpriteMaterialRhiShader::SpriteMaterialRhiShader(int viewCount)
{
    setShaderFileName(VertexStage, QStringLiteral(":/qt-project.org/scenegraph/shaders_ng/sprite.vert.qsb"), viewCount);
    setShaderFileName(FragmentStage, QStringLiteral(":/qt-project.org/scenegraph/shaders_ng/sprite.frag.qsb"), viewCount);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 71, as local:qsgdefaultspritenode.cpp:SpriteMaterialRhiShader::updateUniformData
inline bool SpriteMaterialRhiShader::updateUniformData(RenderState &state,
                                                QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
#ifdef QT_NO_DEBUG
    Q_UNUSED(oldMaterial);
#endif
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickSpriteMaterial *mat = static_cast<QQuickSpriteMaterial *>(newMaterial);

    bool changed = false;
    QByteArray *buf = state.uniformData();
    Q_ASSERT(buf->size() >= 96);

    const int shaderMatrixCount = newMaterial->viewCount();
    const int matrixCount = qMin(state.projectionMatrixCount(), shaderMatrixCount);
    for (int viewIndex = 0; viewIndex < matrixCount; ++viewIndex) {
        if (state.isMatrixDirty()) {
            const QMatrix4x4 m = state.combinedMatrix(viewIndex);
            memcpy(buf->data() + 64 * viewIndex, m.constData(), 64);
            changed = true;
        }
    }

    float animPosAndData[7] = { mat->animX1, mat->animY1, mat->animX2, mat->animY2,
                                mat->animW, mat->animH, mat->animT };
    memcpy(buf->data() + 64 * shaderMatrixCount, animPosAndData, 28);
    changed = true;

    if (state.isOpacityDirty()) {
        const float opacity = state.opacity();
        memcpy(buf->data() + 64 * shaderMatrixCount + 16 + 12, &opacity, 4);
        changed = true;
    }

    return changed;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 108, as local:qsgdefaultspritenode.cpp:SpriteMaterialRhiShader::updateSampledImage
inline void SpriteMaterialRhiShader::updateSampledImage(RenderState &state, int binding, QSGTexture **texture,
                                                 QSGMaterial *newMaterial, QSGMaterial *oldMaterial)
{
    if (binding != 1)
        return;

#ifdef QT_NO_DEBUG
    Q_UNUSED(oldMaterial);
#endif
    Q_ASSERT(oldMaterial == nullptr || newMaterial->type() == oldMaterial->type());
    QQuickSpriteMaterial *mat = static_cast<QQuickSpriteMaterial *>(newMaterial);

    QSGTexture *t = mat->texture;
    t->commitTextureOperations(state.rhi(), state.resourceUpdateBatch());
    *texture = t;
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 125, as local:qsgdefaultspritenode.cpp:QQuickSpriteMaterial::createShader
inline QSGMaterialShader *QQuickSpriteMaterial::createShader(QSGRendererInterface::RenderMode renderMode) const
{
    Q_UNUSED(renderMode);
    return new SpriteMaterialRhiShader(viewCount());
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 165, as _ZN20QSGDefaultSpriteNode10setTextureEP10QSGTexture
inline void QSGDefaultSpriteNode::setTexture(QSGTexture *texture)
{
    m_material->texture = texture;
    m_geometryDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 172, as _ZN20QSGDefaultSpriteNode7setTimeEf
inline void QSGDefaultSpriteNode::setTime(float time)
{
    m_material->animT = time;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 178, as _ZN20QSGDefaultSpriteNode10setSourceAERK6QPoint
inline void QSGDefaultSpriteNode::setSourceA(const QPoint &source)
{
    if (m_sourceA != source) {
        m_sourceA = source;
        m_material->animX1 = static_cast<float>(source.x()) / m_sheetSize.width();
        m_material->animY1 = static_cast<float>(source.y()) / m_sheetSize.height();
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 188, as _ZN20QSGDefaultSpriteNode10setSourceBERK6QPoint
inline void QSGDefaultSpriteNode::setSourceB(const QPoint &source)
{
    if (m_sourceB != source) {
        m_sourceB = source;
        m_material->animX2 = static_cast<float>(source.x()) / m_sheetSize.width();
        m_material->animY2 = static_cast<float>(source.y()) / m_sheetSize.height();
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 198, as _ZN20QSGDefaultSpriteNode13setSpriteSizeERK5QSize
inline void QSGDefaultSpriteNode::setSpriteSize(const QSize &size)
{
    if (m_spriteSize != size) {
        m_spriteSize = size;
        m_material->animW = static_cast<float>(size.width()) / m_sheetSize.width();
        m_material->animH = static_cast<float>(size.height()) / m_sheetSize.height();
        markDirty(DirtyMaterial);
    }

}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 209, as _ZN20QSGDefaultSpriteNode12setSheetSizeERK5QSize
inline void QSGDefaultSpriteNode::setSheetSize(const QSize &size)
{
    if (m_sheetSize != size) {
        m_sheetSize = size;

        // Update all dependent properties
        m_material->animX1 = static_cast<float>(m_sourceA.x()) / m_sheetSize.width();
        m_material->animY1 = static_cast<float>(m_sourceA.y()) / m_sheetSize.height();
        m_material->animX2 = static_cast<float>(m_sourceB.x()) / m_sheetSize.width();
        m_material->animY2 = static_cast<float>(m_sourceB.y()) / m_sheetSize.height();
        m_material->animW = static_cast<float>(m_spriteSize.width()) / m_sheetSize.width();
        m_material->animH = static_cast<float>(m_spriteSize.height()) / m_sheetSize.height();
        markDirty(DirtyMaterial);
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 225, as _ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF
inline void QSGDefaultSpriteNode::setSize(const QSizeF &size)
{
    if (m_size != size) {
        m_size = size;
        m_geometryDirty = true;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 233, as _ZN20QSGDefaultSpriteNode12setFilteringEN10QSGTexture9FilteringE
inline void QSGDefaultSpriteNode::setFiltering(QSGTexture::Filtering filtering)
{
    m_material->texture->setFiltering(filtering);
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/qsgdefaultspritenode.cpp, line 239, as _ZN20QSGDefaultSpriteNode6updateEv
inline void QSGDefaultSpriteNode::update()
{
    if (m_geometryDirty) {
        updateGeometry();
        m_geometryDirty = false;
    }
}
//  -----------------------------------------------------------------------

//  void QSGDefaultSpriteNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode10setTextureEP10QSGTexture(
    QSGDefaultSpriteNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGDefaultSpriteNode::setTime(float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode7setTimeEf(
    QSGDefaultSpriteNode *self,
    float time) {
  self->setTime(time);
}

//  void QSGDefaultSpriteNode::setSourceA(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode10setSourceAERK6QPoint(
    QSGDefaultSpriteNode *self,
    const QPoint *source) {
  self->setSourceA(*source);
}

//  void QSGDefaultSpriteNode::setSourceB(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode10setSourceBERK6QPoint(
    QSGDefaultSpriteNode *self,
    const QPoint *source) {
  self->setSourceB(*source);
}

//  void QSGDefaultSpriteNode::setSpriteSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode13setSpriteSizeERK5QSize(
    QSGDefaultSpriteNode *self,
    const QSize *size) {
  self->setSpriteSize(*size);
}

//  void QSGDefaultSpriteNode::setSheetSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode12setSheetSizeERK5QSize(
    QSGDefaultSpriteNode *self,
    const QSize *size) {
  self->setSheetSize(*size);
}

//  void QSGDefaultSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF(
    QSGDefaultSpriteNode *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  void QSGDefaultSpriteNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode12setFilteringEN10QSGTexture9FilteringE(
    QSGDefaultSpriteNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  void QSGDefaultSpriteNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGDefaultSpriteNode6updateEv(QSGDefaultSpriteNode *self) {
  self->update();
}

//  void QSGDefaultSpriteNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode10setTextureEP10QSGTexture(
    QSGDefaultSpriteNode *self,
    QSGTexture *texture) {
  self->QSGDefaultSpriteNode::setTexture(texture);
}

//  void QSGDefaultSpriteNode::setTime(float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode7setTimeEf(
    QSGDefaultSpriteNode *self,
    float time) {
  self->QSGDefaultSpriteNode::setTime(time);
}

//  void QSGDefaultSpriteNode::setSourceA(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode10setSourceAERK6QPoint(
    QSGDefaultSpriteNode *self,
    const QPoint *source) {
  self->QSGDefaultSpriteNode::setSourceA(*source);
}

//  void QSGDefaultSpriteNode::setSourceB(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode10setSourceBERK6QPoint(
    QSGDefaultSpriteNode *self,
    const QPoint *source) {
  self->QSGDefaultSpriteNode::setSourceB(*source);
}

//  void QSGDefaultSpriteNode::setSpriteSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode13setSpriteSizeERK5QSize(
    QSGDefaultSpriteNode *self,
    const QSize *size) {
  self->QSGDefaultSpriteNode::setSpriteSize(*size);
}

//  void QSGDefaultSpriteNode::setSheetSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode12setSheetSizeERK5QSize(
    QSGDefaultSpriteNode *self,
    const QSize *size) {
  self->QSGDefaultSpriteNode::setSheetSize(*size);
}

//  void QSGDefaultSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode7setSizeERK6QSizeF(
    QSGDefaultSpriteNode *self,
    const QSizeF *size) {
  self->QSGDefaultSpriteNode::setSize(*size);
}

//  void QSGDefaultSpriteNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QSGDefaultSpriteNode12setFilteringEN10QSGTexture9FilteringE(
    QSGDefaultSpriteNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGDefaultSpriteNode::setFiltering(filtering);
}

#endif  // QT_CONFIG(quick_sprite)
#endif  // QT_CONFIG(quick_sprite)
