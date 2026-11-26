//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QHideEvent that Python can take functions over in. Every QHideEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQHideEventCall0)(const void *, int *);
typedef void (*CuteQHideEventCall1)(const void *, bool, int *);
class CuteQHideEvent : public QHideEvent {
public:
  using QHideEvent::QHideEvent;
  CuteQHideEvent(const QHideEvent & other) : QHideEvent(other) {}
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

  //  QHideEvent *QHideEvent::clone() const
  QHideEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHideEventCall0 call = reinterpret_cast<CuteQHideEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QHideEvent *>(given);
    }
    return QHideEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHideEventCall1 call = reinterpret_cast<CuteQHideEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QHideEvent::QHideEvent(const QHideEvent &a0)
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_ZN10QHideEventC1ERKS_(const QHideEvent *a0) {
  return new CuteQHideEvent(*a0);
}

//  QHideEvent &QHideEvent::operator=(const QHideEvent &other)
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_ZN10QHideEventaSERKS_(
    QHideEvent *self,
    const QHideEvent *other) {
  return &(self->operator=(*other));
}

//  QHideEvent *QHideEvent::clone() const
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_ZNK10QHideEvent5cloneEv(const QHideEvent *self) {
  return self->clone();
}

//  QHideEvent::~QHideEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QHideEventD1Ev(QHideEvent *self) {
  delete self;
}

//  QHideEvent::QHideEvent()
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_ZN10QHideEventC1Ev() {
  return new CuteQHideEvent();
}

//  a Python function taken by a CuteQHideEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHideEvent(QHideEvent *self, const char *key, void *call) {
  return static_cast<CuteQHideEvent *>(self)->take(key, call);
}

//  QHideEvent *QHideEvent::clone() const
extern "C" Q_DECL_EXPORT
QHideEvent *ritual_own_ZNK10QHideEvent5cloneEv(const QHideEvent *self) {
  return self->QHideEvent::clone();
}
