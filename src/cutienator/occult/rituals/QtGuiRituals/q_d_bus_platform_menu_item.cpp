//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusplatformmenu_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusplatformmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtGui/qkeysequence.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qdbusplatformmenu_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QDebug>
#include <QtGui/QWindow>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 39, as _ZN21QDBusPlatformMenuItem7setTextERK7QString
inline void QDBusPlatformMenuItem::setText(const QString &text)
{
    qCDebug(qLcMenu) << m_dbusID << text;
    m_text = text;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 45, as _ZN21QDBusPlatformMenuItem7setIconERK5QIcon
inline void QDBusPlatformMenuItem::setIcon(const QIcon &icon)
{
    m_icon = icon;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 54, as _ZN21QDBusPlatformMenuItem7setMenuEP13QPlatformMenu
inline void QDBusPlatformMenuItem::setMenu(QPlatformMenu *menu)
{
    if (m_subMenu)
        static_cast<QDBusPlatformMenu *>(m_subMenu)->setContainingMenuItem(nullptr);
    m_subMenu = menu;
    if (menu)
        static_cast<QDBusPlatformMenu *>(menu)->setContainingMenuItem(this);
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 63, as _ZN21QDBusPlatformMenuItem10setEnabledEb
inline void QDBusPlatformMenuItem::setEnabled(bool enabled)
{
    m_isEnabled = enabled;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 68, as _ZN21QDBusPlatformMenuItem10setVisibleEb
inline void QDBusPlatformMenuItem::setVisible(bool isVisible)
{
    m_isVisible = isVisible;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 73, as _ZN21QDBusPlatformMenuItem14setIsSeparatorEb
inline void QDBusPlatformMenuItem::setIsSeparator(bool isSeparator)
{
    m_isSeparator = isSeparator;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 78, as _ZN21QDBusPlatformMenuItem7setRoleEN17QPlatformMenuItem8MenuRoleE
inline void QDBusPlatformMenuItem::setRole(QPlatformMenuItem::MenuRole role)
{
    m_role = role;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 83, as _ZN21QDBusPlatformMenuItem12setCheckableEb
inline void QDBusPlatformMenuItem::setCheckable(bool checkable)
{
    m_isCheckable = checkable;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 88, as _ZN21QDBusPlatformMenuItem10setCheckedEb
inline void QDBusPlatformMenuItem::setChecked(bool isChecked)
{
    m_isChecked = isChecked;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 93, as _ZN21QDBusPlatformMenuItem20setHasExclusiveGroupEb
inline void QDBusPlatformMenuItem::setHasExclusiveGroup(bool hasExclusiveGroup)
{
    m_hasExclusiveGroup = hasExclusiveGroup;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 99, as _ZN21QDBusPlatformMenuItem11setShortcutERK12QKeySequence
#if !defined(QT_NO_SHORTCUT)
inline void QDBusPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
{
    m_shortcut = shortcut;
}
#endif  // !defined(QT_NO_SHORTCUT)

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 13, as _Z7qLcMenuv
inline const QLoggingCategory &qLcMenu()
{
    static const QLoggingCategory category("qt.qpa.menu");
    return category;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 234, as _ZN17QDBusPlatformMenu21setContainingMenuItemEP21QDBusPlatformMenuItem
inline void QDBusPlatformMenu::setContainingMenuItem(QDBusPlatformMenuItem *item)
{
    m_containingMenuItem = item;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 105, as _ZN21QDBusPlatformMenuItem7triggerEv
inline void QDBusPlatformMenuItem::trigger()
{
    emit activated();
}
//  -----------------------------------------------------------------------

//  A QDBusPlatformMenuItem that Python can take functions over in. Every QDBusPlatformMenuItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDBusPlatformMenuItemCall0)(const void *, const QString *, int *);
typedef void (*CuteQDBusPlatformMenuItemCall1)(const void *, const QIcon *, int *);
typedef void (*CuteQDBusPlatformMenuItemCall2)(const void *, QPlatformMenu *, int *);
typedef void (*CuteQDBusPlatformMenuItemCall3)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuItemCall4)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuItemCall5)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuItemCall6)(const void *, const QFont *, int *);
typedef void (*CuteQDBusPlatformMenuItemCall7)(const void *, int, int *);
typedef void (*CuteQDBusPlatformMenuItemCall8)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuItemCall9)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuItemCall10)(const void *, bool, int *);
#if QT_CONFIG(shortcut)
typedef void (*CuteQDBusPlatformMenuItemCall11)(const void *, const QKeySequence *, int *);
#endif  // QT_CONFIG(shortcut)
typedef void (*CuteQDBusPlatformMenuItemCall12)(const void *, int, int *);
typedef void (*CuteQDBusPlatformMenuItemCall13)(const void *, WId, int *);
typedef void (*CuteQDBusPlatformMenuItemCall14)(const void *, quintptr, int *);
typedef quintptr (*CuteQDBusPlatformMenuItemCall15)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPlatformMenuItemCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPlatformMenuItemCall17)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuItemCall18)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuItemCall19)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuItemCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuItemCall21)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuItemCall22)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusPlatformMenuItem : public QDBusPlatformMenuItem {
public:
  using QDBusPlatformMenuItem::QDBusPlatformMenuItem;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem7setTextERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem7setIconERK5QIcon")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem7setMenuEP13QPlatformMenu")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem10setEnabledEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem10setVisibleEb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem14setIsSeparatorEb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem7setFontERK5QFont")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem7setRoleENS_8MenuRoleE")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem12setCheckableEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem10setCheckedEb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem20setHasExclusiveGroupEb")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem11setShortcutERK12QKeySequence")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(shortcut)
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem11setIconSizeEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem17setNativeContentsEy")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformMenuItem6setTagEy")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QPlatformMenuItem3tagEv")) {
      taken[15] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDBusPlatformMenuItem::setText(const QString &text)
  void setText(const QString &text) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall0 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall0>(taken[0]);
      call(this, &text, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setText(text);
  }

  //  void QDBusPlatformMenuItem::setIcon(const QIcon &icon)
  void setIcon(const QIcon &icon) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall1 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall1>(taken[1]);
      call(this, &icon, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setIcon(icon);
  }

  //  void QDBusPlatformMenuItem::setMenu(QPlatformMenu *menu)
  void setMenu(QPlatformMenu *menu) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall2 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall2>(taken[2]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setMenu(menu);
  }

  //  void QDBusPlatformMenuItem::setEnabled(bool enabled)
  void setEnabled(bool enabled) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall3 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall3>(taken[3]);
      call(this, enabled, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setEnabled(enabled);
  }

  //  void QDBusPlatformMenuItem::setVisible(bool isVisible)
  void setVisible(bool isVisible) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall4 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall4>(taken[4]);
      call(this, isVisible, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setVisible(isVisible);
  }

  //  void QDBusPlatformMenuItem::setIsSeparator(bool isSeparator)
  void setIsSeparator(bool isSeparator) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall5 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall5>(taken[5]);
      call(this, isSeparator, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setIsSeparator(isSeparator);
  }

  //  void QDBusPlatformMenuItem::setFont(const QFont &font)
  void setFont(const QFont &font) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall6 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall6>(taken[6]);
      call(this, &font, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setFont(font);
  }

  //  void QDBusPlatformMenuItem::setRole(MenuRole role)
  void setRole(QPlatformMenuItem::MenuRole role) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall7 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall7>(taken[7]);
      call(this, static_cast<int>(role), &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setRole(role);
  }

  //  void QDBusPlatformMenuItem::setCheckable(bool checkable)
  void setCheckable(bool checkable) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall8 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall8>(taken[8]);
      call(this, checkable, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setCheckable(checkable);
  }

  //  void QDBusPlatformMenuItem::setChecked(bool isChecked)
  void setChecked(bool isChecked) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall9 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall9>(taken[9]);
      call(this, isChecked, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setChecked(isChecked);
  }

  //  void QDBusPlatformMenuItem::setHasExclusiveGroup(bool
  //      hasExclusiveGroup)
  void setHasExclusiveGroup(bool hasExclusiveGroup) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall10 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall10>(taken[10]);
      call(this, hasExclusiveGroup, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setHasExclusiveGroup(hasExclusiveGroup);
  }

#if QT_CONFIG(shortcut)
  //  void QDBusPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
  void setShortcut(const QKeySequence &shortcut) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall11 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall11>(taken[11]);
      call(this, &shortcut, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setShortcut(shortcut);
  }
#endif  // QT_CONFIG(shortcut)

  //  void QDBusPlatformMenuItem::setIconSize(int size)
  void setIconSize(int size) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall12 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall12>(taken[12]);
      call(this, size, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setIconSize(size);
  }

  //  void QDBusPlatformMenuItem::setNativeContents(WId item)
  void setNativeContents(WId item) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall13 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall13>(taken[13]);
      call(this, item, &handled);
      if (handled) return;
    }
    QDBusPlatformMenuItem::setNativeContents(item);
  }

  //  void QPlatformMenuItem::setTag(quintptr tag)
  void setTag(quintptr tag) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall14 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall14>(taken[14]);
      call(this, tag, &handled);
      if (handled) return;
    }
    QPlatformMenuItem::setTag(tag);
  }

  //  quintptr QPlatformMenuItem::tag() const
  quintptr tag() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall15 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall15>(taken[15]);
      quintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMenuItem::tag();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall16 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall16>(taken[16]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall17 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall17>(taken[17]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall18 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall19 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall20 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall21 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall21>(taken[21]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDBusPlatformMenuItemCall22 call = reinterpret_cast<CuteQDBusPlatformMenuItemCall22>(taken[22]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusPlatformMenuItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QDBusPlatformMenuItem10metaObjectEv(
    const QDBusPlatformMenuItem *self) {
  return self->metaObject();
}

//  void *QDBusPlatformMenuItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QDBusPlatformMenuItem11qt_metacastEPKc(
    QDBusPlatformMenuItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusPlatformMenuItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QDBusPlatformMenuItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusPlatformMenuItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QString QDBusPlatformMenuItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QDBusPlatformMenuItem4textEv(
    const QDBusPlatformMenuItem *self) {
  return new QString(self->text());
}

//  void QDBusPlatformMenuItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem7setTextERK7QString(
    QDBusPlatformMenuItem *self,
    const QString *text) {
  self->setText(*text);
}

//  QIcon QDBusPlatformMenuItem::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK21QDBusPlatformMenuItem4iconEv(
    const QDBusPlatformMenuItem *self) {
  return new QIcon(self->icon());
}

//  void QDBusPlatformMenuItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem7setIconERK5QIcon(
    QDBusPlatformMenuItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  const QPlatformMenu *QDBusPlatformMenuItem::menu() const
extern "C" Q_DECL_EXPORT
const QPlatformMenu *ritual_ZNK21QDBusPlatformMenuItem4menuEv(
    const QDBusPlatformMenuItem *self) {
  return self->menu();
}

//  void QDBusPlatformMenuItem::setMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem7setMenuEP13QPlatformMenu(
    QDBusPlatformMenuItem *self,
    QPlatformMenu *menu) {
  self->setMenu(menu);
}

//  bool QDBusPlatformMenuItem::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusPlatformMenuItem9isEnabledEv(
    const QDBusPlatformMenuItem *self) {
  return self->isEnabled();
}

//  void QDBusPlatformMenuItem::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem10setEnabledEb(
    QDBusPlatformMenuItem *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QDBusPlatformMenuItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusPlatformMenuItem9isVisibleEv(
    const QDBusPlatformMenuItem *self) {
  return self->isVisible();
}

//  void QDBusPlatformMenuItem::setVisible(bool isVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem10setVisibleEb(
    QDBusPlatformMenuItem *self,
    bool isVisible) {
  self->setVisible(isVisible);
}

//  bool QDBusPlatformMenuItem::isSeparator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusPlatformMenuItem11isSeparatorEv(
    const QDBusPlatformMenuItem *self) {
  return self->isSeparator();
}

//  void QDBusPlatformMenuItem::setIsSeparator(bool isSeparator)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem14setIsSeparatorEb(
    QDBusPlatformMenuItem *self,
    bool isSeparator) {
  self->setIsSeparator(isSeparator);
}

//  void QDBusPlatformMenuItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem7setFontERK5QFont(
    QDBusPlatformMenuItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QDBusPlatformMenuItem::setRole(MenuRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem7setRoleEN17QPlatformMenuItem8MenuRoleE(
    QDBusPlatformMenuItem *self,
    QPlatformMenuItem::MenuRole role) {
  self->setRole(role);
}

//  bool QDBusPlatformMenuItem::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusPlatformMenuItem11isCheckableEv(
    const QDBusPlatformMenuItem *self) {
  return self->isCheckable();
}

//  void QDBusPlatformMenuItem::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem12setCheckableEb(
    QDBusPlatformMenuItem *self,
    bool checkable) {
  self->setCheckable(checkable);
}

//  bool QDBusPlatformMenuItem::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusPlatformMenuItem9isCheckedEv(
    const QDBusPlatformMenuItem *self) {
  return self->isChecked();
}

//  void QDBusPlatformMenuItem::setChecked(bool isChecked)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem10setCheckedEb(
    QDBusPlatformMenuItem *self,
    bool isChecked) {
  self->setChecked(isChecked);
}

//  bool QDBusPlatformMenuItem::hasExclusiveGroup() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QDBusPlatformMenuItem17hasExclusiveGroupEv(
    const QDBusPlatformMenuItem *self) {
  return self->hasExclusiveGroup();
}

//  void QDBusPlatformMenuItem::setHasExclusiveGroup(bool hasExclusiveGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem20setHasExclusiveGroupEb(
    QDBusPlatformMenuItem *self,
    bool hasExclusiveGroup) {
  self->setHasExclusiveGroup(hasExclusiveGroup);
}

#if QT_CONFIG(shortcut)
//  QKeySequence QDBusPlatformMenuItem::shortcut() const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK21QDBusPlatformMenuItem8shortcutEv(
    const QDBusPlatformMenuItem *self) {
  return new QKeySequence(self->shortcut());
}
#endif  // QT_CONFIG(shortcut)

#if QT_CONFIG(shortcut)
//  void QDBusPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem11setShortcutERK12QKeySequence(
    QDBusPlatformMenuItem *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}
#endif  // QT_CONFIG(shortcut)

//  void QDBusPlatformMenuItem::setIconSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem11setIconSizeEi(
    QDBusPlatformMenuItem *self,
    int size) {
  self->setIconSize(size);
}

//  void QDBusPlatformMenuItem::setNativeContents(WId item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem17setNativeContentsEy(
    QDBusPlatformMenuItem *self,
    WId item) {
  self->setNativeContents(item);
}

//  int QDBusPlatformMenuItem::dbusID() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QDBusPlatformMenuItem6dbusIDEv(
    const QDBusPlatformMenuItem *self) {
  return self->dbusID();
}

//  void QDBusPlatformMenuItem::trigger()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QDBusPlatformMenuItem7triggerEv(
    QDBusPlatformMenuItem *self) {
  self->trigger();
}

//  a Python function taken by a CuteQDBusPlatformMenuItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusPlatformMenuItem(
    QDBusPlatformMenuItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusPlatformMenuItem *>(self)->take(key, call);
}

//  void QDBusPlatformMenuItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem7setTextERK7QString(
    QDBusPlatformMenuItem *self,
    const QString *text) {
  self->QDBusPlatformMenuItem::setText(*text);
}

//  void QDBusPlatformMenuItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem7setIconERK5QIcon(
    QDBusPlatformMenuItem *self,
    const QIcon *icon) {
  self->QDBusPlatformMenuItem::setIcon(*icon);
}

//  void QDBusPlatformMenuItem::setMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem7setMenuEP13QPlatformMenu(
    QDBusPlatformMenuItem *self,
    QPlatformMenu *menu) {
  self->QDBusPlatformMenuItem::setMenu(menu);
}

//  void QDBusPlatformMenuItem::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem10setEnabledEb(
    QDBusPlatformMenuItem *self,
    bool enabled) {
  self->QDBusPlatformMenuItem::setEnabled(enabled);
}

//  void QDBusPlatformMenuItem::setVisible(bool isVisible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem10setVisibleEb(
    QDBusPlatformMenuItem *self,
    bool isVisible) {
  self->QDBusPlatformMenuItem::setVisible(isVisible);
}

//  void QDBusPlatformMenuItem::setIsSeparator(bool isSeparator)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem14setIsSeparatorEb(
    QDBusPlatformMenuItem *self,
    bool isSeparator) {
  self->QDBusPlatformMenuItem::setIsSeparator(isSeparator);
}

//  void QDBusPlatformMenuItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem7setFontERK5QFont(
    QDBusPlatformMenuItem *self,
    const QFont *font) {
  self->QDBusPlatformMenuItem::setFont(*font);
}

//  void QDBusPlatformMenuItem::setRole(MenuRole role)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem7setRoleEN17QPlatformMenuItem8MenuRoleE(
    QDBusPlatformMenuItem *self,
    QPlatformMenuItem::MenuRole role) {
  self->QDBusPlatformMenuItem::setRole(role);
}

//  void QDBusPlatformMenuItem::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem12setCheckableEb(
    QDBusPlatformMenuItem *self,
    bool checkable) {
  self->QDBusPlatformMenuItem::setCheckable(checkable);
}

//  void QDBusPlatformMenuItem::setChecked(bool isChecked)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem10setCheckedEb(
    QDBusPlatformMenuItem *self,
    bool isChecked) {
  self->QDBusPlatformMenuItem::setChecked(isChecked);
}

//  void QDBusPlatformMenuItem::setHasExclusiveGroup(bool hasExclusiveGroup)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem20setHasExclusiveGroupEb(
    QDBusPlatformMenuItem *self,
    bool hasExclusiveGroup) {
  self->QDBusPlatformMenuItem::setHasExclusiveGroup(hasExclusiveGroup);
}

#if QT_CONFIG(shortcut)
#if !defined(QT_NO_SHORTCUT)
//  void QDBusPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem11setShortcutERK12QKeySequence(
    QDBusPlatformMenuItem *self,
    const QKeySequence *shortcut) {
  self->QDBusPlatformMenuItem::setShortcut(*shortcut);
}
#endif  // !defined(QT_NO_SHORTCUT)
#endif  // QT_CONFIG(shortcut)

//  void QDBusPlatformMenuItem::setIconSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem11setIconSizeEi(
    QDBusPlatformMenuItem *self,
    int size) {
  self->QDBusPlatformMenuItem::setIconSize(size);
}

//  void QDBusPlatformMenuItem::setNativeContents(WId item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QDBusPlatformMenuItem17setNativeContentsEy(
    QDBusPlatformMenuItem *self,
    WId item) {
  self->QDBusPlatformMenuItem::setNativeContents(item);
}

//  QList<QDBusPlatformMenuItem *>::QList()
extern "C" Q_DECL_EXPORT
QList<QDBusPlatformMenuItem *> *ritual_list_make_QDBusPlatformMenuItem_ptr() {
  return new QList<QDBusPlatformMenuItem *>();
}

//  void QList<QDBusPlatformMenuItem *>::append(const QDBusPlatformMenuItem *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDBusPlatformMenuItem_ptr(
    QList<QDBusPlatformMenuItem *> *self,
    QDBusPlatformMenuItem *element) {
  self->append(element);
}

//  qsizetype QList<QDBusPlatformMenuItem *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDBusPlatformMenuItem_ptr(
    const QList<QDBusPlatformMenuItem *> *self) {
  return self->size();
}

//  const QDBusPlatformMenuItem * &QList<QDBusPlatformMenuItem
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDBusPlatformMenuItem *ritual_list_at_QDBusPlatformMenuItem_ptr(
    const QList<QDBusPlatformMenuItem *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QDBusPlatformMenuItem *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDBusPlatformMenuItem_ptr(
    QList<QDBusPlatformMenuItem *> *self) {
  delete self;
}

//  a QList<const QDBusPlatformMenuItem *> a ritual of QDBusPlatformMenuItem
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QDBusPlatformMenuItem__QList_const_QDBusPlatformMenuItem(
    QList<const QDBusPlatformMenuItem *> *self) {
  delete self;
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
