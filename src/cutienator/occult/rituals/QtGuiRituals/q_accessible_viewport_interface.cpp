//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>

//  QAccessibleViewportInterface::~QAccessibleViewportInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleViewportInterfaceD1Ev(
    QAccessibleViewportInterface *self) {
  delete self;
}

//  QSizeF QAccessibleViewportInterface::contentSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK28QAccessibleViewportInterface11contentSizeEv(
    const QAccessibleViewportInterface *self) {
  return new QSizeF(self->contentSize());
}

//  QPointF QAccessibleViewportInterface::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK28QAccessibleViewportInterface8positionEv(
    const QAccessibleViewportInterface *self) {
  return new QPointF(self->position());
}

//  QSizeF QAccessibleViewportInterface::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK28QAccessibleViewportInterface12viewportSizeEv(
    const QAccessibleViewportInterface *self) {
  return new QSizeF(self->viewportSize());
}

//  bool QAccessibleViewportInterface::isIndexed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QAccessibleViewportInterface9isIndexedEv(
    const QAccessibleViewportInterface *self) {
  return self->isIndexed();
}

//  void QAccessibleViewportInterface::setPosition(QPointF position)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QAccessibleViewportInterface11setPositionE7QPointF(
    QAccessibleViewportInterface *self,
    const QPointF *position) {
  self->setPosition(*position);
}
