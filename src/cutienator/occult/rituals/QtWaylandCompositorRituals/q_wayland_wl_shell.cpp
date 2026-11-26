//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandwlshell.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandwlshell.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWaylandWlShell that Python can take functions over in. Every QWaylandWlShell
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandWlShellCall0)(const void *, int *);
class CuteQWaylandWlShell : public QWaylandWlShell {
public:
  using QWaylandWlShell::QWaylandWlShell;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QWaylandWlShell10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandWlShell::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandWlShellCall0 call = reinterpret_cast<CuteQWaylandWlShellCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandWlShell::initialize();
  }
};

//  const QMetaObject *QWaylandWlShell::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QWaylandWlShell10metaObjectEv(
    const QWaylandWlShell *self) {
  return self->metaObject();
}

//  void *QWaylandWlShell::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QWaylandWlShell11qt_metacastEPKc(
    QWaylandWlShell *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandWlShell::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QWaylandWlShell11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandWlShell *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandWlShell::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QWaylandWlShell2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandWlShell::tr(s, c, n));
}

//  QWaylandWlShellPrivate *QWaylandWlShell::d_func()
extern "C" Q_DECL_EXPORT
QWaylandWlShellPrivate *ritual_ZN15QWaylandWlShell6d_funcEv(
    QWaylandWlShell *self) {
  return self->d_func();
}

//  const QWaylandWlShellPrivate *QWaylandWlShell::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandWlShellPrivate *ritual_ZNK15QWaylandWlShell6d_funcEv(
    const QWaylandWlShell *self) {
  return self->d_func();
}

//  QWaylandWlShell::QWaylandWlShell()
extern "C" Q_DECL_EXPORT
QWaylandWlShell *ritual_ZN15QWaylandWlShellC1Ev() {
  return new CuteQWaylandWlShell();
}

//  QWaylandWlShell::QWaylandWlShell(QWaylandCompositor *compositor)
extern "C" Q_DECL_EXPORT
QWaylandWlShell *ritual_ZN15QWaylandWlShellC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandWlShell(compositor);
}

//  void QWaylandWlShell::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandWlShell10initializeEv(QWaylandWlShell *self) {
  self->initialize();
}

//  QList<QWaylandWlShellSurface *> QWaylandWlShell::shellSurfaces() const
extern "C" Q_DECL_EXPORT
QList<QWaylandWlShellSurface *> *ritual_ZNK15QWaylandWlShell13shellSurfacesEv(
    const QWaylandWlShell *self) {
  return new QList<QWaylandWlShellSurface *>(self->shellSurfaces());
}

//  QList<QWaylandWlShellSurface *>
//      QWaylandWlShell::shellSurfacesForClient(QWaylandClient *client) const
extern "C" Q_DECL_EXPORT
QList<QWaylandWlShellSurface *> *ritual_ZNK15QWaylandWlShell22shellSurfacesForClientEP14QWaylandClient(
    const QWaylandWlShell *self,
    QWaylandClient *client) {
  return new QList<QWaylandWlShellSurface *>(
      self->shellSurfacesForClient(
          client));
}

//  QList<QWaylandWlShellSurface *> QWaylandWlShell::mappedPopups() const
extern "C" Q_DECL_EXPORT
QList<QWaylandWlShellSurface *> *ritual_ZNK15QWaylandWlShell12mappedPopupsEv(
    const QWaylandWlShell *self) {
  return new QList<QWaylandWlShellSurface *>(self->mappedPopups());
}

//  QWaylandClient *QWaylandWlShell::popupClient() const
extern "C" Q_DECL_EXPORT
QWaylandClient *ritual_ZNK15QWaylandWlShell11popupClientEv(
    const QWaylandWlShell *self) {
  return self->popupClient();
}

//  const struct wl_interface *QWaylandWlShell::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN15QWaylandWlShell9interfaceEv() {
  return QWaylandWlShell::interface();
}

//  QByteArray QWaylandWlShell::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN15QWaylandWlShell13interfaceNameEv() {
  return new QByteArray(QWaylandWlShell::interfaceName());
}

//  void QWaylandWlShell::closeAllPopups()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandWlShell14closeAllPopupsEv(QWaylandWlShell *self) {
  self->closeAllPopups();
}

//  void QWaylandWlShell::wlShellSurfaceRequested(QWaylandSurface *surface,
//      const QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandWlShell23wlShellSurfaceRequestedEP15QWaylandSurfaceRK16QWaylandResource(
    QWaylandWlShell *self,
    QWaylandSurface *surface,
    const QWaylandResource *resource) {
  self->wlShellSurfaceRequested(surface, *resource);
}

//  void QWaylandWlShell::wlShellSurfaceCreated(QWaylandWlShellSurface
//      *shellSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QWaylandWlShell21wlShellSurfaceCreatedEP22QWaylandWlShellSurface(
    QWaylandWlShell *self,
    QWaylandWlShellSurface *shellSurface) {
  self->wlShellSurfaceCreated(shellSurface);
}

//  a Python function taken by a CuteQWaylandWlShell, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandWlShell(
    QWaylandWlShell *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandWlShell *>(self)->take(key, call);
}

//  void QWaylandWlShell::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QWaylandWlShell10initializeEv(QWaylandWlShell *self) {
  self->QWaylandWlShell::initialize();
}
