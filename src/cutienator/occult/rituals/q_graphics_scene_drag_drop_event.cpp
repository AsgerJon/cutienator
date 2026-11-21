//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>

//  QGraphicsSceneDragDropEvent::QGraphicsSceneDragDropEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneDragDropEvent *ritual_ZN27QGraphicsSceneDragDropEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new QGraphicsSceneDragDropEvent(type);
}

//  QGraphicsSceneDragDropEvent::~QGraphicsSceneDragDropEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEventD1Ev(
    QGraphicsSceneDragDropEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneDragDropEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK27QGraphicsSceneDragDropEvent3posEv(
    const QGraphicsSceneDragDropEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneDragDropEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent6setPosERK7QPointF(
    QGraphicsSceneDragDropEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneDragDropEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK27QGraphicsSceneDragDropEvent8scenePosEv(
    const QGraphicsSceneDragDropEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneDragDropEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent11setScenePosERK7QPointF(
    QGraphicsSceneDragDropEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneDragDropEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK27QGraphicsSceneDragDropEvent9screenPosEv(
    const QGraphicsSceneDragDropEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneDragDropEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent12setScreenPosERK6QPoint(
    QGraphicsSceneDragDropEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  Qt::MouseButtons QGraphicsSceneDragDropEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QGraphicsSceneDragDropEvent7buttonsEv(
    const QGraphicsSceneDragDropEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  void QGraphicsSceneDragDropEvent::setButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent10setButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QGraphicsSceneDragDropEvent *self,
    int buttons) {
  self->setButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  Qt::KeyboardModifiers QGraphicsSceneDragDropEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QGraphicsSceneDragDropEvent9modifiersEv(
    const QGraphicsSceneDragDropEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneDragDropEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneDragDropEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  Qt::DropActions QGraphicsSceneDragDropEvent::possibleActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK27QGraphicsSceneDragDropEvent15possibleActionsEv(
    const QGraphicsSceneDragDropEvent *self) {
  return static_cast<int>(self->possibleActions().toInt());
}

//  void QGraphicsSceneDragDropEvent::setPossibleActions(Qt::DropActions
//      actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent18setPossibleActionsE6QFlagsIN2Qt10DropActionEE(
    QGraphicsSceneDragDropEvent *self,
    int actions) {
  self->setPossibleActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  Qt::DropAction QGraphicsSceneDragDropEvent::proposedAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK27QGraphicsSceneDragDropEvent14proposedActionEv(
    const QGraphicsSceneDragDropEvent *self) {
  return self->proposedAction();
}

//  void QGraphicsSceneDragDropEvent::setProposedAction(Qt::DropAction
//      action)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent17setProposedActionEN2Qt10DropActionE(
    QGraphicsSceneDragDropEvent *self,
    Qt::DropAction action) {
  self->setProposedAction(action);
}

//  void QGraphicsSceneDragDropEvent::acceptProposedAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent20acceptProposedActionEv(
    QGraphicsSceneDragDropEvent *self) {
  self->acceptProposedAction();
}

//  Qt::DropAction QGraphicsSceneDragDropEvent::dropAction() const
extern "C" Q_DECL_EXPORT
Qt::DropAction ritual_ZNK27QGraphicsSceneDragDropEvent10dropActionEv(
    const QGraphicsSceneDragDropEvent *self) {
  return self->dropAction();
}

//  void QGraphicsSceneDragDropEvent::setDropAction(Qt::DropAction action)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent13setDropActionEN2Qt10DropActionE(
    QGraphicsSceneDragDropEvent *self,
    Qt::DropAction action) {
  self->setDropAction(action);
}

//  QWidget *QGraphicsSceneDragDropEvent::source() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK27QGraphicsSceneDragDropEvent6sourceEv(
    const QGraphicsSceneDragDropEvent *self) {
  return self->source();
}

//  void QGraphicsSceneDragDropEvent::setSource(QWidget *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent9setSourceEP7QWidget(
    QGraphicsSceneDragDropEvent *self,
    QWidget *source) {
  self->setSource(source);
}

//  const QMimeData *QGraphicsSceneDragDropEvent::mimeData() const
extern "C" Q_DECL_EXPORT
const QMimeData *ritual_ZNK27QGraphicsSceneDragDropEvent8mimeDataEv(
    const QGraphicsSceneDragDropEvent *self) {
  return self->mimeData();
}

//  void QGraphicsSceneDragDropEvent::setMimeData(const QMimeData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsSceneDragDropEvent11setMimeDataEPK9QMimeData(
    QGraphicsSceneDragDropEvent *self,
    const QMimeData *data) {
  self->setMimeData(data);
}
