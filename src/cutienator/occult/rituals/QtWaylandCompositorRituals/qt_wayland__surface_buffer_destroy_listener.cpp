//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwlclientbuffer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the whole file stands under
//  '__has_include(<wayland-server-core.h>)', because Qt's header it needs
//  includes the header of the Wayland server library, which a machine with
//  Qt's kit but without the development headers of the Wayland server
//  library lacks. Kept as it is when the generator runs again.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if __has_include(<wayland-server-core.h>)
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

#endif  // __has_include(<wayland-server-core.h>)
