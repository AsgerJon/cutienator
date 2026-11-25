//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegration_p.h,
//  Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<wayland-server-core.h>)', because Qt's header it needs
//  includes the header of the Wayland server library, which a machine with
//  Qt's kit but without the development headers of the Wayland server
//  library lacks. Kept as it is when the generator runs again.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if __has_include(<wayland-server-core.h>)
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtWayland::ClientBufferIntegration::~ClientBufferIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland23ClientBufferIntegrationD1Ev(
    QtWayland::ClientBufferIntegration *self) {
  delete self;
}

//  void QtWayland::ClientBufferIntegration::setCompositor(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland23ClientBufferIntegration13setCompositorEP18QWaylandCompositor(
    QtWayland::ClientBufferIntegration *self,
    QWaylandCompositor *compositor) {
  self->setCompositor(compositor);
}

//  QWaylandCompositor *QtWayland::ClientBufferIntegration::compositor()
//      const
extern "C" Q_DECL_EXPORT
QWaylandCompositor *ritual_ZNK9QtWayland23ClientBufferIntegration10compositorEv(
    const QtWayland::ClientBufferIntegration *self) {
  return self->compositor();
}

#endif  // __has_include(<wayland-server-core.h>)
