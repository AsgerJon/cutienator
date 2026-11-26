//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qsgnode.h>
#include <QtQuick/private/qsgnode_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick/private/qsgnodeupdater_p.h>
#include <QtQuick/qsgmaterial.h>
#include <algorithm>
#include "limits.h"
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

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 50, as local:qsgbatchrenderer.cpp:size_of_type
namespace QSGBatchRenderer {
static inline int size_of_type(int type)
{
    static int sizes[] = {
        sizeof(char),
        sizeof(unsigned char),
        sizeof(short),
        sizeof(unsigned short),
        sizeof(int),
        sizeof(unsigned int),
        sizeof(float),
        2,
        3,
        4,
        sizeof(double)
    };
    Q_ASSERT(type >= QSGGeometry::ByteType && type <= QSGGeometry::DoubleType);
    return sizes[type - QSGGeometry::ByteType];
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 77, as local:qsgbatchrenderer.cpp:isScale
namespace QSGBatchRenderer {
static bool isScale(const QMatrix4x4 &m) { return m.flags() <= QMatrix4x4::Scale; }
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 630, as local:qsgbatchrenderer.cpp:qsg_positionAttribute
namespace QSGBatchRenderer {
inline int qsg_positionAttribute(QSGGeometry *g)
{
    int vaOffset = 0;
    for (int a=0; a<g->attributeCount(); ++a) {
        const QSGGeometry::Attribute &attr = g->attributes()[a];
        if (attr.isVertexCoordinate && attr.tupleSize == 2 && attr.type == QSGGeometry::FloatType) {
            return vaOffset;
        }
        vaOffset += attr.tupleSize * size_of_type(attr.type);
    }
    return -1;
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgnode.cpp, line 360, as _ZN14QSGNodePrivate15mutabilityGroupEPK7QSGNode
inline quint8 QSGNodePrivate::mutabilityGroup(const QSGNode *node)
{
    return !node->d_ptr.isNull()
               ? node->d_ptr->m_mutabilityGroup
               : 0;
}

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 644, as _ZN16QSGBatchRenderer4Rect3mapERK10QMatrix4x4
namespace QSGBatchRenderer {
inline void Rect::map(const QMatrix4x4 &matrix)
{
    const float *m = matrix.constData();
    if (isScale(matrix)) {
        tl.x = tl.x * m[0] + m[12];
        tl.y = tl.y * m[5] + m[13];
        br.x = br.x * m[0] + m[12];
        br.y = br.y * m[5] + m[13];
        if (tl.x > br.x)
            qSwap(tl.x, br.x);
        if (tl.y > br.y)
            qSwap(tl.y, br.y);
    } else {
        Pt mtl = tl;
        Pt mtr = { br.x, tl.y };
        Pt mbl = { tl.x, br.y };
        Pt mbr = br;

        mtl.map(matrix);
        mtr.map(matrix);
        mbl.map(matrix);
        mbr.map(matrix);

        set(FLT_MAX, FLT_MAX, -FLT_MAX, -FLT_MAX);
        (*this) |= mtl;
        (*this) |= mtr;
        (*this) |= mbl;
        (*this) |= mbr;
    }
}
}  // namespace QSGBatchRenderer

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 675, as _ZN16QSGBatchRenderer7Element13computeBoundsEv
namespace QSGBatchRenderer {
inline void Element::computeBounds()
{
    Q_ASSERT(!boundsComputed);
    boundsComputed = true;

    QSGGeometry *g = node->geometry();
    int offset = qsg_positionAttribute(g);
    if (offset == -1) {
        // No position attribute means overlaps with everything..
        bounds.set(-FLT_MAX, -FLT_MAX, FLT_MAX, FLT_MAX);
        return;
    }

    bounds.set(FLT_MAX, FLT_MAX, -FLT_MAX, -FLT_MAX);
    char *vd = (char *) g->vertexData() + offset;
    for (int i=0; i<g->vertexCount(); ++i) {
        bounds |= *(Pt *) vd;
        vd += g->sizeOfVertex();
    }
    bounds.map(*node->matrix());

    if (!qt_is_finite(bounds.tl.x) || bounds.tl.x == FLT_MAX)
        bounds.tl.x = -FLT_MAX;
    if (!qt_is_finite(bounds.tl.y) || bounds.tl.y == FLT_MAX)
        bounds.tl.y = -FLT_MAX;
    if (!qt_is_finite(bounds.br.x) || bounds.br.x == -FLT_MAX)
        bounds.br.x = FLT_MAX;
    if (!qt_is_finite(bounds.br.y) || bounds.br.y == -FLT_MAX)
        bounds.br.y = FLT_MAX;

    Q_ASSERT(bounds.tl.x <= bounds.br.x);
    Q_ASSERT(bounds.tl.y <= bounds.br.y);

    boundsOutsideFloatRange = bounds.isOutsideFloatRange();
}
}  // namespace QSGBatchRenderer
//  -----------------------------------------------------------------------

//  QSGBatchRenderer::Element::Element()
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::Element *ritual_ZN16QSGBatchRenderer7ElementC1Ev() {
  return new QSGBatchRenderer::Element();
}

//  void QSGBatchRenderer::Element::setNode(QSGGeometryNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7Element7setNodeEP15QSGGeometryNode(
    QSGBatchRenderer::Element *self,
    QSGGeometryNode *n) {
  self->setNode(n);
}

//  void QSGBatchRenderer::Element::ensureBoundsValid()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7Element17ensureBoundsValidEv(
    QSGBatchRenderer::Element *self) {
  self->ensureBoundsValid();
}

//  void QSGBatchRenderer::Element::computeBounds()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7Element13computeBoundsEv(
    QSGBatchRenderer::Element *self) {
  self->computeBounds();
}

//  QSGBatchRenderer::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer7ElementD1Ev(
    QSGBatchRenderer::Element *self) {
  delete self;
}
