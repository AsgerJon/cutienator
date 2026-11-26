//  Written by dev_tooling.RitualGenerator from the records of
//  QtStateMachine/qstatemachine.h, Qt 6.12.0. Changes made here are lost.
#include <QtStateMachine/qstatemachine.h>
#include <cstring>

//  A QStateMachine::WrappedEvent that Python can take functions over in. Every QStateMachine::WrappedEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQStateMachine_WrappedEventCall0)(const void *, bool, int *);
typedef void * (*CuteQStateMachine_WrappedEventCall1)(const void *, int *);
class CuteQStateMachine_WrappedEvent : public QStateMachine::WrappedEvent {
public:
  using QStateMachine::WrappedEvent::WrappedEvent;
  CuteQStateMachine_WrappedEvent(const QStateMachine::WrappedEvent & other) : QStateMachine::WrappedEvent(other) {}
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
      CuteQStateMachine_WrappedEventCall0 call = reinterpret_cast<CuteQStateMachine_WrappedEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQStateMachine_WrappedEventCall1 call = reinterpret_cast<CuteQStateMachine_WrappedEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QStateMachine::WrappedEvent::WrappedEvent(QObject *object, QEvent *event)
extern "C" Q_DECL_EXPORT
QStateMachine::WrappedEvent *ritual_ZN13QStateMachine12WrappedEventC1EP7QObjectP6QEvent(
    QObject *object,
    QEvent *event) {
  return new CuteQStateMachine_WrappedEvent(object, event);
}

//  QStateMachine::WrappedEvent::~WrappedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QStateMachine12WrappedEventD1Ev(
    QStateMachine::WrappedEvent *self) {
  delete self;
}

//  QObject *QStateMachine::WrappedEvent::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QStateMachine12WrappedEvent6objectEv(
    const QStateMachine::WrappedEvent *self) {
  return self->object();
}

//  QEvent *QStateMachine::WrappedEvent::event() const
extern "C" Q_DECL_EXPORT
QEvent *ritual_ZNK13QStateMachine12WrappedEvent5eventEv(
    const QStateMachine::WrappedEvent *self) {
  return self->event();
}

//  a Python function taken by a CuteQStateMachine_WrappedEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStateMachine_WrappedEvent(
    QStateMachine::WrappedEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStateMachine_WrappedEvent *>(self)->take(key, call);
}
