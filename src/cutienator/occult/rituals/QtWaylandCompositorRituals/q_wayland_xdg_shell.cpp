//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandxdgshell.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  const QMetaObject *QWaylandXdgShell::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QWaylandXdgShell10metaObjectEv(
    const QWaylandXdgShell *self) {
  return self->metaObject();
}

//  void *QWaylandXdgShell::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QWaylandXdgShell11qt_metacastEPKc(
    QWaylandXdgShell *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandXdgShell::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QWaylandXdgShell11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandXdgShell *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandXdgShell::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QWaylandXdgShell2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgShell::tr(s, c, n));
}

//  QWaylandXdgShellPrivate *QWaylandXdgShell::d_func()
extern "C" Q_DECL_EXPORT
QWaylandXdgShellPrivate *ritual_ZN16QWaylandXdgShell6d_funcEv(
    QWaylandXdgShell *self) {
  return self->d_func();
}

//  const QWaylandXdgShellPrivate *QWaylandXdgShell::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandXdgShellPrivate *ritual_ZNK16QWaylandXdgShell6d_funcEv(
    const QWaylandXdgShell *self) {
  return self->d_func();
}

//  QWaylandXdgShell::QWaylandXdgShell()
extern "C" Q_DECL_EXPORT
QWaylandXdgShell *ritual_ZN16QWaylandXdgShellC1Ev() {
  return new QWaylandXdgShell();
}

//  QWaylandXdgShell::QWaylandXdgShell(QWaylandCompositor *compositor)
extern "C" Q_DECL_EXPORT
QWaylandXdgShell *ritual_ZN16QWaylandXdgShellC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new QWaylandXdgShell(compositor);
}

//  void QWaylandXdgShell::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell10initializeEv(QWaylandXdgShell *self) {
  self->initialize();
}

//  const struct wl_interface *QWaylandXdgShell::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN16QWaylandXdgShell9interfaceEv() {
  return QWaylandXdgShell::interface();
}

//  QByteArray QWaylandXdgShell::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN16QWaylandXdgShell13interfaceNameEv() {
  return new QByteArray(QWaylandXdgShell::interfaceName());
}

//  uint QWaylandXdgShell::ping(QWaylandClient *client)
extern "C" Q_DECL_EXPORT
uint ritual_ZN16QWaylandXdgShell4pingEP14QWaylandClient(
    QWaylandXdgShell *self,
    QWaylandClient *client) {
  return self->ping(client);
}

//  void QWaylandXdgShell::xdgSurfaceCreated(QWaylandXdgSurface *xdgSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell17xdgSurfaceCreatedEP18QWaylandXdgSurface(
    QWaylandXdgShell *self,
    QWaylandXdgSurface *xdgSurface) {
  self->xdgSurfaceCreated(xdgSurface);
}

//  void QWaylandXdgShell::toplevelCreated(QWaylandXdgToplevel *toplevel,
//      QWaylandXdgSurface *xdgSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell15toplevelCreatedEP19QWaylandXdgToplevelP18QWaylandXdgSurface(
    QWaylandXdgShell *self,
    QWaylandXdgToplevel *toplevel,
    QWaylandXdgSurface *xdgSurface) {
  self->toplevelCreated(toplevel, xdgSurface);
}

//  void QWaylandXdgShell::popupCreated(QWaylandXdgPopup *popup,
//      QWaylandXdgSurface *xdgSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell12popupCreatedEP16QWaylandXdgPopupP18QWaylandXdgSurface(
    QWaylandXdgShell *self,
    QWaylandXdgPopup *popup,
    QWaylandXdgSurface *xdgSurface) {
  self->popupCreated(popup, xdgSurface);
}

//  void QWaylandXdgShell::pong(uint serial)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell4pongEj(
    QWaylandXdgShell *self,
    uint serial) {
  self->pong(serial);
}

//  void QWaylandXdgShell::handleSeatChanged(QWaylandSeat *newSeat,
//      QWaylandSeat *oldSeat)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell17handleSeatChangedEP12QWaylandSeatS1_(
    QWaylandXdgShell *self,
    QWaylandSeat *newSeat,
    QWaylandSeat *oldSeat) {
  self->handleSeatChanged(newSeat, oldSeat);
}

//  void QWaylandXdgShell::handleFocusChanged(QWaylandSurface *newSurface,
//      QWaylandSurface *oldSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWaylandXdgShell18handleFocusChangedEP15QWaylandSurfaceS1_(
    QWaylandXdgShell *self,
    QWaylandSurface *newSurface,
    QWaylandSurface *oldSurface) {
  self->handleFocusChanged(newSurface, oldSurface);
}

//  void QWaylandXdgShell::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QWaylandXdgShell10initializeEv(QWaylandXdgShell *self) {
  self->QWaylandXdgShell::initialize();
}
