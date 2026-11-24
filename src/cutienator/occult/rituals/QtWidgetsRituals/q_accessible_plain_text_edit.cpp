//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
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
#include <QtWidgets/private/qaccessiblewidgets_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qclipboard.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextobject.h>
#if QT_CONFIG(textedit)
#include <QtWidgets/qplaintextedit.h>
#include <QtWidgets/qtextedit.h>
#include <QtWidgets/private/qtextedit_p.h>
#endif
#include <QtCore/qtextboundaryfinder.h>
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#endif
#include <QtCore/qdebug.h>
#include <QtWidgets/QApplication>
#if QT_CONFIG(stackedwidget)
#include <QtWidgets/QStackedWidget>
#endif
#if QT_CONFIG(toolbox)
#include <QtWidgets/QToolBox>
#endif
#if QT_CONFIG(mdiarea)
#include <QtWidgets/QMdiArea>
#include <QtWidgets/QMdiSubWindow>
#endif
#if QT_CONFIG(dialogbuttonbox)
#include <QtWidgets/QDialogButtonBox>
#endif
#include <limits.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/QRubberBand>
#endif
#if QT_CONFIG(textbrowser)
#include <QtWidgets/QTextBrowser>
#endif
#if QT_CONFIG(calendarwidget)
#include <QtWidgets/QCalendarWidget>
#endif
#if QT_CONFIG(itemviews)
#include <QtWidgets/QAbstractItemView>
#endif
#if QT_CONFIG(dockwidget)
#include <QtWidgets/QDockWidget>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(mainwindow)
#include <QtWidgets/QMainWindow>
#endif
#include <QtWidgets/QFocusFrame>
#if QT_CONFIG(menu)
#include <QtWidgets/QMenu>
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 653, as _ZN21QAccessibleTextWidgetC2EP7QWidgetN11QAccessible4RoleERK7QString
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QAccessibleTextWidget::QAccessibleTextWidget(QWidget *o, QAccessible::Role r, const QString &name)
    : QAccessibleWidgetV2(o, r, name)
{

}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 138, as _ZN24QAccessiblePlainTextEdit14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void *QAccessiblePlainTextEdit::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::TextInterface)
        return static_cast<QAccessibleTextInterface*>(this);
    else if (t == QAccessible::EditableTextInterface)
        return static_cast<QAccessibleEditableTextInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 659, as _ZNK21QAccessibleTextWidget5stateEv
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QAccessible::State QAccessibleTextWidget::state() const
{
    QAccessible::State s = QAccessibleWidgetV2::state();
    s.selectableText = true;
    s.multiLine = true;
    return s;
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 108, as _ZNK24QAccessiblePlainTextEdit4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QString QAccessiblePlainTextEdit::text(QAccessible::Text t) const
{
    if (t == QAccessible::Value)
        return plainTextEdit()->toPlainText();

    return QAccessibleWidgetV2::text(t);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 116, as _ZN24QAccessiblePlainTextEdit7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void QAccessiblePlainTextEdit::setText(QAccessible::Text t, const QString &text)
{
    if (t != QAccessible::Value) {
        QAccessibleWidgetV2::setText(t, text);
        return;
    }
    if (plainTextEdit()->isReadOnly())
        return;

    plainTextEdit()->setPlainText(text);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 128, as _ZNK24QAccessiblePlainTextEdit5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QAccessible::State QAccessiblePlainTextEdit::state() const
{
    QAccessible::State st = QAccessibleTextWidget::state();
    if (plainTextEdit()->isReadOnly())
        st.readOnly = true;
    else
        st.editable = true;
    return st;
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 175, as _ZN24QAccessiblePlainTextEdit17scrollToSubstringEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void QAccessiblePlainTextEdit::scrollToSubstring(int startIndex, int endIndex)
{
    //TODO: Not implemented
    Q_UNUSED(startIndex);
    Q_UNUSED(endIndex);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 103, as _ZNK24QAccessiblePlainTextEdit13plainTextEditEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QPlainTextEdit* QAccessiblePlainTextEdit::plainTextEdit() const
{
    return static_cast<QPlainTextEdit *>(widget());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 147, as _ZNK24QAccessiblePlainTextEdit17scrollBarPositionEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QPoint QAccessiblePlainTextEdit::scrollBarPosition() const
{
    QPoint result;
    result.setX(plainTextEdit()->horizontalScrollBar() ? plainTextEdit()->horizontalScrollBar()->sliderPosition() : 0);
    result.setY(plainTextEdit()->verticalScrollBar() ? plainTextEdit()->verticalScrollBar()->sliderPosition() : 0);
    return result;
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 155, as _ZNK24QAccessiblePlainTextEdit10textCursorEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QTextCursor QAccessiblePlainTextEdit::textCursor() const
{
    return plainTextEdit()->textCursor();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 160, as _ZN24QAccessiblePlainTextEdit13setTextCursorERK11QTextCursor
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline void QAccessiblePlainTextEdit::setTextCursor(const QTextCursor &textCursor)
{
    plainTextEdit()->setTextCursor(textCursor);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 165, as _ZNK24QAccessiblePlainTextEdit12textDocumentEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QTextDocument* QAccessiblePlainTextEdit::textDocument() const
{
    return plainTextEdit()->document();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 170, as _ZNK24QAccessiblePlainTextEdit8viewportEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QWidget* QAccessiblePlainTextEdit::viewport() const
{
    return plainTextEdit()->viewport();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  Only a class built on QAccessiblePlainTextEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAccessiblePlainTextEdit : QAccessiblePlainTextEdit {
  using QAccessiblePlainTextEdit::scrollBarPosition;
  using QAccessiblePlainTextEdit::textCursor;
  using QAccessiblePlainTextEdit::setTextCursor;
  using QAccessiblePlainTextEdit::textDocument;
  using QAccessiblePlainTextEdit::viewport;
};

//  A QAccessiblePlainTextEdit that Python can take functions over in. Every QAccessiblePlainTextEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef QString * (*CuteQAccessiblePlainTextEditCall0)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessiblePlainTextEditCall1)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QAccessible::State * (*CuteQAccessiblePlainTextEditCall2)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessiblePlainTextEditCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QPoint * (*CuteQAccessiblePlainTextEditCall4)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QTextCursor * (*CuteQAccessiblePlainTextEditCall5)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessiblePlainTextEditCall6)(const void *, const QTextCursor *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessiblePlainTextEditCall7)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessiblePlainTextEditCall8)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessiblePlainTextEditCall9)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall10)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall11)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall12)(const void *, int, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessiblePlainTextEditCall13)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall14)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef QString * (*CuteQAccessiblePlainTextEditCall15)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessiblePlainTextEditCall16)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QRect * (*CuteQAccessiblePlainTextEditCall17)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessiblePlainTextEditCall18)(const void *, const QPoint *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall19)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall20)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessiblePlainTextEditCall21)(const void *, int, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessiblePlainTextEditCall22)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessiblePlainTextEditCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePlainTextEditCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessiblePlainTextEditCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessiblePlainTextEditCall26)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePlainTextEditCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessiblePlainTextEditCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePlainTextEditCall29)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePlainTextEditCall30)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessiblePlainTextEditCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessiblePlainTextEditCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessiblePlainTextEditCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessiblePlainTextEditCall34)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePlainTextEditCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessiblePlainTextEditCall36)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessiblePlainTextEditCall37)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessiblePlainTextEditCall38)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessiblePlainTextEdit : public QAccessiblePlainTextEdit {
public:
  using QAccessiblePlainTextEdit::QAccessiblePlainTextEdit;
  void *taken[39] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget17scrollBarPositionEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget10textCursorEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZN21QAccessibleTextWidget13setTextCursorERK11QTextCursor")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget12textDocumentEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget8viewportEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
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
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QString QAccessiblePlainTextEdit::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall0 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall0>(taken[0]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessiblePlainTextEdit::text(t);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  void QAccessiblePlainTextEdit::setText(QAccessible::Text t, const
  //      QString &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall1 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall1>(taken[1]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessiblePlainTextEdit::setText(t, text);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QAccessible::State QAccessiblePlainTextEdit::state() const
  QAccessible::State state() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall2 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall2>(taken[2]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessiblePlainTextEdit::state();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  void QAccessiblePlainTextEdit::scrollToSubstring(int startIndex, int
  //      endIndex)
  void scrollToSubstring(int startIndex, int endIndex) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall3 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall3>(taken[3]);
      call(this, startIndex, endIndex, &handled);
      if (handled) return;
    }
    QAccessiblePlainTextEdit::scrollToSubstring(startIndex, endIndex);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QPoint QAccessiblePlainTextEdit::scrollBarPosition() const
  QPoint scrollBarPosition() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall4 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall4>(taken[4]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessiblePlainTextEdit::scrollBarPosition();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QTextCursor QAccessiblePlainTextEdit::textCursor() const
  QTextCursor textCursor() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall5 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall5>(taken[5]);
      const QTextCursor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessiblePlainTextEdit::textCursor();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  void QAccessiblePlainTextEdit::setTextCursor(const QTextCursor
  //      &textCursor)
  void setTextCursor(const QTextCursor &textCursor) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall6 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall6>(taken[6]);
      call(this, &textCursor, &handled);
      if (handled) return;
    }
    QAccessiblePlainTextEdit::setTextCursor(textCursor);
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QTextDocument *QAccessiblePlainTextEdit::textDocument() const
  QTextDocument *textDocument() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall7 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTextDocument *>(given);
    }
    return QAccessiblePlainTextEdit::textDocument();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QWidget *QAccessiblePlainTextEdit::viewport() const
  QWidget *viewport() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall8 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return QAccessiblePlainTextEdit::viewport();
  }
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  int QAccessibleTextWidget::selectionCount() const
  int selectionCount() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall9 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall10 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall11 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall12 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall13 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall14 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall15 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall16 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall17 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall18 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall19 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall20 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall21 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall22 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall22>(taken[22]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall23 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall24 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall25 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall26 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall26>(taken[26]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall27 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall28 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall28>(taken[28]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall29 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall29>(taken[29]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall30 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall30>(taken[30]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall31 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall31>(taken[31]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessiblePlainTextEditCall32 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall32>(taken[32]);
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
      CuteQAccessiblePlainTextEditCall33 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall33>(taken[33]);
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
      CuteQAccessiblePlainTextEditCall34 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall34>(taken[34]);
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
      CuteQAccessiblePlainTextEditCall35 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall35>(taken[35]);
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
      CuteQAccessiblePlainTextEditCall36 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall36>(taken[36]);
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
      CuteQAccessiblePlainTextEditCall37 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall37>(taken[37]);
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
      CuteQAccessiblePlainTextEditCall38 call = reinterpret_cast<CuteQAccessiblePlainTextEditCall38>(taken[38]);
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

//  QString QAccessiblePlainTextEdit::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessiblePlainTextEdit4textEN11QAccessible4TextE(
    const QAccessiblePlainTextEdit *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessiblePlainTextEdit::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessiblePlainTextEdit7setTextEN11QAccessible4TextERK7QString(
    QAccessiblePlainTextEdit *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessible::State QAccessiblePlainTextEdit::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK24QAccessiblePlainTextEdit5stateEv(
    const QAccessiblePlainTextEdit *self) {
  return new QAccessible::State(self->state());
}

//  void QAccessiblePlainTextEdit::scrollToSubstring(int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessiblePlainTextEdit17scrollToSubstringEii(
    QAccessiblePlainTextEdit *self,
    int startIndex,
    int endIndex) {
  self->scrollToSubstring(startIndex, endIndex);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QPlainTextEdit *QAccessiblePlainTextEdit::plainTextEdit() const
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZNK24QAccessiblePlainTextEdit13plainTextEditEv(
    const QAccessiblePlainTextEdit *self) {
  return self->plainTextEdit();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  QPoint QAccessiblePlainTextEdit::scrollBarPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QAccessiblePlainTextEdit17scrollBarPositionEv(
    const QAccessiblePlainTextEdit *self) {
  return new QPoint(self->scrollBarPosition());
}

//  QTextCursor QAccessiblePlainTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK24QAccessiblePlainTextEdit10textCursorEv(
    const QAccessiblePlainTextEdit *self) {
  return new QTextCursor(self->textCursor());
}

//  void QAccessiblePlainTextEdit::setTextCursor(const QTextCursor
//      &textCursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAccessiblePlainTextEdit13setTextCursorERK11QTextCursor(
    QAccessiblePlainTextEdit *self,
    const QTextCursor *textCursor) {
  self->setTextCursor(*textCursor);
}

//  QTextDocument *QAccessiblePlainTextEdit::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK24QAccessiblePlainTextEdit12textDocumentEv(
    const QAccessiblePlainTextEdit *self) {
  return self->textDocument();
}

//  QWidget *QAccessiblePlainTextEdit::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK24QAccessiblePlainTextEdit8viewportEv(
    const QAccessiblePlainTextEdit *self) {
  return self->viewport();
}

//  a Python function taken by a CuteQAccessiblePlainTextEdit, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessiblePlainTextEdit(
    QAccessiblePlainTextEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessiblePlainTextEdit *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QString QAccessiblePlainTextEdit::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QAccessiblePlainTextEdit4textEN11QAccessible4TextE(
    const QAccessiblePlainTextEdit *self,
    QAccessible::Text t) {
  return new QString(self->QAccessiblePlainTextEdit::text(t));
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void QAccessiblePlainTextEdit::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessiblePlainTextEdit7setTextEN11QAccessible4TextERK7QString(
    QAccessiblePlainTextEdit *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessiblePlainTextEdit::setText(t, *text);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QAccessible::State QAccessiblePlainTextEdit::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK24QAccessiblePlainTextEdit5stateEv(
    const QAccessiblePlainTextEdit *self) {
  return new QAccessible::State(self->QAccessiblePlainTextEdit::state());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void QAccessiblePlainTextEdit::scrollToSubstring(int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessiblePlainTextEdit17scrollToSubstringEii(
    QAccessiblePlainTextEdit *self,
    int startIndex,
    int endIndex) {
  self->QAccessiblePlainTextEdit::scrollToSubstring(startIndex, endIndex);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QPoint QAccessiblePlainTextEdit::scrollBarPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK24QAccessiblePlainTextEdit17scrollBarPositionEv(
    const QAccessiblePlainTextEdit *self) {
  return new QPoint(
      static_cast<const OwnQAccessiblePlainTextEdit *>(self)->OwnQAccessiblePlainTextEdit::scrollBarPosition());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QTextCursor QAccessiblePlainTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_own_ZNK24QAccessiblePlainTextEdit10textCursorEv(
    const QAccessiblePlainTextEdit *self) {
  return new QTextCursor(
      static_cast<const OwnQAccessiblePlainTextEdit *>(self)->OwnQAccessiblePlainTextEdit::textCursor());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void QAccessiblePlainTextEdit::setTextCursor(const QTextCursor
//      &textCursor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAccessiblePlainTextEdit13setTextCursorERK11QTextCursor(
    QAccessiblePlainTextEdit *self,
    const QTextCursor *textCursor) {
  static_cast<OwnQAccessiblePlainTextEdit *>(self)->OwnQAccessiblePlainTextEdit::setTextCursor(
      *textCursor);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QTextDocument *QAccessiblePlainTextEdit::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_own_ZNK24QAccessiblePlainTextEdit12textDocumentEv(
    const QAccessiblePlainTextEdit *self) {
  return static_cast<const OwnQAccessiblePlainTextEdit *>(self)->OwnQAccessiblePlainTextEdit::textDocument();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QWidget *QAccessiblePlainTextEdit::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK24QAccessiblePlainTextEdit8viewportEv(
    const QAccessiblePlainTextEdit *self) {
  return static_cast<const OwnQAccessiblePlainTextEdit *>(self)->OwnQAccessiblePlainTextEdit::viewport();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
