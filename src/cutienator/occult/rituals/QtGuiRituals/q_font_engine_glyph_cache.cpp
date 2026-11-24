//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontengineglyphcache_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontengineglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtGui/qcolor.h>

//  QFontEngineGlyphCache::QFontEngineGlyphCache(QFontEngine::GlyphFormat
//      format, const QTransform &matrix, const QColor &color)
extern "C" Q_DECL_EXPORT
QFontEngineGlyphCache *ritual_ZN21QFontEngineGlyphCacheC1EN11QFontEngine11GlyphFormatERK10QTransformRK6QColor(
    QFontEngine::GlyphFormat format,
    const QTransform *matrix,
    const QColor *color) {
  return new QFontEngineGlyphCache(format, *matrix, *color);
}

//  QFontEngineGlyphCache::~QFontEngineGlyphCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QFontEngineGlyphCacheD1Ev(QFontEngineGlyphCache *self) {
  delete self;
}

//  QFontEngine::GlyphFormat QFontEngineGlyphCache::glyphFormat() const
extern "C" Q_DECL_EXPORT
QFontEngine::GlyphFormat ritual_ZNK21QFontEngineGlyphCache11glyphFormatEv(
    const QFontEngineGlyphCache *self) {
  return self->glyphFormat();
}

//  const QTransform &QFontEngineGlyphCache::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK21QFontEngineGlyphCache9transformEv(
    const QFontEngineGlyphCache *self) {
  return new QTransform(self->transform());
}

//  const QColor &QFontEngineGlyphCache::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK21QFontEngineGlyphCache5colorEv(
    const QFontEngineGlyphCache *self) {
  return new QColor(self->color());
}
