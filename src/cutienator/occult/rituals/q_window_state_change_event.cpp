//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

//  QWindowStateChangeEvent *QWindowStateChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_ZNK23QWindowStateChangeEvent5cloneEv(
    const QWindowStateChangeEvent *self) {
  return self->clone();
}

//  QWindowStateChangeEvent::~QWindowStateChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWindowStateChangeEventD1Ev(QWindowStateChangeEvent *self) {
  delete self;
}

//  QWindowStateChangeEvent::QWindowStateChangeEvent(Qt::WindowStates
//      oldState, bool isOverride)
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_ZN23QWindowStateChangeEventC1E6QFlagsIN2Qt11WindowStateEEb(
    int oldState,
    bool isOverride) {
  return new QWindowStateChangeEvent(
      QFlags<Qt::WindowState>::fromInt(oldState),
      isOverride);
}

//  Qt::WindowStates QWindowStateChangeEvent::oldState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QWindowStateChangeEvent8oldStateEv(
    const QWindowStateChangeEvent *self) {
  return static_cast<int>(self->oldState().toInt());
}

//  bool QWindowStateChangeEvent::isOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWindowStateChangeEvent10isOverrideEv(
    const QWindowStateChangeEvent *self) {
  return self->isOverride();
}
