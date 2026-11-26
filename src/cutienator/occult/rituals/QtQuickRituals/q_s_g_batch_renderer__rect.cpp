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

//  from ../qtdeclarative/src/quick/scenegraph/coreapi/qsgbatchrenderer.cpp, line 77, as local:qsgbatchrenderer.cpp:isScale
namespace QSGBatchRenderer {
static bool isScale(const QMatrix4x4 &m) { return m.flags() <= QMatrix4x4::Scale; }
}  // namespace QSGBatchRenderer

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
//  -----------------------------------------------------------------------

//  void QSGBatchRenderer::Rect::operator|=(const Pt &pt)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4RectoRERKNS_2PtE(
    QSGBatchRenderer::Rect *self,
    const QSGBatchRenderer::Pt *pt) {
  self->operator|=(*pt);
}

//  void QSGBatchRenderer::Rect::operator|=(const Rect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4RectoRERKS0_(
    QSGBatchRenderer::Rect *self,
    const QSGBatchRenderer::Rect *r) {
  self->operator|=(*r);
}

//  void QSGBatchRenderer::Rect::map(const QMatrix4x4 &m)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4Rect3mapERK10QMatrix4x4(
    QSGBatchRenderer::Rect *self,
    const QMatrix4x4 *m) {
  self->map(*m);
}

//  void QSGBatchRenderer::Rect::set(float left, float top, float right,
//      float bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4Rect3setEffff(
    QSGBatchRenderer::Rect *self,
    float left,
    float top,
    float right,
    float bottom) {
  self->set(left, top, right, bottom);
}

//  bool QSGBatchRenderer::Rect::intersects(const Rect &r)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QSGBatchRenderer4Rect10intersectsERKS0_(
    QSGBatchRenderer::Rect *self,
    const QSGBatchRenderer::Rect *r) {
  return self->intersects(*r);
}

//  bool QSGBatchRenderer::Rect::isOutsideFloatRange() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QSGBatchRenderer4Rect19isOutsideFloatRangeEv(
    const QSGBatchRenderer::Rect *self) {
  return self->isOutsideFloatRange();
}

//  QSGBatchRenderer::Rect::~Rect()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer4RectD1Ev(QSGBatchRenderer::Rect *self) {
  delete self;
}
