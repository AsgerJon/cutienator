//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapesoftwarerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesoftwarerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgtransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickshapesoftwarerenderer_p.h"
#include <private/qquickpath_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 10, as _ZN27QQuickShapeSoftwareRenderer9beginSyncEiPb
inline void QQuickShapeSoftwareRenderer::beginSync(int totalCount, bool *countChanged)
{
    if (m_sp.size() != totalCount) {
        m_sp.resize(totalCount);
        m_accDirty |= DirtyList;
        *countChanged = true;
    } else {
        *countChanged = false;
    }
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 21, as _ZN27QQuickShapeSoftwareRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE
inline void QQuickShapeSoftwareRenderer::setPath(int index, const QPainterPath &path, QQuickShapePath::PathHints)
{
    ShapePathGuiData &d(m_sp[index]);
    d.path = path;
    d.dirty |= DirtyPath;
    m_accDirty |= DirtyPath;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 29, as _ZN27QQuickShapeSoftwareRenderer14setStrokeColorEiRK6QColor
inline void QQuickShapeSoftwareRenderer::setStrokeColor(int index, const QColor &color)
{
    ShapePathGuiData &d(m_sp[index]);
    d.pen.setColor(color);
    d.dirty |= DirtyPen;
    m_accDirty |= DirtyPen;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 37, as _ZN27QQuickShapeSoftwareRenderer14setStrokeWidthEid
inline void QQuickShapeSoftwareRenderer::setStrokeWidth(int index, qreal w)
{
    ShapePathGuiData &d(m_sp[index]);
    d.strokeWidth = w;
    if (w > 0.0f)
        d.pen.setWidthF(w);
    d.dirty |= DirtyPen;
    m_accDirty |= DirtyPen;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 47, as _ZN27QQuickShapeSoftwareRenderer17setCosmeticStrokeEib
inline void QQuickShapeSoftwareRenderer::setCosmeticStroke(int index, bool c)
{
    ShapePathGuiData &d(m_sp[index]);
    d.pen.setCosmetic(c);
    d.dirty |= DirtyPen;
    m_accDirty |= DirtyPen;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 55, as _ZN27QQuickShapeSoftwareRenderer12setFillColorEiRK6QColor
inline void QQuickShapeSoftwareRenderer::setFillColor(int index, const QColor &color)
{
    ShapePathGuiData &d(m_sp[index]);
    d.fillColor = color;
    d.brush.setColor(color);
    d.dirty |= DirtyBrush;
    m_accDirty |= DirtyBrush;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 64, as _ZN27QQuickShapeSoftwareRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE
inline void QQuickShapeSoftwareRenderer::setFillRule(int index, QQuickShapePath::FillRule fillRule)
{
    ShapePathGuiData &d(m_sp[index]);
    d.fillRule = Qt::FillRule(fillRule);
    d.dirty |= DirtyFillRule;
    m_accDirty |= DirtyFillRule;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 72, as _ZN27QQuickShapeSoftwareRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi
inline void QQuickShapeSoftwareRenderer::setJoinStyle(int index, QQuickShapePath::JoinStyle joinStyle, int miterLimit)
{
    ShapePathGuiData &d(m_sp[index]);
    d.pen.setJoinStyle(Qt::PenJoinStyle(joinStyle));
    d.pen.setMiterLimit(miterLimit);
    d.dirty |= DirtyPen;
    m_accDirty |= DirtyPen;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 81, as _ZN27QQuickShapeSoftwareRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE
inline void QQuickShapeSoftwareRenderer::setCapStyle(int index, QQuickShapePath::CapStyle capStyle)
{
    ShapePathGuiData &d(m_sp[index]);
    d.pen.setCapStyle(Qt::PenCapStyle(capStyle));
    d.dirty |= DirtyPen;
    m_accDirty |= DirtyPen;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 163, as _ZN27QQuickShapeSoftwareRenderer22setFillTextureProviderEiP10QQuickItem
inline void QQuickShapeSoftwareRenderer::setFillTextureProvider(int index, QQuickItem *textureProviderItem)
{
    Q_UNUSED(index);
    Q_UNUSED(textureProviderItem);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 175, as _ZN27QQuickShapeSoftwareRenderer16setFillTransformEiRK12QSGTransform
inline void QQuickShapeSoftwareRenderer::setFillTransform(int index, const QSGTransform &transform)
{
    ShapePathGuiData &d(m_sp[index]);
    if (!(transform.isIdentity() && d.brush.transform().isIdentity())) // No need to copy if both==I
        d.brush.setTransform(transform.matrix().toTransform());
    d.dirty |= DirtyBrush;
    m_accDirty |= DirtyBrush;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 184, as _ZN27QQuickShapeSoftwareRenderer21setTriangulationScaleEid
inline void QQuickShapeSoftwareRenderer::setTriangulationScale(int index, qreal scale)
{
    ShapePathGuiData &d(m_sp[index]);
    d.triangulationScale = scale;
    d.dirty |= DirtyPen;
    m_accDirty |= DirtyPen;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 192, as _ZN27QQuickShapeSoftwareRenderer7endSyncEb
inline void QQuickShapeSoftwareRenderer::endSync(bool)
{
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 169, as _ZN27QQuickShapeSoftwareRenderer17handleSceneChangeEP12QQuickWindow
inline void QQuickShapeSoftwareRenderer::handleSceneChange(QQuickWindow *window)
{
    Q_UNUSED(window);
    // No action needed
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 202, as _ZN27QQuickShapeSoftwareRenderer10updateNodeEv
inline void QQuickShapeSoftwareRenderer::updateNode()
{
    if (!m_accDirty)
        return;

    const int count = m_sp.size();
    const bool listChanged = m_accDirty & DirtyList;
    if (listChanged)
        m_node->m_sp.resize(count);

    m_node->m_boundingRect = QRectF();

    for (int i = 0; i < count; ++i) {
        ShapePathGuiData &src(m_sp[i]);
        QQuickShapeSoftwareRenderNode::ShapePathRenderData &dst(m_node->m_sp[i]);

        if (listChanged || (src.dirty & DirtyPath)) {
            dst.path = src.path;
            dst.path.setFillRule(src.fillRule);
        }

        if (listChanged || (src.dirty & DirtyFillRule))
            dst.path.setFillRule(src.fillRule);

        if (listChanged || (src.dirty & DirtyPen)) {
            dst.pen = src.pen;
            dst.strokeWidth = src.strokeWidth;
            dst.triangulationScale = src.triangulationScale;
        }

        if (listChanged || (src.dirty & DirtyBrush))
            dst.brush = src.brush;

        src.dirty = 0;

        QRectF br = dst.path.boundingRect();
        float sw = qMax(1.0f, dst.strokeWidth);
        if (dst.pen.isCosmetic())
            sw *= 2.0f / dst.triangulationScale;
        br.adjust(-sw, -sw, sw, sw);
        m_node->m_boundingRect |= br;
    }

    m_node->markDirty(QSGNode::DirtyMaterial);
    m_accDirty = 0;
}

//  from ../qtdeclarative/src/quickshapes/qquickshapesoftwarerenderer.cpp, line 196, as _ZN27QQuickShapeSoftwareRenderer7setNodeEP29QQuickShapeSoftwareRenderNode
inline void QQuickShapeSoftwareRenderer::setNode(QQuickShapeSoftwareRenderNode *node)
{
    m_node = node;
    m_accDirty |= DirtyList;
}
//  -----------------------------------------------------------------------

//  void QQuickShapeSoftwareRenderer::beginSync(int totalCount, bool
//      *countChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer9beginSyncEiPb(
    QQuickShapeSoftwareRenderer *self,
    int totalCount,
    bool *countChanged) {
  self->beginSync(totalCount, countChanged);
}

//  void QQuickShapeSoftwareRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickShapeSoftwareRenderer::setStrokeColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer14setStrokeColorEiRK6QColor(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QColor *color) {
  self->setStrokeColor(index, *color);
}

//  void QQuickShapeSoftwareRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer14setStrokeWidthEid(
    QQuickShapeSoftwareRenderer *self,
    int index,
    qreal w) {
  self->setStrokeWidth(index, w);
}

//  void QQuickShapeSoftwareRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer17setCosmeticStrokeEib(
    QQuickShapeSoftwareRenderer *self,
    int index,
    bool c) {
  self->setCosmeticStroke(index, c);
}

//  void QQuickShapeSoftwareRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer12setFillColorEiRK6QColor(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QColor *color) {
  self->setFillColor(index, *color);
}

//  void QQuickShapeSoftwareRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(index, fillRule);
}

//  void QQuickShapeSoftwareRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->setJoinStyle(index, joinStyle, miterLimit);
}

//  void QQuickShapeSoftwareRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->setCapStyle(index, capStyle);
}

//  void QQuickShapeSoftwareRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->setFillTextureProvider(index, textureProviderItem);
}

//  void QQuickShapeSoftwareRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer16setFillTransformEiRK12QSGTransform(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->setFillTransform(index, *transform);
}

//  void QQuickShapeSoftwareRenderer::setTriangulationScale(int index, qreal
//      scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer21setTriangulationScaleEid(
    QQuickShapeSoftwareRenderer *self,
    int index,
    qreal scale) {
  self->setTriangulationScale(index, scale);
}

//  void QQuickShapeSoftwareRenderer::endSync(bool async)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer7endSyncEb(
    QQuickShapeSoftwareRenderer *self,
    bool async) {
  self->endSync(async);
}

//  void QQuickShapeSoftwareRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickShapeSoftwareRenderer *self,
    QQuickWindow *window) {
  self->handleSceneChange(window);
}

//  void QQuickShapeSoftwareRenderer::updateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer10updateNodeEv(
    QQuickShapeSoftwareRenderer *self) {
  self->updateNode();
}

//  void QQuickShapeSoftwareRenderer::setNode(QQuickShapeSoftwareRenderNode
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRenderer7setNodeEP29QQuickShapeSoftwareRenderNode(
    QQuickShapeSoftwareRenderer *self,
    QQuickShapeSoftwareRenderNode *node) {
  self->setNode(node);
}

//  QQuickShapeSoftwareRenderer::~QQuickShapeSoftwareRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickShapeSoftwareRendererD1Ev(
    QQuickShapeSoftwareRenderer *self) {
  delete self;
}

//  void QQuickShapeSoftwareRenderer::setPath(int index, const QPainterPath
//      &path, QQuickShapePath::PathHints pathHints)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer7setPathEiRK12QPainterPath6QFlagsIN15QQuickShapePath8PathHintEE(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QPainterPath *path,
    int pathHints) {
  self->QQuickShapeSoftwareRenderer::setPath(
      index,
      *path,
      QFlags<QQuickShapePath::PathHint>::fromInt(pathHints));
}

//  void QQuickShapeSoftwareRenderer::setStrokeColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer14setStrokeColorEiRK6QColor(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QColor *color) {
  self->QQuickShapeSoftwareRenderer::setStrokeColor(index, *color);
}

//  void QQuickShapeSoftwareRenderer::setStrokeWidth(int index, qreal w)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer14setStrokeWidthEid(
    QQuickShapeSoftwareRenderer *self,
    int index,
    qreal w) {
  self->QQuickShapeSoftwareRenderer::setStrokeWidth(index, w);
}

//  void QQuickShapeSoftwareRenderer::setCosmeticStroke(int index, bool c)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer17setCosmeticStrokeEib(
    QQuickShapeSoftwareRenderer *self,
    int index,
    bool c) {
  self->QQuickShapeSoftwareRenderer::setCosmeticStroke(index, c);
}

//  void QQuickShapeSoftwareRenderer::setFillColor(int index, const QColor
//      &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer12setFillColorEiRK6QColor(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QColor *color) {
  self->QQuickShapeSoftwareRenderer::setFillColor(index, *color);
}

//  void QQuickShapeSoftwareRenderer::setFillRule(int index,
//      QQuickShapePath::FillRule fillRule)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer11setFillRuleEiN15QQuickShapePath8FillRuleE(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickShapePath::FillRule fillRule) {
  self->QQuickShapeSoftwareRenderer::setFillRule(index, fillRule);
}

//  void QQuickShapeSoftwareRenderer::setJoinStyle(int index,
//      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer12setJoinStyleEiN15QQuickShapePath9JoinStyleEi(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickShapePath::JoinStyle joinStyle,
    int miterLimit) {
  self->QQuickShapeSoftwareRenderer::setJoinStyle(
      index,
      joinStyle,
      miterLimit);
}

//  void QQuickShapeSoftwareRenderer::setCapStyle(int index,
//      QQuickShapePath::CapStyle capStyle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer11setCapStyleEiN15QQuickShapePath8CapStyleE(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickShapePath::CapStyle capStyle) {
  self->QQuickShapeSoftwareRenderer::setCapStyle(index, capStyle);
}

//  void QQuickShapeSoftwareRenderer::setFillTextureProvider(int index,
//      QQuickItem *textureProviderItem)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer22setFillTextureProviderEiP10QQuickItem(
    QQuickShapeSoftwareRenderer *self,
    int index,
    QQuickItem *textureProviderItem) {
  self->QQuickShapeSoftwareRenderer::setFillTextureProvider(
      index,
      textureProviderItem);
}

//  void QQuickShapeSoftwareRenderer::setFillTransform(int index, const
//      QSGTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer16setFillTransformEiRK12QSGTransform(
    QQuickShapeSoftwareRenderer *self,
    int index,
    const QSGTransform *transform) {
  self->QQuickShapeSoftwareRenderer::setFillTransform(index, *transform);
}

//  void QQuickShapeSoftwareRenderer::setTriangulationScale(int index, qreal
//      scale)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer21setTriangulationScaleEid(
    QQuickShapeSoftwareRenderer *self,
    int index,
    qreal scale) {
  self->QQuickShapeSoftwareRenderer::setTriangulationScale(index, scale);
}

//  void QQuickShapeSoftwareRenderer::endSync(bool async)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer7endSyncEb(
    QQuickShapeSoftwareRenderer *self,
    bool async) {
  self->QQuickShapeSoftwareRenderer::endSync(async);
}

//  void QQuickShapeSoftwareRenderer::handleSceneChange(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer17handleSceneChangeEP12QQuickWindow(
    QQuickShapeSoftwareRenderer *self,
    QQuickWindow *window) {
  self->QQuickShapeSoftwareRenderer::handleSceneChange(window);
}

//  void QQuickShapeSoftwareRenderer::updateNode()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickShapeSoftwareRenderer10updateNodeEv(
    QQuickShapeSoftwareRenderer *self) {
  self->QQuickShapeSoftwareRenderer::updateNode();
}
