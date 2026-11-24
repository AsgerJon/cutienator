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
typedef const QVariant * (*CuteQAccessibleSpinBoxCall2)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall3)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall4)(const void *, int *);
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
typedef void (*CuteQAccessibleSpinBoxCall7)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall8)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef const QRect * (*CuteQAccessibleSpinBoxCall9)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall10)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall11)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef QString * (*CuteQAccessibleSpinBoxCall12)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall13)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall14)(const void *, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall15)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef int (*CuteQAccessibleSpinBoxCall16)(const void *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall17)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall19)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
typedef void (*CuteQAccessibleSpinBoxCall20)(const void *, int, int, const QString *, int *);
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleSpinBoxCall21)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleSpinBoxCall22)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleSpinBoxCall24)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleSpinBoxCall25)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall26)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleSpinBoxCall27)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall28)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall29)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleSpinBoxCall30)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleSpinBoxCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleSpinBoxCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleSpinBoxCall33)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall34)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleSpinBoxCall35)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleSpinBoxCall36)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleSpinBoxCall37)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleSpinBoxCall38)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleSpinBox : public QAccessibleSpinBox {
public:
  using QAccessibleSpinBox::QAccessibleSpinBox;
  void *taken[39] = {};

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
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10deleteTextEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface10insertTextEiRK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(spinbox)
    if (!std::strcmp(key, "_ZN32QAccessibleEditableTextInterface11replaceTextEiiRK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(spinbox)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
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
  //  QVariant QAccessibleAbstractSpinBox::currentValue() const
  QVariant currentValue() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall2 call = reinterpret_cast<CuteQAccessibleSpinBoxCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall3 call = reinterpret_cast<CuteQAccessibleSpinBoxCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall4 call = reinterpret_cast<CuteQAccessibleSpinBoxCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall5 call = reinterpret_cast<CuteQAccessibleSpinBoxCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall6 call = reinterpret_cast<CuteQAccessibleSpinBoxCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall7 call = reinterpret_cast<CuteQAccessibleSpinBoxCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall8 call = reinterpret_cast<CuteQAccessibleSpinBoxCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall9 call = reinterpret_cast<CuteQAccessibleSpinBoxCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall10 call = reinterpret_cast<CuteQAccessibleSpinBoxCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall11 call = reinterpret_cast<CuteQAccessibleSpinBoxCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall12 call = reinterpret_cast<CuteQAccessibleSpinBoxCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall13 call = reinterpret_cast<CuteQAccessibleSpinBoxCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall14 call = reinterpret_cast<CuteQAccessibleSpinBoxCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall15 call = reinterpret_cast<CuteQAccessibleSpinBoxCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall16 call = reinterpret_cast<CuteQAccessibleSpinBoxCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall17 call = reinterpret_cast<CuteQAccessibleSpinBoxCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall18 call = reinterpret_cast<CuteQAccessibleSpinBoxCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall19 call = reinterpret_cast<CuteQAccessibleSpinBoxCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall20 call = reinterpret_cast<CuteQAccessibleSpinBoxCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall21 call = reinterpret_cast<CuteQAccessibleSpinBoxCall21>(taken[21]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall22 call = reinterpret_cast<CuteQAccessibleSpinBoxCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall23 call = reinterpret_cast<CuteQAccessibleSpinBoxCall23>(taken[23]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall24 call = reinterpret_cast<CuteQAccessibleSpinBoxCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall25 call = reinterpret_cast<CuteQAccessibleSpinBoxCall25>(taken[25]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall26 call = reinterpret_cast<CuteQAccessibleSpinBoxCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall27 call = reinterpret_cast<CuteQAccessibleSpinBoxCall27>(taken[27]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall28 call = reinterpret_cast<CuteQAccessibleSpinBoxCall28>(taken[28]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall29 call = reinterpret_cast<CuteQAccessibleSpinBoxCall29>(taken[29]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleSpinBoxCall30 call = reinterpret_cast<CuteQAccessibleSpinBoxCall30>(taken[30]);
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
      CuteQAccessibleSpinBoxCall31 call = reinterpret_cast<CuteQAccessibleSpinBoxCall31>(taken[31]);
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
      CuteQAccessibleSpinBoxCall32 call = reinterpret_cast<CuteQAccessibleSpinBoxCall32>(taken[32]);
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
      CuteQAccessibleSpinBoxCall33 call = reinterpret_cast<CuteQAccessibleSpinBoxCall33>(taken[33]);
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
      CuteQAccessibleSpinBoxCall34 call = reinterpret_cast<CuteQAccessibleSpinBoxCall34>(taken[34]);
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
      CuteQAccessibleSpinBoxCall35 call = reinterpret_cast<CuteQAccessibleSpinBoxCall35>(taken[35]);
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
      CuteQAccessibleSpinBoxCall36 call = reinterpret_cast<CuteQAccessibleSpinBoxCall36>(taken[36]);
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
      CuteQAccessibleSpinBoxCall37 call = reinterpret_cast<CuteQAccessibleSpinBoxCall37>(taken[37]);
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
      CuteQAccessibleSpinBoxCall38 call = reinterpret_cast<CuteQAccessibleSpinBoxCall38>(taken[38]);
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
