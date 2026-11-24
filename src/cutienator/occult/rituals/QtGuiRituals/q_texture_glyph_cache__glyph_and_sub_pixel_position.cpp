//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextureglyphcache_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTextureGlyphCache::GlyphAndSubPixelPosition::GlyphAndSubPixelPosition(gl
//      yph_t g, const QFixedPoint &spp)
extern "C" Q_DECL_EXPORT
QTextureGlyphCache::GlyphAndSubPixelPosition *ritual_ZN18QTextureGlyphCache24GlyphAndSubPixelPositionC1EjRK11QFixedPoint(
    glyph_t g,
    const QFixedPoint *spp) {
  return new QTextureGlyphCache::GlyphAndSubPixelPosition(g, *spp);
}

//  bool QTextureGlyphCache::GlyphAndSubPixelPosition::operator==(const
//      GlyphAndSubPixelPosition &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTextureGlyphCache24GlyphAndSubPixelPositioneqERKS0_(
    const QTextureGlyphCache::GlyphAndSubPixelPosition *self,
    const QTextureGlyphCache::GlyphAndSubPixelPosition *other) {
  return self->operator==(*other);
}

//  QTextureGlyphCache::GlyphAndSubPixelPosition::~GlyphAndSubPixelPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextureGlyphCache24GlyphAndSubPixelPositionD1Ev(
    QTextureGlyphCache::GlyphAndSubPixelPosition *self) {
  delete self;
}
