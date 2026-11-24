//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPathSegments::Segment::Segment(int pathId, int vertexA, int vertexB)
extern "C" Q_DECL_EXPORT
QPathSegments::Segment *ritual_ZN13QPathSegments7SegmentC1Eiii(
    int pathId,
    int vertexA,
    int vertexB) {
  return new QPathSegments::Segment(pathId, vertexA, vertexB);
}

//  QPathSegments::Segment::~Segment()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPathSegments7SegmentD1Ev(QPathSegments::Segment *self) {
  delete self;
}
