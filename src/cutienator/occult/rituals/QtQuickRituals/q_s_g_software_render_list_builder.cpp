//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderlistbuilder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarerenderlistbuilder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsgsoftwarerenderlistbuilder_p.h"
#include "qsgsoftwarerenderablenode_p.h"
#include "qsgabstractsoftwarerenderer_p.h"
#include "qsgsoftwareinternalimagenode_p.h"
#include "qsgsoftwareinternalrectanglenode_p.h"
#include "qsgsoftwareglyphnode_p.h"
#include "qsgsoftwarepublicnodes_p.h"
#include "qsgsoftwarepainternode_p.h"
#include "qsgsoftwarepixmaptexture_p.h"
#include <QtQuick/qsgsimplerectnode.h>
#include <QtQuick/qsgsimpletexturenode.h>
#include <QtQuick/qsgrendernode.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 22, as _ZN28QSGSoftwareRenderListBuilderC1EP27QSGAbstractSoftwareRenderer
inline QSGSoftwareRenderListBuilder::QSGSoftwareRenderListBuilder(QSGAbstractSoftwareRenderer *renderer)
    : m_renderer(renderer)
{

}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 28, as _ZN28QSGSoftwareRenderListBuilder5visitEP16QSGTransformNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGTransformNode *)
{
    return true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 33, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP16QSGTransformNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGTransformNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 37, as _ZN28QSGSoftwareRenderListBuilder5visitEP11QSGClipNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGClipNode *)
{
    return true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 42, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGClipNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGClipNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 46, as _ZN28QSGSoftwareRenderListBuilder5visitEP15QSGGeometryNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGGeometryNode *node)
{
    return addRenderableNode(node);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 51, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP15QSGGeometryNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGGeometryNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 55, as _ZN28QSGSoftwareRenderListBuilder5visitEP14QSGOpacityNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGOpacityNode *)
{
    return true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 60, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGOpacityNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGOpacityNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 64, as _ZN28QSGSoftwareRenderListBuilder5visitEP20QSGInternalImageNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGInternalImageNode *node)
{
    return addRenderableNode(node);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 69, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP20QSGInternalImageNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGInternalImageNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 73, as _ZN28QSGSoftwareRenderListBuilder5visitEP14QSGPainterNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGPainterNode *node)
{
    return addRenderableNode(node);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 78, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGPainterNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGPainterNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 82, as _ZN28QSGSoftwareRenderListBuilder5visitEP24QSGInternalRectangleNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGInternalRectangleNode *node)
{
    return addRenderableNode(node);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 87, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP24QSGInternalRectangleNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGInternalRectangleNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 91, as _ZN28QSGSoftwareRenderListBuilder5visitEP12QSGGlyphNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGGlyphNode *node)
{
    return addRenderableNode(node);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 96, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP12QSGGlyphNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGGlyphNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 100, as _ZN28QSGSoftwareRenderListBuilder5visitEP11QSGRootNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGRootNode *)
{
    return true;
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 105, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGRootNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGRootNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 110, as _ZN28QSGSoftwareRenderListBuilder5visitEP13QSGSpriteNode
#if QT_CONFIG(quick_sprite)
inline bool QSGSoftwareRenderListBuilder::visit(QSGSpriteNode *node)
{
    return addRenderableNode(node);
}
#endif  // QT_CONFIG(quick_sprite)

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 115, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGSpriteNode
#if QT_CONFIG(quick_sprite)
inline void QSGSoftwareRenderListBuilder::endVisit(QSGSpriteNode *)
{

}
#endif  // QT_CONFIG(quick_sprite)

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 121, as _ZN28QSGSoftwareRenderListBuilder5visitEP13QSGRenderNode
inline bool QSGSoftwareRenderListBuilder::visit(QSGRenderNode *node)
{
    return addRenderableNode(node);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 126, as _ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGRenderNode
inline void QSGSoftwareRenderListBuilder::endVisit(QSGRenderNode *)
{
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarerenderlistbuilder.cpp, line 130, as _ZN28QSGSoftwareRenderListBuilder17addRenderableNodeEP7QSGNode
inline bool QSGSoftwareRenderListBuilder::addRenderableNode(QSGNode *node)
{
    auto renderableNode = m_renderer->renderableNode(node);
    if (renderableNode == nullptr) {
        // Not a node we can render
        return false;
    }
    m_renderer->appendRenderableNode(renderableNode);
    return true;
}
//  -----------------------------------------------------------------------

#if QT_CONFIG(quick_sprite)
//  QSGSoftwareRenderListBuilder::QSGSoftwareRenderListBuilder(QSGAbstractSof
//      twareRenderer *renderer)
extern "C" Q_DECL_EXPORT
QSGSoftwareRenderListBuilder *ritual_ZN28QSGSoftwareRenderListBuilderC1EP27QSGAbstractSoftwareRenderer(
    QSGAbstractSoftwareRenderer *renderer) {
  return new QSGSoftwareRenderListBuilder(renderer);
}
#endif  // QT_CONFIG(quick_sprite)

//  bool QSGSoftwareRenderListBuilder::visit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP16QSGTransformNode(
    QSGSoftwareRenderListBuilder *self,
    QSGTransformNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP16QSGTransformNode(
    QSGSoftwareRenderListBuilder *self,
    QSGTransformNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGClipNode(
    QSGSoftwareRenderListBuilder *self,
    QSGClipNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGClipNode(
    QSGSoftwareRenderListBuilder *self,
    QSGClipNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP15QSGGeometryNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGeometryNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP15QSGGeometryNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGeometryNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGOpacityNode(
    QSGSoftwareRenderListBuilder *self,
    QSGOpacityNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGOpacityNode(
    QSGSoftwareRenderListBuilder *self,
    QSGOpacityNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP20QSGInternalImageNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalImageNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP20QSGInternalImageNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalImageNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGPainterNode(
    QSGSoftwareRenderListBuilder *self,
    QSGPainterNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGPainterNode(
    QSGSoftwareRenderListBuilder *self,
    QSGPainterNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGInternalRectangleNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP24QSGInternalRectangleNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalRectangleNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGInternalRectangleNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP24QSGInternalRectangleNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalRectangleNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP12QSGGlyphNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGlyphNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP12QSGGlyphNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGlyphNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGRootNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRootNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGRootNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRootNode *a0) {
  self->endVisit(a0);
}

#if QT_CONFIG(quick_sprite)
//  bool QSGSoftwareRenderListBuilder::visit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGSpriteNode(
    QSGSoftwareRenderListBuilder *self,
    QSGSpriteNode *a0) {
  return self->visit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
//  void QSGSoftwareRenderListBuilder::endVisit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGSpriteNode(
    QSGSoftwareRenderListBuilder *self,
    QSGSpriteNode *a0) {
  self->endVisit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

//  bool QSGSoftwareRenderListBuilder::visit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGRenderNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRenderNode *a0) {
  return self->visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGRenderNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRenderNode *a0) {
  self->endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::addRenderableNode(QSGNode *node)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSGSoftwareRenderListBuilder17addRenderableNodeEP7QSGNode(
    QSGSoftwareRenderListBuilder *self,
    QSGNode *node) {
  return self->addRenderableNode(node);
}

//  QSGSoftwareRenderListBuilder::~QSGSoftwareRenderListBuilder()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSGSoftwareRenderListBuilderD1Ev(
    QSGSoftwareRenderListBuilder *self) {
  delete self;
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP16QSGTransformNode(
    QSGSoftwareRenderListBuilder *self,
    QSGTransformNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGTransformNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP16QSGTransformNode(
    QSGSoftwareRenderListBuilder *self,
    QSGTransformNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGClipNode(
    QSGSoftwareRenderListBuilder *self,
    QSGClipNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGClipNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGClipNode(
    QSGSoftwareRenderListBuilder *self,
    QSGClipNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP15QSGGeometryNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGeometryNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGGeometryNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP15QSGGeometryNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGeometryNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGOpacityNode(
    QSGSoftwareRenderListBuilder *self,
    QSGOpacityNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGOpacityNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGOpacityNode(
    QSGSoftwareRenderListBuilder *self,
    QSGOpacityNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP20QSGInternalImageNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalImageNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGInternalImageNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP20QSGInternalImageNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalImageNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP14QSGPainterNode(
    QSGSoftwareRenderListBuilder *self,
    QSGPainterNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGPainterNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP14QSGPainterNode(
    QSGSoftwareRenderListBuilder *self,
    QSGPainterNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGInternalRectangleNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP24QSGInternalRectangleNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalRectangleNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGInternalRectangleNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP24QSGInternalRectangleNode(
    QSGSoftwareRenderListBuilder *self,
    QSGInternalRectangleNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP12QSGGlyphNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGlyphNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGGlyphNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP12QSGGlyphNode(
    QSGSoftwareRenderListBuilder *self,
    QSGGlyphNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

//  bool QSGSoftwareRenderListBuilder::visit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP11QSGRootNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRootNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGRootNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP11QSGRootNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRootNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}

#if QT_CONFIG(quick_sprite)
//  bool QSGSoftwareRenderListBuilder::visit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGSpriteNode(
    QSGSoftwareRenderListBuilder *self,
    QSGSpriteNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
//  void QSGSoftwareRenderListBuilder::endVisit(QSGSpriteNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGSpriteNode(
    QSGSoftwareRenderListBuilder *self,
    QSGSpriteNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}
#endif  // QT_CONFIG(quick_sprite)

//  bool QSGSoftwareRenderListBuilder::visit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN28QSGSoftwareRenderListBuilder5visitEP13QSGRenderNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRenderNode *a0) {
  return self->QSGSoftwareRenderListBuilder::visit(a0);
}

//  void QSGSoftwareRenderListBuilder::endVisit(QSGRenderNode *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QSGSoftwareRenderListBuilder8endVisitEP13QSGRenderNode(
    QSGSoftwareRenderListBuilder *self,
    QSGRenderNode *a0) {
  self->QSGSoftwareRenderListBuilder::endVisit(a0);
}
