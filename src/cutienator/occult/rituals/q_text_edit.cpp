//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtextedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtextedit.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/qcolor.h>
#include <QtGui/qfont.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QTextEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTextEdit10metaObjectEv(
    const QTextEdit *self) {
  return self->metaObject();
}

//  QString QTextEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTextEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextEdit::tr(s, c, n));
}

//  QTextEdit::QTextEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZN9QTextEditC1EP7QWidget(QWidget *parent) {
  return new QTextEdit(parent);
}

//  QTextEdit::QTextEdit(const QString &text, QWidget *parent)
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZN9QTextEditC1ERK7QStringP7QWidget(
    const QString *text,
    QWidget *parent) {
  return new QTextEdit(*text, parent);
}

//  QTextEdit::~QTextEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEditD1Ev(QTextEdit *self) {
  delete self;
}

//  void QTextEdit::setDocument(QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11setDocumentEP13QTextDocument(
    QTextEdit *self,
    QTextDocument *document) {
  self->setDocument(document);
}

//  QTextDocument *QTextEdit::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK9QTextEdit8documentEv(const QTextEdit *self) {
  return self->document();
}

//  void QTextEdit::setPlaceholderText(const QString &placeholderText)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setPlaceholderTextERK7QString(
    QTextEdit *self,
    const QString *placeholderText) {
  self->setPlaceholderText(*placeholderText);
}

//  QString QTextEdit::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit15placeholderTextEv(const QTextEdit *self) {
  return new QString(self->placeholderText());
}

//  void QTextEdit::setTextCursor(const QTextCursor &cursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setTextCursorERK11QTextCursor(
    QTextEdit *self,
    const QTextCursor *cursor) {
  self->setTextCursor(*cursor);
}

//  QTextCursor QTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK9QTextEdit10textCursorEv(const QTextEdit *self) {
  return new QTextCursor(self->textCursor());
}

//  bool QTextEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit10isReadOnlyEv(const QTextEdit *self) {
  return self->isReadOnly();
}

//  void QTextEdit::setReadOnly(bool ro)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11setReadOnlyEb(QTextEdit *self, bool ro) {
  self->setReadOnly(ro);
}

//  void QTextEdit::setTextInteractionFlags(Qt::TextInteractionFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit23setTextInteractionFlagsE6QFlagsIN2Qt19TextInteractionFlagEE(
    QTextEdit *self,
    int flags) {
  self->setTextInteractionFlags(
      QFlags<Qt::TextInteractionFlag>::fromInt(flags));
}

//  Qt::TextInteractionFlags QTextEdit::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit20textInteractionFlagsEv(const QTextEdit *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}

//  qreal QTextEdit::fontPointSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextEdit13fontPointSizeEv(const QTextEdit *self) {
  return self->fontPointSize();
}

//  QString QTextEdit::fontFamily() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit10fontFamilyEv(const QTextEdit *self) {
  return new QString(self->fontFamily());
}

//  int QTextEdit::fontWeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit10fontWeightEv(const QTextEdit *self) {
  return self->fontWeight();
}

//  bool QTextEdit::fontUnderline() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit13fontUnderlineEv(const QTextEdit *self) {
  return self->fontUnderline();
}

//  bool QTextEdit::fontItalic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit10fontItalicEv(const QTextEdit *self) {
  return self->fontItalic();
}

//  QColor QTextEdit::textColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QTextEdit9textColorEv(const QTextEdit *self) {
  return new QColor(self->textColor());
}

//  QColor QTextEdit::textBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QTextEdit19textBackgroundColorEv(const QTextEdit *self) {
  return new QColor(self->textBackgroundColor());
}

//  QFont QTextEdit::currentFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK9QTextEdit11currentFontEv(const QTextEdit *self) {
  return new QFont(self->currentFont());
}

//  Qt::Alignment QTextEdit::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit9alignmentEv(const QTextEdit *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QTextEdit::mergeCurrentCharFormat(const QTextCharFormat &modifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit22mergeCurrentCharFormatERK15QTextCharFormat(
    QTextEdit *self,
    const QTextCharFormat *modifier) {
  self->mergeCurrentCharFormat(*modifier);
}

//  void QTextEdit::setCurrentCharFormat(const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit20setCurrentCharFormatERK15QTextCharFormat(
    QTextEdit *self,
    const QTextCharFormat *format) {
  self->setCurrentCharFormat(*format);
}

//  QTextCharFormat QTextEdit::currentCharFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK9QTextEdit17currentCharFormatEv(
    const QTextEdit *self) {
  return new QTextCharFormat(self->currentCharFormat());
}

//  AutoFormatting QTextEdit::autoFormatting() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit14autoFormattingEv(const QTextEdit *self) {
  return static_cast<int>(self->autoFormatting().toInt());
}

//  void QTextEdit::setAutoFormatting(AutoFormatting features)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit17setAutoFormattingE6QFlagsINS_18AutoFormattingFlagEE(
    QTextEdit *self,
    int features) {
  self->setAutoFormatting(
      QFlags<QTextEdit::AutoFormattingFlag>::fromInt(features));
}

//  bool QTextEdit::tabChangesFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit15tabChangesFocusEv(const QTextEdit *self) {
  return self->tabChangesFocus();
}

//  void QTextEdit::setTabChangesFocus(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setTabChangesFocusEb(QTextEdit *self, bool b) {
  self->setTabChangesFocus(b);
}

//  void QTextEdit::setDocumentTitle(const QString &title)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setDocumentTitleERK7QString(
    QTextEdit *self,
    const QString *title) {
  self->setDocumentTitle(*title);
}

//  QString QTextEdit::documentTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit13documentTitleEv(const QTextEdit *self) {
  return new QString(self->documentTitle());
}

//  bool QTextEdit::isUndoRedoEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit17isUndoRedoEnabledEv(const QTextEdit *self) {
  return self->isUndoRedoEnabled();
}

//  void QTextEdit::setUndoRedoEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setUndoRedoEnabledEb(
    QTextEdit *self,
    bool enable) {
  self->setUndoRedoEnabled(enable);
}

//  LineWrapMode QTextEdit::lineWrapMode() const
extern "C" Q_DECL_EXPORT
QTextEdit::LineWrapMode ritual_ZNK9QTextEdit12lineWrapModeEv(
    const QTextEdit *self) {
  return self->lineWrapMode();
}

//  void QTextEdit::setLineWrapMode(LineWrapMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15setLineWrapModeENS_12LineWrapModeE(
    QTextEdit *self,
    QTextEdit::LineWrapMode mode) {
  self->setLineWrapMode(mode);
}

//  int QTextEdit::lineWrapColumnOrWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit21lineWrapColumnOrWidthEv(const QTextEdit *self) {
  return self->lineWrapColumnOrWidth();
}

//  void QTextEdit::setLineWrapColumnOrWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit24setLineWrapColumnOrWidthEi(
    QTextEdit *self,
    int w) {
  self->setLineWrapColumnOrWidth(w);
}

//  QTextOption::WrapMode QTextEdit::wordWrapMode() const
extern "C" Q_DECL_EXPORT
QTextOption::WrapMode ritual_ZNK9QTextEdit12wordWrapModeEv(
    const QTextEdit *self) {
  return self->wordWrapMode();
}

//  void QTextEdit::setWordWrapMode(QTextOption::WrapMode policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15setWordWrapModeEN11QTextOption8WrapModeE(
    QTextEdit *self,
    QTextOption::WrapMode policy) {
  self->setWordWrapMode(policy);
}

//  bool QTextEdit::find(const QString &exp, QTextDocument::FindFlags
//      options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTextEdit4findERK7QString6QFlagsIN13QTextDocument8FindFlagEE(
    QTextEdit *self,
    const QString *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

//  bool QTextEdit::find(const QRegularExpression &exp,
//      QTextDocument::FindFlags options)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QTextEdit4findERK18QRegularExpression6QFlagsIN13QTextDocument8FindFlagEE(
    QTextEdit *self,
    const QRegularExpression *exp,
    int options) {
  return self->find(*exp, QFlags<QTextDocument::FindFlag>::fromInt(options));
}

//  QString QTextEdit::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit11toPlainTextEv(const QTextEdit *self) {
  return new QString(self->toPlainText());
}

//  QString QTextEdit::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit6toHtmlEv(const QTextEdit *self) {
  return new QString(self->toHtml());
}

//  QString QTextEdit::toMarkdown(QTextDocument::MarkdownFeatures features)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit10toMarkdownE6QFlagsIN13QTextDocument15MarkdownFeatureEE(
    const QTextEdit *self,
    int features) {
  return new QString(
      self->toMarkdown(
          QFlags<QTextDocument::MarkdownFeature>::fromInt(features)));
}

//  void QTextEdit::ensureCursorVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit19ensureCursorVisibleEv(QTextEdit *self) {
  self->ensureCursorVisible();
}

//  QVariant QTextEdit::loadResource(int type, const QUrl &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN9QTextEdit12loadResourceEiRK4QUrl(
    QTextEdit *self,
    int type,
    const QUrl *name) {
  return new QVariant(self->loadResource(type, *name));
}

//  QMenu *QTextEdit::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN9QTextEdit25createStandardContextMenuEv(QTextEdit *self) {
  return self->createStandardContextMenu();
}

//  QMenu *QTextEdit::createStandardContextMenu(const QPoint &position)
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN9QTextEdit25createStandardContextMenuERK6QPoint(
    QTextEdit *self,
    const QPoint *position) {
  return self->createStandardContextMenu(*position);
}

//  QTextCursor QTextEdit::cursorForPosition(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK9QTextEdit17cursorForPositionERK6QPoint(
    const QTextEdit *self,
    const QPoint *pos) {
  return new QTextCursor(self->cursorForPosition(*pos));
}

//  QRect QTextEdit::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QTextEdit10cursorRectERK11QTextCursor(
    const QTextEdit *self,
    const QTextCursor *cursor) {
  return new QRect(self->cursorRect(*cursor));
}

//  QRect QTextEdit::cursorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QTextEdit10cursorRectEv(const QTextEdit *self) {
  return new QRect(self->cursorRect());
}

//  QString QTextEdit::anchorAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextEdit8anchorAtERK6QPoint(
    const QTextEdit *self,
    const QPoint *pos) {
  return new QString(self->anchorAt(*pos));
}

//  bool QTextEdit::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit13overwriteModeEv(const QTextEdit *self) {
  return self->overwriteMode();
}

//  void QTextEdit::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setOverwriteModeEb(
    QTextEdit *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  qreal QTextEdit::tabStopDistance() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK9QTextEdit15tabStopDistanceEv(const QTextEdit *self) {
  return self->tabStopDistance();
}

//  void QTextEdit::setTabStopDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit18setTabStopDistanceEd(
    QTextEdit *self,
    qreal distance) {
  self->setTabStopDistance(distance);
}

//  int QTextEdit::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextEdit11cursorWidthEv(const QTextEdit *self) {
  return self->cursorWidth();
}

//  void QTextEdit::setCursorWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14setCursorWidthEi(QTextEdit *self, int width) {
  self->setCursorWidth(width);
}

//  bool QTextEdit::acceptRichText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit14acceptRichTextEv(const QTextEdit *self) {
  return self->acceptRichText();
}

//  void QTextEdit::setAcceptRichText(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit17setAcceptRichTextEb(QTextEdit *self, bool accept) {
  self->setAcceptRichText(accept);
}

//  void QTextEdit::moveCursor(QTextCursor::MoveOperation operation,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10moveCursorEN11QTextCursor13MoveOperationENS0_8MoveModeE(
    QTextEdit *self,
    QTextCursor::MoveOperation operation,
    QTextCursor::MoveMode mode) {
  self->moveCursor(operation, mode);
}

//  bool QTextEdit::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QTextEdit8canPasteEv(const QTextEdit *self) {
  return self->canPaste();
}

//  void QTextEdit::print(QPagedPaintDevice *printer) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QTextEdit5printEP17QPagedPaintDevice(
    const QTextEdit *self,
    QPagedPaintDevice *printer) {
  self->print(printer);
}

//  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}

//  QVariant QTextEdit::inputMethodQuery(Qt::InputMethodQuery query, QVariant
//      argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QTextEdit *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}

//  void QTextEdit::setFontPointSize(qreal s)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setFontPointSizeEd(QTextEdit *self, qreal s) {
  self->setFontPointSize(s);
}

//  void QTextEdit::setFontFamily(const QString &fontFamily)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setFontFamilyERK7QString(
    QTextEdit *self,
    const QString *fontFamily) {
  self->setFontFamily(*fontFamily);
}

//  void QTextEdit::setFontWeight(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setFontWeightEi(QTextEdit *self, int w) {
  self->setFontWeight(w);
}

//  void QTextEdit::setFontUnderline(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit16setFontUnderlineEb(QTextEdit *self, bool b) {
  self->setFontUnderline(b);
}

//  void QTextEdit::setFontItalic(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit13setFontItalicEb(QTextEdit *self, bool b) {
  self->setFontItalic(b);
}

//  void QTextEdit::setTextColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12setTextColorERK6QColor(
    QTextEdit *self,
    const QColor *c) {
  self->setTextColor(*c);
}

//  void QTextEdit::setTextBackgroundColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit22setTextBackgroundColorERK6QColor(
    QTextEdit *self,
    const QColor *c) {
  self->setTextBackgroundColor(*c);
}

//  void QTextEdit::setCurrentFont(const QFont &f)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14setCurrentFontERK5QFont(
    QTextEdit *self,
    const QFont *f) {
  self->setCurrentFont(*f);
}

//  void QTextEdit::setAlignment(Qt::Alignment a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTextEdit *self,
    int a) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(a));
}

//  void QTextEdit::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit12setPlainTextERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->setPlainText(*text);
}

//  void QTextEdit::setHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7setHtmlERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->setHtml(*text);
}

//  void QTextEdit::setMarkdown(const QString &markdown)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit11setMarkdownERK7QString(
    QTextEdit *self,
    const QString *markdown) {
  self->setMarkdown(*markdown);
}

//  void QTextEdit::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7setTextERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->setText(*text);
}

//  void QTextEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit3cutEv(QTextEdit *self) {
  self->cut();
}

//  void QTextEdit::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit4copyEv(QTextEdit *self) {
  self->copy();
}

//  void QTextEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit5pasteEv(QTextEdit *self) {
  self->paste();
}

//  void QTextEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit4undoEv(QTextEdit *self) {
  self->undo();
}

//  void QTextEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit4redoEv(QTextEdit *self) {
  self->redo();
}

//  void QTextEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit5clearEv(QTextEdit *self) {
  self->clear();
}

//  void QTextEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit9selectAllEv(QTextEdit *self) {
  self->selectAll();
}

//  void QTextEdit::insertPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit15insertPlainTextERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->insertPlainText(*text);
}

//  void QTextEdit::insertHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit10insertHtmlERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->insertHtml(*text);
}

//  void QTextEdit::append(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit6appendERK7QString(
    QTextEdit *self,
    const QString *text) {
  self->append(*text);
}

//  void QTextEdit::scrollToAnchor(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit14scrollToAnchorERK7QString(
    QTextEdit *self,
    const QString *name) {
  self->scrollToAnchor(*name);
}

//  void QTextEdit::zoomIn(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit6zoomInEi(QTextEdit *self, int range) {
  self->zoomIn(range);
}

//  void QTextEdit::zoomOut(int range)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextEdit7zoomOutEi(QTextEdit *self, int range) {
  self->zoomOut(range);
}
