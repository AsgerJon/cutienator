//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
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
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/qqml.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenuitemgroup_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 569, as _ZN22QQuickLabsPlatformMenu10removeItemEP26QQuickLabsPlatformMenuItem
inline void QQuickLabsPlatformMenu::removeItem(QQuickLabsPlatformMenuItem *item)
{
    if (!item || !m_items.removeOne(item))
        return;

    m_data.removeOne(item);
    if (m_handle)
        m_handle->removeMenuItem(item->handle());
    item->setMenu(nullptr);
    sync();
    emit itemsChanged();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 553, as _ZN26QQuickLabsPlatformMenuItem10classBeginEv
inline void QQuickLabsPlatformMenuItem::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 233, as _ZN22QQuickLabsPlatformMenu4syncEv
inline void QQuickLabsPlatformMenu::sync()
{
    if (!m_complete || !create())
        return;

    m_handle->setText(m_title);
    m_handle->setEnabled(m_enabled);
    m_handle->setVisible(m_visible);
    m_handle->setMinimumWidth(m_minimumWidth);
    m_handle->setMenuType(m_type);
    m_handle->setFont(m_font);

    if (m_menuBar && m_menuBar->handle())
        m_menuBar->handle()->syncMenu(m_handle);
#if QT_CONFIG(systemtrayicon)
    else if (m_systemTrayIcon && m_systemTrayIcon->handle())
        m_systemTrayIcon->handle()->updateMenu(m_handle);
#endif

    for (QQuickLabsPlatformMenuItem *item : std::as_const(m_items))
        item->sync();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 175, as _ZNK22QQuickLabsPlatformMenu6handleEv
inline QPlatformMenu *QQuickLabsPlatformMenu::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 33, as _ZNK28QQuickLabsPlatformIconLoader7toQIconEv
inline QIcon QQuickLabsPlatformIconLoader::toQIcon() const
{
    QIcon fallback = QPixmap::fromImage(image());
    QIcon icon = QIcon::fromTheme(m_icon.name(), fallback);
    icon.setIsMask(m_icon.isMask());
    return icon;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 180, as _ZNK31QQuickLabsPlatformMenuItemGroup11isExclusiveEv
inline bool QQuickLabsPlatformMenuItemGroup::isExclusive() const
{
    return m_exclusive;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 122, as _ZNK31QQuickLabsPlatformMenuItemGroup9isEnabledEv
inline bool QQuickLabsPlatformMenuItemGroup::isEnabled() const
{
    return m_enabled;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 151, as _ZNK31QQuickLabsPlatformMenuItemGroup9isVisibleEv
inline bool QQuickLabsPlatformMenuItemGroup::isVisible() const
{
    return m_visible;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 41, as _ZNK28QQuickLabsPlatformIconLoader4iconEv
inline QQuickLabsPlatformIcon QQuickLabsPlatformIconLoader::icon() const
{
    return m_icon;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 557, as _ZN26QQuickLabsPlatformMenuItem17componentCompleteEv
inline void QQuickLabsPlatformMenuItem::componentComplete()
{
    if (m_iconLoader)
        m_iconLoader->setEnabled(true);
    m_complete = true;
    sync();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 459, as _ZN26QQuickLabsPlatformMenuItem5eventEP6QEvent
inline bool QQuickLabsPlatformMenuItem::event(QEvent *e)
{
#if QT_CONFIG(shortcut)
    if (e->type() == QEvent::Shortcut) {
        QShortcutEvent *se = static_cast<QShortcutEvent *>(e);
        if (se->shortcutId() == m_shortcutId) {
            activate();
            return true;
        }
    }
#endif
    return QObject::event(e);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 576, as _ZN26QQuickLabsPlatformMenuItem8activateEv
inline void QQuickLabsPlatformMenuItem::activate()
{
    toggle();
    emit triggered();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 547, as _ZN26QQuickLabsPlatformMenuItem6toggleEv
inline void QQuickLabsPlatformMenuItem::toggle()
{
    if (m_checkable)
        setChecked(!m_checked);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 89, as _ZN26QQuickLabsPlatformMenuItemD1Ev
inline QQuickLabsPlatformMenuItem::~QQuickLabsPlatformMenuItem()
{
    if (m_menu)
        m_menu->removeItem(this);
    if (m_group)
        m_group->removeItem(this);
    removeShortcut();
    delete m_iconLoader;
    m_iconLoader = nullptr;
    delete m_handle;
    m_handle = nullptr;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 102, as _ZNK26QQuickLabsPlatformMenuItem6handleEv
inline QPlatformMenuItem *QQuickLabsPlatformMenuItem::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 175, as _ZNK26QQuickLabsPlatformMenuItem4menuEv
inline QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::menu() const
{
    return m_menu;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 196, as _ZNK26QQuickLabsPlatformMenuItem7subMenuEv
inline QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::subMenu() const
{
    return m_subMenu;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 217, as _ZNK26QQuickLabsPlatformMenuItem5groupEv
inline QQuickLabsPlatformMenuItemGroup *QQuickLabsPlatformMenuItem::group() const
{
    return m_group;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 254, as _ZNK26QQuickLabsPlatformMenuItem9isEnabledEv
inline bool QQuickLabsPlatformMenuItem::isEnabled() const
{
    return m_enabled && (!m_group || m_group->isEnabled());
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 283, as _ZNK26QQuickLabsPlatformMenuItem9isVisibleEv
inline bool QQuickLabsPlatformMenuItem::isVisible() const
{
    return m_visible && (!m_group || m_group->isVisible());
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 308, as _ZNK26QQuickLabsPlatformMenuItem11isSeparatorEv
inline bool QQuickLabsPlatformMenuItem::isSeparator() const
{
    return m_separator;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 336, as _ZNK26QQuickLabsPlatformMenuItem11isCheckableEv
inline bool QQuickLabsPlatformMenuItem::isCheckable() const
{
    return m_checkable;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 359, as _ZNK26QQuickLabsPlatformMenuItem9isCheckedEv
inline bool QQuickLabsPlatformMenuItem::isChecked() const
{
    return m_checked;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 400, as _ZNK26QQuickLabsPlatformMenuItem4roleEv
inline QPlatformMenuItem::MenuRole QQuickLabsPlatformMenuItem::role() const
{
    return m_role;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 420, as _ZNK26QQuickLabsPlatformMenuItem4textEv
inline QString QQuickLabsPlatformMenuItem::text() const
{
    return m_text;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 454, as _ZNK26QQuickLabsPlatformMenuItem8shortcutEv
inline QVariant QQuickLabsPlatformMenuItem::shortcut() const
{
    return m_shortcut;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 492, as _ZNK26QQuickLabsPlatformMenuItem4fontEv
inline QFont QQuickLabsPlatformMenuItem::font() const
{
    return m_font;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 525, as _ZNK26QQuickLabsPlatformMenuItem4iconEv
inline QQuickLabsPlatformIcon QQuickLabsPlatformMenuItem::icon() const
{
    if (!m_iconLoader)
        return QQuickLabsPlatformIcon();

    return m_iconLoader->icon();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 587, as _ZN26QQuickLabsPlatformMenuItem11addShortcutEv
inline void QQuickLabsPlatformMenuItem::addShortcut()
{
#if QT_CONFIG(shortcut)
    QKeySequence sequence;
    if (m_shortcut.metaType().id() == QMetaType::Int)
        sequence = QKeySequence(static_cast<QKeySequence::StandardKey>(m_shortcut.toInt()));
    else if (m_shortcut.metaType().id() == QMetaType::QKeySequence)
        sequence = m_shortcut.value<QKeySequence>();
    else
        sequence = QKeySequence::fromString(m_shortcut.toString());
    if (!sequence.isEmpty() && m_enabled) {
        m_shortcutId = QGuiApplicationPrivate::instance()->shortcutMap.addShortcut(this, sequence,
            Qt::WindowShortcut, QQuickShortcutContext::matcher);
    } else {
        m_shortcutId = -1;
    }
#endif
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 606, as _ZN26QQuickLabsPlatformMenuItem14removeShortcutEv
inline void QQuickLabsPlatformMenuItem::removeShortcut()
{
#if QT_CONFIG(shortcut)
    if (m_shortcutId == -1)
        return;

    QKeySequence sequence;
    if (m_shortcut.metaType().id() == QMetaType::Int)
        sequence = QKeySequence(static_cast<QKeySequence::StandardKey>(m_shortcut.toInt()));
    else if (m_shortcut.metaType().id() == QMetaType::QKeySequence)
        sequence = m_shortcut.value<QKeySequence>();
    else
        sequence = QKeySequence::fromString(m_shortcut.toString());
    QGuiApplicationPrivate::instance()->shortcutMap.removeShortcut(m_shortcutId, this, sequence);
#endif
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformMenuItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformMenuItem : QQuickLabsPlatformMenuItem {
  using QQuickLabsPlatformMenuItem::classBegin;
};

//  A QQuickLabsPlatformMenuItem that Python can take functions over in. Every QQuickLabsPlatformMenuItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLabsPlatformMenuItemCall0)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformMenuItemCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuItemCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuItemCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformMenuItem : public QQuickLabsPlatformMenuItem {
public:
  using QQuickLabsPlatformMenuItem::QQuickLabsPlatformMenuItem;
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

  //  void QQuickLabsPlatformMenuItem::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemCall0 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenuItem::classBegin();
  }

  //  void QQuickLabsPlatformMenuItem::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemCall1 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenuItem::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickLabsPlatformMenuItem::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemCall2 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickLabsPlatformMenuItem::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemCall3 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall3>(taken[3]);
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
      CuteQQuickLabsPlatformMenuItemCall4 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall4>(taken[4]);
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
      CuteQQuickLabsPlatformMenuItemCall5 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall5>(taken[5]);
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
      CuteQQuickLabsPlatformMenuItemCall6 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall6>(taken[6]);
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
      CuteQQuickLabsPlatformMenuItemCall7 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall7>(taken[7]);
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
      CuteQQuickLabsPlatformMenuItemCall8 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformMenuItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QQuickLabsPlatformMenuItem10metaObjectEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformMenuItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QQuickLabsPlatformMenuItem11qt_metacastEPKc(
    QQuickLabsPlatformMenuItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformMenuItem::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QQuickLabsPlatformMenuItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformMenuItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QMetaObject *QQuickLabsPlatformMenuItem::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN26QQuickLabsPlatformMenuItem20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformMenuItem::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformMenuItem::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformMenuItem *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickLabsPlatformMenuItem::~QQuickLabsPlatformMenuItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItemD1Ev(
    QQuickLabsPlatformMenuItem *self) {
  delete self;
}

//  QPlatformMenuItem *QQuickLabsPlatformMenuItem::handle() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK26QQuickLabsPlatformMenuItem6handleEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->handle();
}

//  QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::menu() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenu *ritual_ZNK26QQuickLabsPlatformMenuItem4menuEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->menu();
}

//  QQuickLabsPlatformMenu *QQuickLabsPlatformMenuItem::subMenu() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenu *ritual_ZNK26QQuickLabsPlatformMenuItem7subMenuEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->subMenu();
}

//  QQuickLabsPlatformMenuItemGroup *QQuickLabsPlatformMenuItem::group()
//      const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenuItemGroup *ritual_ZNK26QQuickLabsPlatformMenuItem5groupEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->group();
}

//  bool QQuickLabsPlatformMenuItem::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickLabsPlatformMenuItem9isEnabledEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->isEnabled();
}

//  bool QQuickLabsPlatformMenuItem::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickLabsPlatformMenuItem9isVisibleEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->isVisible();
}

//  bool QQuickLabsPlatformMenuItem::isSeparator() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickLabsPlatformMenuItem11isSeparatorEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->isSeparator();
}

//  bool QQuickLabsPlatformMenuItem::isCheckable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickLabsPlatformMenuItem11isCheckableEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->isCheckable();
}

//  bool QQuickLabsPlatformMenuItem::isChecked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickLabsPlatformMenuItem9isCheckedEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->isChecked();
}

//  QPlatformMenuItem::MenuRole QQuickLabsPlatformMenuItem::role() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem::MenuRole ritual_ZNK26QQuickLabsPlatformMenuItem4roleEv(
    const QQuickLabsPlatformMenuItem *self) {
  return self->role();
}

//  QString QQuickLabsPlatformMenuItem::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QQuickLabsPlatformMenuItem4textEv(
    const QQuickLabsPlatformMenuItem *self) {
  return new QString(self->text());
}

//  QVariant QQuickLabsPlatformMenuItem::shortcut() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK26QQuickLabsPlatformMenuItem8shortcutEv(
    const QQuickLabsPlatformMenuItem *self) {
  return new QVariant(self->shortcut());
}

//  QFont QQuickLabsPlatformMenuItem::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK26QQuickLabsPlatformMenuItem4fontEv(
    const QQuickLabsPlatformMenuItem *self) {
  return new QFont(self->font());
}

//  QQuickLabsPlatformIcon QQuickLabsPlatformMenuItem::icon() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformIcon *ritual_ZNK26QQuickLabsPlatformMenuItem4iconEv(
    const QQuickLabsPlatformMenuItem *self) {
  return new QQuickLabsPlatformIcon(self->icon());
}

//  void QQuickLabsPlatformMenuItem::toggle()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem6toggleEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "toggle()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "toggle()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::triggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem9triggeredEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "triggered()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "triggered()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::hovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem7hoveredEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "hovered()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "hovered()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::menuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem11menuChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "menuChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "menuChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::subMenuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem14subMenuChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "subMenuChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "subMenuChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::groupChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem12groupChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "groupChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "groupChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::enabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem14enabledChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
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

//  void QQuickLabsPlatformMenuItem::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem14visibleChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
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

//  void QQuickLabsPlatformMenuItem::separatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem16separatorChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "separatorChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "separatorChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::checkableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem16checkableChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkableChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkableChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::checkedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem14checkedChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "checkedChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "checkedChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::roleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem11roleChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "roleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "roleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem11textChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::shortcutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem15shortcutChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shortcutChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shortcutChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::fontChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem11fontChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
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

//  void QQuickLabsPlatformMenuItem::iconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem11iconChangedEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
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

//  void QQuickLabsPlatformMenuItem::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem10classBeginEv(
    QQuickLabsPlatformMenuItem *self) {
  self->classBegin();
}

//  void QQuickLabsPlatformMenuItem::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem17componentCompleteEv(
    QQuickLabsPlatformMenuItem *self) {
  self->componentComplete();
}

//  bool QQuickLabsPlatformMenuItem::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickLabsPlatformMenuItem5eventEP6QEvent(
    QQuickLabsPlatformMenuItem *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickLabsPlatformMenuItem::activate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem8activateEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformMenuItem::updateIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem10updateIconEv(
    QQuickLabsPlatformMenuItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformMenuItem")) {
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

//  void QQuickLabsPlatformMenuItem::addShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem11addShortcutEv(
    QQuickLabsPlatformMenuItem *self) {
  self->addShortcut();
}

//  void QQuickLabsPlatformMenuItem::removeShortcut()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickLabsPlatformMenuItem14removeShortcutEv(
    QQuickLabsPlatformMenuItem *self) {
  self->removeShortcut();
}

//  QQuickLabsPlatformMenuItem as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickLabsPlatformMenuItem_QQmlParserStatus(
    QQuickLabsPlatformMenuItem *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickLabsPlatformMenuItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformMenuItem(
    QQuickLabsPlatformMenuItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformMenuItem *>(self)->take(key, call);
}

//  void QQuickLabsPlatformMenuItem::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QQuickLabsPlatformMenuItem10classBeginEv(
    QQuickLabsPlatformMenuItem *self) {
  static_cast<OwnQQuickLabsPlatformMenuItem *>(self)->OwnQQuickLabsPlatformMenuItem::classBegin();
}
