//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 48, as local:qsgbatchrenderer.cpp:SHADOWNODE_TRAVERSE
#define SHADOWNODE_TRAVERSE(NODE) for (Node *child = NODE->firstChild(); child; child = child->sibling())

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 76, as local:qsgbatchrenderer.cpp:isTranslate
namespace QSGBatchRenderer {
static bool isTranslate(const QMatrix4x4 &m) { return m.flags() <= QMatrix4x4::Translation; }
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 80, as local:qsgbatchrenderer.cpp:OPAQUE_LIMIT
namespace QSGBatchRenderer {
const float OPAQUE_LIMIT                = 0.999f;
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 603, as _ZN16QSGBatchRenderer7Updater20updateRootTransformsEPNS_4NodeES2_RK10QMatrix4x4
namespace QSGBatchRenderer {
inline void Updater::updateRootTransforms(Node *node, Node *root, const QMatrix4x4 &combined)
{
    BatchRootInfo *info = renderer->batchRootInfo(node);
    QMatrix4x4 m;
    Node *n = node;

    while (n != root) {
        if (n->type() == QSGNode::TransformNodeType)
            m = static_cast<QSGTransformNode *>(n->sgNode)->matrix() * m;
        n = n->parent();
    }

    m = combined * m;

    if (node->type() == QSGNode::ClipNodeType) {
        static_cast<ClipBatchRootInfo *>(info)->matrix = m;
    } else {
        Q_ASSERT(node->type() == QSGNode::TransformNodeType);
        static_cast<QSGTransformNode *>(node->sgNode)->setCombinedMatrix(m);
    }

    for (QSet<Node *>::const_iterator it = info->subRoots.constBegin();
         it != info->subRoots.constEnd(); ++it) {
        updateRootTransforms(*it, node, m);
    }
}
}  // namespace QSGBatchRenderer
//  -----------------------------------------------------------------------

//  void QSGBatchRenderer::Updater::updateRootTransforms(Node *n, Node *root,
//      const QMatrix4x4 &combined)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7Updater20updateRootTransformsEPNS_4NodeES2_RK10QMatrix4x4(
    QSGBatchRenderer::Updater *self,
    QSGBatchRenderer::Node *n,
    QSGBatchRenderer::Node *root,
    const QMatrix4x4 *combined) {
  self->updateRootTransforms(n, root, *combined);
}

//  void QSGBatchRenderer::Updater::updateStates(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7Updater12updateStatesEP7QSGNode(
    QSGBatchRenderer::Updater *self,
    QSGNode *n) {
  self->updateStates(n);
}
