//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandiviapplication.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandiviapplication.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtWaylandCompositor/qwaylandresource.h>
#include <cstring>

//  A QWaylandIviApplication that Python can take functions over in. Every QWaylandIviApplication
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandIviApplicationCall0)(const void *, int *);
class CuteQWaylandIviApplication : public QWaylandIviApplication {
public:
  using QWaylandIviApplication::QWaylandIviApplication;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QWaylandIviApplication10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandIviApplication::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandIviApplicationCall0 call = reinterpret_cast<CuteQWaylandIviApplicationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandIviApplication::initialize();
  }
};

//  const QMetaObject *QWaylandIviApplication::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QWaylandIviApplication10metaObjectEv(
    const QWaylandIviApplication *self) {
  return self->metaObject();
}

//  void *QWaylandIviApplication::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QWaylandIviApplication11qt_metacastEPKc(
    QWaylandIviApplication *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandIviApplication::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QWaylandIviApplication11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandIviApplication *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandIviApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QWaylandIviApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandIviApplication::tr(s, c, n));
}

//  QWaylandIviApplicationPrivate *QWaylandIviApplication::d_func()
extern "C" Q_DECL_EXPORT
QWaylandIviApplicationPrivate *ritual_ZN22QWaylandIviApplication6d_funcEv(
    QWaylandIviApplication *self) {
  return self->d_func();
}

//  const QWaylandIviApplicationPrivate *QWaylandIviApplication::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QWaylandIviApplicationPrivate *ritual_ZNK22QWaylandIviApplication6d_funcEv(
    const QWaylandIviApplication *self) {
  return self->d_func();
}

//  QWaylandIviApplication::QWaylandIviApplication()
extern "C" Q_DECL_EXPORT
QWaylandIviApplication *ritual_ZN22QWaylandIviApplicationC1Ev() {
  return new CuteQWaylandIviApplication();
}

//  QWaylandIviApplication::QWaylandIviApplication(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
QWaylandIviApplication *ritual_ZN22QWaylandIviApplicationC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandIviApplication(compositor);
}

//  void QWaylandIviApplication::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandIviApplication10initializeEv(
    QWaylandIviApplication *self) {
  self->initialize();
}

//  const struct wl_interface *QWaylandIviApplication::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN22QWaylandIviApplication9interfaceEv() {
  return QWaylandIviApplication::interface();
}

//  QByteArray QWaylandIviApplication::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QWaylandIviApplication13interfaceNameEv() {
  return new QByteArray(QWaylandIviApplication::interfaceName());
}

//  void QWaylandIviApplication::iviSurfaceRequested(QWaylandSurface
//      *surface, uint iviId, const QWaylandResource &resource)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandIviApplication19iviSurfaceRequestedEP15QWaylandSurfacejRK16QWaylandResource(
    QWaylandIviApplication *self,
    QWaylandSurface *surface,
    uint iviId,
    const QWaylandResource *resource) {
  self->iviSurfaceRequested(surface, iviId, *resource);
}

//  void QWaylandIviApplication::iviSurfaceCreated(QWaylandIviSurface
//      *iviSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWaylandIviApplication17iviSurfaceCreatedEP18QWaylandIviSurface(
    QWaylandIviApplication *self,
    QWaylandIviSurface *iviSurface) {
  self->iviSurfaceCreated(iviSurface);
}

//  a Python function taken by a CuteQWaylandIviApplication, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandIviApplication(
    QWaylandIviApplication *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandIviApplication *>(self)->take(key, call);
}

//  void QWaylandIviApplication::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QWaylandIviApplication10initializeEv(
    QWaylandIviApplication *self) {
  self->QWaylandIviApplication::initialize();
}
