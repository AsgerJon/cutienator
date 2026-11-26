//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qaccessiblequickpopupitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickpopupitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qaccessiblequickpopupitem_p.h>
#include <QtQuickTemplates2/private/qquickpopup_p.h>
#include <QtQuickTemplates2/private/qquickpopupitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickpopupitem.cpp, line 10, as _ZN25QAccessibleQuickPopupItemC1EP15QQuickPopupItem
inline QAccessibleQuickPopupItem::QAccessibleQuickPopupItem(QQuickPopupItem *popupItem)
    : QAccessibleQuickItem(popupItem)
{
}

//  from ../qtdeclarative/src/quicktemplates/accessible/qaccessiblequickpopupitem.cpp, line 15, as _ZNK25QAccessibleQuickPopupItem5stateEv
inline QAccessible::State QAccessibleQuickPopupItem::state() const
{
    QAccessible::State state = QAccessibleQuickItem::state();

    QQuickPopup *popup = qobject_cast<QQuickPopup *>(object()->parent());
    if (popup)
        state.modal = popup->isModal();

    return state;
}
//  -----------------------------------------------------------------------

//  A QAccessibleQuickPopupItem that Python can take functions over in. Every QAccessibleQuickPopupItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleQuickPopupItemCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleQuickPopupItemCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickPopupItemCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall6)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall8)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickPopupItemCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall11)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall12)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickPopupItemCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall14)(const void *, const QVariant *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickPopupItemCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickPopupItemCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickPopupItemCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall20)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall21)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall22)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall23)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickPopupItemCall24)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall25)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleQuickPopupItemCall26)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleQuickPopupItemCall27)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall28)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleQuickPopupItemCall29)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall30)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall31)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleQuickPopupItemCall32)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickPopupItemCall33)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleQuickPopupItemCall34)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleQuickPopupItemCall35)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickPopupItemCall36)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleQuickPopupItemCall37)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleQuickPopupItem : public QAccessibleQuickPopupItem {
public:
  using QAccessibleQuickPopupItem::QAccessibleQuickPopupItem;
  void *taken[38] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12currentValueEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN25QAccessibleValueInterface15setCurrentValueERK8QVariant")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12maximumValueEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface12minimumValueEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK25QAccessibleValueInterface15minimumStepSizeEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14selectionCountEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12addSelectionEii")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface15removeSelectionEi")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface12setSelectionEiii")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14cursorPositionEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17setCursorPositionEi")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface4textEii")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface14characterCountEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13characterRectEi")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAccessibleTextInterface13offsetAtPointERK6QPoint")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN24QAccessibleTextInterface17scrollToSubstringEii")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
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
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[37] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleQuickPopupItem::state() const
  QAccessible::State state() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall0 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall0>(taken[0]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickPopupItem::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleQuickItem::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall1 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleQuickItem::window() const
  QWindow *window() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall2 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleQuickItem::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleQuickItem::rect() const
  QRect rect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall3 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall3>(taken[3]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickItem::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall4 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall4>(taken[4]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickItem::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickItem::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall5 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickItem::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleQuickItem::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall6 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall6>(taken[6]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleQuickItem::child(index);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::childCount() const
  int childCount() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall7 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::childCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::indexOfChild(const QAccessibleInterface
  //      *iface) const
  int indexOfChild(const QAccessibleInterface *iface) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall8 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall8>(taken[8]);
      int given = call(this, iface, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::indexOfChild(iface);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleQuickItem::role() const
  QAccessible::Role role() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall9 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleQuickItem::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleQuickItem::text(QAccessible::Text a0) const
  QString text(QAccessible::Text a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall10 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall10>(taken[10]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleQuickItem::text(a0);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setText(QAccessible::Text a0, const
  //      QString &text)
  void setText(QAccessible::Text a0, const QString &text) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall11 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall11>(taken[11]);
      call(this, static_cast<int>(a0), &text, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setText(a0, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall12 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall12>(taken[12]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::currentValue() const
  QVariant currentValue() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall13 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall13>(taken[13]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::currentValue();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setCurrentValue(const QVariant &value)
  void setCurrentValue(const QVariant &value) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall14 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall14>(taken[14]);
      call(this, &value, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setCurrentValue(value);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::maximumValue() const
  QVariant maximumValue() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall15 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall15>(taken[15]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::maximumValue();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::minimumValue() const
  QVariant minimumValue() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall16 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall16>(taken[16]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::minimumValue();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::minimumStepSize() const
  QVariant minimumStepSize() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall17 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall17>(taken[17]);
      const QVariant * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::minimumStepSize();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::selectionCount() const
  int selectionCount() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall18 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::selectionCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::addSelection(int startOffset, int
  //      endOffset)
  void addSelection(int startOffset, int endOffset) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall19 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall19>(taken[19]);
      call(this, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::addSelection(startOffset, endOffset);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::removeSelection(int selectionIndex)
  void removeSelection(int selectionIndex) override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall20 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall20>(taken[20]);
      call(this, selectionIndex, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::removeSelection(selectionIndex);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setSelection(int selectionIndex, int
  //      startOffset, int endOffset)
  void setSelection(
      int selectionIndex,
      int startOffset,
      int endOffset) override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall21 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall21>(taken[21]);
      call(this, selectionIndex, startOffset, endOffset, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setSelection(selectionIndex, startOffset, endOffset);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::cursorPosition() const
  int cursorPosition() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall22 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall22>(taken[22]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::cursorPosition();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::setCursorPosition(int position)
  void setCursorPosition(int position) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall23 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall23>(taken[23]);
      call(this, position, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::setCursorPosition(position);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleQuickItem::text(int startOffset, int endOffset)
  //      const
  QString text(int startOffset, int endOffset) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall24 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall24>(taken[24]);
      QString * given = call(this, startOffset, endOffset, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleQuickItem::text(startOffset, endOffset);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::characterCount() const
  int characterCount() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall25 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::characterCount();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleQuickItem::characterRect(int a0) const
  QRect characterRect(int a0) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall26 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall26>(taken[26]);
      const QRect * given = call(this, a0, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::characterRect(a0);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleQuickItem::offsetAtPoint(const QPoint &a0) const
  int offsetAtPoint(const QPoint &a0) const override {
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall27 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall27>(taken[27]);
      int given = call(this, &a0, &handled);
      if (handled) return given;
    }
    return QAccessibleQuickItem::offsetAtPoint(a0);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleQuickItem::scrollToSubstring(int a0, int a1)
  void scrollToSubstring(int a0, int a1) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall28 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall28>(taken[28]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QAccessibleQuickItem::scrollToSubstring(a0, a1);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleQuickItem::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall29 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall29>(taken[29]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleQuickItem::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleQuickItem::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[30]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall30 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall30>(taken[30]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleQuickItem::interface_cast(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall31 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall31>(taken[31]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleObject::object();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall32 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall32>(taken[32]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleInterface::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall33 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall33>(taken[33]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall34 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall34>(taken[34]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[35]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall35 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall35>(taken[35]);
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
    if (taken[36]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall36 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall36>(taken[36]);
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
    if (taken[37]) {
      int handled = 0;
      CuteQAccessibleQuickPopupItemCall37 call = reinterpret_cast<CuteQAccessibleQuickPopupItemCall37>(taken[37]);
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

//  QAccessibleQuickPopupItem::QAccessibleQuickPopupItem(QQuickPopupItem
//      *popupItem)
extern "C" Q_DECL_EXPORT
QAccessibleQuickPopupItem *ritual_ZN25QAccessibleQuickPopupItemC1EP15QQuickPopupItem(
    QQuickPopupItem *popupItem) {
  return new CuteQAccessibleQuickPopupItem(popupItem);
}

//  QAccessible::State QAccessibleQuickPopupItem::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK25QAccessibleQuickPopupItem5stateEv(
    const QAccessibleQuickPopupItem *self) {
  return new QAccessible::State(self->state());
}

//  a Python function taken by a CuteQAccessibleQuickPopupItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleQuickPopupItem(
    QAccessibleQuickPopupItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleQuickPopupItem *>(self)->take(key, call);
}

//  QAccessible::State QAccessibleQuickPopupItem::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK25QAccessibleQuickPopupItem5stateEv(
    const QAccessibleQuickPopupItem *self) {
  return new QAccessible::State(self->QAccessibleQuickPopupItem::state());
}

#endif  // QT_CONFIG(accessibility)
