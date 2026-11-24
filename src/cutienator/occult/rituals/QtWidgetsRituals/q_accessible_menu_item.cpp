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
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qcolor.h>
#include <QtCore/qlist.h>
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

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 358, as _ZNK19QAccessibleMenuItem5ownerEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QWidget *QAccessibleMenuItem::owner() const
{
    return m_owner;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/accessible/qaccessiblemenu.cpp, line 353, as _ZNK19QAccessibleMenuItem6actionEv
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
inline QAction *QAccessibleMenuItem::action() const
{
    return m_action;
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
//  -----------------------------------------------------------------------

//  A QAccessibleMenuItem that Python can take functions over in. Every QAccessibleMenuItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuItemCall0)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuItemCall1)(const void *, int, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef bool (*CuteQAccessibleMenuItemCall2)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuItemCall3)(const void *, const QAccessibleInterface *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuItemCall4)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuItemCall5)(const void *, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuItemCall6)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void * (*CuteQAccessibleMenuItemCall7)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef const QRect * (*CuteQAccessibleMenuItemCall8)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef int (*CuteQAccessibleMenuItemCall9)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void (*CuteQAccessibleMenuItemCall10)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef const QAccessible::State * (*CuteQAccessibleMenuItemCall11)(const void *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef QString * (*CuteQAccessibleMenuItemCall12)(const void *, int, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
typedef void (*CuteQAccessibleMenuItemCall13)(const void *, const QString *, int *);
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef void * (*CuteQAccessibleMenuItemCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuItemCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef const QColor * (*CuteQAccessibleMenuItemCall16)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuItemCall17)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleMenuItemCall18)(const void *, const QString *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleMenuItem : public QAccessibleMenuItem {
public:
  using QAccessibleMenuItem::QAccessibleMenuItem;
  void *taken[19] = {};

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
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface7isValidEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface12indexOfChildEPKS_")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6parentEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5childEi")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6objectEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface6windowEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4rectEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4roleEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN20QAccessibleInterface7setTextEN11QAccessible4TextERK7QString")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface5stateEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface4textEN11QAccessible4TextE")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
    if (!std::strcmp(key, "_ZN26QAccessibleActionInterface8doActionERK7QString")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface10focusChildEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15foregroundColorEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QAccessibleInterface15backgroundColorEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface19localizedActionNameERK7QString")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK26QAccessibleActionInterface26localizedActionDescriptionERK7QString")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  int QAccessibleMenuItem::childCount() const
  int childCount() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall0 call = reinterpret_cast<CuteQAccessibleMenuItemCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleMenuItem::childCount();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenuItem::childAt(int x, int y)
  //      const
  QAccessibleInterface *childAt(int x, int y) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall1 call = reinterpret_cast<CuteQAccessibleMenuItemCall1>(taken[1]);
      void * given = call(this, x, y, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenuItem::childAt(x, y);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  bool QAccessibleMenuItem::isValid() const
  bool isValid() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall2 call = reinterpret_cast<CuteQAccessibleMenuItemCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAccessibleMenuItem::isValid();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  int QAccessibleMenuItem::indexOfChild(const QAccessibleInterface
  //      *child) const
  int indexOfChild(const QAccessibleInterface *child) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall3 call = reinterpret_cast<CuteQAccessibleMenuItemCall3>(taken[3]);
      int given = call(this, child, &handled);
      if (handled) return given;
    }
    return QAccessibleMenuItem::indexOfChild(child);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenuItem::parent() const
  QAccessibleInterface *parent() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall4 call = reinterpret_cast<CuteQAccessibleMenuItemCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenuItem::parent();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessibleInterface *QAccessibleMenuItem::child(int index) const
  QAccessibleInterface *child(int index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall5 call = reinterpret_cast<CuteQAccessibleMenuItemCall5>(taken[5]);
      void * given = call(this, index, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleMenuItem::child(index);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QObject *QAccessibleMenuItem::object() const
  QObject *object() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall6 call = reinterpret_cast<CuteQAccessibleMenuItemCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QAccessibleMenuItem::object();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QWindow *QAccessibleMenuItem::window() const
  QWindow *window() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall7 call = reinterpret_cast<CuteQAccessibleMenuItemCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QAccessibleMenuItem::window();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QRect QAccessibleMenuItem::rect() const
  QRect rect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall8 call = reinterpret_cast<CuteQAccessibleMenuItemCall8>(taken[8]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleMenuItem::rect();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessible::Role QAccessibleMenuItem::role() const
  QAccessible::Role role() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall9 call = reinterpret_cast<CuteQAccessibleMenuItemCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QAccessibleMenuItem::role();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  void QAccessibleMenuItem::setText(QAccessible::Text t, const QString
  //      &text)
  void setText(QAccessible::Text t, const QString &text) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall10 call = reinterpret_cast<CuteQAccessibleMenuItemCall10>(taken[10]);
      call(this, static_cast<int>(t), &text, &handled);
      if (handled) return;
    }
    QAccessibleMenuItem::setText(t, text);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QAccessible::State QAccessibleMenuItem::state() const
  QAccessible::State state() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall11 call = reinterpret_cast<CuteQAccessibleMenuItemCall11>(taken[11]);
      const QAccessible::State * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleMenuItem::state();
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  QString QAccessibleMenuItem::text(QAccessible::Text t) const
  QString text(QAccessible::Text t) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall12 call = reinterpret_cast<CuteQAccessibleMenuItemCall12>(taken[12]);
      QString * given = call(this, static_cast<int>(t), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAccessibleMenuItem::text(t);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
  //  void QAccessibleMenuItem::doAction(const QString &actionName)
  void doAction(const QString &actionName) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall13 call = reinterpret_cast<CuteQAccessibleMenuItemCall13>(taken[13]);
      call(this, &actionName, &handled);
      if (handled) return;
    }
    QAccessibleMenuItem::doAction(actionName);
  }
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QAccessibleInterface::focusChild() const
  QAccessibleInterface *focusChild() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall14 call = reinterpret_cast<CuteQAccessibleMenuItemCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleInterface::focusChild();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::foregroundColor() const
  QColor foregroundColor() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall15 call = reinterpret_cast<CuteQAccessibleMenuItemCall15>(taken[15]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::foregroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QColor QAccessibleInterface::backgroundColor() const
  QColor backgroundColor() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall16 call = reinterpret_cast<CuteQAccessibleMenuItemCall16>(taken[16]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAccessibleInterface::backgroundColor();
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleActionInterface::localizedActionName(const QString
  //      &name) const
  QString localizedActionName(const QString &name) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall17 call = reinterpret_cast<CuteQAccessibleMenuItemCall17>(taken[17]);
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
    if (taken[18]) {
      int handled = 0;
      CuteQAccessibleMenuItemCall18 call = reinterpret_cast<CuteQAccessibleMenuItemCall18>(taken[18]);
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

//  int QAccessibleMenuItem::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleMenuItem10childCountEv(
    const QAccessibleMenuItem *self) {
  return self->childCount();
}

//  QAccessibleInterface *QAccessibleMenuItem::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK19QAccessibleMenuItem7childAtEii(
    const QAccessibleMenuItem *self,
    int x,
    int y) {
  return self->childAt(x, y);
}

//  bool QAccessibleMenuItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAccessibleMenuItem7isValidEv(
    const QAccessibleMenuItem *self) {
  return self->isValid();
}

//  int QAccessibleMenuItem::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAccessibleMenuItem12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenuItem *self,
    const QAccessibleInterface *child) {
  return self->indexOfChild(child);
}

//  QAccessibleInterface *QAccessibleMenuItem::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK19QAccessibleMenuItem6parentEv(
    const QAccessibleMenuItem *self) {
  return self->parent();
}

//  QAccessibleInterface *QAccessibleMenuItem::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK19QAccessibleMenuItem5childEi(
    const QAccessibleMenuItem *self,
    int index) {
  return self->child(index);
}

//  QObject *QAccessibleMenuItem::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK19QAccessibleMenuItem6objectEv(
    const QAccessibleMenuItem *self) {
  return self->object();
}

//  QWindow *QAccessibleMenuItem::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK19QAccessibleMenuItem6windowEv(
    const QAccessibleMenuItem *self) {
  return self->window();
}

//  QRect QAccessibleMenuItem::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QAccessibleMenuItem4rectEv(
    const QAccessibleMenuItem *self) {
  return new QRect(self->rect());
}

//  QAccessible::Role QAccessibleMenuItem::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK19QAccessibleMenuItem4roleEv(
    const QAccessibleMenuItem *self) {
  return self->role();
}

//  void QAccessibleMenuItem::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleMenuItem7setTextEN11QAccessible4TextERK7QString(
    QAccessibleMenuItem *self,
    QAccessible::Text t,
    const QString *text) {
  self->setText(t, *text);
}

//  QAccessible::State QAccessibleMenuItem::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK19QAccessibleMenuItem5stateEv(
    const QAccessibleMenuItem *self) {
  return new QAccessible::State(self->state());
}

//  QStringList QAccessibleMenuItem::actionNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAccessibleMenuItem11actionNamesEv(
    const QAccessibleMenuItem *self) {
  return new QList<QString>(self->actionNames());
}

//  void QAccessibleMenuItem::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAccessibleMenuItem8doActionERK7QString(
    QAccessibleMenuItem *self,
    const QString *actionName) {
  self->doAction(*actionName);
}

//  QStringList QAccessibleMenuItem::keyBindingsForAction(const QString
//      &actionName) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QAccessibleMenuItem20keyBindingsForActionERK7QString(
    const QAccessibleMenuItem *self,
    const QString *actionName) {
  return new QList<QString>(self->keyBindingsForAction(*actionName));
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QWidget *QAccessibleMenuItem::owner() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QAccessibleMenuItem5ownerEv(
    const QAccessibleMenuItem *self) {
  return self->owner();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAction *QAccessibleMenuItem::action() const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK19QAccessibleMenuItem6actionEv(
    const QAccessibleMenuItem *self) {
  return self->action();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

//  QAccessibleMenuItem as the QAccessibleActionInterface it is built on
extern "C" Q_DECL_EXPORT
QAccessibleActionInterface *ritual_cast_QAccessibleMenuItem_QAccessibleActionInterface(
    QAccessibleMenuItem *self) {
  return static_cast<QAccessibleActionInterface *>(self);
}

//  a Python function taken by a CuteQAccessibleMenuItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleMenuItem(
    QAccessibleMenuItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleMenuItem *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  int QAccessibleMenuItem::childCount() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleMenuItem10childCountEv(
    const QAccessibleMenuItem *self) {
  return self->QAccessibleMenuItem::childCount();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessibleInterface *QAccessibleMenuItem::childAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK19QAccessibleMenuItem7childAtEii(
    const QAccessibleMenuItem *self,
    int x,
    int y) {
  return self->QAccessibleMenuItem::childAt(x, y);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  bool QAccessibleMenuItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAccessibleMenuItem7isValidEv(
    const QAccessibleMenuItem *self) {
  return self->QAccessibleMenuItem::isValid();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  int QAccessibleMenuItem::indexOfChild(const QAccessibleInterface *child)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAccessibleMenuItem12indexOfChildEPK20QAccessibleInterface(
    const QAccessibleMenuItem *self,
    const QAccessibleInterface *child) {
  return self->QAccessibleMenuItem::indexOfChild(child);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessibleInterface *QAccessibleMenuItem::parent() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK19QAccessibleMenuItem6parentEv(
    const QAccessibleMenuItem *self) {
  return self->QAccessibleMenuItem::parent();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessibleInterface *QAccessibleMenuItem::child(int index) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK19QAccessibleMenuItem5childEi(
    const QAccessibleMenuItem *self,
    int index) {
  return self->QAccessibleMenuItem::child(index);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QObject *QAccessibleMenuItem::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK19QAccessibleMenuItem6objectEv(
    const QAccessibleMenuItem *self) {
  return self->QAccessibleMenuItem::object();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QWindow *QAccessibleMenuItem::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_own_ZNK19QAccessibleMenuItem6windowEv(
    const QAccessibleMenuItem *self) {
  return self->QAccessibleMenuItem::window();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QRect QAccessibleMenuItem::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK19QAccessibleMenuItem4rectEv(
    const QAccessibleMenuItem *self) {
  return new QRect(self->QAccessibleMenuItem::rect());
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessible::Role QAccessibleMenuItem::role() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK19QAccessibleMenuItem4roleEv(
    const QAccessibleMenuItem *self) {
  return self->QAccessibleMenuItem::role();
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  void QAccessibleMenuItem::setText(QAccessible::Text t, const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleMenuItem7setTextEN11QAccessible4TextERK7QString(
    QAccessibleMenuItem *self,
    QAccessible::Text t,
    const QString *text) {
  self->QAccessibleMenuItem::setText(t, *text);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  QAccessible::State QAccessibleMenuItem::state() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_own_ZNK19QAccessibleMenuItem5stateEv(
    const QAccessibleMenuItem *self) {
  return new QAccessible::State(self->QAccessibleMenuItem::state());
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
#if QT_CONFIG(menu)
//  void QAccessibleMenuItem::doAction(const QString &actionName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAccessibleMenuItem8doActionERK7QString(
    QAccessibleMenuItem *self,
    const QString *actionName) {
  self->QAccessibleMenuItem::doAction(*actionName);
}
#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(menu)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(accessibility)
