//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class; its header writes all
//  of it out.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h>
#include <cstring>

//  A QZeroTimerEvent that Python can take functions over in. Every
//  QZeroTimerEvent Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQZeroTimerEventCall0)(const void *, int *);
typedef void (*CuteQZeroTimerEventCall1)(const void *, bool, int *);
class CuteQZeroTimerEvent : public QZeroTimerEvent {
public:
  using QZeroTimerEvent::QZeroTimerEvent;
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
      CuteQZeroTimerEventCall0 call = reinterpret_cast<CuteQZeroTimerEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTimerEvent *>(given);
    }
    return QTimerEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQZeroTimerEventCall1 call = reinterpret_cast<CuteQZeroTimerEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QZeroTimerEvent::QZeroTimerEvent(int timerId)
extern "C" Q_DECL_EXPORT
QZeroTimerEvent *ritual_ZN15QZeroTimerEventC1Ei(int timerId) {
  return new CuteQZeroTimerEvent(timerId);
}

//  QZeroTimerEvent::~QZeroTimerEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QZeroTimerEventD1Ev(QZeroTimerEvent *self) {
  delete self;
}

//  a Python function taken by a CuteQZeroTimerEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QZeroTimerEvent(
    QZeroTimerEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQZeroTimerEvent *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
