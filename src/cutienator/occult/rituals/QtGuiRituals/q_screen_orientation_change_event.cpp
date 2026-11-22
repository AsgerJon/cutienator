//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QScreenOrientationChangeEvent that Python can take functions over in. Every QScreenOrientationChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScreenOrientationChangeEventCall0)(const void *, int *);
typedef void (*CuteQScreenOrientationChangeEventCall1)(const void *, bool, int *);
class CuteQScreenOrientationChangeEvent : public QScreenOrientationChangeEvent {
public:
  using QScreenOrientationChangeEvent::QScreenOrientationChangeEvent;
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

  //  QScreenOrientationChangeEvent *QScreenOrientationChangeEvent::clone()
  //      const
  QScreenOrientationChangeEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScreenOrientationChangeEventCall0 call = reinterpret_cast<CuteQScreenOrientationChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QScreenOrientationChangeEvent *>(given);
    }
    return QScreenOrientationChangeEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScreenOrientationChangeEventCall1 call = reinterpret_cast<CuteQScreenOrientationChangeEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QScreenOrientationChangeEvent *QScreenOrientationChangeEvent::clone()
//      const
extern "C" Q_DECL_EXPORT
QScreenOrientationChangeEvent *ritual_ZNK29QScreenOrientationChangeEvent5cloneEv(
    const QScreenOrientationChangeEvent *self) {
  return self->clone();
}

//  QScreenOrientationChangeEvent::~QScreenOrientationChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QScreenOrientationChangeEventD1Ev(
    QScreenOrientationChangeEvent *self) {
  delete self;
}

//  QScreenOrientationChangeEvent::QScreenOrientationChangeEvent(QScreen
//      *screen, Qt::ScreenOrientation orientation)
extern "C" Q_DECL_EXPORT
QScreenOrientationChangeEvent *ritual_ZN29QScreenOrientationChangeEventC1EP7QScreenN2Qt17ScreenOrientationE(
    QScreen *screen,
    Qt::ScreenOrientation orientation) {
  return new CuteQScreenOrientationChangeEvent(screen, orientation);
}

//  QScreen *QScreenOrientationChangeEvent::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK29QScreenOrientationChangeEvent6screenEv(
    const QScreenOrientationChangeEvent *self) {
  return self->screen();
}

//  Qt::ScreenOrientation QScreenOrientationChangeEvent::orientation() const
extern "C" Q_DECL_EXPORT
Qt::ScreenOrientation ritual_ZNK29QScreenOrientationChangeEvent11orientationEv(
    const QScreenOrientationChangeEvent *self) {
  return self->orientation();
}

//  a Python function taken by a CuteQScreenOrientationChangeEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScreenOrientationChangeEvent(
    QScreenOrientationChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScreenOrientationChangeEvent *>(self)->take(key, call);
}

//  QScreenOrientationChangeEvent *QScreenOrientationChangeEvent::clone()
//      const
extern "C" Q_DECL_EXPORT
QScreenOrientationChangeEvent *ritual_own_ZNK29QScreenOrientationChangeEvent5cloneEv(
    const QScreenOrientationChangeEvent *self) {
  return self->QScreenOrientationChangeEvent::clone();
}
