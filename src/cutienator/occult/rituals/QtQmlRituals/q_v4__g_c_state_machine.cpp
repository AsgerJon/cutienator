//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::GCStateMachine::step()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414GCStateMachine4stepEv(QV4::GCStateMachine *self) {
  self->step();
}

//  bool QV4::GCStateMachine::inProgress()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV414GCStateMachine10inProgressEv(QV4::GCStateMachine *self) {
  return self->inProgress();
}

//  void QV4::GCStateMachine::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414GCStateMachine5resetEv(QV4::GCStateMachine *self) {
  self->reset();
}

//  void QV4::GCStateMachine::handleTimeout(GCState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414GCStateMachine13handleTimeoutENS0_7GCStateE(
    QV4::GCStateMachine *self,
    QV4::GCStateMachine::GCState state) {
  self->handleTimeout(state);
}
