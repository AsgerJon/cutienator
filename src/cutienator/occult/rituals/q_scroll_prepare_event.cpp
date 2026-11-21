//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>

//  QScrollPrepareEvent *QScrollPrepareEvent::clone() const
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_ZNK19QScrollPrepareEvent5cloneEv(
    const QScrollPrepareEvent *self) {
  return self->clone();
}

//  QScrollPrepareEvent::~QScrollPrepareEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEventD1Ev(QScrollPrepareEvent *self) {
  delete self;
}

//  QScrollPrepareEvent::QScrollPrepareEvent(const QPointF &startPos)
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_ZN19QScrollPrepareEventC1ERK7QPointF(
    const QPointF *startPos) {
  return new QScrollPrepareEvent(*startPos);
}

//  QPointF QScrollPrepareEvent::startPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QScrollPrepareEvent8startPosEv(
    const QScrollPrepareEvent *self) {
  return new QPointF(self->startPos());
}

//  QSizeF QScrollPrepareEvent::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QScrollPrepareEvent12viewportSizeEv(
    const QScrollPrepareEvent *self) {
  return new QSizeF(self->viewportSize());
}

//  QRectF QScrollPrepareEvent::contentPosRange() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QScrollPrepareEvent15contentPosRangeEv(
    const QScrollPrepareEvent *self) {
  return new QRectF(self->contentPosRange());
}

//  QPointF QScrollPrepareEvent::contentPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QScrollPrepareEvent10contentPosEv(
    const QScrollPrepareEvent *self) {
  return new QPointF(self->contentPos());
}

//  void QScrollPrepareEvent::setViewportSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEvent15setViewportSizeERK6QSizeF(
    QScrollPrepareEvent *self,
    const QSizeF *size) {
  self->setViewportSize(*size);
}

//  void QScrollPrepareEvent::setContentPosRange(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEvent18setContentPosRangeERK6QRectF(
    QScrollPrepareEvent *self,
    const QRectF *rect) {
  self->setContentPosRange(*rect);
}

//  void QScrollPrepareEvent::setContentPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEvent13setContentPosERK7QPointF(
    QScrollPrepareEvent *self,
    const QPointF *pos) {
  self->setContentPos(*pos);
}
