//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickflickable_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickflickable_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>

//  QQuickFlickable *QQuickFlickablePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFlickable *ritual_ZN22QQuickFlickablePrivate6q_funcEv(
    QQuickFlickablePrivate *self) {
  return self->q_func();
}

//  const QQuickFlickable *QQuickFlickablePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFlickable *ritual_ZNK22QQuickFlickablePrivate6q_funcEv(
    const QQuickFlickablePrivate *self) {
  return self->q_func();
}

//  QQuickFlickablePrivate *QQuickFlickablePrivate::get(QQuickFlickable *o)
extern "C" Q_DECL_EXPORT
QQuickFlickablePrivate *ritual_ZN22QQuickFlickablePrivate3getEP15QQuickFlickable(
    QQuickFlickable *o) {
  return QQuickFlickablePrivate::get(o);
}

//  QQuickFlickablePrivate::QQuickFlickablePrivate()
extern "C" Q_DECL_EXPORT
QQuickFlickablePrivate *ritual_ZN22QQuickFlickablePrivateC1Ev() {
  return new QQuickFlickablePrivate();
}

//  void QQuickFlickablePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate4initEv(QQuickFlickablePrivate *self) {
  self->init();
}

//  bool QQuickFlickablePrivate::flickX(QEvent::Type eventType, qreal
//      velocity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickFlickablePrivate6flickXEN6QEvent4TypeEd(
    QQuickFlickablePrivate *self,
    QEvent::Type eventType,
    qreal velocity) {
  return self->flickX(eventType, velocity);
}

//  bool QQuickFlickablePrivate::flickY(QEvent::Type eventType, qreal
//      velocity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickFlickablePrivate6flickYEN6QEvent4TypeEd(
    QQuickFlickablePrivate *self,
    QEvent::Type eventType,
    qreal velocity) {
  return self->flickY(eventType, velocity);
}

//  bool QQuickFlickablePrivate::flick(AxisData &data, qreal minExtent, qreal
//      maxExtent, qreal vSize, QQuickTimeLineCallback::Callback
//      fixupCallback, QEvent::Type eventType, qreal velocity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickFlickablePrivate5flickERNS_8AxisDataEdddPFvPvEN6QEvent4TypeEd(
    QQuickFlickablePrivate *self,
    QQuickFlickablePrivate::AxisData *data,
    qreal minExtent,
    qreal maxExtent,
    qreal vSize,
    void *fixupCallback,
    QEvent::Type eventType,
    qreal velocity) {
  return self->flick(
      *data,
      minExtent,
      maxExtent,
      vSize,
      reinterpret_cast<QQuickTimeLineCallback::Callback>(fixupCallback),
      eventType,
      velocity);
}

//  void QQuickFlickablePrivate::flickingStarted(bool flickingH, bool
//      flickingV)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate15flickingStartedEbb(
    QQuickFlickablePrivate *self,
    bool flickingH,
    bool flickingV) {
  self->flickingStarted(flickingH, flickingV);
}

//  void QQuickFlickablePrivate::fixupX()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate6fixupXEv(
    QQuickFlickablePrivate *self) {
  self->fixupX();
}

//  void QQuickFlickablePrivate::fixupY()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate6fixupYEv(
    QQuickFlickablePrivate *self) {
  self->fixupY();
}

//  void QQuickFlickablePrivate::fixup(AxisData &data, qreal minExtent, qreal
//      maxExtent)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate5fixupERNS_8AxisDataEdd(
    QQuickFlickablePrivate *self,
    QQuickFlickablePrivate::AxisData *data,
    qreal minExtent,
    qreal maxExtent) {
  self->fixup(*data, minExtent, maxExtent);
}

//  void QQuickFlickablePrivate::adjustContentPos(AxisData &data, qreal
//      toPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate16adjustContentPosERNS_8AxisDataEd(
    QQuickFlickablePrivate *self,
    QQuickFlickablePrivate::AxisData *data,
    qreal toPos) {
  self->adjustContentPos(*data, toPos);
}

//  void QQuickFlickablePrivate::resetTimeline(AxisData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate13resetTimelineERNS_8AxisDataE(
    QQuickFlickablePrivate *self,
    QQuickFlickablePrivate::AxisData *data) {
  self->resetTimeline(*data);
}

//  void QQuickFlickablePrivate::clearTimeline()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate13clearTimelineEv(
    QQuickFlickablePrivate *self) {
  self->clearTimeline();
}

//  void QQuickFlickablePrivate::updateBeginningEnd()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate18updateBeginningEndEv(
    QQuickFlickablePrivate *self) {
  self->updateBeginningEnd();
}

//  bool QQuickFlickablePrivate::isInnermostPressDelay(QQuickItem *item)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickFlickablePrivate21isInnermostPressDelayEP10QQuickItem(
    const QQuickFlickablePrivate *self,
    QQuickItem *item) {
  return self->isInnermostPressDelay(item);
}

//  void QQuickFlickablePrivate::captureDelayedPress(QQuickItem *item,
//      QPointerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate19captureDelayedPressEP10QQuickItemP13QPointerEvent(
    QQuickFlickablePrivate *self,
    QQuickItem *item,
    QPointerEvent *event) {
  self->captureDelayedPress(item, event);
}

//  void QQuickFlickablePrivate::clearDelayedPress()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate17clearDelayedPressEv(
    QQuickFlickablePrivate *self) {
  self->clearDelayedPress();
}

//  void QQuickFlickablePrivate::replayDelayedPress()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate18replayDelayedPressEv(
    QQuickFlickablePrivate *self) {
  self->replayDelayedPress();
}

//  void QQuickFlickablePrivate::setViewportX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate12setViewportXEd(
    QQuickFlickablePrivate *self,
    qreal x) {
  self->setViewportX(x);
}

//  void QQuickFlickablePrivate::setViewportY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate12setViewportYEd(
    QQuickFlickablePrivate *self,
    qreal y) {
  self->setViewportY(y);
}

//  qreal QQuickFlickablePrivate::overShootDistance(qreal velocity) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickFlickablePrivate17overShootDistanceEd(
    const QQuickFlickablePrivate *self,
    qreal velocity) {
  return self->overShootDistance(velocity);
}

//  void QQuickFlickablePrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickFlickablePrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickFlickablePrivate::draggingStarting()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate16draggingStartingEv(
    QQuickFlickablePrivate *self) {
  self->draggingStarting();
}

//  void QQuickFlickablePrivate::draggingEnding()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate14draggingEndingEv(
    QQuickFlickablePrivate *self) {
  self->draggingEnding();
}

//  bool QQuickFlickablePrivate::isViewMoving() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickFlickablePrivate12isViewMovingEv(
    const QQuickFlickablePrivate *self) {
  return self->isViewMoving();
}

//  void QQuickFlickablePrivate::cancelInteraction()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate17cancelInteractionEv(
    QQuickFlickablePrivate *self) {
  self->cancelInteraction();
}

//  void QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate17addPointerHandlerEP20QQuickPointerHandler(
    QQuickFlickablePrivate *self,
    QQuickPointerHandler *h) {
  self->addPointerHandler(h);
}

//  bool QQuickFlickablePrivate::wantsPointerEvent(const QPointerEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerEvent(
    QQuickFlickablePrivate *self,
    const QPointerEvent *a0) {
  return self->wantsPointerEvent(a0);
}

//  void QQuickFlickablePrivate::fixupY_callback(void *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate15fixupY_callbackEPv(void *a0) {
  QQuickFlickablePrivate::fixupY_callback(a0);
}

//  void QQuickFlickablePrivate::fixupX_callback(void *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate15fixupX_callbackEPv(void *a0) {
  QQuickFlickablePrivate::fixupX_callback(a0);
}

//  void QQuickFlickablePrivate::updateVelocity()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate14updateVelocityEv(
    QQuickFlickablePrivate *self) {
  self->updateVelocity();
}

//  void QQuickFlickablePrivate::viewportAxisMoved(AxisData &data, qreal
//      minExtent, qreal maxExtent, QQuickTimeLineCallback::Callback
//      fixupCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate17viewportAxisMovedERNS_8AxisDataEddPFvPvE(
    QQuickFlickablePrivate *self,
    QQuickFlickablePrivate::AxisData *data,
    qreal minExtent,
    qreal maxExtent,
    void *fixupCallback) {
  self->viewportAxisMoved(
      *data,
      minExtent,
      maxExtent,
      reinterpret_cast<QQuickTimeLineCallback::Callback>(fixupCallback));
}

//  void QQuickFlickablePrivate::handlePressEvent(QPointerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate16handlePressEventEP13QPointerEvent(
    QQuickFlickablePrivate *self,
    QPointerEvent *a0) {
  self->handlePressEvent(a0);
}

//  void QQuickFlickablePrivate::handleMoveEvent(QPointerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate15handleMoveEventEP13QPointerEvent(
    QQuickFlickablePrivate *self,
    QPointerEvent *a0) {
  self->handleMoveEvent(a0);
}

//  void QQuickFlickablePrivate::handleReleaseEvent(QPointerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate18handleReleaseEventEP13QPointerEvent(
    QQuickFlickablePrivate *self,
    QPointerEvent *a0) {
  self->handleReleaseEvent(a0);
}

//  bool QQuickFlickablePrivate::buttonsAccepted(const QSinglePointEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickFlickablePrivate15buttonsAcceptedEPK17QSinglePointEvent(
    QQuickFlickablePrivate *self,
    const QSinglePointEvent *event) {
  return self->buttonsAccepted(event);
}

//  void QQuickFlickablePrivate::maybeBeginDrag(qint64 currentTimestamp,
//      const QPointF &pressPosn, Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate14maybeBeginDragExRK7QPointF6QFlagsIN2Qt11MouseButtonEE(
    QQuickFlickablePrivate *self,
    qint64 currentTimestamp,
    const QPointF *pressPosn,
    int buttons) {
  self->maybeBeginDrag(
      currentTimestamp,
      *pressPosn,
      QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  void QQuickFlickablePrivate::drag(qint64 currentTimestamp, QEvent::Type
//      eventType, const QPointF &localPos, const QVector2D &deltas, bool
//      overThreshold, bool momentum, bool velocitySensitiveOverBounds, const
//      QVector2D &velocity)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate4dragExN6QEvent4TypeERK7QPointFRK9QVector2DbbbS7_(
    QQuickFlickablePrivate *self,
    qint64 currentTimestamp,
    QEvent::Type eventType,
    const QPointF *localPos,
    const QVector2D *deltas,
    bool overThreshold,
    bool momentum,
    bool velocitySensitiveOverBounds,
    const QVector2D *velocity) {
  self->drag(
      currentTimestamp,
      eventType,
      *localPos,
      *deltas,
      overThreshold,
      momentum,
      velocitySensitiveOverBounds,
      *velocity);
}

//  QVector2D QQuickFlickablePrivate::firstPointLocalVelocity(QPointerEvent
//      *event)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN22QQuickFlickablePrivate23firstPointLocalVelocityEP13QPointerEvent(
    QQuickFlickablePrivate *self,
    QPointerEvent *event) {
  return new QVector2D(self->firstPointLocalVelocity(event));
}

//  qint64 QQuickFlickablePrivate::computeCurrentTime(QInputEvent *event)
//      const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QQuickFlickablePrivate18computeCurrentTimeEP11QInputEvent(
    const QQuickFlickablePrivate *self,
    QInputEvent *event) {
  return self->computeCurrentTime(event);
}

//  void QQuickFlickablePrivate::data_append(QQmlListProperty<QObject> *a0,
//      QObject *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate11data_appendEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *a0,
    QObject *a1) {
  QQuickFlickablePrivate::data_append(a0, a1);
}

//  qsizetype QQuickFlickablePrivate::data_count(QQmlListProperty<QObject>
//      *a0)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN22QQuickFlickablePrivate10data_countEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *a0) {
  return QQuickFlickablePrivate::data_count(a0);
}

//  QObject *QQuickFlickablePrivate::data_at(QQmlListProperty<QObject> *a0,
//      qsizetype a1)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN22QQuickFlickablePrivate7data_atEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *a0,
    qsizetype a1) {
  return QQuickFlickablePrivate::data_at(a0, a1);
}

//  void QQuickFlickablePrivate::data_clear(QQmlListProperty<QObject> *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFlickablePrivate10data_clearEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *a0) {
  QQuickFlickablePrivate::data_clear(a0);
}

//  void QQuickFlickablePrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickFlickablePrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickFlickablePrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickFlickablePrivate::itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickFlickablePrivate::addPointerHandler(QQuickPointerHandler *h)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickFlickablePrivate17addPointerHandlerEP20QQuickPointerHandler(
    QQuickFlickablePrivate *self,
    QQuickPointerHandler *h) {
  self->QQuickFlickablePrivate::addPointerHandler(h);
}

//  bool QQuickFlickablePrivate::wantsPointerEvent(const QPointerEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickFlickablePrivate17wantsPointerEventEPK13QPointerEvent(
    QQuickFlickablePrivate *self,
    const QPointerEvent *a0) {
  return self->QQuickFlickablePrivate::wantsPointerEvent(a0);
}
