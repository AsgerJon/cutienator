//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>

//  QGraphicsSceneWheelEvent::QGraphicsSceneWheelEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneWheelEvent *ritual_ZN24QGraphicsSceneWheelEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new QGraphicsSceneWheelEvent(type);
}

//  QGraphicsSceneWheelEvent::~QGraphicsSceneWheelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEventD1Ev(
    QGraphicsSceneWheelEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneWheelEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneWheelEvent3posEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneWheelEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent6setPosERK7QPointF(
    QGraphicsSceneWheelEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneWheelEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneWheelEvent8scenePosEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneWheelEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent11setScenePosERK7QPointF(
    QGraphicsSceneWheelEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneWheelEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneWheelEvent9screenPosEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneWheelEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent12setScreenPosERK6QPoint(
    QGraphicsSceneWheelEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  Qt::MouseButtons QGraphicsSceneWheelEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneWheelEvent7buttonsEv(
    const QGraphicsSceneWheelEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  void QGraphicsSceneWheelEvent::setButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent10setButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QGraphicsSceneWheelEvent *self,
    int buttons) {
  self->setButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  Qt::KeyboardModifiers QGraphicsSceneWheelEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneWheelEvent9modifiersEv(
    const QGraphicsSceneWheelEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneWheelEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneWheelEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  int QGraphicsSceneWheelEvent::delta() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneWheelEvent5deltaEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->delta();
}

//  void QGraphicsSceneWheelEvent::setDelta(int delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent8setDeltaEi(
    QGraphicsSceneWheelEvent *self,
    int delta) {
  self->setDelta(delta);
}

//  Qt::Orientation QGraphicsSceneWheelEvent::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK24QGraphicsSceneWheelEvent11orientationEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->orientation();
}

//  void QGraphicsSceneWheelEvent::setOrientation(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent14setOrientationEN2Qt11OrientationE(
    QGraphicsSceneWheelEvent *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::ScrollPhase QGraphicsSceneWheelEvent::phase() const
extern "C" Q_DECL_EXPORT
Qt::ScrollPhase ritual_ZNK24QGraphicsSceneWheelEvent5phaseEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->phase();
}

//  void QGraphicsSceneWheelEvent::setPhase(Qt::ScrollPhase scrollPhase)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent8setPhaseEN2Qt11ScrollPhaseE(
    QGraphicsSceneWheelEvent *self,
    Qt::ScrollPhase scrollPhase) {
  self->setPhase(scrollPhase);
}

//  QPoint QGraphicsSceneWheelEvent::pixelDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneWheelEvent10pixelDeltaEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPoint(self->pixelDelta());
}

//  void QGraphicsSceneWheelEvent::setPixelDelta(QPoint delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent13setPixelDeltaE6QPoint(
    QGraphicsSceneWheelEvent *self,
    const QPoint *delta) {
  self->setPixelDelta(*delta);
}

//  bool QGraphicsSceneWheelEvent::isInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QGraphicsSceneWheelEvent10isInvertedEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->isInverted();
}

//  void QGraphicsSceneWheelEvent::setInverted(bool inverted)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent11setInvertedEb(
    QGraphicsSceneWheelEvent *self,
    bool inverted) {
  self->setInverted(inverted);
}
