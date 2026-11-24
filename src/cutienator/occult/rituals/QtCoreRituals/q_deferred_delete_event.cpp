//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcoreevent_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcoreevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QDeferredDeleteEvent that Python can take functions over in. Every QDeferredDeleteEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDeferredDeleteEventCall0)(const void *, int *);
typedef void (*CuteQDeferredDeleteEventCall1)(const void *, bool, int *);
class CuteQDeferredDeleteEvent : public QDeferredDeleteEvent {
public:
  using QDeferredDeleteEvent::QDeferredDeleteEvent;
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

  //  QDeferredDeleteEvent *QDeferredDeleteEvent::clone() const
  QDeferredDeleteEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDeferredDeleteEventCall0 call = reinterpret_cast<CuteQDeferredDeleteEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDeferredDeleteEvent *>(given);
    }
    return QDeferredDeleteEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDeferredDeleteEventCall1 call = reinterpret_cast<CuteQDeferredDeleteEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  int QDeferredDeleteEvent::loopLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDeferredDeleteEvent9loopLevelEv(
    const QDeferredDeleteEvent *self) {
  return self->loopLevel();
}

//  int QDeferredDeleteEvent::scopeLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QDeferredDeleteEvent10scopeLevelEv(
    const QDeferredDeleteEvent *self) {
  return self->scopeLevel();
}

//  a Python function taken by a CuteQDeferredDeleteEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDeferredDeleteEvent(
    QDeferredDeleteEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDeferredDeleteEvent *>(self)->take(key, call);
}
