//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QScxmlStateMachinePrivate::Queue::Queue()
extern "C" Q_DECL_EXPORT
QScxmlStateMachinePrivate::Queue *ritual_ZN25QScxmlStateMachinePrivate5QueueC1Ev() {
  return new QScxmlStateMachinePrivate::Queue();
}

//  QScxmlStateMachinePrivate::Queue::~Queue()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate5QueueD1Ev(
    QScxmlStateMachinePrivate::Queue *self) {
  delete self;
}

//  void QScxmlStateMachinePrivate::Queue::enqueue(QScxmlEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QScxmlStateMachinePrivate5Queue7enqueueEP11QScxmlEvent(
    QScxmlStateMachinePrivate::Queue *self,
    QScxmlEvent *e) {
  self->enqueue(e);
}

//  bool QScxmlStateMachinePrivate::Queue::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QScxmlStateMachinePrivate5Queue7isEmptyEv(
    const QScxmlStateMachinePrivate::Queue *self) {
  return self->isEmpty();
}

//  QScxmlEvent *QScxmlStateMachinePrivate::Queue::dequeue()
extern "C" Q_DECL_EXPORT
QScxmlEvent *ritual_ZN25QScxmlStateMachinePrivate5Queue7dequeueEv(
    QScxmlStateMachinePrivate::Queue *self) {
  return self->dequeue();
}
