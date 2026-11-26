//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QShowEvent that Python can take functions over in. Every QShowEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQShowEventCall0)(const void *, int *);
typedef void (*CuteQShowEventCall1)(const void *, bool, int *);
class CuteQShowEvent : public QShowEvent {
public:
  using QShowEvent::QShowEvent;
  CuteQShowEvent(const QShowEvent & other) : QShowEvent(other) {}
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

  //  QShowEvent *QShowEvent::clone() const
  QShowEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQShowEventCall0 call = reinterpret_cast<CuteQShowEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QShowEvent *>(given);
    }
    return QShowEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQShowEventCall1 call = reinterpret_cast<CuteQShowEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QShowEvent::QShowEvent(const QShowEvent &a0)
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_ZN10QShowEventC1ERKS_(const QShowEvent *a0) {
  return new CuteQShowEvent(*a0);
}

//  QShowEvent &QShowEvent::operator=(const QShowEvent &other)
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_ZN10QShowEventaSERKS_(
    QShowEvent *self,
    const QShowEvent *other) {
  return &(self->operator=(*other));
}

//  QShowEvent *QShowEvent::clone() const
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_ZNK10QShowEvent5cloneEv(const QShowEvent *self) {
  return self->clone();
}

//  QShowEvent::~QShowEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QShowEventD1Ev(QShowEvent *self) {
  delete self;
}

//  QShowEvent::QShowEvent()
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_ZN10QShowEventC1Ev() {
  return new CuteQShowEvent();
}

//  a Python function taken by a CuteQShowEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QShowEvent(QShowEvent *self, const char *key, void *call) {
  return static_cast<CuteQShowEvent *>(self)->take(key, call);
}

//  QShowEvent *QShowEvent::clone() const
extern "C" Q_DECL_EXPORT
QShowEvent *ritual_own_ZNK10QShowEvent5cloneEv(const QShowEvent *self) {
  return self->QShowEvent::clone();
}
