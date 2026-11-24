//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdbustrayicon_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(systemtrayicon)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdbustrayicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qicon.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qdbusplatformmenu_p.h"
#include <QDateTime>
#include <QDebug>
#include <QWindow>
#include "qdbustrayicon_p.h"
#ifndef QT_NO_SYSTEMTRAYICON
#include <QString>
#include <QDebug>
#include <QRect>
#include <QLoggingCategory>
#include <QStandardPaths>
#include <QFileInfo>
#include <QDir>
#include <QMetaObject>
#include <QMetaEnum>
#include <QDBusConnectionInterface>
#include <QDBusArgument>
#include <QDBusMetaType>
#include <QDBusServiceWatcher>
#include <qpa/qplatformmenu.h>
#include <qpa/qplatformintegration.h>
#include <qpa/qplatformservices.h>
#include <private/qdbusmenuconnection_p.h>
#include <private/qstatusnotifieritemadaptor_p.h>
#include <private/qdbusmenuadaptor_p.h>
#include <private/qdbusplatformmenu_p.h>
#include <private/qxdgnotificationproxy_p.h>
#include <private/qlockfile_p.h>
#include <private/qguiapplication_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/platform/unix/dbusmenu/qdbusplatformmenu.cpp, line 130, as _ZN17QDBusPlatformMenuC1Ev
inline QDBusPlatformMenu::QDBusPlatformMenu()
    : m_isEnabled(true)
    , m_isVisible(true)
    , m_revision(1)
    , m_containingMenuItem(nullptr)
{
}

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 144, as _ZN13QDBusTrayIcon4initEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QDBusTrayIcon::init()
{
    qCDebug(qLcTray) << "registering" << m_instanceId;
    m_registered = dBusConnection()->registerTrayIcon(this);
    QObject::connect(dBusConnection()->dbusWatcher(), &QDBusServiceWatcher::serviceRegistered,
                     this, &QDBusTrayIcon::watcherServiceRegistered);
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 152, as _ZN13QDBusTrayIcon7cleanupEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QDBusTrayIcon::cleanup()
{
    qCDebug(qLcTray) << "unregistering" << m_instanceId;
    if (m_registered)
        dBusConnection()->unregisterTrayIcon(this);
    delete m_dbusConnection;
    m_dbusConnection = nullptr;
    delete m_notifier;
    m_notifier = nullptr;
    m_registered = false;
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 245, as _ZN13QDBusTrayIcon10updateIconERK5QIcon
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QDBusTrayIcon::updateIcon(const QIcon &icon)
{
    m_iconName = icon.name();
    m_icon = icon;
    if (m_iconName.isEmpty()) {
        if (m_tempIcon)
            delete m_tempIcon;
        m_tempIcon = tempIcon(icon);
        if (m_tempIcon)
            m_iconName = m_tempIcon->fileName();
    }
    qCDebug(qLcTray) << m_iconName << icon.availableSizes();
    emit iconChanged();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 260, as _ZN13QDBusTrayIcon13updateToolTipERK7QString
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QDBusTrayIcon::updateToolTip(const QString &tooltip)
{
    qCDebug(qLcTray) << tooltip;
    m_tooltip = tooltip;
    emit tooltipChanged();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 272, as _ZN13QDBusTrayIcon10updateMenuEP13QPlatformMenu
#if !defined(QT_NO_SYSTEMTRAYICON)
inline void QDBusTrayIcon::updateMenu(QPlatformMenu * menu)
{
    qCDebug(qLcTray) << menu;
    QDBusPlatformMenu *newMenu = qobject_cast<QDBusPlatformMenu *>(menu);
    if (m_menu != newMenu) {
        if (m_menu) {
            dBusConnection()->unregisterTrayIconMenu(this);
            delete m_menuAdaptor;
        }
        m_menu = newMenu;
        m_menuAdaptor = new QDBusMenuAdaptor(m_menu);
        // TODO connect(m_menu, , m_menuAdaptor, SIGNAL(ItemActivationRequested(int,uint)));
        connect(m_menu, SIGNAL(propertiesUpdated(QDBusMenuItemList,QDBusMenuItemKeysList)),
                m_menuAdaptor, SIGNAL(ItemsPropertiesUpdated(QDBusMenuItemList,QDBusMenuItemKeysList)));
        connect(m_menu, SIGNAL(updated(uint,int)),
                m_menuAdaptor, SIGNAL(LayoutUpdated(uint,int)));
        dBusConnection()->registerTrayIconMenu(this);
        emit menuChanged();
    }
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 267, as _ZNK13QDBusTrayIcon10createMenuEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline QPlatformMenu *QDBusTrayIcon::createMenu() const
{
    return new QDBusPlatformMenu();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

//  from src/gui/platform/unix/dbustray/qdbustrayicon.cpp, line 370, as _ZNK13QDBusTrayIcon21isSystemTrayAvailableEv
#if !defined(QT_NO_SYSTEMTRAYICON)
inline bool QDBusTrayIcon::isSystemTrayAvailable() const
{
    QDBusMenuConnection * conn = const_cast<QDBusTrayIcon *>(this)->dBusConnection();

    // If the KDE watcher service is registered, we must be on a desktop
    // where a StatusNotifier-conforming system tray exists.
    qCDebug(qLcTray) << conn->isWatcherRegistered();
    return conn->isWatcherRegistered();
}
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
//  -----------------------------------------------------------------------

//  A QDBusTrayIcon that Python can take functions over in. Every QDBusTrayIcon
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQDBusTrayIconCall0)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQDBusTrayIconCall1)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQDBusTrayIconCall2)(const void *, const QIcon *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQDBusTrayIconCall3)(const void *, const QString *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQDBusTrayIconCall4)(const void *, QPlatformMenu *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void * (*CuteQDBusTrayIconCall5)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQDBusTrayIconCall6)(const void *, const QString *, const QString *, const QIcon *, int, int, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef bool (*CuteQDBusTrayIconCall7)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef bool (*CuteQDBusTrayIconCall8)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
typedef const QRect * (*CuteQDBusTrayIconCall9)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusTrayIconCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusTrayIconCall11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusTrayIconCall12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusTrayIconCall13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusTrayIconCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusTrayIconCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusTrayIconCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusTrayIcon : public QDBusTrayIcon {
public:
  using QDBusTrayIcon::QDBusTrayIcon;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon4initEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon7cleanupEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon10updateIconERK5QIcon")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon13updateToolTipERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon10updateMenuEP13QPlatformMenu")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon10createMenuEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN23QPlatformSystemTrayIcon11showMessageERK7QStringS2_RK5QIconNS_11MessageIconEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon21isSystemTrayAvailableEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon16supportsMessagesEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZNK23QPlatformSystemTrayIcon8geometryEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  void QDBusTrayIcon::init()
  void init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQDBusTrayIconCall0 call = reinterpret_cast<CuteQDBusTrayIconCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QDBusTrayIcon::init();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  void QDBusTrayIcon::cleanup()
  void cleanup() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDBusTrayIconCall1 call = reinterpret_cast<CuteQDBusTrayIconCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QDBusTrayIcon::cleanup();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  void QDBusTrayIcon::updateIcon(const QIcon &icon)
  void updateIcon(const QIcon &icon) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDBusTrayIconCall2 call = reinterpret_cast<CuteQDBusTrayIconCall2>(taken[2]);
      call(this, &icon, &handled);
      if (handled) return;
    }
    QDBusTrayIcon::updateIcon(icon);
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  void QDBusTrayIcon::updateToolTip(const QString &tooltip)
  void updateToolTip(const QString &tooltip) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDBusTrayIconCall3 call = reinterpret_cast<CuteQDBusTrayIconCall3>(taken[3]);
      call(this, &tooltip, &handled);
      if (handled) return;
    }
    QDBusTrayIcon::updateToolTip(tooltip);
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  void QDBusTrayIcon::updateMenu(QPlatformMenu *menu)
  void updateMenu(QPlatformMenu *menu) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDBusTrayIconCall4 call = reinterpret_cast<CuteQDBusTrayIconCall4>(taken[4]);
      call(this, menu, &handled);
      if (handled) return;
    }
    QDBusTrayIcon::updateMenu(menu);
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  QPlatformMenu *QDBusTrayIcon::createMenu() const
  QPlatformMenu *createMenu() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDBusTrayIconCall5 call = reinterpret_cast<CuteQDBusTrayIconCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformMenu *>(given);
    }
    return QDBusTrayIcon::createMenu();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  void QDBusTrayIcon::showMessage(const QString &title, const QString
  //      &msg, const QIcon &icon, MessageIcon iconType, int msecs)
  void showMessage(
      const QString &title,
      const QString &msg,
      const QIcon &icon,
      QPlatformSystemTrayIcon::MessageIcon iconType,
      int msecs) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDBusTrayIconCall6 call = reinterpret_cast<CuteQDBusTrayIconCall6>(taken[6]);
      call(this, &title, &msg, &icon, static_cast<int>(iconType), msecs, &handled);
      if (handled) return;
    }
    QDBusTrayIcon::showMessage(title, msg, icon, iconType, msecs);
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  bool QDBusTrayIcon::isSystemTrayAvailable() const
  bool isSystemTrayAvailable() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQDBusTrayIconCall7 call = reinterpret_cast<CuteQDBusTrayIconCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDBusTrayIcon::isSystemTrayAvailable();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  bool QDBusTrayIcon::supportsMessages() const
  bool supportsMessages() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQDBusTrayIconCall8 call = reinterpret_cast<CuteQDBusTrayIconCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QDBusTrayIcon::supportsMessages();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_SYSTEMTRAYICON)
#if QT_CONFIG(systemtrayicon)
  //  QRect QDBusTrayIcon::geometry() const
  QRect geometry() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQDBusTrayIconCall9 call = reinterpret_cast<CuteQDBusTrayIconCall9>(taken[9]);
      const QRect * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDBusTrayIcon::geometry();
  }
#endif  // QT_CONFIG(systemtrayicon)
#endif  // !defined(QT_NO_SYSTEMTRAYICON)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDBusTrayIconCall10 call = reinterpret_cast<CuteQDBusTrayIconCall10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQDBusTrayIconCall11 call = reinterpret_cast<CuteQDBusTrayIconCall11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQDBusTrayIconCall12 call = reinterpret_cast<CuteQDBusTrayIconCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQDBusTrayIconCall13 call = reinterpret_cast<CuteQDBusTrayIconCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQDBusTrayIconCall14 call = reinterpret_cast<CuteQDBusTrayIconCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQDBusTrayIconCall15 call = reinterpret_cast<CuteQDBusTrayIconCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQDBusTrayIconCall16 call = reinterpret_cast<CuteQDBusTrayIconCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusTrayIcon::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QDBusTrayIcon10metaObjectEv(
    const QDBusTrayIcon *self) {
  return self->metaObject();
}

//  QDBusTrayIcon::~QDBusTrayIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusTrayIconD1Ev(QDBusTrayIcon *self) {
  delete self;
}

//  void QDBusTrayIcon::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusTrayIcon4initEv(QDBusTrayIcon *self) {
  self->init();
}

//  void QDBusTrayIcon::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusTrayIcon7cleanupEv(QDBusTrayIcon *self) {
  self->cleanup();
}

//  void QDBusTrayIcon::updateIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusTrayIcon10updateIconERK5QIcon(
    QDBusTrayIcon *self,
    const QIcon *icon) {
  self->updateIcon(*icon);
}

//  void QDBusTrayIcon::updateToolTip(const QString &tooltip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusTrayIcon13updateToolTipERK7QString(
    QDBusTrayIcon *self,
    const QString *tooltip) {
  self->updateToolTip(*tooltip);
}

//  void QDBusTrayIcon::updateMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QDBusTrayIcon10updateMenuEP13QPlatformMenu(
    QDBusTrayIcon *self,
    QPlatformMenu *menu) {
  self->updateMenu(menu);
}

//  QPlatformMenu *QDBusTrayIcon::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK13QDBusTrayIcon10createMenuEv(
    const QDBusTrayIcon *self) {
  return self->createMenu();
}

//  bool QDBusTrayIcon::isSystemTrayAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDBusTrayIcon21isSystemTrayAvailableEv(
    const QDBusTrayIcon *self) {
  return self->isSystemTrayAvailable();
}

//  bool QDBusTrayIcon::supportsMessages() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDBusTrayIcon16supportsMessagesEv(
    const QDBusTrayIcon *self) {
  return self->supportsMessages();
}

//  QRect QDBusTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QDBusTrayIcon8geometryEv(const QDBusTrayIcon *self) {
  return new QRect(self->geometry());
}

//  QString QDBusTrayIcon::category() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon8categoryEv(const QDBusTrayIcon *self) {
  return new QString(self->category());
}

//  QString QDBusTrayIcon::status() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon6statusEv(const QDBusTrayIcon *self) {
  return new QString(self->status());
}

//  QString QDBusTrayIcon::tooltip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon7tooltipEv(const QDBusTrayIcon *self) {
  return new QString(self->tooltip());
}

//  QString QDBusTrayIcon::iconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon8iconNameEv(const QDBusTrayIcon *self) {
  return new QString(self->iconName());
}

//  const QIcon &QDBusTrayIcon::icon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK13QDBusTrayIcon4iconEv(const QDBusTrayIcon *self) {
  return new QIcon(self->icon());
}

//  bool QDBusTrayIcon::isRequestingAttention() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QDBusTrayIcon21isRequestingAttentionEv(
    const QDBusTrayIcon *self) {
  return self->isRequestingAttention();
}

//  QString QDBusTrayIcon::attentionTitle() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon14attentionTitleEv(
    const QDBusTrayIcon *self) {
  return new QString(self->attentionTitle());
}

//  QString QDBusTrayIcon::attentionMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon16attentionMessageEv(
    const QDBusTrayIcon *self) {
  return new QString(self->attentionMessage());
}

//  QString QDBusTrayIcon::attentionIconName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon17attentionIconNameEv(
    const QDBusTrayIcon *self) {
  return new QString(self->attentionIconName());
}

//  const QIcon &QDBusTrayIcon::attentionIcon() const
extern "C" Q_DECL_EXPORT
QIcon *ritual_ZNK13QDBusTrayIcon13attentionIconEv(
    const QDBusTrayIcon *self) {
  return new QIcon(self->attentionIcon());
}

//  QString QDBusTrayIcon::instanceId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QDBusTrayIcon10instanceIdEv(const QDBusTrayIcon *self) {
  return new QString(self->instanceId());
}

//  QDBusPlatformMenu *QDBusTrayIcon::menu()
extern "C" Q_DECL_EXPORT
QDBusPlatformMenu *ritual_ZN13QDBusTrayIcon4menuEv(QDBusTrayIcon *self) {
  return self->menu();
}

//  a Python function taken by a CuteQDBusTrayIcon, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusTrayIcon(
    QDBusTrayIcon *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusTrayIcon *>(self)->take(key, call);
}

//  bool QDBusTrayIcon::supportsMessages() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QDBusTrayIcon16supportsMessagesEv(
    const QDBusTrayIcon *self) {
  return self->QDBusTrayIcon::supportsMessages();
}

//  QRect QDBusTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK13QDBusTrayIcon8geometryEv(const QDBusTrayIcon *self) {
  return new QRect(self->QDBusTrayIcon::geometry());
}

#endif  // QT_CONFIG(systemtrayicon)
