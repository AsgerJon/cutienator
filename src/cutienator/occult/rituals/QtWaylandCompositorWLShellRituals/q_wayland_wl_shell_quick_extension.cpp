//  Written by hand on 2026-11-25 from
//  QtWaylandCompositorWLShell/6.12.0/QtWaylandCompositorWLShell/private/
//  qwaylandcompositorwlshell_p.h, Qt 6.12.0, from Qt's source. Kept as it is
//  when the generator runs again.
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
#include <QtWaylandCompositorWLShell/6.12.0/QtWaylandCompositorWLShell/private/qwaylandcompositorwlshell_p.h>

//  const QMetaObject *QWaylandWlShellQuickExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QWaylandWlShellQuickExtension10metaObjectEv(
    const QWaylandWlShellQuickExtension *self) {
  return self->metaObject();
}

//  QWaylandWlShellQuickExtension::~QWaylandWlShellQuickExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandWlShellQuickExtensionD1Ev(
    QWaylandWlShellQuickExtension *self) {
  delete self;
}

//  void QWaylandWlShellQuickExtension::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandWlShellQuickExtension10classBeginEv(
    QWaylandWlShellQuickExtension *self) {
  self->classBegin();
}

//  void QWaylandWlShellQuickExtension::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWaylandWlShellQuickExtension17componentCompleteEv(
    QWaylandWlShellQuickExtension *self) {
  self->componentComplete();
}

//  QWaylandWlShellQuickExtension as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandWlShellQuickExtension_QQmlParserStatus(
    QWaylandWlShellQuickExtension *self) {
  return static_cast<QQmlParserStatus *>(self);
}

#endif  // QT_CONFIG(wayland_compositor_quick)
