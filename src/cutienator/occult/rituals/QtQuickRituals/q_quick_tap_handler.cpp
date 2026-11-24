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
