//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtWayland::surface_buffer_destroy_listener::~surface_buffer_destroy_liste
//      ner()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland31surface_buffer_destroy_listenerD1Ev(
    QtWayland::surface_buffer_destroy_listener *self) {
  delete self;
}
