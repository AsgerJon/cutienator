//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbufferintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
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
