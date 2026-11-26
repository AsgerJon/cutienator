//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qaccessible.h>
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

//  from src/widgets/accessible/rangecontrols.cpp, line 357, as _ZN25QAccessibleAbstractSlider14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline void *QAccessibleAbstractSlider::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::ValueInterface)
        return static_cast<QAccessibleValueInterface*>(this);
    return QAccessibleWidgetV2::interface_cast(t);
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 385, as _ZN25QAccessibleAbstractSlider15setCurrentValueERK8QVariant
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline void QAccessibleAbstractSlider::setCurrentValue(const QVariant &value)
{
    abstractSlider()->setValue(value.toInt());
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 351, as _ZN25QAccessibleAbstractSliderC2EP7QWidgetN11QAccessible4RoleE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QAccessibleAbstractSlider::QAccessibleAbstractSlider(QWidget *w, QAccessible::Role r)
    : QAccessibleWidgetV2(w, r)
{
    Q_ASSERT(qobject_cast<QAbstractSlider *>(w));
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 308, as _ZNK20QAccessibleScrollBar4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
inline QString QAccessibleScrollBar::text(QAccessible::Text t) const
{
    if (t == QAccessible::Value)
        return QString::number(scrollBar()->value());
    return QAccessibleAbstractSlider::text(t);
}
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 380, as _ZNK25QAccessibleAbstractSlider12currentValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::currentValue() const
{
    return abstractSlider()->value();
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 390, as _ZNK25QAccessibleAbstractSlider12maximumValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::maximumValue() const
{
    return abstractSlider()->maximum();
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 395, as _ZNK25QAccessibleAbstractSlider12minimumValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::minimumValue() const
{
    return abstractSlider()->minimum();
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 364, as _ZNK25QAccessibleAbstractSlider13attributeKeysEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QList<QAccessible::Attribute> QAccessibleAbstractSlider::attributeKeys() const
{
    QList<QAccessible::Attribute> keys = QAccessibleWidgetV2::attributeKeys();
    keys.append(QAccessible::Attribute::Orientation);

    return keys;
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 372, as _ZNK25QAccessibleAbstractSlider14attributeValueEN11QAccessible9AttributeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute key) const
{
    if (key == QAccessible::Attribute::Orientation)
        return QVariant::fromValue(abstractSlider()->orientation());

    return QAccessibleWidgetV2::attributeValue(key);
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 400, as _ZNK25QAccessibleAbstractSlider15minimumStepSizeEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::minimumStepSize() const
{
    return abstractSlider()->singleStep();
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 303, as _ZNK20QAccessibleScrollBar9scrollBarEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
inline QScrollBar *QAccessibleScrollBar::scrollBar() const
{
    return qobject_cast<QScrollBar*>(object());
}
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleScrollBar that Python can take functions over in. Every QAccessibleScrollBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
typedef QString * (*CuteQAccessibleScrollBarCall0)(const void *, int, int *);
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef void * (*CuteQAccessibleScrollBarCall1)(const void *, int, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleScrollBarCall2)(const void *, int, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleScrollBarCall3)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef void (*CuteQAccessibleScrollBarCall4)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleScrollBarCall5)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleScrollBarCall6)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleScrollBarCall7)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleScrollBarCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollBarCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleScrollBarCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleScrollBarCall11)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollBarCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleScrollBarCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollBarCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollBarCall15)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleScrollBarCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleScrollBarCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleScrollBarCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleScrollBarCall19)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleScrollBarCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollBarCall21)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleScrollBarCall22)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollBarCall23)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleScrollBarCall24)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleScrollBarCall25)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleScrollBarCall26)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleScrollBar : public QAccessibleScrollBar {
public:
  using QAccessibleScrollBar::QAccessibleScrollBar;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
  //  QString QAccessibleScrollBar::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall0 call = reinterpret_cast<CuteQAccessibleScrollBarCall0>(taken[0]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleScrollBar::text(t);
  }
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  void
  //      *QAccessibleAbstractSlider::interface_cast(QAccessible::Interface
  //      Type t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall1 call = reinterpret_cast<CuteQAccessibleScrollBarCall1>(taken[1]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleAbstractSlider::interface_cast(t);
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  QVariant
  //      QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall2 call = reinterpret_cast<CuteQAccessibleScrollBarCall2>(taken[2]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSlider::attributeValue(key);
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  QVariant QAccessibleAbstractSlider::currentValue() const
  QVariant currentValue() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall3 call = reinterpret_cast<CuteQAccessibleScrollBarCall3>(taken[3]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSlider::currentValue();
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  void QAccessibleAbstractSlider::setCurrentValue(const QVariant
  //      &value)
  void setCurrentValue(const QVariant &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall4 call = reinterpret_cast<CuteQAccessibleScrollBarCall4>(taken[4]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QAccessibleAbstractSlider::setCurrentValue(value);
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  QVariant QAccessibleAbstractSlider::maximumValue() const
  QVariant maximumValue() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall5 call = reinterpret_cast<CuteQAccessibleScrollBarCall5>(taken[5]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSlider::maximumValue();
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  QVariant QAccessibleAbstractSlider::minimumValue() const
  QVariant minimumValue() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall6 call = reinterpret_cast<CuteQAccessibleScrollBarCall6>(taken[6]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSlider::minimumValue();
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  QVariant QAccessibleAbstractSlider::minimumStepSize() const
  QVariant minimumStepSize() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall7 call = reinterpret_cast<CuteQAccessibleScrollBarCall7>(taken[7]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleAbstractSlider::minimumStepSize();
  }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall8 call = reinterpret_cast<CuteQAccessibleScrollBarCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall9 call = reinterpret_cast<CuteQAccessibleScrollBarCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall10 call = reinterpret_cast<CuteQAccessibleScrollBarCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall11 call = reinterpret_cast<CuteQAccessibleScrollBarCall11>(taken[11]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall12 call = reinterpret_cast<CuteQAccessibleScrollBarCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall13 call = reinterpret_cast<CuteQAccessibleScrollBarCall13>(taken[13]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall14 call = reinterpret_cast<CuteQAccessibleScrollBarCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall15 call = reinterpret_cast<CuteQAccessibleScrollBarCall15>(taken[15]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall16 call = reinterpret_cast<CuteQAccessibleScrollBarCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall17 call = reinterpret_cast<CuteQAccessibleScrollBarCall17>(taken[17]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall18 call = reinterpret_cast<CuteQAccessibleScrollBarCall18>(taken[18]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall19 call = reinterpret_cast<CuteQAccessibleScrollBarCall19>(taken[19]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall20 call = reinterpret_cast<CuteQAccessibleScrollBarCall20>(taken[20]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall21 call = reinterpret_cast<CuteQAccessibleScrollBarCall21>(taken[21]);
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
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall22 call = reinterpret_cast<CuteQAccessibleScrollBarCall22>(taken[22]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall23 call = reinterpret_cast<CuteQAccessibleScrollBarCall23>(taken[23]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall24 call = reinterpret_cast<CuteQAccessibleScrollBarCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall25 call = reinterpret_cast<CuteQAccessibleScrollBarCall25>(taken[25]);
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
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleScrollBarCall26 call = reinterpret_cast<CuteQAccessibleScrollBarCall26>(taken[26]);
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

//  QString QAccessibleScrollBar::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QAccessibleScrollBar4textEN11QAccessible4TextE(
    const QAccessibleScrollBar *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
//  QScrollBar *QAccessibleScrollBar::scrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK20QAccessibleScrollBar9scrollBarEv(
    const QAccessibleScrollBar *self) {
  return self->scrollBar();
}
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleScrollBar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleScrollBar(
    QAccessibleScrollBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleScrollBar *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollbar)
//  QString QAccessibleScrollBar::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QAccessibleScrollBar4textEN11QAccessible4TextE(
    const QAccessibleScrollBar *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleScrollBar::text(t));
}
#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(scrollbar)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
