//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandxdgshellintegration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject *QtWayland::XdgPopupIntegration::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QtWayland19XdgPopupIntegration10metaObjectEv(
    const QtWayland::XdgPopupIntegration *self) {
  return self->metaObject();
}

//  void *QtWayland::XdgPopupIntegration::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QtWayland19XdgPopupIntegration11qt_metacastEPKc(
    QtWayland::XdgPopupIntegration *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QtWayland::XdgPopupIntegration::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QtWayland19XdgPopupIntegration11qt_metacallEN11QMetaObject4CallEiPPv(
    QtWayland::XdgPopupIntegration *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QtWayland::XdgPopupIntegration::handleGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtWayland19XdgPopupIntegration21handleGeometryChangedEv(
    QtWayland::XdgPopupIntegration *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QtWayland::XdgPopupIntegration")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleGeometryChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleGeometryChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
