//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>
#include <QtCore/qrect.h>

//  QTriangulatingStroker::QTriangulatingStroker()
extern "C" Q_DECL_EXPORT
QTriangulatingStroker *ritual_ZN21QTriangulatingStrokerC1Ev() {
  return new QTriangulatingStroker();
}

//  void QTriangulatingStroker::process(const QVectorPath &path, const QPen
//      &pen, const QRectF &clip, QPainter::RenderHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker7processERK11QVectorPathRK4QPenRK6QRectF6QFlagsIN8QPainter10RenderHintEE(
    QTriangulatingStroker *self,
    const QVectorPath *path,
    const QPen *pen,
    const QRectF *clip,
    int hints) {
  self->process(
      *path,
      *pen,
      *clip,
      QFlags<QPainter::RenderHint>::fromInt(hints));
}

//  int QTriangulatingStroker::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QTriangulatingStroker11vertexCountEv(
    const QTriangulatingStroker *self) {
  return self->vertexCount();
}

//  const float *QTriangulatingStroker::vertices() const
extern "C" Q_DECL_EXPORT
const float *ritual_ZNK21QTriangulatingStroker8verticesEv(
    const QTriangulatingStroker *self) {
  return self->vertices();
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

//  void QTriangulatingStroker::moveTo(const qreal *pts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker6moveToEPKd(
    QTriangulatingStroker *self,
    const qreal *pts) {
  self->moveTo(pts);
}

//  void QTriangulatingStroker::lineTo(const qreal *pts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker6lineToEPKd(
    QTriangulatingStroker *self,
    const qreal *pts) {
  self->lineTo(pts);
}

//  void QTriangulatingStroker::cubicTo(const qreal *pts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker7cubicToEPKd(
    QTriangulatingStroker *self,
    const qreal *pts) {
  self->cubicTo(pts);
}

//  void QTriangulatingStroker::join(const qreal *pts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker4joinEPKd(
    QTriangulatingStroker *self,
    const qreal *pts) {
  self->join(pts);
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

//  void QTriangulatingStroker::endCap(const qreal *pts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker6endCapEPKd(
    QTriangulatingStroker *self,
    const qreal *pts) {
  self->endCap(pts);
}

//  void QTriangulatingStroker::arcPoints(float cx, float cy, float fromX,
//      float fromY, float toX, float toY, QVarLengthArray<float> &points)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker9arcPointsEffffffR15QVarLengthArrayIfLx256EE(
    QTriangulatingStroker *self,
    float cx,
    float cy,
    float fromX,
    float fromY,
    float toX,
    float toY,
    QVarLengthArray<float> *points) {
  self->arcPoints(cx, cy, fromX, fromY, toX, toY, *points);
}

//  void QTriangulatingStroker::endCapOrJoinClosed(const qreal *start, const
//      qreal *cur, bool implicitClose, bool endsAtStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTriangulatingStroker18endCapOrJoinClosedEPKdS1_bb(
    QTriangulatingStroker *self,
    const qreal *start,
    const qreal *cur,
    bool implicitClose,
    bool endsAtStart) {
  self->endCapOrJoinClosed(start, cur, implicitClose, endsAtStart);
}
