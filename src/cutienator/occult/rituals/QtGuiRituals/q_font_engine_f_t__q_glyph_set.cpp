//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h, Qt 6.12.0, as the Qt
//  of macOS and the Qt of Windows install it. Its header needs
//  FreeType's, which these two install with Qt's, in the folder
//  'QtFreetype'.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only what its header
//  writes out is called.
//  Not written: its constructor, its destructor, 'removeGlyphFromCache',
//  'clear' and 'setGlyph', which Qt's library offers not.
//  Edited by hand on 2026-11-25: all after Qt's global headers stands
//  under '__has_include(<ft2build.h>)' as well, as the build on macOS
//  names no folder holding 'ft2build.h' to the compiler: it looks for a
//  part's headers only in the part's framework, and Qt's 'QtFreetype'
//  has none, its headers lying in 'include/QtFreetype'; there these
//  rituals are missing. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype) && __has_include(<ft2build.h>)
#include <QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h>

//  bool QFontEngineFT::QGlyphSet::useFastGlyphData(glyph_t index, const
//      QFixedPoint &subPixelPosition) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT9QGlyphSet16useFastGlyphDataEjRK11QFixedPoint(
    const QFontEngineFT::QGlyphSet *self,
    glyph_t index,
    const QFixedPoint *subPixelPosition) {
  return self->useFastGlyphData(index, *subPixelPosition);
}

//  Glyph *QFontEngineFT::QGlyphSet::getGlyph(glyph_t index, const
//      QFixedPoint &subPixelPositionX) const
extern "C" Q_DECL_EXPORT
QFontEngine::Glyph *ritual_ZNK13QFontEngineFT9QGlyphSet8getGlyphEjRK11QFixedPoint(
    const QFontEngineFT::QGlyphSet *self,
    glyph_t index,
    const QFixedPoint *subPixelPositionX) {
  return self->getGlyph(index, *subPixelPositionX);
}

//  bool QFontEngineFT::QGlyphSet::isGlyphMissing(glyph_t index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT9QGlyphSet14isGlyphMissingEj(
    const QFontEngineFT::QGlyphSet *self,
    glyph_t index) {
  return self->isGlyphMissing(index);
}

//  void QFontEngineFT::QGlyphSet::setGlyphMissing(glyph_t index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QFontEngineFT9QGlyphSet15setGlyphMissingEj(
    const QFontEngineFT::QGlyphSet *self,
    glyph_t index) {
  self->setGlyphMissing(index);
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype) && __has_include(<ft2build.h>)
