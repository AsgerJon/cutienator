//  Written by dev_tooling.RitualGenerator from the records of QtCanvasPainte
//  r/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QCRhiDistanceFieldGlyphCache::TexturedPoint2D::set(float nx, float
//      ny, float ntx, float nty)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache15TexturedPoint2D3setEffff(
    QCRhiDistanceFieldGlyphCache::TexturedPoint2D *self,
    float nx,
    float ny,
    float ntx,
    float nty) {
  self->set(nx, ny, ntx, nty);
}

//  QCRhiDistanceFieldGlyphCache::TexturedPoint2D::~TexturedPoint2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache15TexturedPoint2DD1Ev(
    QCRhiDistanceFieldGlyphCache::TexturedPoint2D *self) {
  delete self;
}
