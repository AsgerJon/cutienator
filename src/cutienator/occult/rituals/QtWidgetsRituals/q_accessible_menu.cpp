//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qaccessiblemenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 47, as _ZNK15QAccessibleMenu10childCountEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline int QAccessibleMenu::childCount() const
{
    return menu()->actions().size();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 105, as _ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline int QAccessibleMenu::indexOfChild( const QAccessibleInterface *child) const
{
    QAccessible::Role r = child->role();
    if ((r == QAccessible::MenuItem || r == QAccessible::Separator) && menu()) {
        return menu()->actions().indexOf(qobject_cast<QAction*>(child->object()));
    }
    return -1;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 71, as _ZNK15QAccessibleMenu4roleEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessible::Role QAccessibleMenu::role() const
{
    return QAccessible::PopupMenu;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 60, as _ZNK15QAccessibleMenu4textEN11QAccessible4TextE
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QString QAccessibleMenu::text(QAccessible::Text t) const
{
    QString tx = QAccessibleWidgetV2::text(t);
    if (!tx.isEmpty())
        return tx;

    if (t == QAccessible::Name)
        return menu()->windowTitle();
    return tx;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 76, as _ZNK15QAccessibleMenu5childEi
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAccessibleInterface *QAccessibleMenu::child(int index) const
{
    if (index < childCount())
        return getOrCreateMenu(menu(), menu()->actions().at(index));
    return nullptr;
}
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

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 42, as _ZNK15QAccessibleMenu4menuEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QMenu *QAccessibleMenu::menu() const
{
    return qobject_cast<QMenu*>(object());
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleMenu that Python can take functions over in. Every QAccessibleMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuCall0)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef QString * (*CuteQAccessibleMenuCall2)(const void *, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuCall3)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuCall4)(const void *, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuCall5)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuCall6)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall7)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QVariant * (*CuteQAccessibleMenuCall8)(const void *, int, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleMenuCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QRect * (*CuteQAccessibleMenuCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QAccessible::State * (*CuteQAccessibleMenuCall13)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuCall16)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuCall17)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuCall18)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void (*CuteQAccessibleMenuCall19)(const void *, int, void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuCall20)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuCall21)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleMenu : public QAccessibleMenu {
public:
  using QAccessibleMenu::QAccessibleMenu;
  void *taken[22] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10childCountEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7childAtEii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface14interface_castEN11QAccessible13InterfaceTypeE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK30QAccessibleAttributesInterface14attributeValueEN11QAccessible9AttributeE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
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
  //  int QAccessibleMenu::childCount() const
  int childCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleMenuCall0 call = reinterpret_cast<CuteQAccessibleMenuCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleMenu::childCount();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenu::childAt(int x, int y) const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleMenuCall1 call = reinterpret_cast<CuteQAccessibleMenuCall1>(taken[1]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenu::childAt(x, y);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QString QAccessibleMenu::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleMenuCall2 call = reinterpret_cast<CuteQAccessibleMenuCall2>(taken[2]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleMenu::text(t);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessible::Role QAccessibleMenu::role() const
  QAccessible::Role role() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleMenuCall3 call = reinterpret_cast<CuteQAccessibleMenuCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleMenu::role();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenu::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleMenuCall4 call = reinterpret_cast<CuteQAccessibleMenuCall4>(taken[4]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenu::child(index);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenu::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleMenuCall5 call = reinterpret_cast<CuteQAccessibleMenuCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenu::parent();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
  //      const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleMenuCall6 call = reinterpret_cast<CuteQAccessibleMenuCall6>(taken[6]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleMenu::indexOfChild(child);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void *QAccessibleWidgetV2::interface_cast(QAccessible::InterfaceType
  //      t)
  void *interface_cast(QAccessible::InterfaceType t) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleMenuCall7 call = reinterpret_cast<CuteQAccessibleMenuCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleMenuCall8 call = reinterpret_cast<CuteQAccessibleMenuCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidgetV2::attributeValue(key);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleWidget::isValid() const
  bool isValid() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleMenuCall9 call = reinterpret_cast<CuteQAccessibleMenuCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleWidget::isValid();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QWindow *QAccessibleWidget::window() const
  QWindow *window() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleMenuCall10 call = reinterpret_cast<CuteQAccessibleMenuCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleWidget::window();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleWidget::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleMenuCall11 call = reinterpret_cast<CuteQAccessibleMenuCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleWidget::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QRect QAccessibleWidget::rect() const
  QRect rect() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleMenuCall12 call = reinterpret_cast<CuteQAccessibleMenuCall12>(taken[12]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::rect();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::State QAccessibleWidget::state() const
  QAccessible::State state() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleMenuCall13 call = reinterpret_cast<CuteQAccessibleMenuCall13>(taken[13]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::state();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleMenuCall14 call = reinterpret_cast<CuteQAccessibleMenuCall14>(taken[14]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleWidget::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleMenuCall15 call = reinterpret_cast<CuteQAccessibleMenuCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleWidget::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleWidget::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleMenuCall16 call = reinterpret_cast<CuteQAccessibleMenuCall16>(taken[16]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleWidget::doAction(actionName);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QObject *QAccessibleObject::object() const
  QObject *object() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleMenuCall17 call = reinterpret_cast<CuteQAccessibleMenuCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleMenuCall18 call = reinterpret_cast<CuteQAccessibleMenuCall18>(taken[18]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleObject::setText(t, text);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  void QAccessibleInterface::virtual_hook(int id, void *data)
  void virtual_hook(int id, void *data) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAccessibleMenuCall19 call = reinterpret_cast<CuteQAccessibleMenuCall19>(taken[19]);
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
      CuteQAccessibleMenuCall20 call = reinterpret_cast<CuteQAccessibleMenuCall20>(taken[20]);
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
      CuteQAccessibleMenuCall21 call = reinterpret_cast<CuteQAccessibleMenuCall21>(taken[21]);
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

//  int QAccessibleMenu::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleMenu10childCountEv(const QAccessibleMenu *self) {
  return self->childCount();
}

//  QAccessibleInterface *QAccessibleMenu::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleMenu7childAtEii(
    const QAccessibleMenu *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  QString QAccessibleMenu::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QAccessibleMenu4textEN11QAccessible4TextE(
    const QAccessibleMenu *self,
    QAccessible::Text t) {
  return new QString(self->text(t));
}

//  QAccessible::Role QAccessibleMenu::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK15QAccessibleMenu4roleEv(
    const QAccessibleMenu *self) {
  return self->role();
}

//  QAccessibleInterface *QAccessibleMenu::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleMenu5childEi(
    const QAccessibleMenu *self,
    int index) {
  return self->child(index);
}

//  QAccessibleInterface *QAccessibleMenu::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK15QAccessibleMenu6parentEv(
    const QAccessibleMenu *self) {
  return self->parent();
}

//  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenu *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QMenu *QAccessibleMenu::menu() const
extern "C" Q_DECL_EXPORT
QMenu *ritual_ZNK15QAccessibleMenu4menuEv(const QAccessibleMenu *self) {
  return self->menu();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  a Python function taken by a CuteQAccessibleMenu, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleMenu(
    QAccessibleMenu *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleMenu *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  int QAccessibleMenu::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleMenu10childCountEv(
    const QAccessibleMenu *self) {
  return self->QAccessibleMenu::childCount();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QString QAccessibleMenu::text(QAccessible::Text t) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK15QAccessibleMenu4textEN11QAccessible4TextE(
    const QAccessibleMenu *self,
    QAccessible::Text t) {
  return new QString(self->QAccessibleMenu::text(t));
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessible::Role QAccessibleMenu::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK15QAccessibleMenu4roleEv(
    const QAccessibleMenu *self) {
  return self->QAccessibleMenu::role();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  int QAccessibleMenu::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK15QAccessibleMenu12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenu *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleMenu::indexOfChild(child);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
