//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtGui/qregion.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QPaintEvent that Python can take functions over in. Every QPaintEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPaintEventCall0)(const void *, int *);
typedef void (*CuteQPaintEventCall1)(const void *, bool, int *);
class CuteQPaintEvent : public QPaintEvent {
public:
  using QPaintEvent::QPaintEvent;
  CuteQPaintEvent(const QPaintEvent & other) : QPaintEvent(other) {}
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

  //  QPaintEvent *QPaintEvent::clone() const
  QPaintEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintEventCall0 call = reinterpret_cast<CuteQPaintEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEvent *>(given);
    }
    return QPaintEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintEventCall1 call = reinterpret_cast<CuteQPaintEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QPaintEvent::QPaintEvent(const QPaintEvent &a0)
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZN11QPaintEventC1ERKS_(const QPaintEvent *a0) {
  return new CuteQPaintEvent(*a0);
}

//  QPaintEvent &QPaintEvent::operator=(const QPaintEvent &other)
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZN11QPaintEventaSERKS_(
    QPaintEvent *self,
    const QPaintEvent *other) {
  return &(self->operator=(*other));
}

//  QPaintEvent *QPaintEvent::clone() const
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZNK11QPaintEvent5cloneEv(const QPaintEvent *self) {
  return self->clone();
}

//  QPaintEvent::~QPaintEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPaintEventD1Ev(QPaintEvent *self) {
  delete self;
}

//  QPaintEvent::QPaintEvent(const QRegion &paintRegion)
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZN11QPaintEventC1ERK7QRegion(
    const QRegion *paintRegion) {
  return new CuteQPaintEvent(*paintRegion);
}

//  QPaintEvent::QPaintEvent(const QRect &paintRect)
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_ZN11QPaintEventC1ERK5QRect(const QRect *paintRect) {
  return new CuteQPaintEvent(*paintRect);
}

//  const QRect &QPaintEvent::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QPaintEvent4rectEv(const QPaintEvent *self) {
  return new QRect(self->rect());
}

//  const QRegion &QPaintEvent::region() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK11QPaintEvent6regionEv(const QPaintEvent *self) {
  return new QRegion(self->region());
}

//  a Python function taken by a CuteQPaintEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintEvent(
    QPaintEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintEvent *>(self)->take(key, call);
}

//  QPaintEvent *QPaintEvent::clone() const
extern "C" Q_DECL_EXPORT
QPaintEvent *ritual_own_ZNK11QPaintEvent5cloneEv(const QPaintEvent *self) {
  return self->QPaintEvent::clone();
}
