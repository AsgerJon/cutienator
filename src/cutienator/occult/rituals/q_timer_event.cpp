//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>

//  QTimerEvent *QTimerEvent::clone() const
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_ZNK11QTimerEvent5cloneEv(const QTimerEvent *self) {
  return self->clone();
}

//  QTimerEvent::~QTimerEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTimerEventD1Ev(QTimerEvent *self) {
  delete self;
}

//  QTimerEvent::QTimerEvent(int timerId)
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_ZN11QTimerEventC1Ei(int timerId) {
  return new QTimerEvent(timerId);
}

//  QTimerEvent::QTimerEvent(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_ZN11QTimerEventC1EN2Qt7TimerIdE(Qt::TimerId timerId) {
  return new QTimerEvent(timerId);
}

//  int QTimerEvent::timerId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTimerEvent7timerIdEv(const QTimerEvent *self) {
  return self->timerId();
}

//  Qt::TimerId QTimerEvent::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK11QTimerEvent2idEv(const QTimerEvent *self) {
  return self->id();
}
