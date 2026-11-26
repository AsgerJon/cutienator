//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QChildWindowEvent that Python can take functions over in. Every QChildWindowEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQChildWindowEventCall0)(const void *, int *);
typedef void (*CuteQChildWindowEventCall1)(const void *, bool, int *);
class CuteQChildWindowEvent : public QChildWindowEvent {
public:
  using QChildWindowEvent::QChildWindowEvent;
  CuteQChildWindowEvent(const QChildWindowEvent & other) : QChildWindowEvent(other) {}
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

  //  QChildWindowEvent *QChildWindowEvent::clone() const
  QChildWindowEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQChildWindowEventCall0 call = reinterpret_cast<CuteQChildWindowEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QChildWindowEvent *>(given);
    }
    return QChildWindowEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQChildWindowEventCall1 call = reinterpret_cast<CuteQChildWindowEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QChildWindowEvent::QChildWindowEvent(const QChildWindowEvent &a0)
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_ZN17QChildWindowEventC1ERKS_(
    const QChildWindowEvent *a0) {
  return new CuteQChildWindowEvent(*a0);
}

//  QChildWindowEvent &QChildWindowEvent::operator=(const QChildWindowEvent
//      &other)
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_ZN17QChildWindowEventaSERKS_(
    QChildWindowEvent *self,
    const QChildWindowEvent *other) {
  return &(self->operator=(*other));
}

//  QChildWindowEvent *QChildWindowEvent::clone() const
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_ZNK17QChildWindowEvent5cloneEv(
    const QChildWindowEvent *self) {
  return self->clone();
}

//  QChildWindowEvent::~QChildWindowEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QChildWindowEventD1Ev(QChildWindowEvent *self) {
  delete self;
}

//  QChildWindowEvent::QChildWindowEvent(Type type, QWindow *childWindow)
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_ZN17QChildWindowEventC1EN6QEvent4TypeEP7QWindow(
    QEvent::Type type,
    QWindow *childWindow) {
  return new CuteQChildWindowEvent(type, childWindow);
}

//  QWindow *QChildWindowEvent::child() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK17QChildWindowEvent5childEv(
    const QChildWindowEvent *self) {
  return self->child();
}

//  a Python function taken by a CuteQChildWindowEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QChildWindowEvent(
    QChildWindowEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQChildWindowEvent *>(self)->take(key, call);
}

//  QChildWindowEvent *QChildWindowEvent::clone() const
extern "C" Q_DECL_EXPORT
QChildWindowEvent *ritual_own_ZNK17QChildWindowEvent5cloneEv(
    const QChildWindowEvent *self) {
  return self->QChildWindowEvent::clone();
}
