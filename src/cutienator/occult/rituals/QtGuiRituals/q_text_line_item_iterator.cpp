//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextengine.cpp, line 4069, as _ZN21QTextLineItemIteratorC1EP11QTextEngineiRK7QPointFPKN11QTextLayout11FormatRangeE
inline QTextLineItemIterator::QTextLineItemIterator(QTextEngine *_eng, int _lineNum, const QPointF &pos,
                                             const QTextLayout::FormatRange *_selection)
    : eng(_eng),
      line(eng->lines[_lineNum]),
      si(nullptr),
      lineNum(_lineNum),
      lineEnd(line.from + line.length),
      firstItem(eng->findItem(line.from)),
      lastItem(eng->findItem(lineEnd - 1, firstItem)),
      nItems((firstItem >= 0 && lastItem >= firstItem)? (lastItem-firstItem+1) : 0),
      logicalItem(-1),
      item(-1),
      visualOrder(nItems),
      selection(_selection)
{
    x = QFixed::fromReal(pos.x());

    x += line.x;

    x += eng->alignLine(line);

    if (nItems > 0) {
        QVarLengthArray<uchar> levels(nItems);
        for (int i = 0; i < nItems; ++i)
            levels[i] = eng->layoutData->items.at(i + firstItem).analysis.bidiLevel;
        QTextEngine::bidiReorder(nItems, levels.data(), visualOrder.data());
    }

    eng->shapeLine(line);
}

//  from src/gui/text/qtextengine.cpp, line 4139, as _ZNK21QTextLineItemIterator18getSelectionBoundsEP6QFixedS1_
inline bool QTextLineItemIterator::getSelectionBounds(QFixed *selectionX, QFixed *selectionWidth) const
{
    *selectionX = *selectionWidth = 0;

    if (!selection)
        return false;

    if (si->analysis.flags >= QScriptAnalysis::TabOrObject) {
        if (si->position >= selection->start + selection->length
            || si->position + itemLength <= selection->start)
            return false;

        *selectionX = x;
        *selectionWidth = itemWidth;
    } else {
        unsigned short *logClusters = eng->logClusters(si);
        QGlyphLayout glyphs = eng->shapedGlyphs(si);

        int from = qMax(itemStart, selection->start) - si->position;
        int to = qMin(itemEnd, selection->start + selection->length) - si->position;
        if (from >= to)
            return false;

        int start_glyph = logClusters[from];
        int end_glyph = (to == itemLength) ? si->num_glyphs : logClusters[to];
        QFixed soff;
        QFixed swidth;
        if (si->analysis.bidiLevel %2) {
            for (int g = glyphsEnd - 1; g >= end_glyph; --g)
                soff += glyphs.effectiveAdvance(g);
            for (int g = end_glyph - 1; g >= start_glyph; --g)
                swidth += glyphs.effectiveAdvance(g);
        } else {
            for (int g = glyphsStart; g < start_glyph; ++g)
                soff += glyphs.effectiveAdvance(g);
            for (int g = start_glyph; g < end_glyph; ++g)
                swidth += glyphs.effectiveAdvance(g);
        }

        // If the starting character is in the middle of a ligature,
        // selection should only contain the right part of that ligature
        // glyph, so we need to get the width of the left part here and
        // add it to *selectionX
        QFixed leftOffsetInLigature = eng->offsetInLigature(si, from, to, start_glyph);
        *selectionX = x + soff + leftOffsetInLigature;
        *selectionWidth = swidth - leftOffsetInLigature;
        // If the ending character is also part of a ligature, swidth does
        // not contain that part yet, we also need to find out the width of
        // that left part
        *selectionWidth += eng->offsetInLigature(si, to, itemLength, end_glyph);
    }
    return true;
}
//  -----------------------------------------------------------------------

//  QTextLineItemIterator::QTextLineItemIterator(QTextEngine *eng, int
//      lineNum, const QPointF &pos, const QTextLayout::FormatRange
//      *_selection)
extern "C" Q_DECL_EXPORT
QTextLineItemIterator *ritual_ZN21QTextLineItemIteratorC1EP11QTextEngineiRK7QPointFPKN11QTextLayout11FormatRangeE(
    QTextEngine *eng,
    int lineNum,
    const QPointF *pos,
    const QTextLayout::FormatRange *_selection) {
  return new QTextLineItemIterator(eng, lineNum, *pos, _selection);
}

//  bool QTextLineItemIterator::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QTextLineItemIterator5atEndEv(
    const QTextLineItemIterator *self) {
  return self->atEnd();
}

//  bool QTextLineItemIterator::atBeginning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QTextLineItemIterator11atBeginningEv(
    const QTextLineItemIterator *self) {
  return self->atBeginning();
}

//  bool QTextLineItemIterator::getSelectionBounds(QFixed *selectionX, QFixed
//      *selectionWidth) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QTextLineItemIterator18getSelectionBoundsEP6QFixedS1_(
    const QTextLineItemIterator *self,
    QFixed *selectionX,
    QFixed *selectionWidth) {
  return self->getSelectionBounds(selectionX, selectionWidth);
}

//  bool QTextLineItemIterator::isOutsideSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QTextLineItemIterator18isOutsideSelectionEv(
    const QTextLineItemIterator *self) {
  return self->isOutsideSelection();
}

//  QTextLineItemIterator::~QTextLineItemIterator()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QTextLineItemIteratorD1Ev(QTextLineItemIterator *self) {
  delete self;
}
