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

//  QString QWaylandXdgShell::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QWaylandXdgShell2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgShell::tr(s, c, n));
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
