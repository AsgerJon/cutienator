//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QEnterEvent *QEnterEvent::clone() const
extern "C" Q_DECL_EXPORT
QEnterEvent *ritual_ZNK11QEnterEvent5cloneEv(const QEnterEvent *self) {
  return self->clone();
}

//  QEnterEvent::~QEnterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QEnterEventD1Ev(QEnterEvent *self) {
  delete self;
}

//  QEnterEvent::QEnterEvent(const QPointF &localPos, const QPointF
//      &scenePos, const QPointF &globalPos, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QEnterEvent *ritual_ZN11QEnterEventC1ERK7QPointFS2_S2_PK15QPointingDevice(
    const QPointF *localPos,
    const QPointF *scenePos,
    const QPointF *globalPos,
    const QPointingDevice *device) {
  return new QEnterEvent(*localPos, *scenePos, *globalPos, device);
}

//  QPoint QEnterEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QEnterEvent3posEv(const QEnterEvent *self) {
  return new QPoint(self->pos());
}

//  QPoint QEnterEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QEnterEvent9globalPosEv(const QEnterEvent *self) {
  return new QPoint(self->globalPos());
}

//  int QEnterEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent1xEv(const QEnterEvent *self) {
  return self->x();
}

//  int QEnterEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent1yEv(const QEnterEvent *self) {
  return self->y();
}

//  int QEnterEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent7globalXEv(const QEnterEvent *self) {
  return self->globalX();
}

//  int QEnterEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QEnterEvent7globalYEv(const QEnterEvent *self) {
  return self->globalY();
}

//  QPointF QEnterEvent::localPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEnterEvent8localPosEv(const QEnterEvent *self) {
  return new QPointF(self->localPos());
}

//  QPointF QEnterEvent::windowPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEnterEvent9windowPosEv(const QEnterEvent *self) {
  return new QPointF(self->windowPos());
}

//  QPointF QEnterEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QEnterEvent9screenPosEv(const QEnterEvent *self) {
  return new QPointF(self->screenPos());
}
