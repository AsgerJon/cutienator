//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformmenuitem_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor, 'tr' and 'action', which
//  Qt's library offers not.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(menu)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformmenuitem_p.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qicon.h>
#include <QtGui/qkeysequence.h>

//  const QMetaObject *QWidgetPlatformMenuItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QWidgetPlatformMenuItem10metaObjectEv(
    const QWidgetPlatformMenuItem *self) {
  return self->metaObject();
}

//  QWidgetPlatformMenuItem::~QWidgetPlatformMenuItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItemD1Ev(QWidgetPlatformMenuItem *self) {
  delete self;
}

//  void QWidgetPlatformMenuItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem7setTextERK7QString(
    QWidgetPlatformMenuItem *self,
    const QString *text) {
  self->setText(*text);
}

//  void QWidgetPlatformMenuItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem7setIconERK5QIcon(
    QWidgetPlatformMenuItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  void QWidgetPlatformMenuItem::setMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem7setMenuEP13QPlatformMenu(
    QWidgetPlatformMenuItem *self,
    QPlatformMenu *menu) {
  self->setMenu(menu);
}

//  void QWidgetPlatformMenuItem::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem10setVisibleEb(
    QWidgetPlatformMenuItem *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QWidgetPlatformMenuItem::setIsSeparator(bool separator)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem14setIsSeparatorEb(
    QWidgetPlatformMenuItem *self,
    bool separator) {
  self->setIsSeparator(separator);
}

//  void QWidgetPlatformMenuItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem7setFontERK5QFont(
    QWidgetPlatformMenuItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QWidgetPlatformMenuItem::setRole(MenuRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem7setRoleEN17QPlatformMenuItem8MenuRoleE(
    QWidgetPlatformMenuItem *self,
    QPlatformMenuItem::MenuRole role) {
  self->setRole(role);
}

//  void QWidgetPlatformMenuItem::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem12setCheckableEb(
    QWidgetPlatformMenuItem *self,
    bool checkable) {
  self->setCheckable(checkable);
}

//  void QWidgetPlatformMenuItem::setChecked(bool checked)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem10setCheckedEb(
    QWidgetPlatformMenuItem *self,
    bool checked) {
  self->setChecked(checked);
}

#if QT_CONFIG(shortcut)
//  void QWidgetPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem11setShortcutERK12QKeySequence(
    QWidgetPlatformMenuItem *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}
#endif  // QT_CONFIG(shortcut)

//  void QWidgetPlatformMenuItem::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem10setEnabledEb(
    QWidgetPlatformMenuItem *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QWidgetPlatformMenuItem::setIconSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWidgetPlatformMenuItem11setIconSizeEi(
    QWidgetPlatformMenuItem *self,
    int size) {
  self->setIconSize(size);
}

#endif  // QT_CONFIG(menu)
