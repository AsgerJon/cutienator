//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h, Qt 6.12.0, as the Qt
//  of macOS and the Qt of Windows install it. Its header needs
//  FreeType's, which these two install with Qt's, in the folder
//  'QtFreetype'.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only what its header
//  writes out is called.
//  Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype)
#include <QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h>

//  QFontEngineFT::GlyphAndSubPixelPosition::GlyphAndSubPixelPosition(glyph_t
//      g, const QFixedPoint spp)
extern "C" Q_DECL_EXPORT
QFontEngineFT::GlyphAndSubPixelPosition *ritual_ZN13QFontEngineFT24GlyphAndSubPixelPositionC1Ej11QFixedPoint(
    glyph_t g,
    const QFixedPoint *spp) {
  return new QFontEngineFT::GlyphAndSubPixelPosition(g, *spp);
}

//  bool QFontEngineFT::GlyphAndSubPixelPosition::operator==(const
//      GlyphAndSubPixelPosition &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFontEngineFT24GlyphAndSubPixelPositioneqERKS0_(
    const QFontEngineFT::GlyphAndSubPixelPosition *self,
    const QFontEngineFT::GlyphAndSubPixelPosition *other) {
  return *self == *other;
}

//  QFontEngineFT::GlyphAndSubPixelPosition::~GlyphAndSubPixelPosition()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT24GlyphAndSubPixelPositionD1Ev(
    QFontEngineFT::GlyphAndSubPixelPosition *self) {
  delete self;
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype)
