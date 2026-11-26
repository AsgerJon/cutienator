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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from src/widgets/accessible/rangecontrols.cpp, line 245, as _ZNK18QAccessibleSpinBox7spinBoxEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
inline QSpinBox *QAccessibleSpinBox::spinBox() const
{
    return qobject_cast<QSpinBox*>(object());
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleSpinBox that Python can take functions over in. Every QAccessibleSpinBox
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QAccessible::State * (*CuteQAccessibleSpinBoxCall0)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleSpinBoxCall1)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void * (*CuteQAccessibleSpinBoxCall2)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall3)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall4)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall5)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall6)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall7)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall8)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall9)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QRect * (*CuteQAccessibleSpinBoxCall10)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall11)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall12)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleSpinBoxCall13)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall14)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall15)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall16)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall17)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall20)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall21)(const void *, int, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall22)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleSpinBoxCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleSpinBoxCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleSpinBoxCall26)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleSpinBoxCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall29)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall30)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleSpinBoxCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleSpinBoxCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleSpinBoxCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleSpinBoxCall34)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall35)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleSpinBoxCall36)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall37)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleSpinBoxCall38)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleSpinBoxCall39)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleSpinBoxCall40)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleSpinBox : public QAccessibleSpinBox {
public:
  using QAccessibleSpinBox::QAccessibleSpinBox;
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
      CuteQAccessibleSpinBoxCall0 call = reinterpret_cast<CuteQAccessibleSpinBoxCall0>(taken[0]);
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
      CuteQAccessibleSpinBoxCall1 call = reinterpret_cast<CuteQAccessibleSpinBoxCall1>(taken[1]);
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
      CuteQAccessibleSpinBoxCall2 call = reinterpret_cast<CuteQAccessibleSpinBoxCall2>(taken[2]);
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
      CuteQAccessibleSpinBoxCall3 call = reinterpret_cast<CuteQAccessibleSpinBoxCall3>(taken[3]);
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
      CuteQAccessibleSpinBoxCall4 call = reinterpret_cast<CuteQAccessibleSpinBoxCall4>(taken[4]);
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
      CuteQAccessibleSpinBoxCall5 call = reinterpret_cast<CuteQAccessibleSpinBoxCall5>(taken[5]);
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
      CuteQAccessibleSpinBoxCall6 call = reinterpret_cast<CuteQAccessibleSpinBoxCall6>(taken[6]);
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
      CuteQAccessibleSpinBoxCall7 call = reinterpret_cast<CuteQAccessibleSpinBoxCall7>(taken[7]);
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
      CuteQAccessibleSpinBoxCall8 call = reinterpret_cast<CuteQAccessibleSpinBoxCall8>(taken[8]);
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
      CuteQAccessibleSpinBoxCall9 call = reinterpret_cast<CuteQAccessibleSpinBoxCall9>(taken[9]);
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
      CuteQAccessibleSpinBoxCall10 call = reinterpret_cast<CuteQAccessibleSpinBoxCall10>(taken[10]);
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
      CuteQAccessibleSpinBoxCall11 call = reinterpret_cast<CuteQAccessibleSpinBoxCall11>(taken[11]);
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
      CuteQAccessibleSpinBoxCall12 call = reinterpret_cast<CuteQAccessibleSpinBoxCall12>(taken[12]);
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
      CuteQAccessibleSpinBoxCall13 call = reinterpret_cast<CuteQAccessibleSpinBoxCall13>(taken[13]);
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
      CuteQAccessibleSpinBoxCall14 call = reinterpret_cast<CuteQAccessibleSpinBoxCall14>(taken[14]);
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
      CuteQAccessibleSpinBoxCall15 call = reinterpret_cast<CuteQAccessibleSpinBoxCall15>(taken[15]);
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
      CuteQAccessibleSpinBoxCall16 call = reinterpret_cast<CuteQAccessibleSpinBoxCall16>(taken[16]);
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
      CuteQAccessibleSpinBoxCall17 call = reinterpret_cast<CuteQAccessibleSpinBoxCall17>(taken[17]);
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
      CuteQAccessibleSpinBoxCall18 call = reinterpret_cast<CuteQAccessibleSpinBoxCall18>(taken[18]);
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
      CuteQAccessibleSpinBoxCall19 call = reinterpret_cast<CuteQAccessibleSpinBoxCall19>(taken[19]);
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
      CuteQAccessibleSpinBoxCall20 call = reinterpret_cast<CuteQAccessibleSpinBoxCall20>(taken[20]);
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
      CuteQAccessibleSpinBoxCall21 call = reinterpret_cast<CuteQAccessibleSpinBoxCall21>(taken[21]);
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
      CuteQAccessibleSpinBoxCall22 call = reinterpret_cast<CuteQAccessibleSpinBoxCall22>(taken[22]);
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
      CuteQAccessibleSpinBoxCall23 call = reinterpret_cast<CuteQAccessibleSpinBoxCall23>(taken[23]);
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
      CuteQAccessibleSpinBoxCall24 call = reinterpret_cast<CuteQAccessibleSpinBoxCall24>(taken[24]);
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
      CuteQAccessibleSpinBoxCall25 call = reinterpret_cast<CuteQAccessibleSpinBoxCall25>(taken[25]);
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
      CuteQAccessibleSpinBoxCall26 call = reinterpret_cast<CuteQAccessibleSpinBoxCall26>(taken[26]);
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
      CuteQAccessibleSpinBoxCall27 call = reinterpret_cast<CuteQAccessibleSpinBoxCall27>(taken[27]);
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
      CuteQAccessibleSpinBoxCall28 call = reinterpret_cast<CuteQAccessibleSpinBoxCall28>(taken[28]);
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
      CuteQAccessibleSpinBoxCall29 call = reinterpret_cast<CuteQAccessibleSpinBoxCall29>(taken[29]);
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
      CuteQAccessibleSpinBoxCall30 call = reinterpret_cast<CuteQAccessibleSpinBoxCall30>(taken[30]);
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
      CuteQAccessibleSpinBoxCall31 call = reinterpret_cast<CuteQAccessibleSpinBoxCall31>(taken[31]);
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
      CuteQAccessibleSpinBoxCall32 call = reinterpret_cast<CuteQAccessibleSpinBoxCall32>(taken[32]);
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
      CuteQAccessibleSpinBoxCall33 call = reinterpret_cast<CuteQAccessibleSpinBoxCall33>(taken[33]);
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
      CuteQAccessibleSpinBoxCall34 call = reinterpret_cast<CuteQAccessibleSpinBoxCall34>(taken[34]);
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
      CuteQAccessibleSpinBoxCall35 call = reinterpret_cast<CuteQAccessibleSpinBoxCall35>(taken[35]);
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
      CuteQAccessibleSpinBoxCall36 call = reinterpret_cast<CuteQAccessibleSpinBoxCall36>(taken[36]);
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
      CuteQAccessibleSpinBoxCall37 call = reinterpret_cast<CuteQAccessibleSpinBoxCall37>(taken[37]);
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
      CuteQAccessibleSpinBoxCall38 call = reinterpret_cast<CuteQAccessibleSpinBoxCall38>(taken[38]);
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
      CuteQAccessibleSpinBoxCall39 call = reinterpret_cast<CuteQAccessibleSpinBoxCall39>(taken[39]);
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
      CuteQAccessibleSpinBoxCall40 call = reinterpret_cast<CuteQAccessibleSpinBoxCall40>(taken[40]);
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

#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
//  QSpinBox *QAccessibleSpinBox::spinBox() const
extern "C" Q_DECL_EXPORT
QSpinBox *ritual_ZNK18QAccessibleSpinBox7spinBoxEv(
    const QAccessibleSpinBox *self) {
  return self->spinBox();
}
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleSpinBox, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleSpinBox(
    QAccessibleSpinBox *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleSpinBox *>(self)->take(key, call);
}

#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
