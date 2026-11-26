//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/complexwidgets_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/complexwidgets_p.h>
#include <QtGui/qaccessible.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qevent.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/qtabbar.h>
#include <QtWidgets/private/qtabbar_p.h>
#endif
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtWidgets/QAbstractScrollArea>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/QScrollArea>
#endif
#if QT_CONFIG(scrollbar)
#include <QtWidgets/QScrollBar>
#endif
#include <QtCore/QDebug>
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

using namespace Qt::StringLiterals;

//  from src/widgets/accessible/complexwidgets.cpp, line 188, as _ZN17QAccessibleTabBar14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline void *QAccessibleTabBar::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::SelectionInterface) {
        return static_cast<QAccessibleSelectionInterface*>(this);
    }
    return QAccessibleWidgetV2::interface_cast(t);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 322, as _ZN17QAccessibleTabBar5clearEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline bool QAccessibleTabBar::clear()
{
    return false;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 302, as _ZN17QAccessibleTabBar6selectEP20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline bool QAccessibleTabBar::select(QAccessibleInterface *childItem)
{
    const int childIndex = indexOfChild(childItem);
    if (childIndex >= 0) {
        tabBar()->setCurrentIndex(childIndex);
        return true;
    }
    return false;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 312, as _ZN17QAccessibleTabBar8unselectEP20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline bool QAccessibleTabBar::unselect(QAccessibleInterface *)
{
    return false;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 317, as _ZN17QAccessibleTabBar9selectAllEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline bool QAccessibleTabBar::selectAll()
{
    return false;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 252, as _ZNK17QAccessibleTabBar10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline int QAccessibleTabBar::childCount() const
{
    // tabs + scroll buttons
    return tabBar()->count() + 2;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 202, as _ZNK17QAccessibleTabBar10focusChildEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline QAccessibleInterface* QAccessibleTabBar::focusChild() const
{
    for (int i = 0; i < childCount(); ++i) {
        if (child(i)->state().focused)
            return child(i);
    }

    return nullptr;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 297, as _ZNK17QAccessibleTabBar10isSelectedEP20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline bool QAccessibleTabBar::isSelected(QAccessibleInterface *childItem) const
{
    return childItem && selectedItem(0) == childItem;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 289, as _ZNK17QAccessibleTabBar12selectedItemEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline QAccessibleInterface* QAccessibleTabBar::selectedItem(int selectionIndex) const
{
    const int currentIndex = tabBar()->currentIndex();
    if (selectionIndex != 0 || currentIndex < 0)
        return nullptr;
    return child(currentIndex);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 280, as _ZNK17QAccessibleTabBar13selectedItemsEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline QList<QAccessibleInterface*> QAccessibleTabBar::selectedItems() const
{
    QList<QAccessibleInterface*> items;
    QAccessibleInterface *selected = selectedItem(0);
    if (selected)
        items.push_back(selected);
    return items;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 273, as _ZNK17QAccessibleTabBar17selectedItemCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline int QAccessibleTabBar::selectedItemCount() const
{
    if (tabBar()->currentIndex() >= 0)
        return 1;
    return 0;
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 182, as _ZN17QAccessibleTabBarD1Ev
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline QAccessibleTabBar::~QAccessibleTabBar()
{
    for (QAccessible::Id id : std::as_const(m_childInterfaces))
        QAccessible::deleteAccessibleInterface(id);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/complexwidgets.cpp, line 197, as _ZNK17QAccessibleTabBar6tabBarEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
inline QTabBar *QAccessibleTabBar::tabBar() const
{
    return qobject_cast<QTabBar*>(object());
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleTabBar that Python can take functions over in. Every QAccessibleTabBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef void * (*CuteQAccessibleTabBarCall0)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef void * (*CuteQAccessibleTabBarCall1)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef int (*CuteQAccessibleTabBarCall2)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef QString * (*CuteQAccessibleTabBarCall3)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef void * (*CuteQAccessibleTabBarCall4)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef int (*CuteQAccessibleTabBarCall5)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef int (*CuteQAccessibleTabBarCall6)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef void * (*CuteQAccessibleTabBarCall7)(const void *, int, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef bool (*CuteQAccessibleTabBarCall8)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef bool (*CuteQAccessibleTabBarCall9)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef bool (*CuteQAccessibleTabBarCall10)(const void *, QAccessibleInterface *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef bool (*CuteQAccessibleTabBarCall11)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
typedef bool (*CuteQAccessibleTabBarCall12)(const void *, int *);
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleTabBarCall13)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleTabBarCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTabBarCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleTabBarCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTabBarCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleTabBarCall18)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleTabBarCall19)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTabBarCall20)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleTabBarCall21)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTabBarCall22)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTabBarCall23)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTabBarCall24)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleTabBarCall25)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleTabBarCall26)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTabBarCall27)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleTabBarCall28)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleTabBar : public QAccessibleTabBar {
public:
  using QAccessibleTabBar::QAccessibleTabBar;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface17selectedItemCountEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface12selectedItemEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInterface")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleInterface")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface9selectAllEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
    if (!std::strcmp(key, "_ZN29QAccessibleSelectionInterface5clearEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  void *QAccessibleTabBar::interface_cast(QAccessible::InterfaceType t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTabBarCall0 call = reinterpret_cast<CuteQAccessibleTabBarCall0>(taken[0]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleTabBar::interface_cast(t);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  QAccessibleInterface *QAccessibleTabBar::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleTabBarCall1 call = reinterpret_cast<CuteQAccessibleTabBarCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTabBar::focusChild();
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  int QAccessibleTabBar::childCount() const
  int childCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleTabBarCall2 call = reinterpret_cast<CuteQAccessibleTabBarCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::childCount();
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  QString QAccessibleTabBar::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleTabBarCall3 call = reinterpret_cast<CuteQAccessibleTabBarCall3>(taken[3]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleTabBar::text(t);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  QAccessibleInterface *QAccessibleTabBar::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleTabBarCall4 call = reinterpret_cast<CuteQAccessibleTabBarCall4>(taken[4]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTabBar::child(index);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  int QAccessibleTabBar::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleTabBarCall5 call = reinterpret_cast<CuteQAccessibleTabBarCall5>(taken[5]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::indexOfChild(child);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  int QAccessibleTabBar::selectedItemCount() const
  int selectedItemCount() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleTabBarCall6 call = reinterpret_cast<CuteQAccessibleTabBarCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::selectedItemCount();
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  QAccessibleInterface *QAccessibleTabBar::selectedItem(int
  //      selectionIndex) const
  QAccessibleInterface *selectedItem(int selectionIndex) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleTabBarCall7 call = reinterpret_cast<CuteQAccessibleTabBarCall7>(taken[7]);
      void * given = call(this, selectionIndex, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleTabBar::selectedItem(selectionIndex);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  bool QAccessibleTabBar::isSelected(QAccessibleInterface *childItem)
  //      const
  bool isSelected(QAccessibleInterface *childItem) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleTabBarCall8 call = reinterpret_cast<CuteQAccessibleTabBarCall8>(taken[8]);
      bool given = call(this, childItem, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::isSelected(childItem);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  bool QAccessibleTabBar::select(QAccessibleInterface *childItem)
  bool select(QAccessibleInterface *childItem) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleTabBarCall9 call = reinterpret_cast<CuteQAccessibleTabBarCall9>(taken[9]);
      bool given = call(this, childItem, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::select(childItem);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  bool QAccessibleTabBar::unselect(QAccessibleInterface *childItem)
  bool unselect(QAccessibleInterface *childItem) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleTabBarCall10 call = reinterpret_cast<CuteQAccessibleTabBarCall10>(taken[10]);
      bool given = call(this, childItem, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::unselect(childItem);
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  bool QAccessibleTabBar::selectAll()
  bool selectAll() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleTabBarCall11 call = reinterpret_cast<CuteQAccessibleTabBarCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::selectAll();
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
  //  bool QAccessibleTabBar::clear()
  bool clear() override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleTabBarCall12 call = reinterpret_cast<CuteQAccessibleTabBarCall12>(taken[12]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleTabBar::clear();
  }
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleTabBarCall13 call = reinterpret_cast<CuteQAccessibleTabBarCall13>(taken[13]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleTabBarCall14 call = reinterpret_cast<CuteQAccessibleTabBarCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleTabBarCall15 call = reinterpret_cast<CuteQAccessibleTabBarCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleTabBarCall16 call = reinterpret_cast<CuteQAccessibleTabBarCall16>(taken[16]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleTabBarCall17 call = reinterpret_cast<CuteQAccessibleTabBarCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::parent();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QAccessibleWidget::role() const
  QAccessible::Role role() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleTabBarCall18 call = reinterpret_cast<CuteQAccessibleTabBarCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleWidget::role();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleTabBarCall19 call = reinterpret_cast<CuteQAccessibleTabBarCall19>(taken[19]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleTabBarCall20 call = reinterpret_cast<CuteQAccessibleTabBarCall20>(taken[20]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleTabBarCall21 call = reinterpret_cast<CuteQAccessibleTabBarCall21>(taken[21]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAccessibleTabBarCall22 call = reinterpret_cast<CuteQAccessibleTabBarCall22>(taken[22]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAccessibleTabBarCall23 call = reinterpret_cast<CuteQAccessibleTabBarCall23>(taken[23]);
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
    if (taken[24]) {
      int handled = 0;
      CuteQAccessibleTabBarCall24 call = reinterpret_cast<CuteQAccessibleTabBarCall24>(taken[24]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQAccessibleTabBarCall25 call = reinterpret_cast<CuteQAccessibleTabBarCall25>(taken[25]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAccessibleTabBarCall26 call = reinterpret_cast<CuteQAccessibleTabBarCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQAccessibleTabBarCall27 call = reinterpret_cast<CuteQAccessibleTabBarCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQAccessibleTabBarCall28 call = reinterpret_cast<CuteQAccessibleTabBarCall28>(taken[28]);
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

//  QAccessibleTabBar::~QAccessibleTabBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAccessibleTabBarD1Ev(QAccessibleTabBar *self) {
  delete self;
}

//  void *QAccessibleTabBar::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QAccessibleTabBar14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleTabBar *self,
    QAccessible::InterfaceType t) {
  return self->interface_cast(t);
}

//  QAccessibleInterface *QAccessibleTabBar::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleTabBar10focusChildEv(
    const QAccessibleTabBar *self) {
  return self->focusChild();
}

//  int QAccessibleTabBar::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleTabBar10childCountEv(
    const QAccessibleTabBar *self) {
  return self->childCount();
}

//  QString QAccessibleTabBar::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAccessibleTabBar4textEN11QAccessible4TextE(
    const QAccessibleTabBar *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessibleInterface *QAccessibleTabBar::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleTabBar5childEi(
    const QAccessibleTabBar *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleTabBar::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleTabBar12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleTabBar *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  int QAccessibleTabBar::selectedItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QAccessibleTabBar17selectedItemCountEv(
    const QAccessibleTabBar *self) {
  return self->selectedItemCount();
}

//  QList<QAccessibleInterface *> QAccessibleTabBar::selectedItems() const
extern "C" Q_DECL_EXPORT
QList<QAccessibleInterface *> *ritual_ZNK17QAccessibleTabBar13selectedItemsEv(
    const QAccessibleTabBar *self) {
  return new QList<QAccessibleInterface *>(self->selectedItems());
}

//  QAccessibleInterface *QAccessibleTabBar::selectedItem(int selectionIndex)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK17QAccessibleTabBar12selectedItemEi(
    const QAccessibleTabBar *self,
    int selectionIndex) {
  return self->selectedItem(selectionIndex);
}

//  bool QAccessibleTabBar::isSelected(QAccessibleInterface *childItem) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAccessibleTabBar10isSelectedEP20QAccessibleInterface(
    const QAccessibleTabBar *self,
    QAccessibleInterface *childItem) {
  return self->isSelected(childItem);
}

//  bool QAccessibleTabBar::select(QAccessibleInterface *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAccessibleTabBar6selectEP20QAccessibleInterface(
    QAccessibleTabBar *self,
    QAccessibleInterface *childItem) {
  return self->select(childItem);
}

//  bool QAccessibleTabBar::unselect(QAccessibleInterface *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAccessibleTabBar8unselectEP20QAccessibleInterface(
    QAccessibleTabBar *self,
    QAccessibleInterface *childItem) {
  return self->unselect(childItem);
}

//  bool QAccessibleTabBar::selectAll()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAccessibleTabBar9selectAllEv(QAccessibleTabBar *self) {
  return self->selectAll();
}

//  bool QAccessibleTabBar::clear()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QAccessibleTabBar5clearEv(QAccessibleTabBar *self) {
  return self->clear();
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  QTabBar *QAccessibleTabBar::tabBar() const
extern "C" Q_DECL_EXPORT
QTabBar *ritual_ZNK17QAccessibleTabBar6tabBarEv(
    const QAccessibleTabBar *self) {
  return self->tabBar();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleTabBar as the QAccessibleSelectionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleSelectionInterface *ritual_cast_QAccessibleTabBar_QAccessibleSelectionInterface(
    QAccessibleTabBar *self) {
  return static_cast<QAccessibleSelectionInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleTabBar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTabBar(
    QAccessibleTabBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTabBar *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  void *QAccessibleTabBar::interface_cast(QAccessible::InterfaceType t)
extern "C" Q_DECL_EXPORT
void *ritual_own_ZN17QAccessibleTabBar14interface_castEN11QAccessible13InterfaceTypeE(
    QAccessibleTabBar *self,
    QAccessible::InterfaceType t) {
  return self->QAccessibleTabBar::interface_cast(t);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  QAccessibleInterface *QAccessibleTabBar::focusChild() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK17QAccessibleTabBar10focusChildEv(
    const QAccessibleTabBar *self) {
  return self->QAccessibleTabBar::focusChild();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  int QAccessibleTabBar::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAccessibleTabBar10childCountEv(
    const QAccessibleTabBar *self) {
  return self->QAccessibleTabBar::childCount();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  int QAccessibleTabBar::selectedItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QAccessibleTabBar17selectedItemCountEv(
    const QAccessibleTabBar *self) {
  return self->QAccessibleTabBar::selectedItemCount();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  QAccessibleInterface *QAccessibleTabBar::selectedItem(int selectionIndex)
//      const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK17QAccessibleTabBar12selectedItemEi(
    const QAccessibleTabBar *self,
    int selectionIndex) {
  return self->QAccessibleTabBar::selectedItem(selectionIndex);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  bool QAccessibleTabBar::isSelected(QAccessibleInterface *childItem) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QAccessibleTabBar10isSelectedEP20QAccessibleInterface(
    const QAccessibleTabBar *self,
    QAccessibleInterface *childItem) {
  return self->QAccessibleTabBar::isSelected(childItem);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  bool QAccessibleTabBar::select(QAccessibleInterface *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAccessibleTabBar6selectEP20QAccessibleInterface(
    QAccessibleTabBar *self,
    QAccessibleInterface *childItem) {
  return self->QAccessibleTabBar::select(childItem);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  bool QAccessibleTabBar::unselect(QAccessibleInterface *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAccessibleTabBar8unselectEP20QAccessibleInterface(
    QAccessibleTabBar *self,
    QAccessibleInterface *childItem) {
  return self->QAccessibleTabBar::unselect(childItem);
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  bool QAccessibleTabBar::selectAll()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAccessibleTabBar9selectAllEv(QAccessibleTabBar *self) {
  return self->QAccessibleTabBar::selectAll();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(tabbar)
//  bool QAccessibleTabBar::clear()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QAccessibleTabBar5clearEv(QAccessibleTabBar *self) {
  return self->QAccessibleTabBar::clear();
}
#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(tabbar)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
