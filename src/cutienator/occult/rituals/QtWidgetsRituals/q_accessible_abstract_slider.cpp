//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/rangecontrols_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/accessible/rangecontrols.cpp, line 380, as _ZNK25QAccessibleAbstractSlider12currentValueEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::currentValue() const
{
    return abstractSlider()->value();
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

//  from src/widgets/accessible/rangecontrols.cpp, line 400, as _ZNK25QAccessibleAbstractSlider15minimumStepSizeEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QVariant QAccessibleAbstractSlider::minimumStepSize() const
{
    return abstractSlider()->singleStep();
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/rangecontrols.cpp, line 405, as _ZNK25QAccessibleAbstractSlider14abstractSliderEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
inline QAbstractSlider *QAccessibleAbstractSlider::abstractSlider() const
{
    return static_cast<QAbstractSlider *>(object());
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleAbstractSlider that Python can take functions over in. Every QAccessibleAbstractSlider
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleAbstractSliderCall0)(const void *, int, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleAbstractSliderCall1)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef void (*CuteQAccessibleAbstractSliderCall2)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleAbstractSliderCall3)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleAbstractSliderCall4)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
typedef const QVariant * (*CuteQAccessibleAbstractSliderCall5)(const void *, int *);
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleAbstractSliderCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSliderCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleAbstractSliderCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleAbstractSliderCall9)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSliderCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleAbstractSliderCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSliderCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSliderCall13)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleAbstractSliderCall14)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleAbstractSliderCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleAbstractSliderCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleAbstractSliderCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleAbstractSliderCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleAbstractSliderCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSliderCall20)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleAbstractSliderCall21)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleAbstractSliderCall22)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleAbstractSliderCall23)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleAbstractSliderCall24)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleAbstractSlider : public QAccessibleAbstractSlider {
public:
  using QAccessibleAbstractSlider::QAccessibleAbstractSlider;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
  //  QVariant
  //      QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall0 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall1 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall2 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall3 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall4 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall5 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall6 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall7 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleWidget::childCount() const
  int childCount() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall8 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall9 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall9>(taken[9]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::indexOfChild(child);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall10 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall11 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall11>(taken[11]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall12 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall13 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall13>(taken[13]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall14 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall15 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall16 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall16>(taken[16]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall17 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall17>(taken[17]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall18 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall18>(taken[18]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall19 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall19>(taken[19]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall20 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall21 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall21>(taken[21]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall22 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall22>(taken[22]);
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
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall23 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleAbstractSliderCall24 call = reinterpret_cast<CuteQAccessibleAbstractSliderCall24>(taken[24]);
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

//  QVariant QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleAbstractSlider14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleAbstractSlider *self,
    QAccessible::Attribute key) {
  return new QVariant(self->attributeValue(key));
}

//  QVariant QAccessibleAbstractSlider::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleAbstractSlider12currentValueEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->currentValue());
}

//  void QAccessibleAbstractSlider::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleAbstractSlider15setCurrentValueERK8QVariant(
    QAccessibleAbstractSlider *self,
    const QVariant *value) {
  self->setCurrentValue(*value);
}

//  QVariant QAccessibleAbstractSlider::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleAbstractSlider12maximumValueEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->maximumValue());
}

//  QVariant QAccessibleAbstractSlider::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleAbstractSlider12minimumValueEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->minimumValue());
}

//  QVariant QAccessibleAbstractSlider::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QAccessibleAbstractSlider15minimumStepSizeEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->minimumStepSize());
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  QAbstractSlider *QAccessibleAbstractSlider::abstractSlider() const
extern "C" Q_DECL_EXPORT
QAbstractSlider *ritual_ZNK25QAccessibleAbstractSlider14abstractSliderEv(
    const QAccessibleAbstractSlider *self) {
  return self->abstractSlider();
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleAbstractSlider as the QAccessibleValueInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleValueInterface *ritual_cast_QAccessibleAbstractSlider_QAccessibleValueInterface(
    QAccessibleAbstractSlider *self) {
  return static_cast<QAccessibleValueInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleAbstractSlider, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleAbstractSlider(
    QAccessibleAbstractSlider *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleAbstractSlider *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  QVariant QAccessibleAbstractSlider::attributeValue(QAccessible::Attribute
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleAbstractSlider14attributeValueEN11QAccessible9AttributeE(
    const QAccessibleAbstractSlider *self,
    QAccessible::Attribute key) {
  return new QVariant(self->QAccessibleAbstractSlider::attributeValue(key));
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  QVariant QAccessibleAbstractSlider::currentValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleAbstractSlider12currentValueEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->QAccessibleAbstractSlider::currentValue());
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  void QAccessibleAbstractSlider::setCurrentValue(const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAccessibleAbstractSlider15setCurrentValueERK8QVariant(
    QAccessibleAbstractSlider *self,
    const QVariant *value) {
  self->QAccessibleAbstractSlider::setCurrentValue(*value);
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  QVariant QAccessibleAbstractSlider::maximumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleAbstractSlider12maximumValueEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->QAccessibleAbstractSlider::maximumValue());
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  QVariant QAccessibleAbstractSlider::minimumValue() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleAbstractSlider12minimumValueEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->QAccessibleAbstractSlider::minimumValue());
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(slider)
//  QVariant QAccessibleAbstractSlider::minimumStepSize() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QAccessibleAbstractSlider15minimumStepSizeEv(
    const QAccessibleAbstractSlider *self) {
  return new QVariant(self->QAccessibleAbstractSlider::minimumStepSize());
}
#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(slider)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
