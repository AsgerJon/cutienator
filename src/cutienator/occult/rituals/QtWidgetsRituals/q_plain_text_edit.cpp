//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qplaintextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qplaintextedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QPlainTextEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QPlainTextEdit10metaObjectEv(
    const QPlainTextEdit *self) {
  return self->metaObject();
}

//  QString QPlainTextEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QPlainTextEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlainTextEdit::tr(s, c, n));
}

//  QPlainTextEdit::QPlainTextEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZN14QPlainTextEditC1EP7QWidget(QWidget *parent) {
  return new QPlainTextEdit(parent);
}

//  QPlainTextEdit::QPlainTextEdit(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZN14QPlainTextEditC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new QPlainTextEdit(*text, parent);
}

//  QPlainTextEdit::~QPlainTextEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEditD1Ev(QPlainTextEdit *self) {
  delete self;
}

//  void QPlainTextEdit::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit11setDocumentEP13QTextDocument(
    QPlainTextEdit *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QPlainTextEdit::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK14QPlainTextEdit8documentEv(
    const QPlainTextEdit *self) {
  return self->document();
}

//  void QPlainTextEdit::setPlaceholderText(const QString &placeholderText)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setPlaceholderTextERK7QString(
    QPlainTextEdit *self,
    const QString *placeholderText) {
  self->setPlaceholderText(*placeholderText);
}

//  QString QPlainTextEdit::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit15placeholderTextEv(
    const QPlainTextEdit *self) {
  return new QString(self->placeholderText());
}

//  void QPlainTextEdit::setTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit13setTextCursorERK11QTextCursor(
    QPlainTextEdit *self,
    const QTextCursor *cursor) {
  self->setTextCursor(*cursor);
}

//  QTextCursor QPlainTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK14QPlainTextEdit10textCursorEv(
    const QPlainTextEdit *self) {
  return new QTextCursor(self->textCursor());
}

//  bool QPlainTextEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit10isReadOnlyEv(const QPlainTextEdit *self) {
  return self->isReadOnly();
}

//  void QPlainTextEdit::setReadOnly(bool ro)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit11setReadOnlyEb(
    QPlainTextEdit *self,
    bool ro) {
  self->setReadOnly(ro);
}

//  void QPlainTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags
//      flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QPlainTextEdit *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QPlainTextEdit::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit20textInteractionFlagsEv(
    const QPlainTextEdit *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  void QPlainTextEdit::mergeCurrentCharFormat(const QTextCharFormat
//      &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit22mergeCurrentCharFormatERK15QTextCharFormat(
    QPlainTextEdit *self,
    const QTextCharFormat *modifier) {
  self->mergeCurrentCharFormat(*modifier);
}

//  void QPlainTextEdit::setCurrentCharFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit20setCurrentCharFormatERK15QTextCharFormat(
    QPlainTextEdit *self,
    const QTextCharFormat *format) {
  self->setCurrentCharFormat(*format);
}

//  QTextCharFormat QPlainTextEdit::currentCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK14QPlainTextEdit17currentCharFormatEv(
    const QPlainTextEdit *self) {
  return new QTextCharFormat(self->currentCharFormat());
}

//  bool QPlainTextEdit::tabChangesFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit15tabChangesFocusEv(
    const QPlainTextEdit *self) {
  return self->tabChangesFocus();
}

//  void QPlainTextEdit::setTabChangesFocus(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setTabChangesFocusEb(
    QPlainTextEdit *self,
    bool b) {
  self->setTabChangesFocus(b);
}

//  void QPlainTextEdit::setDocumentTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit16setDocumentTitleERK7QString(
    QPlainTextEdit *self,
    const QString *title) {
  self->setDocumentTitle(*title);
}

//  QString QPlainTextEdit::documentTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit13documentTitleEv(
    const QPlainTextEdit *self) {
  return new QString(self->documentTitle());
}

//  bool QPlainTextEdit::isUndoRedoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit17isUndoRedoEnabledEv(
    const QPlainTextEdit *self) {
  return self->isUndoRedoEnabled();
}

//  void QPlainTextEdit::setUndoRedoEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setUndoRedoEnabledEb(
    QPlainTextEdit *self,
    bool enable) {
  self->setUndoRedoEnabled(enable);
}

//  void QPlainTextEdit::setMaximumBlockCount(int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit20setMaximumBlockCountEi(
    QPlainTextEdit *self,
    int maximum) {
  self->setMaximumBlockCount(maximum);
}

//  int QPlainTextEdit::maximumBlockCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit17maximumBlockCountEv(
    const QPlainTextEdit *self) {
  return self->maximumBlockCount();
}

//  LineWrapMode QPlainTextEdit::lineWrapMode() const
extern "C" Q_DECL_EXPORT
QPlainTextEdit::LineWrapMode ritual_ZNK14QPlainTextEdit12lineWrapModeEv(
    const QPlainTextEdit *self) {
  return self->lineWrapMode();
}

//  void QPlainTextEdit::setLineWrapMode(LineWrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15setLineWrapModeENS_12LineWrapModeE(
    QPlainTextEdit *self,
    QPlainTextEdit::LineWrapMode mode) {
  self->setLineWrapMode(mode);
}

//  QTextOption::WrapMode QPlainTextEdit::wordWrapMode() const
extern "C" Q_DECL_EXPORT
QTextOption::WrapMode ritual_ZNK14QPlainTextEdit12wordWrapModeEv(
    const QPlainTextEdit *self) {
  return self->wordWrapMode();
}

//  void QPlainTextEdit::setWordWrapMode(QTextOption::WrapMode policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15setWordWrapModeEN11QTextOption8WrapModeE(
    QPlainTextEdit *self,
    QTextOption::WrapMode policy) {
  self->setWordWrapMode(policy);
}

//  void QPlainTextEdit::setBackgroundVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit20setBackgroundVisibleEb(
    QPlainTextEdit *self,
    bool visible) {
  self->setBackgroundVisible(visible);
}

//  bool QPlainTextEdit::backgroundVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit17backgroundVisibleEv(
    const QPlainTextEdit *self) {
  return self->backgroundVisible();
}

//  void QPlainTextEdit::setCenterOnScroll(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit17setCenterOnScrollEb(
    QPlainTextEdit *self,
    bool enabled) {
  self->setCenterOnScroll(enabled);
}

//  bool QPlainTextEdit::centerOnScroll() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit14centerOnScrollEv(
    const QPlainTextEdit *self) {
  return self->centerOnScroll();
}

//  bool QPlainTextEdit::find(const QString &exp, QTextDocument::FindFlags
//      options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QPlainTextEdit4findERK7QString6QFlagsIN13QTextDocument8FindFlagEE(
    QPlainTextEdit *self,
    const QString *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

//  bool QPlainTextEdit::find(const QRegularExpression &exp,
//      QTextDocument::FindFlags options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QPlainTextEdit4findERK18QRegularExpression6QFlagsIN13QTextDocument8FindFlagEE(
    QPlainTextEdit *self,
    const QRegularExpression *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

//  QString QPlainTextEdit::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit11toPlainTextEv(
    const QPlainTextEdit *self) {
  return new QString(self->toPlainText());
}

//  void QPlainTextEdit::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit19ensureCursorVisibleEv(QPlainTextEdit *self) {
  self->ensureCursorVisible();
}

//  QVariant QPlainTextEdit::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QPlainTextEdit12loadResourceEiRK4QUrl(
    QPlainTextEdit *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  QMenu *QPlainTextEdit::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN14QPlainTextEdit25createStandardContextMenuEv(
    QPlainTextEdit *self) {
  return self->createStandardContextMenu();
}

//  QMenu *QPlainTextEdit::createStandardContextMenu(const QPoint &position)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN14QPlainTextEdit25createStandardContextMenuERK6QPoint(
    QPlainTextEdit *self,
    const QPoint *position) {
  return self->createStandardContextMenu(*position);
}

//  QTextCursor QPlainTextEdit::cursorForPosition(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK14QPlainTextEdit17cursorForPositionERK6QPoint(
    const QPlainTextEdit *self,
    const QPoint *pos) {
  return new QTextCursor(self->cursorForPosition(*pos));
}

//  QRect QPlainTextEdit::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QPlainTextEdit10cursorRectERK11QTextCursor(
    const QPlainTextEdit *self,
    const QTextCursor *cursor) {
  return new QRect(self->cursorRect(*cursor));
}

//  QRect QPlainTextEdit::cursorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK14QPlainTextEdit10cursorRectEv(const QPlainTextEdit *self) {
  return new QRect(self->cursorRect());
}

//  QString QPlainTextEdit::anchorAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QPlainTextEdit8anchorAtERK6QPoint(
    const QPlainTextEdit *self,
    const QPoint *pos) {
  return new QString(self->anchorAt(*pos));
}

//  bool QPlainTextEdit::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit13overwriteModeEv(
    const QPlainTextEdit *self) {
  return self->overwriteMode();
}

//  void QPlainTextEdit::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit16setOverwriteModeEb(
    QPlainTextEdit *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  qreal QPlainTextEdit::tabStopDistance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QPlainTextEdit15tabStopDistanceEv(
    const QPlainTextEdit *self) {
  return self->tabStopDistance();
}

//  void QPlainTextEdit::setTabStopDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit18setTabStopDistanceEd(
    QPlainTextEdit *self,
    qreal distance) {
  self->setTabStopDistance(distance);
}

//  int QPlainTextEdit::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit11cursorWidthEv(const QPlainTextEdit *self) {
  return self->cursorWidth();
}

//  void QPlainTextEdit::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit14setCursorWidthEi(
    QPlainTextEdit *self,
    int width) {
  self->setCursorWidth(width);
}

//  void QPlainTextEdit::moveCursor(QTextCursor::MoveOperation operation,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit10moveCursorEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QPlainTextEdit *self,
    QTextCursor::MoveOperation operation,
    QTextCursor::MoveMode mode) {
  self->moveCursor(operation, mode);
}

//  bool QPlainTextEdit::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QPlainTextEdit8canPasteEv(const QPlainTextEdit *self) {
  return self->canPaste();
}

//  void QPlainTextEdit::print(QPagedPaintDevice *printer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QPlainTextEdit5printEP17QPagedPaintDevice(
    const QPlainTextEdit *self,
    QPagedPaintDevice *printer) {
  self->print(printer);
}

//  int QPlainTextEdit::blockCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QPlainTextEdit10blockCountEv(const QPlainTextEdit *self) {
  return self->blockCount();
}

//  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QPlainTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}

//  QVariant QPlainTextEdit::inputMethodQuery(Qt::InputMethodQuery query,
//      QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QPlainTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QPlainTextEdit *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}

//  void QPlainTextEdit::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit12setPlainTextERK7QString(
    QPlainTextEdit *self,
    const QString *text) {
  self->setPlainText(*text);
}

//  void QPlainTextEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit3cutEv(QPlainTextEdit *self) {
  self->cut();
}

//  void QPlainTextEdit::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit4copyEv(QPlainTextEdit *self) {
  self->copy();
}

//  void QPlainTextEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit5pasteEv(QPlainTextEdit *self) {
  self->paste();
}

//  void QPlainTextEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit4undoEv(QPlainTextEdit *self) {
  self->undo();
}

//  void QPlainTextEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit4redoEv(QPlainTextEdit *self) {
  self->redo();
}

//  void QPlainTextEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit5clearEv(QPlainTextEdit *self) {
  self->clear();
}

//  void QPlainTextEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit9selectAllEv(QPlainTextEdit *self) {
  self->selectAll();
}

//  void QPlainTextEdit::insertPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15insertPlainTextERK7QString(
    QPlainTextEdit *self,
    const QString *text) {
  self->insertPlainText(*text);
}

//  void QPlainTextEdit::appendPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit15appendPlainTextERK7QString(
    QPlainTextEdit *self,
    const QString *text) {
  self->appendPlainText(*text);
}

//  void QPlainTextEdit::appendHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit10appendHtmlERK7QString(
    QPlainTextEdit *self,
    const QString *html) {
  self->appendHtml(*html);
}

//  void QPlainTextEdit::centerCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit12centerCursorEv(QPlainTextEdit *self) {
  self->centerCursor();
}

//  void QPlainTextEdit::zoomIn(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit6zoomInEi(QPlainTextEdit *self, int range) {
  self->zoomIn(range);
}

//  void QPlainTextEdit::zoomOut(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QPlainTextEdit7zoomOutEi(QPlainTextEdit *self, int range) {
  self->zoomOut(range);
}
