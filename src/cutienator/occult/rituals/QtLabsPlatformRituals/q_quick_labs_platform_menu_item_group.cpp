//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuitemgroup_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuitemgroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtLabsPlatform/private/qquicklabsplatformmenuitemgroup_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenuitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 364, as _ZN26QQuickLabsPlatformMenuItem10setCheckedEb
inline void QQuickLabsPlatformMenuItem::setChecked(bool checked)
{
    if (m_checked == checked)
        return;

    if (checked && !m_checkable)
        setCheckable(true);

    m_checked = checked;
    sync();
    emit checkedChanged();
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 359, as _ZNK26QQuickLabsPlatformMenuItem9isCheckedEv
inline bool QQuickLabsPlatformMenuItem::isChecked() const
{
    return m_checked;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 109, as _ZN31QQuickLabsPlatformMenuItemGroupD1Ev
inline QQuickLabsPlatformMenuItemGroup::~QQuickLabsPlatformMenuItemGroup()
{
    clear();
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 180, as _ZNK31QQuickLabsPlatformMenuItemGroup11isExclusiveEv
inline bool QQuickLabsPlatformMenuItemGroup::isExclusive() const
{
    return m_exclusive;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 202, as _ZNK31QQuickLabsPlatformMenuItemGroup11checkedItemEv
inline QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenuItemGroup::checkedItem() const
{
    return m_checkedItem;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitemgroup.cpp, line 301, as _ZNK31QQuickLabsPlatformMenuItemGroup11findCurrentEv
inline QQuickLabsPlatformMenuItem *QQuickLabsPlatformMenuItemGroup::findCurrent() const
{
    for (QQuickLabsPlatformMenuItem *item : m_items) {
        if (item->isChecked())
            return item;
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  A QQuickLabsPlatformMenuItemGroup that Python can take functions over in. Every QQuickLabsPlatformMenuItemGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuItemGroupCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuItemGroupCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemGroupCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemGroupCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemGroupCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemGroupCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuItemGroupCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformMenuItemGroup : public QQuickLabsPlatformMenuItemGroup {
public:
  using QQuickLabsPlatformMenuItemGroup::QQuickLabsPlatformMenuItemGroup;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall0 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall1 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall2 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall3 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall4 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall5 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuItemGroupCall6 call = reinterpret_cast<CuteQQuickLabsPlatformMenuItemGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformMenuItemGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickLabsPlatformMenuItemGroup10metaObjectEv(
    const QQuickLabsPlatformMenuItemGroup *self) {
  return self->metaObject();
}

//  QQuickLabsPlatformMenuItemGroup::~QQuickLabsPlatformMenuItemGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickLabsPlatformMenuItemGroupD1Ev(
    QQuickLabsPlatformMenuItemGroup *self) {
  delete self;
}

//  bool QQuickLabsPlatformMenuItemGroup::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuickLabsPlatformMenuItemGroup9isEnabledEv(
    const QQuickLabsPlatformMenuItemGroup *self) {
  return self->isEnabled();
}

//  bool QQuickLabsPlatformMenuItemGroup::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuickLabsPlatformMenuItemGroup9isVisibleEv(
    const QQuickLabsPlatformMenuItemGroup *self) {
  return self->isVisible();
}

//  bool QQuickLabsPlatformMenuItemGroup::isExclusive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QQuickLabsPlatformMenuItemGroup11isExclusiveEv(
    const QQuickLabsPlatformMenuItemGroup *self) {
  return self->isExclusive();
}

//  QQuickLabsPlatformMenuItem
//      *QQuickLabsPlatformMenuItemGroup::checkedItem() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenuItem *ritual_ZNK31QQuickLabsPlatformMenuItemGroup11checkedItemEv(
    const QQuickLabsPlatformMenuItemGroup *self) {
  return self->checkedItem();
}

//  QQuickLabsPlatformMenuItem
//      *QQuickLabsPlatformMenuItemGroup::findCurrent() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenuItem *ritual_ZNK31QQuickLabsPlatformMenuItemGroup11findCurrentEv(
    const QQuickLabsPlatformMenuItemGroup *self) {
  return self->findCurrent();
}

//  a Python function taken by a CuteQQuickLabsPlatformMenuItemGroup, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformMenuItemGroup(
    QQuickLabsPlatformMenuItemGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformMenuItemGroup *>(self)->take(key, call);
}
