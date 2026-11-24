//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/simplewidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "simplewidgets_p.h"
#if QT_CONFIG(abstractbutton)
#include <qabstractbutton.h>
#endif
#if QT_CONFIG(checkbox)
#include <qcheckbox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <qpushbutton.h>
#endif
#if QT_CONFIG(progressbar)
#include <qprogressbar.h>
#endif
#if QT_CONFIG(statusbar)
#include <qstatusbar.h>
#endif
#if QT_CONFIG(radiobutton)
#include <qradiobutton.h>
#endif
#if QT_CONFIG(toolbutton)
#include <qtoolbutton.h>
#endif
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#if QT_CONFIG(label)
#include <qlabel.h>
#endif
#if QT_CONFIG(groupbox)
#include <qgroupbox.h>
#endif
#if QT_CONFIG(lcdnumber)
#include <qlcdnumber.h>
#endif
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#include <private/qlineedit_p.h>
#endif
#ifndef QT_NO_PICTURE
#include <QtGui/qpicture.h>
#endif
#if QT_CONFIG(messagebox)
#include <qmessagebox.h>
#endif
#include <qstyle.h>
#include <qstyleoption.h>
#include <qtextdocument.h>
#include <qwindow.h>
#include <private/qwindowcontainer_p.h>
#include <QtCore/qvarlengtharray.h>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#include <QtGui/qvalidator.h>
#ifdef Q_OS_MACOS
#include <qfocusframe.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/accessible/simplewidgets.cpp, line 682, as _ZNK19QAccessibleLineEdit4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QString QAccessibleLineEdit::text(QAccessible::Text t) const
{
    QString str;
    switch (t) {
    case QAccessible::Value:
        str = lineEdit()->displayText();
        break;
    default:
        break;
    }
    if (str.isEmpty())
        str = QAccessibleWidgetV2::text(t);
    if (str.isEmpty() && t == QAccessible::Description)
        str = lineEdit()->placeholderText();
    return str;
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 699, as _ZN19QAccessibleLineEdit7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::setText(QAccessible::Text t, const QString &text)
{
    if (t != QAccessible::Value) {
        QAccessibleWidgetV2::setText(t, text);
        return;
    }

    QString newText = text;
#if QT_CONFIG(validator)
    if (lineEdit()->validator()) {
        int pos = 0;
        if (lineEdit()->validator()->validate(newText, pos) != QValidator::Acceptable)
            return;
    }
#endif
    lineEdit()->setText(newText);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 717, as _ZNK19QAccessibleLineEdit5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QAccessible::State QAccessibleLineEdit::state() const
{
    QAccessible::State state = QAccessibleWidgetV2::state();

    QLineEdit *l = lineEdit();
    state.editable = true;
    if (l->isReadOnly())
        state.readOnly = true;

    if (l->echoMode() != QLineEdit::Normal)
        state.passwordEdit = true;

    state.selectableText = true;
    return state;
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 742, as _ZN19QAccessibleLineEdit12addSelectionEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::addSelection(int startOffset, int endOffset)
{
    setSelection(0, startOffset, endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 747, as _ZNK19QAccessibleLineEdit10attributesEiPiS0_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QString QAccessibleLineEdit::attributes(int offset, int *startOffset, int *endOffset) const
{
    // QLineEdit doesn't have text attributes
    *startOffset = *endOffset = offset;
    return QString();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 754, as _ZNK19QAccessibleLineEdit14cursorPositionEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline int QAccessibleLineEdit::cursorPosition() const
{
    return lineEdit()->cursorPosition();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 759, as _ZNK19QAccessibleLineEdit13characterRectEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QRect QAccessibleLineEdit::characterRect(int offset) const
{
    int x = lineEdit()->d_func()->control->cursorToX(offset);
    int y = lineEdit()->textMargins().top();
    QFontMetrics fm(lineEdit()->font());
    const QString ch = text(offset, offset + 1);
    if (ch.isEmpty())
        return QRect();
    int w = fm.horizontalAdvance(ch);
    int h = fm.height();
    QRect r(x, y, w, h);
    r.moveTo(lineEdit()->mapToGlobal(r.topLeft()));
    return r;
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 774, as _ZNK19QAccessibleLineEdit14selectionCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline int QAccessibleLineEdit::selectionCount() const
{
    return lineEdit()->hasSelectedText() ? 1 : 0;
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 779, as _ZNK19QAccessibleLineEdit13offsetAtPointERK6QPoint
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline int QAccessibleLineEdit::offsetAtPoint(const QPoint &point) const
{
    QPoint p = lineEdit()->mapFromGlobal(point);

    return lineEdit()->cursorPositionAt(p);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 786, as _ZNK19QAccessibleLineEdit9selectionEiPiS0_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::selection(int selectionIndex, int *startOffset, int *endOffset) const
{
    *startOffset = *endOffset = 0;
    if (selectionIndex != 0)
        return;

    *startOffset = lineEdit()->selectionStart();
    *endOffset = *startOffset + lineEdit()->selectedText().size();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 796, as _ZNK19QAccessibleLineEdit4textEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QString QAccessibleLineEdit::text(int startOffset, int endOffset) const
{
    if (startOffset > endOffset)
        return QString();

    return lineEdit()->displayText().mid(startOffset, endOffset - startOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 804, as _ZNK19QAccessibleLineEdit16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QString QAccessibleLineEdit::textBeforeOffset(int offset, QAccessible::TextBoundaryType boundaryType,
        int *startOffset, int *endOffset) const
{
    if (offset == -2)
        offset = cursorPosition();
    return QAccessibleTextInterface::textBeforeOffset(offset, boundaryType, startOffset, endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 812, as _ZNK19QAccessibleLineEdit15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QString QAccessibleLineEdit::textAfterOffset(int offset, QAccessible::TextBoundaryType boundaryType,
        int *startOffset, int *endOffset) const
{
    if (offset == -2)
        offset = cursorPosition();
    return QAccessibleTextInterface::textAfterOffset(offset, boundaryType, startOffset, endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 820, as _ZNK19QAccessibleLineEdit12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QString QAccessibleLineEdit::textAtOffset(int offset, QAccessible::TextBoundaryType boundaryType,
        int *startOffset, int *endOffset) const
{
    if (offset == -2)
        offset = cursorPosition();
    return QAccessibleTextInterface::textAtOffset(offset, boundaryType, startOffset, endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 828, as _ZN19QAccessibleLineEdit15removeSelectionEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::removeSelection(int selectionIndex)
{
    if (selectionIndex != 0)
        return;

    lineEdit()->deselect();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 836, as _ZN19QAccessibleLineEdit17setCursorPositionEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::setCursorPosition(int position)
{
    lineEdit()->setCursorPosition(position);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 841, as _ZN19QAccessibleLineEdit12setSelectionEiii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::setSelection(int selectionIndex, int startOffset, int endOffset)
{
    if (selectionIndex != 0)
        return;

    lineEdit()->setSelection(startOffset, endOffset - startOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 849, as _ZNK19QAccessibleLineEdit14characterCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline int QAccessibleLineEdit::characterCount() const
{
    return lineEdit()->displayText().size();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 854, as _ZN19QAccessibleLineEdit17scrollToSubstringEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::scrollToSubstring(int startIndex, int endIndex)
{
    lineEdit()->setCursorPosition(endIndex);
    lineEdit()->setCursorPosition(startIndex);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 860, as _ZN19QAccessibleLineEdit10deleteTextEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::deleteText(int startOffset, int endOffset)
{
    lineEdit()->setText(lineEdit()->text().remove(startOffset, endOffset - startOffset));
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 865, as _ZN19QAccessibleLineEdit10insertTextEiRK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::insertText(int offset, const QString &text)
{
    lineEdit()->setText(lineEdit()->text().insert(offset, text));
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 870, as _ZN19QAccessibleLineEdit11replaceTextEiiRK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void QAccessibleLineEdit::replaceText(int startOffset, int endOffset, const QString &text)
{
    lineEdit()->setText(lineEdit()->text().replace(startOffset, endOffset - startOffset, text));
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 677, as _ZNK19QAccessibleLineEdit8lineEditEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QLineEdit *QAccessibleLineEdit::lineEdit() const
{
    return qobject_cast<QLineEdit*>(object());
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleLineEdit that Python can take functions over in. Every QAccessibleLineEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef QString * (*CuteQAccessibleLineEditCall0)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall1)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef const QAccessible::State * (*CuteQAccessibleLineEditCall2)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall3)(const void *, int, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef int (*CuteQAccessibleLineEditCall4)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef const QRect * (*CuteQAccessibleLineEditCall5)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef int (*CuteQAccessibleLineEditCall6)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef int (*CuteQAccessibleLineEditCall7)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef QString * (*CuteQAccessibleLineEditCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall9)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall10)(const void *, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall11)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef int (*CuteQAccessibleLineEditCall12)(const void *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall13)(const void *, int, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall14)(const void *, int, int, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall15)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
typedef void (*CuteQAccessibleLineEditCall16)(const void *, int, int, const QString *, int *);
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleLineEditCall17)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleLineEditCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleLineEditCall19)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleLineEditCall20)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleLineEditCall21)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleLineEditCall22)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleLineEditCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleLineEditCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleLineEditCall25)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleLineEditCall26)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleLineEditCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleLineEditCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleLineEditCall29)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleLineEditCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleLineEditCall31)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleLineEditCall32)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleLineEditCall33)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleLineEdit : public QAccessibleLineEdit {
public:
  using QAccessibleLineEdit::QAccessibleLineEdit;
  void *taken[34] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  QString QAccessibleLineEdit::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleLineEditCall0 call = reinterpret_cast<CuteQAccessibleLineEditCall0>(taken[0]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleLineEdit::text(t);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleLineEditCall1 call = reinterpret_cast<CuteQAccessibleLineEditCall1>(taken[1]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::setText(t, text);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  QAccessible::State QAccessibleLineEdit::state() const
  QAccessible::State state() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleLineEditCall2 call = reinterpret_cast<CuteQAccessibleLineEditCall2>(taken[2]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleLineEdit::state();
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::addSelection(int startOffset, int
  //      endOffset)
  void addSelection(int startOffset, int endOffset) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleLineEditCall3 call = reinterpret_cast<CuteQAccessibleLineEditCall3>(taken[3]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::addSelection(startOffset, endOffset);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  int QAccessibleLineEdit::cursorPosition() const
  int cursorPosition() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleLineEditCall4 call = reinterpret_cast<CuteQAccessibleLineEditCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleLineEdit::cursorPosition();
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  QRect QAccessibleLineEdit::characterRect(int offset) const
  QRect characterRect(int offset) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleLineEditCall5 call = reinterpret_cast<CuteQAccessibleLineEditCall5>(taken[5]);
      const QRect * given = call(this, offset, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleLineEdit::characterRect(offset);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  int QAccessibleLineEdit::selectionCount() const
  int selectionCount() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleLineEditCall6 call = reinterpret_cast<CuteQAccessibleLineEditCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleLineEdit::selectionCount();
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  int QAccessibleLineEdit::offsetAtPoint(const QPoint &point) const
  int offsetAtPoint(const QPoint &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleLineEditCall7 call = reinterpret_cast<CuteQAccessibleLineEditCall7>(taken[7]);
      int given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QAccessibleLineEdit::offsetAtPoint(point);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  QString QAccessibleLineEdit::text(int startOffset, int endOffset)
  //      const
  QString text(int startOffset, int endOffset) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleLineEditCall8 call = reinterpret_cast<CuteQAccessibleLineEditCall8>(taken[8]);
      QString * given = call(this, startOffset, endOffset, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleLineEdit::text(startOffset, endOffset);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::removeSelection(int selectionIndex)
  void removeSelection(int selectionIndex) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleLineEditCall9 call = reinterpret_cast<CuteQAccessibleLineEditCall9>(taken[9]);
      call(this, selectionIndex, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::removeSelection(selectionIndex);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::setCursorPosition(int position)
  void setCursorPosition(int position) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleLineEditCall10 call = reinterpret_cast<CuteQAccessibleLineEditCall10>(taken[10]);
      call(this, position, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::setCursorPosition(position);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::setSelection(int selectionIndex, int
  //      startOffset, int endOffset)
  void setSelection(
      int selectionIndex,
      int startOffset,
      int endOffset) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleLineEditCall11 call = reinterpret_cast<CuteQAccessibleLineEditCall11>(taken[11]);
      call(this, selectionIndex, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::setSelection(selectionIndex, startOffset, endOffset);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  int QAccessibleLineEdit::characterCount() const
  int characterCount() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleLineEditCall12 call = reinterpret_cast<CuteQAccessibleLineEditCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleLineEdit::characterCount();
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::scrollToSubstring(int startIndex, int
  //      endIndex)
  void scrollToSubstring(int startIndex, int endIndex) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleLineEditCall13 call = reinterpret_cast<CuteQAccessibleLineEditCall13>(taken[13]);
      call(this, startIndex, endIndex, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::scrollToSubstring(startIndex, endIndex);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::deleteText(int startOffset, int endOffset)
  void deleteText(int startOffset, int endOffset) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleLineEditCall14 call = reinterpret_cast<CuteQAccessibleLineEditCall14>(taken[14]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::deleteText(startOffset, endOffset);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::insertText(int offset, const QString &text)
  void insertText(int offset, const QString &text) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleLineEditCall15 call = reinterpret_cast<CuteQAccessibleLineEditCall15>(taken[15]);
      call(this, offset, &text, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::insertText(offset, text);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
  //  void QAccessibleLineEdit::replaceText(int startOffset, int endOffset,
  //      const QString &text)
  void replaceText(
      int startOffset,
      int endOffset,
      const QString &text) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleLineEditCall16 call = reinterpret_cast<CuteQAccessibleLineEditCall16>(taken[16]);
      call(this, startOffset, endOffset, &text, &handled);
      if (handled) return;
    }
    QAccessibleLineEdit::replaceText(startOffset, endOffset, text);
  }
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleLineEditCall17 call = reinterpret_cast<CuteQAccessibleLineEditCall17>(taken[17]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleLineEditCall18 call = reinterpret_cast<CuteQAccessibleLineEditCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleLineEditCall19 call = reinterpret_cast<CuteQAccessibleLineEditCall19>(taken[19]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleLineEditCall20 call = reinterpret_cast<CuteQAccessibleLineEditCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleLineEditCall21 call = reinterpret_cast<CuteQAccessibleLineEditCall21>(taken[21]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleLineEditCall22 call = reinterpret_cast<CuteQAccessibleLineEditCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleLineEditCall23 call = reinterpret_cast<CuteQAccessibleLineEditCall23>(taken[23]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleLineEditCall24 call = reinterpret_cast<CuteQAccessibleLineEditCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleLineEditCall25 call = reinterpret_cast<CuteQAccessibleLineEditCall25>(taken[25]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleLineEditCall26 call = reinterpret_cast<CuteQAccessibleLineEditCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleLineEditCall27 call = reinterpret_cast<CuteQAccessibleLineEditCall27>(taken[27]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleLineEditCall28 call = reinterpret_cast<CuteQAccessibleLineEditCall28>(taken[28]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleLineEditCall29 call = reinterpret_cast<CuteQAccessibleLineEditCall29>(taken[29]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleLineEditCall30 call = reinterpret_cast<CuteQAccessibleLineEditCall30>(taken[30]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleLineEditCall31 call = reinterpret_cast<CuteQAccessibleLineEditCall31>(taken[31]);
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
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleLineEditCall32 call = reinterpret_cast<CuteQAccessibleLineEditCall32>(taken[32]);
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
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleLineEditCall33 call = reinterpret_cast<CuteQAccessibleLineEditCall33>(taken[33]);
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

//  QString QAccessibleLineEdit::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleLineEdit4textEN11QAccessible4TextE(
    const QAccessibleLineEdit *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void QAccessibleLineEdit::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit7setTextEN11QAccessible4TextERK7QString(
    QAccessibleLineEdit *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessible::State QAccessibleLineEdit::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK19QAccessibleLineEdit5stateEv(
    const QAccessibleLineEdit *self) {
  return new QAccessible::State(self->state());
}

//  void QAccessibleLineEdit::addSelection(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit12addSelectionEii(
    QAccessibleLineEdit *self,
    int startOffset,
    int endOffset) {
  self->addSelection(startOffset, endOffset);
}

//  QString QAccessibleLineEdit::attributes(int offset, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleLineEdit10attributesEiPiS0_(
    const QAccessibleLineEdit *self,
    int offset,
    int *startOffset,
    int *endOffset) {
  return new QString(self->attributes(offset, startOffset, endOffset));
}

//  int QAccessibleLineEdit::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleLineEdit14cursorPositionEv(
    const QAccessibleLineEdit *self) {
  return self->cursorPosition();
}

//  QRect QAccessibleLineEdit::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QAccessibleLineEdit13characterRectEi(
    const QAccessibleLineEdit *self,
    int offset) {
  return new QRect(self->characterRect(offset));
}

//  int QAccessibleLineEdit::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleLineEdit14selectionCountEv(
    const QAccessibleLineEdit *self) {
  return self->selectionCount();
}

//  int QAccessibleLineEdit::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleLineEdit13offsetAtPointERK6QPoint(
    const QAccessibleLineEdit *self,
    const QPoint *point) {
  return self->offsetAtPoint(*point);
}

//  void QAccessibleLineEdit::selection(int selectionIndex, int *startOffset,
//      int *endOffset) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QAccessibleLineEdit9selectionEiPiS0_(
    const QAccessibleLineEdit *self,
    int selectionIndex,
    int *startOffset,
    int *endOffset) {
  self->selection(selectionIndex, startOffset, endOffset);
}

//  QString QAccessibleLineEdit::text(int startOffset, int endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleLineEdit4textEii(
    const QAccessibleLineEdit *self,
    int startOffset,
    int endOffset) {
  return new QString(self->text(startOffset, endOffset));
}

//  QString QAccessibleLineEdit::textBeforeOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleLineEdit16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleLineEdit *self,
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

//  QString QAccessibleLineEdit::textAfterOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleLineEdit15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleLineEdit *self,
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

//  QString QAccessibleLineEdit::textAtOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAccessibleLineEdit12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleLineEdit *self,
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

//  void QAccessibleLineEdit::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit15removeSelectionEi(
    QAccessibleLineEdit *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleLineEdit::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit17setCursorPositionEi(
    QAccessibleLineEdit *self,
    int position) {
  self->setCursorPosition(position);
}

//  void QAccessibleLineEdit::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit12setSelectionEiii(
    QAccessibleLineEdit *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleLineEdit::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleLineEdit14characterCountEv(
    const QAccessibleLineEdit *self) {
  return self->characterCount();
}

//  void QAccessibleLineEdit::scrollToSubstring(int startIndex, int endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit17scrollToSubstringEii(
    QAccessibleLineEdit *self,
    int startIndex,
    int endIndex) {
  self->scrollToSubstring(startIndex, endIndex);
}

//  void QAccessibleLineEdit::deleteText(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit10deleteTextEii(
    QAccessibleLineEdit *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleLineEdit::insertText(int offset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit10insertTextEiRK7QString(
    QAccessibleLineEdit *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleLineEdit::replaceText(int startOffset, int endOffset,
//      const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleLineEdit11replaceTextEiiRK7QString(
    QAccessibleLineEdit *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  QLineEdit *QAccessibleLineEdit::lineEdit() const
extern "C" Q_DECL_EXPORT
QLineEdit *ritual_ZNK19QAccessibleLineEdit8lineEditEv(
    const QAccessibleLineEdit *self) {
  return self->lineEdit();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleLineEdit as the QAccessibleTextInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleTextInterface *ritual_cast_QAccessibleLineEdit_QAccessibleTextInterface(
    QAccessibleLineEdit *self) {
  return static_cast<QAccessibleTextInterface *>(self);
}

//  QAccessibleLineEdit as the QAccessibleEditableTextInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_cast_QAccessibleLineEdit_QAccessibleEditableTextInterface(
    QAccessibleLineEdit *self) {
  return static_cast<QAccessibleEditableTextInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleLineEdit, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleLineEdit(
    QAccessibleLineEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleLineEdit *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  QString QAccessibleLineEdit::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAccessibleLineEdit4textEN11QAccessible4TextE(
    const QAccessibleLineEdit *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleLineEdit::text(t));
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit7setTextEN11QAccessible4TextERK7QString(
    QAccessibleLineEdit *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessibleLineEdit::setText(t, *text);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  QAccessible::State QAccessibleLineEdit::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK19QAccessibleLineEdit5stateEv(
    const QAccessibleLineEdit *self) {
  return new QAccessible::State(self->QAccessibleLineEdit::state());
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::addSelection(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit12addSelectionEii(
    QAccessibleLineEdit *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleLineEdit::addSelection(startOffset, endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  int QAccessibleLineEdit::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleLineEdit14cursorPositionEv(
    const QAccessibleLineEdit *self) {
  return self->QAccessibleLineEdit::cursorPosition();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  QRect QAccessibleLineEdit::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK19QAccessibleLineEdit13characterRectEi(
    const QAccessibleLineEdit *self,
    int offset) {
  return new QRect(self->QAccessibleLineEdit::characterRect(offset));
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  int QAccessibleLineEdit::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleLineEdit14selectionCountEv(
    const QAccessibleLineEdit *self) {
  return self->QAccessibleLineEdit::selectionCount();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  int QAccessibleLineEdit::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleLineEdit13offsetAtPointERK6QPoint(
    const QAccessibleLineEdit *self,
    const QPoint *point) {
  return self->QAccessibleLineEdit::offsetAtPoint(*point);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  QString QAccessibleLineEdit::text(int startOffset, int endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAccessibleLineEdit4textEii(
    const QAccessibleLineEdit *self,
    int startOffset,
    int endOffset) {
  return new QString(
      self->QAccessibleLineEdit::text(
          startOffset,
          endOffset));
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit15removeSelectionEi(
    QAccessibleLineEdit *self,
    int selectionIndex) {
  self->QAccessibleLineEdit::removeSelection(selectionIndex);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit17setCursorPositionEi(
    QAccessibleLineEdit *self,
    int position) {
  self->QAccessibleLineEdit::setCursorPosition(position);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit12setSelectionEiii(
    QAccessibleLineEdit *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->QAccessibleLineEdit::setSelection(
      selectionIndex,
      startOffset,
      endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  int QAccessibleLineEdit::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleLineEdit14characterCountEv(
    const QAccessibleLineEdit *self) {
  return self->QAccessibleLineEdit::characterCount();
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::scrollToSubstring(int startIndex, int endIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit17scrollToSubstringEii(
    QAccessibleLineEdit *self,
    int startIndex,
    int endIndex) {
  self->QAccessibleLineEdit::scrollToSubstring(startIndex, endIndex);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::deleteText(int startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit10deleteTextEii(
    QAccessibleLineEdit *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleLineEdit::deleteText(startOffset, endOffset);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::insertText(int offset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit10insertTextEiRK7QString(
    QAccessibleLineEdit *self,
    int offset,
    const QString *text) {
  self->QAccessibleLineEdit::insertText(offset, *text);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
//  void QAccessibleLineEdit::replaceText(int startOffset, int endOffset,
//      const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleLineEdit11replaceTextEiiRK7QString(
    QAccessibleLineEdit *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->QAccessibleLineEdit::replaceText(startOffset, endOffset, *text);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)
