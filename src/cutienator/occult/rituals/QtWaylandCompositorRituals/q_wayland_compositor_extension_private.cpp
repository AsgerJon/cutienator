//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorextension_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandcompositorextension.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandcompositorextension_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWaylandCompositorExtension *QWaylandCompositorExtensionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtension *ritual_ZN34QWaylandCompositorExtensionPrivate6q_funcEv(
    QWaylandCompositorExtensionPrivate *self) {
  return self->q_func();
}

//  const QWaylandCompositorExtension
//      *QWaylandCompositorExtensionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWaylandCompositorExtension *ritual_ZNK34QWaylandCompositorExtensionPrivate6q_funcEv(
    const QWaylandCompositorExtensionPrivate *self) {
  return self->q_func();
}

//  QWaylandCompositorExtensionPrivate::QWaylandCompositorExtensionPrivate()
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtensionPrivate *ritual_ZN34QWaylandCompositorExtensionPrivateC1Ev() {
  return new QWaylandCompositorExtensionPrivate();
}

//  QWaylandCompositorExtensionPrivate
//      *QWaylandCompositorExtensionPrivate::get(QWaylandCompositorExtension
//      *extension)
extern "C" Q_DECL_EXPORT
QWaylandCompositorExtensionPrivate *ritual_ZN34QWaylandCompositorExtensionPrivate3getEP27QWaylandCompositorExtension(
    QWaylandCompositorExtension *extension) {
  return QWaylandCompositorExtensionPrivate::get(extension);
}
