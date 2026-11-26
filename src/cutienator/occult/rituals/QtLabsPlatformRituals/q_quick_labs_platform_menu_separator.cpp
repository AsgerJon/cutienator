//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuseparator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenuseparator_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 553, as _ZN26QQuickLabsPlatformMenuItem10classBeginEv
inline void QQuickLabsPlatformMenuItem::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 313, as _ZN26QQuickLabsPlatformMenuItem12setSeparatorEb
inline void QQuickLabsPlatformMenuItem::setSeparator(bool separator)
{
    if (m_separator == separator)
        return;

    m_separator = separator;
    sync();
    emit separatorChanged();
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 72, as _ZN26QQuickLabsPlatformMenuItemC2EP7QObject
inline QQuickLabsPlatformMenuItem::QQuickLabsPlatformMenuItem(QObject *parent)
    : QObject(parent),
      m_complete(false),
      m_enabled(true),
      m_visible(true),
      m_separator(false),
      m_checkable(false),
      m_checked(false),
      m_role(QPlatformMenuItem::TextHeuristicRole),
      m_menu(nullptr),
      m_subMenu(nullptr),
      m_group(nullptr),
      m_iconLoader(nullptr),
      m_handle(nullptr)
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenuitem.cpp, line 89, as _ZN26QQuickLabsPlatformMenuItemD2Ev
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
//  -----------------------------------------------------------------------

//  A QQuickLabsPlatformMenuSeparator that Python can take functions over in. Every QQuickLabsPlatformMenuSeparator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall0)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuSeparatorCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuSeparatorCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuSeparatorCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformMenuSeparator : public QQuickLabsPlatformMenuSeparator {
public:
  using QQuickLabsPlatformMenuSeparator::QQuickLabsPlatformMenuSeparator;
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
      CuteQQuickLabsPlatformMenuSeparatorCall0 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenuItem::classBegin();
  }

  //  void QQuickLabsPlatformMenuItem::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuSeparatorCall1 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall1>(taken[1]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall2 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall2>(taken[2]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall3 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall3>(taken[3]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall4 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall4>(taken[4]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall5 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall5>(taken[5]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall6 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall6>(taken[6]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall7 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall7>(taken[7]);
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
      CuteQQuickLabsPlatformMenuSeparatorCall8 call = reinterpret_cast<CuteQQuickLabsPlatformMenuSeparatorCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformMenuSeparator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuickLabsPlatformMenuSeparator10metaObjectEv(
    const QQuickLabsPlatformMenuSeparator *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformMenuSeparator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QQuickLabsPlatformMenuSeparator11qt_metacastEPKc(
    QQuickLabsPlatformMenuSeparator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformMenuSeparator::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QQuickLabsPlatformMenuSeparator11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformMenuSeparator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  a Python function taken by a CuteQQuickLabsPlatformMenuSeparator, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformMenuSeparator(
    QQuickLabsPlatformMenuSeparator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformMenuSeparator *>(self)->take(key, call);
}
