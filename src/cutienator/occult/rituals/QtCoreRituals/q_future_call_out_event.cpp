//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfutureinterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfutureinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QFutureCallOutEvent that Python can take functions over in. Every QFutureCallOutEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(future)
typedef void * (*CuteQFutureCallOutEventCall0)(const void *, int *);
#endif  // QT_CONFIG(future)
typedef void (*CuteQFutureCallOutEventCall1)(const void *, bool, int *);
class CuteQFutureCallOutEvent : public QFutureCallOutEvent {
public:
  using QFutureCallOutEvent::QFutureCallOutEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(future)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(future)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(future)
  //  QFutureCallOutEvent *QFutureCallOutEvent::clone() const
  QFutureCallOutEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFutureCallOutEventCall0 call = reinterpret_cast<CuteQFutureCallOutEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QFutureCallOutEvent *>(given);
    }
    return QFutureCallOutEvent::clone();
  }
#endif  // QT_CONFIG(future)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFutureCallOutEventCall1 call = reinterpret_cast<CuteQFutureCallOutEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QFutureCallOutEvent *QFutureCallOutEvent::clone() const
extern "C" Q_DECL_EXPORT
QFutureCallOutEvent *ritual_ZNK19QFutureCallOutEvent5cloneEv(
    const QFutureCallOutEvent *self) {
  return self->clone();
}

//  QFutureCallOutEvent::~QFutureCallOutEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFutureCallOutEventD1Ev(QFutureCallOutEvent *self) {
  delete self;
}

//  QFutureCallOutEvent::QFutureCallOutEvent()
extern "C" Q_DECL_EXPORT
QFutureCallOutEvent *ritual_ZN19QFutureCallOutEventC1Ev() {
  return new CuteQFutureCallOutEvent();
}

//  QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
//      index1)
extern "C" Q_DECL_EXPORT
QFutureCallOutEvent *ritual_ZN19QFutureCallOutEventC1ENS_11CallOutTypeEi(
    QFutureCallOutEvent::CallOutType callOutType,
    int index1) {
  return new CuteQFutureCallOutEvent(callOutType, index1);
}

//  QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
//      index1, int index2)
extern "C" Q_DECL_EXPORT
QFutureCallOutEvent *ritual_ZN19QFutureCallOutEventC1ENS_11CallOutTypeEii(
    QFutureCallOutEvent::CallOutType callOutType,
    int index1,
    int index2) {
  return new CuteQFutureCallOutEvent(callOutType, index1, index2);
}

//  QFutureCallOutEvent::QFutureCallOutEvent(CallOutType callOutType, int
//      index1, const QString &text)
extern "C" Q_DECL_EXPORT
QFutureCallOutEvent *ritual_ZN19QFutureCallOutEventC1ENS_11CallOutTypeEiRK7QString(
    QFutureCallOutEvent::CallOutType callOutType,
    int index1,
    const QString *text) {
  return new CuteQFutureCallOutEvent(callOutType, index1, *text);
}

//  a Python function taken by a CuteQFutureCallOutEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFutureCallOutEvent(
    QFutureCallOutEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFutureCallOutEvent *>(self)->take(key, call);
}

//  QFutureCallOutEvent *QFutureCallOutEvent::clone() const
extern "C" Q_DECL_EXPORT
QFutureCallOutEvent *ritual_own_ZNK19QFutureCallOutEvent5cloneEv(
    const QFutureCallOutEvent *self) {
  return self->QFutureCallOutEvent::clone();
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
