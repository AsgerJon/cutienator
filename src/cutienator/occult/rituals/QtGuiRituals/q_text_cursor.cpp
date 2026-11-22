//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextcursor.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextdocumentfragment.h>
#include <QtGui/qimage.h>

//  QTextCursor::QTextCursor()
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZN11QTextCursorC1Ev() {
  return new QTextCursor();
}

//  QTextCursor::QTextCursor(QTextDocument *document)
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZN11QTextCursorC1EP13QTextDocument(
    QTextDocument *document) {
  return new QTextCursor(document);
}

//  QTextCursor::QTextCursor(QTextFrame *frame)
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZN11QTextCursorC1EP10QTextFrame(QTextFrame *frame) {
  return new QTextCursor(frame);
}

//  QTextCursor::QTextCursor(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZN11QTextCursorC1ERK10QTextBlock(
    const QTextBlock *block) {
  return new QTextCursor(*block);
}

//  QTextCursor::QTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZN11QTextCursorC1ERKS_(const QTextCursor *cursor) {
  return new QTextCursor(*cursor);
}

//  QTextCursor::~QTextCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursorD1Ev(QTextCursor *self) {
  delete self;
}

//  bool QTextCursor::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor6isNullEv(const QTextCursor *self) {
  return self->isNull();
}

//  void QTextCursor::setPosition(int pos, MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11setPositionEiNS_8MoveModeE(
    QTextCursor *self,
    int pos,
    QTextCursor::MoveMode mode) {
  self->setPosition(pos, mode);
}

//  int QTextCursor::position() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor8positionEv(const QTextCursor *self) {
  return self->position();
}

//  int QTextCursor::positionInBlock() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor15positionInBlockEv(const QTextCursor *self) {
  return self->positionInBlock();
}

//  int QTextCursor::anchor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor6anchorEv(const QTextCursor *self) {
  return self->anchor();
}

//  void QTextCursor::insertText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor10insertTextERK7QString(
    QTextCursor *self,
    const QString *text) {
  self->insertText(*text);
}

//  void QTextCursor::insertText(const QString &text, const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor10insertTextERK7QStringRK15QTextCharFormat(
    QTextCursor *self,
    const QString *text,
    const QTextCharFormat *format) {
  self->insertText(*text, *format);
}

//  bool QTextCursor::movePosition(MoveOperation op, MoveMode a1, int n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTextCursor12movePositionENS_13MoveOperationENS_8MoveModeEi(
    QTextCursor *self,
    QTextCursor::MoveOperation op,
    QTextCursor::MoveMode a1,
    int n) {
  return self->movePosition(op, a1, n);
}

//  bool QTextCursor::visualNavigation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor16visualNavigationEv(const QTextCursor *self) {
  return self->visualNavigation();
}

//  void QTextCursor::setVisualNavigation(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor19setVisualNavigationEb(
    QTextCursor *self,
    bool b) {
  self->setVisualNavigation(b);
}

//  void QTextCursor::setVerticalMovementX(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor20setVerticalMovementXEi(
    QTextCursor *self,
    int x) {
  self->setVerticalMovementX(x);
}

//  int QTextCursor::verticalMovementX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor17verticalMovementXEv(const QTextCursor *self) {
  return self->verticalMovementX();
}

//  void QTextCursor::setKeepPositionOnInsert(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor23setKeepPositionOnInsertEb(
    QTextCursor *self,
    bool b) {
  self->setKeepPositionOnInsert(b);
}

//  bool QTextCursor::keepPositionOnInsert() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor20keepPositionOnInsertEv(
    const QTextCursor *self) {
  return self->keepPositionOnInsert();
}

//  void QTextCursor::deleteChar()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor10deleteCharEv(QTextCursor *self) {
  self->deleteChar();
}

//  void QTextCursor::deletePreviousChar()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor18deletePreviousCharEv(QTextCursor *self) {
  self->deletePreviousChar();
}

//  void QTextCursor::select(SelectionType selection)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor6selectENS_13SelectionTypeE(
    QTextCursor *self,
    QTextCursor::SelectionType selection) {
  self->select(selection);
}

//  bool QTextCursor::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor12hasSelectionEv(const QTextCursor *self) {
  return self->hasSelection();
}

//  bool QTextCursor::hasComplexSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor19hasComplexSelectionEv(
    const QTextCursor *self) {
  return self->hasComplexSelection();
}

//  void QTextCursor::removeSelectedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor18removeSelectedTextEv(QTextCursor *self) {
  self->removeSelectedText();
}

//  void QTextCursor::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor14clearSelectionEv(QTextCursor *self) {
  self->clearSelection();
}

//  int QTextCursor::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor14selectionStartEv(const QTextCursor *self) {
  return self->selectionStart();
}

//  int QTextCursor::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor12selectionEndEv(const QTextCursor *self) {
  return self->selectionEnd();
}

//  QString QTextCursor::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTextCursor12selectedTextEv(const QTextCursor *self) {
  return new QString(self->selectedText());
}

//  QTextDocumentFragment QTextCursor::selection() const
extern "C" Q_DECL_EXPORT
QTextDocumentFragment *ritual_ZNK11QTextCursor9selectionEv(
    const QTextCursor *self) {
  return new QTextDocumentFragment(self->selection());
}

//  void QTextCursor::selectedTableCells(int *firstRow, int *numRows, int
//      *firstColumn, int *numColumns) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QTextCursor18selectedTableCellsEPiS0_S0_S0_(
    const QTextCursor *self,
    int *firstRow,
    int *numRows,
    int *firstColumn,
    int *numColumns) {
  self->selectedTableCells(firstRow, numRows, firstColumn, numColumns);
}

//  QTextBlock QTextCursor::block() const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK11QTextCursor5blockEv(const QTextCursor *self) {
  return new QTextBlock(self->block());
}

//  QTextCharFormat QTextCursor::charFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK11QTextCursor10charFormatEv(
    const QTextCursor *self) {
  return new QTextCharFormat(self->charFormat());
}

//  void QTextCursor::setCharFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor13setCharFormatERK15QTextCharFormat(
    QTextCursor *self,
    const QTextCharFormat *format) {
  self->setCharFormat(*format);
}

//  void QTextCursor::mergeCharFormat(const QTextCharFormat &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor15mergeCharFormatERK15QTextCharFormat(
    QTextCursor *self,
    const QTextCharFormat *modifier) {
  self->mergeCharFormat(*modifier);
}

//  QTextBlockFormat QTextCursor::blockFormat() const
extern "C" Q_DECL_EXPORT
QTextBlockFormat *ritual_ZNK11QTextCursor11blockFormatEv(
    const QTextCursor *self) {
  return new QTextBlockFormat(self->blockFormat());
}

//  void QTextCursor::setBlockFormat(const QTextBlockFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor14setBlockFormatERK16QTextBlockFormat(
    QTextCursor *self,
    const QTextBlockFormat *format) {
  self->setBlockFormat(*format);
}

//  void QTextCursor::mergeBlockFormat(const QTextBlockFormat &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor16mergeBlockFormatERK16QTextBlockFormat(
    QTextCursor *self,
    const QTextBlockFormat *modifier) {
  self->mergeBlockFormat(*modifier);
}

//  QTextCharFormat QTextCursor::blockCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK11QTextCursor15blockCharFormatEv(
    const QTextCursor *self) {
  return new QTextCharFormat(self->blockCharFormat());
}

//  void QTextCursor::setBlockCharFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor18setBlockCharFormatERK15QTextCharFormat(
    QTextCursor *self,
    const QTextCharFormat *format) {
  self->setBlockCharFormat(*format);
}

//  void QTextCursor::mergeBlockCharFormat(const QTextCharFormat &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor20mergeBlockCharFormatERK15QTextCharFormat(
    QTextCursor *self,
    const QTextCharFormat *modifier) {
  self->mergeBlockCharFormat(*modifier);
}

//  bool QTextCursor::atBlockStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor12atBlockStartEv(const QTextCursor *self) {
  return self->atBlockStart();
}

//  bool QTextCursor::atBlockEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor10atBlockEndEv(const QTextCursor *self) {
  return self->atBlockEnd();
}

//  bool QTextCursor::atStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor7atStartEv(const QTextCursor *self) {
  return self->atStart();
}

//  bool QTextCursor::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor5atEndEv(const QTextCursor *self) {
  return self->atEnd();
}

//  void QTextCursor::insertBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertBlockEv(QTextCursor *self) {
  self->insertBlock();
}

//  void QTextCursor::insertBlock(const QTextBlockFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertBlockERK16QTextBlockFormat(
    QTextCursor *self,
    const QTextBlockFormat *format) {
  self->insertBlock(*format);
}

//  void QTextCursor::insertBlock(const QTextBlockFormat &format, const
//      QTextCharFormat &charFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertBlockERK16QTextBlockFormatRK15QTextCharFormat(
    QTextCursor *self,
    const QTextBlockFormat *format,
    const QTextCharFormat *charFormat) {
  self->insertBlock(*format, *charFormat);
}

//  QTextList *QTextCursor::insertList(const QTextListFormat &format)
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZN11QTextCursor10insertListERK15QTextListFormat(
    QTextCursor *self,
    const QTextListFormat *format) {
  return self->insertList(*format);
}

//  QTextList *QTextCursor::insertList(QTextListFormat::Style style)
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZN11QTextCursor10insertListEN15QTextListFormat5StyleE(
    QTextCursor *self,
    QTextListFormat::Style style) {
  return self->insertList(style);
}

//  QTextList *QTextCursor::createList(const QTextListFormat &format)
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZN11QTextCursor10createListERK15QTextListFormat(
    QTextCursor *self,
    const QTextListFormat *format) {
  return self->createList(*format);
}

//  QTextList *QTextCursor::createList(QTextListFormat::Style style)
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZN11QTextCursor10createListEN15QTextListFormat5StyleE(
    QTextCursor *self,
    QTextListFormat::Style style) {
  return self->createList(style);
}

//  QTextList *QTextCursor::currentList() const
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZNK11QTextCursor11currentListEv(const QTextCursor *self) {
  return self->currentList();
}

//  QTextTable *QTextCursor::insertTable(int rows, int cols, const
//      QTextTableFormat &format)
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZN11QTextCursor11insertTableEiiRK16QTextTableFormat(
    QTextCursor *self,
    int rows,
    int cols,
    const QTextTableFormat *format) {
  return self->insertTable(rows, cols, *format);
}

//  QTextTable *QTextCursor::insertTable(int rows, int cols)
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZN11QTextCursor11insertTableEii(
    QTextCursor *self,
    int rows,
    int cols) {
  return self->insertTable(rows, cols);
}

//  QTextTable *QTextCursor::currentTable() const
extern "C" Q_DECL_EXPORT
QTextTable *ritual_ZNK11QTextCursor12currentTableEv(
    const QTextCursor *self) {
  return self->currentTable();
}

//  QTextFrame *QTextCursor::insertFrame(const QTextFrameFormat &format)
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZN11QTextCursor11insertFrameERK16QTextFrameFormat(
    QTextCursor *self,
    const QTextFrameFormat *format) {
  return self->insertFrame(*format);
}

//  QTextFrame *QTextCursor::currentFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK11QTextCursor12currentFrameEv(
    const QTextCursor *self) {
  return self->currentFrame();
}

//  void QTextCursor::insertFragment(const QTextDocumentFragment &fragment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor14insertFragmentERK21QTextDocumentFragment(
    QTextCursor *self,
    const QTextDocumentFragment *fragment) {
  self->insertFragment(*fragment);
}

//  void QTextCursor::insertHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor10insertHtmlERK7QString(
    QTextCursor *self,
    const QString *html) {
  self->insertHtml(*html);
}

//  void QTextCursor::insertMarkdown(const QString &markdown,
//      QTextDocument::MarkdownFeatures features)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor14insertMarkdownERK7QString6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    QTextCursor *self,
    const QString *markdown,
    int features) {
  self->insertMarkdown(
      *markdown,
      QFlags<QTextDocument::MarkdownFeature>::fromInt(features));
}

//  void QTextCursor::insertImage(const QTextImageFormat &format,
//      QTextFrameFormat::Position alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertImageERK16QTextImageFormatN16QTextFrameFormat8PositionE(
    QTextCursor *self,
    const QTextImageFormat *format,
    QTextFrameFormat::Position alignment) {
  self->insertImage(*format, alignment);
}

//  void QTextCursor::insertImage(const QTextImageFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertImageERK16QTextImageFormat(
    QTextCursor *self,
    const QTextImageFormat *format) {
  self->insertImage(*format);
}

//  void QTextCursor::insertImage(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertImageERK7QString(
    QTextCursor *self,
    const QString *name) {
  self->insertImage(*name);
}

//  void QTextCursor::insertImage(const QImage &image, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor11insertImageERK6QImageRK7QString(
    QTextCursor *self,
    const QImage *image,
    const QString *name) {
  self->insertImage(*image, *name);
}

//  void QTextCursor::beginEditBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor14beginEditBlockEv(QTextCursor *self) {
  self->beginEditBlock();
}

//  void QTextCursor::joinPreviousEditBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor21joinPreviousEditBlockEv(QTextCursor *self) {
  self->joinPreviousEditBlock();
}

//  void QTextCursor::endEditBlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTextCursor12endEditBlockEv(QTextCursor *self) {
  self->endEditBlock();
}

//  bool QTextCursor::operator!=(const QTextCursor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursorneERKS_(
    const QTextCursor *self,
    const QTextCursor *rhs) {
  return self->operator!=(*rhs);
}

//  bool QTextCursor::operator<(const QTextCursor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursorltERKS_(
    const QTextCursor *self,
    const QTextCursor *rhs) {
  return self->operator<(*rhs);
}

//  bool QTextCursor::operator<=(const QTextCursor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursorleERKS_(
    const QTextCursor *self,
    const QTextCursor *rhs) {
  return self->operator<=(*rhs);
}

//  bool QTextCursor::operator==(const QTextCursor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursoreqERKS_(
    const QTextCursor *self,
    const QTextCursor *rhs) {
  return self->operator==(*rhs);
}

//  bool QTextCursor::operator>=(const QTextCursor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursorgeERKS_(
    const QTextCursor *self,
    const QTextCursor *rhs) {
  return self->operator>=(*rhs);
}

//  bool QTextCursor::operator>(const QTextCursor &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursorgtERKS_(
    const QTextCursor *self,
    const QTextCursor *rhs) {
  return self->operator>(*rhs);
}

//  bool QTextCursor::isCopyOf(const QTextCursor &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTextCursor8isCopyOfERKS_(
    const QTextCursor *self,
    const QTextCursor *other) {
  return self->isCopyOf(*other);
}

//  int QTextCursor::blockNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor11blockNumberEv(const QTextCursor *self) {
  return self->blockNumber();
}

//  int QTextCursor::columnNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTextCursor12columnNumberEv(const QTextCursor *self) {
  return self->columnNumber();
}

//  QTextDocument *QTextCursor::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK11QTextCursor8documentEv(const QTextCursor *self) {
  return self->document();
}
