//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicktextcontrol_p.h"
#include "qquicktextcontrol_p_p.h"
#ifndef QT_NO_TEXTCONTROL
#include <qcoreapplication.h>
#include <qfont.h>
#include <qfontmetrics.h>
#include <qevent.h>
#include <qdebug.h>
#include <qclipboard.h>
#include <qtimer.h>
#include <qinputmethod.h>
#include "private/qtextdocumentlayout_p.h"
#include "private/qabstracttextdocumentlayout_p.h"
#include "qtextdocument.h"
#include "private/qtextdocument_p.h"
#include "qtextlist.h"
#include "qtextdocumentwriter.h"
#include "private/qtextcursor_p.h"
#include <QtCore/qloggingcategory.h>
#include <qtextformat.h>
#include <qtransform.h>
#include <qdatetime.h>
#include <qbuffer.h>
#include <qguiapplication.h>
#include <limits.h>
#include <qtexttable.h>
#include <qvariant.h>
#include <qurl.h>
#include <qstylehints.h>
#include <qmetaobject.h>
#include <private/qqmlglobal_p.h>
#include <private/qquickdeliveryagent_p_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
