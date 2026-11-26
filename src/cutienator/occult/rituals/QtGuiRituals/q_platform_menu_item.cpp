//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformmenu.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformmenu.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtGui/qfont.h>
#include <QtGui/qkeysequence.h>

//  const QMetaObject *QPlatformMenuItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QPlatformMenuItem10metaObjectEv(
    const QPlatformMenuItem *self) {
  return self->metaObject();
}

//  void *QPlatformMenuItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QPlatformMenuItem11qt_metacastEPKc(
    QPlatformMenuItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformMenuItem::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QPlatformMenuItem11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformMenuItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformMenuItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QPlatformMenuItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformMenuItem::tr(s, c, n));
}

//  void QPlatformMenuItem::setTag(quintptr tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem6setTagEy(
    QPlatformMenuItem *self,
    quintptr tag) {
  self->setTag(tag);
}

//  quintptr QPlatformMenuItem::tag() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK17QPlatformMenuItem3tagEv(const QPlatformMenuItem *self) {
  return self->tag();
}

//  void QPlatformMenuItem::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem7setTextERK7QString(
    QPlatformMenuItem *self,
    const QString *text) {
  self->setText(*text);
}

//  void QPlatformMenuItem::setIcon(const QIcon &icon)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem7setIconERK5QIcon(
    QPlatformMenuItem *self,
    const QIcon *icon) {
  self->setIcon(*icon);
}

//  void QPlatformMenuItem::setMenu(QPlatformMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem7setMenuEP13QPlatformMenu(
    QPlatformMenuItem *self,
    QPlatformMenu *menu) {
  self->setMenu(menu);
}

//  void QPlatformMenuItem::setVisible(bool isVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem10setVisibleEb(
    QPlatformMenuItem *self,
    bool isVisible) {
  self->setVisible(isVisible);
}

//  void QPlatformMenuItem::setIsSeparator(bool isSeparator)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem14setIsSeparatorEb(
    QPlatformMenuItem *self,
    bool isSeparator) {
  self->setIsSeparator(isSeparator);
}

//  void QPlatformMenuItem::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem7setFontERK5QFont(
    QPlatformMenuItem *self,
    const QFont *font) {
  self->setFont(*font);
}

//  void QPlatformMenuItem::setRole(MenuRole role)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem7setRoleENS_8MenuRoleE(
    QPlatformMenuItem *self,
    QPlatformMenuItem::MenuRole role) {
  self->setRole(role);
}

//  void QPlatformMenuItem::setCheckable(bool checkable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem12setCheckableEb(
    QPlatformMenuItem *self,
    bool checkable) {
  self->setCheckable(checkable);
}

//  void QPlatformMenuItem::setChecked(bool isChecked)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem10setCheckedEb(
    QPlatformMenuItem *self,
    bool isChecked) {
  self->setChecked(isChecked);
}

#if QT_CONFIG(shortcut)
//  void QPlatformMenuItem::setShortcut(const QKeySequence &shortcut)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem11setShortcutERK12QKeySequence(
    QPlatformMenuItem *self,
    const QKeySequence *shortcut) {
  self->setShortcut(*shortcut);
}
#endif  // QT_CONFIG(shortcut)

//  void QPlatformMenuItem::setEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem10setEnabledEb(
    QPlatformMenuItem *self,
    bool enabled) {
  self->setEnabled(enabled);
}

//  void QPlatformMenuItem::setIconSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem11setIconSizeEi(
    QPlatformMenuItem *self,
    int size) {
  self->setIconSize(size);
}

//  void QPlatformMenuItem::setNativeContents(WId item)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem17setNativeContentsEy(
    QPlatformMenuItem *self,
    WId item) {
  self->setNativeContents(item);
}

//  void QPlatformMenuItem::setHasExclusiveGroup(bool hasExclusiveGroup)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem20setHasExclusiveGroupEb(
    QPlatformMenuItem *self,
    bool hasExclusiveGroup) {
  self->setHasExclusiveGroup(hasExclusiveGroup);
}

//  void QPlatformMenuItem::activated()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem9activatedEv(QPlatformMenuItem *self) {
  self->activated();
}

//  void QPlatformMenuItem::hovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformMenuItem7hoveredEv(QPlatformMenuItem *self) {
  self->hovered();
}

//  void QPlatformMenuItem::setTag(quintptr tag)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPlatformMenuItem6setTagEy(
    QPlatformMenuItem *self,
    quintptr tag) {
  self->QPlatformMenuItem::setTag(tag);
}

//  quintptr QPlatformMenuItem::tag() const
extern "C" Q_DECL_EXPORT
quintptr ritual_own_ZNK17QPlatformMenuItem3tagEv(
    const QPlatformMenuItem *self) {
  return self->QPlatformMenuItem::tag();
}

//  void QPlatformMenuItem::setNativeContents(WId item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPlatformMenuItem17setNativeContentsEy(
    QPlatformMenuItem *self,
    WId item) {
  self->QPlatformMenuItem::setNativeContents(item);
}

//  void QPlatformMenuItem::setHasExclusiveGroup(bool hasExclusiveGroup)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPlatformMenuItem20setHasExclusiveGroupEb(
    QPlatformMenuItem *self,
    bool hasExclusiveGroup) {
  self->QPlatformMenuItem::setHasExclusiveGroup(hasExclusiveGroup);
}
