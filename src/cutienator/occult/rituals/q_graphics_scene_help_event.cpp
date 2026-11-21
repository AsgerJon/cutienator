//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>

//  QGraphicsSceneHelpEvent::QGraphicsSceneHelpEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneHelpEvent *ritual_ZN23QGraphicsSceneHelpEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new QGraphicsSceneHelpEvent(type);
}

//  QGraphicsSceneHelpEvent::~QGraphicsSceneHelpEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneHelpEventD1Ev(QGraphicsSceneHelpEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneHelpEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QGraphicsSceneHelpEvent8scenePosEv(
    const QGraphicsSceneHelpEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneHelpEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneHelpEvent11setScenePosERK7QPointF(
    QGraphicsSceneHelpEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneHelpEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK23QGraphicsSceneHelpEvent9screenPosEv(
    const QGraphicsSceneHelpEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneHelpEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneHelpEvent12setScreenPosERK6QPoint(
    QGraphicsSceneHelpEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}
