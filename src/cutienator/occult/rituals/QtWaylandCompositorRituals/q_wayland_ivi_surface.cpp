//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandivisurface.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandivisurface.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qsize.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  const QMetaObject *QWaylandIviSurface::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWaylandIviSurface10metaObjectEv(
    const QWaylandIviSurface *self) {
  return self->metaObject();
}

//  void *QWaylandIviSurface::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QWaylandIviSurface11qt_metacastEPKc(
    QWaylandIviSurface *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandIviSurface::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QWaylandIviSurface11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandIviSurface *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandIviSurface::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandIviSurface2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandIviSurface::tr(s, c, n));
}

//  QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func()
extern "C" Q_DECL_EXPORT
QWaylandIviSurfacePrivate *ritual_ZN18QWaylandIviSurface6d_funcEv(
    QWaylandIviSurface *self) {
  return self->d_func();
}

//  const QWaylandIviSurfacePrivate *QWaylandIviSurface::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandIviSurfacePrivate *ritual_ZNK18QWaylandIviSurface6d_funcEv(
    const QWaylandIviSurface *self) {
  return self->d_func();
}

#if QT_CONFIG(wayland_compositor_quick)
//  QQmlListProperty<QObject> QWaylandIviSurface::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN18QWaylandIviSurface4dataEv(
    QWaylandIviSurface *self) {
  return new QQmlListProperty<QObject>(self->data());
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  void QWaylandIviSurface::appendFunction(QQmlListProperty<QObject> *list,
//      QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface14appendFunctionEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *object) {
  QWaylandIviSurface::appendFunction(list, object);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  qsizetype QWaylandIviSurface::countFunction(QQmlListProperty<QObject>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN18QWaylandIviSurface13countFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  return QWaylandIviSurface::countFunction(list);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  QObject *QWaylandIviSurface::atFunction(QQmlListProperty<QObject> *list,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN18QWaylandIviSurface10atFunctionEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *list,
    qsizetype index) {
  return QWaylandIviSurface::atFunction(list, index);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

#if QT_CONFIG(wayland_compositor_quick)
//  void QWaylandIviSurface::clearFunction(QQmlListProperty<QObject> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface13clearFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  QWaylandIviSurface::clearFunction(list);
}
#endif  // QT_CONFIG(wayland_compositor_quick)

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

//  const struct wl_interface *QWaylandIviSurface::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN18QWaylandIviSurface9interfaceEv() {
  return QWaylandIviSurface::interface();
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

//  QWaylandIviSurface *QWaylandIviSurface::fromResource(::wl_resource
//      *resource)
extern "C" Q_DECL_EXPORT
QWaylandIviSurface *ritual_ZN18QWaylandIviSurface12fromResourceEP11wl_resource(
    ::wl_resource *resource) {
  return QWaylandIviSurface::fromResource(resource);
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

//  void QWaylandIviSurface::surfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface14surfaceChangedEv(
    QWaylandIviSurface *self) {
  self->surfaceChanged();
}

//  void QWaylandIviSurface::iviIdChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandIviSurface12iviIdChangedEv(
    QWaylandIviSurface *self) {
  self->iviIdChanged();
}

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

//  a QQmlListProperty<QObject> a ritual of QWaylandIviSurface gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandIviSurface__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}
