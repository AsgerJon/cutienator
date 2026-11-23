//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QDragLeaveEvent that Python can take functions over in. Every QDragLeaveEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDragLeaveEventCall0)(const void *, int *);
typedef void (*CuteQDragLeaveEventCall1)(const void *, bool, int *);
class CuteQDragLeaveEvent : public QDragLeaveEvent {
public:
  using QDragLeaveEvent::QDragLeaveEvent;
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

  //  QDragLeaveEvent *QDragLeaveEvent::clone() const
  QDragLeaveEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDragLeaveEventCall0 call = reinterpret_cast<CuteQDragLeaveEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QDragLeaveEvent *>(given);
    }
    return QDragLeaveEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQDragLeaveEventCall1 call = reinterpret_cast<CuteQDragLeaveEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QDragLeaveEvent *QDragLeaveEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragLeaveEvent *ritual_ZNK15QDragLeaveEvent5cloneEv(
    const QDragLeaveEvent *self) {
  return self->clone();
}

//  QDragLeaveEvent::~QDragLeaveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDragLeaveEventD1Ev(QDragLeaveEvent *self) {
  delete self;
}

//  QDragLeaveEvent::QDragLeaveEvent()
extern "C" Q_DECL_EXPORT
QDragLeaveEvent *ritual_ZN15QDragLeaveEventC1Ev() {
  return new CuteQDragLeaveEvent();
}

//  a Python function taken by a CuteQDragLeaveEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDragLeaveEvent(
    QDragLeaveEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDragLeaveEvent *>(self)->take(key, call);
}

//  QDragLeaveEvent *QDragLeaveEvent::clone() const
extern "C" Q_DECL_EXPORT
QDragLeaveEvent *ritual_own_ZNK15QDragLeaveEvent5cloneEv(
    const QDragLeaveEvent *self) {
  return self->QDragLeaveEvent::clone();
}
