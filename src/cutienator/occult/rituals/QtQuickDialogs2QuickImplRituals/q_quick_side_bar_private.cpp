//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksidebar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  Only a class built on QQuickSideBarPrivate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSideBarPrivate : QQuickSideBarPrivate {
  using QQuickSideBarPrivate::getContentWidth;
  using QQuickSideBarPrivate::getContentHeight;
  using QQuickSideBarPrivate::itemGeometryChanged;
  using QQuickSideBarPrivate::itemImplicitWidthChanged;
  using QQuickSideBarPrivate::itemImplicitHeightChanged;
};

//  QQuickSideBar *QQuickSideBarPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickSideBar *ritual_ZN20QQuickSideBarPrivate6q_funcEv(
    QQuickSideBarPrivate *self) {
  return self->q_func();
}

//  const QQuickSideBar *QQuickSideBarPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickSideBar *ritual_ZNK20QQuickSideBarPrivate6q_funcEv(
    const QQuickSideBarPrivate *self) {
  return self->q_func();
}

//  QQuickSideBarPrivate *QQuickSideBarPrivate::get(QQuickSideBar *sidebar)
extern "C" Q_DECL_EXPORT
QQuickSideBarPrivate *ritual_ZN20QQuickSideBarPrivate3getEP13QQuickSideBar(
    QQuickSideBar *sidebar) {
  return QQuickSideBarPrivate::get(sidebar);
}

//  QQuickItem *QQuickSideBarPrivate::createDelegateItem(QQmlComponent
//      *component, const QVariantMap &initialProperties)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN20QQuickSideBarPrivate18createDelegateItemEP13QQmlComponentRK4QMapI7QString8QVariantE(
    QQuickSideBarPrivate *self,
    QQmlComponent *component,
    const QMap<QString, QVariant> *initialProperties) {
  return self->createDelegateItem(component, *initialProperties);
}

//  void QQuickSideBarPrivate::repopulate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate10repopulateEv(
    QQuickSideBarPrivate *self) {
  self->repopulate();
}

//  void QQuickSideBarPrivate::buttonClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate13buttonClickedEv(
    QQuickSideBarPrivate *self) {
  self->buttonClicked();
}

//  QUrl QQuickSideBarPrivate::dialogFolder() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickSideBarPrivate12dialogFolderEv(
    const QQuickSideBarPrivate *self) {
  return new QUrl(self->dialogFolder());
}

//  void QQuickSideBarPrivate::setDialogFolder(const QUrl &folder)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate15setDialogFolderERK4QUrl(
    QQuickSideBarPrivate *self,
    const QUrl *folder) {
  self->setDialogFolder(*folder);
}

//  QString QQuickSideBarPrivate::displayNameFromFolderPath(const QString
//      &filePath)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickSideBarPrivate25displayNameFromFolderPathERK7QString(
    QQuickSideBarPrivate *self,
    const QString *filePath) {
  return new QString(self->displayNameFromFolderPath(*filePath));
}

//  QUrl QQuickSideBarPrivate::folderIconSource() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickSideBarPrivate16folderIconSourceEv(
    const QQuickSideBarPrivate *self) {
  return new QUrl(self->folderIconSource());
}

//  QUrl
//      QQuickSideBarPrivate::folderIconSource(QStandardPaths::StandardLocati
//      on stdLocation) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickSideBarPrivate16folderIconSourceEN14QStandardPaths16StandardLocationE(
    const QQuickSideBarPrivate *self,
    QStandardPaths::StandardLocation stdLocation) {
  return new QUrl(self->folderIconSource(stdLocation));
}

//  QSize QQuickSideBarPrivate::dialogIconSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QQuickSideBarPrivate14dialogIconSizeEv(
    const QQuickSideBarPrivate *self) {
  return new QSize(self->dialogIconSize());
}

//  void QQuickSideBarPrivate::folderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate13folderChangedEv(
    QQuickSideBarPrivate *self) {
  self->folderChanged();
}

//  void QQuickSideBarPrivate::readSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate12readSettingsEv(
    QQuickSideBarPrivate *self) {
  self->readSettings();
}

//  void QQuickSideBarPrivate::writeSettings() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QQuickSideBarPrivate13writeSettingsEv(
    const QQuickSideBarPrivate *self) {
  self->writeSettings();
}

//  void QQuickSideBarPrivate::addFavorite(const QUrl &favorite)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate11addFavoriteERK4QUrl(
    QQuickSideBarPrivate *self,
    const QUrl *favorite) {
  self->addFavorite(*favorite);
}

//  void QQuickSideBarPrivate::removeFavorite(const QUrl &favorite)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate14removeFavoriteERK4QUrl(
    QQuickSideBarPrivate *self,
    const QUrl *favorite) {
  self->removeFavorite(*favorite);
}

//  bool QQuickSideBarPrivate::showAddFavoriteDelegate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickSideBarPrivate23showAddFavoriteDelegateEv(
    const QQuickSideBarPrivate *self) {
  return self->showAddFavoriteDelegate();
}

//  void QQuickSideBarPrivate::setShowAddFavoriteDelegate(bool show)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate26setShowAddFavoriteDelegateEb(
    QQuickSideBarPrivate *self,
    bool show) {
  self->setShowAddFavoriteDelegate(show);
}

//  bool QQuickSideBarPrivate::addFavoriteDelegateHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickSideBarPrivate26addFavoriteDelegateHoveredEv(
    const QQuickSideBarPrivate *self) {
  return self->addFavoriteDelegateHovered();
}

//  void QQuickSideBarPrivate::setAddFavoriteDelegateHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate29setAddFavoriteDelegateHoveredEb(
    QQuickSideBarPrivate *self,
    bool hovered) {
  self->setAddFavoriteDelegateHovered(hovered);
}

//  QUrl QQuickSideBarPrivate::addFavoriteIconUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK20QQuickSideBarPrivate18addFavoriteIconUrlEv(
    const QQuickSideBarPrivate *self) {
  return new QUrl(self->addFavoriteIconUrl());
}

//  void QQuickSideBarPrivate::initContextMenu()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate15initContextMenuEv(
    QQuickSideBarPrivate *self) {
  self->initContextMenu();
}

//  void QQuickSideBarPrivate::handleContextMenuRequested(QPointF pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate26handleContextMenuRequestedE7QPointF(
    QQuickSideBarPrivate *self,
    const QPointF *pos) {
  self->handleContextMenuRequested(*pos);
}

//  void QQuickSideBarPrivate::handleRemoveAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate18handleRemoveActionEv(
    QQuickSideBarPrivate *self) {
  self->handleRemoveAction();
}

//  qreal QQuickSideBarPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickSideBarPrivate15getContentWidthEv(
    const QQuickSideBarPrivate *self) {
  return self->getContentWidth();
}

//  qreal QQuickSideBarPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickSideBarPrivate16getContentHeightEv(
    const QQuickSideBarPrivate *self) {
  return self->getContentHeight();
}

//  void QQuickSideBarPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickSideBarPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickSideBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickSideBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickSideBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickSideBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickSideBarPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  qreal QQuickSideBarPrivate::getContentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QQuickSideBarPrivate15getContentWidthEv(
    const QQuickSideBarPrivate *self) {
  return static_cast<const OwnQQuickSideBarPrivate *>(self)->OwnQQuickSideBarPrivate::getContentWidth();
}

//  qreal QQuickSideBarPrivate::getContentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK20QQuickSideBarPrivate16getContentHeightEv(
    const QQuickSideBarPrivate *self) {
  return static_cast<const OwnQQuickSideBarPrivate *>(self)->OwnQQuickSideBarPrivate::getContentHeight();
}

//  void QQuickSideBarPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSideBarPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickSideBarPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  static_cast<OwnQQuickSideBarPrivate *>(self)->OwnQQuickSideBarPrivate::itemGeometryChanged(
      item,
      *change,
      *diff);
}

//  void QQuickSideBarPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSideBarPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickSideBarPrivate *self,
    QQuickItem *item) {
  static_cast<OwnQQuickSideBarPrivate *>(self)->OwnQQuickSideBarPrivate::itemImplicitWidthChanged(
      item);
}

//  void QQuickSideBarPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickSideBarPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickSideBarPrivate *self,
    QQuickItem *item) {
  static_cast<OwnQQuickSideBarPrivate *>(self)->OwnQQuickSideBarPrivate::itemImplicitHeightChanged(
      item);
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
