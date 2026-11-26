//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <cstring>

//  A QPlatformSurfaceEvent that Python can take functions over in. Every QPlatformSurfaceEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformSurfaceEventCall0)(const void *, int *);
typedef void (*CuteQPlatformSurfaceEventCall1)(const void *, bool, int *);
class CuteQPlatformSurfaceEvent : public QPlatformSurfaceEvent {
public:
  using QPlatformSurfaceEvent::QPlatformSurfaceEvent;
  CuteQPlatformSurfaceEvent(const QPlatformSurfaceEvent & other) : QPlatformSurfaceEvent(other) {}
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

  //  QPlatformSurfaceEvent *QPlatformSurfaceEvent::clone() const
  QPlatformSurfaceEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformSurfaceEventCall0 call = reinterpret_cast<CuteQPlatformSurfaceEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurfaceEvent *>(given);
    }
    return QPlatformSurfaceEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformSurfaceEventCall1 call = reinterpret_cast<CuteQPlatformSurfaceEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QPlatformSurfaceEvent::QPlatformSurfaceEvent(const QPlatformSurfaceEvent
//      &a0)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent *ritual_ZN21QPlatformSurfaceEventC1ERKS_(
    const QPlatformSurfaceEvent *a0) {
  return new CuteQPlatformSurfaceEvent(*a0);
}

//  QPlatformSurfaceEvent &QPlatformSurfaceEvent::operator=(const
//      QPlatformSurfaceEvent &other)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent *ritual_ZN21QPlatformSurfaceEventaSERKS_(
    QPlatformSurfaceEvent *self,
    const QPlatformSurfaceEvent *other) {
  return &(self->operator=(*other));
}

//  QPlatformSurfaceEvent *QPlatformSurfaceEvent::clone() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent *ritual_ZNK21QPlatformSurfaceEvent5cloneEv(
    const QPlatformSurfaceEvent *self) {
  return self->clone();
}

//  QPlatformSurfaceEvent::~QPlatformSurfaceEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformSurfaceEventD1Ev(QPlatformSurfaceEvent *self) {
  delete self;
}

//  QPlatformSurfaceEvent::QPlatformSurfaceEvent(SurfaceEventType
//      surfaceEventType)
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent *ritual_ZN21QPlatformSurfaceEventC1ENS_16SurfaceEventTypeE(
    QPlatformSurfaceEvent::SurfaceEventType surfaceEventType) {
  return new CuteQPlatformSurfaceEvent(surfaceEventType);
}

//  SurfaceEventType QPlatformSurfaceEvent::surfaceEventType() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent::SurfaceEventType ritual_ZNK21QPlatformSurfaceEvent16surfaceEventTypeEv(
    const QPlatformSurfaceEvent *self) {
  return self->surfaceEventType();
}

//  a Python function taken by a CuteQPlatformSurfaceEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformSurfaceEvent(
    QPlatformSurfaceEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformSurfaceEvent *>(self)->take(key, call);
}

//  QPlatformSurfaceEvent *QPlatformSurfaceEvent::clone() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent *ritual_own_ZNK21QPlatformSurfaceEvent5cloneEv(
    const QPlatformSurfaceEvent *self) {
  return self->QPlatformSurfaceEvent::clone();
}
