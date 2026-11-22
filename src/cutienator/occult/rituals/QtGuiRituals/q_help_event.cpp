//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QHelpEvent *QHelpEvent::clone() const
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_ZNK10QHelpEvent5cloneEv(const QHelpEvent *self) {
  return self->clone();
}

//  QHelpEvent::~QHelpEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHelpEventD1Ev(QHelpEvent *self) {
  delete self;
}

//  QHelpEvent::QHelpEvent(Type type, const QPoint &pos, const QPoint
//      &globalPos)
extern "C" Q_DECL_EXPORT
QHelpEvent *ritual_ZN10QHelpEventC1EN6QEvent4TypeERK6QPointS4_(
    QEvent::Type type,
    const QPoint *pos,
    const QPoint *globalPos) {
  return new QHelpEvent(type, *pos, *globalPos);
}

//  int QHelpEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent1xEv(const QHelpEvent *self) {
  return self->x();
}

//  int QHelpEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent1yEv(const QHelpEvent *self) {
  return self->y();
}

//  int QHelpEvent::globalX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent7globalXEv(const QHelpEvent *self) {
  return self->globalX();
}

//  int QHelpEvent::globalY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QHelpEvent7globalYEv(const QHelpEvent *self) {
  return self->globalY();
}

//  const QPoint &QHelpEvent::pos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QHelpEvent3posEv(const QHelpEvent *self) {
  return new QPoint(self->pos());
}

//  const QPoint &QHelpEvent::globalPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QHelpEvent9globalPosEv(const QHelpEvent *self) {
  return new QPoint(self->globalPos());
}
