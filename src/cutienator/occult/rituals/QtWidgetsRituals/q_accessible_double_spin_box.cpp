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
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
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

//  from src/widgets/accessible/rangecontrols.cpp, line 44, as _ZN26QAccessibleAbstractSpinBoxC2EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QAccessibleAbstractSpinBox::QAccessibleAbstractSpinBox(QWidget *w)
    : QAccessibleWidgetV2(w, QAccessible::SpinBox), lineEdit(nullptr)
{
    Q_ASSERT(abstractSpinBox());
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

//  from src/widgets/accessible/rangecontrols.cpp, line 273, as _ZNK24QAccessibleDoubleSpinBox4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QString QAccessibleDoubleSpinBox::text(QAccessible::Text textType) const
{
    if (textType == QAccessible::Value)
        return doubleSpinBox()->textFromValue(doubleSpinBox()->value());
    return QAccessibleWidgetV2::text(textType);
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

//  from src/widgets/accessible/rangecontrols.cpp, line 268, as _ZNK24QAccessibleDoubleSpinBox13doubleSpinBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QDoubleSpinBox *QAccessibleDoubleSpinBox::doubleSpinBox() const
{
    return static_cast<QDoubleSpinBox*>(object());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleDoubleSpinBox that Python can take functions over in. Every QAccessibleDoubleSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleDoubleSpinBoxCall0)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QAccessible::State * (*CuteQAccessibleDoubleSpinBoxCall1)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall2)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleDoubleSpinBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall4)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleDoubleSpinBoxCall5)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleDoubleSpinBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleDoubleSpinBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleDoubleSpinBoxCall9)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QRect * (*CuteQAccessibleDoubleSpinBoxCall10)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleDoubleSpinBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleDoubleSpinBoxCall12)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleDoubleSpinBoxCall13)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall14)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall15)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall16)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleDoubleSpinBoxCall17)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall20)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleDoubleSpinBoxCall21)(const void *, int, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleDoubleSpinBoxCall22)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleDoubleSpinBoxCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDoubleSpinBoxCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDoubleSpinBoxCall26)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleDoubleSpinBoxCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall29)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall30)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleDoubleSpinBoxCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDoubleSpinBoxCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleDoubleSpinBoxCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDoubleSpinBoxCall34)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDoubleSpinBoxCall36)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleDoubleSpinBoxCall37)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleDoubleSpinBoxCall38)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDoubleSpinBoxCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleDoubleSpinBoxCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleDoubleSpinBox : public QAccessibleDoubleSpinBox {
public:
  using QAccessibleDoubleSpinBox::QAccessibleDoubleSpinBox;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
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
  //  QString QAccessibleDoubleSpinBox::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleDoubleSpinBoxCall0 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall0>(taken[0]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleDoubleSpinBox::text(t);
  }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
  //  QAccessible::State QAccessibleAbstractSpinBox::state() const
  QAccessible::State state() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleDoubleSpinBoxCall1 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall1>(taken[1]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSpinBox::state();
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
      CuteQAccessibleDoubleSpinBoxCall2 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall2>(taken[2]);
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
      CuteQAccessibleDoubleSpinBoxCall3 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall3>(taken[3]);
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
      CuteQAccessibleDoubleSpinBoxCall4 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall4>(taken[4]);
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
      CuteQAccessibleDoubleSpinBoxCall5 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall5>(taken[5]);
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
      CuteQAccessibleDoubleSpinBoxCall6 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall6>(taken[6]);
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
      CuteQAccessibleDoubleSpinBoxCall7 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall7>(taken[7]);
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
      CuteQAccessibleDoubleSpinBoxCall8 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall8>(taken[8]);
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
      CuteQAccessibleDoubleSpinBoxCall9 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall9>(taken[9]);
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
      CuteQAccessibleDoubleSpinBoxCall10 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall10>(taken[10]);
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
      CuteQAccessibleDoubleSpinBoxCall11 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall11>(taken[11]);
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
      CuteQAccessibleDoubleSpinBoxCall12 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall12>(taken[12]);
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
      CuteQAccessibleDoubleSpinBoxCall13 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall13>(taken[13]);
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
      CuteQAccessibleDoubleSpinBoxCall14 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall14>(taken[14]);
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
      CuteQAccessibleDoubleSpinBoxCall15 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall15>(taken[15]);
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
      CuteQAccessibleDoubleSpinBoxCall16 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall16>(taken[16]);
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
      CuteQAccessibleDoubleSpinBoxCall17 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall17>(taken[17]);
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
      CuteQAccessibleDoubleSpinBoxCall18 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall18>(taken[18]);
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
      CuteQAccessibleDoubleSpinBoxCall19 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall19>(taken[19]);
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
      CuteQAccessibleDoubleSpinBoxCall20 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall20>(taken[20]);
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
      CuteQAccessibleDoubleSpinBoxCall21 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall21>(taken[21]);
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
      CuteQAccessibleDoubleSpinBoxCall22 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall22>(taken[22]);
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
      CuteQAccessibleDoubleSpinBoxCall23 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall23>(taken[23]);
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
      CuteQAccessibleDoubleSpinBoxCall24 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall24>(taken[24]);
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
      CuteQAccessibleDoubleSpinBoxCall25 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall25>(taken[25]);
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
      CuteQAccessibleDoubleSpinBoxCall26 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall26>(taken[26]);
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
      CuteQAccessibleDoubleSpinBoxCall27 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall27>(taken[27]);
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
      CuteQAccessibleDoubleSpinBoxCall28 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall28>(taken[28]);
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
      CuteQAccessibleDoubleSpinBoxCall29 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall29>(taken[29]);
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
      CuteQAccessibleDoubleSpinBoxCall30 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall30>(taken[30]);
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
      CuteQAccessibleDoubleSpinBoxCall31 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall31>(taken[31]);
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
      CuteQAccessibleDoubleSpinBoxCall32 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall32>(taken[32]);
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
      CuteQAccessibleDoubleSpinBoxCall33 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall33>(taken[33]);
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
      CuteQAccessibleDoubleSpinBoxCall34 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall34>(taken[34]);
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
      CuteQAccessibleDoubleSpinBoxCall35 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall35>(taken[35]);
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
      CuteQAccessibleDoubleSpinBoxCall36 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall36>(taken[36]);
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
      CuteQAccessibleDoubleSpinBoxCall37 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall37>(taken[37]);
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
      CuteQAccessibleDoubleSpinBoxCall38 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall38>(taken[38]);
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
      CuteQAccessibleDoubleSpinBoxCall39 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall39>(taken[39]);
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
      CuteQAccessibleDoubleSpinBoxCall40 call = reinterpret_cast<CuteQAccessibleDoubleSpinBoxCall40>(taken[40]);
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

//  QString QAccessibleDoubleSpinBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QAccessibleDoubleSpinBox4textEN11QAccessible4TextE(
    const QAccessibleDoubleSpinBox *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QDoubleSpinBox *QAccessibleDoubleSpinBox::doubleSpinBox() const
extern "C" Q_DECL_EXPORT
QDoubleSpinBox *ritual_ZNK24QAccessibleDoubleSpinBox13doubleSpinBoxEv(
    const QAccessibleDoubleSpinBox *self) {
  return self->doubleSpinBox();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleDoubleSpinBox, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleDoubleSpinBox(
    QAccessibleDoubleSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleDoubleSpinBox *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QString QAccessibleDoubleSpinBox::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QAccessibleDoubleSpinBox4textEN11QAccessible4TextE(
    const QAccessibleDoubleSpinBox *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleDoubleSpinBox::text(t));
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
