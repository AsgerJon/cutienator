//  Written by hand on 2026-11-25 from
//  QtWaylandCompositorXdgShell/6.12.0/QtWaylandCompositorXdgShell/private/
//  qwaylandcompositorxdgshell_p.h, Qt 6.12.0, from Qt's source. Kept as it
//  is when the generator runs again.
//  Qt builds the part only where QtWaylandCompositor has
//  'wayland-compositor-quick', so the file stands under
//  QT_CONFIG(wayland_compositor_quick).
//  An empty struct whose class line has no export macro; it only
//  tells QML, by QML_FOREIGN, the name XdgToplevel of
//  QWaylandXdgToplevel, and by QML_UNCREATABLE that QML makes none.
//  Q_GADGET gives it staticMetaObject, a variable, and no function to
//  call. Written: the implicit destructor and what the QML macros
//  give it, all inline.
//  Not written: its implicit constructors, which a class Qt does not
//  export does not get; 'operator='; qt_check_for_QGADGET_macro,
//  which Q_GADGET declares and nothing defines; qt_static_metacall,
//  moc's.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositorXdgShell/6.12.0/QtWaylandCompositorXdgShell/private/qwaylandcompositorxdgshell_p.h>

//  QWaylandXdgTopLevelForeign::~QWaylandXdgTopLevelForeign()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandXdgTopLevelForeignD1Ev(
    QWaylandXdgTopLevelForeign *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
