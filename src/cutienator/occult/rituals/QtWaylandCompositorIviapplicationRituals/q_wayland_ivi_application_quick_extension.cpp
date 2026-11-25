//  Written by hand on 2026-11-25 from
//  QtWaylandCompositorIviapplication/6.12.0/
//  QtWaylandCompositorIviapplication/private/
//  qwaylandcompositoriviapplicationforeign_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt builds the part only where QtWaylandCompositor has
//  'wayland-compositor-quick', so the file stands under
//  QT_CONFIG(wayland_compositor_quick).
//  The class is made by Q_COMPOSITOR_DECLARE_QUICK_EXTENSION_NAMED_ELEMENT
//  of qwaylandquickextension.h. Its class line carries
//  'Q_WAYLANDCOMPOSITOR_EXPORT', the macro of QtWaylandCompositor,
//  which in this part's library says import, and the part has no
//  export macro of its own: Qt does not export the class, so only its
//  virtual functions are called, through the object.
//  Not written: the constructor and 'tr'; 'data', which gives a
//  'QQmlListProperty', a template.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositorIviapplication/6.12.0/QtWaylandCompositorIviapplication/private/qwaylandcompositoriviapplicationforeign_p.h>

//  const QMetaObject *QWaylandIviApplicationQuickExtension::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK36QWaylandIviApplicationQuickExtension10metaObjectEv(
    const QWaylandIviApplicationQuickExtension *self) {
  return self->metaObject();
}

//  QWaylandIviApplicationQuickExtension::
//      ~QWaylandIviApplicationQuickExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWaylandIviApplicationQuickExtensionD1Ev(
    QWaylandIviApplicationQuickExtension *self) {
  delete self;
}

//  void QWaylandIviApplicationQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWaylandIviApplicationQuickExtension10classBeginEv(
    QWaylandIviApplicationQuickExtension *self) {
  self->classBegin();
}

//  void QWaylandIviApplicationQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWaylandIviApplicationQuickExtension17componentCompleteEv(
    QWaylandIviApplicationQuickExtension *self) {
  self->componentComplete();
}

//  QWaylandIviApplicationQuickExtension as the QQmlParserStatus it is built
//      on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandIviApplicationQuickExtension_QQmlParserStatus(
    QWaylandIviApplicationQuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
