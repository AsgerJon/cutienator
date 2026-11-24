//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbezier_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbezier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qpolygon.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qline.h>

//  QBezier QBezier::fromPoints(const QPointF &p1, const QPointF &p2, const
//      QPointF &p3, const QPointF &p4)
extern "C" Q_DECL_EXPORT
QBezier *ritual_ZN7QBezier10fromPointsERK7QPointFS2_S2_S2_(
    const QPointF *p1,
    const QPointF *p2,
    const QPointF *p3,
    const QPointF *p4) {
  return new QBezier(QBezier::fromPoints(*p1, *p2, *p3, *p4));
}

//  void QBezier::coefficients(qreal t, qreal &a, qreal &b, qreal &c, qreal
//      &d)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBezier12coefficientsEdRdS0_S0_S0_(
    qreal t,
    qreal *a,
    qreal *b,
    qreal *c,
    qreal *d) {
  QBezier::coefficients(t, *a, *b, *c, *d);
}

//  QPointF QBezier::pointAt(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier7pointAtEd(const QBezier *self, qreal t) {
  return new QPointF(self->pointAt(t));
}

//  QPointF QBezier::normalVector(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier12normalVectorEd(const QBezier *self, qreal t) {
  return new QPointF(self->normalVector(t));
}

//  QPointF QBezier::derivedAt(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier9derivedAtEd(const QBezier *self, qreal t) {
  return new QPointF(self->derivedAt(t));
}

//  QPointF QBezier::secondDerivedAt(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier15secondDerivedAtEd(
    const QBezier *self,
    qreal t) {
  return new QPointF(self->secondDerivedAt(t));
}

//  QPolygonF QBezier::toPolygon(qreal bezier_flattening_threshold) const
extern "C" Q_DECL_EXPORT
QPolygonF *ritual_ZNK7QBezier9toPolygonEd(
    const QBezier *self,
    qreal bezier_flattening_threshold) {
  return new QPolygonF(self->toPolygon(bezier_flattening_threshold));
}

//  void QBezier::addToPolygon(QPolygonF *p, qreal
//      bezier_flattening_threshold) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QBezier12addToPolygonEP9QPolygonFd(
    const QBezier *self,
    QPolygonF *p,
    qreal bezier_flattening_threshold) {
  self->addToPolygon(p, bezier_flattening_threshold);
}

//  QRectF QBezier::bounds() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK7QBezier6boundsEv(const QBezier *self) {
  return new QRectF(self->bounds());
}

//  qreal QBezier::length(qreal error) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBezier6lengthEd(const QBezier *self, qreal error) {
  return self->length(error);
}

//  void QBezier::addIfClose(qreal *length, qreal error) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK7QBezier10addIfCloseEPdd(
    const QBezier *self,
    qreal *length,
    qreal error) {
  self->addIfClose(length, error);
}

//  qreal QBezier::tAtLength(qreal len) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBezier9tAtLengthEd(const QBezier *self, qreal len) {
  return self->tAtLength(len);
}

//  int QBezier::stationaryYPoints(qreal &t0, qreal &t1) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QBezier17stationaryYPointsERdS0_(
    const QBezier *self,
    qreal *t0,
    qreal *t1) {
  return self->stationaryYPoints(*t0, *t1);
}

//  qreal QBezier::tForY(qreal t0, qreal t1, qreal y) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QBezier5tForYEddd(
    const QBezier *self,
    qreal t0,
    qreal t1,
    qreal y) {
  return self->tForY(t0, t1, y);
}

//  QPointF QBezier::pt1() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier3pt1Ev(const QBezier *self) {
  return new QPointF(self->pt1());
}

//  QPointF QBezier::pt2() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier3pt2Ev(const QBezier *self) {
  return new QPointF(self->pt2());
}

//  QPointF QBezier::pt3() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier3pt3Ev(const QBezier *self) {
  return new QPointF(self->pt3());
}

//  QPointF QBezier::pt4() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier3pt4Ev(const QBezier *self) {
  return new QPointF(self->pt4());
}

//  QBezier QBezier::mapBy(const QTransform &transform) const
extern "C" Q_DECL_EXPORT
QBezier *ritual_ZNK7QBezier5mapByERK10QTransform(
    const QBezier *self,
    const QTransform *transform) {
  return new QBezier(self->mapBy(*transform));
}

//  QPointF QBezier::midPoint() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QBezier8midPointEv(const QBezier *self) {
  return new QPointF(self->midPoint());
}

//  QLineF QBezier::midTangent() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK7QBezier10midTangentEv(const QBezier *self) {
  return new QLineF(self->midTangent());
}

//  QLineF QBezier::startTangent() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK7QBezier12startTangentEv(const QBezier *self) {
  return new QLineF(self->startTangent());
}

//  QLineF QBezier::endTangent() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK7QBezier10endTangentEv(const QBezier *self) {
  return new QLineF(self->endTangent());
}

//  void QBezier::parameterSplitLeft(qreal t, QBezier *left)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBezier18parameterSplitLeftEdPS_(
    QBezier *self,
    qreal t,
    QBezier *left) {
  self->parameterSplitLeft(t, left);
}

//  int QBezier::shifted(QBezier *curveSegments, int maxSegmets, qreal
//      offset, float threshold) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QBezier7shiftedEPS_idf(
    const QBezier *self,
    QBezier *curveSegments,
    int maxSegmets,
    qreal offset,
    float threshold) {
  return self->shifted(curveSegments, maxSegmets, offset, threshold);
}

//  QBezier QBezier::bezierOnInterval(qreal t0, qreal t1) const
extern "C" Q_DECL_EXPORT
QBezier *ritual_ZNK7QBezier16bezierOnIntervalEdd(
    const QBezier *self,
    qreal t0,
    qreal t1) {
  return new QBezier(self->bezierOnInterval(t0, t1));
}

//  QBezier QBezier::getSubRange(qreal t0, qreal t1) const
extern "C" Q_DECL_EXPORT
QBezier *ritual_ZNK7QBezier11getSubRangeEdd(
    const QBezier *self,
    qreal t0,
    qreal t1) {
  return new QBezier(self->getSubRange(t0, t1));
}

//  QBezier::~QBezier()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QBezierD1Ev(QBezier *self) {
  delete self;
}
