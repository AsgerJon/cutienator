//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontsubset_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontsubset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfontsubset_p.h"
#include <qdebug.h>
#include <qendian.h>
#include <qpainterpath.h>
#include "private/qpdf_p.h"
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qfontsubset.cpp, line 252, as _ZN11QFontSubset8addGlyphEj
#if !defined(QT_NO_PDF)
inline qsizetype QFontSubset::addGlyph(uint index)
{
    qsizetype idx = glyph_indices.indexOf(index);
    if (idx < 0) {
        idx = glyph_indices.size();
        glyph_indices.append(index);
    }
    return idx;
}
#endif  // !defined(QT_NO_PDF)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_PDF)
//  QFontSubset::QFontSubset(QFontEngine *fe, uint obj_id)
extern "C" Q_DECL_EXPORT
QFontSubset *ritual_ZN11QFontSubsetC1EP11QFontEnginej(
    QFontEngine *fe,
    uint obj_id) {
  return new QFontSubset(fe, obj_id);
}
#endif  // !defined(QT_NO_PDF)

//  QFontSubset::~QFontSubset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontSubsetD1Ev(QFontSubset *self) {
  delete self;
}

#if !defined(QT_NO_PDF)
//  qsizetype QFontSubset::addGlyph(uint index)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN11QFontSubset8addGlyphEj(QFontSubset *self, uint index) {
  return self->addGlyph(index);
}
#endif  // !defined(QT_NO_PDF)

//  qsizetype QFontSubset::nGlyphs() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QFontSubset7nGlyphsEv(const QFontSubset *self) {
  return self->nGlyphs();
}
