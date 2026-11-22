//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>

//  QGraphicsSceneMoveEvent::QGraphicsSceneMoveEvent()
extern "C" Q_DECL_EXPORT
QGraphicsSceneMoveEvent *ritual_ZN23QGraphicsSceneMoveEventC1Ev() {
  return new QGraphicsSceneMoveEvent();
}

//  QGraphicsSceneMoveEvent::~QGraphicsSceneMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneMoveEventD1Ev(QGraphicsSceneMoveEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneMoveEvent::oldPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QGraphicsSceneMoveEvent6oldPosEv(
    const QGraphicsSceneMoveEvent *self) {
  return new QPointF(self->oldPos());
}

//  void QGraphicsSceneMoveEvent::setOldPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneMoveEvent9setOldPosERK7QPointF(
    QGraphicsSceneMoveEvent *self,
    const QPointF *pos) {
  self->setOldPos(*pos);
}

//  QPointF QGraphicsSceneMoveEvent::newPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QGraphicsSceneMoveEvent6newPosEv(
    const QGraphicsSceneMoveEvent *self) {
  return new QPointF(self->newPos());
}

//  void QGraphicsSceneMoveEvent::setNewPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneMoveEvent9setNewPosERK7QPointF(
    QGraphicsSceneMoveEvent *self,
    const QPointF *pos) {
  self->setNewPos(*pos);
}
