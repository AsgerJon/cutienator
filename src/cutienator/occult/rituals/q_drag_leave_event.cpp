//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QDragLeaveEvent *QDragLeaveEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragLeaveEvent *ritual_ZNK15QDragLeaveEvent5cloneEv(
    const QDragLeaveEvent *self) {
  return self->clone();
}

//  QDragLeaveEvent::~QDragLeaveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDragLeaveEventD1Ev(QDragLeaveEvent *self) {
  delete self;
}

//  QDragLeaveEvent::QDragLeaveEvent()
extern "C" Q_DECL_EXPORT
QDragLeaveEvent *ritual_ZN15QDragLeaveEventC1Ev() {
  return new QDragLeaveEvent();
}
