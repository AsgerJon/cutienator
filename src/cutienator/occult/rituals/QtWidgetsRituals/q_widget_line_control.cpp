//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetlinecontrol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetlinecontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qchar.h>
#include <QtGui/qfont.h>
#include <QtGui/qpalette.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QWidgetLineControl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWidgetLineControl : QWidgetLineControl {
  using QWidgetLineControl::timerEvent;
};

//  A QWidgetLineControl that Python can take functions over in. Every QWidgetLineControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
typedef void (*CuteQWidgetLineControlCall0)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWidgetLineControlCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWidgetLineControlCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetLineControlCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetLineControlCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetLineControlCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetLineControlCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWidgetLineControl : public QWidgetLineControl {
public:
  using QWidgetLineControl::QWidgetLineControl;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(lineedit)
  //  void QWidgetLineControl::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetLineControlCall0 call = reinterpret_cast<CuteQWidgetLineControlCall0>(taken[0]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidgetLineControl::timerEvent(event);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetLineControlCall1 call = reinterpret_cast<CuteQWidgetLineControlCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetLineControlCall2 call = reinterpret_cast<CuteQWidgetLineControlCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetLineControlCall3 call = reinterpret_cast<CuteQWidgetLineControlCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetLineControlCall4 call = reinterpret_cast<CuteQWidgetLineControlCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetLineControlCall5 call = reinterpret_cast<CuteQWidgetLineControlCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetLineControlCall6 call = reinterpret_cast<CuteQWidgetLineControlCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWidgetLineControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWidgetLineControl10metaObjectEv(
    const QWidgetLineControl *self) {
  return self->metaObject();
}

//  QString QWidgetLineControl::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWidgetLineControl2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWidgetLineControl::tr(s, c, n));
}

//  QWidgetLineControl::QWidgetLineControl(const QString &txt)
extern "C" Q_DECL_EXPORT
QWidgetLineControl *ritual_ZN18QWidgetLineControlC1ERK7QString(
    const QString *txt) {
  return new CuteQWidgetLineControl(*txt);
}

//  QWidgetLineControl::~QWidgetLineControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControlD1Ev(QWidgetLineControl *self) {
  delete self;
}

//  void QWidgetLineControl::setAccessibleObject(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl19setAccessibleObjectEP7QObject(
    QWidgetLineControl *self,
    QObject *object) {
  self->setAccessibleObject(object);
}

//  QObject *QWidgetLineControl::accessibleObject()
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN18QWidgetLineControl16accessibleObjectEv(
    QWidgetLineControl *self) {
  return self->accessibleObject();
}

//  int QWidgetLineControl::nextMaskBlank(int pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QWidgetLineControl13nextMaskBlankEi(
    QWidgetLineControl *self,
    int pos) {
  return self->nextMaskBlank(pos);
}

//  int QWidgetLineControl::prevMaskBlank(int pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QWidgetLineControl13prevMaskBlankEi(
    QWidgetLineControl *self,
    int pos) {
  return self->prevMaskBlank(pos);
}

//  bool QWidgetLineControl::isUndoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl15isUndoAvailableEv(
    const QWidgetLineControl *self) {
  return self->isUndoAvailable();
}

//  bool QWidgetLineControl::isRedoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl15isRedoAvailableEv(
    const QWidgetLineControl *self) {
  return self->isRedoAvailable();
}

//  void QWidgetLineControl::clearUndo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl9clearUndoEv(QWidgetLineControl *self) {
  self->clearUndo();
}

//  bool QWidgetLineControl::isModified() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl10isModifiedEv(
    const QWidgetLineControl *self) {
  return self->isModified();
}

//  void QWidgetLineControl::setModified(bool modified)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl11setModifiedEb(
    QWidgetLineControl *self,
    bool modified) {
  self->setModified(modified);
}

//  bool QWidgetLineControl::allSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl11allSelectedEv(
    const QWidgetLineControl *self) {
  return self->allSelected();
}

//  bool QWidgetLineControl::hasSelectedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl15hasSelectedTextEv(
    const QWidgetLineControl *self) {
  return self->hasSelectedText();
}

//  int QWidgetLineControl::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl5widthEv(const QWidgetLineControl *self) {
  return self->width();
}

//  int QWidgetLineControl::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl6heightEv(const QWidgetLineControl *self) {
  return self->height();
}

//  int QWidgetLineControl::ascent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl6ascentEv(const QWidgetLineControl *self) {
  return self->ascent();
}

//  qreal QWidgetLineControl::naturalTextWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWidgetLineControl16naturalTextWidthEv(
    const QWidgetLineControl *self) {
  return self->naturalTextWidth();
}

//  void QWidgetLineControl::setSelection(int start, int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12setSelectionEii(
    QWidgetLineControl *self,
    int start,
    int length) {
  self->setSelection(start, length);
}

//  QString QWidgetLineControl::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl12selectedTextEv(
    const QWidgetLineControl *self) {
  return new QString(self->selectedText());
}

//  QString QWidgetLineControl::textBeforeSelection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl19textBeforeSelectionEv(
    const QWidgetLineControl *self) {
  return new QString(self->textBeforeSelection());
}

//  QString QWidgetLineControl::textAfterSelection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl18textAfterSelectionEv(
    const QWidgetLineControl *self) {
  return new QString(self->textAfterSelection());
}

//  int QWidgetLineControl::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl14selectionStartEv(
    const QWidgetLineControl *self) {
  return self->selectionStart();
}

//  int QWidgetLineControl::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl12selectionEndEv(
    const QWidgetLineControl *self) {
  return self->selectionEnd();
}

//  bool QWidgetLineControl::inSelection(int x) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl11inSelectionEi(
    const QWidgetLineControl *self,
    int x) {
  return self->inSelection(x);
}

//  void QWidgetLineControl::removeSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl15removeSelectionEv(
    QWidgetLineControl *self) {
  self->removeSelection();
}

//  int QWidgetLineControl::start() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl5startEv(const QWidgetLineControl *self) {
  return self->start();
}

//  int QWidgetLineControl::end() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl3endEv(const QWidgetLineControl *self) {
  return self->end();
}

#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetLineControl::copy(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QWidgetLineControl4copyEN10QClipboard4ModeE(
    const QWidgetLineControl *self,
    QClipboard::Mode mode) {
  self->copy(mode);
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetLineControl::paste(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl5pasteEN10QClipboard4ModeE(
    QWidgetLineControl *self,
    QClipboard::Mode mode) {
  self->paste(mode);
}
#endif  // !defined(QT_NO_CLIPBOARD)

//  int QWidgetLineControl::cursor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl6cursorEv(const QWidgetLineControl *self) {
  return self->cursor();
}

//  int QWidgetLineControl::preeditCursor() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl13preeditCursorEv(
    const QWidgetLineControl *self) {
  return self->preeditCursor();
}

//  int QWidgetLineControl::cursorWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl11cursorWidthEv(
    const QWidgetLineControl *self) {
  return self->cursorWidth();
}

//  void QWidgetLineControl::setCursorWidth(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl14setCursorWidthEi(
    QWidgetLineControl *self,
    int value) {
  self->setCursorWidth(value);
}

//  Qt::CursorMoveStyle QWidgetLineControl::cursorMoveStyle() const
extern "C" Q_DECL_EXPORT
Qt::CursorMoveStyle ritual_ZNK18QWidgetLineControl15cursorMoveStyleEv(
    const QWidgetLineControl *self) {
  return self->cursorMoveStyle();
}

//  void QWidgetLineControl::setCursorMoveStyle(Qt::CursorMoveStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl18setCursorMoveStyleEN2Qt15CursorMoveStyleE(
    QWidgetLineControl *self,
    Qt::CursorMoveStyle style) {
  self->setCursorMoveStyle(style);
}

//  void QWidgetLineControl::moveCursor(int pos, bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl10moveCursorEib(
    QWidgetLineControl *self,
    int pos,
    bool mark) {
  self->moveCursor(pos, mark);
}

//  void QWidgetLineControl::cursorForward(bool mark, int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl13cursorForwardEbi(
    QWidgetLineControl *self,
    bool mark,
    int steps) {
  self->cursorForward(mark, steps);
}

//  void QWidgetLineControl::cursorWordForward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl17cursorWordForwardEb(
    QWidgetLineControl *self,
    bool mark) {
  self->cursorWordForward(mark);
}

//  void QWidgetLineControl::cursorWordBackward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl18cursorWordBackwardEb(
    QWidgetLineControl *self,
    bool mark) {
  self->cursorWordBackward(mark);
}

//  void QWidgetLineControl::home(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl4homeEb(
    QWidgetLineControl *self,
    bool mark) {
  self->home(mark);
}

//  void QWidgetLineControl::end(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl3endEb(
    QWidgetLineControl *self,
    bool mark) {
  self->end(mark);
}

//  int QWidgetLineControl::xToPos(int x, QTextLine::CursorPosition a1) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl6xToPosEiN9QTextLine14CursorPositionE(
    const QWidgetLineControl *self,
    int x,
    QTextLine::CursorPosition a1) {
  return self->xToPos(x, a1);
}

//  QRect QWidgetLineControl::rectForPos(int pos) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QWidgetLineControl10rectForPosEi(
    const QWidgetLineControl *self,
    int pos) {
  return new QRect(self->rectForPos(pos));
}

//  QRect QWidgetLineControl::cursorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QWidgetLineControl10cursorRectEv(
    const QWidgetLineControl *self) {
  return new QRect(self->cursorRect());
}

//  QRect QWidgetLineControl::anchorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QWidgetLineControl10anchorRectEv(
    const QWidgetLineControl *self) {
  return new QRect(self->anchorRect());
}

//  qreal QWidgetLineControl::cursorToX(int cursor) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWidgetLineControl9cursorToXEi(
    const QWidgetLineControl *self,
    int cursor) {
  return self->cursorToX(cursor);
}

//  qreal QWidgetLineControl::cursorToX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QWidgetLineControl9cursorToXEv(
    const QWidgetLineControl *self) {
  return self->cursorToX();
}

//  bool QWidgetLineControl::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl10isReadOnlyEv(
    const QWidgetLineControl *self) {
  return self->isReadOnly();
}

//  void QWidgetLineControl::setReadOnly(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl11setReadOnlyEb(
    QWidgetLineControl *self,
    bool enable) {
  self->setReadOnly(enable);
}

//  QString QWidgetLineControl::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl4textEv(
    const QWidgetLineControl *self) {
  return new QString(self->text());
}

//  void QWidgetLineControl::setText(const QString &txt)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl7setTextERK7QString(
    QWidgetLineControl *self,
    const QString *txt) {
  self->setText(*txt);
}

//  void QWidgetLineControl::commitPreedit()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl13commitPreeditEv(
    QWidgetLineControl *self) {
  self->commitPreedit();
}

//  QString QWidgetLineControl::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl11displayTextEv(
    const QWidgetLineControl *self) {
  return new QString(self->displayText());
}

//  QString QWidgetLineControl::surroundingText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl15surroundingTextEv(
    const QWidgetLineControl *self) {
  return new QString(self->surroundingText());
}

//  void QWidgetLineControl::backspace()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl9backspaceEv(QWidgetLineControl *self) {
  self->backspace();
}

//  void QWidgetLineControl::del()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl3delEv(QWidgetLineControl *self) {
  self->del();
}

//  void QWidgetLineControl::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl8deselectEv(QWidgetLineControl *self) {
  self->deselect();
}

//  void QWidgetLineControl::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl9selectAllEv(QWidgetLineControl *self) {
  self->selectAll();
}

//  void QWidgetLineControl::insert(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl6insertERK7QString(
    QWidgetLineControl *self,
    const QString *a0) {
  self->insert(*a0);
}

//  void QWidgetLineControl::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl5clearEv(QWidgetLineControl *self) {
  self->clear();
}

//  void QWidgetLineControl::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl4undoEv(QWidgetLineControl *self) {
  self->undo();
}

//  void QWidgetLineControl::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl4redoEv(QWidgetLineControl *self) {
  self->redo();
}

//  void QWidgetLineControl::selectWordAtPos(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl15selectWordAtPosEi(
    QWidgetLineControl *self,
    int a0) {
  self->selectWordAtPos(a0);
}

//  uint QWidgetLineControl::echoMode() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QWidgetLineControl8echoModeEv(
    const QWidgetLineControl *self) {
  return self->echoMode();
}

//  void QWidgetLineControl::setEchoMode(uint mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl11setEchoModeEj(
    QWidgetLineControl *self,
    uint mode) {
  self->setEchoMode(mode);
}

//  int QWidgetLineControl::maxLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl9maxLengthEv(
    const QWidgetLineControl *self) {
  return self->maxLength();
}

//  void QWidgetLineControl::setMaxLength(int maxLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12setMaxLengthEi(
    QWidgetLineControl *self,
    int maxLength) {
  self->setMaxLength(maxLength);
}

#if !defined(QT_NO_VALIDATOR)
//  const QValidator *QWidgetLineControl::validator() const
extern "C" Q_DECL_EXPORT
const QValidator *ritual_ZNK18QWidgetLineControl9validatorEv(
    const QWidgetLineControl *self) {
  return self->validator();
}
#endif  // !defined(QT_NO_VALIDATOR)

#if !defined(QT_NO_VALIDATOR)
//  void QWidgetLineControl::setValidator(const QValidator *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12setValidatorEPK10QValidator(
    QWidgetLineControl *self,
    const QValidator *v) {
  self->setValidator(v);
}
#endif  // !defined(QT_NO_VALIDATOR)

#if QT_CONFIG(completer)
//  QCompleter *QWidgetLineControl::completer() const
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZNK18QWidgetLineControl9completerEv(
    const QWidgetLineControl *self) {
  return self->completer();
}
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
//  void QWidgetLineControl::setCompleter(const QCompleter *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12setCompleterEPK10QCompleter(
    QWidgetLineControl *self,
    const QCompleter *c) {
  self->setCompleter(c);
}
#endif  // QT_CONFIG(completer)

#if QT_CONFIG(completer)
//  void QWidgetLineControl::complete(int key)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl8completeEi(
    QWidgetLineControl *self,
    int key) {
  self->complete(key);
}
#endif  // QT_CONFIG(completer)

//  int QWidgetLineControl::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl14cursorPositionEv(
    const QWidgetLineControl *self) {
  return self->cursorPosition();
}

//  void QWidgetLineControl::setCursorPosition(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl17setCursorPositionEi(
    QWidgetLineControl *self,
    int pos) {
  self->setCursorPosition(pos);
}

//  bool QWidgetLineControl::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl18hasAcceptableInputEv(
    const QWidgetLineControl *self) {
  return self->hasAcceptableInput();
}

//  bool QWidgetLineControl::fixup()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetLineControl5fixupEv(QWidgetLineControl *self) {
  return self->fixup();
}

//  QString QWidgetLineControl::inputMask() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl9inputMaskEv(
    const QWidgetLineControl *self) {
  return new QString(self->inputMask());
}

//  void QWidgetLineControl::setInputMask(const QString &mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12setInputMaskERK7QString(
    QWidgetLineControl *self,
    const QString *mask) {
  self->setInputMask(*mask);
}

#if !defined(QT_NO_IM)
//  bool QWidgetLineControl::composeMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl11composeModeEv(
    const QWidgetLineControl *self) {
  return self->composeMode();
}
#endif  // !defined(QT_NO_IM)

#if !defined(QT_NO_IM)
//  void QWidgetLineControl::setPreeditArea(int cursor, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl14setPreeditAreaEiRK7QString(
    QWidgetLineControl *self,
    int cursor,
    const QString *text) {
  self->setPreeditArea(cursor, *text);
}
#endif  // !defined(QT_NO_IM)

//  QString QWidgetLineControl::preeditAreaText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl15preeditAreaTextEv(
    const QWidgetLineControl *self) {
  return new QString(self->preeditAreaText());
}

//  void QWidgetLineControl::updatePasswordEchoEditing(bool editing)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl25updatePasswordEchoEditingEb(
    QWidgetLineControl *self,
    bool editing) {
  self->updatePasswordEchoEditing(editing);
}

//  bool QWidgetLineControl::passwordEchoEditing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl19passwordEchoEditingEv(
    const QWidgetLineControl *self) {
  return self->passwordEchoEditing();
}

//  QChar QWidgetLineControl::passwordCharacter() const
extern "C" Q_DECL_EXPORT
QChar *ritual_ZNK18QWidgetLineControl17passwordCharacterEv(
    const QWidgetLineControl *self) {
  return new QChar(self->passwordCharacter());
}

//  void QWidgetLineControl::setPasswordCharacter(QChar character)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl20setPasswordCharacterE5QChar(
    QWidgetLineControl *self,
    const QChar *character) {
  self->setPasswordCharacter(*character);
}

//  int QWidgetLineControl::passwordMaskDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl17passwordMaskDelayEv(
    const QWidgetLineControl *self) {
  return self->passwordMaskDelay();
}

//  void QWidgetLineControl::setPasswordMaskDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl20setPasswordMaskDelayEi(
    QWidgetLineControl *self,
    int delay) {
  self->setPasswordMaskDelay(delay);
}

//  Qt::LayoutDirection QWidgetLineControl::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK18QWidgetLineControl15layoutDirectionEv(
    const QWidgetLineControl *self) {
  return self->layoutDirection();
}

//  void QWidgetLineControl::setLayoutDirection(Qt::LayoutDirection
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QWidgetLineControl *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

//  void QWidgetLineControl::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl7setFontERK5QFont(
    QWidgetLineControl *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QWidgetLineControl::processInputMethodEvent(QInputMethodEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl23processInputMethodEventEP17QInputMethodEvent(
    QWidgetLineControl *self,
    QInputMethodEvent *event) {
  self->processInputMethodEvent(event);
}

//  void QWidgetLineControl::processKeyEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl15processKeyEventEP9QKeyEvent(
    QWidgetLineControl *self,
    QKeyEvent *ev) {
  self->processKeyEvent(ev);
}

//  void QWidgetLineControl::setBlinkingCursorEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl24setBlinkingCursorEnabledEb(
    QWidgetLineControl *self,
    bool enable) {
  self->setBlinkingCursorEnabled(enable);
}

//  void QWidgetLineControl::updateCursorBlinking()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl20updateCursorBlinkingEv(
    QWidgetLineControl *self) {
  self->updateCursorBlinking();
}

//  void QWidgetLineControl::resetCursorBlinkTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl21resetCursorBlinkTimerEv(
    QWidgetLineControl *self) {
  self->resetCursorBlinkTimer();
}

//  bool QWidgetLineControl::cursorBlinkStatus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl17cursorBlinkStatusEv(
    const QWidgetLineControl *self) {
  return self->cursorBlinkStatus();
}

//  QString QWidgetLineControl::cancelText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl10cancelTextEv(
    const QWidgetLineControl *self) {
  return new QString(self->cancelText());
}

//  void QWidgetLineControl::setCancelText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl13setCancelTextERK7QString(
    QWidgetLineControl *self,
    const QString *text) {
  self->setCancelText(*text);
}

//  const QPalette &QWidgetLineControl::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK18QWidgetLineControl7paletteEv(
    const QWidgetLineControl *self) {
  return new QPalette(self->palette());
}

//  void QWidgetLineControl::setPalette(const QPalette &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl10setPaletteERK8QPalette(
    QWidgetLineControl *self,
    const QPalette *p) {
  self->setPalette(*p);
}

//  void QWidgetLineControl::draw(QPainter *a0, const QPoint &a1, const QRect
//      &a2, int flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl4drawEP8QPainterRK6QPointRK5QRecti(
    QWidgetLineControl *self,
    QPainter *a0,
    const QPoint *a1,
    const QRect *a2,
    int flags) {
  self->draw(a0, *a1, *a2, flags);
}

#if !defined(QT_NO_SHORTCUT)
//  void QWidgetLineControl::processShortcutOverrideEvent(QKeyEvent *ke)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl28processShortcutOverrideEventEP9QKeyEvent(
    QWidgetLineControl *self,
    QKeyEvent *ke) {
  self->processShortcutOverrideEvent(ke);
}
#endif  // !defined(QT_NO_SHORTCUT)

//  QTextLayout *QWidgetLineControl::textLayout() const
extern "C" Q_DECL_EXPORT
QTextLayout *ritual_ZNK18QWidgetLineControl10textLayoutEv(
    const QWidgetLineControl *self) {
  return self->textLayout();
}

//  void QWidgetLineControl::init(const QString &txt)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl4initERK7QString(
    QWidgetLineControl *self,
    const QString *txt) {
  self->init(*txt);
}

//  void QWidgetLineControl::removeSelectedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl18removeSelectedTextEv(
    QWidgetLineControl *self) {
  self->removeSelectedText();
}

//  void QWidgetLineControl::internalSetText(const QString &txt, int pos,
//      bool edited)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl15internalSetTextERK7QStringib(
    QWidgetLineControl *self,
    const QString *txt,
    int pos,
    bool edited) {
  self->internalSetText(*txt, pos, edited);
}

//  void QWidgetLineControl::updateDisplayText(bool forceUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl17updateDisplayTextEb(
    QWidgetLineControl *self,
    bool forceUpdate) {
  self->updateDisplayText(forceUpdate);
}

//  void QWidgetLineControl::internalInsert(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl14internalInsertERK7QString(
    QWidgetLineControl *self,
    const QString *s) {
  self->internalInsert(*s);
}

//  void QWidgetLineControl::internalDelete(bool wasBackspace)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl14internalDeleteEb(
    QWidgetLineControl *self,
    bool wasBackspace) {
  self->internalDelete(wasBackspace);
}

//  void QWidgetLineControl::internalDeselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl16internalDeselectEv(
    QWidgetLineControl *self) {
  self->internalDeselect();
}

//  void QWidgetLineControl::internalUndo(int until)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12internalUndoEi(
    QWidgetLineControl *self,
    int until) {
  self->internalUndo(until);
}

//  void QWidgetLineControl::internalRedo()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl12internalRedoEv(
    QWidgetLineControl *self) {
  self->internalRedo();
}

//  void QWidgetLineControl::emitCursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl25emitCursorPositionChangedEv(
    QWidgetLineControl *self) {
  self->emitCursorPositionChanged();
}

//  bool QWidgetLineControl::finishChange(int validateFromState, bool update,
//      bool edited)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetLineControl12finishChangeEibb(
    QWidgetLineControl *self,
    int validateFromState,
    bool update,
    bool edited) {
  return self->finishChange(validateFromState, update, edited);
}

#if QT_CONFIG(completer)
//  bool QWidgetLineControl::advanceToEnabledItem(int dir)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QWidgetLineControl20advanceToEnabledItemEi(
    QWidgetLineControl *self,
    int dir) {
  return self->advanceToEnabledItem(dir);
}
#endif  // QT_CONFIG(completer)

//  void QWidgetLineControl::separate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl8separateEv(QWidgetLineControl *self) {
  self->separate();
}

//  void QWidgetLineControl::parseInputMask(const QString &maskFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl14parseInputMaskERK7QString(
    QWidgetLineControl *self,
    const QString *maskFields) {
  self->parseInputMask(*maskFields);
}

//  bool QWidgetLineControl::isValidInput(QChar key, QChar mask) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl12isValidInputE5QCharS0_(
    const QWidgetLineControl *self,
    const QChar *key,
    const QChar *mask) {
  return self->isValidInput(*key, *mask);
}

//  bool QWidgetLineControl::hasAcceptableInput(const QString &text) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QWidgetLineControl18hasAcceptableInputERK7QString(
    const QWidgetLineControl *self,
    const QString *text) {
  return self->hasAcceptableInput(*text);
}

//  QString QWidgetLineControl::maskString(int pos, const QString &str, bool
//      clear) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl10maskStringEiRK7QStringb(
    const QWidgetLineControl *self,
    int pos,
    const QString *str,
    bool clear) {
  return new QString(self->maskString(pos, *str, clear));
}

//  QString QWidgetLineControl::clearString(int pos, int len) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl11clearStringEii(
    const QWidgetLineControl *self,
    int pos,
    int len) {
  return new QString(self->clearString(pos, len));
}

//  QString QWidgetLineControl::stripString(const QString &str) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QWidgetLineControl11stripStringERK7QString(
    const QWidgetLineControl *self,
    const QString *str) {
  return new QString(self->stripString(*str));
}

//  int QWidgetLineControl::findInMask(int pos, bool forward, bool
//      findSeparator, QChar searchChar) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl10findInMaskEibb5QChar(
    const QWidgetLineControl *self,
    int pos,
    bool forward,
    bool findSeparator,
    const QChar *searchChar) {
  return self->findInMask(pos, forward, findSeparator, *searchChar);
}

//  void QWidgetLineControl::cancelPasswordEchoTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl23cancelPasswordEchoTimerEv(
    QWidgetLineControl *self) {
  self->cancelPasswordEchoTimer();
}

//  int QWidgetLineControl::redoTextLayout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QWidgetLineControl14redoTextLayoutEv(
    const QWidgetLineControl *self) {
  return self->redoTextLayout();
}

//  void QWidgetLineControl::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl10timerEventEP11QTimerEvent(
    QWidgetLineControl *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  void QWidgetLineControl::_q_deleteSelected()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWidgetLineControl17_q_deleteSelectedEv(
    QWidgetLineControl *self) {
  self->_q_deleteSelected();
}

//  a Python function taken by a CuteQWidgetLineControl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetLineControl(
    QWidgetLineControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetLineControl *>(self)->take(key, call);
}

//  void QWidgetLineControl::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWidgetLineControl10timerEventEP11QTimerEvent(
    QWidgetLineControl *self,
    QTimerEvent *event) {
  static_cast<OwnQWidgetLineControl *>(self)->OwnQWidgetLineControl::timerEvent(
      event);
}

#endif  // QT_CONFIG(lineedit)
