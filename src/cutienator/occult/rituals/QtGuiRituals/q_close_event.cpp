//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QCloseEvent *QCloseEvent::clone() const
extern "C" Q_DECL_EXPORT
QCloseEvent *ritual_ZNK11QCloseEvent5cloneEv(const QCloseEvent *self) {
  return self->clone();
}

//  QCloseEvent::~QCloseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCloseEventD1Ev(QCloseEvent *self) {
  delete self;
}

//  QCloseEvent::QCloseEvent()
extern "C" Q_DECL_EXPORT
QCloseEvent *ritual_ZN11QCloseEventC1Ev() {
  return new QCloseEvent();
}
