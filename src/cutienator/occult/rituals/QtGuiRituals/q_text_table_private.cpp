//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexttable_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qtexttable.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexttable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#include <QtCore/qchar.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtexttable.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qdebug.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/private/qtexttable_p.h>
#include <QtCore/qvarlengtharray.h>
#include <algorithm>
#include <stdlib.h>
#include <QtGui/qtextobject.h>
#include <QtGui/private/qtextobject_p.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextformat_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtCore/qdebug.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/text/qtexttable.cpp, line 333, as local:qtexttable.cpp:QFragmentFindHelper
struct QFragmentFindHelper
{
    inline QFragmentFindHelper(int _pos, const QTextDocumentPrivate::FragmentMap &map)
        : pos(_pos), fragmentMap(map) {}
    uint pos;
    const QTextDocumentPrivate::FragmentMap &fragmentMap;
};

//  from src/gui/text/qtexttable.cpp, line 379, as _ZN17QTextTablePrivate15fragmentRemovedE5QCharj
inline void QTextTablePrivate::fragmentRemoved(QChar type, uint fragment)
{
    dirty = true;
    if (blockFragmentUpdates)
        return;
    if (type == QTextBeginningOfFrame) {
        Q_ASSERT(cells.indexOf(int(fragment)) != -1);
        cells.removeAll(int(fragment));
        if (fragment_start == fragment && cells.size()) {
            fragment_start = cells.at(0);
        }
        if (fragment_start != fragment)
            return;
    }
    QTextFramePrivate::fragmentRemoved(type, fragment);
}

//  from src/gui/text/qtextobject.cpp, line 491, as _ZN17QTextFramePrivate13fragmentAddedE5QCharj
inline void QTextFramePrivate::fragmentAdded(QChar type, uint fragment)
{
    if (type == QTextBeginningOfFrame) {
        Q_ASSERT(!fragment_start);
        fragment_start = fragment;
    } else if (type == QTextEndOfFrame) {
        Q_ASSERT(!fragment_end);
        fragment_end = fragment;
    } else if (type == QChar::ObjectReplacementCharacter) {
        Q_ASSERT(!fragment_start);
        Q_ASSERT(!fragment_end);
        fragment_start = fragment;
        fragment_end = fragment;
    } else {
        Q_ASSERT(false);
    }
}

//  from src/gui/text/qtextobject.cpp, line 509, as _ZN17QTextFramePrivate15fragmentRemovedE5QCharj
inline void QTextFramePrivate::fragmentRemoved(QChar type, uint fragment)
{
    Q_UNUSED(fragment); // --release warning
    if (type == QTextBeginningOfFrame) {
        Q_ASSERT(fragment_start == fragment);
        fragment_start = 0;
    } else if (type == QTextEndOfFrame) {
        Q_ASSERT(fragment_end == fragment);
        fragment_end = 0;
    } else if (type == QChar::ObjectReplacementCharacter) {
        Q_ASSERT(fragment_start == fragment);
        Q_ASSERT(fragment_end == fragment);
        fragment_start = 0;
        fragment_end = 0;
    } else {
        Q_ASSERT(false);
    }
    remove_me();
}

//  from src/gui/text/qtextobject.cpp, line 530, as _ZN17QTextFramePrivate9remove_meEv
inline void QTextFramePrivate::remove_me()
{
    Q_Q(QTextFrame);
    if (fragment_start == 0 && fragment_end == 0
        && !parentFrame) {
        QTextDocumentPrivate::get(q->document())->deleteObject(q);
        return;
    }

    if (!parentFrame)
        return;

    int index = parentFrame->d_func()->childFrames.indexOf(q);

    // iterator over all children and move them to the parent
    for (int i = 0; i < childFrames.size(); ++i) {
        QTextFrame *c = childFrames.at(i);
        parentFrame->d_func()->childFrames.insert(index, c);
        c->d_func()->parentFrame = parentFrame;
        ++index;
    }
    Q_ASSERT(parentFrame->d_func()->childFrames.at(index) == q);
    parentFrame->d_func()->childFrames.removeAt(index);

    childFrames.clear();
    parentFrame = nullptr;
}

//  from src/gui/text/qtexttable.cpp, line 289, as _ZN17QTextTablePrivate11createTableEP20QTextDocumentPrivateiiiRK16QTextTableFormat
inline QTextTable *QTextTablePrivate::createTable(QTextDocumentPrivate *pieceTable, int pos, int rows, int cols, const QTextTableFormat &tableFormat)
{
    QTextTableFormat fmt = tableFormat;
    fmt.setColumns(cols);
    QTextTable *table = qobject_cast<QTextTable *>(pieceTable->createObject(fmt));
    Q_ASSERT(table);

    pieceTable->beginEditBlock();

//     qDebug("---> createTable: rows=%d, cols=%d at %d", rows, cols, pos);
    // add block after table
    QTextCharFormat charFmt;
    charFmt.setObjectIndex(table->objectIndex());
    charFmt.setObjectType(QTextFormat::TableCellObject);


    int charIdx = pieceTable->formatCollection()->indexForFormat(charFmt);
    int cellIdx = pieceTable->formatCollection()->indexForFormat(QTextBlockFormat());

    QTextTablePrivate *d = table->d_func();
    d->blockFragmentUpdates = true;

    d->fragment_start = pieceTable->insertBlock(QTextBeginningOfFrame, pos, cellIdx, charIdx);
    d->cells.append(d->fragment_start);
    ++pos;

    for (int i = 1; i < rows*cols; ++i) {
        d->cells.append(pieceTable->insertBlock(QTextBeginningOfFrame, pos, cellIdx, charIdx));
//      qDebug("      addCell at %d", pos);
        ++pos;
    }

    d->fragment_end = pieceTable->insertBlock(QTextEndOfFrame, pos, cellIdx, charIdx);
//  qDebug("      addEOR at %d", pos);
    ++pos;

    d->blockFragmentUpdates = false;
    d->dirty = true;

    pieceTable->endEditBlock();

    return table;
}

//  from src/gui/text/qtexttable.cpp, line 401, as _ZNK17QTextTablePrivate6updateEv
inline void QTextTablePrivate::update() const
{
    Q_Q(const QTextTable);
    nCols = q->format().columns();
    nRows = (cells.size() + nCols-1)/nCols;
//     qDebug(">>>> QTextTablePrivate::update, nRows=%d, nCols=%d", nRows, nCols);

    grid.assign(nRows * nCols, 0);

    QTextDocumentPrivate *p = pieceTable;
    QTextFormatCollection *c = p->formatCollection();

    cellIndices.resize(cells.size());

    int cell = 0;
    for (int i = 0; i < cells.size(); ++i) {
        int fragment = cells.at(i);
        QTextCharFormat fmt = c->charFormat(QTextDocumentPrivate::FragmentIterator(&p->fragmentMap(), fragment)->format);
        int rowspan = fmt.tableCellRowSpan();
        int colspan = fmt.tableCellColumnSpan();

        // skip taken cells
        while (cell < nRows*nCols && grid[cell])
            ++cell;

        int r = cell/nCols;
        int c = cell%nCols;
        cellIndices[i] = cell;

        if (r + rowspan > nRows) {
            grid.resize((r + rowspan) * nCols, 0);
            nRows = r + rowspan;
        }

        Q_ASSERT(c + colspan <= nCols);
        for (int ii = 0; ii < rowspan; ++ii) {
            for (int jj = 0; jj < colspan; ++jj) {
                Q_ASSERT(grid[(r+ii)*nCols + c+jj] == 0);
                grid[(r+ii)*nCols + c+jj] = fragment;
//              qDebug("    setting cell %d span=%d/%d at %d/%d", fragment, rowspan, colspan, r+ii, c+jj);
            }
        }
    }
//     qDebug("<<<< end: nRows=%d, nCols=%d", nRows, nCols);

    dirty = false;
}
//  -----------------------------------------------------------------------

//  A QTextTablePrivate that Python can take functions over in. Every QTextTablePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTextTablePrivateCall0)(const void *, const QChar *, uint, int *);
typedef void (*CuteQTextTablePrivateCall1)(const void *, const QChar *, uint, int *);
class CuteQTextTablePrivate : public QTextTablePrivate {
public:
  using QTextTablePrivate::QTextTablePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QTextFramePrivate13fragmentAddedE5QCharj")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QTextFramePrivate15fragmentRemovedE5QCharj")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QTextTablePrivate::fragmentAdded(QChar type, uint fragment)
  void fragmentAdded(QChar type, uint fragment) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextTablePrivateCall0 call = reinterpret_cast<CuteQTextTablePrivateCall0>(taken[0]);
      call(this, &type, fragment, &handled);
      if (handled) return;
    }
    QTextTablePrivate::fragmentAdded(type, fragment);
  }

  //  void QTextTablePrivate::fragmentRemoved(QChar type, uint fragment)
  void fragmentRemoved(QChar type, uint fragment) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextTablePrivateCall1 call = reinterpret_cast<CuteQTextTablePrivateCall1>(taken[1]);
      call(this, &type, fragment, &handled);
      if (handled) return;
    }
    QTextTablePrivate::fragmentRemoved(type, fragment);
  }
};

//  QTextTable *QTextTablePrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZN17QTextTablePrivate6q_funcEv(QTextTablePrivate *self) {
  return self->q_func();
}

//  const QTextTable *QTextTablePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextTable *ritual_ZNK17QTextTablePrivate6q_funcEv(
    const QTextTablePrivate *self) {
  return self->q_func();
}

//  QTextTable *QTextTablePrivate::createTable(QTextDocumentPrivate *a0, int
//      pos, int rows, int cols, const QTextTableFormat &tableFormat)
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZN17QTextTablePrivate11createTableEP20QTextDocumentPrivateiiiRK16QTextTableFormat(
    QTextDocumentPrivate *a0,
    int pos,
    int rows,
    int cols,
    const QTextTableFormat *tableFormat) {
  return QTextTablePrivate::createTable(a0, pos, rows, cols, *tableFormat);
}

//  void QTextTablePrivate::fragmentAdded(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextTablePrivate13fragmentAddedE5QCharj(
    QTextTablePrivate *self,
    const QChar *type,
    uint fragment) {
  self->fragmentAdded(*type, fragment);
}

//  void QTextTablePrivate::fragmentRemoved(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextTablePrivate15fragmentRemovedE5QCharj(
    QTextTablePrivate *self,
    const QChar *type,
    uint fragment) {
  self->fragmentRemoved(*type, fragment);
}

//  void QTextTablePrivate::update() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QTextTablePrivate6updateEv(const QTextTablePrivate *self) {
  self->update();
}

//  a Python function taken by a CuteQTextTablePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextTablePrivate(
    QTextTablePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextTablePrivate *>(self)->take(key, call);
}

//  void QTextTablePrivate::fragmentRemoved(QChar type, uint fragment)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTextTablePrivate15fragmentRemovedE5QCharj(
    QTextTablePrivate *self,
    const QChar *type,
    uint fragment) {
  self->QTextTablePrivate::fragmentRemoved(*type, fragment);
}
