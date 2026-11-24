//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdesignersupport_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_designer)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdesignersupport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <QtGui/qtransform.h>
#include <QtCore/qstring.h>
#include <QtCore/qobject.h>
#include <QtCore/qlist.h>

//  QQuickDesignerSupport::QQuickDesignerSupport()
extern "C" Q_DECL_EXPORT
QQuickDesignerSupport *ritual_ZN21QQuickDesignerSupportC1Ev() {
  return new QQuickDesignerSupport();
}

//  QQuickDesignerSupport::~QQuickDesignerSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupportD1Ev(QQuickDesignerSupport *self) {
  delete self;
}

//  void QQuickDesignerSupport::refFromEffectItem(QQuickItem *referencedItem,
//      bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport17refFromEffectItemEP10QQuickItemb(
    QQuickDesignerSupport *self,
    QQuickItem *referencedItem,
    bool hide) {
  self->refFromEffectItem(referencedItem, hide);
}

//  void QQuickDesignerSupport::derefFromEffectItem(QQuickItem
//      *referencedItem, bool unhide)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport19derefFromEffectItemEP10QQuickItemb(
    QQuickDesignerSupport *self,
    QQuickItem *referencedItem,
    bool unhide) {
  self->derefFromEffectItem(referencedItem, unhide);
}

//  QImage QQuickDesignerSupport::renderImageForItem(QQuickItem
//      *referencedItem, const QRectF &boundingRect, const QSize &imageSize)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN21QQuickDesignerSupport18renderImageForItemEP10QQuickItemRK6QRectFRK5QSize(
    QQuickDesignerSupport *self,
    QQuickItem *referencedItem,
    const QRectF *boundingRect,
    const QSize *imageSize) {
  return new QImage(
      self->renderImageForItem(
          referencedItem,
          *boundingRect,
          *imageSize));
}

//  bool QQuickDesignerSupport::isDirty(QQuickItem *referencedItem, DirtyType
//      dirtyType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport7isDirtyEP10QQuickItemNS_9DirtyTypeE(
    QQuickItem *referencedItem,
    QQuickDesignerSupport::DirtyType dirtyType) {
  return QQuickDesignerSupport::isDirty(referencedItem, dirtyType);
}

//  void QQuickDesignerSupport::addDirty(QQuickItem *referencedItem,
//      DirtyType dirtyType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport8addDirtyEP10QQuickItemNS_9DirtyTypeE(
    QQuickItem *referencedItem,
    QQuickDesignerSupport::DirtyType dirtyType) {
  QQuickDesignerSupport::addDirty(referencedItem, dirtyType);
}

//  void QQuickDesignerSupport::resetDirty(QQuickItem *referencedItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport10resetDirtyEP10QQuickItem(
    QQuickItem *referencedItem) {
  QQuickDesignerSupport::resetDirty(referencedItem);
}

//  QTransform QQuickDesignerSupport::windowTransform(QQuickItem
//      *referencedItem)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN21QQuickDesignerSupport15windowTransformEP10QQuickItem(
    QQuickItem *referencedItem) {
  return new QTransform(
      QQuickDesignerSupport::windowTransform(
          referencedItem));
}

//  QTransform QQuickDesignerSupport::parentTransform(QQuickItem
//      *referencedItem)
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZN21QQuickDesignerSupport15parentTransformEP10QQuickItem(
    QQuickItem *referencedItem) {
  return new QTransform(
      QQuickDesignerSupport::parentTransform(
          referencedItem));
}

//  bool QQuickDesignerSupport::isAnchoredTo(QQuickItem *fromItem, QQuickItem
//      *toItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport12isAnchoredToEP10QQuickItemS1_(
    QQuickItem *fromItem,
    QQuickItem *toItem) {
  return QQuickDesignerSupport::isAnchoredTo(fromItem, toItem);
}

//  bool QQuickDesignerSupport::areChildrenAnchoredTo(QQuickItem *fromItem,
//      QQuickItem *toItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport21areChildrenAnchoredToEP10QQuickItemS1_(
    QQuickItem *fromItem,
    QQuickItem *toItem) {
  return QQuickDesignerSupport::areChildrenAnchoredTo(fromItem, toItem);
}

//  bool QQuickDesignerSupport::hasAnchor(QQuickItem *item, const QString
//      &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport9hasAnchorEP10QQuickItemRK7QString(
    QQuickItem *item,
    const QString *name) {
  return QQuickDesignerSupport::hasAnchor(item, *name);
}

//  QQuickItem *QQuickDesignerSupport::anchorFillTargetItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN21QQuickDesignerSupport20anchorFillTargetItemEP10QQuickItem(
    QQuickItem *item) {
  return QQuickDesignerSupport::anchorFillTargetItem(item);
}

//  QQuickItem *QQuickDesignerSupport::anchorCenterInTargetItem(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN21QQuickDesignerSupport24anchorCenterInTargetItemEP10QQuickItem(
    QQuickItem *item) {
  return QQuickDesignerSupport::anchorCenterInTargetItem(item);
}

//  void QQuickDesignerSupport::resetAnchor(QQuickItem *item, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport11resetAnchorEP10QQuickItemRK7QString(
    QQuickItem *item,
    const QString *name) {
  QQuickDesignerSupport::resetAnchor(item, *name);
}

//  void QQuickDesignerSupport::emitComponentCompleteSignalForAttachedPropert
//      y(QObject *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport46emitComponentCompleteSignalForAttachedPropertyEP7QObject(
    QObject *item) {
  QQuickDesignerSupport::emitComponentCompleteSignalForAttachedProperty(
      item);
}

//  QList<QObject *> QQuickDesignerSupport::statesForItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZN21QQuickDesignerSupport13statesForItemEP10QQuickItem(
    QQuickItem *item) {
  return new QList<QObject *>(QQuickDesignerSupport::statesForItem(item));
}

//  bool QQuickDesignerSupport::isComponentComplete(QQuickItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport19isComponentCompleteEP10QQuickItem(
    QQuickItem *item) {
  return QQuickDesignerSupport::isComponentComplete(item);
}

//  int QQuickDesignerSupport::borderWidth(QQuickItem *item)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickDesignerSupport11borderWidthEP10QQuickItem(
    QQuickItem *item) {
  return QQuickDesignerSupport::borderWidth(item);
}

//  void QQuickDesignerSupport::refreshExpressions(QQmlContext *context)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport18refreshExpressionsEP11QQmlContext(
    QQmlContext *context) {
  QQuickDesignerSupport::refreshExpressions(context);
}

//  void QQuickDesignerSupport::setRootItem(QQuickView *view, QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport11setRootItemEP10QQuickViewP10QQuickItem(
    QQuickView *view,
    QQuickItem *item) {
  QQuickDesignerSupport::setRootItem(view, item);
}

//  bool QQuickDesignerSupport::isValidWidth(QQuickItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport12isValidWidthEP10QQuickItem(
    QQuickItem *item) {
  return QQuickDesignerSupport::isValidWidth(item);
}

//  bool QQuickDesignerSupport::isValidHeight(QQuickItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickDesignerSupport13isValidHeightEP10QQuickItem(
    QQuickItem *item) {
  return QQuickDesignerSupport::isValidHeight(item);
}

//  void QQuickDesignerSupport::updateDirtyNode(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport15updateDirtyNodeEP10QQuickItem(
    QQuickItem *item) {
  QQuickDesignerSupport::updateDirtyNode(item);
}

//  void QQuickDesignerSupport::activateDesignerMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport20activateDesignerModeEv() {
  QQuickDesignerSupport::activateDesignerMode();
}

//  void QQuickDesignerSupport::disableComponentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport24disableComponentCompleteEv() {
  QQuickDesignerSupport::disableComponentComplete();
}

//  void QQuickDesignerSupport::enableComponentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport23enableComponentCompleteEv() {
  QQuickDesignerSupport::enableComponentComplete();
}

//  void QQuickDesignerSupport::polishItems(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickDesignerSupport11polishItemsEP12QQuickWindow(
    QQuickWindow *window) {
  QQuickDesignerSupport::polishItems(window);
}

#endif  // QT_CONFIG(quick_designer)
