//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtQuick/private/qquicktextcontrol_p.h>
#include <QtQuick/private/qquicktextcontrol_p_p.h>
#ifndef QT_NO_TEXTCONTROL
#include <QtCore/qcoreapplication.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtGui/qclipboard.h>
#include <QtCore/qtimer.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qtextdocumentwriter.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtransform.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbuffer.h>
#include <QtGui/qguiapplication.h>
#include <limits.h>
#include <QtGui/qtexttable.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qquickdeliveryagent_p_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 43, as local:qquicktextcontrol.cpp:textCursorWidth
#if !defined(QT_NO_TEXTCONTROL)
const int textCursorWidth = 1;
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 48, as local:qquicktextcontrol.cpp:currentTextLine
#if !defined(QT_NO_TEXTCONTROL)
static QTextLine currentTextLine(const QTextCursor &cursor)
{
    const QTextBlock block = cursor.block();
    if (!block.isValid())
        return QTextLine();

    const QTextLayout *layout = block.layout();
    if (!layout)
        return QTextLine();

    const int relativePos = cursor.position() - block.position();
    return layout->lineForTextPosition(relativePos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/util/qquickdeliveryagent.cpp, line 38, as _Z12lcHoverTracev
inline const QLoggingCategory &lcHoverTrace()
{
    static const QLoggingCategory category("qt.quick.hover.trace");
    return category;
}

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 62, as _ZN24QQuickTextControlPrivateC1Ev
#if !defined(QT_NO_TEXTCONTROL)
inline QQuickTextControlPrivate::QQuickTextControlPrivate()
    : doc(nullptr),
#if QT_CONFIG(im)
      preeditCursor(0),
#endif
      interactionFlags(Qt::TextEditorInteraction),
      cursorOn(false),
      cursorIsFocusIndicator(false),
      mousePressed(false),
      lastSelectionState(false),
      ignoreAutomaticScrollbarAdjustement(false),
      overwriteMode(false),
      acceptRichText(true),
      cursorVisible(false),
      cursorBlinkingEnabled(false),
      hasFocus(false),
      hadSelectionOnMousePress(false),
      wordSelectionEnabled(false),
      hasImState(false),
      cursorRectangleChanged(false),
      hoveredMarker(false),
      selectByTouchDrag(false),
      imSelectionAfterPress(false),
      beingEdited(false),
      lastSelectionStart(-1),
      lastSelectionEnd(-1)
{}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 324, as _ZN24QQuickTextControlPrivate17setCursorPositionERK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::setCursorPosition(const QPointF &pos)
{
    Q_Q(QQuickTextControl);
    const int cursorPos = q->hitTest(pos, Qt::FuzzyHit);
    if (cursorPos == -1)
        return;
    cursor.setPosition(cursorPos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 333, as _ZN24QQuickTextControlPrivate17setCursorPositionEiN11QTextCursor8MoveModeE
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::setCursorPosition(int pos, QTextCursor::MoveMode mode)
{
    cursor.setPosition(pos, mode);

    if (mode != QTextCursor::KeepAnchor) {
        selectedWordOnDoubleClick = QTextCursor();
        selectedBlockOnTripleClick = QTextCursor();
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 419, as _ZN24QQuickTextControlPrivate21setClipboardSelectionEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(clipboard)
inline void QQuickTextControlPrivate::setClipboardSelection()
{
    QClipboard *clipboard = QGuiApplication::clipboard();
    if (!cursor.hasSelection() || !clipboard->supportsSelection())
        return;
    Q_Q(QQuickTextControl);
    QMimeData *data = q->createMimeDataFromSelection();
    clipboard->setMimeData(data, QClipboard::Selection);
}
#endif  // QT_CONFIG(clipboard)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 808, as _ZN24QQuickTextControlPrivate15keyReleaseEventEP9QKeyEvent
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::keyReleaseEvent(QKeyEvent *e)
{
    e->ignore();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1289, as _ZN24QQuickTextControlPrivate28sendMouseEventToInputContextEP11QMouseEventRK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControlPrivate::sendMouseEventToInputContext(QMouseEvent *e, const QPointF &pos)
{
#if QT_CONFIG(im)
    Q_Q(QQuickTextControl);

    Q_UNUSED(e);

    if (isPreediting()) {
        QTextLayout *layout = cursor.block().layout();
        int cursorPos = q->hitTest(pos, Qt::FuzzyHit) - cursor.position();

        if (cursorPos >= 0 && cursorPos <= layout->preeditAreaText().size()) {
            if (e->type() == QEvent::MouseButtonRelease) {
                QGuiApplication::inputMethod()->invokeAction(QInputMethod::Click, cursorPos);
            }

            return true;
        }
    }
#else
    Q_UNUSED(e);
    Q_UNUSED(pos);
#endif
    return false;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1794, as _ZNK24QQuickTextControlPrivate12isPreeditingEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(im)
inline bool QQuickTextControlPrivate::isPreediting() const
{
    QTextLayout *layout = cursor.block().layout();
    if (layout && !layout->preeditAreaText().isEmpty())
        return true;

    return false;
}
#endif  // QT_CONFIG(im)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1803, as _ZN24QQuickTextControlPrivate13commitPreeditEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(im)
inline void QQuickTextControlPrivate::commitPreedit()
{
    Q_Q(QQuickTextControl);

    if (!hasImState)
        return;

    QGuiApplication::inputMethod()->commit();

    if (!hasImState)
        return;

    QInputMethodEvent event;
    QCoreApplication::sendEvent(q->parent(), &event);
}
#endif  // QT_CONFIG(im)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1819, as _ZN24QQuickTextControlPrivate13cancelPreeditEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(im)
inline void QQuickTextControlPrivate::cancelPreedit()
{
    Q_Q(QQuickTextControl);

    if (!hasImState)
        return;

    QGuiApplication::inputMethod()->reset();

    QInputMethodEvent event;
    QCoreApplication::sendEvent(q->parent(), &event);
}
#endif  // QT_CONFIG(im)
#endif  // !defined(QT_NO_TEXTCONTROL)
//  -----------------------------------------------------------------------

//  QQuickTextControl *QQuickTextControlPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTextControl *ritual_ZN24QQuickTextControlPrivate6q_funcEv(
    QQuickTextControlPrivate *self) {
  return self->q_func();
}

//  const QQuickTextControl *QQuickTextControlPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextControl *ritual_ZNK24QQuickTextControlPrivate6q_funcEv(
    const QQuickTextControlPrivate *self) {
  return self->q_func();
}

//  QQuickTextControlPrivate::QQuickTextControlPrivate()
extern "C" Q_DECL_EXPORT
QQuickTextControlPrivate *ritual_ZN24QQuickTextControlPrivateC1Ev() {
  return new QQuickTextControlPrivate();
}

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControlPrivate::setCursorPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTextControlPrivate17setCursorPositionERK7QPointF(
    QQuickTextControlPrivate *self,
    const QPointF *pos) {
  self->setCursorPosition(*pos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControlPrivate::setCursorPosition(int pos,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTextControlPrivate17setCursorPositionEiN11QTextCursor8MoveModeE(
    QQuickTextControlPrivate *self,
    int pos,
    QTextCursor::MoveMode mode) {
  self->setCursorPosition(pos, mode);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_CONFIG(clipboard)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControlPrivate::setClipboardSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTextControlPrivate21setClipboardSelectionEv(
    QQuickTextControlPrivate *self) {
  self->setClipboardSelection();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(clipboard)

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControlPrivate::keyReleaseEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTextControlPrivate15keyReleaseEventEP9QKeyEvent(
    QQuickTextControlPrivate *self,
    QKeyEvent *e) {
  self->keyReleaseEvent(e);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(im)
//  bool QQuickTextControlPrivate::sendMouseEventToInputContext(QMouseEvent
//      *event, const QPointF &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickTextControlPrivate28sendMouseEventToInputContextEP11QMouseEventRK7QPointF(
    QQuickTextControlPrivate *self,
    QMouseEvent *event,
    const QPointF *pos) {
  return self->sendMouseEventToInputContext(event, *pos);
}
#endif  // QT_CONFIG(im)
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_CONFIG(im)
#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControlPrivate::isPreediting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickTextControlPrivate12isPreeditingEv(
    const QQuickTextControlPrivate *self) {
  return self->isPreediting();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControlPrivate::commitPreedit()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTextControlPrivate13commitPreeditEv(
    QQuickTextControlPrivate *self) {
  self->commitPreedit();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControlPrivate::cancelPreedit()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickTextControlPrivate13cancelPreeditEv(
    QQuickTextControlPrivate *self) {
  self->cancelPreedit();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(im)
