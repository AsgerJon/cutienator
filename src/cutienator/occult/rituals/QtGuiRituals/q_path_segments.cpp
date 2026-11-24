//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qline.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>

//  QPathSegments::QPathSegments(int reserve)
extern "C" Q_DECL_EXPORT
QPathSegments *ritual_ZN13QPathSegmentsC1Ei(int reserve) {
  return new QPathSegments(reserve);
}

//  int QPathSegments::intersections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPathSegments13intersectionsEv(const QPathSegments *self) {
  return self->intersections();
}

//  int QPathSegments::segments() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPathSegments8segmentsEv(const QPathSegments *self) {
  return self->segments();
}

//  int QPathSegments::points() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPathSegments6pointsEv(const QPathSegments *self) {
  return self->points();
}

//  const Segment &QPathSegments::segmentAt(int index) const
extern "C" Q_DECL_EXPORT
QPathSegments::Segment *ritual_ZNK13QPathSegments9segmentAtEi(
    const QPathSegments *self,
    int index) {
  return new QPathSegments::Segment(self->segmentAt(index));
}

//  const QLineF QPathSegments::lineAt(int index) const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK13QPathSegments6lineAtEi(
    const QPathSegments *self,
    int index) {
  return new QLineF(self->lineAt(index));
}

//  const QRectF &QPathSegments::elementBounds(int index) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK13QPathSegments13elementBoundsEi(
    const QPathSegments *self,
    int index) {
  return new QRectF(self->elementBounds(index));
}

//  int QPathSegments::pathId(int index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPathSegments6pathIdEi(
    const QPathSegments *self,
    int index) {
  return self->pathId(index);
}

//  const QPointF &QPathSegments::pointAt(int vertex) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QPathSegments7pointAtEi(
    const QPathSegments *self,
    int vertex) {
  return new QPointF(self->pointAt(vertex));
}

//  int QPathSegments::addPoint(const QPointF &point)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QPathSegments8addPointERK7QPointF(
    QPathSegments *self,
    const QPointF *point) {
  return self->addPoint(*point);
}

//  const Intersection *QPathSegments::intersectionAt(int index) const
extern "C" Q_DECL_EXPORT
const QPathSegments::Intersection *ritual_ZNK13QPathSegments14intersectionAtEi(
    const QPathSegments *self,
    int index) {
  return self->intersectionAt(index);
}

//  void QPathSegments::addIntersection(int index, const Intersection
//      &intersection)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPathSegments15addIntersectionEiRKNS_12IntersectionE(
    QPathSegments *self,
    int index,
    const QPathSegments::Intersection *intersection) {
  self->addIntersection(index, *intersection);
}
