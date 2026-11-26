//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextcursor.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 953, as _ZNK21QAccessibleTextWidget17scrollBarPositionEv
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QPoint QAccessibleTextWidget::scrollBarPosition() const
{
    return QPoint(0, 0);
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

//  from src/widgets/accessible/qaccessiblewidgets.cpp, line 1020, as _ZNK21QAccessibleTextWidget18textCursorForRangeEii
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
inline QTextCursor QAccessibleTextWidget::textCursorForRange(int startOffset, int endOffset) const
{
    QTextCursor cursor = textCursor();
    cursor.setPosition(startOffset, QTextCursor::MoveAnchor);
    cursor.setPosition(endOffset, QTextCursor::KeepAnchor);

    return cursor;
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  Only a class built on QAccessibleTextWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQAccessibleTextWidget : QAccessibleTextWidget {
  using QAccessibleTextWidget::scrollBarPosition;
};

//  A QAccessibleTextWidget that Python can take functions over in. Every QAccessibleTextWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QAccessible::State * (*CuteQAccessibleTextWidgetCall0)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextWidgetCall1)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall2)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall3)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall4)(const void *, int, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextWidgetCall5)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall6)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef QString * (*CuteQAccessibleTextWidgetCall7)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextWidgetCall8)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QRect * (*CuteQAccessibleTextWidgetCall9)(const void *, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef int (*CuteQAccessibleTextWidgetCall10)(const void *, const QPoint *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall11)(const void *, int, int, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall12)(const void *, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall13)(const void *, int, int, const QString *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QPoint * (*CuteQAccessibleTextWidgetCall14)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef const QTextCursor * (*CuteQAccessibleTextWidgetCall15)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void (*CuteQAccessibleTextWidgetCall16)(const void *, const QTextCursor *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void * (*CuteQAccessibleTextWidgetCall17)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
typedef void * (*CuteQAccessibleTextWidgetCall18)(const void *, int *);
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall19)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleTextWidgetCall20)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTextWidgetCall21)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall22)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextWidgetCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextWidgetCall24)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleTextWidgetCall26)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall28)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextWidgetCall29)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTextWidgetCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTextWidgetCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTextWidgetCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextWidgetCall33)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall34)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextWidgetCall35)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTextWidgetCall36)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextWidgetCall37)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTextWidgetCall38)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextWidgetCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTextWidgetCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTextWidget : public QAccessibleTextWidget {
public:
  using QAccessibleTextWidget::QAccessibleTextWidget;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget17scrollBarPositionEv")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget10textCursorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZN21QAccessibleTextWidget13setTextCursorERK11QTextCursor")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget12textDocumentEv")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
    if (!std::strcmp(key, "_ZNK21QAccessibleTextWidget8viewportEv")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
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
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
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
  //  QAccessible::State QAccessibleTextWidget::state() const
  QAccessible::State state() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall0 call = reinterpret_cast<CuteQAccessibleTextWidgetCall0>(taken[0]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleTextWidget::state();
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  int QAccessibleTextWidget::selectionCount() const
  int selectionCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall1 call = reinterpret_cast<CuteQAccessibleTextWidgetCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall2 call = reinterpret_cast<CuteQAccessibleTextWidgetCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall3 call = reinterpret_cast<CuteQAccessibleTextWidgetCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall4 call = reinterpret_cast<CuteQAccessibleTextWidgetCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall5 call = reinterpret_cast<CuteQAccessibleTextWidgetCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall6 call = reinterpret_cast<CuteQAccessibleTextWidgetCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall7 call = reinterpret_cast<CuteQAccessibleTextWidgetCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall8 call = reinterpret_cast<CuteQAccessibleTextWidgetCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall9 call = reinterpret_cast<CuteQAccessibleTextWidgetCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall10 call = reinterpret_cast<CuteQAccessibleTextWidgetCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall11 call = reinterpret_cast<CuteQAccessibleTextWidgetCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall12 call = reinterpret_cast<CuteQAccessibleTextWidgetCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall13 call = reinterpret_cast<CuteQAccessibleTextWidgetCall13>(taken[13]);
      call(this, startOffset, endOffset, &text, &handled);
      if (handled) return;
    }
    QAccessibleTextWidget::replaceText(startOffset, endOffset, text);
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  QPoint QAccessibleTextWidget::scrollBarPosition() const
  QPoint scrollBarPosition() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall14 call = reinterpret_cast<CuteQAccessibleTextWidgetCall14>(taken[14]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleTextWidget::scrollBarPosition();
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  QTextCursor QAccessibleTextWidget::textCursor() const
  QTextCursor textCursor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall15 call = reinterpret_cast<CuteQAccessibleTextWidgetCall15>(taken[15]);
      const QTextCursor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  void QAccessibleTextWidget::setTextCursor(const QTextCursor &a0)
  void setTextCursor(const QTextCursor &a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall16 call = reinterpret_cast<CuteQAccessibleTextWidgetCall16>(taken[16]);
      call(this, &a0, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  QTextDocument *QAccessibleTextWidget::textDocument() const
  QTextDocument *textDocument() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall17 call = reinterpret_cast<CuteQAccessibleTextWidgetCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTextDocument *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
  //  QWidget *QAccessibleTextWidget::viewport() const
  QWidget *viewport() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall18 call = reinterpret_cast<CuteQAccessibleTextWidgetCall18>(taken[18]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall19 call = reinterpret_cast<CuteQAccessibleTextWidgetCall19>(taken[19]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleWidgetV2::interface_cast(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall20 call = reinterpret_cast<CuteQAccessibleTextWidgetCall20>(taken[20]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall21 call = reinterpret_cast<CuteQAccessibleTextWidgetCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall22 call = reinterpret_cast<CuteQAccessibleTextWidgetCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall23 call = reinterpret_cast<CuteQAccessibleTextWidgetCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall24 call = reinterpret_cast<CuteQAccessibleTextWidgetCall24>(taken[24]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall25 call = reinterpret_cast<CuteQAccessibleTextWidgetCall25>(taken[25]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall26 call = reinterpret_cast<CuteQAccessibleTextWidgetCall26>(taken[26]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall27 call = reinterpret_cast<CuteQAccessibleTextWidgetCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall28 call = reinterpret_cast<CuteQAccessibleTextWidgetCall28>(taken[28]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall29 call = reinterpret_cast<CuteQAccessibleTextWidgetCall29>(taken[29]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleWidget::text(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall30 call = reinterpret_cast<CuteQAccessibleTextWidgetCall30>(taken[30]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall31 call = reinterpret_cast<CuteQAccessibleTextWidgetCall31>(taken[31]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall32 call = reinterpret_cast<CuteQAccessibleTextWidgetCall32>(taken[32]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall33 call = reinterpret_cast<CuteQAccessibleTextWidgetCall33>(taken[33]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall34 call = reinterpret_cast<CuteQAccessibleTextWidgetCall34>(taken[34]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleObject::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall35 call = reinterpret_cast<CuteQAccessibleTextWidgetCall35>(taken[35]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall36 call = reinterpret_cast<CuteQAccessibleTextWidgetCall36>(taken[36]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleTextInterface::scrollToSubstring(int startIndex, int
  //      endIndex)
  void scrollToSubstring(int startIndex, int endIndex) override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall37 call = reinterpret_cast<CuteQAccessibleTextWidgetCall37>(taken[37]);
      call(this, startIndex, endIndex, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[38]) {
      int handled = 0;
      CuteQAccessibleTextWidgetCall38 call = reinterpret_cast<CuteQAccessibleTextWidgetCall38>(taken[38]);
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
      CuteQAccessibleTextWidgetCall39 call = reinterpret_cast<CuteQAccessibleTextWidgetCall39>(taken[39]);
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
      CuteQAccessibleTextWidgetCall40 call = reinterpret_cast<CuteQAccessibleTextWidgetCall40>(taken[40]);
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

//  QAccessible::State QAccessibleTextWidget::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK21QAccessibleTextWidget5stateEv(
    const QAccessibleTextWidget *self) {
  return new QAccessible::State(self->state());
}

//  void QAccessibleTextWidget::selection(int selectionIndex, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAccessibleTextWidget9selectionEiPiS0_(
    const QAccessibleTextWidget *self,
    int selectionIndex,
    int *startOffset,
    int *endOffset) {
  self->selection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleTextWidget::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleTextWidget14selectionCountEv(
    const QAccessibleTextWidget *self) {
  return self->selectionCount();
}

//  void QAccessibleTextWidget::addSelection(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget12addSelectionEii(
    QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  self->addSelection(startOffset, endOffset);
}

//  void QAccessibleTextWidget::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget15removeSelectionEi(
    QAccessibleTextWidget *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleTextWidget::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget12setSelectionEiii(
    QAccessibleTextWidget *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleTextWidget::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleTextWidget14cursorPositionEv(
    const QAccessibleTextWidget *self) {
  return self->cursorPosition();
}

//  void QAccessibleTextWidget::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget17setCursorPositionEi(
    QAccessibleTextWidget *self,
    int position) {
  self->setCursorPosition(position);
}

//  QString QAccessibleTextWidget::text(int startOffset, int endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleTextWidget4textEii(
    const QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  return new QString(self->text(startOffset, endOffset));
}

//  QString QAccessibleTextWidget::textBeforeOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleTextWidget16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextWidget *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textBeforeOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleTextWidget::textAfterOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleTextWidget15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextWidget *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAfterOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  QString QAccessibleTextWidget::textAtOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleTextWidget12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleTextWidget *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *startOffset,
    int *endOffset) {
  return new QString(
      self->textAtOffset(
          offset,
          boundaryType,
          startOffset,
          endOffset));
}

//  int QAccessibleTextWidget::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleTextWidget14characterCountEv(
    const QAccessibleTextWidget *self) {
  return self->characterCount();
}

//  QRect QAccessibleTextWidget::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK21QAccessibleTextWidget13characterRectEi(
    const QAccessibleTextWidget *self,
    int offset) {
  return new QRect(self->characterRect(offset));
}

//  int QAccessibleTextWidget::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAccessibleTextWidget13offsetAtPointERK6QPoint(
    const QAccessibleTextWidget *self,
    const QPoint *point) {
  return self->offsetAtPoint(*point);
}

//  QString QAccessibleTextWidget::attributes(int offset, int *startOffset,
//      int *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QAccessibleTextWidget10attributesEiPiS0_(
    const QAccessibleTextWidget *self,
    int offset,
    int *startOffset,
    int *endOffset) {
  return new QString(self->attributes(offset, startOffset, endOffset));
}

//  void QAccessibleTextWidget::deleteText(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget10deleteTextEii(
    QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleTextWidget::insertText(int offset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget10insertTextEiRK7QString(
    QAccessibleTextWidget *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleTextWidget::replaceText(int startOffset, int endOffset,
//      const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget11replaceTextEiiRK7QString(
    QAccessibleTextWidget *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  QTextCursor QAccessibleTextWidget::textCursorForRange(int startOffset,
//      int endOffset) const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK21QAccessibleTextWidget18textCursorForRangeEii(
    const QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  return new QTextCursor(self->textCursorForRange(startOffset, endOffset));
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

//  QPoint QAccessibleTextWidget::scrollBarPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK21QAccessibleTextWidget17scrollBarPositionEv(
    const QAccessibleTextWidget *self) {
  return new QPoint(self->scrollBarPosition());
}

//  QTextCursor QAccessibleTextWidget::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK21QAccessibleTextWidget10textCursorEv(
    const QAccessibleTextWidget *self) {
  return new QTextCursor(self->textCursor());
}

//  void QAccessibleTextWidget::setTextCursor(const QTextCursor &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAccessibleTextWidget13setTextCursorERK11QTextCursor(
    QAccessibleTextWidget *self,
    const QTextCursor *a0) {
  self->setTextCursor(*a0);
}

//  QTextDocument *QAccessibleTextWidget::textDocument() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK21QAccessibleTextWidget12textDocumentEv(
    const QAccessibleTextWidget *self) {
  return self->textDocument();
}

//  QWidget *QAccessibleTextWidget::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK21QAccessibleTextWidget8viewportEv(
    const QAccessibleTextWidget *self) {
  return self->viewport();
}

//  QAccessibleTextWidget as the QAccessibleTextInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleTextInterface *ritual_cast_QAccessibleTextWidget_QAccessibleTextInterface(
    QAccessibleTextWidget *self) {
  return static_cast<QAccessibleTextInterface *>(self);
}

//  QAccessibleTextWidget as the QAccessibleEditableTextInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_cast_QAccessibleTextWidget_QAccessibleEditableTextInterface(
    QAccessibleTextWidget *self) {
  return static_cast<QAccessibleEditableTextInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleTextWidget, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTextWidget(
    QAccessibleTextWidget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTextWidget *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  QAccessible::State QAccessibleTextWidget::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK21QAccessibleTextWidget5stateEv(
    const QAccessibleTextWidget *self) {
  return new QAccessible::State(self->QAccessibleTextWidget::state());
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  int QAccessibleTextWidget::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleTextWidget14selectionCountEv(
    const QAccessibleTextWidget *self) {
  return self->QAccessibleTextWidget::selectionCount();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::addSelection(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget12addSelectionEii(
    QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleTextWidget::addSelection(startOffset, endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget15removeSelectionEi(
    QAccessibleTextWidget *self,
    int selectionIndex) {
  self->QAccessibleTextWidget::removeSelection(selectionIndex);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget12setSelectionEiii(
    QAccessibleTextWidget *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->QAccessibleTextWidget::setSelection(
      selectionIndex,
      startOffset,
      endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  int QAccessibleTextWidget::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleTextWidget14cursorPositionEv(
    const QAccessibleTextWidget *self) {
  return self->QAccessibleTextWidget::cursorPosition();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget17setCursorPositionEi(
    QAccessibleTextWidget *self,
    int position) {
  self->QAccessibleTextWidget::setCursorPosition(position);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  QString QAccessibleTextWidget::text(int startOffset, int endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK21QAccessibleTextWidget4textEii(
    const QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  return new QString(
      self->QAccessibleTextWidget::text(
          startOffset,
          endOffset));
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  int QAccessibleTextWidget::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleTextWidget14characterCountEv(
    const QAccessibleTextWidget *self) {
  return self->QAccessibleTextWidget::characterCount();
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  QRect QAccessibleTextWidget::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK21QAccessibleTextWidget13characterRectEi(
    const QAccessibleTextWidget *self,
    int offset) {
  return new QRect(self->QAccessibleTextWidget::characterRect(offset));
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  int QAccessibleTextWidget::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAccessibleTextWidget13offsetAtPointERK6QPoint(
    const QAccessibleTextWidget *self,
    const QPoint *point) {
  return self->QAccessibleTextWidget::offsetAtPoint(*point);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::deleteText(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget10deleteTextEii(
    QAccessibleTextWidget *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleTextWidget::deleteText(startOffset, endOffset);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::insertText(int offset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget10insertTextEiRK7QString(
    QAccessibleTextWidget *self,
    int offset,
    const QString *text) {
  self->QAccessibleTextWidget::insertText(offset, *text);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  void QAccessibleTextWidget::replaceText(int startOffset, int endOffset,
//      const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAccessibleTextWidget11replaceTextEiiRK7QString(
    QAccessibleTextWidget *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->QAccessibleTextWidget::replaceText(startOffset, endOffset, *text);
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if !defined(QT_NO_CURSOR)
//  QPoint QAccessibleTextWidget::scrollBarPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK21QAccessibleTextWidget17scrollBarPositionEv(
    const QAccessibleTextWidget *self) {
  return new QPoint(
      static_cast<const OwnQAccessibleTextWidget *>(self)->OwnQAccessibleTextWidget::scrollBarPosition());
}
#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)

#endif  // !defined(QT_NO_CURSOR)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
