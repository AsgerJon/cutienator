//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qflatmap_p.h>
#include <QtGui/private/qtguiglobal_p.h>
#include <QtCore/qdebug.h>
#include <QtGui/qtextformat.h>
#include <QtGui/private/qtextformat_p.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qtextboundaryfinder.h>
#include <QtCore/private/qunicodetables_p.h>
#include <QtCore/qvarlengtharray.h>
#include <QtGui/qfont.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtCore/qstring.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qrawfont.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qinputmethod.h>
#include <QtCore/qlocale.h>
#include <algorithm>
#include <stdlib.h>
#if QT_CONFIG(harfbuzz)
#include <QtGui/private/qharfbuzzng_p.h>
#endif
#if !defined(QT_NO_EMOJISEGMENTER)
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextengine.cpp, line 3963, as _ZN12QTextItemIntC1ERK11QScriptItemP5QFontRK15QTextCharFormat
inline QTextItemInt::QTextItemInt(const QScriptItem &si, QFont *font, const QTextCharFormat &format)
    : charFormat(format),
      f(font),
      fontEngine(font->d->engineForScript(si.analysis.script))
{
    Q_ASSERT(fontEngine);

    initWithScriptItem(si);
}

//  from src/gui/text/qtextengine.cpp, line 3973, as _ZN12QTextItemIntC1ERK12QGlyphLayoutP5QFontPK5QChariP11QFontEngineRK15QTextCharFormat
inline QTextItemInt::QTextItemInt(const QGlyphLayout &g, QFont *font, const QChar *chars_, int numChars, QFontEngine *fe, const QTextCharFormat &format)
    : charFormat(format),
      num_chars(numChars),
      chars(chars_),
      f(font),
      glyphs(g),
      fontEngine(fe)
{
}

//  from src/gui/text/qtextengine.cpp, line 4011, as _ZNK12QTextItemInt7midItemEP11QFontEngineii
inline QTextItemInt QTextItemInt::midItem(QFontEngine *fontEngine, int firstGlyphIndex, int numGlyphs) const
{
    QTextItemInt ti = *this;
    const int end = firstGlyphIndex + numGlyphs;
    ti.glyphs = glyphs.mid(firstGlyphIndex, numGlyphs);
    ti.fontEngine = fontEngine;

    if (logClusters && chars) {
        const int logClusterOffset = logClusters[0];
        while (logClusters[ti.chars - chars] - logClusterOffset < firstGlyphIndex)
            ++ti.chars;

        ti.logClusters += (ti.chars - chars);

        ti.num_chars = 0;
        int char_start = ti.chars - chars;
        while (char_start + ti.num_chars < num_chars && ti.logClusters[ti.num_chars] - logClusterOffset < end)
            ++ti.num_chars;
    }
    return ti;
}

//  from src/gui/text/qtextengine.cpp, line 3984, as _ZN12QTextItemInt18initWithScriptItemERK11QScriptItem
inline void QTextItemInt::initWithScriptItem(const QScriptItem &si)
{
    // explicitly initialize flags so that initFontAttributes can be called
    // multiple times on the same TextItem
    flags = { };
    if (si.analysis.bidiLevel %2)
        flags |= QTextItem::RightToLeft;
    ascent = si.ascent;
    descent = si.descent;

    if (charFormat.hasProperty(QTextFormat::TextUnderlineStyle)) {
        underlineStyle = charFormat.underlineStyle();
    } else if (charFormat.boolProperty(QTextFormat::FontUnderline)
               || f->d->underline) {
        underlineStyle = QTextCharFormat::SingleUnderline;
    }

    // compat
    if (underlineStyle == QTextCharFormat::SingleUnderline)
        flags |= QTextItem::Underline;

    if (f->d->overline || charFormat.fontOverline())
        flags |= QTextItem::Overline;
    if (f->d->strikeOut || charFormat.fontStrikeOut())
        flags |= QTextItem::StrikeOut;
}
//  -----------------------------------------------------------------------

//  QTextItemInt::QTextItemInt()
extern "C" Q_DECL_EXPORT
QTextItemInt *ritual_ZN12QTextItemIntC1Ev() {
  return new QTextItemInt();
}

//  QTextItemInt::QTextItemInt(const QScriptItem &si, QFont *font, const
//      QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
QTextItemInt *ritual_ZN12QTextItemIntC1ERK11QScriptItemP5QFontRK15QTextCharFormat(
    const QScriptItem *si,
    QFont *font,
    const QTextCharFormat *format) {
  return new QTextItemInt(*si, font, *format);
}

//  QTextItemInt::QTextItemInt(const QGlyphLayout &g, QFont *font, const
//      QChar *chars, int numChars, QFontEngine *fe, const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
QTextItemInt *ritual_ZN12QTextItemIntC1ERK12QGlyphLayoutP5QFontPK5QChariP11QFontEngineRK15QTextCharFormat(
    const QGlyphLayout *g,
    QFont *font,
    const QChar *chars,
    int numChars,
    QFontEngine *fe,
    const QTextCharFormat *format) {
  return new QTextItemInt(*g, font, chars, numChars, fe, *format);
}

//  QTextItemInt QTextItemInt::midItem(QFontEngine *fontEngine, int
//      firstGlyphIndex, int numGlyphs) const
extern "C" Q_DECL_EXPORT
QTextItemInt *ritual_ZNK12QTextItemInt7midItemEP11QFontEngineii(
    const QTextItemInt *self,
    QFontEngine *fontEngine,
    int firstGlyphIndex,
    int numGlyphs) {
  return new QTextItemInt(
      self->midItem(
          fontEngine,
          firstGlyphIndex,
          numGlyphs));
}

//  void QTextItemInt::initWithScriptItem(const QScriptItem &si)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextItemInt18initWithScriptItemERK11QScriptItem(
    QTextItemInt *self,
    const QScriptItem *si) {
  self->initWithScriptItem(*si);
}

//  QTextItemInt::~QTextItemInt()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTextItemIntD1Ev(QTextItemInt *self) {
  delete self;
}
