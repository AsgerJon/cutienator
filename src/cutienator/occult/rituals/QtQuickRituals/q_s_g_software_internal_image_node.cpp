//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalimagenode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtGui/QPainter>
#include <QtCore/qmath.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 395, as local:qsgsoftwareinternalimagenode.cpp:getTileRule
static Qt::TileRule getTileRule(qreal factor)
{
    int ifactor = qRound(factor);
    if (qFuzzyCompare(factor, ifactor )) {
        if (ifactor  == 1 || ifactor  == 0)
            return Qt::StretchTile;
        return Qt::RoundTile;
    }
    return Qt::RepeatTile;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 293, as _ZN28QSGSoftwareInternalImageNode13setTargetRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setTargetRect(const QRectF &rect)
{
    if (rect == m_targetRect)
        return;
    m_targetRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 301, as _ZN28QSGSoftwareInternalImageNode18setInnerTargetRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setInnerTargetRect(const QRectF &rect)
{
    if (rect == m_innerTargetRect)
        return;
    m_innerTargetRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 309, as _ZN28QSGSoftwareInternalImageNode18setInnerSourceRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setInnerSourceRect(const QRectF &rect)
{
    if (rect == m_innerSourceRect)
        return;
    m_innerSourceRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 317, as _ZN28QSGSoftwareInternalImageNode16setSubSourceRectERK6QRectF
inline void QSGSoftwareInternalImageNode::setSubSourceRect(const QRectF &rect)
{
    if (rect == m_subSourceRect)
        return;
    m_subSourceRect = rect;
    markDirty(DirtyGeometry);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 325, as _ZN28QSGSoftwareInternalImageNode10setTextureEP10QSGTexture
inline void QSGSoftwareInternalImageNode::setTexture(QSGTexture *texture)
{
    m_texture = texture;
    m_cachedMirroredPixmapIsDirty = true;
    m_textureIsLayer = static_cast<bool>(qobject_cast<QSGSoftwareLayer*>(texture));
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 333, as _ZN28QSGSoftwareInternalImageNode9setMirrorEbb
inline void QSGSoftwareInternalImageNode::setMirror(bool mirrorHorizontally, bool mirrorVertically)
{
    if (mirrorHorizontally == m_mirrorHorizontally && mirrorVertically == m_mirrorVertically)
        return;
    m_mirrorHorizontally = mirrorHorizontally;
    m_mirrorVertically = mirrorVertically;
    m_cachedMirroredPixmapIsDirty = true;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 343, as _ZN28QSGSoftwareInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE
inline void QSGSoftwareInternalImageNode::setMipmapFiltering(QSGTexture::Filtering /*filtering*/)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 347, as _ZN28QSGSoftwareInternalImageNode12setFilteringEN10QSGTexture9FilteringE
inline void QSGSoftwareInternalImageNode::setFiltering(QSGTexture::Filtering filtering)
{
    bool smooth = (filtering == QSGTexture::Linear);
    if (smooth == m_smooth)
        return;

    m_smooth = smooth;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 357, as _ZN28QSGSoftwareInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE
inline void QSGSoftwareInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapMode wrapMode)
{
    bool tileHorizontal = (wrapMode == QSGTexture::Repeat);
    if (tileHorizontal == m_tileHorizontal)
        return;

    m_tileHorizontal = tileHorizontal;
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 367, as _ZN28QSGSoftwareInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE
inline void QSGSoftwareInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMode wrapMode)
{
    bool tileVertical = (wrapMode == QSGTexture::Repeat);
    if (tileVertical == m_tileVertical)
        return;

    m_tileVertical = (wrapMode == QSGTexture::Repeat);
    markDirty(DirtyMaterial);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 377, as _ZN28QSGSoftwareInternalImageNode6updateEv
inline void QSGSoftwareInternalImageNode::update()
{
    updateCachedMirroredPixmap();
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 382, as _ZN28QSGSoftwareInternalImageNode10preprocessEv
inline void QSGSoftwareInternalImageNode::preprocess()
{
    bool doDirty = false;
    QSGLayer *t = qobject_cast<QSGLayer *>(m_texture);
    if (t) {
        doDirty = t->updateTexture();
        markDirty(DirtyGeometry);
    }
    if (doDirty)
        markDirty(DirtyMaterial);
    m_cachedMirroredPixmapIsDirty = doDirty;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 459, as _ZN28QSGSoftwareInternalImageNode26updateCachedMirroredPixmapEv
inline void QSGSoftwareInternalImageNode::updateCachedMirroredPixmap()
{
    if (m_cachedMirroredPixmapIsDirty) {
        if (m_mirrorHorizontally || m_mirrorVertically || m_textureIsLayer) {
            QTransform transform(
                (m_mirrorHorizontally ? -1 : 1), 0,
                0                              , (m_textureIsLayer ? -1 : 1) * (m_mirrorVertically ? -1 : 1),
                0                              , 0
                );
            m_cachedMirroredPixmap = pixmap().transformed(transform);
        } else {
            //Cleanup cached pixmap if necessary
            if (!m_cachedMirroredPixmap.isNull())
                m_cachedMirroredPixmap = QPixmap();
        }
        m_cachedMirroredPixmapIsDirty = false;
    }
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 448, as _ZNK28QSGSoftwareInternalImageNode6pixmapEv
inline const QPixmap &QSGSoftwareInternalImageNode::pixmap() const
{
    if (QSGSoftwarePixmapTexture *pt = qobject_cast<QSGSoftwarePixmapTexture*>(m_texture))
        return pt->pixmap();
    if (QSGSoftwareLayer *layer = qobject_cast<QSGSoftwareLayer*>(m_texture))
        return layer->pixmap();
    Q_ASSERT(m_texture == nullptr);
    static const QPixmap nullPixmap;
    return nullPixmap;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwareinternalimagenode.cpp, line 443, as _ZNK28QSGSoftwareInternalImageNode4rectEv
inline QRectF QSGSoftwareInternalImageNode::rect() const
{
    return m_targetRect;
}
//  -----------------------------------------------------------------------

//  void QSGSoftwareInternalImageNode::setTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode13setTargetRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->setTargetRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setInnerTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode18setInnerTargetRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->setInnerTargetRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setInnerSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode18setInnerSourceRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->setInnerSourceRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setSubSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode16setSubSourceRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->setSubSourceRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode10setTextureEP10QSGTexture(
    QSGSoftwareInternalImageNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGSoftwareInternalImageNode::setMirror(bool mirrorHorizontally,
//      bool mirrorVertically)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode9setMirrorEbb(
    QSGSoftwareInternalImageNode *self,
    bool mirrorHorizontally,
    bool mirrorVertically) {
  self->setMirror(mirrorHorizontally, mirrorVertically);
}

//  void
//      QSGSoftwareInternalImageNode::setMipmapFiltering(QSGTexture::Filterin
//      g filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setMipmapFiltering(filtering);
}

//  void QSGSoftwareInternalImageNode::setFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  void
//      QSGSoftwareInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapM
//      ode wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->setHorizontalWrapMode(wrapMode);
}

//  void
//      QSGSoftwareInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMod
//      e wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->setVerticalWrapMode(wrapMode);
}

//  void QSGSoftwareInternalImageNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode6updateEv(
    QSGSoftwareInternalImageNode *self) {
  self->update();
}

//  void QSGSoftwareInternalImageNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareInternalImageNode10preprocessEv(
    QSGSoftwareInternalImageNode *self) {
  self->preprocess();
}

//  QRectF QSGSoftwareInternalImageNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK28QSGSoftwareInternalImageNode4rectEv(
    const QSGSoftwareInternalImageNode *self) {
  return new QRectF(self->rect());
}

//  void QSGSoftwareInternalImageNode::setTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode13setTargetRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->QSGSoftwareInternalImageNode::setTargetRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setInnerTargetRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode18setInnerTargetRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->QSGSoftwareInternalImageNode::setInnerTargetRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setInnerSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode18setInnerSourceRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->QSGSoftwareInternalImageNode::setInnerSourceRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setSubSourceRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode16setSubSourceRectERK6QRectF(
    QSGSoftwareInternalImageNode *self,
    const QRectF *rect) {
  self->QSGSoftwareInternalImageNode::setSubSourceRect(*rect);
}

//  void QSGSoftwareInternalImageNode::setMirror(bool mirrorHorizontally,
//      bool mirrorVertically)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode9setMirrorEbb(
    QSGSoftwareInternalImageNode *self,
    bool mirrorHorizontally,
    bool mirrorVertically) {
  self->QSGSoftwareInternalImageNode::setMirror(
      mirrorHorizontally,
      mirrorVertically);
}

//  void
//      QSGSoftwareInternalImageNode::setMipmapFiltering(QSGTexture::Filterin
//      g filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode18setMipmapFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGSoftwareInternalImageNode::setMipmapFiltering(filtering);
}

//  void QSGSoftwareInternalImageNode::setFiltering(QSGTexture::Filtering
//      filtering)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::Filtering filtering) {
  self->QSGSoftwareInternalImageNode::setFiltering(filtering);
}

//  void
//      QSGSoftwareInternalImageNode::setHorizontalWrapMode(QSGTexture::WrapM
//      ode wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode21setHorizontalWrapModeEN10QSGTexture8WrapModeE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->QSGSoftwareInternalImageNode::setHorizontalWrapMode(wrapMode);
}

//  void
//      QSGSoftwareInternalImageNode::setVerticalWrapMode(QSGTexture::WrapMod
//      e wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode19setVerticalWrapModeEN10QSGTexture8WrapModeE(
    QSGSoftwareInternalImageNode *self,
    QSGTexture::WrapMode wrapMode) {
  self->QSGSoftwareInternalImageNode::setVerticalWrapMode(wrapMode);
}

//  void QSGSoftwareInternalImageNode::preprocess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareInternalImageNode10preprocessEv(
    QSGSoftwareInternalImageNode *self) {
  self->QSGSoftwareInternalImageNode::preprocess();
}
