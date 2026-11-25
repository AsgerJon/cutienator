//  Written by hand on 2026-11-25 from
//  QtWaylandCompositorXdgShell/6.12.0/QtWaylandCompositorXdgShell/private/
//  qwaylandcompositorxdgshell_p.h, Qt 6.12.0, from Qt's source. Kept as it
//  is when the generator runs again.
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
#include <QtWaylandCompositorXdgShell/6.12.0/QtWaylandCompositorXdgShell/private/qwaylandcompositorxdgshell_p.h>

//  const QMetaObject
//      *QWaylandXdgDecorationManagerV1QuickExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK44QWaylandXdgDecorationManagerV1QuickExtension10metaObjectEv(
    const QWaylandXdgDecorationManagerV1QuickExtension *self) {
  return self->metaObject();
}

//  QWaylandXdgDecorationManagerV1QuickExtension::
//      ~QWaylandXdgDecorationManagerV1QuickExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN44QWaylandXdgDecorationManagerV1QuickExtensionD1Ev(
    QWaylandXdgDecorationManagerV1QuickExtension *self) {
  delete self;
}

//  void QWaylandXdgDecorationManagerV1QuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN44QWaylandXdgDecorationManagerV1QuickExtension10classBeginEv(
    QWaylandXdgDecorationManagerV1QuickExtension *self) {
  self->classBegin();
}

//  void QWaylandXdgDecorationManagerV1QuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN44QWaylandXdgDecorationManagerV1QuickExtension17componentCompleteEv(
    QWaylandXdgDecorationManagerV1QuickExtension *self) {
  self->componentComplete();
}

//  QWaylandXdgDecorationManagerV1QuickExtension as the QQmlParserStatus it
//      is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandXdgDecorationManagerV1QuickExtension_QQmlParserStatus(
    QWaylandXdgDecorationManagerV1QuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
