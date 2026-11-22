//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QApplicationStateChangeEvent that Python can take functions over in. Every QApplicationStateChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQApplicationStateChangeEventCall0)(const void *, int *);
typedef void (*CuteQApplicationStateChangeEventCall1)(const void *, bool, int *);
class CuteQApplicationStateChangeEvent : public QApplicationStateChangeEvent {
public:
  using QApplicationStateChangeEvent::QApplicationStateChangeEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QApplicationStateChangeEvent *QApplicationStateChangeEvent::clone()
  //      const
  QApplicationStateChangeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQApplicationStateChangeEventCall0 call = reinterpret_cast<CuteQApplicationStateChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QApplicationStateChangeEvent *>(given);
    }
    return QApplicationStateChangeEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQApplicationStateChangeEventCall1 call = reinterpret_cast<CuteQApplicationStateChangeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

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
  return new CuteQApplicationStateChangeEvent(state);
}

//  Qt::ApplicationState QApplicationStateChangeEvent::applicationState()
//      const
extern "C" Q_DECL_EXPORT
Qt::ApplicationState ritual_ZNK28QApplicationStateChangeEvent16applicationStateEv(
    const QApplicationStateChangeEvent *self) {
  return self->applicationState();
}

//  a Python function taken by a CuteQApplicationStateChangeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QApplicationStateChangeEvent(
    QApplicationStateChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQApplicationStateChangeEvent *>(self)->take(key, call);
}

//  QApplicationStateChangeEvent *QApplicationStateChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QApplicationStateChangeEvent *ritual_own_ZNK28QApplicationStateChangeEvent5cloneEv(
    const QApplicationStateChangeEvent *self) {
  return self->QApplicationStateChangeEvent::clone();
}
