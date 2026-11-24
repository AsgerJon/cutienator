//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qchar.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qfont.h>

//  QTextDocument *QTextDocumentPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZN20QTextDocumentPrivate6q_funcEv(
    QTextDocumentPrivate *self) {
  return self->q_func();
}

//  const QTextDocument *QTextDocumentPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTextDocument *ritual_ZNK20QTextDocumentPrivate6q_funcEv(
    const QTextDocumentPrivate *self) {
  return self->q_func();
}

//  QTextDocumentPrivate::QTextDocumentPrivate()
extern "C" Q_DECL_EXPORT
QTextDocumentPrivate *ritual_ZN20QTextDocumentPrivateC1Ev() {
  return new QTextDocumentPrivate();
}

//  QTextDocumentPrivate::~QTextDocumentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivateD1Ev(QTextDocumentPrivate *self) {
  delete self;
}

//  void QTextDocumentPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate4initEv(QTextDocumentPrivate *self) {
  self->init();
}

//  void QTextDocumentPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate5clearEv(QTextDocumentPrivate *self) {
  self->clear();
}

//  void QTextDocumentPrivate::setLayout(QAbstractTextDocumentLayout *layout)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate9setLayoutEP27QAbstractTextDocumentLayout(
    QTextDocumentPrivate *self,
    QAbstractTextDocumentLayout *layout) {
  self->setLayout(layout);
}

//  void QTextDocumentPrivate::insert(int pos, QStringView text, int format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate6insertEi11QStringViewi(
    QTextDocumentPrivate *self,
    int pos,
    const QString *text,
    int format) {
  self->insert(pos, QStringView(*text), format);
}

//  void QTextDocumentPrivate::insert(int pos, QChar c, int format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate6insertEi5QChari(
    QTextDocumentPrivate *self,
    int pos,
    const QChar *c,
    int format) {
  self->insert(pos, *c, format);
}

//  void QTextDocumentPrivate::insert(int pos, int strPos, int strLength, int
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate6insertEiiii(
    QTextDocumentPrivate *self,
    int pos,
    int strPos,
    int strLength,
    int format) {
  self->insert(pos, strPos, strLength, format);
}

//  int QTextDocumentPrivate::insertBlock(int pos, int blockFormat, int
//      charFormat, QTextUndoCommand::Operation a3)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTextDocumentPrivate11insertBlockEiiiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int pos,
    int blockFormat,
    int charFormat,
    QTextUndoCommand::Operation a3) {
  return self->insertBlock(pos, blockFormat, charFormat, a3);
}

//  int QTextDocumentPrivate::insertBlock(QChar blockSeparator, int pos, int
//      blockFormat, int charFormat, QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTextDocumentPrivate11insertBlockE5QChariiiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    const QChar *blockSeparator,
    int pos,
    int blockFormat,
    int charFormat,
    QTextUndoCommand::Operation op) {
  return self->insertBlock(
      *blockSeparator,
      pos,
      blockFormat,
      charFormat,
      op);
}

//  void QTextDocumentPrivate::move(int from, int to, int length,
//      QTextUndoCommand::Operation a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate4moveEiiiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int from,
    int to,
    int length,
    QTextUndoCommand::Operation a3) {
  self->move(from, to, length, a3);
}

//  void QTextDocumentPrivate::remove(int pos, int length,
//      QTextUndoCommand::Operation a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate6removeEiiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int pos,
    int length,
    QTextUndoCommand::Operation a2) {
  self->remove(pos, length, a2);
}

//  void QTextDocumentPrivate::aboutToRemoveCell(int cursorFrom, int
//      cursorEnd)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate17aboutToRemoveCellEii(
    QTextDocumentPrivate *self,
    int cursorFrom,
    int cursorEnd) {
  self->aboutToRemoveCell(cursorFrom, cursorEnd);
}

//  QTextFrame *QTextDocumentPrivate::insertFrame(int start, int end, const
//      QTextFrameFormat &format)
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZN20QTextDocumentPrivate11insertFrameEiiRK16QTextFrameFormat(
    QTextDocumentPrivate *self,
    int start,
    int end,
    const QTextFrameFormat *format) {
  return self->insertFrame(start, end, *format);
}

//  void QTextDocumentPrivate::removeFrame(QTextFrame *frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate11removeFrameEP10QTextFrame(
    QTextDocumentPrivate *self,
    QTextFrame *frame) {
  self->removeFrame(frame);
}

//  void QTextDocumentPrivate::setCharFormat(int pos, int length, const
//      QTextCharFormat &newFormat, FormatChangeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate13setCharFormatEiiRK15QTextCharFormatNS_16FormatChangeModeE(
    QTextDocumentPrivate *self,
    int pos,
    int length,
    const QTextCharFormat *newFormat,
    QTextDocumentPrivate::FormatChangeMode mode) {
  self->setCharFormat(pos, length, *newFormat, mode);
}

//  void QTextDocumentPrivate::setBlockFormat(const QTextBlock &from, const
//      QTextBlock &to, const QTextBlockFormat &newFormat, FormatChangeMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14setBlockFormatERK10QTextBlockS2_RK16QTextBlockFormatNS_16FormatChangeModeE(
    QTextDocumentPrivate *self,
    const QTextBlock *from,
    const QTextBlock *to,
    const QTextBlockFormat *newFormat,
    QTextDocumentPrivate::FormatChangeMode mode) {
  self->setBlockFormat(*from, *to, *newFormat, mode);
}

//  void QTextDocumentPrivate::emitUndoAvailable(bool available)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate17emitUndoAvailableEb(
    QTextDocumentPrivate *self,
    bool available) {
  self->emitUndoAvailable(available);
}

//  void QTextDocumentPrivate::emitRedoAvailable(bool available)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate17emitRedoAvailableEb(
    QTextDocumentPrivate *self,
    bool available) {
  self->emitRedoAvailable(available);
}

//  int QTextDocumentPrivate::undoRedo(bool undo)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTextDocumentPrivate8undoRedoEb(
    QTextDocumentPrivate *self,
    bool undo) {
  return self->undoRedo(undo);
}

//  void QTextDocumentPrivate::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate4undoEv(QTextDocumentPrivate *self) {
  self->undo();
}

//  void QTextDocumentPrivate::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate4redoEv(QTextDocumentPrivate *self) {
  self->redo();
}

//  void QTextDocumentPrivate::appendUndoItem(QAbstractUndoItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14appendUndoItemEP17QAbstractUndoItem(
    QTextDocumentPrivate *self,
    QAbstractUndoItem *a0) {
  self->appendUndoItem(a0);
}

//  void QTextDocumentPrivate::beginEditBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14beginEditBlockEv(
    QTextDocumentPrivate *self) {
  self->beginEditBlock();
}

//  void QTextDocumentPrivate::joinPreviousEditBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate21joinPreviousEditBlockEv(
    QTextDocumentPrivate *self) {
  self->joinPreviousEditBlock();
}

//  void QTextDocumentPrivate::endEditBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate12endEditBlockEv(
    QTextDocumentPrivate *self) {
  self->endEditBlock();
}

//  void QTextDocumentPrivate::finishEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate10finishEditEv(
    QTextDocumentPrivate *self) {
  self->finishEdit();
}

//  bool QTextDocumentPrivate::isInEditBlock() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextDocumentPrivate13isInEditBlockEv(
    const QTextDocumentPrivate *self) {
  return self->isInEditBlock();
}

//  void QTextDocumentPrivate::enableUndoRedo(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14enableUndoRedoEb(
    QTextDocumentPrivate *self,
    bool enable) {
  self->enableUndoRedo(enable);
}

//  bool QTextDocumentPrivate::isUndoRedoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextDocumentPrivate17isUndoRedoEnabledEv(
    const QTextDocumentPrivate *self) {
  return self->isUndoRedoEnabled();
}

//  bool QTextDocumentPrivate::isUndoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextDocumentPrivate15isUndoAvailableEv(
    const QTextDocumentPrivate *self) {
  return self->isUndoAvailable();
}

//  bool QTextDocumentPrivate::isRedoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextDocumentPrivate15isRedoAvailableEv(
    const QTextDocumentPrivate *self) {
  return self->isRedoAvailable();
}

//  int QTextDocumentPrivate::availableUndoSteps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate18availableUndoStepsEv(
    const QTextDocumentPrivate *self) {
  return self->availableUndoSteps();
}

//  int QTextDocumentPrivate::availableRedoSteps() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate18availableRedoStepsEv(
    const QTextDocumentPrivate *self) {
  return self->availableRedoSteps();
}

//  QString QTextDocumentPrivate::buffer() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QTextDocumentPrivate6bufferEv(
    const QTextDocumentPrivate *self) {
  return new QString(self->buffer());
}

//  QString QTextDocumentPrivate::plainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QTextDocumentPrivate9plainTextEv(
    const QTextDocumentPrivate *self) {
  return new QString(self->plainText());
}

//  int QTextDocumentPrivate::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate6lengthEv(
    const QTextDocumentPrivate *self) {
  return self->length();
}

//  QTextFormatCollection *QTextDocumentPrivate::formatCollection()
extern "C" Q_DECL_EXPORT
QTextFormatCollection *ritual_ZN20QTextDocumentPrivate16formatCollectionEv(
    QTextDocumentPrivate *self) {
  return self->formatCollection();
}

//  const QTextFormatCollection *QTextDocumentPrivate::formatCollection()
//      const
extern "C" Q_DECL_EXPORT
const QTextFormatCollection *ritual_ZNK20QTextDocumentPrivate16formatCollectionEv(
    const QTextDocumentPrivate *self) {
  return self->formatCollection();
}

//  QAbstractTextDocumentLayout *QTextDocumentPrivate::layout() const
extern "C" Q_DECL_EXPORT
QAbstractTextDocumentLayout *ritual_ZNK20QTextDocumentPrivate6layoutEv(
    const QTextDocumentPrivate *self) {
  return self->layout();
}

//  QTextBlock QTextDocumentPrivate::blocksBegin() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK20QTextDocumentPrivate11blocksBeginEv(
    const QTextDocumentPrivate *self) {
  return new QTextBlock(self->blocksBegin());
}

//  QTextBlock QTextDocumentPrivate::blocksEnd() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK20QTextDocumentPrivate9blocksEndEv(
    const QTextDocumentPrivate *self) {
  return new QTextBlock(self->blocksEnd());
}

//  QTextBlock QTextDocumentPrivate::blocksFind(int pos) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK20QTextDocumentPrivate10blocksFindEi(
    const QTextDocumentPrivate *self,
    int pos) {
  return new QTextBlock(self->blocksFind(pos));
}

//  int QTextDocumentPrivate::blockCharFormatIndex(int node) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate20blockCharFormatIndexEi(
    const QTextDocumentPrivate *self,
    int node) {
  return self->blockCharFormatIndex(node);
}

//  int QTextDocumentPrivate::numBlocks() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate9numBlocksEv(
    const QTextDocumentPrivate *self) {
  return self->numBlocks();
}

//  const QTextBlockData *QTextDocumentPrivate::block(const QTextBlock &it)
extern "C" Q_DECL_EXPORT
const QTextBlockData *ritual_ZN20QTextDocumentPrivate5blockERK10QTextBlock(
    const QTextBlock *it) {
  return QTextDocumentPrivate::block(*it);
}

//  int QTextDocumentPrivate::nextCursorPosition(int position,
//      QTextLayout::CursorMode mode) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate18nextCursorPositionEiN11QTextLayout10CursorModeE(
    const QTextDocumentPrivate *self,
    int position,
    QTextLayout::CursorMode mode) {
  return self->nextCursorPosition(position, mode);
}

//  int QTextDocumentPrivate::previousCursorPosition(int position,
//      QTextLayout::CursorMode mode) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate22previousCursorPositionEiN11QTextLayout10CursorModeE(
    const QTextDocumentPrivate *self,
    int position,
    QTextLayout::CursorMode mode) {
  return self->previousCursorPosition(position, mode);
}

//  int QTextDocumentPrivate::leftCursorPosition(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate18leftCursorPositionEi(
    const QTextDocumentPrivate *self,
    int position) {
  return self->leftCursorPosition(position);
}

//  int QTextDocumentPrivate::rightCursorPosition(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTextDocumentPrivate19rightCursorPositionEi(
    const QTextDocumentPrivate *self,
    int position) {
  return self->rightCursorPosition(position);
}

//  void QTextDocumentPrivate::changeObjectFormat(QTextObject *group, int
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate18changeObjectFormatEP11QTextObjecti(
    QTextDocumentPrivate *self,
    QTextObject *group,
    int format) {
  self->changeObjectFormat(group, format);
}

//  void QTextDocumentPrivate::setModified(bool m)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate11setModifiedEb(
    QTextDocumentPrivate *self,
    bool m) {
  self->setModified(m);
}

//  bool QTextDocumentPrivate::isModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextDocumentPrivate10isModifiedEv(
    const QTextDocumentPrivate *self) {
  return self->isModified();
}

//  QFont QTextDocumentPrivate::defaultFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK20QTextDocumentPrivate11defaultFontEv(
    const QTextDocumentPrivate *self) {
  return new QFont(self->defaultFont());
}

//  void QTextDocumentPrivate::setDefaultFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14setDefaultFontERK5QFont(
    QTextDocumentPrivate *self,
    const QFont *f) {
  self->setDefaultFont(*f);
}

//  void QTextDocumentPrivate::clearUndoRedoStacks(QTextDocument::Stacks
//      stacksToClear, bool emitSignals)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate19clearUndoRedoStacksEN13QTextDocument6StacksEb(
    QTextDocumentPrivate *self,
    QTextDocument::Stacks stacksToClear,
    bool emitSignals) {
  self->clearUndoRedoStacks(stacksToClear, emitSignals);
}

//  bool QTextDocumentPrivate::split(int pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTextDocumentPrivate5splitEi(
    QTextDocumentPrivate *self,
    int pos) {
  return self->split(pos);
}

//  bool QTextDocumentPrivate::unite(uint f)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTextDocumentPrivate5uniteEj(
    QTextDocumentPrivate *self,
    uint f) {
  return self->unite(f);
}

//  void QTextDocumentPrivate::insert_string(int pos, uint strPos, uint
//      length, int format, QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate13insert_stringEijjiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int pos,
    uint strPos,
    uint length,
    int format,
    QTextUndoCommand::Operation op) {
  self->insert_string(pos, strPos, length, format, op);
}

//  int QTextDocumentPrivate::insert_block(int pos, uint strPos, int format,
//      int blockformat, QTextUndoCommand::Operation op, int command)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTextDocumentPrivate12insert_blockEijiiN16QTextUndoCommand9OperationEi(
    QTextDocumentPrivate *self,
    int pos,
    uint strPos,
    int format,
    int blockformat,
    QTextUndoCommand::Operation op,
    int command) {
  return self->insert_block(pos, strPos, format, blockformat, op, command);
}

//  int QTextDocumentPrivate::remove_string(int pos, uint length,
//      QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTextDocumentPrivate13remove_stringEijN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int pos,
    uint length,
    QTextUndoCommand::Operation op) {
  return self->remove_string(pos, length, op);
}

//  int QTextDocumentPrivate::remove_block(int pos, int *blockformat, int
//      command, QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QTextDocumentPrivate12remove_blockEiPiiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int pos,
    int *blockformat,
    int command,
    QTextUndoCommand::Operation op) {
  return self->remove_block(pos, blockformat, command, op);
}

//  void QTextDocumentPrivate::insert_frame(QTextFrame *f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate12insert_frameEP10QTextFrame(
    QTextDocumentPrivate *self,
    QTextFrame *f) {
  self->insert_frame(f);
}

//  void QTextDocumentPrivate::scan_frames(int pos, int charsRemoved, int
//      charsAdded)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate11scan_framesEiii(
    QTextDocumentPrivate *self,
    int pos,
    int charsRemoved,
    int charsAdded) {
  self->scan_frames(pos, charsRemoved, charsAdded);
}

//  void QTextDocumentPrivate::clearFrame(QTextFrame *f)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate10clearFrameEP10QTextFrame(
    QTextFrame *f) {
  QTextDocumentPrivate::clearFrame(f);
}

//  void QTextDocumentPrivate::adjustDocumentChangesAndCursors(int from, int
//      addedOrRemoved, QTextUndoCommand::Operation op)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate31adjustDocumentChangesAndCursorsEiiN16QTextUndoCommand9OperationE(
    QTextDocumentPrivate *self,
    int from,
    int addedOrRemoved,
    QTextUndoCommand::Operation op) {
  self->adjustDocumentChangesAndCursors(from, addedOrRemoved, op);
}

//  void QTextDocumentPrivate::documentChange(int from, int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14documentChangeEii(
    QTextDocumentPrivate *self,
    int from,
    int length) {
  self->documentChange(from, length);
}

//  void QTextDocumentPrivate::addCursor(QTextCursorPrivate *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate9addCursorEP18QTextCursorPrivate(
    QTextDocumentPrivate *self,
    QTextCursorPrivate *c) {
  self->addCursor(c);
}

//  void QTextDocumentPrivate::removeCursor(QTextCursorPrivate *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate12removeCursorEP18QTextCursorPrivate(
    QTextDocumentPrivate *self,
    QTextCursorPrivate *c) {
  self->removeCursor(c);
}

//  QTextFrame *QTextDocumentPrivate::frameAt(int pos) const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK20QTextDocumentPrivate7frameAtEi(
    const QTextDocumentPrivate *self,
    int pos) {
  return self->frameAt(pos);
}

//  QTextFrame *QTextDocumentPrivate::rootFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK20QTextDocumentPrivate9rootFrameEv(
    const QTextDocumentPrivate *self) {
  return self->rootFrame();
}

//  QTextObject *QTextDocumentPrivate::objectForIndex(int objectIndex) const
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZNK20QTextDocumentPrivate14objectForIndexEi(
    const QTextDocumentPrivate *self,
    int objectIndex) {
  return self->objectForIndex(objectIndex);
}

//  QTextObject *QTextDocumentPrivate::objectForFormat(int formatIndex) const
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZNK20QTextDocumentPrivate15objectForFormatEi(
    const QTextDocumentPrivate *self,
    int formatIndex) {
  return self->objectForFormat(formatIndex);
}

//  QTextObject *QTextDocumentPrivate::objectForFormat(const QTextFormat &f)
//      const
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZNK20QTextDocumentPrivate15objectForFormatERK11QTextFormat(
    const QTextDocumentPrivate *self,
    const QTextFormat *f) {
  return self->objectForFormat(*f);
}

//  QTextObject *QTextDocumentPrivate::createObject(const QTextFormat
//      &newFormat, int objectIndex)
extern "C" Q_DECL_EXPORT
QTextObject *ritual_ZN20QTextDocumentPrivate12createObjectERK11QTextFormati(
    QTextDocumentPrivate *self,
    const QTextFormat *newFormat,
    int objectIndex) {
  return self->createObject(*newFormat, objectIndex);
}

//  void QTextDocumentPrivate::deleteObject(QTextObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate12deleteObjectEP11QTextObject(
    QTextDocumentPrivate *self,
    QTextObject *object) {
  self->deleteObject(object);
}

//  QTextDocument *QTextDocumentPrivate::document()
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZN20QTextDocumentPrivate8documentEv(
    QTextDocumentPrivate *self) {
  return self->document();
}

//  const QTextDocument *QTextDocumentPrivate::document() const
extern "C" Q_DECL_EXPORT
const QTextDocument *ritual_ZNK20QTextDocumentPrivate8documentEv(
    const QTextDocumentPrivate *self) {
  return self->document();
}

//  bool QTextDocumentPrivate::ensureMaximumBlockCount()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTextDocumentPrivate23ensureMaximumBlockCountEv(
    QTextDocumentPrivate *self) {
  return self->ensureMaximumBlockCount();
}

//  const QTextDocumentPrivate *QTextDocumentPrivate::get(const QTextDocument
//      *document)
extern "C" Q_DECL_EXPORT
const QTextDocumentPrivate *ritual_ZN20QTextDocumentPrivate3getEPK13QTextDocument(
    const QTextDocument *document) {
  return QTextDocumentPrivate::get(document);
}

//  QTextDocumentPrivate *QTextDocumentPrivate::get(QTextDocument *document)
extern "C" Q_DECL_EXPORT
QTextDocumentPrivate *ritual_ZN20QTextDocumentPrivate3getEP13QTextDocument(
    QTextDocument *document) {
  return QTextDocumentPrivate::get(document);
}

//  const QTextDocumentPrivate *QTextDocumentPrivate::get(const QTextBlock
//      &block)
extern "C" Q_DECL_EXPORT
const QTextDocumentPrivate *ritual_ZN20QTextDocumentPrivate3getERK10QTextBlock(
    const QTextBlock *block) {
  return QTextDocumentPrivate::get(*block);
}

//  QTextDocumentPrivate *QTextDocumentPrivate::get(QTextObject *object)
extern "C" Q_DECL_EXPORT
QTextDocumentPrivate *ritual_ZN20QTextDocumentPrivate3getEP11QTextObject(
    QTextObject *object) {
  return QTextDocumentPrivate::get(object);
}

//  const QTextDocumentPrivate *QTextDocumentPrivate::get(const QTextObject
//      *object)
extern "C" Q_DECL_EXPORT
const QTextDocumentPrivate *ritual_ZN20QTextDocumentPrivate3getEPK11QTextObject(
    const QTextObject *object) {
  return QTextDocumentPrivate::get(object);
}

//  bool QTextDocumentPrivate::canLayout() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QTextDocumentPrivate9canLayoutEv(
    const QTextDocumentPrivate *self) {
  return self->canLayout();
}

//  void QTextDocumentPrivate::appendUndoItem(const QTextUndoCommand &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate14appendUndoItemERK16QTextUndoCommand(
    QTextDocumentPrivate *self,
    const QTextUndoCommand *c) {
  self->appendUndoItem(*c);
}

//  void QTextDocumentPrivate::contentsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate15contentsChangedEv(
    QTextDocumentPrivate *self) {
  self->contentsChanged();
}

//  void QTextDocumentPrivate::compressPieceTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate18compressPieceTableEv(
    QTextDocumentPrivate *self) {
  self->compressPieceTable();
}

//  void QTextDocumentPrivate::mergeCachedResources(const
//      QTextDocumentPrivate *priv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTextDocumentPrivate20mergeCachedResourcesEPKS_(
    QTextDocumentPrivate *self,
    const QTextDocumentPrivate *priv) {
  self->mergeCachedResources(priv);
}
