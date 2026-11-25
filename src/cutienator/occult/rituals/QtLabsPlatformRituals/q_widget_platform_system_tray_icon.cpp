//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformsystemtrayicon_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemtrayicon)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformsystemtrayicon_p.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>

//  const QMetaObject *QWidgetPlatformSystemTrayIcon::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QWidgetPlatformSystemTrayIcon10metaObjectEv(
    const QWidgetPlatformSystemTrayIcon *self) {
  return self->metaObject();
}

//  QWidgetPlatformSystemTrayIcon::~QWidgetPlatformSystemTrayIcon()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIconD1Ev(
    QWidgetPlatformSystemTrayIcon *self) {
  delete self;
}

//  void QWidgetPlatformSystemTrayIcon::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIcon4initEv(
    QWidgetPlatformSystemTrayIcon *self) {
  self->init();
}

//  void QWidgetPlatformSystemTrayIcon::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIcon7cleanupEv(
    QWidgetPlatformSystemTrayIcon *self) {
  self->cleanup();
}

//  void QWidgetPlatformSystemTrayIcon::updateIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIcon10updateIconERK5QIcon(
    QWidgetPlatformSystemTrayIcon *self,
    const QIcon *icon) {
  self->updateIcon(*icon);
}

//  void QWidgetPlatformSystemTrayIcon::updateToolTip(const QString &tooltip)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIcon13updateToolTipERK7QString(
    QWidgetPlatformSystemTrayIcon *self,
    const QString *tooltip) {
  self->updateToolTip(*tooltip);
}

//  void QWidgetPlatformSystemTrayIcon::updateMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIcon10updateMenuEP13QPlatformMenu(
    QWidgetPlatformSystemTrayIcon *self,
    QPlatformMenu *menu) {
  self->updateMenu(menu);
}

//  QRect QWidgetPlatformSystemTrayIcon::geometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK29QWidgetPlatformSystemTrayIcon8geometryEv(
    const QWidgetPlatformSystemTrayIcon *self) {
  return new QRect(self->geometry());
}

//  void QWidgetPlatformSystemTrayIcon::showMessage(const QString &title,
//      const QString &msg, const QIcon &icon, MessageIcon iconType, int
//      msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWidgetPlatformSystemTrayIcon11showMessageERK7QStringS2_RK5QIconN23QPlatformSystemTrayIcon11MessageIconEi(
    QWidgetPlatformSystemTrayIcon *self,
    const QString *title,
    const QString *msg,
    const QIcon *icon,
    QPlatformSystemTrayIcon::MessageIcon iconType,
    int msecs) {
  self->showMessage(*title, *msg, *icon, iconType, msecs);
}

//  bool QWidgetPlatformSystemTrayIcon::isSystemTrayAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWidgetPlatformSystemTrayIcon21isSystemTrayAvailableEv(
    const QWidgetPlatformSystemTrayIcon *self) {
  return self->isSystemTrayAvailable();
}

//  bool QWidgetPlatformSystemTrayIcon::supportsMessages() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWidgetPlatformSystemTrayIcon16supportsMessagesEv(
    const QWidgetPlatformSystemTrayIcon *self) {
  return self->supportsMessages();
}

//  QPlatformMenu *QWidgetPlatformSystemTrayIcon::createMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK29QWidgetPlatformSystemTrayIcon10createMenuEv(
    const QWidgetPlatformSystemTrayIcon *self) {
  return self->createMenu();
}

#endif  // QT_CONFIG(systemtrayicon)
