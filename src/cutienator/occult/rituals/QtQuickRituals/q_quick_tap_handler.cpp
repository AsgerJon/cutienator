//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktaphandler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktaphandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qeventpoint.h>

//  Only a class built on QQuickTapHandler may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTapHandler : QQuickTapHandler {
  using QQuickTapHandler::timerEvent;
  using QQuickTapHandler::wantsEventPoint;
};

//  const QMetaObject *QQuickTapHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickTapHandler10metaObjectEv(
    const QQuickTapHandler *self) {
  return self->metaObject();
}

//  void *QQuickTapHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuickTapHandler11qt_metacastEPKc(
    QQuickTapHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTapHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuickTapHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTapHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTapHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickTapHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTapHandler::tr(s, c, n));
}

//  QQuickTapHandler::QQuickTapHandler(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTapHandler *ritual_ZN16QQuickTapHandlerC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickTapHandler(parent);
}

//  bool QQuickTapHandler::isPressed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickTapHandler9isPressedEv(const QQuickTapHandler *self) {
  return self->isPressed();
}

//  int QQuickTapHandler::tapCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickTapHandler8tapCountEv(const QQuickTapHandler *self) {
  return self->tapCount();
}

//  qreal QQuickTapHandler::timeHeld() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTapHandler8timeHeldEv(const QQuickTapHandler *self) {
  return self->timeHeld();
}

//  qreal QQuickTapHandler::longPressThreshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QQuickTapHandler18longPressThresholdEv(
    const QQuickTapHandler *self) {
  return self->longPressThreshold();
}

//  void QQuickTapHandler::setLongPressThreshold(qreal longPressThreshold)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler21setLongPressThresholdEd(
    QQuickTapHandler *self,
    qreal longPressThreshold) {
  self->setLongPressThreshold(longPressThreshold);
}

//  void QQuickTapHandler::resetLongPressThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler23resetLongPressThresholdEv(
    QQuickTapHandler *self) {
  self->resetLongPressThreshold();
}

//  GesturePolicy QQuickTapHandler::gesturePolicy() const
extern "C" Q_DECL_EXPORT
QQuickTapHandler::GesturePolicy ritual_ZNK16QQuickTapHandler13gesturePolicyEv(
    const QQuickTapHandler *self) {
  return self->gesturePolicy();
}

//  void QQuickTapHandler::setGesturePolicy(GesturePolicy gesturePolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler16setGesturePolicyENS_13GesturePolicyE(
    QQuickTapHandler *self,
    QQuickTapHandler::GesturePolicy gesturePolicy) {
  self->setGesturePolicy(gesturePolicy);
}

//  QQuickTapHandler::ExclusiveSignals QQuickTapHandler::exclusiveSignals()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuickTapHandler16exclusiveSignalsEv(
    const QQuickTapHandler *self) {
  return static_cast<int>(self->exclusiveSignals().toInt());
}

//  void
//      QQuickTapHandler::setExclusiveSignals(QQuickTapHandler::ExclusiveSign
//      als newexclusiveSignals)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler19setExclusiveSignalsE6QFlagsINS_15ExclusiveSignalEE(
    QQuickTapHandler *self,
    int newexclusiveSignals) {
  self->setExclusiveSignals(
      QFlags<QQuickTapHandler::ExclusiveSignal>::fromInt(newexclusiveSignals));
}

//  void QQuickTapHandler::pressedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler14pressedChangedEv(QQuickTapHandler *self) {
  self->pressedChanged();
}

//  void QQuickTapHandler::tapCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler15tapCountChangedEv(QQuickTapHandler *self) {
  self->tapCountChanged();
}

//  void QQuickTapHandler::timeHeldChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler15timeHeldChangedEv(QQuickTapHandler *self) {
  self->timeHeldChanged();
}

//  void QQuickTapHandler::longPressThresholdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler25longPressThresholdChangedEv(
    QQuickTapHandler *self) {
  self->longPressThresholdChanged();
}

//  void QQuickTapHandler::gesturePolicyChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler20gesturePolicyChangedEv(
    QQuickTapHandler *self) {
  self->gesturePolicyChanged();
}

//  void QQuickTapHandler::exclusiveSignalsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler23exclusiveSignalsChangedEv(
    QQuickTapHandler *self) {
  self->exclusiveSignalsChanged();
}

//  void QQuickTapHandler::tapped(QEventPoint eventPoint, Qt::MouseButton a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler6tappedE11QEventPointN2Qt11MouseButtonE(
    QQuickTapHandler *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton a1) {
  self->tapped(*eventPoint, a1);
}

//  void QQuickTapHandler::singleTapped(QEventPoint eventPoint,
//      Qt::MouseButton a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler12singleTappedE11QEventPointN2Qt11MouseButtonE(
    QQuickTapHandler *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton a1) {
  self->singleTapped(*eventPoint, a1);
}

//  void QQuickTapHandler::doubleTapped(QEventPoint eventPoint,
//      Qt::MouseButton a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler12doubleTappedE11QEventPointN2Qt11MouseButtonE(
    QQuickTapHandler *self,
    const QEventPoint *eventPoint,
    Qt::MouseButton a1) {
  self->doubleTapped(*eventPoint, a1);
}

//  void QQuickTapHandler::longPressed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler11longPressedEv(QQuickTapHandler *self) {
  self->longPressed();
}

//  void QQuickTapHandler::onGrabChanged(QQuickPointerHandler *grabber,
//      QPointingDevice::GrabTransition transition, QPointerEvent *ev,
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler13onGrabChangedEP20QQuickPointerHandlerN15QPointingDevice14GrabTransitionEP13QPointerEventR11QEventPoint(
    QQuickTapHandler *self,
    QQuickPointerHandler *grabber,
    QPointingDevice::GrabTransition transition,
    QPointerEvent *ev,
    QEventPoint *point) {
  self->onGrabChanged(grabber, transition, ev, *point);
}

//  void QQuickTapHandler::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler10timerEventEP11QTimerEvent(
    QQuickTapHandler *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  bool QQuickTapHandler::wantsEventPoint(const QPointerEvent *event, const
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuickTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickTapHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->wantsEventPoint(event, *point);
}

//  void QQuickTapHandler::handleEventPoint(QPointerEvent *event, QEventPoint
//      &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler16handleEventPointEP13QPointerEventR11QEventPoint(
    QQuickTapHandler *self,
    QPointerEvent *event,
    QEventPoint *point) {
  self->handleEventPoint(event, *point);
}

//  void QQuickTapHandler::setPressed(bool press, bool cancel, QPointerEvent
//      *event, QEventPoint &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler10setPressedEbbP13QPointerEventR11QEventPoint(
    QQuickTapHandler *self,
    bool press,
    bool cancel,
    QPointerEvent *event,
    QEventPoint *point) {
  self->setPressed(press, cancel, event, *point);
}

//  void QQuickTapHandler::connectPreRenderSignal(bool conn)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler22connectPreRenderSignalEb(
    QQuickTapHandler *self,
    bool conn) {
  self->connectPreRenderSignal(conn);
}

//  void QQuickTapHandler::updateTimeHeld()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickTapHandler14updateTimeHeldEv(QQuickTapHandler *self) {
  self->updateTimeHeld();
}

//  void QQuickTapHandler::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickTapHandler10timerEventEP11QTimerEvent(
    QQuickTapHandler *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickTapHandler *>(self)->OwnQQuickTapHandler::timerEvent(
      event);
}

//  bool QQuickTapHandler::wantsEventPoint(const QPointerEvent *event, const
//      QEventPoint &point)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuickTapHandler15wantsEventPointEPK13QPointerEventRK11QEventPoint(
    QQuickTapHandler *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return static_cast<OwnQQuickTapHandler *>(self)->OwnQQuickTapHandler::wantsEventPoint(
      event,
      *point);
}
