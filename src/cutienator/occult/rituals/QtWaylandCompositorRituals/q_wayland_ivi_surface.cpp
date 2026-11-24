//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandivisurface.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandivisurface.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QWaylandIviSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWaylandIviSurface10metaObjectEv(
    const QWaylandIviSurface *self) {
  return self->metaObject();
}

//  QString QWaylandIviSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandIviSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandIviSurface::tr(s, c, n));
}

//  QWaylandIviSurface::QWaylandIviSurface()
extern "C" Q_DECL_EXPORT
QWaylandIviSurface *ritual_ZN18QWaylandIviSurfaceC1Ev() {
  return new QWaylandIviSurface();
}

//  QWaylandIviSurface::QWaylandIviSurface(QWaylandIviApplication
//      *application, QWaylandSurface *surface, uint iviId, const
//      QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
QWaylandIviSurface *ritual_ZN18QWaylandIviSurfaceC1EP22QWaylandIviApplicationP15QWaylandSurfacejRK16QWaylandResource(
    QWaylandIviApplication *application,
    QWaylandSurface *surface,
    uint iviId,
    const QWaylandResource *resource) {
  return new QWaylandIviSurface(application, surface, iviId, *resource);
}

//  void QWaylandIviSurface::initialize(QWaylandIviApplication
//      *iviApplication, QWaylandSurface *surface, uint iviId, const
//      QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface10initializeEP22QWaylandIviApplicationP15QWaylandSurfacejRK16QWaylandResource(
    QWaylandIviSurface *self,
    QWaylandIviApplication *iviApplication,
    QWaylandSurface *surface,
    uint iviId,
    const QWaylandResource *resource) {
  self->initialize(iviApplication, surface, iviId, *resource);
}

//  QWaylandSurface *QWaylandIviSurface::surface() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK18QWaylandIviSurface7surfaceEv(
    const QWaylandIviSurface *self) {
  return self->surface();
}

//  uint QWaylandIviSurface::iviId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK18QWaylandIviSurface5iviIdEv(const QWaylandIviSurface *self) {
  return self->iviId();
}

//  QByteArray QWaylandIviSurface::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QWaylandIviSurface13interfaceNameEv() {
  return new QByteArray(QWaylandIviSurface::interfaceName());
}

//  QWaylandSurfaceRole *QWaylandIviSurface::role()
extern "C" Q_DECL_EXPORT
QWaylandSurfaceRole *ritual_ZN18QWaylandIviSurface4roleEv() {
  return QWaylandIviSurface::role();
}

//  void QWaylandIviSurface::sendConfigure(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface13sendConfigureERK5QSize(
    QWaylandIviSurface *self,
    const QSize *size) {
  self->sendConfigure(*size);
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandIviSurface::createIntegration(QWaylandQuickShellSurfaceItem
//      *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_ZN18QWaylandIviSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandIviSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  void QWaylandIviSurface::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface10initializeEv(QWaylandIviSurface *self) {
  self->initialize();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QWaylandQuickShellIntegration
//      *QWaylandIviSurface::createIntegration(QWaylandQuickShellSurfaceItem
//      *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellIntegration *ritual_own_ZN18QWaylandIviSurface17createIntegrationEP29QWaylandQuickShellSurfaceItem(
    QWaylandIviSurface *self,
    QWaylandQuickShellSurfaceItem *item) {
  return self->QWaylandIviSurface::createIntegration(item);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

//  void QWaylandIviSurface::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWaylandIviSurface10initializeEv(
    QWaylandIviSurface *self) {
  self->QWaylandIviSurface::initialize();
}
