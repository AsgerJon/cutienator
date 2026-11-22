//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QCloseEvent that Python can take functions over in. Every QCloseEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCloseEventCall0)(const void *, int *);
typedef void (*CuteQCloseEventCall1)(const void *, bool, int *);
class CuteQCloseEvent : public QCloseEvent {
public:
  using QCloseEvent::QCloseEvent;
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

  //  QCloseEvent *QCloseEvent::clone() const
  QCloseEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCloseEventCall0 call = reinterpret_cast<CuteQCloseEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCloseEvent *>(given);
    }
    return QCloseEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCloseEventCall1 call = reinterpret_cast<CuteQCloseEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QCloseEvent *QCloseEvent::clone() const
extern "C" Q_DECL_EXPORT
QCloseEvent *ritual_ZNK11QCloseEvent5cloneEv(const QCloseEvent *self) {
  return self->clone();
}

//  QCloseEvent::~QCloseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCloseEventD1Ev(QCloseEvent *self) {
  delete self;
}

//  QCloseEvent::QCloseEvent()
extern "C" Q_DECL_EXPORT
QCloseEvent *ritual_ZN11QCloseEventC1Ev() {
  return new CuteQCloseEvent();
}

//  a Python function taken by a CuteQCloseEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCloseEvent(
    QCloseEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCloseEvent *>(self)->take(key, call);
}

//  QCloseEvent *QCloseEvent::clone() const
extern "C" Q_DECL_EXPORT
QCloseEvent *ritual_own_ZNK11QCloseEvent5cloneEv(const QCloseEvent *self) {
  return self->QCloseEvent::clone();
}
