//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusmenubar_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qdbusplatformmenu_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QDebug>
#include <QtGui/QWindow>
#include <QtGui/private/qdbusmenubar_p.h>
#include <QtGui/private/qdbusmenuregistrarproxy_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qdesktopunixservices_p.h>
#include <QtGui/qpa/qplatformintegration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 206, as _ZN17QDBusPlatformMenu11emitUpdatedEv
inline void QDBusPlatformMenu::emitUpdated()
{
    if (m_containingMenuItem)
        emit updated(++m_revision, m_containingMenuItem->dbusID());
    else
        emit updated(++m_revision, 0);
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 130, as _ZN17QDBusPlatformMenuC1Ev
inline QDBusPlatformMenu::QDBusPlatformMenu()
    : m_isEnabled(true)
    , m_isVisible(true)
    , m_revision(1)
    , m_containingMenuItem(nullptr)
{
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenubar.cpp, line 70, as _ZN12QDBusMenuBar10insertMenuEP13QPlatformMenuS1_
inline void QDBusMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu *before)
{
    QDBusPlatformMenuItem *menuItem = menuItemForMenu(menu);
    QDBusPlatformMenuItem *beforeItem = menuItemForMenu(before);
    m_menu->insertMenuItem(menuItem, beforeItem);
    m_menu->emitUpdated();
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenubar.cpp, line 78, as _ZN12QDBusMenuBar10removeMenuEP13QPlatformMenu
inline void QDBusMenuBar::removeMenu(QPlatformMenu *menu)
{
    QDBusPlatformMenuItem *menuItem = menuItemForMenu(menu);
    m_menu->removeMenuItem(menuItem);
    m_menu->emitUpdated();
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenubar.cpp, line 85, as _ZN12QDBusMenuBar8syncMenuEP13QPlatformMenu
inline void QDBusMenuBar::syncMenu(QPlatformMenu *menu)
{
    QDBusPlatformMenuItem *menuItem = menuItemForMenu(menu);
    updateMenuItem(menuItem, menu);
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenubar.cpp, line 91, as _ZN12QDBusMenuBar14handleReparentEP7QWindow
inline void QDBusMenuBar::handleReparent(QWindow *newParentWindow)
{
    if (newParentWindow) {
        unregisterMenuBar();
        m_window = newParentWindow;
        registerMenuBar();
    }
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenubar.cpp, line 100, as _ZNK12QDBusMenuBar10menuForTagEy
inline QPlatformMenu *QDBusMenuBar::menuForTag(quintptr tag) const
{
    QDBusPlatformMenuItem *menuItem = m_menuItems.value(tag);
    if (menuItem)
        return const_cast<QPlatformMenu *>(menuItem->menu());
    return nullptr;
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenubar.cpp, line 108, as _ZNK12QDBusMenuBar10createMenuEv
inline QPlatformMenu *QDBusMenuBar::createMenu() const
{
    return new QDBusPlatformMenu;
}
//  -----------------------------------------------------------------------

//  A QDBusMenuBar that Python can take functions over in. Every QDBusMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDBusMenuBarCall0)(const void *, QPlatformMenu *, QPlatformMenu *, int *);
typedef void (*CuteQDBusMenuBarCall1)(const void *, QPlatformMenu *, int *);
typedef void (*CuteQDBusMenuBarCall2)(const void *, QPlatformMenu *, int *);
typedef void (*CuteQDBusMenuBarCall3)(const void *, QWindow *, int *);
typedef void * (*CuteQDBusMenuBarCall4)(const void *, quintptr, int *);
typedef void * (*CuteQDBusMenuBarCall5)(const void *, int *);
typedef void * (*CuteQDBusMenuBarCall6)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuBarCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusMenuBarCall8)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuBarCall9)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuBarCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuBarCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuBarCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusMenuBarCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusMenuBar : public QDBusMenuBar {
public:
  using QDBusMenuBar::QDBusMenuBar;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar10insertMenuEP13QPlatformMenuS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar10removeMenuEP13QPlatformMenu")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar8syncMenuEP13QPlatformMenu")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QPlatformMenuBar14handleReparentEP7QWindow")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformMenuBar10menuForTagEy")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformMenuBar10createMenuEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QPlatformMenuBar12parentWindowEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDBusMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu
  //      *before)
  void insertMenu(QPlatformMenu *menu, QPlatformMenu *before) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusMenuBarCall0 call = reinterpret_cast<CuteQDBusMenuBarCall0>(taken[0]);
      call(this, menu, before, &handled);
      if (handled) return;
    }
    QDBusMenuBar::insertMenu(menu, before);
  }

  //  void QDBusMenuBar::removeMenu(QPlatformMenu *menu)
  void removeMenu(QPlatformMenu *menu) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusMenuBarCall1 call = reinterpret_cast<CuteQDBusMenuBarCall1>(taken[1]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QDBusMenuBar::removeMenu(menu);
  }

  //  void QDBusMenuBar::syncMenu(QPlatformMenu *menu)
  void syncMenu(QPlatformMenu *menu) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusMenuBarCall2 call = reinterpret_cast<CuteQDBusMenuBarCall2>(taken[2]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QDBusMenuBar::syncMenu(menu);
  }

  //  void QDBusMenuBar::handleReparent(QWindow *newParentWindow)
  void handleReparent(QWindow *newParentWindow) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusMenuBarCall3 call = reinterpret_cast<CuteQDBusMenuBarCall3>(taken[3]);
      call(this, newParentWindow, &handled);
      if (handled) return;
    }
    QDBusMenuBar::handleReparent(newParentWindow);
  }

  //  QPlatformMenu *QDBusMenuBar::menuForTag(quintptr tag) const
  QPlatformMenu *menuForTag(quintptr tag) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDBusMenuBarCall4 call = reinterpret_cast<CuteQDBusMenuBarCall4>(taken[4]);
      void * given = call(this, tag, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QDBusMenuBar::menuForTag(tag);
  }

  //  QPlatformMenu *QDBusMenuBar::createMenu() const
  QPlatformMenu *createMenu() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDBusMenuBarCall5 call = reinterpret_cast<CuteQDBusMenuBarCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QDBusMenuBar::createMenu();
  }

  //  QWindow *QPlatformMenuBar::parentWindow() const
  QWindow *parentWindow() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDBusMenuBarCall6 call = reinterpret_cast<CuteQDBusMenuBarCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindow *>(given);
    }
    return QPlatformMenuBar::parentWindow();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDBusMenuBarCall7 call = reinterpret_cast<CuteQDBusMenuBarCall7>(taken[7]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDBusMenuBarCall8 call = reinterpret_cast<CuteQDBusMenuBarCall8>(taken[8]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDBusMenuBarCall9 call = reinterpret_cast<CuteQDBusMenuBarCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDBusMenuBarCall10 call = reinterpret_cast<CuteQDBusMenuBarCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDBusMenuBarCall11 call = reinterpret_cast<CuteQDBusMenuBarCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDBusMenuBarCall12 call = reinterpret_cast<CuteQDBusMenuBarCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDBusMenuBarCall13 call = reinterpret_cast<CuteQDBusMenuBarCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QDBusMenuBar10metaObjectEv(
    const QDBusMenuBar *self) {
  return self->metaObject();
}

//  QDBusMenuBar::~QDBusMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMenuBarD1Ev(QDBusMenuBar *self) {
  delete self;
}

//  void QDBusMenuBar::insertMenu(QPlatformMenu *menu, QPlatformMenu *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMenuBar10insertMenuEP13QPlatformMenuS1_(
    QDBusMenuBar *self,
    QPlatformMenu *menu,
    QPlatformMenu *before) {
  self->insertMenu(menu, before);
}

//  void QDBusMenuBar::removeMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMenuBar10removeMenuEP13QPlatformMenu(
    QDBusMenuBar *self,
    QPlatformMenu *menu) {
  self->removeMenu(menu);
}

//  void QDBusMenuBar::syncMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMenuBar8syncMenuEP13QPlatformMenu(
    QDBusMenuBar *self,
    QPlatformMenu *menu) {
  self->syncMenu(menu);
}

//  void QDBusMenuBar::handleReparent(QWindow *newParentWindow)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDBusMenuBar14handleReparentEP7QWindow(
    QDBusMenuBar *self,
    QWindow *newParentWindow) {
  self->handleReparent(newParentWindow);
}

//  QPlatformMenu *QDBusMenuBar::menuForTag(quintptr tag) const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK12QDBusMenuBar10menuForTagEy(
    const QDBusMenuBar *self,
    quintptr tag) {
  return self->menuForTag(tag);
}

//  QPlatformMenu *QDBusMenuBar::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK12QDBusMenuBar10createMenuEv(
    const QDBusMenuBar *self) {
  return self->createMenu();
}

//  a Python function taken by a CuteQDBusMenuBar, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusMenuBar(
    QDBusMenuBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusMenuBar *>(self)->take(key, call);
}

//  QPlatformMenu *QDBusMenuBar::menuForTag(quintptr tag) const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_own_ZNK12QDBusMenuBar10menuForTagEy(
    const QDBusMenuBar *self,
    quintptr tag) {
  return self->QDBusMenuBar::menuForTag(tag);
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
