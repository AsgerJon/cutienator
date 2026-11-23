//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QFocusEvent that Python can take functions over in. Every QFocusEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQFocusEventCall0)(const void *, int *);
typedef void (*CuteQFocusEventCall1)(const void *, bool, int *);
class CuteQFocusEvent : public QFocusEvent {
public:
  using QFocusEvent::QFocusEvent;
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

  //  QFocusEvent *QFocusEvent::clone() const
  QFocusEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFocusEventCall0 call = reinterpret_cast<CuteQFocusEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QFocusEvent *>(given);
    }
    return QFocusEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFocusEventCall1 call = reinterpret_cast<CuteQFocusEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QFocusEvent *QFocusEvent::clone() const
extern "C" Q_DECL_EXPORT
QFocusEvent *ritual_ZNK11QFocusEvent5cloneEv(const QFocusEvent *self) {
  return self->clone();
}

//  QFocusEvent::~QFocusEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFocusEventD1Ev(QFocusEvent *self) {
  delete self;
}

//  QFocusEvent::QFocusEvent(Type type, Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
QFocusEvent *ritual_ZN11QFocusEventC1EN6QEvent4TypeEN2Qt11FocusReasonE(
    QEvent::Type type,
    Qt::FocusReason reason) {
  return new CuteQFocusEvent(type, reason);
}

//  bool QFocusEvent::gotFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFocusEvent8gotFocusEv(const QFocusEvent *self) {
  return self->gotFocus();
}

//  bool QFocusEvent::lostFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFocusEvent9lostFocusEv(const QFocusEvent *self) {
  return self->lostFocus();
}

//  Qt::FocusReason QFocusEvent::reason() const
extern "C" Q_DECL_EXPORT
Qt::FocusReason ritual_ZNK11QFocusEvent6reasonEv(const QFocusEvent *self) {
  return self->reason();
}

//  a Python function taken by a CuteQFocusEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFocusEvent(
    QFocusEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFocusEvent *>(self)->take(key, call);
}

//  QFocusEvent *QFocusEvent::clone() const
extern "C" Q_DECL_EXPORT
QFocusEvent *ritual_own_ZNK11QFocusEvent5cloneEv(const QFocusEvent *self) {
  return self->QFocusEvent::clone();
}
