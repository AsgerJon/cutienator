//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h, Qt 6.12.0, as the Qt
//  of macOS and the Qt of Windows install it. Its header needs
//  FreeType's, which these two install with Qt's, in the folder
//  'QtFreetype'.
//  Qt's library offers none of its functions by name, a class inside an
//  exported one being no exported class itself: only what its header
//  writes out is called.
//  Edited by hand on 2026-11-25: all after Qt's global headers stands
//  under '__has_include(<ft2build.h>)' as well, as the build on macOS
//  names no folder holding 'ft2build.h' to the compiler: it looks for a
//  part's headers only in the part's framework, and Qt's 'QtFreetype'
//  has none, its headers lying in 'include/QtFreetype'; there this
//  ritual is missing. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype) && __has_include(<ft2build.h>)
#include <QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h>

//  QFontEngineFT::GlyphInfo::~GlyphInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFontEngineFT9GlyphInfoD1Ev(QFontEngineFT::GlyphInfo *self) {
  delete self;
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype) && __has_include(<ft2build.h>)
