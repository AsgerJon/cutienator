//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenubar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  QQuickMenuBar *QQuickMenuBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMenuBar *ritual_ZN20QQuickMenuBarPrivate6q_funcEv(
    QQuickMenuBarPrivate *self) {
  return self->q_func();
}

//  const QQuickMenuBar *QQuickMenuBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickMenuBar *ritual_ZNK20QQuickMenuBarPrivate6q_funcEv(
    const QQuickMenuBarPrivate *self) {
  return self->q_func();
}

//  QQuickMenuBarPrivate *QQuickMenuBarPrivate::get(QQuickMenuBar *menuBar)
extern "C" Q_DECL_EXPORT
QQuickMenuBarPrivate *ritual_ZN20QQuickMenuBarPrivate3getEP13QQuickMenuBar(
    QQuickMenuBar *menuBar) {
  return QQuickMenuBarPrivate::get(menuBar);
}

//  QQmlListProperty<QQuickMenu> QQuickMenuBarPrivate::menus()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuickMenu> *ritual_ZN20QQuickMenuBarPrivate5menusEv(
    QQuickMenuBarPrivate *self) {
  return new QQmlListProperty<QQuickMenu>(self->menus());
}

//  QQmlListProperty<QObject> QQuickMenuBarPrivate::contentData()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN20QQuickMenuBarPrivate11contentDataEv(
    QQuickMenuBarPrivate *self) {
  return new QQmlListProperty<QObject>(self->contentData());
}

//  QQuickItem *QQuickMenuBarPrivate::createItemFromDelegate()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN20QQuickMenuBarPrivate22createItemFromDelegateEv(
    QQuickMenuBarPrivate *self) {
  return self->createItemFromDelegate();
}

//  QQuickMenuBarItem *QQuickMenuBarPrivate::createMenuBarItem(QQuickMenu
//      *menu)
extern "C" Q_DECL_EXPORT
QQuickMenuBarItem *ritual_ZN20QQuickMenuBarPrivate17createMenuBarItemEP10QQuickMenu(
    QQuickMenuBarPrivate *self,
    QQuickMenu *menu) {
  return self->createMenuBarItem(menu);
}

//  void QQuickMenuBarPrivate::openCurrentMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate15openCurrentMenuEv(
    QQuickMenuBarPrivate *self) {
  self->openCurrentMenu();
}

//  void QQuickMenuBarPrivate::closeCurrentMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate16closeCurrentMenuEv(
    QQuickMenuBarPrivate *self) {
  self->closeCurrentMenu();
}

//  void QQuickMenuBarPrivate::activateMenuItem(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate16activateMenuItemEi(
    QQuickMenuBarPrivate *self,
    int index) {
  self->activateMenuItem(index);
}

//  void QQuickMenuBarPrivate::activateItem(QQuickMenuBarItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate12activateItemEP17QQuickMenuBarItem(
    QQuickMenuBarPrivate *self,
    QQuickMenuBarItem *item) {
  self->activateItem(item);
}

//  void QQuickMenuBarPrivate::activateNextItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate16activateNextItemEv(
    QQuickMenuBarPrivate *self) {
  self->activateNextItem();
}

//  void QQuickMenuBarPrivate::activatePreviousItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate20activatePreviousItemEv(
    QQuickMenuBarPrivate *self) {
  self->activatePreviousItem();
}

//  void QQuickMenuBarPrivate::onItemHovered()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate13onItemHoveredEv(
    QQuickMenuBarPrivate *self) {
  self->onItemHovered();
}

//  void QQuickMenuBarPrivate::onItemTriggered()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate15onItemTriggeredEv(
    QQuickMenuBarPrivate *self) {
  self->onItemTriggered();
}

//  void QQuickMenuBarPrivate::onMenuAboutToHide(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate17onMenuAboutToHideEP10QQuickMenu(
    QQuickMenuBarPrivate *self,
    QQuickMenu *menu) {
  self->onMenuAboutToHide(menu);
}

//  void QQuickMenuBarPrivate::insertMenu(int index, QQuickMenu *menu,
//      QQuickMenuBarItem *delegateItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate10insertMenuEiP10QQuickMenuP17QQuickMenuBarItem(
    QQuickMenuBarPrivate *self,
    int index,
    QQuickMenu *menu,
    QQuickMenuBarItem *delegateItem) {
  self->insertMenu(index, menu, delegateItem);
}

//  QQuickMenu *QQuickMenuBarPrivate::takeMenu(int index)
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZN20QQuickMenuBarPrivate8takeMenuEi(
    QQuickMenuBarPrivate *self,
    int index) {
  return self->takeMenu(index);
}

//  void QQuickMenuBarPrivate::insertNativeMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate16insertNativeMenuEP10QQuickMenu(
    QQuickMenuBarPrivate *self,
    QQuickMenu *menu) {
  self->insertNativeMenu(menu);
}

//  void QQuickMenuBarPrivate::removeNativeMenu(QQuickMenu *menu)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate16removeNativeMenuEP10QQuickMenu(
    QQuickMenuBarPrivate *self,
    QQuickMenu *menu) {
  self->removeNativeMenu(menu);
}

//  void QQuickMenuBarPrivate::syncMenuBarItemVisibilty(QQuickMenuBarItem
//      *menuBarItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate24syncMenuBarItemVisibiltyEP17QQuickMenuBarItem(
    QQuickMenuBarPrivate *self,
    QQuickMenuBarItem *menuBarItem) {
  self->syncMenuBarItemVisibilty(menuBarItem);
}

//  QWindow *QQuickMenuBarPrivate::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK20QQuickMenuBarPrivate6windowEv(
    const QQuickMenuBarPrivate *self) {
  return self->window();
}

//  int QQuickMenuBarPrivate::menuIndex(QQuickMenu *menu) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickMenuBarPrivate9menuIndexEP10QQuickMenu(
    const QQuickMenuBarPrivate *self,
    QQuickMenu *menu) {
  return self->menuIndex(menu);
}

//  QPlatformMenuBar *QQuickMenuBarPrivate::nativeHandle() const
extern "C" Q_DECL_EXPORT
QPlatformMenuBar *ritual_ZNK20QQuickMenuBarPrivate12nativeHandleEv(
    const QQuickMenuBarPrivate *self) {
  return self->nativeHandle();
}

//  bool QQuickMenuBarPrivate::useNativeMenuBar() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickMenuBarPrivate16useNativeMenuBarEv(
    const QQuickMenuBarPrivate *self) {
  return self->useNativeMenuBar();
}

//  bool QQuickMenuBarPrivate::useNativeMenu(const QQuickMenu *menu) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickMenuBarPrivate13useNativeMenuEPK10QQuickMenu(
    const QQuickMenuBarPrivate *self,
    const QQuickMenu *menu) {
  return self->useNativeMenu(menu);
}

//  void QQuickMenuBarPrivate::syncNativeMenuBarVisible()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate24syncNativeMenuBarVisibleEv(
    QQuickMenuBarPrivate *self) {
  self->syncNativeMenuBarVisible();
}

//  void QQuickMenuBarPrivate::createNativeMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate19createNativeMenuBarEv(
    QQuickMenuBarPrivate *self) {
  self->createNativeMenuBar();
}

//  void QQuickMenuBarPrivate::removeNativeMenuBar()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate19removeNativeMenuBarEv(
    QQuickMenuBarPrivate *self) {
  self->removeNativeMenuBar();
}

//  qreal QQuickMenuBarPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickMenuBarPrivate15getContentWidthEv(
    const QQuickMenuBarPrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickMenuBarPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickMenuBarPrivate16getContentHeightEv(
    const QQuickMenuBarPrivate *self) {
  return self->getContentHeight();
}

//  void QQuickMenuBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickMenuBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickMenuBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickMenuBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickMenuBarPrivate::contentData_append(QQmlListProperty<QObject>
//      *prop, QObject *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate18contentData_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *prop,
    QObject *obj) {
  QQuickMenuBarPrivate::contentData_append(prop, obj);
}

//  void QQuickMenuBarPrivate::menus_append(QQmlListProperty<QQuickMenu>
//      *prop, QQuickMenu *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate12menus_appendEP16QQmlListPropertyI10QQuickMenuEPS1_(
    QQmlListProperty<QQuickMenu> *prop,
    QQuickMenu *obj) {
  QQuickMenuBarPrivate::menus_append(prop, obj);
}

//  qsizetype QQuickMenuBarPrivate::menus_count(QQmlListProperty<QQuickMenu>
//      *prop)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QQuickMenuBarPrivate11menus_countEP16QQmlListPropertyI10QQuickMenuE(
    QQmlListProperty<QQuickMenu> *prop) {
  return QQuickMenuBarPrivate::menus_count(prop);
}

//  QQuickMenu *QQuickMenuBarPrivate::menus_at(QQmlListProperty<QQuickMenu>
//      *prop, qsizetype index)
extern "C" Q_DECL_EXPORT
QQuickMenu *ritual_ZN20QQuickMenuBarPrivate8menus_atEP16QQmlListPropertyI10QQuickMenuEx(
    QQmlListProperty<QQuickMenu> *prop,
    qsizetype index) {
  return QQuickMenuBarPrivate::menus_at(prop, index);
}

//  void QQuickMenuBarPrivate::menus_clear(QQmlListProperty<QQuickMenu>
//      *prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickMenuBarPrivate11menus_clearEP16QQmlListPropertyI10QQuickMenuE(
    QQmlListProperty<QQuickMenu> *prop) {
  QQuickMenuBarPrivate::menus_clear(prop);
}

//  QPalette QQuickMenuBarPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK20QQuickMenuBarPrivate14defaultPaletteEv(
    const QQuickMenuBarPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  qreal QQuickMenuBarPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QQuickMenuBarPrivate15getContentWidthEv(
    const QQuickMenuBarPrivate *self) {
  return self->QQuickMenuBarPrivate::getContentWidth();
}

//  qreal QQuickMenuBarPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QQuickMenuBarPrivate16getContentHeightEv(
    const QQuickMenuBarPrivate *self) {
  return self->QQuickMenuBarPrivate::getContentHeight();
}

//  void QQuickMenuBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickMenuBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickMenuBarPrivate *self,
    QQuickItem *item) {
  self->QQuickMenuBarPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickMenuBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickMenuBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickMenuBarPrivate *self,
    QQuickItem *item) {
  self->QQuickMenuBarPrivate::itemImplicitHeightChanged(item);
}

//  QPalette QQuickMenuBarPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK20QQuickMenuBarPrivate14defaultPaletteEv(
    const QQuickMenuBarPrivate *self) {
  return new QPalette(self->QQuickMenuBarPrivate::defaultPalette());
}

//  a QQmlListProperty<QQuickMenu> a ritual of QQuickMenuBarPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickMenuBarPrivate__QQmlListProperty_QQuickMenu(
    QQmlListProperty<QQuickMenu> *self) {
  delete self;
}

//  a QQmlListProperty<QObject> a ritual of QQuickMenuBarPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickMenuBarPrivate__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(quicktemplates2_container)
