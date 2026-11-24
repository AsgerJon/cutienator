//  Written by dev_tooling.RitualGenerator from the records of QtCanvasPainte
//  r/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcrhidistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  bool QCRhiDistanceFieldGlyphCache::TextureInfo::operator==(const
//      TextureInfo &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QCRhiDistanceFieldGlyphCache11TextureInfoeqERKS0_(
    const QCRhiDistanceFieldGlyphCache::TextureInfo *self,
    const QCRhiDistanceFieldGlyphCache::TextureInfo *other) {
  return self->operator==(*other);
}

//  QCRhiDistanceFieldGlyphCache::TextureInfo::TextureInfo(const QRect
//      &preallocRect)
extern "C" Q_DECL_EXPORT
QCRhiDistanceFieldGlyphCache::TextureInfo *ritual_ZN28QCRhiDistanceFieldGlyphCache11TextureInfoC1ERK5QRect(
    const QRect *preallocRect) {
  return new QCRhiDistanceFieldGlyphCache::TextureInfo(*preallocRect);
}

//  QCRhiDistanceFieldGlyphCache::TextureInfo::~TextureInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QCRhiDistanceFieldGlyphCache11TextureInfoD1Ev(
    QCRhiDistanceFieldGlyphCache::TextureInfo *self) {
  delete self;
}
