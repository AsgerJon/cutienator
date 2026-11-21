//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QMoveEvent *QMoveEvent::clone() const
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_ZNK10QMoveEvent5cloneEv(const QMoveEvent *self) {
  return self->clone();
}

//  QMoveEvent::~QMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMoveEventD1Ev(QMoveEvent *self) {
  delete self;
}

//  QMoveEvent::QMoveEvent(const QPoint &pos, const QPoint &oldPos)
extern "C" Q_DECL_EXPORT
QMoveEvent *ritual_ZN10QMoveEventC1ERK6QPointS2_(
    const QPoint *pos,
    const QPoint *oldPos) {
  return new QMoveEvent(*pos, *oldPos);
}

//  const QPoint &QMoveEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QMoveEvent3posEv(const QMoveEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint &QMoveEvent::oldPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QMoveEvent6oldPosEv(const QMoveEvent *self) {
  return new QPoint(self->oldPos());
}
