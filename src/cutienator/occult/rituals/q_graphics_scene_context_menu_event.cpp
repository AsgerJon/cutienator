//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>

//  QGraphicsSceneContextMenuEvent::QGraphicsSceneContextMenuEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneContextMenuEvent *ritual_ZN30QGraphicsSceneContextMenuEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new QGraphicsSceneContextMenuEvent(type);
}

//  QGraphicsSceneContextMenuEvent::~QGraphicsSceneContextMenuEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEventD1Ev(
    QGraphicsSceneContextMenuEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneContextMenuEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK30QGraphicsSceneContextMenuEvent3posEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneContextMenuEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent6setPosERK7QPointF(
    QGraphicsSceneContextMenuEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneContextMenuEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK30QGraphicsSceneContextMenuEvent8scenePosEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneContextMenuEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent11setScenePosERK7QPointF(
    QGraphicsSceneContextMenuEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneContextMenuEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK30QGraphicsSceneContextMenuEvent9screenPosEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneContextMenuEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent12setScreenPosERK6QPoint(
    QGraphicsSceneContextMenuEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  Qt::KeyboardModifiers QGraphicsSceneContextMenuEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QGraphicsSceneContextMenuEvent9modifiersEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneContextMenuEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneContextMenuEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  Reason QGraphicsSceneContextMenuEvent::reason() const
extern "C" Q_DECL_EXPORT
QGraphicsSceneContextMenuEvent::Reason ritual_ZNK30QGraphicsSceneContextMenuEvent6reasonEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return self->reason();
}

//  void QGraphicsSceneContextMenuEvent::setReason(Reason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent9setReasonENS_6ReasonE(
    QGraphicsSceneContextMenuEvent *self,
    QGraphicsSceneContextMenuEvent::Reason reason) {
  self->setReason(reason);
}
