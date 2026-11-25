//  Written by hand on 2026-11-25 from
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformmenu_p.h,
//  Qt 6.12.0, as the Qt of macOS and of Windows installs it, the
//  same text as on Linux. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object.
//  Not written: the constructor, 'tr' and 'menu', which
//  Qt's library offers not.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(menu)
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformmenu_p.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qicon.h>
#include <QtGui/qwindow.h>

//  const QMetaObject *QWidgetPlatformMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QWidgetPlatformMenu10metaObjectEv(
    const QWidgetPlatformMenu *self) {
  return self->metaObject();
}

//  QWidgetPlatformMenu::~QWidgetPlatformMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenuD1Ev(QWidgetPlatformMenu *self) {
  delete self;
}

//  void QWidgetPlatformMenu::insertMenuItem(QPlatformMenuItem *item,
//      QPlatformMenuItem *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_(
    QWidgetPlatformMenu *self,
    QPlatformMenuItem *item,
    QPlatformMenuItem *before) {
  self->insertMenuItem(item, before);
}

//  void QWidgetPlatformMenu::removeMenuItem(QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu14removeMenuItemEP17QPlatformMenuItem(
    QWidgetPlatformMenu *self,
    QPlatformMenuItem *item) {
  self->removeMenuItem(item);
}

//  void QWidgetPlatformMenu::syncMenuItem(QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu12syncMenuItemEP17QPlatformMenuItem(
    QWidgetPlatformMenu *self,
    QPlatformMenuItem *item) {
  self->syncMenuItem(item);
}

//  void QWidgetPlatformMenu::syncSeparatorsCollapsible(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu25syncSeparatorsCollapsibleEb(
    QWidgetPlatformMenu *self,
    bool enable) {
  self->syncSeparatorsCollapsible(enable);
}

//  void QWidgetPlatformMenu::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu7setTextERK7QString(
    QWidgetPlatformMenu *self,
    const QString *text) {
  self->setText(*text);
}

//  void QWidgetPlatformMenu::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu7setIconERK5QIcon(
    QWidgetPlatformMenu *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  void QWidgetPlatformMenu::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu10setEnabledEb(
    QWidgetPlatformMenu *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QWidgetPlatformMenu::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWidgetPlatformMenu9isEnabledEv(
    const QWidgetPlatformMenu *self) {
  return self->isEnabled();
}

//  void QWidgetPlatformMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu10setVisibleEb(
    QWidgetPlatformMenu *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QWidgetPlatformMenu::setMinimumWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu15setMinimumWidthEi(
    QWidgetPlatformMenu *self,
    int width) {
  self->setMinimumWidth(width);
}

//  void QWidgetPlatformMenu::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu7setFontERK5QFont(
    QWidgetPlatformMenu *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QWidgetPlatformMenu::setMenuType(MenuType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu11setMenuTypeEN13QPlatformMenu8MenuTypeE(
    QWidgetPlatformMenu *self,
    QPlatformMenu::MenuType type) {
  self->setMenuType(type);
}

//  void QWidgetPlatformMenu::showPopup(const QWindow *window, const QRect
//      &targetRect, const QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMenuItem(
    QWidgetPlatformMenu *self,
    const QWindow *window,
    const QRect *targetRect,
    const QPlatformMenuItem *item) {
  self->showPopup(window, *targetRect, item);
}

//  void QWidgetPlatformMenu::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWidgetPlatformMenu7dismissEv(QWidgetPlatformMenu *self) {
  self->dismiss();
}

//  QPlatformMenuItem *QWidgetPlatformMenu::menuItemAt(int position) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK19QWidgetPlatformMenu10menuItemAtEi(
    const QWidgetPlatformMenu *self,
    int position) {
  return self->menuItemAt(position);
}

//  QPlatformMenuItem *QWidgetPlatformMenu::menuItemForTag(quintptr tag)
//      const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK19QWidgetPlatformMenu14menuItemForTagEy(
    const QWidgetPlatformMenu *self,
    quintptr tag) {
  return self->menuItemForTag(tag);
}

//  QPlatformMenuItem *QWidgetPlatformMenu::createMenuItem() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK19QWidgetPlatformMenu14createMenuItemEv(
    const QWidgetPlatformMenu *self) {
  return self->createMenuItem();
}

//  QPlatformMenu *QWidgetPlatformMenu::createSubMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK19QWidgetPlatformMenu13createSubMenuEv(
    const QWidgetPlatformMenu *self) {
  return self->createSubMenu();
}

#endif  // QT_CONFIG(menu)
