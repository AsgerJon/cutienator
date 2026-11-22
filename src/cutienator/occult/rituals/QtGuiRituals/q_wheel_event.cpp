//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QWheelEvent *QWheelEvent::clone() const
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_ZNK11QWheelEvent5cloneEv(const QWheelEvent *self) {
  return self->clone();
}

//  QWheelEvent::~QWheelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QWheelEventD1Ev(QWheelEvent *self) {
  delete self;
}

//  QWheelEvent::QWheelEvent(const QPointF &pos, const QPointF &globalPos,
//      QPoint pixelDelta, QPoint angleDelta, Qt::MouseButtons buttons,
//      Qt::KeyboardModifiers modifiers, Qt::ScrollPhase phase, bool
//      inverted, Qt::MouseEventSource source, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QWheelEvent *ritual_ZN11QWheelEventC1ERK7QPointFS2_6QPointS3_6QFlagsIN2Qt11MouseButtonEES4_INS5_16KeyboardModifierEENS5_11ScrollPhaseEbNS5_16MouseEventSourceEPK15QPointingDevice(
    const QPointF *pos,
    const QPointF *globalPos,
    const QPoint *pixelDelta,
    const QPoint *angleDelta,
    int buttons,
    int modifiers,
    Qt::ScrollPhase phase,
    bool inverted,
    Qt::MouseEventSource source,
    const QPointingDevice *device) {
  return new QWheelEvent(
      *pos,
      *globalPos,
      *pixelDelta,
      *angleDelta,
      QFlags<Qt::MouseButton>::fromInt(buttons),
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      phase,
      inverted,
      source,
      device);
}

//  QPoint QWheelEvent::pixelDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QWheelEvent10pixelDeltaEv(const QWheelEvent *self) {
  return new QPoint(self->pixelDelta());
}

//  QPoint QWheelEvent::angleDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QWheelEvent10angleDeltaEv(const QWheelEvent *self) {
  return new QPoint(self->angleDelta());
}

//  Qt::ScrollPhase QWheelEvent::phase() const
extern "C" Q_DECL_EXPORT
Qt::ScrollPhase ritual_ZNK11QWheelEvent5phaseEv(const QWheelEvent *self) {
  return self->phase();
}

//  bool QWheelEvent::inverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent8invertedEv(const QWheelEvent *self) {
  return self->inverted();
}

//  bool QWheelEvent::isInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent10isInvertedEv(const QWheelEvent *self) {
  return self->isInverted();
}

//  bool QWheelEvent::hasPixelDelta() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent13hasPixelDeltaEv(const QWheelEvent *self) {
  return self->hasPixelDelta();
}

//  bool QWheelEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent12isBeginEventEv(const QWheelEvent *self) {
  return self->isBeginEvent();
}

//  bool QWheelEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent13isUpdateEventEv(const QWheelEvent *self) {
  return self->isUpdateEvent();
}

//  bool QWheelEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QWheelEvent10isEndEventEv(const QWheelEvent *self) {
  return self->isEndEvent();
}

//  Qt::MouseEventSource QWheelEvent::source() const
extern "C" Q_DECL_EXPORT
Qt::MouseEventSource ritual_ZNK11QWheelEvent6sourceEv(
    const QWheelEvent *self) {
  return self->source();
}
