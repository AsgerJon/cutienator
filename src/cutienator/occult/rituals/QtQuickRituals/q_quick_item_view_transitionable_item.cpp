//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  QQuickItemViewTransitionableItem::QQuickItemViewTransitionableItem(QQuick
//      Item *i)
extern "C" Q_DECL_EXPORT
QQuickItemViewTransitionableItem *ritual_ZN32QQuickItemViewTransitionableItemC1EP10QQuickItem(
    QQuickItem *i) {
  return new QQuickItemViewTransitionableItem(i);
}

//  QQuickItemViewTransitionableItem::~QQuickItemViewTransitionableItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItemD1Ev(
    QQuickItemViewTransitionableItem *self) {
  delete self;
}

//  qreal QQuickItemViewTransitionableItem::itemX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK32QQuickItemViewTransitionableItem5itemXEv(
    const QQuickItemViewTransitionableItem *self) {
  return self->itemX();
}

//  qreal QQuickItemViewTransitionableItem::itemY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK32QQuickItemViewTransitionableItem5itemYEv(
    const QQuickItemViewTransitionableItem *self) {
  return self->itemY();
}

//  void QQuickItemViewTransitionableItem::moveTo(const QPointF &pos, bool
//      immediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem6moveToERK7QPointFb(
    QQuickItemViewTransitionableItem *self,
    const QPointF *pos,
    bool immediate) {
  self->moveTo(*pos, immediate);
}

//  bool QQuickItemViewTransitionableItem::transitionScheduledOrRunning()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickItemViewTransitionableItem28transitionScheduledOrRunningEv(
    const QQuickItemViewTransitionableItem *self) {
  return self->transitionScheduledOrRunning();
}

//  bool QQuickItemViewTransitionableItem::transitionRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickItemViewTransitionableItem17transitionRunningEv(
    const QQuickItemViewTransitionableItem *self) {
  return self->transitionRunning();
}

//  bool QQuickItemViewTransitionableItem::isPendingRemoval() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickItemViewTransitionableItem16isPendingRemovalEv(
    const QQuickItemViewTransitionableItem *self) {
  return self->isPendingRemoval();
}

//  bool QQuickItemViewTransitionableItem::prepareTransition(QQuickItemViewTr
//      ansitioner *transitioner, int index, const QRectF &viewBounds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QQuickItemViewTransitionableItem17prepareTransitionEP26QQuickItemViewTransitioneriRK6QRectF(
    QQuickItemViewTransitionableItem *self,
    QQuickItemViewTransitioner *transitioner,
    int index,
    const QRectF *viewBounds) {
  return self->prepareTransition(transitioner, index, *viewBounds);
}

//  void QQuickItemViewTransitionableItem::startTransition(QQuickItemViewTran
//      sitioner *transitioner, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem15startTransitionEP26QQuickItemViewTransitioneri(
    QQuickItemViewTransitionableItem *self,
    QQuickItemViewTransitioner *transitioner,
    int index) {
  self->startTransition(transitioner, index);
}

//  void
//      QQuickItemViewTransitionableItem::completeTransition(QQuickTransition
//      *quickTransition)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem18completeTransitionEP16QQuickTransition(
    QQuickItemViewTransitionableItem *self,
    QQuickTransition *quickTransition) {
  self->completeTransition(quickTransition);
}

//  void QQuickItemViewTransitionableItem::setNextTransition(QQuickItemViewTr
//      ansitioner::TransitionType a0, bool isTargetItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem17setNextTransitionEN26QQuickItemViewTransitioner14TransitionTypeEb(
    QQuickItemViewTransitionableItem *self,
    QQuickItemViewTransitioner::TransitionType a0,
    bool isTargetItem) {
  self->setNextTransition(a0, isTargetItem);
}

//  bool QQuickItemViewTransitionableItem::transitionWillChangePosition()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QQuickItemViewTransitionableItem28transitionWillChangePositionEv(
    const QQuickItemViewTransitionableItem *self) {
  return self->transitionWillChangePosition();
}

//  void QQuickItemViewTransitionableItem::finishedTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem18finishedTransitionEv(
    QQuickItemViewTransitionableItem *self) {
  self->finishedTransition();
}

//  void QQuickItemViewTransitionableItem::resetNextTransitionPos()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem22resetNextTransitionPosEv(
    QQuickItemViewTransitionableItem *self) {
  self->resetNextTransitionPos();
}

//  void QQuickItemViewTransitionableItem::clearCurrentScheduledTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem31clearCurrentScheduledTransitionEv(
    QQuickItemViewTransitionableItem *self) {
  self->clearCurrentScheduledTransition();
}

//  void QQuickItemViewTransitionableItem::stopTransition()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickItemViewTransitionableItem14stopTransitionEv(
    QQuickItemViewTransitionableItem *self) {
  self->stopTransition();
}

#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_viewtransitions)
