//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QWindowStateChangeEvent that Python can take functions over in. Every QWindowStateChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQWindowStateChangeEventCall0)(const void *, int *);
typedef void (*CuteQWindowStateChangeEventCall1)(const void *, bool, int *);
class CuteQWindowStateChangeEvent : public QWindowStateChangeEvent {
public:
  using QWindowStateChangeEvent::QWindowStateChangeEvent;
  CuteQWindowStateChangeEvent(const QWindowStateChangeEvent & other) : QWindowStateChangeEvent(other) {}
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

  //  QWindowStateChangeEvent *QWindowStateChangeEvent::clone() const
  QWindowStateChangeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowStateChangeEventCall0 call = reinterpret_cast<CuteQWindowStateChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWindowStateChangeEvent *>(given);
    }
    return QWindowStateChangeEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowStateChangeEventCall1 call = reinterpret_cast<CuteQWindowStateChangeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QWindowStateChangeEvent::QWindowStateChangeEvent(const
//      QWindowStateChangeEvent &a0)
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_ZN23QWindowStateChangeEventC1ERKS_(
    const QWindowStateChangeEvent *a0) {
  return new CuteQWindowStateChangeEvent(*a0);
}

//  QWindowStateChangeEvent &QWindowStateChangeEvent::operator=(const
//      QWindowStateChangeEvent &other)
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_ZN23QWindowStateChangeEventaSERKS_(
    QWindowStateChangeEvent *self,
    const QWindowStateChangeEvent *other) {
  return &(self->operator=(*other));
}

//  QWindowStateChangeEvent *QWindowStateChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_ZNK23QWindowStateChangeEvent5cloneEv(
    const QWindowStateChangeEvent *self) {
  return self->clone();
}

//  QWindowStateChangeEvent::~QWindowStateChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWindowStateChangeEventD1Ev(QWindowStateChangeEvent *self) {
  delete self;
}

//  QWindowStateChangeEvent::QWindowStateChangeEvent(Qt::WindowStates
//      oldState, bool isOverride)
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_ZN23QWindowStateChangeEventC1E6QFlagsIN2Qt11WindowStateEEb(
    int oldState,
    bool isOverride) {
  return new CuteQWindowStateChangeEvent(
      QFlags<Qt::WindowState>::fromInt(oldState),
      isOverride);
}

//  Qt::WindowStates QWindowStateChangeEvent::oldState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QWindowStateChangeEvent8oldStateEv(
    const QWindowStateChangeEvent *self) {
  return static_cast<int>(self->oldState().toInt());
}

//  bool QWindowStateChangeEvent::isOverride() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWindowStateChangeEvent10isOverrideEv(
    const QWindowStateChangeEvent *self) {
  return self->isOverride();
}

//  a Python function taken by a CuteQWindowStateChangeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowStateChangeEvent(
    QWindowStateChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowStateChangeEvent *>(self)->take(key, call);
}

//  QWindowStateChangeEvent *QWindowStateChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QWindowStateChangeEvent *ritual_own_ZNK23QWindowStateChangeEvent5cloneEv(
    const QWindowStateChangeEvent *self) {
  return self->QWindowStateChangeEvent::clone();
}
