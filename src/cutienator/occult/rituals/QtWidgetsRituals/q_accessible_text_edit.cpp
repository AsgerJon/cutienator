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

using namespace Qt::StringLiterals;

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 735, as local:qaccessiblewidgets.cpp:AttributeFormatterRef
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
namespace {
class AttributeFormatterRef {
    QString &string;
    const char *key;
    friend class AttributeFormatter;
    AttributeFormatterRef(QString &string, const char *key) : string(string), key(key) {}
public:
    template <typename RHS>
    void operator=(RHS &&rhs)
    { string += QLatin1StringView(key) + u':' + std::forward<RHS>(rhs) + u';'; }
};
}  // namespace
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 201, as _ZNK19QAccessibleTextEdit8textEditEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
inline QTextEdit *QAccessibleTextEdit::textEdit() const
{
    return static_cast<QTextEdit *>(widget());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  Only a class built on QAccessibleTextEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAccessibleTextEdit : QAccessibleTextEdit {
  using QAccessibleTextEdit::scrollBarPosition;
  using QAccessibleTextEdit::textCursor;
  using QAccessibleTextEdit::setTextCursor;
  using QAccessibleTextEdit::textDocument;
  using QAccessibleTextEdit::viewport;
};

//  A QAccessibleTextEdit that Python can take functions over in. Every QAccessibleTextEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef QString * (*CuteQAccessibleTextEditCall0)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessibleTextEditCall1)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QAccessible::State * (*CuteQAccessibleTextEditCall2)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessibleTextEditCall3)(const void *, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessibleTextEditCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QPoint * (*CuteQAccessibleTextEditCall5)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef const QTextCursor * (*CuteQAccessibleTextEditCall6)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void (*CuteQAccessibleTextEditCall7)(const void *, const QTextCursor *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessibleTextEditCall8)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
typedef void * (*CuteQAccessibleTextEditCall9)(const void *, int *);
#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextEditCall10)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall11)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall12)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall13)(const void *, int, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextEditCall14)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall15)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef QString * (*CuteQAccessibleTextEditCall16)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextEditCall17)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QRect * (*CuteQAccessibleTextEditCall18)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextEditCall19)(const void *, const QPoint *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall20)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall21)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextEditCall22)(const void *, int, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleTextEditCall23)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTextEditCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextEditCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextEditCall26)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextEditCall27)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextEditCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleTextEditCall29)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextEditCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextEditCall31)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextEditCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTextEditCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTextEditCall34)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextEditCall35)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextEditCall36)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextEditCall37)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextEditCall38)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextEditCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextEditCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTextEdit : public QAccessibleTextEdit {
public:
  using QAccessibleTextEdit::QAccessibleTextEdit;
  void *taken[41] = {};

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
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[38] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[39] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[40] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#if QT_CONFIG(textedit)
  //  QString QAccessibleTextEdit::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTextEditCall0 call = reinterpret_cast<CuteQAccessibleTextEditCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTextEditCall1 call = reinterpret_cast<CuteQAccessibleTextEditCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTextEditCall2 call = reinterpret_cast<CuteQAccessibleTextEditCall2>(taken[2]);
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
  //  void *QAccessibleTextEdit::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTextEditCall3 call = reinterpret_cast<CuteQAccessibleTextEditCall3>(taken[3]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleTextEdit::interface_cast(t);
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
      CuteQAccessibleTextEditCall4 call = reinterpret_cast<CuteQAccessibleTextEditCall4>(taken[4]);
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
      CuteQAccessibleTextEditCall5 call = reinterpret_cast<CuteQAccessibleTextEditCall5>(taken[5]);
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
      CuteQAccessibleTextEditCall6 call = reinterpret_cast<CuteQAccessibleTextEditCall6>(taken[6]);
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
      CuteQAccessibleTextEditCall7 call = reinterpret_cast<CuteQAccessibleTextEditCall7>(taken[7]);
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
      CuteQAccessibleTextEditCall8 call = reinterpret_cast<CuteQAccessibleTextEditCall8>(taken[8]);
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
      CuteQAccessibleTextEditCall9 call = reinterpret_cast<CuteQAccessibleTextEditCall9>(taken[9]);
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
      CuteQAccessibleTextEditCall10 call = reinterpret_cast<CuteQAccessibleTextEditCall10>(taken[10]);
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
      CuteQAccessibleTextEditCall11 call = reinterpret_cast<CuteQAccessibleTextEditCall11>(taken[11]);
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
      CuteQAccessibleTextEditCall12 call = reinterpret_cast<CuteQAccessibleTextEditCall12>(taken[12]);
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
      CuteQAccessibleTextEditCall13 call = reinterpret_cast<CuteQAccessibleTextEditCall13>(taken[13]);
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
      CuteQAccessibleTextEditCall14 call = reinterpret_cast<CuteQAccessibleTextEditCall14>(taken[14]);
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
      CuteQAccessibleTextEditCall15 call = reinterpret_cast<CuteQAccessibleTextEditCall15>(taken[15]);
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
      CuteQAccessibleTextEditCall16 call = reinterpret_cast<CuteQAccessibleTextEditCall16>(taken[16]);
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
      CuteQAccessibleTextEditCall17 call = reinterpret_cast<CuteQAccessibleTextEditCall17>(taken[17]);
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
      CuteQAccessibleTextEditCall18 call = reinterpret_cast<CuteQAccessibleTextEditCall18>(taken[18]);
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
      CuteQAccessibleTextEditCall19 call = reinterpret_cast<CuteQAccessibleTextEditCall19>(taken[19]);
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
      CuteQAccessibleTextEditCall20 call = reinterpret_cast<CuteQAccessibleTextEditCall20>(taken[20]);
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
      CuteQAccessibleTextEditCall21 call = reinterpret_cast<CuteQAccessibleTextEditCall21>(taken[21]);
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
      CuteQAccessibleTextEditCall22 call = reinterpret_cast<CuteQAccessibleTextEditCall22>(taken[22]);
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
      CuteQAccessibleTextEditCall23 call = reinterpret_cast<CuteQAccessibleTextEditCall23>(taken[23]);
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
      CuteQAccessibleTextEditCall24 call = reinterpret_cast<CuteQAccessibleTextEditCall24>(taken[24]);
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
      CuteQAccessibleTextEditCall25 call = reinterpret_cast<CuteQAccessibleTextEditCall25>(taken[25]);
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
      CuteQAccessibleTextEditCall26 call = reinterpret_cast<CuteQAccessibleTextEditCall26>(taken[26]);
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
      CuteQAccessibleTextEditCall27 call = reinterpret_cast<CuteQAccessibleTextEditCall27>(taken[27]);
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
      CuteQAccessibleTextEditCall28 call = reinterpret_cast<CuteQAccessibleTextEditCall28>(taken[28]);
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
      CuteQAccessibleTextEditCall29 call = reinterpret_cast<CuteQAccessibleTextEditCall29>(taken[29]);
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
      CuteQAccessibleTextEditCall30 call = reinterpret_cast<CuteQAccessibleTextEditCall30>(taken[30]);
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
      CuteQAccessibleTextEditCall31 call = reinterpret_cast<CuteQAccessibleTextEditCall31>(taken[31]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleTextEditCall32 call = reinterpret_cast<CuteQAccessibleTextEditCall32>(taken[32]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleTextEditCall33 call = reinterpret_cast<CuteQAccessibleTextEditCall33>(taken[33]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleTextEditCall34 call = reinterpret_cast<CuteQAccessibleTextEditCall34>(taken[34]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleTextEditCall35 call = reinterpret_cast<CuteQAccessibleTextEditCall35>(taken[35]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleTextEditCall36 call = reinterpret_cast<CuteQAccessibleTextEditCall36>(taken[36]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleTextEditCall37 call = reinterpret_cast<CuteQAccessibleTextEditCall37>(taken[37]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAccessibleTextEditCall38 call = reinterpret_cast<CuteQAccessibleTextEditCall38>(taken[38]);
      call(this, id, data, &handled);
      if (handled) return;
    }
    QAccessibleInterface::virtual_hook(id, data);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQAccessibleTextEditCall39 call = reinterpret_cast<CuteQAccessibleTextEditCall39>(taken[39]);
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
    if (taken[40]) {
      int handled = 0;
      CuteQAccessibleTextEditCall40 call = reinterpret_cast<CuteQAccessibleTextEditCall40>(taken[40]);
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

//  QString QAccessibleTextEdit::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleTextEdit4textEN11QAccessible4TextE(
    const QAccessibleTextEdit *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessibleTextEdit::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleTextEdit7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTextEdit *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessible::State QAccessibleTextEdit::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK19QAccessibleTextEdit5stateEv(
    const QAccessibleTextEdit *self) {
  return new QAccessible::State(self->state());
}

//  void *QAccessibleTextEdit::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QAccessibleTextEdit14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleTextEdit *self,
    QAccessible::InterfaceType t) {
  return self->interface_cast(t);
}

//  void QAccessibleTextEdit::scrollToSubstring(int startIndex, int endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleTextEdit17scrollToSubstringEii(
    QAccessibleTextEdit *self,
    int startIndex,
    int endIndex) {
  self->scrollToSubstring(startIndex, endIndex);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QTextEdit *QAccessibleTextEdit::textEdit() const
extern "C" Q_DECL_EXPORT
QTextEdit *ritual_ZNK19QAccessibleTextEdit8textEditEv(
    const QAccessibleTextEdit *self) {
  return self->textEdit();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  QPoint QAccessibleTextEdit::scrollBarPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QAccessibleTextEdit17scrollBarPositionEv(
    const QAccessibleTextEdit *self) {
  return new QPoint(self->scrollBarPosition());
}

//  QTextCursor QAccessibleTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK19QAccessibleTextEdit10textCursorEv(
    const QAccessibleTextEdit *self) {
  return new QTextCursor(self->textCursor());
}

//  void QAccessibleTextEdit::setTextCursor(const QTextCursor &textCursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleTextEdit13setTextCursorERK11QTextCursor(
    QAccessibleTextEdit *self,
    const QTextCursor *textCursor) {
  self->setTextCursor(*textCursor);
}

//  QTextDocument *QAccessibleTextEdit::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK19QAccessibleTextEdit12textDocumentEv(
    const QAccessibleTextEdit *self) {
  return self->textDocument();
}

//  QWidget *QAccessibleTextEdit::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QAccessibleTextEdit8viewportEv(
    const QAccessibleTextEdit *self) {
  return self->viewport();
}

//  a Python function taken by a CuteQAccessibleTextEdit, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextEdit(
    QAccessibleTextEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextEdit *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QString QAccessibleTextEdit::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAccessibleTextEdit4textEN11QAccessible4TextE(
    const QAccessibleTextEdit *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleTextEdit::text(t));
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void QAccessibleTextEdit::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleTextEdit7setTextEN11QAccessible4TextERK7QString(
    QAccessibleTextEdit *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessibleTextEdit::setText(t, *text);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#if !defined(QT_NO_CURSOR)
//  QAccessible::State QAccessibleTextEdit::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK19QAccessibleTextEdit5stateEv(
    const QAccessibleTextEdit *self) {
  return new QAccessible::State(self->QAccessibleTextEdit::state());
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void *QAccessibleTextEdit::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN19QAccessibleTextEdit14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleTextEdit *self,
    QAccessible::InterfaceType t) {
  return self->QAccessibleTextEdit::interface_cast(t);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void QAccessibleTextEdit::scrollToSubstring(int startIndex, int endIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleTextEdit17scrollToSubstringEii(
    QAccessibleTextEdit *self,
    int startIndex,
    int endIndex) {
  self->QAccessibleTextEdit::scrollToSubstring(startIndex, endIndex);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QPoint QAccessibleTextEdit::scrollBarPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK19QAccessibleTextEdit17scrollBarPositionEv(
    const QAccessibleTextEdit *self) {
  return new QPoint(
      static_cast<const OwnQAccessibleTextEdit *>(self)->OwnQAccessibleTextEdit::scrollBarPosition());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QTextCursor QAccessibleTextEdit::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_own_ZNK19QAccessibleTextEdit10textCursorEv(
    const QAccessibleTextEdit *self) {
  return new QTextCursor(
      static_cast<const OwnQAccessibleTextEdit *>(self)->OwnQAccessibleTextEdit::textCursor());
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  void QAccessibleTextEdit::setTextCursor(const QTextCursor &textCursor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleTextEdit13setTextCursorERK11QTextCursor(
    QAccessibleTextEdit *self,
    const QTextCursor *textCursor) {
  static_cast<OwnQAccessibleTextEdit *>(self)->OwnQAccessibleTextEdit::setTextCursor(
      *textCursor);
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QTextDocument *QAccessibleTextEdit::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_own_ZNK19QAccessibleTextEdit12textDocumentEv(
    const QAccessibleTextEdit *self) {
  return static_cast<const OwnQAccessibleTextEdit *>(self)->OwnQAccessibleTextEdit::textDocument();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
//  QWidget *QAccessibleTextEdit::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK19QAccessibleTextEdit8viewportEv(
    const QAccessibleTextEdit *self) {
  return static_cast<const OwnQAccessibleTextEdit *>(self)->OwnQAccessibleTextEdit::viewport();
}
#endif  // QT_CONFIG(textedit) && !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(textedit)
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
