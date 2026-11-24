//  Written by dev_tooling.RitualGenerator from the records of QtCanvasPainte
//  r/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcdistancefieldglyphcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qrawfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qcdistancefieldglyphcache_p.h"
#include "qcanvaspainter_p.h"
#include <private/qrawfont_p.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/engine/qcdistancefieldglyphcache.cpp, line 425, as _ZN25QCDistanceFieldGlyphCache7FontKeyC1ERK8QRawFont
inline QCDistanceFieldGlyphCache::FontKey::FontKey(const QRawFont &font)
{
    QFontEngine *fe = QRawFontPrivate::get(font)->fontEngine;
    if (fe != nullptr)
        faceId = fe->faceId();
    style = font.style();
    weight = font.weight();
    if (faceId.filename.isEmpty()) {
        familyName = font.familyName();
        styleName = font.styleName();
    }
}
//  -----------------------------------------------------------------------

//  QCDistanceFieldGlyphCache::FontKey::FontKey(const QRawFont &font)
extern "C" Q_DECL_EXPORT
QCDistanceFieldGlyphCache::FontKey *ritual_ZN25QCDistanceFieldGlyphCache7FontKeyC1ERK8QRawFont(
    const QRawFont *font) {
  return new QCDistanceFieldGlyphCache::FontKey(*font);
}

//  QCDistanceFieldGlyphCache::FontKey::~FontKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCDistanceFieldGlyphCache7FontKeyD1Ev(
    QCDistanceFieldGlyphCache::FontKey *self) {
  delete self;
}
