//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qflatmap_p.h>
#include <QtGui/private/qtguiglobal_p.h>
#include "qdebug.h"
#include "qtextformat.h"
#include "qtextformat_p.h"
#include "qtextengine_p.h"
#include "qabstracttextdocumentlayout.h"
#include "qabstracttextdocumentlayout_p.h"
#include "qtextlayout.h"
#include "qtextboundaryfinder.h"
#include <QtCore/private/qunicodetables_p.h>
#include "qvarlengtharray.h"
#include "qfont.h"
#include "qfont_p.h"
#include "qfontengine_p.h"
#include "qstring.h"
#include "qtextdocument_p.h"
#include "qrawfont.h"
#include "qrawfont_p.h"
#include <qguiapplication.h>
#include <qinputmethod.h>
#include <qlocale.h>
#include <algorithm>
#include <stdlib.h>
#if QT_CONFIG(harfbuzz)
#include "qharfbuzzng_p.h"
#endif
#if !defined(QT_NO_EMOJISEGMENTER)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextengine.cpp, line 2959, as _ZN12QGlyphLayout4copyEPS_
inline void QGlyphLayout::copy(QGlyphLayout *oldLayout)
{
    Q_ASSERT(offsets != oldLayout->offsets);

    int n = std::min(numGlyphs, oldLayout->numGlyphs);

    memcpy(offsets, oldLayout->offsets, n * sizeof(QFixedPoint));
    memcpy(attributes, oldLayout->attributes, n * sizeof(QGlyphAttributes));
    memcpy(justifications, oldLayout->justifications, n * sizeof(QGlyphJustification));
    memcpy(advances, oldLayout->advances, n * sizeof(QFixed));
    memcpy(glyphs, oldLayout->glyphs, n * sizeof(glyph_t));

    numGlyphs = n;
}
//  -----------------------------------------------------------------------

//  QGlyphLayout::QGlyphLayout()
extern "C" Q_DECL_EXPORT
QGlyphLayout *ritual_ZN12QGlyphLayoutC1Ev() {
  return new QGlyphLayout();
}

//  QGlyphLayout QGlyphLayout::mid(int position, int n) const
extern "C" Q_DECL_EXPORT
QGlyphLayout *ritual_ZNK12QGlyphLayout3midEii(
    const QGlyphLayout *self,
    int position,
    int n) {
  return new QGlyphLayout(self->mid(position, n));
}

//  QFixed QGlyphLayout::effectiveAdvance(int item) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK12QGlyphLayout16effectiveAdvanceEi(
    const QGlyphLayout *self,
    int item) {
  return new QFixed(self->effectiveAdvance(item));
}

//  void QGlyphLayout::clear(int first, int last)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGlyphLayout5clearEii(
    QGlyphLayout *self,
    int first,
    int last) {
  self->clear(first, last);
}

//  void QGlyphLayout::copy(QGlyphLayout *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGlyphLayout4copyEPS_(
    QGlyphLayout *self,
    QGlyphLayout *other) {
  self->copy(other);
}

//  QGlyphLayout::~QGlyphLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGlyphLayoutD1Ev(QGlyphLayout *self) {
  delete self;
}
