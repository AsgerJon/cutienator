//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QShowEvent *QShowEvent::clone() const
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_ZNK10QShowEvent5cloneEv(const QShowEvent *self) {
  return self->clone();
}

//  QShowEvent::~QShowEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QShowEventD1Ev(QShowEvent *self) {
  delete self;
}

//  QShowEvent::QShowEvent()
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_ZN10QShowEventC1Ev() {
  return new QShowEvent();
}
