//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qaccessiblemenu_p.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#if QT_CONFIG(menubar)
#include <QtWidgets/qmenubar.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/private/qwidget_p.h>
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

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 26, as local:qaccessiblemenu.cpp:getOrCreateMenu
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleInterface *getOrCreateMenu(QWidget *menu, QAction *action)
{
    QAccessibleInterface *iface = QAccessible::queryAccessibleInterface(action);
    if (!iface) {
        iface = new QAccessibleMenuItem(menu, action);
        QAccessible::registerAccessibleInterface(iface);
    }
    return iface;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 126, as _ZNK18QAccessibleMenuBar10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
inline int QAccessibleMenuBar::childCount() const
{
    return menuBar()->actions().size();
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 139, as _ZNK18QAccessibleMenuBar12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
inline int QAccessibleMenuBar::indexOfChild(const QAccessibleInterface *child) const
{
    QAccessible::Role r = child->role();
    if ((r == QAccessible::MenuItem || r == QAccessible::Separator) && menuBar()) {
        return menuBar()->actions().indexOf(qobject_cast<QAction*>(child->object()));
    }
    return -1;
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 131, as _ZNK18QAccessibleMenuBar5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
inline QAccessibleInterface *QAccessibleMenuBar::child(int index) const
{
    if (index < childCount()) {
        return getOrCreateMenu(menuBar(), menuBar()->actions().at(index));
    }
    return nullptr;
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 155, as _ZN19QAccessibleMenuItemC1EP7QWidgetP7QAction
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleMenuItem::QAccessibleMenuItem(QWidget *owner, QAction *action)
: m_action(action), m_owner(owner)
{
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 160, as _ZN19QAccessibleMenuItemD1Ev
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleMenuItem::~QAccessibleMenuItem()
{}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 203, as _ZN19QAccessibleMenuItem14interface_castEN11QAccessible13InterfaceTypeE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline void *QAccessibleMenuItem::interface_cast(QAccessible::InterfaceType t)
{
    if (t == QAccessible::ActionInterface)
        return static_cast<QAccessibleActionInterface*>(this);
    return nullptr;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 174, as _ZNK19QAccessibleMenuItem10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline int QAccessibleMenuItem::childCount() const
{
    return m_action->menu() ? 1 : 0;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 163, as _ZNK19QAccessibleMenuItem7childAtEii
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleInterface *QAccessibleMenuItem::childAt(int x, int y ) const
{
    for (int i = childCount() - 1; i >= 0; --i) {
        QAccessibleInterface *childInterface = child(i);
        if (childInterface->rect().contains(x,y)) {
            return childInterface;
        }
    }
    return nullptr;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 186, as _ZNK19QAccessibleMenuItem7isValidEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline bool QAccessibleMenuItem::isValid() const
{
    return m_action && m_owner;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 179, as _ZNK19QAccessibleMenuItem12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline int QAccessibleMenuItem::indexOfChild(const QAccessibleInterface * child) const
{
    if (child && child->role() == QAccessible::PopupMenu && child->object() == m_action->menu())
        return 0;
    return -1;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 191, as _ZNK19QAccessibleMenuItem6parentEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleInterface *QAccessibleMenuItem::parent() const
{
    return QAccessible::queryAccessibleInterface(owner());
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 196, as _ZNK19QAccessibleMenuItem5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleInterface *QAccessibleMenuItem::child(int index) const
{
    if (index == 0 && action()->menu())
        return QAccessible::queryAccessibleInterface(action()->menu());
    return nullptr;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 210, as _ZNK19QAccessibleMenuItem6objectEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QObject *QAccessibleMenuItem::object() const
{
    return m_action;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 216, as _ZNK19QAccessibleMenuItem6windowEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QWindow *QAccessibleMenuItem::window() const
{
    return m_owner.isNull()
        ? nullptr
        : qt_widget_private(m_owner.data())->windowHandle(QWidgetPrivate::WindowHandleMode::Closest);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 223, as _ZNK19QAccessibleMenuItem4rectEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QRect QAccessibleMenuItem::rect() const
{
    QRect rect;
    QWidget *own = owner();
#if QT_CONFIG(menubar)
    if (QMenuBar *menuBar = qobject_cast<QMenuBar*>(own)) {
        rect = menuBar->actionGeometry(m_action);
        QPoint globalPos = menuBar->mapToGlobal(QPoint(0,0));
        rect = rect.translated(globalPos);
    } else
#endif // QT_CONFIG(menubar)
    if (QMenu *menu = qobject_cast<QMenu*>(own)) {
        rect = menu->actionGeometry(m_action);
        QPoint globalPos = menu->mapToGlobal(QPoint(0,0));
        rect = rect.translated(globalPos);
    }
    return rect;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 242, as _ZNK19QAccessibleMenuItem4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessible::Role QAccessibleMenuItem::role() const
{
    return m_action->isSeparator() ? QAccessible::Separator : QAccessible::MenuItem;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 247, as _ZN19QAccessibleMenuItem7setTextEN11QAccessible4TextERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline void QAccessibleMenuItem::setText(QAccessible::Text /*t*/, const QString & /*text */)
{
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 251, as _ZNK19QAccessibleMenuItem5stateEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessible::State QAccessibleMenuItem::state() const
{
    QAccessible::State s;
    QWidget *own = owner();

    if (own && (own->testAttribute(Qt::WA_WState_Visible) == false || m_action->isVisible() == false)) {
        s.invisible = true;
    }

    if (QMenu *menu = qobject_cast<QMenu*>(own)) {
        if (menu->activeAction() == m_action)
            s.focused = true;
#if QT_CONFIG(menubar)
    } else if (QMenuBar *menuBar = qobject_cast<QMenuBar*>(own)) {
        if (menuBar->activeAction() == m_action)
            s.focused = true;
#endif
    }
    if (own && own->style()->styleHint(QStyle::SH_Menu_MouseTracking, nullptr, own))
        s.hotTracked = true;
    if (m_action->isSeparator() || !m_action->isEnabled())
        s.disabled = true;
    if (m_action->isChecked())
        s.checked = true;
    if (m_action->isCheckable())
        s.checkable = true;

    return s;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 306, as _ZNK19QAccessibleMenuItem11actionNamesEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QStringList QAccessibleMenuItem::actionNames() const
{
    QStringList actions;
    if (!m_action || m_action->isSeparator())
        return actions;

    if (m_action->menu()) {
        actions << showMenuAction();
    } else {
        actions << pressAction();
    }
    return actions;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 320, as _ZN19QAccessibleMenuItem8doActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline void QAccessibleMenuItem::doAction(const QString &actionName)
{
    if (!m_action->isEnabled())
        return;

    if (actionName == pressAction()) {
        m_action->trigger();
    } else if (actionName == showMenuAction()) {
#if QT_CONFIG(menubar)
        if (QMenuBar *bar = qobject_cast<QMenuBar*>(owner())) {
            if (m_action->menu() && m_action->menu()->isVisible()) {
                m_action->menu()->hide();
            } else {
                bar->setActiveAction(m_action);
            }
        } else
#endif
          if (QMenu *menu = qobject_cast<QMenu*>(owner())){
            if (m_action->menu() && m_action->menu()->isVisible()) {
                m_action->menu()->hide();
            } else {
                menu->setActiveAction(m_action);
            }
        }
    }
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 347, as _ZNK19QAccessibleMenuItem20keyBindingsForActionERK7QString
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QStringList QAccessibleMenuItem::keyBindingsForAction(const QString &) const
{
    return QStringList();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 121, as _ZNK18QAccessibleMenuBar7menuBarEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
inline QMenuBar *QAccessibleMenuBar::menuBar() const
{
    return qobject_cast<QMenuBar*>(object());
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleMenuBar that Python can take functions over in. Every QAccessibleMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
typedef void * (*CuteQAccessibleMenuBarCall0)(const void *, int, int *);
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
typedef int (*CuteQAccessibleMenuBarCall1)(const void *, int *);
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
typedef int (*CuteQAccessibleMenuBarCall2)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuBarCall3)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleMenuBarCall4)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleMenuBarCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuBarCall6)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuBarCall7)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleMenuBarCall8)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuBarCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuBarCall10)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleMenuBarCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleMenuBarCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuBarCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuBarCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuBarCall15)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuBarCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuBarCall17)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuBarCall18)(const void *, int, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuBarCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuBarCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuBarCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleMenuBar : public QAccessibleMenuBar {
public:
  using QAccessibleMenuBar::QAccessibleMenuBar;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface12virtual_hookEiPv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
  //  QAccessibleInterface *QAccessibleMenuBar::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall0 call = reinterpret_cast<CuteQAccessibleMenuBarCall0>(taken[0]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenuBar::child(index);
  }
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
  //  int QAccessibleMenuBar::childCount() const
  int childCount() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall1 call = reinterpret_cast<CuteQAccessibleMenuBarCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleMenuBar::childCount();
  }
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
  //  int QAccessibleMenuBar::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall2 call = reinterpret_cast<CuteQAccessibleMenuBarCall2>(taken[2]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleMenuBar::indexOfChild(child);
  }
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall3 call = reinterpret_cast<CuteQAccessibleMenuBarCall3>(taken[3]);
      void * given = call(this, static_cast<int>(t), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QAccessibleWidgetV2::interface_cast(t);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QVariant QAccessibleWidgetV2::attributeValue(QAccessible::Attribute
  //      key) const
  QVariant attributeValue(QAccessible::Attribute key) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall4 call = reinterpret_cast<CuteQAccessibleMenuBarCall4>(taken[4]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall5 call = reinterpret_cast<CuteQAccessibleMenuBarCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall6 call = reinterpret_cast<CuteQAccessibleMenuBarCall6>(taken[6]);
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
      CuteQAccessibleMenuBarCall7 call = reinterpret_cast<CuteQAccessibleMenuBarCall7>(taken[7]);
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
      CuteQAccessibleMenuBarCall8 call = reinterpret_cast<CuteQAccessibleMenuBarCall8>(taken[8]);
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
      CuteQAccessibleMenuBarCall9 call = reinterpret_cast<CuteQAccessibleMenuBarCall9>(taken[9]);
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
      CuteQAccessibleMenuBarCall10 call = reinterpret_cast<CuteQAccessibleMenuBarCall10>(taken[10]);
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
      CuteQAccessibleMenuBarCall11 call = reinterpret_cast<CuteQAccessibleMenuBarCall11>(taken[11]);
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
      CuteQAccessibleMenuBarCall12 call = reinterpret_cast<CuteQAccessibleMenuBarCall12>(taken[12]);
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
      CuteQAccessibleMenuBarCall13 call = reinterpret_cast<CuteQAccessibleMenuBarCall13>(taken[13]);
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
      CuteQAccessibleMenuBarCall14 call = reinterpret_cast<CuteQAccessibleMenuBarCall14>(taken[14]);
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
      CuteQAccessibleMenuBarCall15 call = reinterpret_cast<CuteQAccessibleMenuBarCall15>(taken[15]);
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
      CuteQAccessibleMenuBarCall16 call = reinterpret_cast<CuteQAccessibleMenuBarCall16>(taken[16]);
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
      CuteQAccessibleMenuBarCall17 call = reinterpret_cast<CuteQAccessibleMenuBarCall17>(taken[17]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleObject::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall18 call = reinterpret_cast<CuteQAccessibleMenuBarCall18>(taken[18]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleObject::childAt(x, y);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall19 call = reinterpret_cast<CuteQAccessibleMenuBarCall19>(taken[19]);
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
    if (taken[20]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall20 call = reinterpret_cast<CuteQAccessibleMenuBarCall20>(taken[20]);
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
    if (taken[21]) {
      int handled = 0;
      CuteQAccessibleMenuBarCall21 call = reinterpret_cast<CuteQAccessibleMenuBarCall21>(taken[21]);
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

//  QAccessibleInterface *QAccessibleMenuBar::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK18QAccessibleMenuBar5childEi(
    const QAccessibleMenuBar *self,
    int index) {
  return self->child(index);
}

//  int QAccessibleMenuBar::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAccessibleMenuBar10childCountEv(
    const QAccessibleMenuBar *self) {
  return self->childCount();
}

//  int QAccessibleMenuBar::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAccessibleMenuBar12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenuBar *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
//  QMenuBar *QAccessibleMenuBar::menuBar() const
extern "C" Q_DECL_EXPORT
QMenuBar *ritual_ZNK18QAccessibleMenuBar7menuBarEv(
    const QAccessibleMenuBar *self) {
  return self->menuBar();
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleMenuBar, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleMenuBar(
    QAccessibleMenuBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleMenuBar *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
//  int QAccessibleMenuBar::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QAccessibleMenuBar10childCountEv(
    const QAccessibleMenuBar *self) {
  return self->QAccessibleMenuBar::childCount();
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#if QT_CONFIG(menubar)
//  int QAccessibleMenuBar::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK18QAccessibleMenuBar12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenuBar *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleMenuBar::indexOfChild(child);
}
#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(menubar)
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
