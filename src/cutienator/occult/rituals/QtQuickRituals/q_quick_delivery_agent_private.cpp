//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtCore/qobject.h>
#include <QtQuick/qquickitem.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>

//  QQuickDeliveryAgent *QQuickDeliveryAgentPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgent *ritual_ZN26QQuickDeliveryAgentPrivate6q_funcEv(
    QQuickDeliveryAgentPrivate *self) {
  return self->q_func();
}

//  const QQuickDeliveryAgent *QQuickDeliveryAgentPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDeliveryAgent *ritual_ZNK26QQuickDeliveryAgentPrivate6q_funcEv(
    const QQuickDeliveryAgentPrivate *self) {
  return self->q_func();
}

//  QQuickDeliveryAgentPrivate::QQuickDeliveryAgentPrivate(QQuickItem *root)
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgentPrivate *ritual_ZN26QQuickDeliveryAgentPrivateC1EP10QQuickItem(
    QQuickItem *root) {
  return new QQuickDeliveryAgentPrivate(root);
}

//  QQuickDeliveryAgentPrivate::~QQuickDeliveryAgentPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivateD1Ev(
    QQuickDeliveryAgentPrivate *self) {
  delete self;
}

//  void QQuickDeliveryAgentPrivate::deliverKeyEvent(QKeyEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate15deliverKeyEventEP9QKeyEvent(
    QQuickDeliveryAgentPrivate *self,
    QKeyEvent *e) {
  self->deliverKeyEvent(e);
}

//  void QQuickDeliveryAgentPrivate::setFocusInScope(QQuickItem *scope,
//      QQuickItem *item, Qt::FocusReason reason, FocusOptions a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate15setFocusInScopeEP10QQuickItemS1_N2Qt11FocusReasonE6QFlagsINS_11FocusOptionEE(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *scope,
    QQuickItem *item,
    Qt::FocusReason reason,
    int a3) {
  self->setFocusInScope(
      scope,
      item,
      reason,
      QFlags<QQuickDeliveryAgentPrivate::FocusOption>::fromInt(a3));
}

//  void QQuickDeliveryAgentPrivate::clearFocusInScope(QQuickItem *scope,
//      QQuickItem *item, Qt::FocusReason reason, FocusOptions a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate17clearFocusInScopeEP10QQuickItemS1_N2Qt11FocusReasonE6QFlagsINS_11FocusOptionEE(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *scope,
    QQuickItem *item,
    Qt::FocusReason reason,
    int a3) {
  self->clearFocusInScope(
      scope,
      item,
      reason,
      QFlags<QQuickDeliveryAgentPrivate::FocusOption>::fromInt(a3));
}

//  void QQuickDeliveryAgentPrivate::clearFocusObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate16clearFocusObjectEv(
    QQuickDeliveryAgentPrivate *self) {
  self->clearFocusObject();
}

//  void QQuickDeliveryAgentPrivate::updateFocusItemTransform()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate24updateFocusItemTransformEv(
    QQuickDeliveryAgentPrivate *self) {
  self->updateFocusItemTransform();
}

//  QQuickItem *QQuickDeliveryAgentPrivate::focusTargetItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK26QQuickDeliveryAgentPrivate15focusTargetItemEv(
    const QQuickDeliveryAgentPrivate *self) {
  return self->focusTargetItem();
}

//  QQuickDeliveryAgent
//      *QQuickDeliveryAgentPrivate::currentOrItemDeliveryAgent(const
//      QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgent *ritual_ZN26QQuickDeliveryAgentPrivate26currentOrItemDeliveryAgentEPK10QQuickItem(
    const QQuickItem *item) {
  return QQuickDeliveryAgentPrivate::currentOrItemDeliveryAgent(item);
}

//  bool QQuickDeliveryAgentPrivate::isDeliveringTouchAsMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QQuickDeliveryAgentPrivate24isDeliveringTouchAsMouseEv(
    const QQuickDeliveryAgentPrivate *self) {
  return self->isDeliveringTouchAsMouse();
}

//  void QQuickDeliveryAgentPrivate::cancelTouchMouseSynthesis()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate25cancelTouchMouseSynthesisEv(
    QQuickDeliveryAgentPrivate *self) {
  self->cancelTouchMouseSynthesis();
}

//  bool QQuickDeliveryAgentPrivate::checkIfDoubleTapped(ulong
//      newPressEventTimestamp, const QPoint &newPressPos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate19checkIfDoubleTappedEmRK6QPoint(
    QQuickDeliveryAgentPrivate *self,
    ulong newPressEventTimestamp,
    const QPoint *newPressPos) {
  return self->checkIfDoubleTapped(newPressEventTimestamp, *newPressPos);
}

//  void QQuickDeliveryAgentPrivate::resetIfDoubleTapPrevented(const
//      QEventPoint &pressedPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate25resetIfDoubleTapPreventedERK11QEventPoint(
    QQuickDeliveryAgentPrivate *self,
    const QEventPoint *pressedPoint) {
  self->resetIfDoubleTapPrevented(*pressedPoint);
}

//  QPointingDevicePrivate::EventPointData
//      *QQuickDeliveryAgentPrivate::mousePointData()
extern "C" Q_DECL_EXPORT
QPointingDevicePrivate::EventPointData *ritual_ZN26QQuickDeliveryAgentPrivate14mousePointDataEv(
    QQuickDeliveryAgentPrivate *self) {
  return self->mousePointData();
}

//  QPointerEvent *QQuickDeliveryAgentPrivate::eventInDelivery() const
extern "C" Q_DECL_EXPORT
QPointerEvent *ritual_ZNK26QQuickDeliveryAgentPrivate15eventInDeliveryEv(
    const QQuickDeliveryAgentPrivate *self) {
  return self->eventInDelivery();
}

//  bool QQuickDeliveryAgentPrivate::deliverTouchAsMouse(QQuickItem *item,
//      QTouchEvent *pointerEvent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate19deliverTouchAsMouseEP10QQuickItemP11QTouchEvent(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *item,
    QTouchEvent *pointerEvent) {
  return self->deliverTouchAsMouse(item, pointerEvent);
}

//  void QQuickDeliveryAgentPrivate::translateTouchEvent(QTouchEvent
//      *touchEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate19translateTouchEventEP11QTouchEvent(
    QTouchEvent *touchEvent) {
  QQuickDeliveryAgentPrivate::translateTouchEvent(touchEvent);
}

//  void QQuickDeliveryAgentPrivate::removeGrabber(QQuickItem *grabber, bool
//      mouse, bool touch, bool cancel)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate13removeGrabberEP10QQuickItembbb(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *grabber,
    bool mouse,
    bool touch,
    bool cancel) {
  self->removeGrabber(grabber, mouse, touch, cancel);
}

//  void QQuickDeliveryAgentPrivate::clearGrabbers(QPointerEvent
//      *pointerEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate13clearGrabbersEP13QPointerEvent(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *pointerEvent) {
  self->clearGrabbers(pointerEvent);
}

//  void QQuickDeliveryAgentPrivate::onGrabChanged(QObject *grabber,
//      QPointingDevice::GrabTransition transition, const QPointerEvent
//      *event, const QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate13onGrabChangedEP7QObjectN15QPointingDevice14GrabTransitionEPK13QPointerEventRK11QEventPoint(
    QQuickDeliveryAgentPrivate *self,
    QObject *grabber,
    QPointingDevice::GrabTransition transition,
    const QPointerEvent *event,
    const QEventPoint *point) {
  self->onGrabChanged(grabber, transition, event, *point);
}

//  bool QQuickDeliveryAgentPrivate::sendFilteredMouseEvent(QEvent *event,
//      QQuickItem *receiver, QQuickItem *filteringParent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate22sendFilteredMouseEventEP6QEventP10QQuickItemS3_(
    QQuickDeliveryAgentPrivate *self,
    QEvent *event,
    QQuickItem *receiver,
    QQuickItem *filteringParent) {
  return self->sendFilteredMouseEvent(event, receiver, filteringParent);
}

//  bool QQuickDeliveryAgentPrivate::sendFilteredPointerEvent(QPointerEvent
//      *event, QQuickItem *receiver, QQuickItem *filteringParent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate24sendFilteredPointerEventEP13QPointerEventP10QQuickItemS3_(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *event,
    QQuickItem *receiver,
    QQuickItem *filteringParent) {
  return self->sendFilteredPointerEvent(event, receiver, filteringParent);
}

//  bool
//      QQuickDeliveryAgentPrivate::sendFilteredPointerEventImpl(QPointerEven
//      t *event, QQuickItem *receiver, QQuickItem *filteringParent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate28sendFilteredPointerEventImplEP13QPointerEventP10QQuickItemS3_(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *event,
    QQuickItem *receiver,
    QQuickItem *filteringParent) {
  return self->sendFilteredPointerEventImpl(
      event,
      receiver,
      filteringParent);
}

//  bool QQuickDeliveryAgentPrivate::deliverSinglePointEventUntilAccepted(QPo
//      interEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate36deliverSinglePointEventUntilAcceptedEP13QPointerEvent(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *a0) {
  return self->deliverSinglePointEventUntilAccepted(a0);
}

//  void QQuickDeliveryAgentPrivate::handleTouchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate16handleTouchEventEP11QTouchEvent(
    QQuickDeliveryAgentPrivate *self,
    QTouchEvent *a0) {
  self->handleTouchEvent(a0);
}

//  void QQuickDeliveryAgentPrivate::handleMouseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate16handleMouseEventEP11QMouseEvent(
    QQuickDeliveryAgentPrivate *self,
    QMouseEvent *a0) {
  self->handleMouseEvent(a0);
}

//  bool QQuickDeliveryAgentPrivate::compressTouchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate18compressTouchEventEP11QTouchEvent(
    QQuickDeliveryAgentPrivate *self,
    QTouchEvent *a0) {
  return self->compressTouchEvent(a0);
}

//  void QQuickDeliveryAgentPrivate::flushFrameSynchronousEvents(QQuickWindow
//      *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate27flushFrameSynchronousEventsEP12QQuickWindow(
    QQuickDeliveryAgentPrivate *self,
    QQuickWindow *win) {
  self->flushFrameSynchronousEvents(win);
}

//  void QQuickDeliveryAgentPrivate::deliverDelayedTouchEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate24deliverDelayedTouchEventEv(
    QQuickDeliveryAgentPrivate *self) {
  self->deliverDelayedTouchEvent();
}

//  void QQuickDeliveryAgentPrivate::handleWindowDeactivate(QQuickWindow
//      *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate22handleWindowDeactivateEP12QQuickWindow(
    QQuickDeliveryAgentPrivate *self,
    QQuickWindow *win) {
  self->handleWindowDeactivate(win);
}

//  void QQuickDeliveryAgentPrivate::handleWindowHidden(QQuickWindow *win)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate18handleWindowHiddenEP12QQuickWindow(
    QQuickDeliveryAgentPrivate *self,
    QQuickWindow *win) {
  self->handleWindowHidden(win);
}

//  bool QQuickDeliveryAgentPrivate::allUpdatedPointsAccepted(const
//      QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate24allUpdatedPointsAcceptedEPK13QPointerEvent(
    QQuickDeliveryAgentPrivate *self,
    const QPointerEvent *ev) {
  return self->allUpdatedPointsAccepted(ev);
}

//  void QQuickDeliveryAgentPrivate::localizePointerEvent(QPointerEvent *ev,
//      const QQuickItem *dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate20localizePointerEventEP13QPointerEventPK10QQuickItem(
    QPointerEvent *ev,
    const QQuickItem *dest) {
  QQuickDeliveryAgentPrivate::localizePointerEvent(ev, dest);
}

//  QList<QObject *>
//      QQuickDeliveryAgentPrivate::exclusiveGrabbers(QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
QList<QObject *> *ritual_ZN26QQuickDeliveryAgentPrivate17exclusiveGrabbersEP13QPointerEvent(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *ev) {
  return new QList<QObject *>(self->exclusiveGrabbers(ev));
}

//  bool QQuickDeliveryAgentPrivate::anyPointGrabbed(const QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate15anyPointGrabbedEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::anyPointGrabbed(ev);
}

//  bool QQuickDeliveryAgentPrivate::allPointsGrabbed(const QPointerEvent
//      *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate16allPointsGrabbedEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::allPointsGrabbed(ev);
}

//  bool QQuickDeliveryAgentPrivate::isMouseEvent(const QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate12isMouseEventEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isMouseEvent(ev);
}

//  bool QQuickDeliveryAgentPrivate::isMouseOrWheelEvent(const QPointerEvent
//      *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate19isMouseOrWheelEventEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isMouseOrWheelEvent(ev);
}

//  bool QQuickDeliveryAgentPrivate::isHoverEvent(const QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate12isHoverEventEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isHoverEvent(ev);
}

//  bool QQuickDeliveryAgentPrivate::isTouchEvent(const QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate12isTouchEventEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isTouchEvent(ev);
}

//  bool QQuickDeliveryAgentPrivate::isTabletEvent(const QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate13isTabletEventEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isTabletEvent(ev);
}

//  bool QQuickDeliveryAgentPrivate::isEventFromMouseOrTouchpad(const
//      QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate26isEventFromMouseOrTouchpadEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isEventFromMouseOrTouchpad(ev);
}

//  bool QQuickDeliveryAgentPrivate::isSynthMouse(const QPointerEvent *ev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate12isSynthMouseEPK13QPointerEvent(
    const QPointerEvent *ev) {
  return QQuickDeliveryAgentPrivate::isSynthMouse(ev);
}

//  bool QQuickDeliveryAgentPrivate::isWithinDoubleClickInterval(ulong
//      timeInterval)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate27isWithinDoubleClickIntervalEm(
    ulong timeInterval) {
  return QQuickDeliveryAgentPrivate::isWithinDoubleClickInterval(
      timeInterval);
}

//  bool QQuickDeliveryAgentPrivate::isWithinDoubleTapDistance(const QPoint
//      &distanceBetweenPresses)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate25isWithinDoubleTapDistanceERK6QPoint(
    const QPoint *distanceBetweenPresses) {
  return QQuickDeliveryAgentPrivate::isWithinDoubleTapDistance(
      *distanceBetweenPresses);
}

//  bool QQuickDeliveryAgentPrivate::isSinglePointDevice(const QInputDevice
//      *dev)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate19isSinglePointDeviceEPK12QInputDevice(
    const QInputDevice *dev) {
  return QQuickDeliveryAgentPrivate::isSinglePointDevice(dev);
}

//  QQuickPointingDeviceExtra *QQuickDeliveryAgentPrivate::deviceExtra(const
//      QInputDevice *device)
extern "C" Q_DECL_EXPORT
QQuickPointingDeviceExtra *ritual_ZN26QQuickDeliveryAgentPrivate11deviceExtraEPK12QInputDevice(
    const QInputDevice *device) {
  return QQuickDeliveryAgentPrivate::deviceExtra(device);
}

//  void QQuickDeliveryAgentPrivate::touchToMouseEvent(QEvent::Type type,
//      const QEventPoint &p, const QTouchEvent *touchEvent,
//      QMutableSinglePointEvent *mouseEvent)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate17touchToMouseEventEN6QEvent4TypeERK11QEventPointPK11QTouchEventP24QMutableSinglePointEvent(
    QQuickDeliveryAgentPrivate *self,
    QEvent::Type type,
    const QEventPoint *p,
    const QTouchEvent *touchEvent,
    QMutableSinglePointEvent *mouseEvent) {
  self->touchToMouseEvent(type, *p, touchEvent, mouseEvent);
}

//  void QQuickDeliveryAgentPrivate::ensureDeviceConnected(const
//      QPointingDevice *dev)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate21ensureDeviceConnectedEPK15QPointingDevice(
    QQuickDeliveryAgentPrivate *self,
    const QPointingDevice *dev) {
  self->ensureDeviceConnected(dev);
}

//  void QQuickDeliveryAgentPrivate::deliverPointerEvent(QPointerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate19deliverPointerEventEP13QPointerEvent(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *a0) {
  self->deliverPointerEvent(a0);
}

//  bool QQuickDeliveryAgentPrivate::deliverTouchCancelEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate23deliverTouchCancelEventEP11QTouchEvent(
    QQuickDeliveryAgentPrivate *self,
    QTouchEvent *a0) {
  return self->deliverTouchCancelEvent(a0);
}

//  bool QQuickDeliveryAgentPrivate::deliverPressOrReleaseEvent(QPointerEvent
//      *a0, bool handlersOnly)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate26deliverPressOrReleaseEventEP13QPointerEventb(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *a0,
    bool handlersOnly) {
  return self->deliverPressOrReleaseEvent(a0, handlersOnly);
}

//  void QQuickDeliveryAgentPrivate::deliverUpdatedPoints(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate20deliverUpdatedPointsEP13QPointerEvent(
    QQuickDeliveryAgentPrivate *self,
    QPointerEvent *event) {
  self->deliverUpdatedPoints(event);
}

//  void QQuickDeliveryAgentPrivate::deliverMatchingPointsToItem(QQuickItem
//      *item, bool isGrabber, QPointerEvent *pointerEvent, bool
//      handlersOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate27deliverMatchingPointsToItemEP10QQuickItembP13QPointerEventb(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *item,
    bool isGrabber,
    QPointerEvent *pointerEvent,
    bool handlersOnly) {
  self->deliverMatchingPointsToItem(
      item,
      isGrabber,
      pointerEvent,
      handlersOnly);
}

//  QList<QQuickItem *> QQuickDeliveryAgentPrivate::pointerTargets(QQuickItem
//      *a0, const QPointerEvent *event, const QEventPoint &point, bool
//      checkMouseButtons, bool checkAcceptsTouch) const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK26QQuickDeliveryAgentPrivate14pointerTargetsEP10QQuickItemPK13QPointerEventRK11QEventPointbb(
    const QQuickDeliveryAgentPrivate *self,
    QQuickItem *a0,
    const QPointerEvent *event,
    const QEventPoint *point,
    bool checkMouseButtons,
    bool checkAcceptsTouch) {
  return new QList<QQuickItem *>(
      self->pointerTargets(
          a0,
          event,
          *point,
          checkMouseButtons,
          checkAcceptsTouch));
}

//  QList<QQuickItem *> QQuickDeliveryAgentPrivate::mergePointerTargets(const
//      QList<QQuickItem *> &list1, const QList<QQuickItem *> &list2) const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK26QQuickDeliveryAgentPrivate19mergePointerTargetsERK5QListIP10QQuickItemES5_(
    const QQuickDeliveryAgentPrivate *self,
    const QList<QQuickItem *> *list1,
    const QList<QQuickItem *> *list2) {
  return new QList<QQuickItem *>(self->mergePointerTargets(*list1, *list2));
}

//  bool QQuickDeliveryAgentPrivate::deliverHoverEvent(const QPointF
//      &scenePos, const QPointF &lastScenePos, Qt::KeyboardModifiers
//      modifiers, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate17deliverHoverEventERK7QPointFS2_6QFlagsIN2Qt16KeyboardModifierEEm(
    QQuickDeliveryAgentPrivate *self,
    const QPointF *scenePos,
    const QPointF *lastScenePos,
    int modifiers,
    ulong timestamp) {
  return self->deliverHoverEvent(
      *scenePos,
      *lastScenePos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      timestamp);
}

//  bool QQuickDeliveryAgentPrivate::deliverHoverEventRecursive(QQuickItem
//      *a0, const QPointF &localPos, const QPointF &scenePos, const QPointF
//      &lastScenePos, const QPointF &globalPos, Qt::KeyboardModifiers
//      modifiers, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate26deliverHoverEventRecursiveEP10QQuickItemRK7QPointFS4_S4_S4_6QFlagsIN2Qt16KeyboardModifierEEm(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *a0,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *lastScenePos,
    const QPointF *globalPos,
    int modifiers,
    ulong timestamp) {
  return self->deliverHoverEventRecursive(
      a0,
      *localPos,
      *scenePos,
      *lastScenePos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      timestamp);
}

//  bool QQuickDeliveryAgentPrivate::deliverHoverEventToItem(QQuickItem
//      *item, const QPointF &localPos, const QPointF &scenePos, const
//      QPointF &lastScenePos, const QPointF &globalPos,
//      Qt::KeyboardModifiers modifiers, ulong timestamp, HoverChange
//      hoverChange)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate23deliverHoverEventToItemEP10QQuickItemRK7QPointFS4_S4_S4_6QFlagsIN2Qt16KeyboardModifierEEmNS_11HoverChangeE(
    QQuickDeliveryAgentPrivate *self,
    QQuickItem *item,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *lastScenePos,
    const QPointF *globalPos,
    int modifiers,
    ulong timestamp,
    QQuickDeliveryAgentPrivate::HoverChange hoverChange) {
  return self->deliverHoverEventToItem(
      item,
      *localPos,
      *scenePos,
      *lastScenePos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      timestamp,
      hoverChange);
}

//  bool QQuickDeliveryAgentPrivate::sendHoverEvent(QEvent::Type a0,
//      QQuickItem *a1, const QPointF &localPos, const QPointF &scenePos,
//      const QPointF &lastScenePos, const QPointF &globalPos,
//      Qt::KeyboardModifiers modifiers, ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate14sendHoverEventEN6QEvent4TypeEP10QQuickItemRK7QPointFS6_S6_S6_6QFlagsIN2Qt16KeyboardModifierEEm(
    QQuickDeliveryAgentPrivate *self,
    QEvent::Type a0,
    QQuickItem *a1,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *lastScenePos,
    const QPointF *globalPos,
    int modifiers,
    ulong timestamp) {
  return self->sendHoverEvent(
      a0,
      a1,
      *localPos,
      *scenePos,
      *lastScenePos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      timestamp);
}

//  bool QQuickDeliveryAgentPrivate::clearHover(ulong timestamp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate10clearHoverEm(
    QQuickDeliveryAgentPrivate *self,
    ulong timestamp) {
  return self->clearHover(timestamp);
}

#if QT_CONFIG(quick_draganddrop)
//  void QQuickDeliveryAgentPrivate::deliverDragEvent(QQuickDragGrabber *a0,
//      QEvent *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate16deliverDragEventEP17QQuickDragGrabberP6QEvent(
    QQuickDeliveryAgentPrivate *self,
    QQuickDragGrabber *a0,
    QEvent *a1) {
  self->deliverDragEvent(a0, a1);
}
#endif  // QT_CONFIG(quick_draganddrop)

//  bool QQuickDeliveryAgentPrivate::dragOverThreshold(qreal d, Qt::Axis
//      axis, QMouseEvent *event, int startDragThreshold)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate17dragOverThresholdEdN2Qt4AxisEP11QMouseEventi(
    qreal d,
    Qt::Axis axis,
    QMouseEvent *event,
    int startDragThreshold) {
  return QQuickDeliveryAgentPrivate::dragOverThreshold(
      d,
      axis,
      event,
      startDragThreshold);
}

//  bool QQuickDeliveryAgentPrivate::dragOverThreshold(qreal d, Qt::Axis
//      axis, const QEventPoint &tp, int startDragThreshold)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate17dragOverThresholdEdN2Qt4AxisERK11QEventPointi(
    qreal d,
    Qt::Axis axis,
    const QEventPoint *tp,
    int startDragThreshold) {
  return QQuickDeliveryAgentPrivate::dragOverThreshold(
      d,
      axis,
      *tp,
      startDragThreshold);
}

//  bool QQuickDeliveryAgentPrivate::dragOverThreshold(QVector2D delta)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QQuickDeliveryAgentPrivate17dragOverThresholdE9QVector2D(
    const QVector2D *delta) {
  return QQuickDeliveryAgentPrivate::dragOverThreshold(*delta);
}

//  QList<QQuickItem *>
//      QQuickDeliveryAgentPrivate::contextMenuTargets(QQuickItem *item,
//      const QContextMenuEvent *event) const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK26QQuickDeliveryAgentPrivate18contextMenuTargetsEP10QQuickItemPK17QContextMenuEvent(
    const QQuickDeliveryAgentPrivate *self,
    QQuickItem *item,
    const QContextMenuEvent *event) {
  return new QList<QQuickItem *>(self->contextMenuTargets(item, event));
}

//  void
//      QQuickDeliveryAgentPrivate::deliverContextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQuickDeliveryAgentPrivate23deliverContextMenuEventEP17QContextMenuEvent(
    QQuickDeliveryAgentPrivate *self,
    QContextMenuEvent *event) {
  self->deliverContextMenuEvent(event);
}
