//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTriangulatingStroker::QTriangulatingStroker()
extern "C" Q_DECL_EXPORT
QTriangulatingStroker *ritual_ZN21QTriangulatingStrokerC1Ev() {
  return new QTriangulatingStroker();
}

//  int QTriangulatingStroker::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QTriangulatingStroker11vertexCountEv(
    const QTriangulatingStroker *self) {
  return self->vertexCount();
}

//  void QTriangulatingStroker::setInvScale(qreal invScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker11setInvScaleEd(
    QTriangulatingStroker *self,
    qreal invScale) {
  self->setInvScale(invScale);
}

//  void QTriangulatingStroker::emitLineSegment(float x, float y, float nx,
//      float ny)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker15emitLineSegmentEffff(
    QTriangulatingStroker *self,
    float x,
    float y,
    float nx,
    float ny) {
  self->emitLineSegment(x, y, nx, ny);
}

//  void QTriangulatingStroker::normalVector(float x1, float y1, float x2,
//      float y2, float *nx, float *ny)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker12normalVectorEffffPfS0_(
    QTriangulatingStroker *self,
    float x1,
    float y1,
    float x2,
    float y2,
    float *nx,
    float *ny) {
  self->normalVector(x1, y1, x2, y2, nx, ny);
}
