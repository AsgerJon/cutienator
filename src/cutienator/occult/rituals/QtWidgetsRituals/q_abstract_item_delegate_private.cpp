//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractitemdelegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractitemdelegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtWidgets/qabstractitemview.h>
#include <QtGui/qfontmetrics.h>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(textedit)
#include <QtWidgets/qtextedit.h>
#include <QtWidgets/qplaintextedit.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtGui/qvalidator.h>
#include <QtCore/qjsonvalue.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtWidgets/private/qabstractitemdelegate_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qpa/qplatformdrag.h>
#include <QtGui/private/qdnd_p.h>
#endif
#include <QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qabstractitemdelegate.cpp, line 432, as local:qabstractitemdelegate.cpp:editorHandlesKeyEvent
static bool editorHandlesKeyEvent(QWidget *editor, const QKeyEvent *event)
{
#if QT_CONFIG(textedit)
    // do not filter enter / return / tab / backtab for QTextEdit or QPlainTextEdit
    if (qobject_cast<QTextEdit *>(editor) || qobject_cast<QPlainTextEdit *>(editor)) {
        switch (event->key()) {
        case Qt::Key_Tab:
        case Qt::Key_Backtab:
        case Qt::Key_Enter:
        case Qt::Key_Return:
            return true;

        default:
            break;
        }
    }
#endif // QT_CONFIG(textedit)

    Q_UNUSED(editor);
    Q_UNUSED(event);
    return false;
}

//  from src/widgets/itemviews/qabstractitemdelegate.cpp, line 384, as _ZN28QAbstractItemDelegatePrivateC1Ev
inline QAbstractItemDelegatePrivate::QAbstractItemDelegatePrivate()
    : QObjectPrivate()
{
}

//  from src/widgets/itemviews/qabstractitemdelegate.cpp, line 455, as _ZN28QAbstractItemDelegatePrivate17handleEditorEventEP7QObjectP6QEvent
inline bool QAbstractItemDelegatePrivate::handleEditorEvent(QObject *object, QEvent *event)
{
    Q_Q(QAbstractItemDelegate);

    QWidget *editor = qobject_cast<QWidget*>(object);
    if (!editor)
        return false;
    if (event->type() == QEvent::KeyPress) {
        QKeyEvent *keyEvent = static_cast<QKeyEvent *>(event);
        if (editorHandlesKeyEvent(editor, keyEvent))
            return false;

#ifndef QT_NO_SHORTCUT
        if (keyEvent->matches(QKeySequence::Cancel)) {
            // don't commit data
            emit q->closeEditor(editor, QAbstractItemDelegate::RevertModelCache);
            return true;
        }
#endif

        switch (keyEvent->key()) {
        case Qt::Key_Tab:
            if (tryFixup(editor)) {
                emit q->commitData(editor);
                emit q->closeEditor(editor, QAbstractItemDelegate::EditNextItem);
            }
            return true;
        case Qt::Key_Backtab:
            if (tryFixup(editor)) {
                emit q->commitData(editor);
                emit q->closeEditor(editor, QAbstractItemDelegate::EditPreviousItem);
            }
            return true;
        case Qt::Key_Enter:
        case Qt::Key_Return:
            // We want the editor to be able to process the key press
            // before committing the data (e.g. so it can do
            // validation/fixup of the input).
            if (!tryFixup(editor))
                return true;

            QMetaObject::invokeMethod(q, "_q_commitDataAndCloseEditor",
                                      Qt::QueuedConnection, Q_ARG(QWidget*, editor));
            return false;
        default:
            return false;
        }
    } else if (event->type() == QEvent::FocusOut || (event->type() == QEvent::Hide && editor->isWindow())) {
        //the Hide event will take care of he editors that are in fact complete dialogs
        if (!editor->isActiveWindow() || (QApplication::focusWidget() != editor)) {
            QWidget *w = QApplication::focusWidget();
            while (w) { // don't worry about focus changes internally in the editor
                if (w == editor)
                    return false;
                w = w->parentWidget();
            }
#if QT_CONFIG(draganddrop)
            // The window may lose focus during an drag operation.
            // i.e when dragging involves the taskbar on Windows.
            QPlatformDrag *platformDrag = QGuiApplicationPrivate::instance()->platformIntegration()->drag();
            if (platformDrag && platformDrag->currentDrag()) {
                return false;
            }
#endif
            if (tryFixup(editor))
                emit q->commitData(editor);

            // If the application loses focus while editing, then the focus needs to go back
            // to the itemview when the editor closes. This ensures that when the application
            // is active again it will have the focus on the itemview as expected.
            QWidget *editorParent = editor->parentWidget();
            const bool manuallyFixFocus = (event->type() == QEvent::FocusOut) && !editor->hasFocus() &&
                    editorParent &&
                    (static_cast<QFocusEvent *>(event)->reason() == Qt::ActiveWindowFocusReason);
            emit q->closeEditor(editor, QAbstractItemDelegate::NoHint);
            if (manuallyFixFocus)
                editorParent->setFocus();
        }
#ifndef QT_NO_SHORTCUT
    } else if (event->type() == QEvent::ShortcutOverride) {
        if (static_cast<QKeyEvent*>(event)->matches(QKeySequence::Cancel)) {
            event->accept();
            return true;
        }
#endif
    }
    return false;
}

//  from src/widgets/itemviews/qabstractitemdelegate.cpp, line 544, as _ZN28QAbstractItemDelegatePrivate8tryFixupEP7QWidget
inline bool QAbstractItemDelegatePrivate::tryFixup(QWidget *editor)
{
#if QT_CONFIG(lineedit)
    if (QLineEdit *e = qobject_cast<QLineEdit*>(editor)) {
        if (!e->hasAcceptableInput()) {
#if QT_CONFIG(validator)
            if (const QValidator *validator = e->validator()) {
                QString text = e->text();
                validator->fixup(text);
                e->setText(text);
            }
#endif
            return e->hasAcceptableInput();
        }
    }
#endif
#if QT_CONFIG(spinbox)
    // Give a chance to the spinbox to interpret the text and emit
    // the appropriate signals before committing data.
    if (QAbstractSpinBox *sb = qobject_cast<QAbstractSpinBox *>(editor)) {
        if (!sb->keyboardTracking())
            sb->interpretText();
    }
#else
    Q_UNUSED(editor);
#endif // QT_CONFIG(lineedit)

    return true;
}

//  from src/widgets/itemviews/qabstractitemdelegate.cpp, line 574, as _ZNK28QAbstractItemDelegatePrivate11textForRoleEN2Qt12ItemDataRoleERK8QVariantRK7QLocalei
inline QString QAbstractItemDelegatePrivate::textForRole(Qt::ItemDataRole role, const QVariant &value, const QLocale &locale, int precision) const
{
    const QLocale::FormatType formatType = (role == Qt::DisplayRole) ? QLocale::ShortFormat : QLocale::LongFormat;
    QString text;
    switch (value.userType()) {
    case QMetaType::Float:
        text = locale.toString(value.toFloat());
        break;
    case QMetaType::Double:
        text = locale.toString(value.toDouble(), 'g', precision);
        break;
    case QMetaType::Int:
    case QMetaType::LongLong:
        text = locale.toString(value.toLongLong());
        break;
    case QMetaType::UInt:
    case QMetaType::ULongLong:
        text = locale.toString(value.toULongLong());
        break;
    case QMetaType::QDate:
        text = locale.toString(value.toDate(), formatType);
        break;
    case QMetaType::QTime:
        text = locale.toString(value.toTime(), formatType);
        break;
    case QMetaType::QDateTime:
        text = locale.toString(value.toDateTime(), formatType);
        break;
    case QMetaType::QJsonValue: {
        const QJsonValue val = value.toJsonValue();
        if (val.isBool()) {
            text = QVariant(val.toBool()).toString();
            break;
        }
        if (val.isDouble()) {
            text = locale.toString(val.toDouble(), 'g', precision);
            break;
        }
        // val is a string (or null) here
        Q_FALLTHROUGH();
    }
    default: {
        text = value.toString();
        if (role == Qt::DisplayRole)
            text.replace(u'\n', QChar::LineSeparator);
        break;
    }
    }
    return text;
}

//  from src/widgets/itemviews/qabstractitemdelegate.cpp, line 625, as _ZN28QAbstractItemDelegatePrivate27_q_commitDataAndCloseEditorEP7QWidget
inline void QAbstractItemDelegatePrivate::_q_commitDataAndCloseEditor(QWidget *editor)
{
    Q_Q(QAbstractItemDelegate);
    emit q->commitData(editor);
    emit q->closeEditor(editor, QAbstractItemDelegate::SubmitModelCache);
}
//  -----------------------------------------------------------------------

//  QAbstractItemDelegate *QAbstractItemDelegatePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZN28QAbstractItemDelegatePrivate6q_funcEv(
    QAbstractItemDelegatePrivate *self) {
  return self->q_func();
}

//  const QAbstractItemDelegate *QAbstractItemDelegatePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemDelegate *ritual_ZNK28QAbstractItemDelegatePrivate6q_funcEv(
    const QAbstractItemDelegatePrivate *self) {
  return self->q_func();
}

//  QAbstractItemDelegatePrivate::QAbstractItemDelegatePrivate()
extern "C" Q_DECL_EXPORT
QAbstractItemDelegatePrivate *ritual_ZN28QAbstractItemDelegatePrivateC1Ev() {
  return new QAbstractItemDelegatePrivate();
}

//  bool QAbstractItemDelegatePrivate::handleEditorEvent(QObject *object,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QAbstractItemDelegatePrivate17handleEditorEventEP7QObjectP6QEvent(
    QAbstractItemDelegatePrivate *self,
    QObject *object,
    QEvent *event) {
  return self->handleEditorEvent(object, event);
}

//  bool QAbstractItemDelegatePrivate::tryFixup(QWidget *editor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QAbstractItemDelegatePrivate8tryFixupEP7QWidget(
    QAbstractItemDelegatePrivate *self,
    QWidget *editor) {
  return self->tryFixup(editor);
}

//  QString QAbstractItemDelegatePrivate::textForRole(Qt::ItemDataRole role,
//      const QVariant &value, const QLocale &locale, int precision) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QAbstractItemDelegatePrivate11textForRoleEN2Qt12ItemDataRoleERK8QVariantRK7QLocalei(
    const QAbstractItemDelegatePrivate *self,
    Qt::ItemDataRole role,
    const QVariant *value,
    const QLocale *locale,
    int precision) {
  return new QString(self->textForRole(role, *value, *locale, precision));
}

//  void QAbstractItemDelegatePrivate::_q_commitDataAndCloseEditor(QWidget
//      *editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAbstractItemDelegatePrivate27_q_commitDataAndCloseEditorEP7QWidget(
    QAbstractItemDelegatePrivate *self,
    QWidget *editor) {
  self->_q_commitDataAndCloseEditor(editor);
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
