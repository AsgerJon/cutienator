//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QNativeGestureEvent *QNativeGestureEvent::clone() const
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_ZNK19QNativeGestureEvent5cloneEv(
    const QNativeGestureEvent *self) {
  return self->clone();
}

//  QNativeGestureEvent::~QNativeGestureEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNativeGestureEventD1Ev(QNativeGestureEvent *self) {
  delete self;
}

//  QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
//      const QPointingDevice *dev, const QPointF &localPos, const QPointF
//      &scenePos, const QPointF &globalPos, qreal value, quint64 sequenceId,
//      quint64 intArgument)
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_ZN19QNativeGestureEventC1EN2Qt17NativeGestureTypeEPK15QPointingDeviceRK7QPointFS7_S7_dyy(
    Qt::NativeGestureType type,
    const QPointingDevice *dev,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    qreal value,
    quint64 sequenceId,
    quint64 intArgument) {
  return new QNativeGestureEvent(
      type,
      dev,
      *localPos,
      *scenePos,
      *globalPos,
      value,
      sequenceId,
      intArgument);
}

//  QNativeGestureEvent::QNativeGestureEvent(Qt::NativeGestureType type,
//      const QPointingDevice *dev, int fingerCount, const QPointF &localPos,
//      const QPointF &scenePos, const QPointF &globalPos, qreal value, const
//      QPointF &delta, quint64 sequenceId)
extern "C" Q_DECL_EXPORT
QNativeGestureEvent *ritual_ZN19QNativeGestureEventC1EN2Qt17NativeGestureTypeEPK15QPointingDeviceiRK7QPointFS7_S7_dS7_y(
    Qt::NativeGestureType type,
    const QPointingDevice *dev,
    int fingerCount,
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    qreal value,
    const QPointF *delta,
    quint64 sequenceId) {
  return new QNativeGestureEvent(
      type,
      dev,
      fingerCount,
      *localPos,
      *scenePos,
      *globalPos,
      value,
      *delta,
      sequenceId);
}

//  Qt::NativeGestureType QNativeGestureEvent::gestureType() const
extern "C" Q_DECL_EXPORT
Qt::NativeGestureType ritual_ZNK19QNativeGestureEvent11gestureTypeEv(
    const QNativeGestureEvent *self) {
  return self->gestureType();
}

//  int QNativeGestureEvent::fingerCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QNativeGestureEvent11fingerCountEv(
    const QNativeGestureEvent *self) {
  return self->fingerCount();
}

//  qreal QNativeGestureEvent::value() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QNativeGestureEvent5valueEv(
    const QNativeGestureEvent *self) {
  return self->value();
}

//  QPointF QNativeGestureEvent::delta() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent5deltaEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->delta());
}

//  const QPoint QNativeGestureEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QNativeGestureEvent3posEv(
    const QNativeGestureEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint QNativeGestureEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QNativeGestureEvent9globalPosEv(
    const QNativeGestureEvent *self) {
  return new QPoint(self->globalPos());
}

//  QPointF QNativeGestureEvent::localPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent8localPosEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->localPos());
}

//  QPointF QNativeGestureEvent::windowPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent9windowPosEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->windowPos());
}

//  QPointF QNativeGestureEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QNativeGestureEvent9screenPosEv(
    const QNativeGestureEvent *self) {
  return new QPointF(self->screenPos());
}
