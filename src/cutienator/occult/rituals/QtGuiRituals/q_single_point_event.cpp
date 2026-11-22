//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>

//  QSinglePointEvent *QSinglePointEvent::clone() const
extern "C" Q_DECL_EXPORT
QSinglePointEvent *ritual_ZNK17QSinglePointEvent5cloneEv(
    const QSinglePointEvent *self) {
  return self->clone();
}

//  QSinglePointEvent::~QSinglePointEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSinglePointEventD1Ev(QSinglePointEvent *self) {
  delete self;
}

//  Qt::MouseButton QSinglePointEvent::button() const
extern "C" Q_DECL_EXPORT
Qt::MouseButton ritual_ZNK17QSinglePointEvent6buttonEv(
    const QSinglePointEvent *self) {
  return self->button();
}

//  Qt::MouseButtons QSinglePointEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSinglePointEvent7buttonsEv(const QSinglePointEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  QPointF QSinglePointEvent::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSinglePointEvent8positionEv(
    const QSinglePointEvent *self) {
  return new QPointF(self->position());
}

//  QPointF QSinglePointEvent::scenePosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSinglePointEvent13scenePositionEv(
    const QSinglePointEvent *self) {
  return new QPointF(self->scenePosition());
}

//  QPointF QSinglePointEvent::globalPosition() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QSinglePointEvent14globalPositionEv(
    const QSinglePointEvent *self) {
  return new QPointF(self->globalPosition());
}

//  bool QSinglePointEvent::isBeginEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSinglePointEvent12isBeginEventEv(
    const QSinglePointEvent *self) {
  return self->isBeginEvent();
}

//  bool QSinglePointEvent::isUpdateEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSinglePointEvent13isUpdateEventEv(
    const QSinglePointEvent *self) {
  return self->isUpdateEvent();
}

//  bool QSinglePointEvent::isEndEvent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSinglePointEvent10isEndEventEv(
    const QSinglePointEvent *self) {
  return self->isEndEvent();
}

//  QObject *QSinglePointEvent::exclusivePointGrabber() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK17QSinglePointEvent21exclusivePointGrabberEv(
    const QSinglePointEvent *self) {
  return self->exclusivePointGrabber();
}

//  void QSinglePointEvent::setExclusivePointGrabber(QObject
//      *exclusiveGrabber)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSinglePointEvent24setExclusivePointGrabberEP7QObject(
    QSinglePointEvent *self,
    QObject *exclusiveGrabber) {
  self->setExclusivePointGrabber(exclusiveGrabber);
}
