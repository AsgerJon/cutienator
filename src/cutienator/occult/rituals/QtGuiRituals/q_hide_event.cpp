//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QHideEvent *QHideEvent::clone() const
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_ZNK10QHideEvent5cloneEv(const QHideEvent *self) {
  return self->clone();
}

//  QHideEvent::~QHideEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHideEventD1Ev(QHideEvent *self) {
  delete self;
}

//  QHideEvent::QHideEvent()
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_ZN10QHideEventC1Ev() {
  return new QHideEvent();
}
