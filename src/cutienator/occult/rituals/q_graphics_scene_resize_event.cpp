//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qsize.h>

//  QGraphicsSceneResizeEvent::QGraphicsSceneResizeEvent()
extern "C" Q_DECL_EXPORT
QGraphicsSceneResizeEvent *ritual_ZN25QGraphicsSceneResizeEventC1Ev() {
  return new QGraphicsSceneResizeEvent();
}

//  QGraphicsSceneResizeEvent::~QGraphicsSceneResizeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneResizeEventD1Ev(
    QGraphicsSceneResizeEvent *self) {
  delete self;
}

//  QSizeF QGraphicsSceneResizeEvent::oldSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK25QGraphicsSceneResizeEvent7oldSizeEv(
    const QGraphicsSceneResizeEvent *self) {
  return new QSizeF(self->oldSize());
}

//  void QGraphicsSceneResizeEvent::setOldSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneResizeEvent10setOldSizeERK6QSizeF(
    QGraphicsSceneResizeEvent *self,
    const QSizeF *size) {
  self->setOldSize(*size);
}

//  QSizeF QGraphicsSceneResizeEvent::newSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK25QGraphicsSceneResizeEvent7newSizeEv(
    const QGraphicsSceneResizeEvent *self) {
  return new QSizeF(self->newSize());
}

//  void QGraphicsSceneResizeEvent::setNewSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGraphicsSceneResizeEvent10setNewSizeERK6QSizeF(
    QGraphicsSceneResizeEvent *self,
    const QSizeF *size) {
  self->setNewSize(*size);
}
