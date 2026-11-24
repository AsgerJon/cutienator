//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextcursor_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextcursor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextcursor.h>

//  QTextCursorPrivate::QTextCursorPrivate(QTextDocumentPrivate *p)
extern "C" Q_DECL_EXPORT
QTextCursorPrivate *ritual_ZN18QTextCursorPrivateC1EP20QTextDocumentPrivate(
    QTextDocumentPrivate *p) {
  return new QTextCursorPrivate(p);
}

//  QTextCursorPrivate::QTextCursorPrivate(const QTextCursorPrivate &rhs)
extern "C" Q_DECL_EXPORT
QTextCursorPrivate *ritual_ZN18QTextCursorPrivateC1ERKS_(
    const QTextCursorPrivate *rhs) {
  return new QTextCursorPrivate(*rhs);
}

//  QTextCursorPrivate::~QTextCursorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivateD1Ev(QTextCursorPrivate *self) {
  delete self;
}

//  QTextCursorPrivate *QTextCursorPrivate::getPrivate(QTextCursor *c)
extern "C" Q_DECL_EXPORT
QTextCursorPrivate *ritual_ZN18QTextCursorPrivate10getPrivateEP11QTextCursor(
    QTextCursor *c) {
  return QTextCursorPrivate::getPrivate(c);
}

//  AdjustResult QTextCursorPrivate::adjustPosition(int positionOfChange, int
//      charsAddedOrRemoved, QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
QTextCursorPrivate::AdjustResult ritual_ZN18QTextCursorPrivate14adjustPositionEiiN16QTextUndoCommand9OperationE(
    QTextCursorPrivate *self,
    int positionOfChange,
    int charsAddedOrRemoved,
    QTextUndoCommand::Operation op) {
  return self->adjustPosition(positionOfChange, charsAddedOrRemoved, op);
}

//  void QTextCursorPrivate::adjustCursor(QTextCursor::MoveOperation m)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate12adjustCursorEN11QTextCursor13MoveOperationE(
    QTextCursorPrivate *self,
    QTextCursor::MoveOperation m) {
  self->adjustCursor(m);
}

//  void QTextCursorPrivate::remove()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate6removeEv(QTextCursorPrivate *self) {
  self->remove();
}

//  void QTextCursorPrivate::clearCells(QTextTable *table, int startRow, int
//      startCol, int numRows, int numCols, QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate10clearCellsEP10QTextTableiiiiN16QTextUndoCommand9OperationE(
    QTextCursorPrivate *self,
    QTextTable *table,
    int startRow,
    int startCol,
    int numRows,
    int numCols,
    QTextUndoCommand::Operation op) {
  self->clearCells(table, startRow, startCol, numRows, numCols, op);
}

//  bool QTextCursorPrivate::setPosition(int newPosition)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextCursorPrivate11setPositionEi(
    QTextCursorPrivate *self,
    int newPosition) {
  return self->setPosition(newPosition);
}

//  void QTextCursorPrivate::setX()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate4setXEv(QTextCursorPrivate *self) {
  self->setX();
}

//  bool QTextCursorPrivate::canDelete(int pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QTextCursorPrivate9canDeleteEi(
    const QTextCursorPrivate *self,
    int pos) {
  return self->canDelete(pos);
}

//  void QTextCursorPrivate::insertBlock(const QTextBlockFormat &format,
//      const QTextCharFormat &charFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate11insertBlockERK16QTextBlockFormatRK15QTextCharFormat(
    QTextCursorPrivate *self,
    const QTextBlockFormat *format,
    const QTextCharFormat *charFormat) {
  self->insertBlock(*format, *charFormat);
}

//  bool QTextCursorPrivate::movePosition(QTextCursor::MoveOperation op,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QTextCursorPrivate12movePositionEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QTextCursorPrivate *self,
    QTextCursor::MoveOperation op,
    QTextCursor::MoveMode mode) {
  return self->movePosition(op, mode);
}

//  QTextBlock QTextCursorPrivate::block() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK18QTextCursorPrivate5blockEv(
    const QTextCursorPrivate *self) {
  return new QTextBlock(self->block());
}

//  QTextBlockFormat QTextCursorPrivate::blockFormat() const
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZNK18QTextCursorPrivate11blockFormatEv(
    const QTextCursorPrivate *self) {
  return new QTextBlockFormat(self->blockFormat());
}

//  QTextTable *QTextCursorPrivate::complexSelectionTable() const
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZNK18QTextCursorPrivate21complexSelectionTableEv(
    const QTextCursorPrivate *self) {
  return self->complexSelectionTable();
}

//  void QTextCursorPrivate::selectedTableCells(int *firstRow, int *numRows,
//      int *firstColumn, int *numColumns) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QTextCursorPrivate18selectedTableCellsEPiS0_S0_S0_(
    const QTextCursorPrivate *self,
    int *firstRow,
    int *numRows,
    int *firstColumn,
    int *numColumns) {
  self->selectedTableCells(firstRow, numRows, firstColumn, numColumns);
}

//  void QTextCursorPrivate::setBlockCharFormat(const QTextCharFormat
//      &format, QTextDocumentPrivate::FormatChangeMode changeMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate18setBlockCharFormatERK15QTextCharFormatN20QTextDocumentPrivate16FormatChangeModeE(
    QTextCursorPrivate *self,
    const QTextCharFormat *format,
    QTextDocumentPrivate::FormatChangeMode changeMode) {
  self->setBlockCharFormat(*format, changeMode);
}

//  void QTextCursorPrivate::setBlockFormat(const QTextBlockFormat &format,
//      QTextDocumentPrivate::FormatChangeMode changeMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate14setBlockFormatERK16QTextBlockFormatN20QTextDocumentPrivate16FormatChangeModeE(
    QTextCursorPrivate *self,
    const QTextBlockFormat *format,
    QTextDocumentPrivate::FormatChangeMode changeMode) {
  self->setBlockFormat(*format, changeMode);
}

//  void QTextCursorPrivate::setCharFormat(const QTextCharFormat &format,
//      QTextDocumentPrivate::FormatChangeMode changeMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate13setCharFormatERK15QTextCharFormatN20QTextDocumentPrivate16FormatChangeModeE(
    QTextCursorPrivate *self,
    const QTextCharFormat *format,
    QTextDocumentPrivate::FormatChangeMode changeMode) {
  self->setCharFormat(*format, changeMode);
}

//  void QTextCursorPrivate::aboutToRemoveCell(int from, int to)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTextCursorPrivate17aboutToRemoveCellEii(
    QTextCursorPrivate *self,
    int from,
    int to) {
  self->aboutToRemoveCell(from, to);
}

//  QTextCursor QTextCursorPrivate::fromPosition(QTextDocumentPrivate *d, int
//      pos)
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZN18QTextCursorPrivate12fromPositionEP20QTextDocumentPrivatei(
    QTextDocumentPrivate *d,
    int pos) {
  return new QTextCursor(QTextCursorPrivate::fromPosition(d, pos));
}
