//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgfont_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgfont_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpainterpath.h>

//  QSvgGlyph::QSvgGlyph(const QString &unicode, const QPainterPath &path,
//      qreal horizAdvX)
extern "C" Q_DECL_EXPORT
QSvgGlyph *ritual_ZN9QSvgGlyphC1ERK7QStringRK12QPainterPathd(
    const QString *unicode,
    const QPainterPath *path,
    qreal horizAdvX) {
  return new QSvgGlyph(*unicode, *path, horizAdvX);
}

//  QSvgGlyph::QSvgGlyph()
extern "C" Q_DECL_EXPORT
QSvgGlyph *ritual_ZN9QSvgGlyphC1Ev() {
  return new QSvgGlyph();
}

//  QSvgGlyph::~QSvgGlyph()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgGlyphD1Ev(QSvgGlyph *self) {
  delete self;
}
