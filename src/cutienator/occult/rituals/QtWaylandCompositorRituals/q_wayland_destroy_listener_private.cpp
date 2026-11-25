//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylanddestroylistener_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: the constructor is left out, with the
//  code taken for it and for 'handler', which it alone uses: it calls
//  'wl_list_init' of the Wayland library, outside Qt. Kept as it is
//  when the generator runs again.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylanddestroylistener.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylanddestroylistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/qwaylanddestroylistener.h>
#include <QtWaylandCompositor/private/qwaylanddestroylistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWaylandDestroyListener *QWaylandDestroyListenerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandDestroyListener *ritual_ZN30QWaylandDestroyListenerPrivate6q_funcEv(
    QWaylandDestroyListenerPrivate *self) {
  return self->q_func();
}

//  const QWaylandDestroyListener *QWaylandDestroyListenerPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QWaylandDestroyListener *ritual_ZNK30QWaylandDestroyListenerPrivate6q_funcEv(
    const QWaylandDestroyListenerPrivate *self) {
  return self->q_func();
}

