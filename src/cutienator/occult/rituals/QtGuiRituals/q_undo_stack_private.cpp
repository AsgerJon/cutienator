//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qundostack_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(undostack)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qundostack.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qundostack_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include "qundostack.h"
#if QT_CONFIG(undogroup)
#include "qundogroup.h"
#endif
#include "qundostack_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/util/qundostack.cpp, line 416, as _ZN17QUndoStackPrivate8setIndexEib
#if QT_CONFIG(undostack)
inline void QUndoStackPrivate::setIndex(int idx, bool clean)
{
    Q_Q(QUndoStack);

    bool was_clean = index == clean_index;

    const bool indexChanged = idx != index;
    if (indexChanged) {
        index = idx;
        emit q->indexChanged(index);
    }

    if (ActionState newUndoState{q->canUndo(), q->undoText()};
        indexChanged || newUndoState != undoActionState) {
        undoActionState = std::move(newUndoState);
        emit q->canUndoChanged(undoActionState.enabled);
        emit q->undoTextChanged(undoActionState.text);
    }

    if (ActionState newRedoState{q->canRedo(), q->redoText()};
        indexChanged || newRedoState != redoActionState) {
        redoActionState = std::move(newRedoState);
        emit q->canRedoChanged(redoActionState.enabled);
        emit q->redoTextChanged(redoActionState.text);
    }

    if (clean)
        clean_index = index;

    bool is_clean = index == clean_index;
    if (is_clean != was_clean)
        emit q->cleanChanged(is_clean);
}
#endif  // QT_CONFIG(undostack)

//  from src/gui/util/qundostack.cpp, line 457, as _ZN17QUndoStackPrivate14checkUndoLimitEv
#if QT_CONFIG(undostack)
inline bool QUndoStackPrivate::checkUndoLimit()
{
    if (undo_limit <= 0 || !macro_stack.isEmpty() || undo_limit >= command_list.size())
        return false;

    int del_count = command_list.size() - undo_limit;

    for (int i = 0; i < del_count; ++i)
        delete command_list.takeFirst();

    index -= del_count;
    if (clean_index != -1) {
        if (clean_index < del_count)
            clean_index = -1; // we've deleted the clean command
        else
            clean_index -= del_count;
    }

    return true;
}
#endif  // QT_CONFIG(undostack)

//  from src/gui/util/qundostack.cpp, line 1020, as _ZN17QUndoStackPrivate15setPrefixedTextEP7QActionRK7QStringS4_S4_
#if QT_CONFIG(undostack)
#if !defined(QT_NO_ACTION)
inline void QUndoStackPrivate::setPrefixedText(QAction *action, const QString &prefix, const QString &defaultText, const QString &text)
{
    if (defaultText.isEmpty()) {
        QString s = prefix;
        if (!prefix.isEmpty() && !text.isEmpty())
            s.append(u' ');
        s.append(text);
        action->setText(s);
    } else {
        if (text.isEmpty())
            action->setText(defaultText);
        else
            action->setText(prefix.arg(text));
    }
};

/*!
    Creates an undo QAction object with the given \a parent.

    Triggering this action will cause a call to undo(). The text of this action
    is the text of the command which will be undone in the next call to undo(),
    prefixed by the specified \a prefix. If there is no command available for undo,
    this action will be disabled.

    If \a prefix is empty, the default template "Undo %1" is used instead of prefix.
    Before Qt 4.8, the prefix "Undo" was used by default.

    \sa createRedoAction(), canUndo(), QUndoCommand::text()
*/

QAction *QUndoStack::createUndoAction(QObject *parent, const QString &prefix) const
{
    QAction *action = new QAction(parent);
    action->setEnabled(canUndo());

    QString effectivePrefix = prefix;
    QString defaultText;
    if (prefix.isEmpty()) {
        effectivePrefix = tr("Undo %1");
        defaultText = tr("Undo", "Default text for undo action");
    }

    QUndoStackPrivate::setPrefixedText(action, effectivePrefix, defaultText, undoText());

    connect(this, &QUndoStack::canUndoChanged, action, &QAction::setEnabled);
    connect(this, &QUndoStack::undoTextChanged, action, [=](const QString &text) {
        QUndoStackPrivate::setPrefixedText(action, effectivePrefix, defaultText, text);
    });
    connect(action, &QAction::triggered, this, &QUndoStack::undo);

    return action;
}
#endif  // !defined(QT_NO_ACTION)
#endif  // QT_CONFIG(undostack)
//  -----------------------------------------------------------------------

//  QUndoStack *QUndoStackPrivate::q_func()
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZN17QUndoStackPrivate6q_funcEv(QUndoStackPrivate *self) {
  return self->q_func();
}

//  const QUndoStack *QUndoStackPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QUndoStack *ritual_ZNK17QUndoStackPrivate6q_funcEv(
    const QUndoStackPrivate *self) {
  return self->q_func();
}

//  QUndoStackPrivate::QUndoStackPrivate()
extern "C" Q_DECL_EXPORT
QUndoStackPrivate *ritual_ZN17QUndoStackPrivateC1Ev() {
  return new QUndoStackPrivate();
}

#if QT_CONFIG(undostack)
//  void QUndoStackPrivate::setIndex(int idx, bool clean)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QUndoStackPrivate8setIndexEib(
    QUndoStackPrivate *self,
    int idx,
    bool clean) {
  self->setIndex(idx, clean);
}
#endif  // QT_CONFIG(undostack)

#if QT_CONFIG(undostack)
//  bool QUndoStackPrivate::checkUndoLimit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QUndoStackPrivate14checkUndoLimitEv(
    QUndoStackPrivate *self) {
  return self->checkUndoLimit();
}
#endif  // QT_CONFIG(undostack)

#if !defined(QT_NO_ACTION)
#if QT_CONFIG(undostack)
//  void QUndoStackPrivate::setPrefixedText(QAction *action, const QString
//      &prefix, const QString &defaultText, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QUndoStackPrivate15setPrefixedTextEP7QActionRK7QStringS4_S4_(
    QAction *action,
    const QString *prefix,
    const QString *defaultText,
    const QString *text) {
  QUndoStackPrivate::setPrefixedText(action, *prefix, *defaultText, *text);
}
#endif  // QT_CONFIG(undostack)
#endif  // !defined(QT_NO_ACTION)

#endif  // QT_CONFIG(undostack)
