//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QApplicationStateChangeEvent *QApplicationStateChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QApplicationStateChangeEvent *ritual_ZNK28QApplicationStateChangeEvent5cloneEv(
    const QApplicationStateChangeEvent *self) {
  return self->clone();
}

//  QApplicationStateChangeEvent::~QApplicationStateChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QApplicationStateChangeEventD1Ev(
    QApplicationStateChangeEvent *self) {
  delete self;
}

//  QApplicationStateChangeEvent::QApplicationStateChangeEvent(Qt::Applicatio
//      nState state)
extern "C" Q_DECL_EXPORT
QApplicationStateChangeEvent *ritual_ZN28QApplicationStateChangeEventC1EN2Qt16ApplicationStateE(
    Qt::ApplicationState state) {
  return new QApplicationStateChangeEvent(state);
}

//  Qt::ApplicationState QApplicationStateChangeEvent::applicationState()
//      const
extern "C" Q_DECL_EXPORT
Qt::ApplicationState ritual_ZNK28QApplicationStateChangeEvent16applicationStateEv(
    const QApplicationStateChangeEvent *self) {
  return self->applicationState();
}
