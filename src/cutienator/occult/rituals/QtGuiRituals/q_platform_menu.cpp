//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformmenu.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformmenu.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QPlatformMenu::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QPlatformMenu10metaObjectEv(
    const QPlatformMenu *self) {
  return self->metaObject();
}

//  void *QPlatformMenu::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QPlatformMenu11qt_metacastEPKc(
    QPlatformMenu *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformMenu::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QPlatformMenu11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformMenu *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformMenu::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QPlatformMenu2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMenu::tr(s, c, n));
}

//  void QPlatformMenu::insertMenuItem(QPlatformMenuItem *menuItem,
//      QPlatformMenuItem *before)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu14insertMenuItemEP17QPlatformMenuItemS1_(
    QPlatformMenu *self,
    QPlatformMenuItem *menuItem,
    QPlatformMenuItem *before) {
  self->insertMenuItem(menuItem, before);
}

//  void QPlatformMenu::removeMenuItem(QPlatformMenuItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu14removeMenuItemEP17QPlatformMenuItem(
    QPlatformMenu *self,
    QPlatformMenuItem *menuItem) {
  self->removeMenuItem(menuItem);
}

//  void QPlatformMenu::syncMenuItem(QPlatformMenuItem *menuItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu12syncMenuItemEP17QPlatformMenuItem(
    QPlatformMenu *self,
    QPlatformMenuItem *menuItem) {
  self->syncMenuItem(menuItem);
}

//  void QPlatformMenu::syncSeparatorsCollapsible(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu25syncSeparatorsCollapsibleEb(
    QPlatformMenu *self,
    bool enable) {
  self->syncSeparatorsCollapsible(enable);
}

//  void QPlatformMenu::setTag(quintptr tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu6setTagEy(QPlatformMenu *self, quintptr tag) {
  self->setTag(tag);
}

//  quintptr QPlatformMenu::tag() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK13QPlatformMenu3tagEv(const QPlatformMenu *self) {
  return self->tag();
}

//  void QPlatformMenu::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu7setTextERK7QString(
    QPlatformMenu *self,
    const QString *text) {
  self->setText(*text);
}

//  void QPlatformMenu::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu7setIconERK5QIcon(
    QPlatformMenu *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  void QPlatformMenu::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu10setEnabledEb(
    QPlatformMenu *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  bool QPlatformMenu::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlatformMenu9isEnabledEv(const QPlatformMenu *self) {
  return self->isEnabled();
}

//  void QPlatformMenu::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu10setVisibleEb(
    QPlatformMenu *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QPlatformMenu::setMinimumWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu15setMinimumWidthEi(
    QPlatformMenu *self,
    int width) {
  self->setMinimumWidth(width);
}

//  void QPlatformMenu::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu7setFontERK5QFont(
    QPlatformMenu *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QPlatformMenu::setMenuType(MenuType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu11setMenuTypeENS_8MenuTypeE(
    QPlatformMenu *self,
    QPlatformMenu::MenuType type) {
  self->setMenuType(type);
}

//  void QPlatformMenu::showPopup(const QWindow *parentWindow, const QRect
//      &targetRect, const QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMenuItem(
    QPlatformMenu *self,
    const QWindow *parentWindow,
    const QRect *targetRect,
    const QPlatformMenuItem *item) {
  self->showPopup(parentWindow, *targetRect, item);
}

//  void QPlatformMenu::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu7dismissEv(QPlatformMenu *self) {
  self->dismiss();
}

//  QPlatformMenuItem *QPlatformMenu::menuItemAt(int position) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK13QPlatformMenu10menuItemAtEi(
    const QPlatformMenu *self,
    int position) {
  return self->menuItemAt(position);
}

//  QPlatformMenuItem *QPlatformMenu::menuItemForTag(quintptr tag) const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK13QPlatformMenu14menuItemForTagEy(
    const QPlatformMenu *self,
    quintptr tag) {
  return self->menuItemForTag(tag);
}

//  QPlatformMenuItem *QPlatformMenu::createMenuItem() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_ZNK13QPlatformMenu14createMenuItemEv(
    const QPlatformMenu *self) {
  return self->createMenuItem();
}

//  QPlatformMenu *QPlatformMenu::createSubMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_ZNK13QPlatformMenu13createSubMenuEv(
    const QPlatformMenu *self) {
  return self->createSubMenu();
}

//  void QPlatformMenu::aboutToShow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu11aboutToShowEv(QPlatformMenu *self) {
  self->aboutToShow();
}

//  void QPlatformMenu::aboutToHide()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlatformMenu11aboutToHideEv(QPlatformMenu *self) {
  self->aboutToHide();
}

//  void QPlatformMenu::setTag(quintptr tag)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformMenu6setTagEy(
    QPlatformMenu *self,
    quintptr tag) {
  self->QPlatformMenu::setTag(tag);
}

//  quintptr QPlatformMenu::tag() const
extern "C" Q_DECL_EXPORT
quintptr ritual_own_ZNK13QPlatformMenu3tagEv(const QPlatformMenu *self) {
  return self->QPlatformMenu::tag();
}

//  bool QPlatformMenu::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QPlatformMenu9isEnabledEv(const QPlatformMenu *self) {
  return self->QPlatformMenu::isEnabled();
}

//  void QPlatformMenu::setMinimumWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformMenu15setMinimumWidthEi(
    QPlatformMenu *self,
    int width) {
  self->QPlatformMenu::setMinimumWidth(width);
}

//  void QPlatformMenu::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformMenu7setFontERK5QFont(
    QPlatformMenu *self,
    const QFont *font) {
  self->QPlatformMenu::setFont(*font);
}

//  void QPlatformMenu::setMenuType(MenuType type)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformMenu11setMenuTypeENS_8MenuTypeE(
    QPlatformMenu *self,
    QPlatformMenu::MenuType type) {
  self->QPlatformMenu::setMenuType(type);
}

//  void QPlatformMenu::showPopup(const QWindow *parentWindow, const QRect
//      &targetRect, const QPlatformMenuItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformMenu9showPopupEPK7QWindowRK5QRectPK17QPlatformMenuItem(
    QPlatformMenu *self,
    const QWindow *parentWindow,
    const QRect *targetRect,
    const QPlatformMenuItem *item) {
  self->QPlatformMenu::showPopup(parentWindow, *targetRect, item);
}

//  void QPlatformMenu::dismiss()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QPlatformMenu7dismissEv(QPlatformMenu *self) {
  self->QPlatformMenu::dismiss();
}

//  QPlatformMenuItem *QPlatformMenu::createMenuItem() const
extern "C" Q_DECL_EXPORT
QPlatformMenuItem *ritual_own_ZNK13QPlatformMenu14createMenuItemEv(
    const QPlatformMenu *self) {
  return self->QPlatformMenu::createMenuItem();
}

//  QPlatformMenu *QPlatformMenu::createSubMenu() const
extern "C" Q_DECL_EXPORT
QPlatformMenu *ritual_own_ZNK13QPlatformMenu13createSubMenuEv(
    const QPlatformMenu *self) {
  return self->QPlatformMenu::createSubMenu();
}
