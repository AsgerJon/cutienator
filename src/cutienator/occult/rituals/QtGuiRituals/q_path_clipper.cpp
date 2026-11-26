//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpainterpath.h>
#include <QtCore/qrect.h>

//  QPathClipper::QPathClipper(const QPainterPath &subject, const
//      QPainterPath &clip)
extern "C" Q_DECL_EXPORT
QPathClipper *ritual_ZN12QPathClipperC1ERK12QPainterPathS2_(
    const QPainterPath *subject,
    const QPainterPath *clip) {
  return new QPathClipper(*subject, *clip);
}

//  QPainterPath QPathClipper::clip(Operation op)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12QPathClipper4clipENS_9OperationE(
    QPathClipper *self,
    QPathClipper::Operation op) {
  return new QPainterPath(self->clip(op));
}

//  bool QPathClipper::intersect()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPathClipper9intersectEv(QPathClipper *self) {
  return self->intersect();
}

//  bool QPathClipper::contains()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPathClipper8containsEv(QPathClipper *self) {
  return self->contains();
}

//  bool QPathClipper::pathToRect(const QPainterPath &path, QRectF *rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPathClipper10pathToRectERK12QPainterPathP6QRectF(
    const QPainterPath *path,
    QRectF *rect) {
  return QPathClipper::pathToRect(*path, rect);
}

//  QPainterPath QPathClipper::intersect(const QPainterPath &path, const
//      QRectF &rect)
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZN12QPathClipper9intersectERK12QPainterPathRK6QRectF(
    const QPainterPath *path,
    const QRectF *rect) {
  return new QPainterPath(QPathClipper::intersect(*path, *rect));
}

//  bool QPathClipper::handleCrossingEdges(QWingedEdge &list, qreal y,
//      ClipperMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPathClipper19handleCrossingEdgesER11QWingedEdgedNS_11ClipperModeE(
    QPathClipper *self,
    QWingedEdge *list,
    qreal y,
    QPathClipper::ClipperMode mode) {
  return self->handleCrossingEdges(*list, y, mode);
}

//  bool QPathClipper::doClip(QWingedEdge &list, ClipperMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPathClipper6doClipER11QWingedEdgeNS_11ClipperModeE(
    QPathClipper *self,
    QWingedEdge *list,
    QPathClipper::ClipperMode mode) {
  return self->doClip(*list, mode);
}
