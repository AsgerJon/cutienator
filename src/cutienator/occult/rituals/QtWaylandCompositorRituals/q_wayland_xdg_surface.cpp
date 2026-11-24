//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandxdgshell.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <QtCore/qrect.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QWaylandXdgSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWaylandXdgSurface10metaObjectEv(
    const QWaylandXdgSurface *self) {
  return self->metaObject();
}

//  QString QWaylandXdgSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandXdgSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgSurface::tr(s, c, n));
}

//  QWaylandXdgSurface::QWaylandXdgSurface()
extern "C" Q_DECL_EXPORT
QWaylandXdgSurface *ritual_ZN18QWaylandXdgSurfaceC1Ev() {
  return new QWaylandXdgSurface();
}

//  QWaylandXdgSurface::QWaylandXdgSurface(QWaylandXdgShell *xdgShell,
//      QWaylandSurface *surface, const QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
QWaylandXdgSurface *ritual_ZN18QWaylandXdgSurfaceC1EP16QWaylandXdgShellP15QWaylandSurfaceRK16QWaylandResource(
    QWaylandXdgShell *xdgShell,
    QWaylandSurface *surface,
    const QWaylandResource *resource) {
  return new QWaylandXdgSurface(xdgShell, surface, *resource);
}

//  void QWaylandXdgSurface::initialize(QWaylandXdgShell *xdgShell,
//      QWaylandSurface *surface, const QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface10initializeEP16QWaylandXdgShellP15QWaylandSurfaceRK16QWaylandResource(
    QWaylandXdgSurface *self,
    QWaylandXdgShell *xdgShell,
    QWaylandSurface *surface,
    const QWaylandResource *resource) {
  self->initialize(xdgShell, surface, *resource);
}

//  Qt::WindowType QWaylandXdgSurface::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_ZNK18QWaylandXdgSurface10windowTypeEv(
    const QWaylandXdgSurface *self) {
  return self->windowType();
}

//  QWaylandXdgShell *QWaylandXdgSurface::shell() const
extern "C" Q_DECL_EXPORT
QWaylandXdgShell *ritual_ZNK18QWaylandXdgSurface5shellEv(
    const QWaylandXdgSurface *self) {
  return self->shell();
}

//  QWaylandSurface *QWaylandXdgSurface::surface() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK18QWaylandXdgSurface7surfaceEv(
    const QWaylandXdgSurface *self) {
  return self->surface();
}

//  QWaylandXdgToplevel *QWaylandXdgSurface::toplevel() const
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevel *ritual_ZNK18QWaylandXdgSurface8toplevelEv(
    const QWaylandXdgSurface *self) {
  return self->toplevel();
}

//  QWaylandXdgPopup *QWaylandXdgSurface::popup() const
extern "C" Q_DECL_EXPORT
QWaylandXdgPopup *ritual_ZNK18QWaylandXdgSurface5popupEv(
    const QWaylandXdgSurface *self) {
  return self->popup();
}

//  QRect QWaylandXdgSurface::windowGeometry() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK18QWaylandXdgSurface14windowGeometryEv(
    const QWaylandXdgSurface *self) {
  return new QRect(self->windowGeometry());
}

//  QByteArray QWaylandXdgSurface::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QWaylandXdgSurface13interfaceNameEv() {
  return new QByteArray(QWaylandXdgSurface::interfaceName());
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandXdgSurface::createIntegration(QWaylandQuickShellSurfaceItem
//      *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_ZN18QWaylandXdgSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandXdgSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  void QWaylandXdgSurface::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface10initializeEv(QWaylandXdgSurface *self) {
  self->initialize();
}

//  void QWaylandXdgSurface::handleSurfaceSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface24handleSurfaceSizeChangedEv(
    QWaylandXdgSurface *self) {
  self->handleSurfaceSizeChanged();
}

//  void QWaylandXdgSurface::handleBufferScaleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface24handleBufferScaleChangedEv(
    QWaylandXdgSurface *self) {
  self->handleBufferScaleChanged();
}

//  Qt::WindowType QWaylandXdgSurface::windowType() const
extern "C" Q_DECL_EXPORT
Qt::WindowType ritual_own_ZNK18QWaylandXdgSurface10windowTypeEv(
    const QWaylandXdgSurface *self) {
  return self->QWaylandXdgSurface::windowType();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandXdgSurface::createIntegration(QWaylandQuickShellSurfaceItem
//      *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_own_ZN18QWaylandXdgSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandXdgSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->QWaylandXdgSurface::createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  void QWaylandXdgSurface::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWaylandXdgSurface10initializeEv(
    QWaylandXdgSurface *self) {
  self->QWaylandXdgSurface::initialize();
}
