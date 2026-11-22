//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QIconDragEvent *QIconDragEvent::clone() const
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_ZNK14QIconDragEvent5cloneEv(
    const QIconDragEvent *self) {
  return self->clone();
}

//  QIconDragEvent::~QIconDragEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QIconDragEventD1Ev(QIconDragEvent *self) {
  delete self;
}

//  QIconDragEvent::QIconDragEvent()
extern "C" Q_DECL_EXPORT
QIconDragEvent *ritual_ZN14QIconDragEventC1Ev() {
  return new QIconDragEvent();
}
