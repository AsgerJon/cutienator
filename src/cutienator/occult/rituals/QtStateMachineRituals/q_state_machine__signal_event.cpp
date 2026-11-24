//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qstatemachine.h, Qt 6.12.0. Changes made here are lost.
#include <QtStateMachine/qstatemachine.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QStateMachine::SignalEvent that Python can take functions over in. Every QStateMachine::SignalEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStateMachine_SignalEventCall0)(const void *, bool, int *);
typedef void * (*CuteQStateMachine_SignalEventCall1)(const void *, int *);
class CuteQStateMachine_SignalEvent : public QStateMachine::SignalEvent {
public:
  using QStateMachine::SignalEvent::SignalEvent;
  CuteQStateMachine_SignalEvent(const QStateMachine::SignalEvent &other) : QStateMachine::SignalEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQStateMachine_SignalEventCall0 call = reinterpret_cast<CuteQStateMachine_SignalEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStateMachine_SignalEventCall1 call = reinterpret_cast<CuteQStateMachine_SignalEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QStateMachine::SignalEvent::SignalEvent(QObject *sender, int signalIndex,
//      const QList<QVariant> &arguments)
extern "C" Q_DECL_EXPORT
QStateMachine::SignalEvent *ritual_ZN13QStateMachine11SignalEventC1EP7QObjectiRK5QListI8QVariantE(
    QObject *sender,
    int signalIndex,
    const QList<QVariant> *arguments) {
  return new CuteQStateMachine_SignalEvent(sender, signalIndex, *arguments);
}

//  QStateMachine::SignalEvent::~SignalEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine11SignalEventD1Ev(
    QStateMachine::SignalEvent *self) {
  delete self;
}

//  QObject *QStateMachine::SignalEvent::sender() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QStateMachine11SignalEvent6senderEv(
    const QStateMachine::SignalEvent *self) {
  return self->sender();
}

//  int QStateMachine::SignalEvent::signalIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QStateMachine11SignalEvent11signalIndexEv(
    const QStateMachine::SignalEvent *self) {
  return self->signalIndex();
}

//  QList<QVariant> QStateMachine::SignalEvent::arguments() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK13QStateMachine11SignalEvent9argumentsEv(
    const QStateMachine::SignalEvent *self) {
  return new QList<QVariant>(self->arguments());
}

//  a Python function taken by a CuteQStateMachine_SignalEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStateMachine_SignalEvent(
    QStateMachine::SignalEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStateMachine_SignalEvent *>(self)->take(key, call);
}
