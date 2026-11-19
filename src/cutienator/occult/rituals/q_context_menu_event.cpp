//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QContextMenuEvent *QContextMenuEvent::clone() const
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_ZNK17QContextMenuEvent5cloneEv(
    const QContextMenuEvent *self) {
  return self->clone();
}

//  QContextMenuEvent::~QContextMenuEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QContextMenuEventD1Ev(QContextMenuEvent *self) {
  delete self;
}

//  QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos,
//      const QPoint &globalPos, Qt::KeyboardModifiers modifiers)
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_ZN17QContextMenuEventC1ENS_6ReasonERK6QPointS3_6QFlagsIN2Qt16KeyboardModifierEE(
    QContextMenuEvent::Reason reason,
    const QPoint *pos,
    const QPoint *globalPos,
    int modifiers) {
  return new QContextMenuEvent(
      reason,
      *pos,
      *globalPos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  QContextMenuEvent::QContextMenuEvent(Reason reason, const QPoint &pos)
extern "C" Q_DECL_EXPORT
QContextMenuEvent *ritual_ZN17QContextMenuEventC1ENS_6ReasonERK6QPoint(
    QContextMenuEvent::Reason reason,
    const QPoint *pos) {
  return new QContextMenuEvent(reason, *pos);
}

//  int QContextMenuEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent1xEv(const QContextMenuEvent *self) {
  return self->x();
}

//  int QContextMenuEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent1yEv(const QContextMenuEvent *self) {
  return self->y();
}

//  int QContextMenuEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent7globalXEv(const QContextMenuEvent *self) {
  return self->globalX();
}

//  int QContextMenuEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QContextMenuEvent7globalYEv(const QContextMenuEvent *self) {
  return self->globalY();
}

//  const QPoint &QContextMenuEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QContextMenuEvent3posEv(const QContextMenuEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint &QContextMenuEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QContextMenuEvent9globalPosEv(
    const QContextMenuEvent *self) {
  return new QPoint(self->globalPos());
}

//  Reason QContextMenuEvent::reason() const
extern "C" Q_DECL_EXPORT
QContextMenuEvent::Reason ritual_ZNK17QContextMenuEvent6reasonEv(
    const QContextMenuEvent *self) {
  return self->reason();
}
