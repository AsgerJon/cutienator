//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbusplatformmenu_p.h, Qt 6.12.0. Changes made
//  here are lost.
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
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbusmenutypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qdbusplatformmenu_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QDebug>
#include <QtGui/QWindow>
#include <QtGui/private/qdbusmenutypes_p.h>
#include <QDBusConnection>
#include <QDBusMetaType>
#include <QtGui/QImage>
#include <QtGui/QIcon>
#include <QtGui/QImage>
#include <QtGui/QPixmap>
#include <QtCore/QDebug>
#include <QtCore/QtEndian>
#include <QtCore/QBuffer>
#if QT_CONFIG(shortcut)
#  include <QtGui/private/qkeysequence_p.h>
#endif
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/private/qdbusplatformmenu_p.h>
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

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 224, as _ZN17QDBusPlatformMenu10setEnabledEb
inline void QDBusPlatformMenu::setEnabled(bool enabled)
{
    m_isEnabled = enabled;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 229, as _ZN17QDBusPlatformMenu10setVisibleEb
inline void QDBusPlatformMenu::setVisible(bool isVisible)
{
    m_isVisible = isVisible;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 144, as _ZN17QDBusPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_
inline void QDBusPlatformMenu::insertMenuItem(QPlatformMenuItem *menuItem, QPlatformMenuItem *before)
{
    QDBusPlatformMenuItem *item = static_cast<QDBusPlatformMenuItem *>(menuItem);
    QDBusPlatformMenuItem *beforeItem = static_cast<QDBusPlatformMenuItem *>(before);
    int idx = m_items.indexOf(beforeItem);
    qCDebug(qLcMenu) << item->dbusID() << item->text();
    if (idx < 0)
        m_items.append(item);
    else
        m_items.insert(idx, item);
    m_itemsByTag.insert(item->tag(), item);
    if (item->menu())
        syncSubMenu(static_cast<const QDBusPlatformMenu *>(item->menu()));
    emitUpdated();
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 160, as _ZN17QDBusPlatformMenu14removeMenuItemEP17QPlatformMenuItem
inline void QDBusPlatformMenu::removeMenuItem(QPlatformMenuItem *menuItem)
{
    QDBusPlatformMenuItem *item = static_cast<QDBusPlatformMenuItem *>(menuItem);
    m_items.removeAll(item);
    m_itemsByTag.remove(menuItem->tag());
    if (item->menu()) {
        // disconnect from the signals we connected to in syncSubMenu()
        const QDBusPlatformMenu *menu = static_cast<const QDBusPlatformMenu *>(item->menu());
        disconnect(menu, &QDBusPlatformMenu::propertiesUpdated,
                   this, &QDBusPlatformMenu::propertiesUpdated);
        disconnect(menu, &QDBusPlatformMenu::updated,
                   this, &QDBusPlatformMenu::updated);
        disconnect(menu, &QDBusPlatformMenu::popupRequested,
                   this, &QDBusPlatformMenu::popupRequested);
    }
    emitUpdated();
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 190, as _ZN17QDBusPlatformMenu12syncMenuItemEP17QPlatformMenuItem
inline void QDBusPlatformMenu::syncMenuItem(QPlatformMenuItem *menuItem)
{
    QDBusPlatformMenuItem *item = static_cast<QDBusPlatformMenuItem *>(menuItem);
    // if a submenu was added to this item, we need to connect to its signals
    if (item->menu())
        syncSubMenu(static_cast<const QDBusPlatformMenu *>(item->menu()));
    // TODO keep around copies of the QDBusMenuLayoutItems so they can be updated?
    // or eliminate them by putting dbus streaming operators in this class instead?
    // or somehow tell the dbusmenu client that something has changed, so it will ask for properties again
    QDBusMenuItemList updated;
    QDBusMenuItemKeysList removed;
    updated << QDBusMenuItem(item);
    qCDebug(qLcMenu) << updated;
    emit propertiesUpdated(updated, removed);
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 214, as _ZN17QDBusPlatformMenu7setTextERK7QString
inline void QDBusPlatformMenu::setText(const QString &text)
{
    m_text = text;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 219, as _ZN17QDBusPlatformMenu7setIconERK5QIcon
inline void QDBusPlatformMenu::setIcon(const QIcon &icon)
{
    m_icon = icon;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 239, as _ZN17QDBusPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMenuItem
inline void QDBusPlatformMenu::showPopup(const QWindow *parentWindow, const QRect &targetRect, const QPlatformMenuItem *item)
{
    Q_UNUSED(parentWindow);
    Q_UNUSED(targetRect);
    Q_UNUSED(item);
    setVisible(true);
    emit popupRequested(m_containingMenuItem->dbusID(), QDateTime::currentMSecsSinceEpoch());
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 248, as _ZNK17QDBusPlatformMenu10menuItemAtEi
inline QPlatformMenuItem *QDBusPlatformMenu::menuItemAt(int position) const
{
    return m_items.value(position);
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 253, as _ZNK17QDBusPlatformMenu14menuItemForTagEy
inline QPlatformMenuItem *QDBusPlatformMenu::menuItemForTag(quintptr tag) const
{
    return m_itemsByTag[tag];
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 263, as _ZNK17QDBusPlatformMenu14createMenuItemEv
inline QPlatformMenuItem *QDBusPlatformMenu::createMenuItem() const
{
    QDBusPlatformMenuItem *ret = new QDBusPlatformMenuItem();
    return ret;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 269, as _ZNK17QDBusPlatformMenu13createSubMenuEv
inline QPlatformMenu *QDBusPlatformMenu::createSubMenu() const
{
    return new QDBusPlatformMenu;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 13, as _Z7qLcMenuv
inline const QLoggingCategory &qLcMenu()
{
    static const QLoggingCategory category("qt.qpa.menu");
    return category;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 206, as _ZN17QDBusPlatformMenu11emitUpdatedEv
inline void QDBusPlatformMenu::emitUpdated()
{
    if (m_containingMenuItem)
        emit updated(++m_revision, m_containingMenuItem->dbusID());
    else
        emit updated(++m_revision, 0);
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 178, as _ZN17QDBusPlatformMenu11syncSubMenuEPKS_
inline void QDBusPlatformMenu::syncSubMenu(const QDBusPlatformMenu *menu)
{
    // The adaptor is only connected to the propertiesUpdated signal of the top-level
    // menu, so the submenus should transfer their signals to their parents.
    connect(menu, &QDBusPlatformMenu::propertiesUpdated,
            this, &QDBusPlatformMenu::propertiesUpdated, Qt::UniqueConnection);
    connect(menu, &QDBusPlatformMenu::updated,
            this, &QDBusPlatformMenu::updated, Qt::UniqueConnection);
    connect(menu, &QDBusPlatformMenu::popupRequested,
            this, &QDBusPlatformMenu::popupRequested, Qt::UniqueConnection);
}

//  from src/gui/platform/unix/dbusmenu/qdbusmenutypes.cpp, line 158, as _ZN13QDBusMenuItemC1EPK21QDBusPlatformMenuItem
inline QDBusMenuItem::QDBusMenuItem(const QDBusPlatformMenuItem *item)
    : m_id(item->dbusID())
{
    if (item->isSeparator()) {
        m_properties.insert("type"_L1, "separator"_L1);
    } else {
        m_properties.insert("label"_L1, convertMnemonic(item->text()));
        if (item->menu())
            m_properties.insert("children-display"_L1, "submenu"_L1);
        m_properties.insert("enabled"_L1, item->isEnabled());
        if (item->isCheckable()) {
            QString toggleType = item->hasExclusiveGroup() ? "radio"_L1 : "checkmark"_L1;
            m_properties.insert("toggle-type"_L1, toggleType);
            m_properties.insert("toggle-state"_L1, item->isChecked() ? 1 : 0);
        }
#ifndef QT_NO_SHORTCUT
        const QKeySequence &scut = item->shortcut();
        if (!scut.isEmpty()) {
            QDBusMenuShortcut shortcut = convertKeySequence(scut);
            m_properties.insert("shortcut"_L1, QVariant::fromValue(shortcut));
        }
#endif
        const QIcon &icon = item->icon();
        if (!icon.name().isEmpty()) {
            m_properties.insert("icon-name"_L1, icon.name());
        } else if (!icon.isNull()) {
            QBuffer buf;
            icon.pixmap(16).save(&buf, "PNG");
            m_properties.insert("icon-data"_L1, buf.data());
        }
    }
    m_properties.insert("visible"_L1, item->isVisible());
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 130, as _ZN17QDBusPlatformMenuC1Ev
inline QDBusPlatformMenu::QDBusPlatformMenu()
    : m_isEnabled(true)
    , m_isVisible(true)
    , m_revision(1)
    , m_containingMenuItem(nullptr)
{
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 138, as _ZN17QDBusPlatformMenuD1Ev
inline QDBusPlatformMenu::~QDBusPlatformMenu()
{
    if (m_containingMenuItem)
        m_containingMenuItem->setMenu(nullptr);
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 234, as _ZN17QDBusPlatformMenu21setContainingMenuItemEP21QDBusPlatformMenuItem
inline void QDBusPlatformMenu::setContainingMenuItem(QDBusPlatformMenuItem *item)
{
    m_containingMenuItem = item;
}

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 258, as _ZNK17QDBusPlatformMenu5itemsEv
inline const QList<QDBusPlatformMenuItem *> QDBusPlatformMenu::items() const
{
    return m_items;
}
//  -----------------------------------------------------------------------

//  A QDBusPlatformMenu that Python can take functions over in. Every QDBusPlatformMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQDBusPlatformMenuCall0)(const void *, QPlatformMenuItem *, QPlatformMenuItem *, int *);
typedef void (*CuteQDBusPlatformMenuCall1)(const void *, QPlatformMenuItem *, int *);
typedef void (*CuteQDBusPlatformMenuCall2)(const void *, QPlatformMenuItem *, int *);
typedef void (*CuteQDBusPlatformMenuCall3)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuCall4)(const void *, const QString *, int *);
typedef void (*CuteQDBusPlatformMenuCall5)(const void *, const QIcon *, int *);
typedef bool (*CuteQDBusPlatformMenuCall6)(const void *, int *);
typedef void (*CuteQDBusPlatformMenuCall7)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuCall8)(const void *, bool, int *);
typedef void (*CuteQDBusPlatformMenuCall9)(const void *, int, int *);
typedef void (*CuteQDBusPlatformMenuCall10)(const void *, const QFont *, int *);
typedef void (*CuteQDBusPlatformMenuCall11)(const void *, int, int *);
typedef void (*CuteQDBusPlatformMenuCall12)(const void *, const QWindow *, const QRect *, const QPlatformMenuItem *, int *);
typedef void (*CuteQDBusPlatformMenuCall13)(const void *, int *);
typedef void * (*CuteQDBusPlatformMenuCall14)(const void *, int, int *);
typedef void * (*CuteQDBusPlatformMenuCall15)(const void *, quintptr, int *);
typedef void * (*CuteQDBusPlatformMenuCall16)(const void *, int *);
typedef void * (*CuteQDBusPlatformMenuCall17)(const void *, int *);
typedef void (*CuteQDBusPlatformMenuCall18)(const void *, quintptr, int *);
typedef quintptr (*CuteQDBusPlatformMenuCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPlatformMenuCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPlatformMenuCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPlatformMenuCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusPlatformMenu : public QDBusPlatformMenu {
public:
  using QDBusPlatformMenu::QDBusPlatformMenu;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu14removeMenuItemEP17QPlatformMenuItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu12syncMenuItemEP17QPlatformMenuItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu25syncSeparatorsCollapsibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu7setTextERK7QString")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu7setIconERK5QIcon")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlatformMenu9isEnabledEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu10setEnabledEb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu10setVisibleEb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu15setMinimumWidthEi")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu7setFontERK5QFont")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu11setMenuTypeENS_8MenuTypeE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMenuItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu7dismissEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlatformMenu10menuItemAtEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlatformMenu14menuItemForTagEy")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlatformMenu14createMenuItemEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlatformMenu13createSubMenuEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13QPlatformMenu6setTagEy")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13QPlatformMenu3tagEv")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QDBusPlatformMenu::insertMenuItem(QPlatformMenuItem *menuItem,
  //      QPlatformMenuItem *before)
  void insertMenuItem(
      QPlatformMenuItem *menuItem,
      QPlatformMenuItem *before) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall0 call = reinterpret_cast<CuteQDBusPlatformMenuCall0>(taken[0]);
      call(this, menuItem, before, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::insertMenuItem(menuItem, before);
  }

  //  void QDBusPlatformMenu::removeMenuItem(QPlatformMenuItem *menuItem)
  void removeMenuItem(QPlatformMenuItem *menuItem) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall1 call = reinterpret_cast<CuteQDBusPlatformMenuCall1>(taken[1]);
      call(this, menuItem, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::removeMenuItem(menuItem);
  }

  //  void QDBusPlatformMenu::syncMenuItem(QPlatformMenuItem *menuItem)
  void syncMenuItem(QPlatformMenuItem *menuItem) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall2 call = reinterpret_cast<CuteQDBusPlatformMenuCall2>(taken[2]);
      call(this, menuItem, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::syncMenuItem(menuItem);
  }

  //  void QDBusPlatformMenu::syncSeparatorsCollapsible(bool enable)
  void syncSeparatorsCollapsible(bool enable) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall3 call = reinterpret_cast<CuteQDBusPlatformMenuCall3>(taken[3]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::syncSeparatorsCollapsible(enable);
  }

  //  void QDBusPlatformMenu::setText(const QString &text)
  void setText(const QString &text) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall4 call = reinterpret_cast<CuteQDBusPlatformMenuCall4>(taken[4]);
      call(this, &text, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setText(text);
  }

  //  void QDBusPlatformMenu::setIcon(const QIcon &icon)
  void setIcon(const QIcon &icon) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall5 call = reinterpret_cast<CuteQDBusPlatformMenuCall5>(taken[5]);
      call(this, &icon, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setIcon(icon);
  }

  //  bool QDBusPlatformMenu::isEnabled() const
  bool isEnabled() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall6 call = reinterpret_cast<CuteQDBusPlatformMenuCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDBusPlatformMenu::isEnabled();
  }

  //  void QDBusPlatformMenu::setEnabled(bool enabled)
  void setEnabled(bool enabled) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall7 call = reinterpret_cast<CuteQDBusPlatformMenuCall7>(taken[7]);
      call(this, enabled, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setEnabled(enabled);
  }

  //  void QDBusPlatformMenu::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall8 call = reinterpret_cast<CuteQDBusPlatformMenuCall8>(taken[8]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setVisible(visible);
  }

  //  void QDBusPlatformMenu::setMinimumWidth(int width)
  void setMinimumWidth(int width) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall9 call = reinterpret_cast<CuteQDBusPlatformMenuCall9>(taken[9]);
      call(this, width, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setMinimumWidth(width);
  }

  //  void QDBusPlatformMenu::setFont(const QFont &font)
  void setFont(const QFont &font) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall10 call = reinterpret_cast<CuteQDBusPlatformMenuCall10>(taken[10]);
      call(this, &font, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setFont(font);
  }

  //  void QDBusPlatformMenu::setMenuType(MenuType type)
  void setMenuType(QPlatformMenu::MenuType type) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall11 call = reinterpret_cast<CuteQDBusPlatformMenuCall11>(taken[11]);
      call(this, static_cast<int>(type), &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::setMenuType(type);
  }

  //  void QDBusPlatformMenu::showPopup(const QWindow *parentWindow, const
  //      QRect &targetRect, const QPlatformMenuItem *item)
  void showPopup(
      const QWindow *parentWindow,
      const QRect &targetRect,
      const QPlatformMenuItem *item) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall12 call = reinterpret_cast<CuteQDBusPlatformMenuCall12>(taken[12]);
      call(this, parentWindow, &targetRect, item, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::showPopup(parentWindow, targetRect, item);
  }

  //  void QDBusPlatformMenu::dismiss()
  void dismiss() override {
    if (taken[13]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall13 call = reinterpret_cast<CuteQDBusPlatformMenuCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QDBusPlatformMenu::dismiss();
  }

  //  QPlatformMenuItem *QDBusPlatformMenu::menuItemAt(int position) const
  QPlatformMenuItem *menuItemAt(int position) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall14 call = reinterpret_cast<CuteQDBusPlatformMenuCall14>(taken[14]);
      void * given = call(this, position, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QDBusPlatformMenu::menuItemAt(position);
  }

  //  QPlatformMenuItem *QDBusPlatformMenu::menuItemForTag(quintptr tag)
  //      const
  QPlatformMenuItem *menuItemForTag(quintptr tag) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall15 call = reinterpret_cast<CuteQDBusPlatformMenuCall15>(taken[15]);
      void * given = call(this, tag, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QDBusPlatformMenu::menuItemForTag(tag);
  }

  //  QPlatformMenuItem *QDBusPlatformMenu::createMenuItem() const
  QPlatformMenuItem *createMenuItem() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall16 call = reinterpret_cast<CuteQDBusPlatformMenuCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenuItem *>(given);
    }
    return QDBusPlatformMenu::createMenuItem();
  }

  //  QPlatformMenu *QDBusPlatformMenu::createSubMenu() const
  QPlatformMenu *createSubMenu() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall17 call = reinterpret_cast<CuteQDBusPlatformMenuCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QDBusPlatformMenu::createSubMenu();
  }

  //  void QPlatformMenu::setTag(quintptr tag)
  void setTag(quintptr tag) override {
    if (taken[18]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall18 call = reinterpret_cast<CuteQDBusPlatformMenuCall18>(taken[18]);
      call(this, tag, &handled);
      if (handled) return;
    }
    QPlatformMenu::setTag(tag);
  }

  //  quintptr QPlatformMenu::tag() const
  quintptr tag() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall19 call = reinterpret_cast<CuteQDBusPlatformMenuCall19>(taken[19]);
      quintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformMenu::tag();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall20 call = reinterpret_cast<CuteQDBusPlatformMenuCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall21 call = reinterpret_cast<CuteQDBusPlatformMenuCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall22 call = reinterpret_cast<CuteQDBusPlatformMenuCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall23 call = reinterpret_cast<CuteQDBusPlatformMenuCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall24 call = reinterpret_cast<CuteQDBusPlatformMenuCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall25 call = reinterpret_cast<CuteQDBusPlatformMenuCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQDBusPlatformMenuCall26 call = reinterpret_cast<CuteQDBusPlatformMenuCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusPlatformMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QDBusPlatformMenu10metaObjectEv(
    const QDBusPlatformMenu *self) {
  return self->metaObject();
}

//  void *QDBusPlatformMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QDBusPlatformMenu11qt_metacastEPKc(
    QDBusPlatformMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusPlatformMenu::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QDBusPlatformMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusPlatformMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QDBusPlatformMenu::~QDBusPlatformMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenuD1Ev(QDBusPlatformMenu *self) {
  delete self;
}

//  void QDBusPlatformMenu::insertMenuItem(QPlatformMenuItem *menuItem,
//      QPlatformMenuItem *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_(
    QDBusPlatformMenu *self,
    QPlatformMenuItem *menuItem,
    QPlatformMenuItem *before) {
  self->insertMenuItem(menuItem, before);
}

//  void QDBusPlatformMenu::removeMenuItem(QPlatformMenuItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu14removeMenuItemEP17QPlatformMenuItem(
    QDBusPlatformMenu *self,
    QPlatformMenuItem *menuItem) {
  self->removeMenuItem(menuItem);
}

//  void QDBusPlatformMenu::syncMenuItem(QPlatformMenuItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu12syncMenuItemEP17QPlatformMenuItem(
    QDBusPlatformMenu *self,
    QPlatformMenuItem *menuItem) {
  self->syncMenuItem(menuItem);
}

//  void QDBusPlatformMenu::syncSeparatorsCollapsible(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu25syncSeparatorsCollapsibleEb(
    QDBusPlatformMenu *self,
    bool enable) {
  self->syncSeparatorsCollapsible(enable);
}

//  const QString QDBusPlatformMenu::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QDBusPlatformMenu4textEv(
    const QDBusPlatformMenu *self) {
  return new QString(self->text());
}

//  void QDBusPlatformMenu::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu7setTextERK7QString(
    QDBusPlatformMenu *self,
    const QString *text) {
  self->setText(*text);
}

//  QIcon QDBusPlatformMenu::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK17QDBusPlatformMenu4iconEv(const QDBusPlatformMenu *self) {
  return new QIcon(self->icon());
}

//  void QDBusPlatformMenu::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu7setIconERK5QIcon(
    QDBusPlatformMenu *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  bool QDBusPlatformMenu::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDBusPlatformMenu9isEnabledEv(
    const QDBusPlatformMenu *self) {
  return self->isEnabled();
}

//  void QDBusPlatformMenu::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu10setEnabledEb(
    QDBusPlatformMenu *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QDBusPlatformMenu::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QDBusPlatformMenu9isVisibleEv(
    const QDBusPlatformMenu *self) {
  return self->isVisible();
}

//  void QDBusPlatformMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu10setVisibleEb(
    QDBusPlatformMenu *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QDBusPlatformMenu::setMinimumWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu15setMinimumWidthEi(
    QDBusPlatformMenu *self,
    int width) {
  self->setMinimumWidth(width);
}

//  void QDBusPlatformMenu::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu7setFontERK5QFont(
    QDBusPlatformMenu *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QDBusPlatformMenu::setMenuType(MenuType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu11setMenuTypeEN13QPlatformMenu8MenuTypeE(
    QDBusPlatformMenu *self,
    QPlatformMenu::MenuType type) {
  self->setMenuType(type);
}

//  void QDBusPlatformMenu::setContainingMenuItem(QDBusPlatformMenuItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu21setContainingMenuItemEP21QDBusPlatformMenuItem(
    QDBusPlatformMenu *self,
    QDBusPlatformMenuItem *item) {
  self->setContainingMenuItem(item);
}

//  void QDBusPlatformMenu::showPopup(const QWindow *parentWindow, const
//      QRect &targetRect, const QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMenuItem(
    QDBusPlatformMenu *self,
    const QWindow *parentWindow,
    const QRect *targetRect,
    const QPlatformMenuItem *item) {
  self->showPopup(parentWindow, *targetRect, item);
}

//  void QDBusPlatformMenu::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu7dismissEv(QDBusPlatformMenu *self) {
  self->dismiss();
}

//  QPlatformMenuItem *QDBusPlatformMenu::menuItemAt(int position) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK17QDBusPlatformMenu10menuItemAtEi(
    const QDBusPlatformMenu *self,
    int position) {
  return self->menuItemAt(position);
}

//  QPlatformMenuItem *QDBusPlatformMenu::menuItemForTag(quintptr tag) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK17QDBusPlatformMenu14menuItemForTagEy(
    const QDBusPlatformMenu *self,
    quintptr tag) {
  return self->menuItemForTag(tag);
}

//  const QList<QDBusPlatformMenuItem *> QDBusPlatformMenu::items() const
extern "C" Q_DECL_EXPORT
QList<QDBusPlatformMenuItem *> *ritual_ZNK17QDBusPlatformMenu5itemsEv(
    const QDBusPlatformMenu *self) {
  return new QList<QDBusPlatformMenuItem *>(self->items());
}

//  QPlatformMenuItem *QDBusPlatformMenu::createMenuItem() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK17QDBusPlatformMenu14createMenuItemEv(
    const QDBusPlatformMenu *self) {
  return self->createMenuItem();
}

//  QPlatformMenu *QDBusPlatformMenu::createSubMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK17QDBusPlatformMenu13createSubMenuEv(
    const QDBusPlatformMenu *self) {
  return self->createSubMenu();
}

//  uint QDBusPlatformMenu::revision() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK17QDBusPlatformMenu8revisionEv(
    const QDBusPlatformMenu *self) {
  return self->revision();
}

//  void QDBusPlatformMenu::updated(uint revision, int dbusId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu7updatedEji(
    QDBusPlatformMenu *self,
    uint revision,
    int dbusId) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updated(uint,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updated(uint,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&revision)),
      const_cast<void *>(static_cast<const void *>(&dbusId)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusPlatformMenu::propertiesUpdated(QDBusMenuItemList updatedProps,
//      QDBusMenuItemKeysList removedProps)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu17propertiesUpdatedE5QListI13QDBusMenuItemES0_I17QDBusMenuItemKeysE(
    QDBusPlatformMenu *self,
    const QList<QDBusMenuItem> *updatedProps,
    const QList<QDBusMenuItemKeys> *removedProps) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "propertiesUpdated(QDBusMenuItemList,QDBusMenuItemKeysList)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "propertiesUpdated(QDBusMenuItemList,QDBusMenuItemKeysList)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(updatedProps)),
      const_cast<void *>(static_cast<const void *>(removedProps)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QDBusPlatformMenu::popupRequested(int id, uint timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDBusPlatformMenu14popupRequestedEij(
    QDBusPlatformMenu *self,
    int id,
    uint timestamp) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QDBusPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "popupRequested(int,uint)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "popupRequested(int,uint)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&id)),
      const_cast<void *>(static_cast<const void *>(&timestamp)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQDBusPlatformMenu, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusPlatformMenu(
    QDBusPlatformMenu *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusPlatformMenu *>(self)->take(key, call);
}

//  void QDBusPlatformMenu::syncSeparatorsCollapsible(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu25syncSeparatorsCollapsibleEb(
    QDBusPlatformMenu *self,
    bool enable) {
  self->QDBusPlatformMenu::syncSeparatorsCollapsible(enable);
}

//  void QDBusPlatformMenu::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu7setTextERK7QString(
    QDBusPlatformMenu *self,
    const QString *text) {
  self->QDBusPlatformMenu::setText(*text);
}

//  void QDBusPlatformMenu::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu7setIconERK5QIcon(
    QDBusPlatformMenu *self,
    const QIcon *icon) {
  self->QDBusPlatformMenu::setIcon(*icon);
}

//  bool QDBusPlatformMenu::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QDBusPlatformMenu9isEnabledEv(
    const QDBusPlatformMenu *self) {
  return self->QDBusPlatformMenu::isEnabled();
}

//  void QDBusPlatformMenu::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu10setEnabledEb(
    QDBusPlatformMenu *self,
    bool enabled) {
  self->QDBusPlatformMenu::setEnabled(enabled);
}

//  void QDBusPlatformMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu10setVisibleEb(
    QDBusPlatformMenu *self,
    bool visible) {
  self->QDBusPlatformMenu::setVisible(visible);
}

//  void QDBusPlatformMenu::setMinimumWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu15setMinimumWidthEi(
    QDBusPlatformMenu *self,
    int width) {
  self->QDBusPlatformMenu::setMinimumWidth(width);
}

//  void QDBusPlatformMenu::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu7setFontERK5QFont(
    QDBusPlatformMenu *self,
    const QFont *font) {
  self->QDBusPlatformMenu::setFont(*font);
}

//  void QDBusPlatformMenu::setMenuType(MenuType type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu11setMenuTypeEN13QPlatformMenu8MenuTypeE(
    QDBusPlatformMenu *self,
    QPlatformMenu::MenuType type) {
  self->QDBusPlatformMenu::setMenuType(type);
}

//  void QDBusPlatformMenu::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QDBusPlatformMenu7dismissEv(QDBusPlatformMenu *self) {
  self->QDBusPlatformMenu::dismiss();
}

//  QPlatformMenuItem *QDBusPlatformMenu::menuItemAt(int position) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_own_ZNK17QDBusPlatformMenu10menuItemAtEi(
    const QDBusPlatformMenu *self,
    int position) {
  return self->QDBusPlatformMenu::menuItemAt(position);
}

//  QPlatformMenuItem *QDBusPlatformMenu::menuItemForTag(quintptr tag) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_own_ZNK17QDBusPlatformMenu14menuItemForTagEy(
    const QDBusPlatformMenu *self,
    quintptr tag) {
  return self->QDBusPlatformMenu::menuItemForTag(tag);
}

#endif  // 1 && defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !defined(Q_OS_MACOS)) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
