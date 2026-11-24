//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformmenubar_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformmenubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicklabsplatformmenu_p.h"
#include "qquicklabsplatformmenubar_p.h"
#include "qquicklabsplatformmenuitem_p.h"
#include "qquicklabsplatformiconloader_p.h"
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
#include "qquicklabsplatformsystemtrayicon_p.h"
#endif
#include "qquicklabsplatformmenubar_p.h"
#include "qquicklabsplatformmenu_p.h"
#include <QtCore/qloggingcategory.h>
#include <QtGui/qpa/qplatformmenu.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickitem.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 293, as _ZN22QQuickLabsPlatformMenu10setMenuBarEP25QQuickLabsPlatformMenuBar
inline void QQuickLabsPlatformMenu::setMenuBar(QQuickLabsPlatformMenuBar *menuBar)
{
    if (m_menuBar == menuBar)
        return;

    m_menuBar = menuBar;
    destroy();
    emit menuBarChanged();
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

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 85, as _ZN25QQuickLabsPlatformMenuBarD1Ev
inline QQuickLabsPlatformMenuBar::~QQuickLabsPlatformMenuBar()
{
    for (QQuickLabsPlatformMenu *menu : std::as_const(m_menus))
        menu->setMenuBar(nullptr);
    delete m_handle;
    m_handle = nullptr;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 93, as _ZNK25QQuickLabsPlatformMenuBar6handleEv
inline QPlatformMenuBar *QQuickLabsPlatformMenuBar::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 132, as _ZNK25QQuickLabsPlatformMenuBar6windowEv
inline QWindow *QQuickLabsPlatformMenuBar::window() const
{
    return m_window;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 218, as _ZN25QQuickLabsPlatformMenuBar10classBeginEv
inline void QQuickLabsPlatformMenuBar::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 222, as _ZN25QQuickLabsPlatformMenuBar17componentCompleteEv
inline void QQuickLabsPlatformMenuBar::componentComplete()
{
    m_complete = true;
    for (QQuickLabsPlatformMenu *menu : std::as_const(m_menus))
        menu->sync();
    if (!m_window)
        setWindow(findWindow());
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenubar.cpp, line 231, as _ZNK25QQuickLabsPlatformMenuBar10findWindowEv
inline QWindow *QQuickLabsPlatformMenuBar::findWindow() const
{
    QObject *obj = parent();
    while (obj) {
        QWindow *window = qobject_cast<QWindow *>(obj);
        if (window)
            return window;
        QQuickItem *item = qobject_cast<QQuickItem *>(obj);
        if (item && item->window())
            return item->window();
        obj = obj->parent();
    }
    return nullptr;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformMenuBar may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformMenuBar : QQuickLabsPlatformMenuBar {
  using QQuickLabsPlatformMenuBar::classBegin;
};

//  A QQuickLabsPlatformMenuBar that Python can take functions over in. Every QQuickLabsPlatformMenuBar
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLabsPlatformMenuBarCall0)(const void *, int *);
typedef void (*CuteQQuickLabsPlatformMenuBarCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuBarCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformMenuBarCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuBarCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuBarCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuBarCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuBarCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformMenuBarCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformMenuBar : public QQuickLabsPlatformMenuBar {
public:
  using QQuickLabsPlatformMenuBar::QQuickLabsPlatformMenuBar;
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

  //  void QQuickLabsPlatformMenuBar::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuBarCall0 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenuBar::classBegin();
  }

  //  void QQuickLabsPlatformMenuBar::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuBarCall1 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformMenuBar::componentComplete();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabsPlatformMenuBarCall2 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall2>(taken[2]);
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
      CuteQQuickLabsPlatformMenuBarCall3 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall3>(taken[3]);
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
      CuteQQuickLabsPlatformMenuBarCall4 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall4>(taken[4]);
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
      CuteQQuickLabsPlatformMenuBarCall5 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall5>(taken[5]);
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
      CuteQQuickLabsPlatformMenuBarCall6 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall6>(taken[6]);
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
      CuteQQuickLabsPlatformMenuBarCall7 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall7>(taken[7]);
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
      CuteQQuickLabsPlatformMenuBarCall8 call = reinterpret_cast<CuteQQuickLabsPlatformMenuBarCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformMenuBar::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickLabsPlatformMenuBar10metaObjectEv(
    const QQuickLabsPlatformMenuBar *self) {
  return self->metaObject();
}

//  QQuickLabsPlatformMenuBar::~QQuickLabsPlatformMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickLabsPlatformMenuBarD1Ev(
    QQuickLabsPlatformMenuBar *self) {
  delete self;
}

//  QPlatformMenuBar *QQuickLabsPlatformMenuBar::handle() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_ZNK25QQuickLabsPlatformMenuBar6handleEv(
    const QQuickLabsPlatformMenuBar *self) {
  return self->handle();
}

//  QWindow *QQuickLabsPlatformMenuBar::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK25QQuickLabsPlatformMenuBar6windowEv(
    const QQuickLabsPlatformMenuBar *self) {
  return self->window();
}

//  void QQuickLabsPlatformMenuBar::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickLabsPlatformMenuBar10classBeginEv(
    QQuickLabsPlatformMenuBar *self) {
  self->classBegin();
}

//  void QQuickLabsPlatformMenuBar::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickLabsPlatformMenuBar17componentCompleteEv(
    QQuickLabsPlatformMenuBar *self) {
  self->componentComplete();
}

//  QWindow *QQuickLabsPlatformMenuBar::findWindow() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK25QQuickLabsPlatformMenuBar10findWindowEv(
    const QQuickLabsPlatformMenuBar *self) {
  return self->findWindow();
}

//  QQuickLabsPlatformMenuBar as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickLabsPlatformMenuBar_QQmlParserStatus(
    QQuickLabsPlatformMenuBar *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickLabsPlatformMenuBar, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformMenuBar(
    QQuickLabsPlatformMenuBar *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformMenuBar *>(self)->take(key, call);
}

//  void QQuickLabsPlatformMenuBar::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QQuickLabsPlatformMenuBar10classBeginEv(
    QQuickLabsPlatformMenuBar *self) {
  static_cast<OwnQQuickLabsPlatformMenuBar *>(self)->OwnQQuickLabsPlatformMenuBar::classBegin();
}
