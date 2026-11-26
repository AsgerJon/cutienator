//  Written by dev_tooling.RitualGenerator from the records of QtLabsPlatform
//  /6.12.0/QtLabsPlatform/private/qquicklabsplatformsystemtrayicon_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemtrayicon)
#if QT_CONFIG(systemtrayicon)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformsystemtrayicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtCore/qobject.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/qqml.h>
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
#include <QtLabsPlatform/private/qquicklabsplatformsystemtrayicon_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformmenu_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformiconloader_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtLabsPlatform/private/qquicklabsplatformicon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 26, as _ZN28QQuickLabsPlatformIconLoader10setEnabledEb
inline void QQuickLabsPlatformIconLoader::setEnabled(bool enabled)
{
    m_enabled = enabled;
    if (m_enabled)
        loadIcon();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 338, as _ZN22QQuickLabsPlatformMenu17setSystemTrayIconEP32QQuickLabsPlatformSystemTrayIcon
#if QT_CONFIG(systemtrayicon)
inline void QQuickLabsPlatformMenu::setSystemTrayIcon(QQuickLabsPlatformSystemTrayIcon *icon)
{
    if (m_systemTrayIcon == icon)
        return;

    m_systemTrayIcon = icon;
    destroy();
    emit systemTrayIconChanged();
}
#endif  // QT_CONFIG(systemtrayicon)

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 41, as _ZNK28QQuickLabsPlatformIconLoader4iconEv
inline QQuickLabsPlatformIcon QQuickLabsPlatformIconLoader::icon() const
{
    return m_icon;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 46, as _ZN28QQuickLabsPlatformIconLoader7setIconERK22QQuickLabsPlatformIcon
inline void QQuickLabsPlatformIconLoader::setIcon(const QQuickLabsPlatformIcon& icon)
{
    m_icon = icon;
    if (m_enabled)
        loadIcon();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 13, as _ZN28QQuickLabsPlatformIconLoaderC1EiP7QObject
inline QQuickLabsPlatformIconLoader::QQuickLabsPlatformIconLoader(int slot, QObject *parent)
    : m_parent(parent),
      m_slot(slot),
      m_enabled(false)
{
    Q_ASSERT(slot != -1 && parent);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformmenu.cpp, line 175, as _ZNK22QQuickLabsPlatformMenu6handleEv
inline QPlatformMenu *QQuickLabsPlatformMenu::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 379, as _ZN32QQuickLabsPlatformSystemTrayIcon10classBeginEv
inline void QQuickLabsPlatformSystemTrayIcon::classBegin()
{
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 383, as _ZN32QQuickLabsPlatformSystemTrayIcon17componentCompleteEv
inline void QQuickLabsPlatformSystemTrayIcon::componentComplete()
{
    m_complete = true;
    if (m_visible)
        init();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformiconloader.cpp, line 53, as _ZN28QQuickLabsPlatformIconLoader8loadIconEv
inline void QQuickLabsPlatformIconLoader::loadIcon()
{
    if (m_icon.source().isEmpty()) {
        clear(m_parent);
    } else {
        load(qmlEngine(m_parent), m_icon.source());
        if (m_slot != -1 && isLoading()) {
            connectFinished(m_parent, m_slot);
            m_slot = -1;
        }
    }

    if (!isLoading())
        m_parent->metaObject()->method(m_slot).invoke(m_parent);
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformicon.cpp, line 9, as _ZNK22QQuickLabsPlatformIcon6sourceEv
inline QUrl QQuickLabsPlatformIcon::source() const
{
    return m_source;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 155, as _ZN32QQuickLabsPlatformSystemTrayIconD1Ev
inline QQuickLabsPlatformSystemTrayIcon::~QQuickLabsPlatformSystemTrayIcon()
{
    if (m_menu)
        m_menu->setSystemTrayIcon(nullptr);
    cleanup();
    delete m_iconLoader;
    m_iconLoader = nullptr;
    delete m_handle;
    m_handle = nullptr;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 166, as _ZNK32QQuickLabsPlatformSystemTrayIcon6handleEv
inline QPlatformSystemTrayIcon *QQuickLabsPlatformSystemTrayIcon::handle() const
{
    return m_handle;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 177, as _ZNK32QQuickLabsPlatformSystemTrayIcon11isAvailableEv
inline bool QQuickLabsPlatformSystemTrayIcon::isAvailable() const
{
    return m_handle && m_handle->isSystemTrayAvailable();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 190, as _ZNK32QQuickLabsPlatformSystemTrayIcon16supportsMessagesEv
inline bool QQuickLabsPlatformSystemTrayIcon::supportsMessages() const
{
    return m_handle && m_handle->supportsMessages();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 202, as _ZNK32QQuickLabsPlatformSystemTrayIcon9isVisibleEv
inline bool QQuickLabsPlatformSystemTrayIcon::isVisible() const
{
    return m_visible;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 228, as _ZNK32QQuickLabsPlatformSystemTrayIcon7tooltipEv
inline QString QQuickLabsPlatformSystemTrayIcon::tooltip() const
{
    return m_tooltip;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 250, as _ZNK32QQuickLabsPlatformSystemTrayIcon4menuEv
inline QQuickLabsPlatformMenu *QQuickLabsPlatformSystemTrayIcon::menu() const
{
    return m_menu;
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 283, as _ZNK32QQuickLabsPlatformSystemTrayIcon8geometryEv
inline QRect QQuickLabsPlatformSystemTrayIcon::geometry() const
{
    return m_handle ? m_handle->geometry() : QRect();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 303, as _ZNK32QQuickLabsPlatformSystemTrayIcon4iconEv
inline QQuickLabsPlatformIcon QQuickLabsPlatformSystemTrayIcon::icon() const
{
    if (!m_iconLoader)
        return QQuickLabsPlatformIcon();

    return m_iconLoader->icon();
}

//  from ../qtdeclarative/src/labs/platform/qquicklabsplatformsystemtrayicon.cpp, line 371, as _ZN32QQuickLabsPlatformSystemTrayIcon7cleanupEv
inline void QQuickLabsPlatformSystemTrayIcon::cleanup()
{
    if (m_handle)
        m_handle->cleanup();
    if (m_iconLoader)
        m_iconLoader->setEnabled(false);
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLabsPlatformSystemTrayIcon may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLabsPlatformSystemTrayIcon : QQuickLabsPlatformSystemTrayIcon {
  using QQuickLabsPlatformSystemTrayIcon::classBegin;
};

//  A QQuickLabsPlatformSystemTrayIcon that Python can take functions over in. Every QQuickLabsPlatformSystemTrayIcon
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall0)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#if QT_CONFIG(systemtrayicon)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall1)(const void *, int *);
#endif  // QT_CONFIG(systemtrayicon)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformSystemTrayIconCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickLabsPlatformSystemTrayIconCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickLabsPlatformSystemTrayIconCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickLabsPlatformSystemTrayIcon : public QQuickLabsPlatformSystemTrayIcon {
public:
  using QQuickLabsPlatformSystemTrayIcon::QQuickLabsPlatformSystemTrayIcon;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
#if QT_CONFIG(systemtrayicon)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(systemtrayicon)
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

#if QT_CONFIG(systemtrayicon)
  //  void QQuickLabsPlatformSystemTrayIcon::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabsPlatformSystemTrayIconCall0 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformSystemTrayIcon::classBegin();
  }
#endif  // QT_CONFIG(systemtrayicon)

#if QT_CONFIG(systemtrayicon)
  //  void QQuickLabsPlatformSystemTrayIcon::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabsPlatformSystemTrayIconCall1 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickLabsPlatformSystemTrayIcon::componentComplete();
  }
#endif  // QT_CONFIG(systemtrayicon)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabsPlatformSystemTrayIconCall2 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall2>(taken[2]);
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
      CuteQQuickLabsPlatformSystemTrayIconCall3 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall3>(taken[3]);
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
      CuteQQuickLabsPlatformSystemTrayIconCall4 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall4>(taken[4]);
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
      CuteQQuickLabsPlatformSystemTrayIconCall5 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall5>(taken[5]);
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
      CuteQQuickLabsPlatformSystemTrayIconCall6 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall6>(taken[6]);
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
      CuteQQuickLabsPlatformSystemTrayIconCall7 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall7>(taken[7]);
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
      CuteQQuickLabsPlatformSystemTrayIconCall8 call = reinterpret_cast<CuteQQuickLabsPlatformSystemTrayIconCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickLabsPlatformSystemTrayIcon::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QQuickLabsPlatformSystemTrayIcon10metaObjectEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return self->metaObject();
}

//  void *QQuickLabsPlatformSystemTrayIcon::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN32QQuickLabsPlatformSystemTrayIcon11qt_metacastEPKc(
    QQuickLabsPlatformSystemTrayIcon *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickLabsPlatformSystemTrayIcon::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN32QQuickLabsPlatformSystemTrayIcon11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickLabsPlatformSystemTrayIcon *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  const QMetaObject
//      *QQuickLabsPlatformSystemTrayIcon::qmlExtendedNamespace()
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZN32QQuickLabsPlatformSystemTrayIcon20qmlExtendedNamespaceEv() {
  return QQuickLabsPlatformSystemTrayIcon::qmlExtendedNamespace();
}

//  void QQuickLabsPlatformSystemTrayIcon::qt_qmlMarker_extendedNamespace()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon30qt_qmlMarker_extendedNamespaceEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  self->qt_qmlMarker_extendedNamespace();
}

//  QQuickLabsPlatformSystemTrayIcon::~QQuickLabsPlatformSystemTrayIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIconD1Ev(
    QQuickLabsPlatformSystemTrayIcon *self) {
  delete self;
}

//  QPlatformSystemTrayIcon *QQuickLabsPlatformSystemTrayIcon::handle() const
extern "C" Q_DECL_EXPORT
QPlatformSystemTrayIcon *ritual_ZNK32QQuickLabsPlatformSystemTrayIcon6handleEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return self->handle();
}

//  bool QQuickLabsPlatformSystemTrayIcon::isAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickLabsPlatformSystemTrayIcon11isAvailableEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return self->isAvailable();
}

//  bool QQuickLabsPlatformSystemTrayIcon::supportsMessages() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickLabsPlatformSystemTrayIcon16supportsMessagesEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return self->supportsMessages();
}

//  bool QQuickLabsPlatformSystemTrayIcon::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickLabsPlatformSystemTrayIcon9isVisibleEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return self->isVisible();
}

//  QString QQuickLabsPlatformSystemTrayIcon::tooltip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK32QQuickLabsPlatformSystemTrayIcon7tooltipEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return new QString(self->tooltip());
}

//  QQuickLabsPlatformMenu *QQuickLabsPlatformSystemTrayIcon::menu() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformMenu *ritual_ZNK32QQuickLabsPlatformSystemTrayIcon4menuEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return self->menu();
}

//  QRect QQuickLabsPlatformSystemTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK32QQuickLabsPlatformSystemTrayIcon8geometryEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return new QRect(self->geometry());
}

//  QQuickLabsPlatformIcon QQuickLabsPlatformSystemTrayIcon::icon() const
extern "C" Q_DECL_EXPORT
QQuickLabsPlatformIcon *ritual_ZNK32QQuickLabsPlatformSystemTrayIcon4iconEv(
    const QQuickLabsPlatformSystemTrayIcon *self) {
  return new QQuickLabsPlatformIcon(self->icon());
}

//  void QQuickLabsPlatformSystemTrayIcon::show()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon4showEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "show()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "show()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::hide()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon4hideEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "hide()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "hide()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::showMessage(const QString &title,
//      const QString &message, QPlatformSystemTrayIcon::MessageIcon
//      iconType, int msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon11showMessageERK7QStringS2_N23QPlatformSystemTrayIcon11MessageIconEi(
    QQuickLabsPlatformSystemTrayIcon *self,
    const QString *title,
    const QString *message,
    QPlatformSystemTrayIcon::MessageIcon iconType,
    int msecs) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "showMessage(const QString &,const QString &,QPlatformSystemTrayIcon::MessageIcon,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "showMessage(const QString &,const QString &,QPlatformSystemTrayIcon::MessageIcon,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(title)),
      const_cast<void *>(static_cast<const void *>(message)),
      const_cast<void *>(static_cast<const void *>(&iconType)),
      const_cast<void *>(static_cast<const void *>(&msecs)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::activated(QPlatformSystemTrayIcon:
//      :ActivationReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon9activatedEN23QPlatformSystemTrayIcon16ActivationReasonE(
    QQuickLabsPlatformSystemTrayIcon *self,
    QPlatformSystemTrayIcon::ActivationReason reason) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "activated(QPlatformSystemTrayIcon::ActivationReason)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "activated(QPlatformSystemTrayIcon::ActivationReason)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&reason)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::messageClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon14messageClickedEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "messageClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "messageClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::visibleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon14visibleChangedEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
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

//  void QQuickLabsPlatformSystemTrayIcon::tooltipChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon14tooltipChangedEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "tooltipChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "tooltipChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::menuChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon11menuChangedEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
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

//  void QQuickLabsPlatformSystemTrayIcon::geometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon15geometryChangedEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "geometryChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "geometryChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickLabsPlatformSystemTrayIcon::iconChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon11iconChangedEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
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

//  void QQuickLabsPlatformSystemTrayIcon::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon7cleanupEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  self->cleanup();
}

//  void QQuickLabsPlatformSystemTrayIcon::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon10classBeginEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  self->classBegin();
}

//  void QQuickLabsPlatformSystemTrayIcon::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon17componentCompleteEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  self->componentComplete();
}

//  void QQuickLabsPlatformSystemTrayIcon::updateIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickLabsPlatformSystemTrayIcon10updateIconEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickLabsPlatformSystemTrayIcon")) {
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

//  QQuickLabsPlatformSystemTrayIcon as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QQuickLabsPlatformSystemTrayIcon_QQmlParserStatus(
    QQuickLabsPlatformSystemTrayIcon *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  a Python function taken by a CuteQQuickLabsPlatformSystemTrayIcon, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabsPlatformSystemTrayIcon(
    QQuickLabsPlatformSystemTrayIcon *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabsPlatformSystemTrayIcon *>(self)->take(key, call);
}

//  void QQuickLabsPlatformSystemTrayIcon::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN32QQuickLabsPlatformSystemTrayIcon10classBeginEv(
    QQuickLabsPlatformSystemTrayIcon *self) {
  static_cast<OwnQQuickLabsPlatformSystemTrayIcon *>(self)->OwnQQuickLabsPlatformSystemTrayIcon::classBegin();
}

#endif  // QT_CONFIG(systemtrayicon)
#endif  // QT_CONFIG(systemtrayicon)
