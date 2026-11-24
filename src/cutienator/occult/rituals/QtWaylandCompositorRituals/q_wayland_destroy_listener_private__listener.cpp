//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylanddestroylistener_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylanddestroylistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWaylandDestroyListenerPrivate::Listener::~Listener()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWaylandDestroyListenerPrivate8ListenerD1Ev(
    QWaylandDestroyListenerPrivate::Listener *self) {
  delete self;
}
