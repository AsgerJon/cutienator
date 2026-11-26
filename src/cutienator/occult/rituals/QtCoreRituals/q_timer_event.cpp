//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcoreevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcoreevent.h>
#include <cstring>

//  A QTimerEvent that Python can take functions over in. Every QTimerEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQTimerEventCall0)(const void *, int *);
typedef void (*CuteQTimerEventCall1)(const void *, bool, int *);
class CuteQTimerEvent : public QTimerEvent {
public:
  using QTimerEvent::QTimerEvent;
  CuteQTimerEvent(const QTimerEvent & other) : QTimerEvent(other) {}
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

  //  QTimerEvent *QTimerEvent::clone() const
  QTimerEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTimerEventCall0 call = reinterpret_cast<CuteQTimerEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTimerEvent *>(given);
    }
    return QTimerEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTimerEventCall1 call = reinterpret_cast<CuteQTimerEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QTimerEvent::QTimerEvent(const QTimerEvent &a0)
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_ZN11QTimerEventC1ERKS_(const QTimerEvent *a0) {
  return new CuteQTimerEvent(*a0);
}

//  QTimerEvent &QTimerEvent::operator=(const QTimerEvent &other)
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_ZN11QTimerEventaSERKS_(
    QTimerEvent *self,
    const QTimerEvent *other) {
  return &(self->operator=(*other));
}

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
  return new CuteQTimerEvent(timerId);
}

//  QTimerEvent::QTimerEvent(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_ZN11QTimerEventC1EN2Qt7TimerIdE(Qt::TimerId timerId) {
  return new CuteQTimerEvent(timerId);
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

//  bool QTimerEvent::matches(const QBasicTimer &timer) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTimerEvent7matchesERK11QBasicTimer(
    const QTimerEvent *self,
    const QBasicTimer *timer) {
  return self->matches(*timer);
}

//  a Python function taken by a CuteQTimerEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTimerEvent(
    QTimerEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTimerEvent *>(self)->take(key, call);
}

//  QTimerEvent *QTimerEvent::clone() const
extern "C" Q_DECL_EXPORT
QTimerEvent *ritual_own_ZNK11QTimerEvent5cloneEv(const QTimerEvent *self) {
  return self->QTimerEvent::clone();
}
