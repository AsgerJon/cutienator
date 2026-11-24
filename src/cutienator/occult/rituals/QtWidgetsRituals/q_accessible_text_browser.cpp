//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qaccessiblewidgets_p.h"
#include "qabstracttextdocumentlayout.h"
#include "qapplication.h"
#include "qclipboard.h"
#include "qtextdocument.h"
#include "qtextobject.h"
#if QT_CONFIG(textedit)
#include "qplaintextedit.h"
#include "qtextedit.h"
#include "private/qtextedit_p.h"
#endif
#include "qtextboundaryfinder.h"
#if QT_CONFIG(scrollbar)
#include "qscrollbar.h"
#endif
#include "qdebug.h"
#include <QApplication>
#if QT_CONFIG(stackedwidget)
#include <QStackedWidget>
#endif
#if QT_CONFIG(toolbox)
#include <QToolBox>
#endif
#if QT_CONFIG(mdiarea)
#include <QMdiArea>
#include <QMdiSubWindow>
#endif
#if QT_CONFIG(dialogbuttonbox)
#include <QDialogButtonBox>
#endif
#include <limits.h>
#if QT_CONFIG(rubberband)
#include <QRubberBand>
#endif
#if QT_CONFIG(textbrowser)
#include <QTextBrowser>
#endif
#if QT_CONFIG(calendarwidget)
#include <QCalendarWidget>
#endif
#if QT_CONFIG(itemviews)
#include <QAbstractItemView>
#endif
#if QT_CONFIG(dockwidget)
#include <QDockWidget>
#include <private/qdockwidget_p.h>
#endif
#if QT_CONFIG(mainwindow)
#include <QMainWindow>
#endif
#include <QFocusFrame>
#if QT_CONFIG(menu)
#include <QMenu>
#endif
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 216, as _ZN19QAccessibleTextEdit13setTextCursorERK11QTextCursor
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void QAccessibleTextEdit::setTextCursor(const QTextCursor &textCursor)
{
    textEdit()->setTextCursor(textCursor);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 264, as _ZN19QAccessibleTextEdit14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void *QAccessibleTextEdit::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::TextInterface)
        return static_cast<QAccessibleTextInterface*>(this);
    else if (t == QAccessible::EditableTextInterface)
        return static_cast<QAccessibleEditableTextInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 273, as _ZN19QAccessibleTextEdit17scrollToSubstringEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void QAccessibleTextEdit::scrollToSubstring(int startIndex, int endIndex)
{
    QTextEdit *edit = textEdit();

    QTextCursor cursor = textCursor();
    cursor.setPosition(startIndex);
    QRect r = edit->cursorRect(cursor);

    cursor.setPosition(endIndex);
    r.setBottomRight(edit->cursorRect(cursor).bottomRight());

    r.moveTo(r.x() + edit->horizontalScrollBar()->value(),
             r.y() + edit->verticalScrollBar()->value());

    // E V I L, but ensureVisible is not public
    if (Q_UNLIKELY(!QMetaObject::invokeMethod(edit, "_q_ensureVisible", Q_ARG(QRectF, r))))
        qWarning("AccessibleTextEdit::scrollToSubstring failed!");
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 242, as _ZN19QAccessibleTextEdit7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void QAccessibleTextEdit::setText(QAccessible::Text t, const QString &text)
{
    if (t != QAccessible::Value) {
        QAccessibleWidgetV2::setText(t, text);
        return;
    }
    if (textEdit()->isReadOnly())
        return;

    textEdit()->setText(text);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 194, as _ZN19QAccessibleTextEditC2EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QAccessibleTextEdit::QAccessibleTextEdit(QWidget *o)
: QAccessibleTextWidget(o, QAccessible::EditableText)
{
    Q_ASSERT(qobject_cast<QTextEdit *>(widget()));
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 1029, as _ZN21QAccessibleTextWidget10deleteTextEii
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::deleteText(int startOffset, int endOffset)
{
    QTextCursor cursor = textCursorForRange(startOffset, endOffset);
    cursor.removeSelectedText();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 1035, as _ZN21QAccessibleTextWidget10insertTextEiRK7QString
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::insertText(int offset, const QString &text)
{
    QTextCursor cursor = textCursor();
    cursor.setPosition(offset);
    cursor.insertText(text);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 1042, as _ZN21QAccessibleTextWidget11replaceTextEiiRK7QString
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::replaceText(int startOffset, int endOffset, const QString &text)
{
    QTextCursor cursor = textCursorForRange(startOffset, endOffset);
    cursor.removeSelectedText();
    cursor.insertText(text);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 987, as _ZN21QAccessibleTextWidget12addSelectionEii
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::addSelection(int startOffset, int endOffset)
{
    setSelection(0, startOffset, endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 1002, as _ZN21QAccessibleTextWidget12setSelectionEiii
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::setSelection(int selectionIndex, int startOffset, int endOffset)
{
    if (selectionIndex != 0)
        return;

    QTextCursor cursor = textCursor();
    cursor.setPosition(startOffset, QTextCursor::MoveAnchor);
    cursor.setPosition(endOffset, QTextCursor::KeepAnchor);
    setTextCursor(cursor);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 992, as _ZN21QAccessibleTextWidget15removeSelectionEi
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::removeSelection(int selectionIndex)
{
    if (selectionIndex != 0)
        return;

    QTextCursor cursor = textCursor();
    cursor.clearSelection();
    setTextCursor(cursor);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 980, as _ZN21QAccessibleTextWidget17setCursorPositionEi
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::setCursorPosition(int position)
{
    QTextCursor cursor = textCursor();
    cursor.setPosition(position);
    setTextCursor(cursor);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 206, as _ZNK19QAccessibleTextEdit10textCursorEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QTextCursor QAccessibleTextEdit::textCursor() const
{
    return textEdit()->textCursor();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 211, as _ZNK19QAccessibleTextEdit12textDocumentEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QTextDocument *QAccessibleTextEdit::textDocument() const
{
    return textEdit()->document();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 226, as _ZNK19QAccessibleTextEdit17scrollBarPositionEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QPoint QAccessibleTextEdit::scrollBarPosition() const
{
    QPoint result;
    result.setX(textEdit()->horizontalScrollBar() ? textEdit()->horizontalScrollBar()->sliderPosition() : 0);
    result.setY(textEdit()->verticalScrollBar() ? textEdit()->verticalScrollBar()->sliderPosition() : 0);
    return result;
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 234, as _ZNK19QAccessibleTextEdit4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QString QAccessibleTextEdit::text(QAccessible::Text t) const
{
    if (t == QAccessible::Value)
        return textEdit()->toPlainText();

    return QAccessibleWidgetV2::text(t);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 254, as _ZNK19QAccessibleTextEdit5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QAccessible::State QAccessibleTextEdit::state() const
{
    QAccessible::State st = QAccessibleTextWidget::state();
    if (textEdit()->isReadOnly())
        st.readOnly = true;
    else
        st.editable = true;
    return st;
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 221, as _ZNK19QAccessibleTextEdit8viewportEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QWidget *QAccessibleTextEdit::viewport() const
{
    return textEdit()->viewport();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 973, as _ZNK21QAccessibleTextWidget12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QString QAccessibleTextWidget::textAtOffset(int offset, QAccessible::TextBoundaryType boundaryType,
                                            int *startOffset, int *endOffset) const
{
    return qt_accTextAtOffsetHelper(*this, textCursor(), offset, boundaryType, startOffset,
                                    endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 667, as _ZNK21QAccessibleTextWidget13characterRectEi
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QRect QAccessibleTextWidget::characterRect(int offset) const
{
    QTextBlock block = textDocument()->findBlock(offset);
    if (!block.isValid())
        return QRect();

    QTextLayout *layout = block.layout();
    QPointF layoutPosition = layout->position();
    int relativeOffset = offset - block.position();
    QTextLine line = layout->lineForTextPosition(relativeOffset);

    QRect r;

    if (line.isValid()) {
        qreal x = line.cursorToX(relativeOffset);

        QTextCharFormat format;
        QTextBlock::iterator iter = block.begin();
        if (iter.atEnd())
            format = block.charFormat();
        else {
            while (!iter.atEnd() && !iter.fragment().contains(offset))
                ++iter;
            if (iter.atEnd()) // newline should have same format as preceding character
                --iter;
            format = iter.fragment().charFormat();
        }

        QFontMetrics fm(format.font());
        const QString ch = text(offset, offset + 1);
        if (!ch.isEmpty()) {
            int w = fm.horizontalAdvance(ch);
            int h = fm.height();
            r = QRect(layoutPosition.x() + x, layoutPosition.y() + line.y() + line.ascent() + fm.descent() - h,
                      w, h);
            r.moveTo(viewport()->mapToGlobal(r.topLeft()));
        }
        r.translate(-scrollBarPosition());
    }

    return r;
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 710, as _ZNK21QAccessibleTextWidget13offsetAtPointERK6QPoint
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline int QAccessibleTextWidget::offsetAtPoint(const QPoint &point) const
{
    QPoint p = viewport()->mapFromGlobal(point);
    // convert to document coordinates
    p += scrollBarPosition();
    return textDocument()->documentLayout()->hitTest(p, Qt::ExactHit);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 1013, as _ZNK21QAccessibleTextWidget14characterCountEv
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline int QAccessibleTextWidget::characterCount() const
{
    QTextCursor cursor = textCursor();
    cursor.movePosition(QTextCursor::End);
    return cursor.position();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 926, as _ZNK21QAccessibleTextWidget14cursorPositionEv
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline int QAccessibleTextWidget::cursorPosition() const
{
    return textCursor().position();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 718, as _ZNK21QAccessibleTextWidget14selectionCountEv
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline int QAccessibleTextWidget::selectionCount() const
{
    return textCursor().hasSelection() ? 1 : 0;
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 966, as _ZNK21QAccessibleTextWidget15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QString QAccessibleTextWidget::textAfterOffset(int offset, QAccessible::TextBoundaryType boundaryType,
                                              int *startOffset, int *endOffset) const
{
    return qt_accTextAfterOffsetHelper(*this, textCursor(), offset, boundaryType, startOffset,
                                       endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 959, as _ZNK21QAccessibleTextWidget16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QString QAccessibleTextWidget::textBeforeOffset(int offset, QAccessible::TextBoundaryType boundaryType,
                                                int *startOffset, int *endOffset) const
{
    return qt_accTextBeforeOffsetHelper(*this, textCursor(), offset, boundaryType, startOffset,
                                        endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 943, as _ZNK21QAccessibleTextWidget4textEii
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QString QAccessibleTextWidget::text(int startOffset, int endOffset) const
{
    QTextCursor cursor(textCursor());

    cursor.setPosition(startOffset, QTextCursor::MoveAnchor);
    cursor.setPosition(endOffset, QTextCursor::KeepAnchor);

    return cursor.selectedText().replace(QChar(QChar::ParagraphSeparator), u'\n');
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 931, as _ZNK21QAccessibleTextWidget9selectionEiPiS0_
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline void QAccessibleTextWidget::selection(int selectionIndex, int *startOffset, int *endOffset) const
{
    *startOffset = *endOffset = 0;
    QTextCursor cursor = textCursor();

    if (selectionIndex != 0 || !cursor.hasSelection())
        return;

    *startOffset = cursor.selectionStart();
    *endOffset = cursor.selectionEnd();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 496, as _ZNK22QAccessibleTextBrowser4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
inline QAccessible::Role QAccessibleTextBrowser::role() const
{
    return QAccessible::StaticText;
}
#endif  // QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleTextBrowser that Python can take functions over in. Every QAccessibleTextBrowser
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextBrowserCall0)(const void *, int *);
#endif  // QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef QString * (*CuteQAccessibleTextBrowserCall1)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessibleTextBrowserCall2)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QAccessible::State * (*CuteQAccessibleTextBrowserCall3)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessibleTextBrowserCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QPoint * (*CuteQAccessibleTextBrowserCall5)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QTextCursor * (*CuteQAccessibleTextBrowserCall6)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessibleTextBrowserCall7)(const void *, const QTextCursor *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessibleTextBrowserCall8)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessibleTextBrowserCall9)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextBrowserCall10)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall11)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall12)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall13)(const void *, int, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextBrowserCall14)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall15)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef QString * (*CuteQAccessibleTextBrowserCall16)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextBrowserCall17)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QRect * (*CuteQAccessibleTextBrowserCall18)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextBrowserCall19)(const void *, const QPoint *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall20)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall21)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextBrowserCall22)(const void *, int, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleTextBrowserCall23)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTextBrowserCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextBrowserCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextBrowserCall26)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextBrowserCall27)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextBrowserCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleTextBrowserCall29)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextBrowserCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextBrowserCall31)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTextBrowserCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTextBrowserCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextBrowserCall34)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextBrowserCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextBrowserCall36)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextBrowserCall37)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextBrowserCall38)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTextBrowser : public QAccessibleTextBrowser {
public:
  using QAccessibleTextBrowser::QAccessibleTextBrowser;
  void *taken[39] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget17scrollBarPositionEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget10textCursorEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN21QAccessibleTextWidget13setTextCursorERK11QTextCursor")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget12textDocumentEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget8viewportEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
  //  QAccessible::Role QAccessibleTextBrowser::role() const
  QAccessible::Role role() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall0 call = reinterpret_cast<CuteQAccessibleTextBrowserCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleTextBrowser::role();
  }
#endif  // QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QString QAccessibleTextEdit::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall1 call = reinterpret_cast<CuteQAccessibleTextBrowserCall1>(taken[1]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleTextEdit::text(t);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  void QAccessibleTextEdit::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall2 call = reinterpret_cast<CuteQAccessibleTextBrowserCall2>(taken[2]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleTextEdit::setText(t, text);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QAccessible::State QAccessibleTextEdit::state() const
  QAccessible::State state() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall3 call = reinterpret_cast<CuteQAccessibleTextBrowserCall3>(taken[3]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleTextEdit::state();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  void QAccessibleTextEdit::scrollToSubstring(int startIndex, int
  //      endIndex)
  void scrollToSubstring(int startIndex, int endIndex) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall4 call = reinterpret_cast<CuteQAccessibleTextBrowserCall4>(taken[4]);
      call(this, startIndex, endIndex, &handled);
      if (handled) return;
    }
    QAccessibleTextEdit::scrollToSubstring(startIndex, endIndex);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QPoint QAccessibleTextEdit::scrollBarPosition() const
  QPoint scrollBarPosition() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall5 call = reinterpret_cast<CuteQAccessibleTextBrowserCall5>(taken[5]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleTextEdit::scrollBarPosition();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QTextCursor QAccessibleTextEdit::textCursor() const
  QTextCursor textCursor() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall6 call = reinterpret_cast<CuteQAccessibleTextBrowserCall6>(taken[6]);
      const QTextCursor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleTextEdit::textCursor();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  void QAccessibleTextEdit::setTextCursor(const QTextCursor
  //      &textCursor)
  void setTextCursor(const QTextCursor &textCursor) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall7 call = reinterpret_cast<CuteQAccessibleTextBrowserCall7>(taken[7]);
      call(this, &textCursor, &handled);
      if (handled) return;
    }
    QAccessibleTextEdit::setTextCursor(textCursor);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QTextDocument *QAccessibleTextEdit::textDocument() const
  QTextDocument *textDocument() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall8 call = reinterpret_cast<CuteQAccessibleTextBrowserCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTextDocument *>(given);
    }
    return QAccessibleTextEdit::textDocument();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QWidget *QAccessibleTextEdit::viewport() const
  QWidget *viewport() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall9 call = reinterpret_cast<CuteQAccessibleTextBrowserCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAccessibleTextEdit::viewport();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  int QAccessibleTextWidget::selectionCount() const
  int selectionCount() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall10 call = reinterpret_cast<CuteQAccessibleTextBrowserCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTextWidget::selectionCount();
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::addSelection(int startOffset, int
  //      endOffset)
  void addSelection(int startOffset, int endOffset) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall11 call = reinterpret_cast<CuteQAccessibleTextBrowserCall11>(taken[11]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::addSelection(startOffset, endOffset);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::removeSelection(int selectionIndex)
  void removeSelection(int selectionIndex) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall12 call = reinterpret_cast<CuteQAccessibleTextBrowserCall12>(taken[12]);
      call(this, selectionIndex, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::removeSelection(selectionIndex);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::setSelection(int selectionIndex, int
  //      startOffset, int endOffset)
  void setSelection(
      int selectionIndex,
      int startOffset,
      int endOffset) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall13 call = reinterpret_cast<CuteQAccessibleTextBrowserCall13>(taken[13]);
      call(this, selectionIndex, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::setSelection(selectionIndex, startOffset, endOffset);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  int QAccessibleTextWidget::cursorPosition() const
  int cursorPosition() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall14 call = reinterpret_cast<CuteQAccessibleTextBrowserCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTextWidget::cursorPosition();
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::setCursorPosition(int position)
  void setCursorPosition(int position) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall15 call = reinterpret_cast<CuteQAccessibleTextBrowserCall15>(taken[15]);
      call(this, position, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::setCursorPosition(position);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  QString QAccessibleTextWidget::text(int startOffset, int endOffset)
  //      const
  QString text(int startOffset, int endOffset) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall16 call = reinterpret_cast<CuteQAccessibleTextBrowserCall16>(taken[16]);
      QString * given = call(this, startOffset, endOffset, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleTextWidget::text(startOffset, endOffset);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  int QAccessibleTextWidget::characterCount() const
  int characterCount() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall17 call = reinterpret_cast<CuteQAccessibleTextBrowserCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTextWidget::characterCount();
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  QRect QAccessibleTextWidget::characterRect(int offset) const
  QRect characterRect(int offset) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall18 call = reinterpret_cast<CuteQAccessibleTextBrowserCall18>(taken[18]);
      const QRect * given = call(this, offset, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleTextWidget::characterRect(offset);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  int QAccessibleTextWidget::offsetAtPoint(const QPoint &point) const
  int offsetAtPoint(const QPoint &point) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall19 call = reinterpret_cast<CuteQAccessibleTextBrowserCall19>(taken[19]);
      int given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QAccessibleTextWidget::offsetAtPoint(point);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::deleteText(int startOffset, int
  //      endOffset)
  void deleteText(int startOffset, int endOffset) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall20 call = reinterpret_cast<CuteQAccessibleTextBrowserCall20>(taken[20]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::deleteText(startOffset, endOffset);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::insertText(int offset, const QString
  //      &text)
  void insertText(int offset, const QString &text) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall21 call = reinterpret_cast<CuteQAccessibleTextBrowserCall21>(taken[21]);
      call(this, offset, &text, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::insertText(offset, text);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::replaceText(int startOffset, int
  //      endOffset, const QString &text)
  void replaceText(
      int startOffset,
      int endOffset,
      const QString &text) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall22 call = reinterpret_cast<CuteQAccessibleTextBrowserCall22>(taken[22]);
      call(this, startOffset, endOffset, &text, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::replaceText(startOffset, endOffset, text);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall23 call = reinterpret_cast<CuteQAccessibleTextBrowserCall23>(taken[23]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall24 call = reinterpret_cast<CuteQAccessibleTextBrowserCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall25 call = reinterpret_cast<CuteQAccessibleTextBrowserCall25>(taken[25]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall26 call = reinterpret_cast<CuteQAccessibleTextBrowserCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall27 call = reinterpret_cast<CuteQAccessibleTextBrowserCall27>(taken[27]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall28 call = reinterpret_cast<CuteQAccessibleTextBrowserCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall29 call = reinterpret_cast<CuteQAccessibleTextBrowserCall29>(taken[29]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall30 call = reinterpret_cast<CuteQAccessibleTextBrowserCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall31 call = reinterpret_cast<CuteQAccessibleTextBrowserCall31>(taken[31]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall32 call = reinterpret_cast<CuteQAccessibleTextBrowserCall32>(taken[32]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall33 call = reinterpret_cast<CuteQAccessibleTextBrowserCall33>(taken[33]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall34 call = reinterpret_cast<CuteQAccessibleTextBrowserCall34>(taken[34]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall35 call = reinterpret_cast<CuteQAccessibleTextBrowserCall35>(taken[35]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall36 call = reinterpret_cast<CuteQAccessibleTextBrowserCall36>(taken[36]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall37 call = reinterpret_cast<CuteQAccessibleTextBrowserCall37>(taken[37]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionName(name);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionDescription(const
  //      QString &name) const
  QString localizedActionDescription(const QString &name) const override {
    if (taken[38]) {
      int handled = 0;
      CuteQAccessibleTextBrowserCall38 call = reinterpret_cast<CuteQAccessibleTextBrowserCall38>(taken[38]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleActionInterface::localizedActionDescription(name);
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessible::Role QAccessibleTextBrowser::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK22QAccessibleTextBrowser4roleEv(
    const QAccessibleTextBrowser *self) {
  return self->role();
}

//  a Python function taken by a CuteQAccessibleTextBrowser, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextBrowser(
    QAccessibleTextBrowser *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextBrowser *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
//  QAccessible::Role QAccessibleTextBrowser::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK22QAccessibleTextBrowser4roleEv(
    const QAccessibleTextBrowser *self) {
  return self->QAccessibleTextBrowser::role();
}
#endif  // QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(textbrowser) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
