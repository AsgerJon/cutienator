//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "complexwidgets_p.h"
#include <qaccessible.h>
#include <qapplication.h>
#include <qevent.h>
#if QT_CONFIG(itemviews)
#include <qheaderview.h>
#endif
#if QT_CONFIG(tabbar)
#include <qtabbar.h>
#include <private/qtabbar_p.h>
#endif
#if QT_CONFIG(combobox)
#include <qcombobox.h>
#endif
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#endif
#include <qstyle.h>
#include <qstyleoption.h>
#if QT_CONFIG(tooltip)
#include <qtooltip.h>
#endif
#if QT_CONFIG(whatsthis)
#include <qwhatsthis.h>
#endif
#include <QAbstractScrollArea>
#if QT_CONFIG(scrollarea)
#include <QScrollArea>
#endif
#if QT_CONFIG(scrollbar)
#include <QScrollBar>
#endif
#include <QDebug>
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

//  from src/widgets/accessible/complexwidgets.cpp, line 501, as _ZN29QAccessibleAbstractScrollAreaC2EP7QWidget
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleAbstractScrollArea::QAccessibleAbstractScrollArea(QWidget *widget)
    : QAccessibleWidgetV2(widget, QAccessible::Client)
{
    Q_ASSERT(qobject_cast<QAbstractScrollArea *>(widget));
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 512, as _ZNK29QAccessibleAbstractScrollArea10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline int QAccessibleAbstractScrollArea::childCount() const
{
    return accessibleChildren().size();
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 517, as _ZNK29QAccessibleAbstractScrollArea12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline int QAccessibleAbstractScrollArea::indexOfChild(const QAccessibleInterface *child) const
{
    if (!child || !child->object())
        return -1;
    return accessibleChildren().indexOf(qobject_cast<QWidget *>(child->object()));
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 507, as _ZNK29QAccessibleAbstractScrollArea5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleInterface *QAccessibleAbstractScrollArea::child(int index) const
{
    return QAccessible::queryAccessibleInterface(accessibleChildren().at(index));
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 529, as _ZNK29QAccessibleAbstractScrollArea7childAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline QAccessibleInterface *QAccessibleAbstractScrollArea::childAt(int x, int y) const
{
    if (!abstractScrollArea()->isVisible())
        return nullptr;

    for (int i = 0; i < childCount(); ++i) {
        QPoint wpos = accessibleChildren().at(i)->mapToGlobal(QPoint(0, 0));
        QRect rect = QRect(wpos, accessibleChildren().at(i)->size());
        if (rect.contains(x, y))
            return child(i);
    }
    return nullptr;
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 524, as _ZNK29QAccessibleAbstractScrollArea7isValidEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
inline bool QAccessibleAbstractScrollArea::isValid() const
{
    return (QAccessibleWidgetV2::isValid() && abstractScrollArea() && abstractScrollArea()->viewport());
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleScrollArea that Python can take functions over in. Every QAccessibleScrollArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
typedef void * (*CuteQAccessibleScrollAreaCall0)(const void *, int, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
typedef int (*CuteQAccessibleScrollAreaCall1)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
typedef int (*CuteQAccessibleScrollAreaCall2)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQAccessibleScrollAreaCall3)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
typedef void * (*CuteQAccessibleScrollAreaCall4)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleScrollAreaCall5)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollAreaCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollAreaCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleScrollAreaCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollAreaCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleScrollAreaCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleScrollAreaCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleScrollAreaCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleScrollAreaCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleScrollAreaCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleScrollAreaCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleScrollAreaCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleScrollAreaCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleScrollAreaCall18)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleScrollAreaCall19)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleScrollArea : public QAccessibleScrollArea {
public:
  using QAccessibleScrollArea::QAccessibleScrollArea;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
  //  QAccessibleInterface *QAccessibleAbstractScrollArea::child(int index)
  //      const
  QAccessibleInterface *child(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall0 call = reinterpret_cast<CuteQAccessibleScrollAreaCall0>(taken[0]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleAbstractScrollArea::child(index);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
  //  int QAccessibleAbstractScrollArea::childCount() const
  int childCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall1 call = reinterpret_cast<CuteQAccessibleScrollAreaCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractScrollArea::childCount();
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
  //  int QAccessibleAbstractScrollArea::indexOfChild(const
  //      QAccessibleInterface *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall2 call = reinterpret_cast<CuteQAccessibleScrollAreaCall2>(taken[2]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractScrollArea::indexOfChild(child);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
  //  bool QAccessibleAbstractScrollArea::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall3 call = reinterpret_cast<CuteQAccessibleScrollAreaCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleAbstractScrollArea::isValid();
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(scrollarea)
  //  QAccessibleInterface *QAccessibleAbstractScrollArea::childAt(int x,
  //      int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall4 call = reinterpret_cast<CuteQAccessibleScrollAreaCall4>(taken[4]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleAbstractScrollArea::childAt(x, y);
  }
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall5 call = reinterpret_cast<CuteQAccessibleScrollAreaCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall6 call = reinterpret_cast<CuteQAccessibleScrollAreaCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall7 call = reinterpret_cast<CuteQAccessibleScrollAreaCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall8 call = reinterpret_cast<CuteQAccessibleScrollAreaCall8>(taken[8]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall9 call = reinterpret_cast<CuteQAccessibleScrollAreaCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleWidget::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall10 call = reinterpret_cast<CuteQAccessibleScrollAreaCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall11 call = reinterpret_cast<CuteQAccessibleScrollAreaCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall12 call = reinterpret_cast<CuteQAccessibleScrollAreaCall12>(taken[12]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall13 call = reinterpret_cast<CuteQAccessibleScrollAreaCall13>(taken[13]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall14 call = reinterpret_cast<CuteQAccessibleScrollAreaCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall15 call = reinterpret_cast<CuteQAccessibleScrollAreaCall15>(taken[15]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall16 call = reinterpret_cast<CuteQAccessibleScrollAreaCall16>(taken[16]);
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
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall17 call = reinterpret_cast<CuteQAccessibleScrollAreaCall17>(taken[17]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall18 call = reinterpret_cast<CuteQAccessibleScrollAreaCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleScrollAreaCall19 call = reinterpret_cast<CuteQAccessibleScrollAreaCall19>(taken[19]);
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

//  a Python function taken by a CuteQAccessibleScrollArea, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleScrollArea(
    QAccessibleScrollArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleScrollArea *>(self)->take(key, call);
}

#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(accessibility)
