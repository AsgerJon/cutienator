//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QStatusTipEvent that Python can take functions over in. Every QStatusTipEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQStatusTipEventCall0)(const void *, int *);
typedef void (*CuteQStatusTipEventCall1)(const void *, bool, int *);
class CuteQStatusTipEvent : public QStatusTipEvent {
public:
  using QStatusTipEvent::QStatusTipEvent;
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

  //  QStatusTipEvent *QStatusTipEvent::clone() const
  QStatusTipEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQStatusTipEventCall0 call = reinterpret_cast<CuteQStatusTipEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QStatusTipEvent *>(given);
    }
    return QStatusTipEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQStatusTipEventCall1 call = reinterpret_cast<CuteQStatusTipEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QStatusTipEvent *QStatusTipEvent::clone() const
extern "C" Q_DECL_EXPORT
QStatusTipEvent *ritual_ZNK15QStatusTipEvent5cloneEv(
    const QStatusTipEvent *self) {
  return self->clone();
}

//  QStatusTipEvent::~QStatusTipEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QStatusTipEventD1Ev(QStatusTipEvent *self) {
  delete self;
}

//  QStatusTipEvent::QStatusTipEvent(const QString &tip)
extern "C" Q_DECL_EXPORT
QStatusTipEvent *ritual_ZN15QStatusTipEventC1ERK7QString(
    const QString *tip) {
  return new CuteQStatusTipEvent(*tip);
}

//  QString QStatusTipEvent::tip() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QStatusTipEvent3tipEv(const QStatusTipEvent *self) {
  return new QString(self->tip());
}

//  a Python function taken by a CuteQStatusTipEvent, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QStatusTipEvent(
    QStatusTipEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQStatusTipEvent *>(self)->take(key, call);
}

//  QStatusTipEvent *QStatusTipEvent::clone() const
extern "C" Q_DECL_EXPORT
QStatusTipEvent *ritual_own_ZNK15QStatusTipEvent5cloneEv(
    const QStatusTipEvent *self) {
  return self->QStatusTipEvent::clone();
}
