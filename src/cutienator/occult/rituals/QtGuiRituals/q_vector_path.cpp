//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qvectorpath_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qvectorpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpainterpath.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpainterpath_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QVectorPath::~QVectorPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QVectorPathD1Ev(QVectorPath *self) {
  delete self;
}

//  QRectF QVectorPath::controlPointRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QVectorPath16controlPointRectEv(
    const QVectorPath *self) {
  return new QRectF(self->controlPointRect());
}

//  Hint QVectorPath::shape() const
extern "C" Q_DECL_EXPORT
QVectorPath::Hint ritual_ZNK11QVectorPath5shapeEv(const QVectorPath *self) {
  return self->shape();
}

//  bool QVectorPath::isConvex() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath8isConvexEv(const QVectorPath *self) {
  return self->isConvex();
}

//  bool QVectorPath::isCurved() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath8isCurvedEv(const QVectorPath *self) {
  return self->isCurved();
}

//  bool QVectorPath::isCacheable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath11isCacheableEv(const QVectorPath *self) {
  return self->isCacheable();
}

//  bool QVectorPath::hasImplicitClose() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath16hasImplicitCloseEv(const QVectorPath *self) {
  return self->hasImplicitClose();
}

//  bool QVectorPath::hasExplicitOpen() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath15hasExplicitOpenEv(const QVectorPath *self) {
  return self->hasExplicitOpen();
}

//  bool QVectorPath::hasWindingFill() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath14hasWindingFillEv(const QVectorPath *self) {
  return self->hasWindingFill();
}

//  void QVectorPath::makeCacheable() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QVectorPath13makeCacheableEv(const QVectorPath *self) {
  self->makeCacheable();
}

//  uint QVectorPath::hints() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK11QVectorPath5hintsEv(const QVectorPath *self) {
  return self->hints();
}

//  bool QVectorPath::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath7isEmptyEv(const QVectorPath *self) {
  return self->isEmpty();
}

//  int QVectorPath::elementCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QVectorPath12elementCountEv(const QVectorPath *self) {
  return self->elementCount();
}

//  const QPainterPath QVectorPath::convertToPainterPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK11QVectorPath20convertToPainterPathEv(
    const QVectorPath *self) {
  return new QPainterPath(self->convertToPainterPath());
}

//  uint QVectorPath::polygonFlags(QPaintEngine::PolygonDrawMode mode)
extern "C" Q_DECL_EXPORT
uint ritual_ZN11QVectorPath12polygonFlagsEN12QPaintEngine15PolygonDrawModeE(
    QPaintEngine::PolygonDrawMode mode) {
  return QVectorPath::polygonFlags(mode);
}

//  CacheEntry *QVectorPath::lookupCacheData(QPaintEngineEx *engine) const
extern "C" Q_DECL_EXPORT
QVectorPath::CacheEntry *ritual_ZNK11QVectorPath15lookupCacheDataEP14QPaintEngineEx(
    const QVectorPath *self,
    QPaintEngineEx *engine) {
  return self->lookupCacheData(engine);
}

//  bool QVectorPath::isRect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QVectorPath6isRectEv(const QVectorPath *self) {
  return self->isRect();
}
