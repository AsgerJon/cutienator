//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>

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
  return new QPlatformSurfaceEvent(surfaceEventType);
}

//  SurfaceEventType QPlatformSurfaceEvent::surfaceEventType() const
extern "C" Q_DECL_EXPORT
QPlatformSurfaceEvent::SurfaceEventType ritual_ZNK21QPlatformSurfaceEvent16surfaceEventTypeEv(
    const QPlatformSurfaceEvent *self) {
  return self->surfaceEventType();
}
