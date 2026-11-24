//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_TOOLBAR)
#include <QtGui/qevent.h>
#include <cstring>

//  A QToolBarChangeEvent that Python can take functions over in. Every QToolBarChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_TOOLBAR)
typedef void * (*CuteQToolBarChangeEventCall0)(const void *, int *);
#endif  // !defined(QT_NO_TOOLBAR)
typedef void (*CuteQToolBarChangeEventCall1)(const void *, bool, int *);
class CuteQToolBarChangeEvent : public QToolBarChangeEvent {
public:
  using QToolBarChangeEvent::QToolBarChangeEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_TOOLBAR)
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_TOOLBAR)
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

#if !defined(QT_NO_TOOLBAR)
  //  QToolBarChangeEvent *QToolBarChangeEvent::clone() const
  QToolBarChangeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQToolBarChangeEventCall0 call = reinterpret_cast<CuteQToolBarChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QToolBarChangeEvent *>(given);
    }
    return QToolBarChangeEvent::clone();
  }
#endif  // !defined(QT_NO_TOOLBAR)

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQToolBarChangeEventCall1 call = reinterpret_cast<CuteQToolBarChangeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QToolBarChangeEvent *QToolBarChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QToolBarChangeEvent *ritual_ZNK19QToolBarChangeEvent5cloneEv(
    const QToolBarChangeEvent *self) {
  return self->clone();
}

//  QToolBarChangeEvent::~QToolBarChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QToolBarChangeEventD1Ev(QToolBarChangeEvent *self) {
  delete self;
}

//  QToolBarChangeEvent::QToolBarChangeEvent(bool t)
extern "C" Q_DECL_EXPORT
QToolBarChangeEvent *ritual_ZN19QToolBarChangeEventC1Eb(bool t) {
  return new CuteQToolBarChangeEvent(t);
}

//  bool QToolBarChangeEvent::toggle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QToolBarChangeEvent6toggleEv(
    const QToolBarChangeEvent *self) {
  return self->toggle();
}

//  a Python function taken by a CuteQToolBarChangeEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QToolBarChangeEvent(
    QToolBarChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQToolBarChangeEvent *>(self)->take(key, call);
}

//  QToolBarChangeEvent *QToolBarChangeEvent::clone() const
extern "C" Q_DECL_EXPORT
QToolBarChangeEvent *ritual_own_ZNK19QToolBarChangeEvent5cloneEv(
    const QToolBarChangeEvent *self) {
  return self->QToolBarChangeEvent::clone();
}

#endif  // !defined(QT_NO_TOOLBAR)
