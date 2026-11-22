//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QHoverEvent *QHoverEvent::clone() const
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_ZNK11QHoverEvent5cloneEv(const QHoverEvent *self) {
  return self->clone();
}

//  QHoverEvent::~QHoverEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QHoverEventD1Ev(QHoverEvent *self) {
  delete self;
}

//  QHoverEvent::QHoverEvent(Type type, const QPointF &scenePos, const
//      QPointF &globalPos, const QPointF &oldPos, Qt::KeyboardModifiers
//      modifiers, const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_ZN11QHoverEventC1EN6QEvent4TypeERK7QPointFS4_S4_6QFlagsIN2Qt16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *scenePos,
    const QPointF *globalPos,
    const QPointF *oldPos,
    int modifiers,
    const QPointingDevice *device) {
  return new QHoverEvent(
      type,
      *scenePos,
      *globalPos,
      *oldPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QHoverEvent::QHoverEvent(Type type, const QPointF &pos, const QPointF
//      &oldPos, Qt::KeyboardModifiers modifiers, const QPointingDevice
//      *device)
extern "C" Q_DECL_EXPORT
QHoverEvent *ritual_ZN11QHoverEventC1EN6QEvent4TypeERK7QPointFS4_6QFlagsIN2Qt16KeyboardModifierEEPK15QPointingDevice(
    QEvent::Type type,
    const QPointF *pos,
    const QPointF *oldPos,
    int modifiers,
    const QPointingDevice *device) {
  return new QHoverEvent(
      type,
      *pos,
      *oldPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      device);
}

//  QPoint QHoverEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QHoverEvent3posEv(const QHoverEvent *self) {
  return new QPoint(self->pos());
}

//  QPointF QHoverEvent::posF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QHoverEvent4posFEv(const QHoverEvent *self) {
  return new QPointF(self->posF());
}

//  bool QHoverEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QHoverEvent13isUpdateEventEv(const QHoverEvent *self) {
  return self->isUpdateEvent();
}

//  QPoint QHoverEvent::oldPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK11QHoverEvent6oldPosEv(const QHoverEvent *self) {
  return new QPoint(self->oldPos());
}

//  QPointF QHoverEvent::oldPosF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QHoverEvent7oldPosFEv(const QHoverEvent *self) {
  return new QPointF(self->oldPosF());
}
