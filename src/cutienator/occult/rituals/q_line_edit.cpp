//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlineedit.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlineedit.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmargins.h>
#include <QtGui/qicon.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QLineEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QLineEdit10metaObjectEv(
    const QLineEdit *self) {
  return self->metaObject();
}

//  QString QLineEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QLineEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLineEdit::tr(s, c, n));
}

//  QLineEdit::QLineEdit(QWidget *parent)
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZN9QLineEditC1EP7QWidget(QWidget *parent) {
  return new QLineEdit(parent);
}

//  QLineEdit::QLineEdit(const QString &a0, QWidget *parent)
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZN9QLineEditC1ERK7QStringP7QWidget(
    const QString *a0,
    QWidget *parent) {
  return new QLineEdit(*a0, parent);
}

//  QLineEdit::~QLineEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEditD1Ev(QLineEdit *self) {
  delete self;
}

//  QString QLineEdit::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit4textEv(const QLineEdit *self) {
  return new QString(self->text());
}

//  QString QLineEdit::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit11displayTextEv(const QLineEdit *self) {
  return new QString(self->displayText());
}

//  QString QLineEdit::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit15placeholderTextEv(const QLineEdit *self) {
  return new QString(self->placeholderText());
}

//  void QLineEdit::setPlaceholderText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit18setPlaceholderTextERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->setPlaceholderText(*a0);
}

//  int QLineEdit::maxLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit9maxLengthEv(const QLineEdit *self) {
  return self->maxLength();
}

//  void QLineEdit::setMaxLength(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setMaxLengthEi(QLineEdit *self, int a0) {
  self->setMaxLength(a0);
}

//  void QLineEdit::setFrame(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit8setFrameEb(QLineEdit *self, bool a0) {
  self->setFrame(a0);
}

//  bool QLineEdit::hasFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit8hasFrameEv(const QLineEdit *self) {
  return self->hasFrame();
}

//  void QLineEdit::setClearButtonEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit21setClearButtonEnabledEb(
    QLineEdit *self,
    bool enable) {
  self->setClearButtonEnabled(enable);
}

//  bool QLineEdit::isClearButtonEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit20isClearButtonEnabledEv(const QLineEdit *self) {
  return self->isClearButtonEnabled();
}

//  EchoMode QLineEdit::echoMode() const
extern "C" Q_DECL_EXPORT
QLineEdit::EchoMode ritual_ZNK9QLineEdit8echoModeEv(const QLineEdit *self) {
  return self->echoMode();
}

//  void QLineEdit::setEchoMode(EchoMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11setEchoModeENS_8EchoModeE(
    QLineEdit *self,
    QLineEdit::EchoMode a0) {
  self->setEchoMode(a0);
}

//  bool QLineEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit10isReadOnlyEv(const QLineEdit *self) {
  return self->isReadOnly();
}

//  void QLineEdit::setReadOnly(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11setReadOnlyEb(QLineEdit *self, bool a0) {
  self->setReadOnly(a0);
}

//  void QLineEdit::setValidator(const QValidator *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setValidatorEPK10QValidator(
    QLineEdit *self,
    const QValidator *a0) {
  self->setValidator(a0);
}

//  const QValidator *QLineEdit::validator() const
extern "C" Q_DECL_EXPORT
const QValidator *ritual_ZNK9QLineEdit9validatorEv(const QLineEdit *self) {
  return self->validator();
}

//  void QLineEdit::setCompleter(QCompleter *completer)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setCompleterEP10QCompleter(
    QLineEdit *self,
    QCompleter *completer) {
  self->setCompleter(completer);
}

//  QCompleter *QLineEdit::completer() const
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZNK9QLineEdit9completerEv(const QLineEdit *self) {
  return self->completer();
}

//  QSize QLineEdit::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QLineEdit8sizeHintEv(const QLineEdit *self) {
  return new QSize(self->sizeHint());
}

//  QSize QLineEdit::minimumSizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QLineEdit15minimumSizeHintEv(const QLineEdit *self) {
  return new QSize(self->minimumSizeHint());
}

//  int QLineEdit::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit14cursorPositionEv(const QLineEdit *self) {
  return self->cursorPosition();
}

//  void QLineEdit::setCursorPosition(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit17setCursorPositionEi(QLineEdit *self, int a0) {
  self->setCursorPosition(a0);
}

//  int QLineEdit::cursorPositionAt(const QPoint &pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QLineEdit16cursorPositionAtERK6QPoint(
    QLineEdit *self,
    const QPoint *pos) {
  return self->cursorPositionAt(*pos);
}

//  void QLineEdit::setAlignment(Qt::Alignment flag)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QLineEdit *self,
    int flag) {
  self->setAlignment(QFlags<Qt::AlignmentFlag>::fromInt(flag));
}

//  Qt::Alignment QLineEdit::alignment() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit9alignmentEv(const QLineEdit *self) {
  return static_cast<int>(self->alignment().toInt());
}

//  void QLineEdit::cursorForward(bool mark, int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit13cursorForwardEbi(
    QLineEdit *self,
    bool mark,
    int steps) {
  self->cursorForward(mark, steps);
}

//  void QLineEdit::cursorBackward(bool mark, int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14cursorBackwardEbi(
    QLineEdit *self,
    bool mark,
    int steps) {
  self->cursorBackward(mark, steps);
}

//  void QLineEdit::cursorWordForward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit17cursorWordForwardEb(QLineEdit *self, bool mark) {
  self->cursorWordForward(mark);
}

//  void QLineEdit::cursorWordBackward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit18cursorWordBackwardEb(QLineEdit *self, bool mark) {
  self->cursorWordBackward(mark);
}

//  void QLineEdit::backspace()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9backspaceEv(QLineEdit *self) {
  self->backspace();
}

//  void QLineEdit::del()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit3delEv(QLineEdit *self) {
  self->del();
}

//  void QLineEdit::home(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit4homeEb(QLineEdit *self, bool mark) {
  self->home(mark);
}

//  void QLineEdit::end(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit3endEb(QLineEdit *self, bool mark) {
  self->end(mark);
}

//  bool QLineEdit::isModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit10isModifiedEv(const QLineEdit *self) {
  return self->isModified();
}

//  void QLineEdit::setModified(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit11setModifiedEb(QLineEdit *self, bool a0) {
  self->setModified(a0);
}

//  void QLineEdit::setSelection(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setSelectionEii(QLineEdit *self, int a0, int a1) {
  self->setSelection(a0, a1);
}

//  bool QLineEdit::hasSelectedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit15hasSelectedTextEv(const QLineEdit *self) {
  return self->hasSelectedText();
}

//  QString QLineEdit::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit12selectedTextEv(const QLineEdit *self) {
  return new QString(self->selectedText());
}

//  int QLineEdit::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit14selectionStartEv(const QLineEdit *self) {
  return self->selectionStart();
}

//  int QLineEdit::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit12selectionEndEv(const QLineEdit *self) {
  return self->selectionEnd();
}

//  int QLineEdit::selectionLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QLineEdit15selectionLengthEv(const QLineEdit *self) {
  return self->selectionLength();
}

//  bool QLineEdit::isUndoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit15isUndoAvailableEv(const QLineEdit *self) {
  return self->isUndoAvailable();
}

//  bool QLineEdit::isRedoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit15isRedoAvailableEv(const QLineEdit *self) {
  return self->isRedoAvailable();
}

//  void QLineEdit::setDragEnabled(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14setDragEnabledEb(QLineEdit *self, bool b) {
  self->setDragEnabled(b);
}

//  bool QLineEdit::dragEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit11dragEnabledEv(const QLineEdit *self) {
  return self->dragEnabled();
}

//  void QLineEdit::setCursorMoveStyle(Qt::CursorMoveStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit18setCursorMoveStyleEN2Qt15CursorMoveStyleE(
    QLineEdit *self,
    Qt::CursorMoveStyle style) {
  self->setCursorMoveStyle(style);
}

//  Qt::CursorMoveStyle QLineEdit::cursorMoveStyle() const
extern "C" Q_DECL_EXPORT
Qt::CursorMoveStyle ritual_ZNK9QLineEdit15cursorMoveStyleEv(
    const QLineEdit *self) {
  return self->cursorMoveStyle();
}

//  QString QLineEdit::inputMask() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QLineEdit9inputMaskEv(const QLineEdit *self) {
  return new QString(self->inputMask());
}

//  void QLineEdit::setInputMask(const QString &inputMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit12setInputMaskERK7QString(
    QLineEdit *self,
    const QString *inputMask) {
  self->setInputMask(*inputMask);
}

//  bool QLineEdit::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLineEdit18hasAcceptableInputEv(const QLineEdit *self) {
  return self->hasAcceptableInput();
}

//  void QLineEdit::setTextMargins(int left, int top, int right, int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14setTextMarginsEiiii(
    QLineEdit *self,
    int left,
    int top,
    int right,
    int bottom) {
  self->setTextMargins(left, top, right, bottom);
}

//  void QLineEdit::setTextMargins(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit14setTextMarginsERK8QMargins(
    QLineEdit *self,
    const QMargins *margins) {
  self->setTextMargins(*margins);
}

//  QMargins QLineEdit::textMargins() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK9QLineEdit11textMarginsEv(const QLineEdit *self) {
  return new QMargins(self->textMargins());
}

//  void QLineEdit::addAction(QAction *action, ActionPosition position)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9addActionEP7QActionNS_14ActionPositionE(
    QLineEdit *self,
    QAction *action,
    QLineEdit::ActionPosition position) {
  self->addAction(action, position);
}

//  QAction *QLineEdit::addAction(const QIcon &icon, ActionPosition position)
extern "C" Q_DECL_EXPORT
QAction *ritual_ZN9QLineEdit9addActionERK5QIconNS_14ActionPositionE(
    QLineEdit *self,
    const QIcon *icon,
    QLineEdit::ActionPosition position) {
  return self->addAction(*icon, position);
}

//  void QLineEdit::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit7setTextERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->setText(*a0);
}

//  void QLineEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit5clearEv(QLineEdit *self) {
  self->clear();
}

//  void QLineEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit9selectAllEv(QLineEdit *self) {
  self->selectAll();
}

//  void QLineEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit4undoEv(QLineEdit *self) {
  self->undo();
}

//  void QLineEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit4redoEv(QLineEdit *self) {
  self->redo();
}

//  void QLineEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit3cutEv(QLineEdit *self) {
  self->cut();
}

//  void QLineEdit::copy() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK9QLineEdit4copyEv(const QLineEdit *self) {
  self->copy();
}

//  void QLineEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit5pasteEv(QLineEdit *self) {
  self->paste();
}

//  void QLineEdit::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit8deselectEv(QLineEdit *self) {
  self->deselect();
}

//  void QLineEdit::insert(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit6insertERK7QString(
    QLineEdit *self,
    const QString *a0) {
  self->insert(*a0);
}

//  QMenu *QLineEdit::createStandardContextMenu()
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZN9QLineEdit25createStandardContextMenuEv(QLineEdit *self) {
  return self->createStandardContextMenu();
}

//  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery a0) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QLineEdit *self,
    Qt::InputMethodQuery a0) {
  return new QVariant(self->inputMethodQuery(a0));
}

//  QVariant QLineEdit::inputMethodQuery(Qt::InputMethodQuery property,
//      QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QLineEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QLineEdit *self,
    Qt::InputMethodQuery property,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(property, *argument));
}

//  void QLineEdit::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLineEdit10timerEventEP11QTimerEvent(
    QLineEdit *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  bool QLineEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QLineEdit5eventEP6QEvent(QLineEdit *self, QEvent *a0) {
  return self->event(a0);
}
