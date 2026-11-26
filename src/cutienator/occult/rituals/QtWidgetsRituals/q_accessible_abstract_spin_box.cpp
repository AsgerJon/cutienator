//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/rangecontrols_p.h>
#if QT_CONFIG(slider)
#include <QtWidgets/qslider.h>
#endif
#if QT_CONFIG(dial)
#include <QtWidgets/qdial.h>
#endif
#if QT_CONFIG(spinbox)
#include <QtWidgets/qspinbox.h>
#endif
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qdebug.h>
#include <QtCore/qglobal.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#include <QtCore/qmath.h>
#include <QtGui/private/qmath_p.h>
#include <QtWidgets/private/simplewidgets_p.h> // let spinbox use line edit's interface
#include <QtWidgets/private/simplewidgets_p.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#if QT_CONFIG(checkbox)
#include <QtWidgets/qcheckbox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#if QT_CONFIG(progressbar)
#include <QtWidgets/qprogressbar.h>
#endif
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#if QT_CONFIG(radiobutton)
#include <QtWidgets/qradiobutton.h>
#endif
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(label)
#include <QtWidgets/qlabel.h>
#endif
#if QT_CONFIG(groupbox)
#include <QtWidgets/qgroupbox.h>
#endif
#if QT_CONFIG(lcdnumber)
#include <QtWidgets/qlcdnumber.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/private/qlineedit_p.h>
#endif
#ifndef QT_NO_PICTURE
#include <QtGui/qpicture.h>
#endif
#if QT_CONFIG(messagebox)
#include <QtWidgets/qmessagebox.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qwindow.h>
#include <QtWidgets/private/qwindowcontainer_p.h>
#include <QtCore/qvarlengtharray.h>
#if QT_CONFIG(accessibility)
#include <QtGui/private/qaccessiblehelper_p.h>
#endif
#include <QtGui/qvalidator.h>
#ifdef Q_OS_MACOS
#include <QtWidgets/qfocusframe.h>
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

//  from src/widgets/accessible/rangecontrols.cpp, line 208, as _ZN26QAccessibleAbstractSpinBox10deleteTextEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::deleteText(int startOffset, int endOffset)
{
    lineEditIface()->editableTextInterface()->deleteText(startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 213, as _ZN26QAccessibleAbstractSpinBox10insertTextEiRK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::insertText(int offset, const QString &text)
{
    lineEditIface()->editableTextInterface()->insertText(offset, text);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 218, as _ZN26QAccessibleAbstractSpinBox11replaceTextEiiRK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::replaceText(int startOffset, int endOffset, const QString &text)
{
    lineEditIface()->editableTextInterface()->replaceText(startOffset, endOffset, text);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 128, as _ZN26QAccessibleAbstractSpinBox12addSelectionEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::addSelection(int startOffset, int endOffset)
{
    lineEditIface()->textInterface()->addSelection(startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 193, as _ZN26QAccessibleAbstractSpinBox12setSelectionEiii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::setSelection(int selectionIndex, int startOffset, int endOffset)
{
    lineEditIface()->textInterface()->setSelection(selectionIndex, startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 92, as _ZN26QAccessibleAbstractSpinBox14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void *QAccessibleAbstractSpinBox::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::ValueInterface)
        return static_cast<QAccessibleValueInterface*>(this);
    if (t == QAccessible::TextInterface)
        return static_cast<QAccessibleTextInterface*>(this);
    if (t == QAccessible::EditableTextInterface)
        return static_cast<QAccessibleEditableTextInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 183, as _ZN26QAccessibleAbstractSpinBox15removeSelectionEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::removeSelection(int selectionIndex)
{
    lineEditIface()->textInterface()->removeSelection(selectionIndex);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 108, as _ZN26QAccessibleAbstractSpinBox15setCurrentValueERK8QVariant
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::setCurrentValue(const QVariant &value)
{
    abstractSpinBox()->setProperty("value", value);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 203, as _ZN26QAccessibleAbstractSpinBox17scrollToSubstringEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::scrollToSubstring(int startIndex, int endIndex)
{
    lineEditIface()->textInterface()->scrollToSubstring(startIndex, endIndex);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 188, as _ZN26QAccessibleAbstractSpinBox17setCursorPositionEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::setCursorPosition(int position)
{
    lineEditIface()->textInterface()->setCursorPosition(position);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 50, as _ZN26QAccessibleAbstractSpinBoxD2Ev
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QAccessibleAbstractSpinBox::~QAccessibleAbstractSpinBox()
{
    delete lineEdit;
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 133, as _ZNK26QAccessibleAbstractSpinBox10attributesEiPiS0_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleAbstractSpinBox::attributes(int offset, int *startOffset, int *endOffset) const
{
    return lineEditIface()->textInterface()->attributes(offset, startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 103, as _ZNK26QAccessibleAbstractSpinBox12currentValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QVariant QAccessibleAbstractSpinBox::currentValue() const
{
    return abstractSpinBox()->property("value");
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 113, as _ZNK26QAccessibleAbstractSpinBox12maximumValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QVariant QAccessibleAbstractSpinBox::maximumValue() const
{
    return abstractSpinBox()->property("maximum");
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 118, as _ZNK26QAccessibleAbstractSpinBox12minimumValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QVariant QAccessibleAbstractSpinBox::minimumValue() const
{
    return abstractSpinBox()->property("minimum");
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 178, as _ZNK26QAccessibleAbstractSpinBox12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleAbstractSpinBox::textAtOffset(int offset, QAccessible::TextBoundaryType boundaryType, int *startOffset, int *endOffset) const
{
    return lineEditIface()->textInterface()->textAtOffset(offset, boundaryType, startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 143, as _ZNK26QAccessibleAbstractSpinBox13characterRectEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QRect QAccessibleAbstractSpinBox::characterRect(int offset) const
{
    return lineEditIface()->textInterface()->characterRect(offset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 153, as _ZNK26QAccessibleAbstractSpinBox13offsetAtPointERK6QPoint
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline int QAccessibleAbstractSpinBox::offsetAtPoint(const QPoint &point) const
{
    return lineEditIface()->textInterface()->offsetAtPoint(point);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 198, as _ZNK26QAccessibleAbstractSpinBox14characterCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline int QAccessibleAbstractSpinBox::characterCount() const
{
    return lineEditIface()->textInterface()->characterCount();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 138, as _ZNK26QAccessibleAbstractSpinBox14cursorPositionEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline int QAccessibleAbstractSpinBox::cursorPosition() const
{
    return lineEditIface()->textInterface()->cursorPosition();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 148, as _ZNK26QAccessibleAbstractSpinBox14selectionCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline int QAccessibleAbstractSpinBox::selectionCount() const
{
    return lineEditIface()->textInterface()->selectionCount();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 123, as _ZNK26QAccessibleAbstractSpinBox15minimumStepSizeEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QVariant QAccessibleAbstractSpinBox::minimumStepSize() const
{
    return abstractSpinBox()->property("singleStep");
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 173, as _ZNK26QAccessibleAbstractSpinBox15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleAbstractSpinBox::textAfterOffset(int offset, QAccessible::TextBoundaryType boundaryType, int *startOffset, int *endOffset) const
{
    return lineEditIface()->textInterface()->textAfterOffset(offset, boundaryType, startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 168, as _ZNK26QAccessibleAbstractSpinBox16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleAbstractSpinBox::textBeforeOffset(int offset, QAccessible::TextBoundaryType boundaryType, int *startOffset, int *endOffset) const
{
    return lineEditIface()->textInterface()->textBeforeOffset(offset, boundaryType, startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 85, as _ZNK26QAccessibleAbstractSpinBox4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleAbstractSpinBox::text(QAccessible::Text t) const
{
    if (t == QAccessible::Value)
        return abstractSpinBox()->text();
    return QAccessibleWidgetV2::text(t);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 163, as _ZNK26QAccessibleAbstractSpinBox4textEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleAbstractSpinBox::text(int startOffset, int endOffset) const
{
    return lineEditIface()->textInterface()->text(startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 75, as _ZNK26QAccessibleAbstractSpinBox5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QAccessible::State QAccessibleAbstractSpinBox::state() const
{
    QAccessible::State state = QAccessibleWidgetV2::state();
    if (abstractSpinBox()->isReadOnly())
        state.readOnly = true;
    else
        state.editable = true;
    return state;
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 158, as _ZNK26QAccessibleAbstractSpinBox9selectionEiPiS0_
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline void QAccessibleAbstractSpinBox::selection(int selectionIndex, int *startOffset, int *endOffset) const
{
    lineEditIface()->textInterface()->selection(selectionIndex, startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/simplewidgets.cpp, line 669, as _ZN19QAccessibleLineEditC1EP7QWidgetRK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline QAccessibleLineEdit::QAccessibleLineEdit(QWidget *w, const QString &name)
: QAccessibleWidgetV2(w, QAccessible::EditableText, name)
{
    addControllingSignal("textChanged(const QString&)"_L1);
    addControllingSignal("returnPressed()"_L1);
}
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

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

//  from src/widgets/accessible/simplewidgets.cpp, line 733, as _ZN19QAccessibleLineEdit14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
inline void *QAccessibleLineEdit::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::TextInterface)
        return static_cast<QAccessibleTextInterface*>(this);
    if (t == QAccessible::EditableTextInterface)
        return static_cast<QAccessibleEditableTextInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
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

//  from src/widgets/accessible/rangecontrols.cpp, line 58, as _ZNK26QAccessibleAbstractSpinBox15abstractSpinBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QAbstractSpinBox *QAccessibleAbstractSpinBox::abstractSpinBox() const
{
    return qobject_cast<QAbstractSpinBox*>(object());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 63, as _ZNK26QAccessibleAbstractSpinBox13lineEditIfaceEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QAccessibleInterface *QAccessibleAbstractSpinBox::lineEditIface() const
{
#if QT_CONFIG(lineedit)
    // QAccessibleLineEdit is only used to forward the text functions
    if (!lineEdit)
        lineEdit = new QAccessibleLineEdit(abstractSpinBox()->lineEdit());
    return lineEdit;
#else
    return nullptr;
#endif
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleAbstractSpinBox that Python can take functions over in. Every QAccessibleAbstractSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QAccessible::State * (*CuteQAccessibleAbstractSpinBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleAbstractSpinBoxCall1)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall2)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleAbstractSpinBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall4)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleAbstractSpinBoxCall5)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleAbstractSpinBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleAbstractSpinBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleAbstractSpinBoxCall9)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QRect * (*CuteQAccessibleAbstractSpinBoxCall10)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleAbstractSpinBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleAbstractSpinBoxCall12)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleAbstractSpinBoxCall13)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall14)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall15)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall16)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleAbstractSpinBoxCall17)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall20)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleAbstractSpinBoxCall21)(const void *, int, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleAbstractSpinBoxCall22)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleAbstractSpinBoxCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleAbstractSpinBoxCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleAbstractSpinBoxCall26)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleAbstractSpinBoxCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall29)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall30)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleAbstractSpinBoxCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleAbstractSpinBoxCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleAbstractSpinBoxCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleAbstractSpinBoxCall34)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleAbstractSpinBoxCall36)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSpinBoxCall37)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleAbstractSpinBoxCall38)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleAbstractSpinBoxCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleAbstractSpinBoxCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleAbstractSpinBox : public QAccessibleAbstractSpinBox {
public:
  using QAccessibleAbstractSpinBox::QAccessibleAbstractSpinBox;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
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
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
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
#if QT_CONFIG(spinbox)
  //  QAccessible::State QAccessibleAbstractSpinBox::state() const
  QAccessible::State state() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall0 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall0>(taken[0]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::state();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QString QAccessibleAbstractSpinBox::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall1 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall1>(taken[1]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleAbstractSpinBox::text(t);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void *QAccessibleAbstractSpinBox::interface_cast(QAccessible::Interfa
  //      ceType t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall2 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall2>(taken[2]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleAbstractSpinBox::interface_cast(t);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QVariant QAccessibleAbstractSpinBox::currentValue() const
  QVariant currentValue() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall3 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall3>(taken[3]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::currentValue();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::setCurrentValue(const QVariant
  //      &value)
  void setCurrentValue(const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall4 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall4>(taken[4]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::setCurrentValue(value);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QVariant QAccessibleAbstractSpinBox::maximumValue() const
  QVariant maximumValue() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall5 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall5>(taken[5]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::maximumValue();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QVariant QAccessibleAbstractSpinBox::minimumValue() const
  QVariant minimumValue() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall6 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall6>(taken[6]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::minimumValue();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QVariant QAccessibleAbstractSpinBox::minimumStepSize() const
  QVariant minimumStepSize() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall7 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall7>(taken[7]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::minimumStepSize();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::addSelection(int startOffset, int
  //      endOffset)
  void addSelection(int startOffset, int endOffset) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall8 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall8>(taken[8]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::addSelection(startOffset, endOffset);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  int QAccessibleAbstractSpinBox::cursorPosition() const
  int cursorPosition() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall9 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractSpinBox::cursorPosition();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QRect QAccessibleAbstractSpinBox::characterRect(int offset) const
  QRect characterRect(int offset) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall10 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall10>(taken[10]);
      const QRect * given = call(this, offset, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::characterRect(offset);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  int QAccessibleAbstractSpinBox::selectionCount() const
  int selectionCount() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall11 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractSpinBox::selectionCount();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  int QAccessibleAbstractSpinBox::offsetAtPoint(const QPoint &point)
  //      const
  int offsetAtPoint(const QPoint &point) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall12 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall12>(taken[12]);
      int given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractSpinBox::offsetAtPoint(point);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QString QAccessibleAbstractSpinBox::text(int startOffset, int
  //      endOffset) const
  QString text(int startOffset, int endOffset) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall13 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall13>(taken[13]);
      QString * given = call(this, startOffset, endOffset, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleAbstractSpinBox::text(startOffset, endOffset);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::removeSelection(int selectionIndex)
  void removeSelection(int selectionIndex) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall14 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall14>(taken[14]);
      call(this, selectionIndex, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::removeSelection(selectionIndex);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::setCursorPosition(int position)
  void setCursorPosition(int position) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall15 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall15>(taken[15]);
      call(this, position, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::setCursorPosition(position);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::setSelection(int selectionIndex, int
  //      startOffset, int endOffset)
  void setSelection(
      int selectionIndex,
      int startOffset,
      int endOffset) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall16 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall16>(taken[16]);
      call(this, selectionIndex, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::setSelection(selectionIndex, startOffset, endOffset);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  int QAccessibleAbstractSpinBox::characterCount() const
  int characterCount() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall17 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractSpinBox::characterCount();
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::scrollToSubstring(int startIndex,
  //      int endIndex)
  void scrollToSubstring(int startIndex, int endIndex) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall18 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall18>(taken[18]);
      call(this, startIndex, endIndex, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::scrollToSubstring(startIndex, endIndex);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::deleteText(int startOffset, int
  //      endOffset)
  void deleteText(int startOffset, int endOffset) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall19 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall19>(taken[19]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::deleteText(startOffset, endOffset);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::insertText(int offset, const QString
  //      &text)
  void insertText(int offset, const QString &text) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall20 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall20>(taken[20]);
      call(this, offset, &text, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::insertText(offset, text);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  void QAccessibleAbstractSpinBox::replaceText(int startOffset, int
  //      endOffset, const QString &text)
  void replaceText(
      int startOffset,
      int endOffset,
      const QString &text) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall21 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall21>(taken[21]);
      call(this, startOffset, endOffset, &text, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSpinBox::replaceText(startOffset, endOffset, text);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall22 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall22>(taken[22]);
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
      CuteQAccessibleAbstractSpinBoxCall23 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall23>(taken[23]);
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
      CuteQAccessibleAbstractSpinBoxCall24 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall24>(taken[24]);
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
      CuteQAccessibleAbstractSpinBoxCall25 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall25>(taken[25]);
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
      CuteQAccessibleAbstractSpinBoxCall26 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall26>(taken[26]);
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
      CuteQAccessibleAbstractSpinBoxCall27 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall27>(taken[27]);
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
      CuteQAccessibleAbstractSpinBoxCall28 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall28>(taken[28]);
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
      CuteQAccessibleAbstractSpinBoxCall29 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall29>(taken[29]);
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
      CuteQAccessibleAbstractSpinBoxCall30 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall30>(taken[30]);
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
      CuteQAccessibleAbstractSpinBoxCall31 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall31>(taken[31]);
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
      CuteQAccessibleAbstractSpinBoxCall32 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall32>(taken[32]);
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
      CuteQAccessibleAbstractSpinBoxCall33 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall33>(taken[33]);
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
      CuteQAccessibleAbstractSpinBoxCall34 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall34>(taken[34]);
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
      CuteQAccessibleAbstractSpinBoxCall35 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall36 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall36>(taken[36]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleAbstractSpinBoxCall37 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall37>(taken[37]);
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
      CuteQAccessibleAbstractSpinBoxCall38 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall38>(taken[38]);
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
      CuteQAccessibleAbstractSpinBoxCall39 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall39>(taken[39]);
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
      CuteQAccessibleAbstractSpinBoxCall40 call = reinterpret_cast<CuteQAccessibleAbstractSpinBoxCall40>(taken[40]);
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

//  QAccessibleAbstractSpinBox::~QAccessibleAbstractSpinBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBoxD1Ev(
    QAccessibleAbstractSpinBox *self) {
  delete self;
}

//  QAccessible::State QAccessibleAbstractSpinBox::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK26QAccessibleAbstractSpinBox5stateEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QAccessible::State(self->state());
}

//  QString QAccessibleAbstractSpinBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleAbstractSpinBox4textEN11QAccessible4TextE(
    const QAccessibleAbstractSpinBox *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  void
//      *QAccessibleAbstractSpinBox::interface_cast(QAccessible::InterfaceTyp
//      e t)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QAccessibleAbstractSpinBox14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleAbstractSpinBox *self,
    QAccessible::InterfaceType t) {
  return self->interface_cast(t);
}

//  QVariant QAccessibleAbstractSpinBox::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QAccessibleAbstractSpinBox12currentValueEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->currentValue());
}

//  void QAccessibleAbstractSpinBox::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox15setCurrentValueERK8QVariant(
    QAccessibleAbstractSpinBox *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QAccessibleAbstractSpinBox::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QAccessibleAbstractSpinBox12maximumValueEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleAbstractSpinBox::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QAccessibleAbstractSpinBox12minimumValueEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleAbstractSpinBox::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QAccessibleAbstractSpinBox15minimumStepSizeEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->minimumStepSize());
}

//  void QAccessibleAbstractSpinBox::addSelection(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox12addSelectionEii(
    QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset) {
  self->addSelection(startOffset, endOffset);
}

//  QString QAccessibleAbstractSpinBox::attributes(int offset, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleAbstractSpinBox10attributesEiPiS0_(
    const QAccessibleAbstractSpinBox *self,
    int offset,
    int *startOffset,
    int *endOffset) {
  return new QString(self->attributes(offset, startOffset, endOffset));
}

//  int QAccessibleAbstractSpinBox::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleAbstractSpinBox14cursorPositionEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->cursorPosition();
}

//  QRect QAccessibleAbstractSpinBox::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK26QAccessibleAbstractSpinBox13characterRectEi(
    const QAccessibleAbstractSpinBox *self,
    int offset) {
  return new QRect(self->characterRect(offset));
}

//  int QAccessibleAbstractSpinBox::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleAbstractSpinBox14selectionCountEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->selectionCount();
}

//  int QAccessibleAbstractSpinBox::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleAbstractSpinBox13offsetAtPointERK6QPoint(
    const QAccessibleAbstractSpinBox *self,
    const QPoint *point) {
  return self->offsetAtPoint(*point);
}

//  void QAccessibleAbstractSpinBox::selection(int selectionIndex, int
//      *startOffset, int *endOffset) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK26QAccessibleAbstractSpinBox9selectionEiPiS0_(
    const QAccessibleAbstractSpinBox *self,
    int selectionIndex,
    int *startOffset,
    int *endOffset) {
  self->selection(selectionIndex, startOffset, endOffset);
}

//  QString QAccessibleAbstractSpinBox::text(int startOffset, int endOffset)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleAbstractSpinBox4textEii(
    const QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset) {
  return new QString(self->text(startOffset, endOffset));
}

//  QString QAccessibleAbstractSpinBox::textBeforeOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *endOffset, int
//      *startOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleAbstractSpinBox16textBeforeOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleAbstractSpinBox *self,
    int offset,
    QAccessible::TextBoundaryType boundaryType,
    int *endOffset,
    int *startOffset) {
  return new QString(
      self->textBeforeOffset(
          offset,
          boundaryType,
          endOffset,
          startOffset));
}

//  QString QAccessibleAbstractSpinBox::textAfterOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleAbstractSpinBox15textAfterOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleAbstractSpinBox *self,
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

//  QString QAccessibleAbstractSpinBox::textAtOffset(int offset,
//      QAccessible::TextBoundaryType boundaryType, int *startOffset, int
//      *endOffset) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QAccessibleAbstractSpinBox12textAtOffsetEiN11QAccessible16TextBoundaryTypeEPiS2_(
    const QAccessibleAbstractSpinBox *self,
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

//  void QAccessibleAbstractSpinBox::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox15removeSelectionEi(
    QAccessibleAbstractSpinBox *self,
    int selectionIndex) {
  self->removeSelection(selectionIndex);
}

//  void QAccessibleAbstractSpinBox::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox17setCursorPositionEi(
    QAccessibleAbstractSpinBox *self,
    int position) {
  self->setCursorPosition(position);
}

//  void QAccessibleAbstractSpinBox::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox12setSelectionEiii(
    QAccessibleAbstractSpinBox *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->setSelection(selectionIndex, startOffset, endOffset);
}

//  int QAccessibleAbstractSpinBox::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QAccessibleAbstractSpinBox14characterCountEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->characterCount();
}

//  void QAccessibleAbstractSpinBox::scrollToSubstring(int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox17scrollToSubstringEii(
    QAccessibleAbstractSpinBox *self,
    int startIndex,
    int endIndex) {
  self->scrollToSubstring(startIndex, endIndex);
}

//  void QAccessibleAbstractSpinBox::deleteText(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox10deleteTextEii(
    QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset) {
  self->deleteText(startOffset, endOffset);
}

//  void QAccessibleAbstractSpinBox::insertText(int offset, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox10insertTextEiRK7QString(
    QAccessibleAbstractSpinBox *self,
    int offset,
    const QString *text) {
  self->insertText(offset, *text);
}

//  void QAccessibleAbstractSpinBox::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAccessibleAbstractSpinBox11replaceTextEiiRK7QString(
    QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->replaceText(startOffset, endOffset, *text);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QAbstractSpinBox *QAccessibleAbstractSpinBox::abstractSpinBox() const
extern "C" Q_DECL_EXPORT
QAbstractSpinBox *ritual_ZNK26QAccessibleAbstractSpinBox15abstractSpinBoxEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->abstractSpinBox();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  QAccessibleInterface *QAccessibleAbstractSpinBox::lineEditIface() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK26QAccessibleAbstractSpinBox13lineEditIfaceEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->lineEditIface();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleAbstractSpinBox as the QAccessibleValueInterface it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessibleValueInterface *ritual_cast_QAccessibleAbstractSpinBox_QAccessibleValueInterface(
    QAccessibleAbstractSpinBox *self) {
  return static_cast<QAccessibleValueInterface *>(self);
}

//  QAccessibleAbstractSpinBox as the QAccessibleTextInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleTextInterface *ritual_cast_QAccessibleAbstractSpinBox_QAccessibleTextInterface(
    QAccessibleAbstractSpinBox *self) {
  return static_cast<QAccessibleTextInterface *>(self);
}

//  QAccessibleAbstractSpinBox as the QAccessibleEditableTextInterface it is
//      built on
extern "C" Q_DECL_EXPORT
QAccessibleEditableTextInterface *ritual_cast_QAccessibleAbstractSpinBox_QAccessibleEditableTextInterface(
    QAccessibleAbstractSpinBox *self) {
  return static_cast<QAccessibleEditableTextInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleAbstractSpinBox, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleAbstractSpinBox(
    QAccessibleAbstractSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleAbstractSpinBox *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QAccessible::State QAccessibleAbstractSpinBox::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK26QAccessibleAbstractSpinBox5stateEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QAccessible::State(self->QAccessibleAbstractSpinBox::state());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QString QAccessibleAbstractSpinBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QAccessibleAbstractSpinBox4textEN11QAccessible4TextE(
    const QAccessibleAbstractSpinBox *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleAbstractSpinBox::text(t));
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  void
//      *QAccessibleAbstractSpinBox::interface_cast(QAccessible::InterfaceTyp
//      e t)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN26QAccessibleAbstractSpinBox14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleAbstractSpinBox *self,
    QAccessible::InterfaceType t) {
  return self->QAccessibleAbstractSpinBox::interface_cast(t);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QVariant QAccessibleAbstractSpinBox::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK26QAccessibleAbstractSpinBox12currentValueEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->QAccessibleAbstractSpinBox::currentValue());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox15setCurrentValueERK8QVariant(
    QAccessibleAbstractSpinBox *self,
    const QVariant *value) {
  self->QAccessibleAbstractSpinBox::setCurrentValue(*value);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QVariant QAccessibleAbstractSpinBox::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK26QAccessibleAbstractSpinBox12maximumValueEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->QAccessibleAbstractSpinBox::maximumValue());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QVariant QAccessibleAbstractSpinBox::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK26QAccessibleAbstractSpinBox12minimumValueEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->QAccessibleAbstractSpinBox::minimumValue());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QVariant QAccessibleAbstractSpinBox::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK26QAccessibleAbstractSpinBox15minimumStepSizeEv(
    const QAccessibleAbstractSpinBox *self) {
  return new QVariant(self->QAccessibleAbstractSpinBox::minimumStepSize());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::addSelection(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox12addSelectionEii(
    QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleAbstractSpinBox::addSelection(startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  int QAccessibleAbstractSpinBox::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleAbstractSpinBox14cursorPositionEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->QAccessibleAbstractSpinBox::cursorPosition();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  QRect QAccessibleAbstractSpinBox::characterRect(int offset) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK26QAccessibleAbstractSpinBox13characterRectEi(
    const QAccessibleAbstractSpinBox *self,
    int offset) {
  return new QRect(self->QAccessibleAbstractSpinBox::characterRect(offset));
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  int QAccessibleAbstractSpinBox::selectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleAbstractSpinBox14selectionCountEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->QAccessibleAbstractSpinBox::selectionCount();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  int QAccessibleAbstractSpinBox::offsetAtPoint(const QPoint &point) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleAbstractSpinBox13offsetAtPointERK6QPoint(
    const QAccessibleAbstractSpinBox *self,
    const QPoint *point) {
  return self->QAccessibleAbstractSpinBox::offsetAtPoint(*point);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  QString QAccessibleAbstractSpinBox::text(int startOffset, int endOffset)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK26QAccessibleAbstractSpinBox4textEii(
    const QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset) {
  return new QString(
      self->QAccessibleAbstractSpinBox::text(
          startOffset,
          endOffset));
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::removeSelection(int selectionIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox15removeSelectionEi(
    QAccessibleAbstractSpinBox *self,
    int selectionIndex) {
  self->QAccessibleAbstractSpinBox::removeSelection(selectionIndex);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::setCursorPosition(int position)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox17setCursorPositionEi(
    QAccessibleAbstractSpinBox *self,
    int position) {
  self->QAccessibleAbstractSpinBox::setCursorPosition(position);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::setSelection(int selectionIndex, int
//      startOffset, int endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox12setSelectionEiii(
    QAccessibleAbstractSpinBox *self,
    int selectionIndex,
    int startOffset,
    int endOffset) {
  self->QAccessibleAbstractSpinBox::setSelection(
      selectionIndex,
      startOffset,
      endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  int QAccessibleAbstractSpinBox::characterCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK26QAccessibleAbstractSpinBox14characterCountEv(
    const QAccessibleAbstractSpinBox *self) {
  return self->QAccessibleAbstractSpinBox::characterCount();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::scrollToSubstring(int startIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox17scrollToSubstringEii(
    QAccessibleAbstractSpinBox *self,
    int startIndex,
    int endIndex) {
  self->QAccessibleAbstractSpinBox::scrollToSubstring(startIndex, endIndex);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::deleteText(int startOffset, int
//      endOffset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox10deleteTextEii(
    QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset) {
  self->QAccessibleAbstractSpinBox::deleteText(startOffset, endOffset);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::insertText(int offset, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox10insertTextEiRK7QString(
    QAccessibleAbstractSpinBox *self,
    int offset,
    const QString *text) {
  self->QAccessibleAbstractSpinBox::insertText(offset, *text);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(lineedit)
#if QT_CONFIG(spinbox)
//  void QAccessibleAbstractSpinBox::replaceText(int startOffset, int
//      endOffset, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QAccessibleAbstractSpinBox11replaceTextEiiRK7QString(
    QAccessibleAbstractSpinBox *self,
    int startOffset,
    int endOffset,
    const QString *text) {
  self->QAccessibleAbstractSpinBox::replaceText(
      startOffset,
      endOffset,
      *text);
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(lineedit)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
