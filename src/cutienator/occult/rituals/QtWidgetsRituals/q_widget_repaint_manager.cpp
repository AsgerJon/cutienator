//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetrepaintmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetrepaintmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtWidgets/qwidget.h>
#include <QtCore/qlist.h>

//  QWidgetRepaintManager::QWidgetRepaintManager(QWidget *t)
extern "C" Q_DECL_EXPORT
QWidgetRepaintManager *ritual_ZN21QWidgetRepaintManagerC1EP7QWidget(
    QWidget *t) {
  return new QWidgetRepaintManager(t);
}

//  QWidgetRepaintManager::~QWidgetRepaintManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManagerD1Ev(QWidgetRepaintManager *self) {
  delete self;
}

//  QBackingStore *QWidgetRepaintManager::backingStore() const
extern "C" Q_DECL_EXPORT
QBackingStore *ritual_ZNK21QWidgetRepaintManager12backingStoreEv(
    const QWidgetRepaintManager *self) {
  return self->backingStore();
}

//  void QWidgetRepaintManager::setBackingStore(QBackingStore *backingStore)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager15setBackingStoreEP13QBackingStore(
    QWidgetRepaintManager *self,
    QBackingStore *backingStore) {
  self->setBackingStore(backingStore);
}

//  void QWidgetRepaintManager::removeDirtyWidget(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager17removeDirtyWidgetEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *w) {
  self->removeDirtyWidget(w);
}

//  void QWidgetRepaintManager::sync(QWidget *exposedWidget, const QRegion
//      &exposedRegion)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager4syncEP7QWidgetRK7QRegion(
    QWidgetRepaintManager *self,
    QWidget *exposedWidget,
    const QRegion *exposedRegion) {
  self->sync(exposedWidget, *exposedRegion);
}

//  void QWidgetRepaintManager::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager4syncEv(QWidgetRepaintManager *self) {
  self->sync();
}

//  void QWidgetRepaintManager::markNeedsFlush(QWidget *widget, const QRegion
//      &region, const QPoint &topLevelOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager14markNeedsFlushEP7QWidgetRK7QRegionRK6QPoint(
    QWidgetRepaintManager *self,
    QWidget *widget,
    const QRegion *region,
    const QPoint *topLevelOffset) {
  self->markNeedsFlush(widget, *region, *topLevelOffset);
}

//  void QWidgetRepaintManager::addStaticWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager15addStaticWidgetEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *widget) {
  self->addStaticWidget(widget);
}

//  void QWidgetRepaintManager::moveStaticWidgets(QWidget *reparented)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager17moveStaticWidgetsEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *reparented) {
  self->moveStaticWidgets(reparented);
}

//  void QWidgetRepaintManager::removeStaticWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager18removeStaticWidgetEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *widget) {
  self->removeStaticWidget(widget);
}

//  QRegion QWidgetRepaintManager::staticContents(QWidget *widget, const
//      QRect &withinClipRect) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK21QWidgetRepaintManager14staticContentsEP7QWidgetRK5QRect(
    const QWidgetRepaintManager *self,
    QWidget *widget,
    const QRect *withinClipRect) {
  return new QRegion(self->staticContents(widget, *withinClipRect));
}

//  QRegion QWidgetRepaintManager::dirtyRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK21QWidgetRepaintManager11dirtyRegionEv(
    const QWidgetRepaintManager *self) {
  return new QRegion(self->dirtyRegion());
}

//  QList<QWidget *> QWidgetRepaintManager::dirtyWidgetList() const
extern "C" Q_DECL_EXPORT
QList<QWidget *> *ritual_ZNK21QWidgetRepaintManager15dirtyWidgetListEv(
    const QWidgetRepaintManager *self) {
  return new QList<QWidget *>(self->dirtyWidgetList());
}

//  bool QWidgetRepaintManager::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWidgetRepaintManager7isDirtyEv(
    const QWidgetRepaintManager *self) {
  return self->isDirty();
}

//  bool QWidgetRepaintManager::bltRect(const QRect &rect, int dx, int dy,
//      QWidget *widget)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QWidgetRepaintManager7bltRectERK5QRectiiP7QWidget(
    QWidgetRepaintManager *self,
    const QRect *rect,
    int dx,
    int dy,
    QWidget *widget) {
  return self->bltRect(*rect, dx, dy, widget);
}

//  void QWidgetRepaintManager::updateLists(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager11updateListsEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *widget) {
  self->updateLists(widget);
}

//  void QWidgetRepaintManager::addDirtyWidget(QWidget *widget, const QRegion
//      &rgn)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager14addDirtyWidgetEP7QWidgetRK7QRegion(
    QWidgetRepaintManager *self,
    QWidget *widget,
    const QRegion *rgn) {
  self->addDirtyWidget(widget, *rgn);
}

//  void QWidgetRepaintManager::resetWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager11resetWidgetEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *widget) {
  self->resetWidget(widget);
}

//  void QWidgetRepaintManager::addDirtyRenderToTextureWidget(QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager29addDirtyRenderToTextureWidgetEP7QWidget(
    QWidgetRepaintManager *self,
    QWidget *widget) {
  self->addDirtyRenderToTextureWidget(widget);
}

//  void QWidgetRepaintManager::sendUpdateRequest(QWidget *widget, UpdateTime
//      updateTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager17sendUpdateRequestEP7QWidgetNS_10UpdateTimeE(
    QWidgetRepaintManager *self,
    QWidget *widget,
    QWidgetRepaintManager::UpdateTime updateTime) {
  self->sendUpdateRequest(widget, updateTime);
}

//  bool QWidgetRepaintManager::syncAllowed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QWidgetRepaintManager11syncAllowedEv(
    QWidgetRepaintManager *self) {
  return self->syncAllowed();
}

//  void QWidgetRepaintManager::paintAndFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager13paintAndFlushEv(
    QWidgetRepaintManager *self) {
  self->paintAndFlush();
}

//  void QWidgetRepaintManager::markNeedsFlush(QWidget *widget, const QRegion
//      &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager14markNeedsFlushEP7QWidgetRK7QRegion(
    QWidgetRepaintManager *self,
    QWidget *widget,
    const QRegion *region) {
  self->markNeedsFlush(widget, *region);
}

//  void QWidgetRepaintManager::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager5flushEv(QWidgetRepaintManager *self) {
  self->flush();
}

//  void QWidgetRepaintManager::flush(QWidget *widget, const QRegion &region,
//      QPlatformTextureList *widgetTextures)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager5flushEP7QWidgetRK7QRegionP20QPlatformTextureList(
    QWidgetRepaintManager *self,
    QWidget *widget,
    const QRegion *region,
    QPlatformTextureList *widgetTextures) {
  self->flush(widget, *region, widgetTextures);
}

//  bool QWidgetRepaintManager::hasStaticContents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QWidgetRepaintManager17hasStaticContentsEv(
    const QWidgetRepaintManager *self) {
  return self->hasStaticContents();
}

//  void QWidgetRepaintManager::updateStaticContentsSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetRepaintManager24updateStaticContentsSizeEv(
    QWidgetRepaintManager *self) {
  self->updateStaticContentsSize();
}
