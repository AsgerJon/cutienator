//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgbatchrenderer_p.h>
#include <QtCore/qmath.h>
#include <QtCore/QElapsedTimer>
#include <QtCore/QtNumeric>
#include <QtGui/QGuiApplication>
#include <QtCore/private/qnumeric_p.h>
#include <QtQuick/private/qsgmaterialshader_p.h>
#include <QtQuick/private/qsgrhivisualizer_p.h>
#include <QtQuick/private/qsgnode_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 78, as local:qsgbatchrenderer.cpp:is2DSafe
namespace QSGBatchRenderer {
static bool is2DSafe(const QMatrix4x4 &m) { return m.flags() < QMatrix4x4::Rotation; }
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 735, as _ZN16QSGBatchRenderer5Batch18geometryWasChangedEP15QSGGeometryNode
namespace QSGBatchRenderer {
inline bool Batch::geometryWasChanged(QSGGeometryNode *gn)
{
    Element *e = first;
    Q_ASSERT_X(e, "Batch::geometryWasChanged", "Batch is expected to 'valid' at this time");
    // 'gn' is the first node in the batch, compare against the next one.
    while (e && (e->node == gn || e->removed))
        e = e->nextInBatch;
    if (!e || e->node->geometry()->attributes() == gn->geometry()->attributes()) {
        needsUpload = true;
        return true;
    } else {
        return false;
    }
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 711, as _ZNK16QSGBatchRenderer5Batch20isMaterialCompatibleEPNS_7ElementE
namespace QSGBatchRenderer {
inline BatchCompatibility Batch::isMaterialCompatible(Element *e) const
{
    Element *n = first;
    // Skip to the first node other than e which has not been removed
    while (n && (n == e || n->removed))
        n = n->nextInBatch;

    // Only 'e' in this batch, so a material change doesn't change anything as long as
    // its blending is still in sync with this batch...
    if (!n)
        return BatchIsCompatible;

    QSGMaterial *m = e->node->activeMaterial();
    QSGMaterial *nm = n->node->activeMaterial();
    return (nm->type() == m->type() && nm->viewCount() == m->viewCount() && nm->compare(m) == 0)
            ? BatchIsCompatible
            : BatchBreaksOnCompare;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 779, as _ZN16QSGBatchRenderer5Batch10invalidateEv
namespace QSGBatchRenderer {
inline void Batch::invalidate()
{
    cleanupRemovedElements();
    Element *e = first;
    first = nullptr;
    root = nullptr;
    while (e) {
        e->batch = nullptr;
        Element *n = e->nextInBatch;
        e->nextInBatch = nullptr;
        e = n;
    }
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 750, as _ZN16QSGBatchRenderer5Batch22cleanupRemovedElementsEv
namespace QSGBatchRenderer {
inline void Batch::cleanupRemovedElements()
{
    if (!needsPurge)
        return;

    // remove from front of batch..
    while (first && first->removed) {
        first = first->nextInBatch;
    }

    // Then continue and remove other nodes further out in the batch..
    if (first) {
        Element *e = first;
        while (e->nextInBatch) {
            if (e->nextInBatch->removed)
                e->nextInBatch = e->nextInBatch->nextInBatch;
            else
                e = e->nextInBatch;

        }
    }

    needsPurge = false;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 793, as _ZNK16QSGBatchRenderer5Batch21isTranslateOnlyToRootEv
namespace QSGBatchRenderer {
inline bool Batch::isTranslateOnlyToRoot() const {
    bool only = true;
    Element *e = first;
    while (e && only) {
        only &= e->translateOnlyToRoot;
        e = e->nextInBatch;
    }
    return only;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 820, as _ZNK16QSGBatchRenderer5Batch13isSafeToBatchEv
namespace QSGBatchRenderer {
inline bool Batch::isSafeToBatch() const {
    Element *e = first;
    while (e) {
        if (e->boundsOutsideFloatRange)
            return false;
        if (!is2DSafe(*e->node->matrix()))
            return false;
        e = e->nextInBatch;
    }
    return true;
}
}  // namespace QSGBatchRenderer
//  -----------------------------------------------------------------------

//  QSGBatchRenderer::Batch::Batch()
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Batch *ritual_ZN16QSGBatchRenderer5BatchC1Ev() {
  return new QSGBatchRenderer::Batch();
}

//  bool QSGBatchRenderer::Batch::geometryWasChanged(QSGGeometryNode *gn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer5Batch18geometryWasChangedEP15QSGGeometryNode(
    QSGBatchRenderer::Batch *self,
    QSGGeometryNode *gn) {
  return self->geometryWasChanged(gn);
}

//  BatchCompatibility QSGBatchRenderer::Batch::isMaterialCompatible(Element
//      *e) const
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::BatchCompatibility ritual_ZNK16QSGBatchRenderer5Batch20isMaterialCompatibleEPNS_7ElementE(
    const QSGBatchRenderer::Batch *self,
    QSGBatchRenderer::Element *e) {
  return self->isMaterialCompatible(e);
}

//  void QSGBatchRenderer::Batch::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer5Batch10invalidateEv(
    QSGBatchRenderer::Batch *self) {
  self->invalidate();
}

//  void QSGBatchRenderer::Batch::cleanupRemovedElements()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer5Batch22cleanupRemovedElementsEv(
    QSGBatchRenderer::Batch *self) {
  self->cleanupRemovedElements();
}

//  bool QSGBatchRenderer::Batch::isTranslateOnlyToRoot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer5Batch21isTranslateOnlyToRootEv(
    const QSGBatchRenderer::Batch *self) {
  return self->isTranslateOnlyToRoot();
}

//  bool QSGBatchRenderer::Batch::isSafeToBatch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer5Batch13isSafeToBatchEv(
    const QSGBatchRenderer::Batch *self) {
  return self->isSafeToBatch();
}

//  void QSGBatchRenderer::Batch::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer5Batch4initEv(
    QSGBatchRenderer::Batch *self) {
  self->init();
}
