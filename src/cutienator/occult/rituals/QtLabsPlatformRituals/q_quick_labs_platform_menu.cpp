//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenu_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenu_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformmenu_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenubar_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qicon.h>
#include <QtGui/qcursor.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQuick/qquickrendercontrol.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickitem.h>
#if QT_CONFIG(systemtrayicon)
#include <QtLabsPlatform/private/qquicklabsplatformsystemtrayicon_p.h>
#endif
#include <QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenu_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenuitemgroup_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtGui/qicon.h>
#if QT_CONFIG(shortcut)
#include <QtGui/qkeysequence.h>
#endif
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuickTemplates2/private/qquickshortcutcontext_p_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenubar_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenu_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickitem.h>
#include <QtLabsPlatform/private/qquicklabsplatformsystemtrayicon_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenu_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 737, as local:qquicklabsplatformmenu.cpp:effectiveWindow
static QWindow *effectiveWindow(QWindow *window, QPoint *offset)
{
    QQuickWindow *quickWindow = qobject_cast<QQuickWindow *>(window);
    if (quickWindow) {
        QWindow *renderWindow = QQuickRenderControl::renderWindowFor(quickWindow, offset);
        if (renderWindow)
            return renderWindow;
    }
    return window;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 714, as _ZN22QQuickLabsPlatformMenu10classBeginEv
inline void QQuickLabsPlatformMenu::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 611, as _ZN22QQuickLabsPlatformMenu10removeMenuEPS_
inline void QQuickLabsPlatformMenu::removeMenu(QQuickLabsPlatformMenu *menu)
{
    if (!menu)
        return;

    menu->setParentMenu(nullptr);
    removeItem(menu->menuItem());
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 127, as _ZN26QQuickLabsPlatformMenuItem4syncEv
inline void QQuickLabsPlatformMenuItem::sync()
{
    if (!m_complete || !create())
        return;

    m_handle->setEnabled(isEnabled());
    m_handle->setVisible(isVisible());
    m_handle->setIsSeparator(m_separator);
    m_handle->setCheckable(m_checkable);
    m_handle->setChecked(m_checked);
    m_handle->setRole(m_role);
    m_handle->setText(m_text);
    m_handle->setFont(m_font);
    m_handle->setHasExclusiveGroup(m_group && m_group->isExclusive());

    if (m_iconLoader)
        m_handle->setIcon(m_iconLoader->toQIcon());

    if (m_subMenu) {
        // Sync first as dynamically created menus may need to get the
        // handle recreated
        m_subMenu->sync();
        if (m_subMenu->handle())
            m_handle->setMenu(m_subMenu->handle());
    }

#if QT_CONFIG(shortcut)
    QKeySequence sequence;
    if (m_shortcut.metaType().id() == QMetaType::Int)
        sequence = QKeySequence(static_cast<QKeySequence::StandardKey>(m_shortcut.toInt()));
    else if (m_shortcut.metaType().id() == QMetaType::QKeySequence)
        sequence = m_shortcut.value<QKeySequence>();
    else
        sequence = QKeySequence::fromString(m_shortcut.toString());
    m_handle->setShortcut(sequence.toString());
#endif

    if (m_menu && m_menu->handle())
        m_menu->handle()->syncMenuItem(m_handle);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 93, as _ZNK25QQuickLabsPlatformMenuBar6handleEv
inline QPlatformMenuBar *QQuickLabsPlatformMenuBar::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 166, as _ZNK32QQuickLabsPlatformSystemTrayIcon6handleEv
inline QPlatformSystemTrayIcon *QQuickLabsPlatformSystemTrayIcon::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 625, as _ZN22QQuickLabsPlatformMenu5clearEv
inline void QQuickLabsPlatformMenu::clear()
{
    if (m_items.isEmpty())
        return;

    for (QQuickLabsPlatformMenuItem *item : std::as_const(m_items)) {
        m_data.removeOne(item);
        if (m_handle)
            m_handle->removeMenuItem(item->handle());
        item->setMenu(nullptr);
        delete item;
    }

    m_items.clear();
    sync();
    emit itemsChanged();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 538, as _ZN22QQuickLabsPlatformMenu7addItemEP26QQuickLabsPlatformMenuItem
inline void QQuickLabsPlatformMenu::addItem(QQuickLabsPlatformMenuItem *item)
{
    insertItem(m_items.size(), item);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 718, as _ZN22QQuickLabsPlatformMenu17componentCompleteEv
inline void QQuickLabsPlatformMenu::componentComplete()
{
    m_complete = true;
    if (m_handle && m_iconLoader)
        m_iconLoader->setEnabled(true);
    sync();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 548, as _ZN22QQuickLabsPlatformMenu10insertItemEiP26QQuickLabsPlatformMenuItem
inline void QQuickLabsPlatformMenu::insertItem(int index, QQuickLabsPlatformMenuItem *item)
{
    if (!item || m_items.contains(item))
        return;

    m_items.insert(index, item);
    m_data.append(item);
    item->setMenu(this);
    if (m_handle && item->create()) {
        QQuickLabsPlatformMenuItem *before = m_items.value(index + 1);
        m_handle->insertMenuItem(item->handle(), before ? before->create() : nullptr);
    }
    sync();
    emit itemsChanged();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 151, as _ZN22QQuickLabsPlatformMenuD1Ev
inline QQuickLabsPlatformMenu::~QQuickLabsPlatformMenu()
{
    if (m_menuBar)
        m_menuBar->removeMenu(this);
    if (m_parentMenu)
        m_parentMenu->removeMenu(this);

    unparentSubmenus();

    delete m_iconLoader;
    m_iconLoader = nullptr;
    delete m_handle;
    m_handle = nullptr;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 175, as _ZNK22QQuickLabsPlatformMenu6handleEv
inline QPlatformMenu *QQuickLabsPlatformMenu::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 288, as _ZNK22QQuickLabsPlatformMenu7menuBarEv
inline QQuickLabsPlatformMenuBar *QQuickLabsPlatformMenu::menuBar() const
{
    return m_menuBar;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 310, as _ZNK22QQuickLabsPlatformMenu10parentMenuEv
inline QQuickLabsPlatformMenu *QQuickLabsPlatformMenu::parentMenu() const
{
    return m_parentMenu;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 333, as _ZNK22QQuickLabsPlatformMenu14systemTrayIconEv
#if QT_CONFIG(systemtrayicon)
inline QQuickLabsPlatformSystemTrayIcon *QQuickLabsPlatformMenu::systemTrayIcon() const
{
    return m_systemTrayIcon;
}
#endif  // QT_CONFIG(systemtrayicon)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 375, as _ZNK22QQuickLabsPlatformMenu9isEnabledEv
inline bool QQuickLabsPlatformMenu::isEnabled() const
{
    return m_enabled;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 398, as _ZNK22QQuickLabsPlatformMenu9isVisibleEv
inline bool QQuickLabsPlatformMenu::isVisible() const
{
    return m_visible;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 421, as _ZNK22QQuickLabsPlatformMenu12minimumWidthEv
inline int QQuickLabsPlatformMenu::minimumWidth() const
{
    return m_minimumWidth;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 445, as _ZNK22QQuickLabsPlatformMenu4typeEv
inline QPlatformMenu::MenuType QQuickLabsPlatformMenu::type() const
{
    return m_type;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 465, as _ZNK22QQuickLabsPlatformMenu5titleEv
inline QString QQuickLabsPlatformMenu::title() const
{
    return m_title;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 490, as _ZNK22QQuickLabsPlatformMenu4fontEv
inline QFont QQuickLabsPlatformMenu::font() const
{
    return m_font;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 782, as _ZN22QQuickLabsPlatformMenu10data_countEP16QQmlListPropertyI7QObjectE
inline qsizetype QQuickLabsPlatformMenu::data_count(QQmlListProperty<QObject> *property)
{
    QQuickLabsPlatformMenu *menu = static_cast<QQuickLabsPlatformMenu *>(property->object);
    return menu->m_data.size();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 788, as _ZN22QQuickLabsPlatformMenu7data_atEP16QQmlListPropertyI7QObjectEx
inline QObject *QQuickLabsPlatformMenu::data_at(QQmlListProperty<QObject> *property, qsizetype index)
{
    QQuickLabsPlatformMenu *menu = static_cast<QQuickLabsPlatformMenu *>(property->object);
    return menu->m_data.value(index);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 794, as _ZN22QQuickLabsPlatformMenu10data_clearEP16QQmlListPropertyI7QObjectE
inline void QQuickLabsPlatformMenu::data_clear(QQmlListProperty<QObject> *property)
{
    QQuickLabsPlatformMenu *menu = static_cast<QQuickLabsPlatformMenu *>(property->object);
    menu->m_data.clear();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 806, as _ZN22QQuickLabsPlatformMenu11items_countEP16QQmlListPropertyI26QQuickLabsPlatformMenuItemE
inline qsizetype QQuickLabsPlatformMenu::items_count(QQmlListProperty<QQuickLabsPlatformMenuItem> *property)
{
    QQuickLabsPlatformMenu *menu = static_cast<QQuickLabsPlatformMenu *>(property->object);
    return menu->m_items.size();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 812, as _ZN22QQuickLabsPlatformMenu8items_atEP16QQmlListPropertyI26QQuickLabsPlatformMenuItemEx
inline QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenu::items_at(QQmlListProperty<QQuickLabsPlatformMenuItem> *property, qsizetype index)
{
    QQuickLabsPlatformMenu *menu = static_cast<QQuickLabsPlatformMenu *>(property->object);
    return menu->m_items.value(index);
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformMenu may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformMenu : QQuickLabsPlatformMenu {
  using QQuickLabsPlatformMenu::classBegin;
};

//  A QQuickLabsPlatformMenu that Python can take functions over in. Every QQuickLabsPlatformMenu
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLabsPlatformMenuCall0)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformMenuCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformMenu : public QQuickLabsPlatformMenu {
public:
  using QQuickLabsPlatformMenu::QQuickLabsPlatformMenu;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickLabsPlatformMenu::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall0 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenu::classBegin();
  }

  //  void QQuickLabsPlatformMenu::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall1 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenu::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall2 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall3 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall4 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall5 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall6 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall7 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuCall8 call = reinterpret_cast<CuteQQuickLabsPlatformMenuCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickLabsPlatformMenu10metaObjectEv(
    const QQuickLabsPlatformMenu *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickLabsPlatformMenu11qt_metacastEPKc(
    QQuickLabsPlatformMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformMenu::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickLabsPlatformMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QMetaObject *QQuickLabsPlatformMenu::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN22QQuickLabsPlatformMenu20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformMenu::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformMenu::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformMenu *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickLabsPlatformMenu::~QQuickLabsPlatformMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenuD1Ev(QQuickLabsPlatformMenu *self) {
  delete self;
}

//  QPlatformMenu *QQuickLabsPlatformMenu::handle() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK22QQuickLabsPlatformMenu6handleEv(
    const QQuickLabsPlatformMenu *self) {
  return self->handle();
}

//  QQuickLabsPlatformMenuBar *QQuickLabsPlatformMenu::menuBar() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenuBar *ritual_ZNK22QQuickLabsPlatformMenu7menuBarEv(
    const QQuickLabsPlatformMenu *self) {
  return self->menuBar();
}

//  QQuickLabsPlatformMenu *QQuickLabsPlatformMenu::parentMenu() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenu *ritual_ZNK22QQuickLabsPlatformMenu10parentMenuEv(
    const QQuickLabsPlatformMenu *self) {
  return self->parentMenu();
}

#if QT_CONFIG(systemtrayicon)
//  QQuickLabsPlatformSystemTrayIcon
//      *QQuickLabsPlatformMenu::systemTrayIcon() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformSystemTrayIcon *ritual_ZNK22QQuickLabsPlatformMenu14systemTrayIconEv(
    const QQuickLabsPlatformMenu *self) {
  return self->systemTrayIcon();
}
#endif  // QT_CONFIG(systemtrayicon)

//  bool QQuickLabsPlatformMenu::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickLabsPlatformMenu9isEnabledEv(
    const QQuickLabsPlatformMenu *self) {
  return self->isEnabled();
}

//  bool QQuickLabsPlatformMenu::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickLabsPlatformMenu9isVisibleEv(
    const QQuickLabsPlatformMenu *self) {
  return self->isVisible();
}

//  int QQuickLabsPlatformMenu::minimumWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickLabsPlatformMenu12minimumWidthEv(
    const QQuickLabsPlatformMenu *self) {
  return self->minimumWidth();
}

//  QPlatformMenu::MenuType QQuickLabsPlatformMenu::type() const
extern "C" Q_DECL_EXPORT
QPlatformMenu::MenuType ritual_ZNK22QQuickLabsPlatformMenu4typeEv(
    const QQuickLabsPlatformMenu *self) {
  return self->type();
}

//  QString QQuickLabsPlatformMenu::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickLabsPlatformMenu5titleEv(
    const QQuickLabsPlatformMenu *self) {
  return new QString(self->title());
}

//  QFont QQuickLabsPlatformMenu::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK22QQuickLabsPlatformMenu4fontEv(
    const QQuickLabsPlatformMenu *self) {
  return new QFont(self->font());
}

//  void QQuickLabsPlatformMenu::addItem(QQuickLabsPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu7addItemEP26QQuickLabsPlatformMenuItem(
    QQuickLabsPlatformMenu *self,
    QQuickLabsPlatformMenuItem *item) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "addItem(QQuickLabsPlatformMenuItem *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "addItem(QQuickLabsPlatformMenuItem *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&item)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::removeItem(QQuickLabsPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu10removeItemEP26QQuickLabsPlatformMenuItem(
    QQuickLabsPlatformMenu *self,
    QQuickLabsPlatformMenuItem *item) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeItem(QQuickLabsPlatformMenuItem *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeItem(QQuickLabsPlatformMenuItem *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&item)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::addMenu(QQuickLabsPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu7addMenuEPS_(
    QQuickLabsPlatformMenu *self,
    QQuickLabsPlatformMenu *menu) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "addMenu(QQuickLabsPlatformMenu *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "addMenu(QQuickLabsPlatformMenu *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&menu)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::removeMenu(QQuickLabsPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu10removeMenuEPS_(
    QQuickLabsPlatformMenu *self,
    QQuickLabsPlatformMenu *menu) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "removeMenu(QQuickLabsPlatformMenu *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "removeMenu(QQuickLabsPlatformMenu *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&menu)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu5clearEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clear()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clear()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::open(QQmlV4FunctionPtr args)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu4openEP14QQmlV4Function(
    QQuickLabsPlatformMenu *self,
    QQmlV4FunctionPtr args) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "open(QQmlV4FunctionPtr)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "open(QQmlV4FunctionPtr)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&args)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu5closeEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "close()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "close()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::aboutToShow()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu11aboutToShowEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "aboutToShow()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "aboutToShow()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::aboutToHide()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu11aboutToHideEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "aboutToHide()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "aboutToHide()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::itemsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu12itemsChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "itemsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "itemsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::menuBarChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu14menuBarChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuBarChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuBarChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::parentMenuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu17parentMenuChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "parentMenuChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "parentMenuChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::systemTrayIconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu21systemTrayIconChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "systemTrayIconChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "systemTrayIconChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::titleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu12titleChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "titleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "titleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu14enabledChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "enabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "enabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu14visibleChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "visibleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "visibleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::minimumWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu19minimumWidthChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "minimumWidthChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "minimumWidthChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu11fontChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "fontChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "fontChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::typeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu11typeChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "typeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "typeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::iconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu11iconChangedEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "iconChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "iconChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenu::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu10classBeginEv(
    QQuickLabsPlatformMenu *self) {
  self->classBegin();
}

//  void QQuickLabsPlatformMenu::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu17componentCompleteEv(
    QQuickLabsPlatformMenu *self) {
  self->componentComplete();
}

//  qsizetype QQuickLabsPlatformMenu::data_count(QQmlListProperty<QObject>
//      *property)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuickLabsPlatformMenu10data_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *property) {
  return QQuickLabsPlatformMenu::data_count(property);
}

//  QObject *QQuickLabsPlatformMenu::data_at(QQmlListProperty<QObject>
//      *property, qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQuickLabsPlatformMenu7data_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *property,
    qsizetype index) {
  return QQuickLabsPlatformMenu::data_at(property, index);
}

//  void QQuickLabsPlatformMenu::data_clear(QQmlListProperty<QObject>
//      *property)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu10data_clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *property) {
  QQuickLabsPlatformMenu::data_clear(property);
}

//  qsizetype QQuickLabsPlatformMenu::items_count(QQmlListProperty<QQuickLabs
//      PlatformMenuItem> *property)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuickLabsPlatformMenu11items_countEP16QQmlListPropertyI26QQuickLabsPlatformMenuItemE(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property) {
  return QQuickLabsPlatformMenu::items_count(property);
}

//  QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenu::items_at(QQmlListProp
//      erty<QQuickLabsPlatformMenuItem> *property, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenuItem *ritual_ZN22QQuickLabsPlatformMenu8items_atEP16QQmlListPropertyI26QQuickLabsPlatformMenuItemEx(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *property,
    qsizetype index) {
  return QQuickLabsPlatformMenu::items_at(property, index);
}

//  void QQuickLabsPlatformMenu::updateIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickLabsPlatformMenu10updateIconEv(
    QQuickLabsPlatformMenu *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenu")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateIcon()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateIcon()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  QQuickLabsPlatformMenu as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickLabsPlatformMenu_QQmlParserStatus(
    QQuickLabsPlatformMenu *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickLabsPlatformMenu, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformMenu(
    QQuickLabsPlatformMenu *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformMenu *>(self)->take(key, call);
}

//  void QQuickLabsPlatformMenu::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickLabsPlatformMenu10classBeginEv(
    QQuickLabsPlatformMenu *self) {
  static_cast<OwnQQuickLabsPlatformMenu *>(self)->OwnQQuickLabsPlatformMenu::classBegin();
}

//  a QQmlListProperty<QObject> a ritual of QQuickLabsPlatformMenu gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickLabsPlatformMenu__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QQmlListProperty<QQuickLabsPlatformMenuItem> a ritual of
//      QQuickLabsPlatformMenu gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickLabsPlatformMenu__QQmlListProperty_QQuickLabsPlatformMenuItem(
    QQmlListProperty<QQuickLabsPlatformMenuItem> *self) {
  delete self;
}
