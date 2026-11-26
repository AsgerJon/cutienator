//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextdocumentfragment.h>
#include <QtGui/private/qtextdocumentfragment_p.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/qtextlist.h>
#if QT_CONFIG(textmarkdownreader)
#include <QtGui/private/qtextmarkdownimporter_p.h>
#endif
#if QT_CONFIG(textmarkdownwriter)
#include <QtGui/private/qtextmarkdownwriter_p.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdatetime.h>
#include <QtCore/private/qstringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/text/qtextdocumentfragment.cpp, line 127, as _ZN15QTextCopyHelper4copyEv
inline void QTextCopyHelper::copy()
{
    if (cursor.hasComplexSelection()) {
        QTextTable *table = cursor.currentTable();
        int row_start, col_start, num_rows, num_cols;
        cursor.selectedTableCells(&row_start, &num_rows, &col_start, &num_cols);

        QTextTableFormat tableFormat = table->format();
        tableFormat.setColumns(num_cols);
        tableFormat.clearColumnWidthConstraints();
        const int objectIndex = dst->formatCollection()->createObjectIndex(tableFormat);

        Q_ASSERT(row_start != -1);
        for (int r = row_start; r < row_start + num_rows; ++r) {
            for (int c = col_start; c < col_start + num_cols; ++c) {
                QTextTableCell cell = table->cellAt(r, c);
                const int rspan = cell.rowSpan();
                const int cspan = cell.columnSpan();
                if (rspan != 1) {
                    int cr = cell.row();
                    if (cr != r)
                        continue;
                }
                if (cspan != 1) {
                    int cc = cell.column();
                    if (cc != c)
                        continue;
                }

                // add the QTextBeginningOfFrame
                QTextCharFormat cellFormat = cell.format();
                if (r + rspan >= row_start + num_rows) {
                    cellFormat.setTableCellRowSpan(row_start + num_rows - r);
                }
                if (c + cspan >= col_start + num_cols) {
                    cellFormat.setTableCellColumnSpan(col_start + num_cols - c);
                }
                const int charFormatIndex = convertFormatIndex(cellFormat, objectIndex);

                int blockIdx = -2;
                const int cellPos = cell.firstPosition();
                QTextBlock block = src->blocksFind(cellPos);
                if (block.position() == cellPos) {
                    blockIdx = convertFormatIndex(block.blockFormat());
                }

                dst->insertBlock(QTextBeginningOfFrame, insertPos, blockIdx, charFormatIndex);
                ++insertPos;

                // nothing to add for empty cells
                if (cell.lastPosition() > cellPos) {
                    // add the contents
                    appendFragments(cellPos, cell.lastPosition());
                }
            }
        }

        // add end of table
        int end = table->lastPosition();
        appendFragment(end, end+1, objectIndex);
    } else {
        appendFragments(cursor.selectionStart(), cursor.selectionEnd());
    }
}

//  from src/gui/text/qtextdocumentfragment.cpp, line 119, as _ZN15QTextCopyHelper15appendFragmentsEii
inline void QTextCopyHelper::appendFragments(int pos, int endPos)
{
    Q_ASSERT(pos < endPos);

    while (pos < endPos)
        pos += appendFragment(pos, endPos);
}

//  from src/gui/text/qtextdocumentfragment.cpp, line 60, as _ZN15QTextCopyHelper14appendFragmentEiii
inline int QTextCopyHelper::appendFragment(int pos, int endPos, int objectIndex)
{
    QTextDocumentPrivate::FragmentIterator fragIt = src->find(pos);
    const QTextFragmentData * const frag = fragIt.value();

    Q_ASSERT(objectIndex == -1
             || (frag->size_array[0] == 1 && src->formatCollection()->format(frag->format).objectIndex() != -1));

    int charFormatIndex;
    if (forceCharFormat)
       charFormatIndex = primaryCharFormatIndex;
    else
       charFormatIndex = convertFormatIndex(frag->format, objectIndex);

    const int inFragmentOffset = qMax(0, pos - fragIt.position());
    int charsToCopy = qMin(int(frag->size_array[0] - inFragmentOffset), endPos - pos);

    QTextBlock nextBlock = src->blocksFind(pos + 1);

    int blockIdx = -2;
    if (nextBlock.position() == pos + 1) {
        blockIdx = convertFormatIndex(nextBlock.blockFormat());
    } else if (pos == 0 && insertPos == 0) {
        dst->setBlockFormat(dst->blocksBegin(), dst->blocksBegin(), convertFormat(src->blocksBegin().blockFormat()).toBlockFormat());
        dst->setCharFormat(-1, 1, convertFormat(src->blocksBegin().charFormat()).toCharFormat());
    }

    QString txtToInsert(originalText.constData() + frag->stringPosition + inFragmentOffset, charsToCopy);
    if (txtToInsert.size() == 1
        && (txtToInsert.at(0) == QChar::ParagraphSeparator
            || txtToInsert.at(0) == QTextBeginningOfFrame
            || txtToInsert.at(0) == QTextEndOfFrame
           )
       ) {
        dst->insertBlock(txtToInsert.at(0), insertPos, blockIdx, charFormatIndex);
        ++insertPos;
    } else {
        if (nextBlock.textList()) {
            QTextBlock dstBlock = dst->blocksFind(insertPos);
            if (!dstBlock.textList()) {
                // insert a new text block with the block and char format from the
                // source block to make sure that the following text fragments
                // end up in a list as they should
                int listBlockFormatIndex = convertFormatIndex(nextBlock.blockFormat());
                int listCharFormatIndex = convertFormatIndex(nextBlock.charFormat());
                dst->insertBlock(insertPos, listBlockFormatIndex, listCharFormatIndex);
                ++insertPos;
            }
        }
        dst->insert(insertPos, txtToInsert, charFormatIndex);
        const int userState = nextBlock.userState();
        if (userState != -1)
            dst->blocksFind(insertPos).setUserState(userState);
        insertPos += txtToInsert.size();
    }

    return charsToCopy;
}

//  from src/gui/text/qtextdocumentfragment.cpp, line 40, as _ZN15QTextCopyHelper18convertFormatIndexERK11QTextFormati
inline int QTextCopyHelper::convertFormatIndex(const QTextFormat &oldFormat, int objectIndexToSet)
{
    QTextFormat fmt = oldFormat;
    if (objectIndexToSet != -1) {
        fmt.setObjectIndex(objectIndexToSet);
    } else if (fmt.objectIndex() != -1) {
        int newObjectIndex = objectIndexMap.value(fmt.objectIndex(), -1);
        if (newObjectIndex == -1) {
            QTextFormat objFormat = src->formatCollection()->objectFormat(fmt.objectIndex());
            Q_ASSERT(objFormat.objectIndex() == -1);
            newObjectIndex = formatCollection.createObjectIndex(objFormat);
            objectIndexMap.insert(fmt.objectIndex(), newObjectIndex);
        }
        fmt.setObjectIndex(newObjectIndex);
    }
    int idx = formatCollection.indexForFormat(fmt);
    Q_ASSERT(formatCollection.format(idx).type() == oldFormat.type());
    return idx;
}
//  -----------------------------------------------------------------------

//  void QTextCopyHelper::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCopyHelper4copyEv(QTextCopyHelper *self) {
  self->copy();
}

//  void QTextCopyHelper::appendFragments(int pos, int endPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCopyHelper15appendFragmentsEii(
    QTextCopyHelper *self,
    int pos,
    int endPos) {
  self->appendFragments(pos, endPos);
}

//  int QTextCopyHelper::appendFragment(int pos, int endPos, int objectIndex)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QTextCopyHelper14appendFragmentEiii(
    QTextCopyHelper *self,
    int pos,
    int endPos,
    int objectIndex) {
  return self->appendFragment(pos, endPos, objectIndex);
}

//  int QTextCopyHelper::convertFormatIndex(const QTextFormat &oldFormat, int
//      objectIndexToSet)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QTextCopyHelper18convertFormatIndexERK11QTextFormati(
    QTextCopyHelper *self,
    const QTextFormat *oldFormat,
    int objectIndexToSet) {
  return self->convertFormatIndex(*oldFormat, objectIndexToSet);
}

//  int QTextCopyHelper::convertFormatIndex(int oldFormatIndex, int
//      objectIndexToSet)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QTextCopyHelper18convertFormatIndexEii(
    QTextCopyHelper *self,
    int oldFormatIndex,
    int objectIndexToSet) {
  return self->convertFormatIndex(oldFormatIndex, objectIndexToSet);
}

//  QTextFormat QTextCopyHelper::convertFormat(const QTextFormat &fmt)
extern "C" Q_DECL_EXPORT
QTextFormat *ritual_ZN15QTextCopyHelper13convertFormatERK11QTextFormat(
    QTextCopyHelper *self,
    const QTextFormat *fmt) {
  return new QTextFormat(self->convertFormat(*fmt));
}

//  QTextCopyHelper::~QTextCopyHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextCopyHelperD1Ev(QTextCopyHelper *self) {
  delete self;
}
