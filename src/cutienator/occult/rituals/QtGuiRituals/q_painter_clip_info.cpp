//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpainter_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtGui/qtransform.h>
#include <QtGui/qregion.h>
#include <QtCore/qrect.h>

//  QPainterClipInfo::QPainterClipInfo()
extern "C" Q_DECL_EXPORT
QPainterClipInfo *ritual_ZN16QPainterClipInfoC1Ev() {
  return new QPainterClipInfo();
}

//  QPainterClipInfo::QPainterClipInfo(const QPainterPath &p,
//      Qt::ClipOperation op, const QTransform &m)
extern "C" Q_DECL_EXPORT
QPainterClipInfo *ritual_ZN16QPainterClipInfoC1ERK12QPainterPathN2Qt13ClipOperationERK10QTransform(
    const QPainterPath *p,
    Qt::ClipOperation op,
    const QTransform *m) {
  return new QPainterClipInfo(*p, op, *m);
}

//  QPainterClipInfo::QPainterClipInfo(const QRegion &r, Qt::ClipOperation
//      op, const QTransform &m)
extern "C" Q_DECL_EXPORT
QPainterClipInfo *ritual_ZN16QPainterClipInfoC1ERK7QRegionN2Qt13ClipOperationERK10QTransform(
    const QRegion *r,
    Qt::ClipOperation op,
    const QTransform *m) {
  return new QPainterClipInfo(*r, op, *m);
}

//  QPainterClipInfo::QPainterClipInfo(const QRect &r, Qt::ClipOperation op,
//      const QTransform &m)
extern "C" Q_DECL_EXPORT
QPainterClipInfo *ritual_ZN16QPainterClipInfoC1ERK5QRectN2Qt13ClipOperationERK10QTransform(
    const QRect *r,
    Qt::ClipOperation op,
    const QTransform *m) {
  return new QPainterClipInfo(*r, op, *m);
}

//  QPainterClipInfo::QPainterClipInfo(const QRectF &r, Qt::ClipOperation op,
//      const QTransform &m)
extern "C" Q_DECL_EXPORT
QPainterClipInfo *ritual_ZN16QPainterClipInfoC1ERK6QRectFN2Qt13ClipOperationERK10QTransform(
    const QRectF *r,
    Qt::ClipOperation op,
    const QTransform *m) {
  return new QPainterClipInfo(*r, op, *m);
}

//  QPainterClipInfo::~QPainterClipInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPainterClipInfoD1Ev(QPainterClipInfo *self) {
  delete self;
}
