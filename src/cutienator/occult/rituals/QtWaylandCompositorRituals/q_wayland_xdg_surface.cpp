//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandxdgshell.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <QtCore/qrect.h>
#include <QtCore/qbytearray.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  const QMetaObject *QWaylandXdgSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWaylandXdgSurface10metaObjectEv(
    const QWaylandXdgSurface *self) {
  return self->metaObject();
}

//  void *QWaylandXdgSurface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QWaylandXdgSurface11qt_metacastEPKc(
    QWaylandXdgSurface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandXdgSurface::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QWaylandXdgSurface11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandXdgSurface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandXdgSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandXdgSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgSurface::tr(s, c, n));
}

//  QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func()
extern "C" Q_DECL_EXPORT
QWaylandXdgSurfacePrivate *ritual_ZN18QWaylandXdgSurface6d_funcEv(
    QWaylandXdgSurface *self) {
  return self->d_func();
}

//  const QWaylandXdgSurfacePrivate *QWaylandXdgSurface::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandXdgSurfacePrivate *ritual_ZNK18QWaylandXdgSurface6d_funcEv(
    const QWaylandXdgSurface *self) {
  return self->d_func();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QQmlListProperty<QObject> QWaylandXdgSurface::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN18QWaylandXdgSurface4dataEv(
    QWaylandXdgSurface *self) {
  return new QQmlListProperty<QObject>(self->data());
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  void QWaylandXdgSurface::appendFunction(QQmlListProperty<QObject> *list,
//      QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface14appendFunctionEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *object) {
  QWaylandXdgSurface::appendFunction(list, object);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  qsizetype QWaylandXdgSurface::countFunction(QQmlListProperty<QObject>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN18QWaylandXdgSurface13countFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  return QWaylandXdgSurface::countFunction(list);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  QObject *QWaylandXdgSurface::atFunction(QQmlListProperty<QObject> *list,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN18QWaylandXdgSurface10atFunctionEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *list,
    qsizetype index) {
  return QWaylandXdgSurface::atFunction(list, index);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  void QWaylandXdgSurface::clearFunction(QQmlListProperty<QObject> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface13clearFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  QWaylandXdgSurface::clearFunction(list);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

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

//  const struct wl_interface *QWaylandXdgSurface::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN18QWaylandXdgSurface9interfaceEv() {
  return QWaylandXdgSurface::interface();
}

//  QByteArray QWaylandXdgSurface::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN18QWaylandXdgSurface13interfaceNameEv() {
  return new QByteArray(QWaylandXdgSurface::interfaceName());
}

//  QWaylandXdgSurface *QWaylandXdgSurface::fromResource(::wl_resource
//      *resource)
extern "C" Q_DECL_EXPORT
QWaylandXdgSurface *ritual_ZN18QWaylandXdgSurface12fromResourceEP11wl_resource(
    ::wl_resource *resource) {
  return QWaylandXdgSurface::fromResource(resource);
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

//  void QWaylandXdgSurface::shellChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface12shellChangedEv(
    QWaylandXdgSurface *self) {
  self->shellChanged();
}

//  void QWaylandXdgSurface::surfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface14surfaceChangedEv(
    QWaylandXdgSurface *self) {
  self->surfaceChanged();
}

//  void QWaylandXdgSurface::toplevelCreated()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface15toplevelCreatedEv(
    QWaylandXdgSurface *self) {
  self->toplevelCreated();
}

//  void QWaylandXdgSurface::popupCreated()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface12popupCreatedEv(
    QWaylandXdgSurface *self) {
  self->popupCreated();
}

//  void QWaylandXdgSurface::windowGeometryChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandXdgSurface21windowGeometryChangedEv(
    QWaylandXdgSurface *self) {
  self->windowGeometryChanged();
}

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

//  a QQmlListProperty<QObject> a ritual of QWaylandXdgSurface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandXdgSurface__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
