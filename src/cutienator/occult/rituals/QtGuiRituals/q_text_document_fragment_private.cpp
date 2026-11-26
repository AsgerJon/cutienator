//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  -----------------------------------------------------------------------

//  QTextDocumentFragmentPrivate::~QTextDocumentFragmentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QTextDocumentFragmentPrivateD1Ev(
    QTextDocumentFragmentPrivate *self) {
  delete self;
}
