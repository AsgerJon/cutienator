//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QScrollEvent *QScrollEvent::clone() const
extern "C" Q_DECL_EXPORT
QScrollEvent *ritual_ZNK12QScrollEvent5cloneEv(const QScrollEvent *self) {
  return self->clone();
}

//  QScrollEvent::~QScrollEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QScrollEventD1Ev(QScrollEvent *self) {
  delete self;
}

//  QScrollEvent::QScrollEvent(const QPointF &contentPos, const QPointF
//      &overshoot, ScrollState scrollState)
extern "C" Q_DECL_EXPORT
QScrollEvent *ritual_ZN12QScrollEventC1ERK7QPointFS2_NS_11ScrollStateE(
    const QPointF *contentPos,
    const QPointF *overshoot,
    QScrollEvent::ScrollState scrollState) {
  return new QScrollEvent(*contentPos, *overshoot, scrollState);
}

//  QPointF QScrollEvent::contentPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QScrollEvent10contentPosEv(const QScrollEvent *self) {
  return new QPointF(self->contentPos());
}

//  QPointF QScrollEvent::overshootDistance() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QScrollEvent17overshootDistanceEv(
    const QScrollEvent *self) {
  return new QPointF(self->overshootDistance());
}

//  ScrollState QScrollEvent::scrollState() const
extern "C" Q_DECL_EXPORT
QScrollEvent::ScrollState ritual_ZNK12QScrollEvent11scrollStateEv(
    const QScrollEvent *self) {
  return self->scrollState();
}
