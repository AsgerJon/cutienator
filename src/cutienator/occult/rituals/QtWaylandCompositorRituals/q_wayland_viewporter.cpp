//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandviewporter.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandviewporter.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWaylandViewporter that Python can take functions over in. Every QWaylandViewporter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandViewporterCall0)(const void *, int *);
class CuteQWaylandViewporter : public QWaylandViewporter {
public:
  using QWaylandViewporter::QWaylandViewporter;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN18QWaylandViewporter10initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandViewporter::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandViewporterCall0 call = reinterpret_cast<CuteQWaylandViewporterCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandViewporter::initialize();
  }
};

//  const QMetaObject *QWaylandViewporter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QWaylandViewporter10metaObjectEv(
    const QWaylandViewporter *self) {
  return self->metaObject();
}

//  void *QWaylandViewporter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QWaylandViewporter11qt_metacastEPKc(
    QWaylandViewporter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandViewporter::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QWaylandViewporter11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandViewporter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandViewporter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandViewporter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandViewporter::tr(s, c, n));
}

//  QWaylandViewporterPrivate *QWaylandViewporter::d_func()
extern "C" Q_DECL_EXPORT
QWaylandViewporterPrivate *ritual_ZN18QWaylandViewporter6d_funcEv(
    QWaylandViewporter *self) {
  return self->d_func();
}

//  const QWaylandViewporterPrivate *QWaylandViewporter::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandViewporterPrivate *ritual_ZNK18QWaylandViewporter6d_funcEv(
    const QWaylandViewporter *self) {
  return self->d_func();
}

//  QWaylandViewporter::QWaylandViewporter()
extern "C" Q_DECL_EXPORT
QWaylandViewporter *ritual_ZN18QWaylandViewporterC1Ev() {
  return new CuteQWaylandViewporter();
}

//  QWaylandViewporter::QWaylandViewporter(QWaylandCompositor *compositor)
extern "C" Q_DECL_EXPORT
QWaylandViewporter *ritual_ZN18QWaylandViewporterC1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandViewporter(compositor);
}

//  void QWaylandViewporter::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QWaylandViewporter10initializeEv(QWaylandViewporter *self) {
  self->initialize();
}

//  const struct wl_interface *QWaylandViewporter::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN18QWaylandViewporter9interfaceEv() {
  return QWaylandViewporter::interface();
}

//  a Python function taken by a CuteQWaylandViewporter, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandViewporter(
    QWaylandViewporter *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandViewporter *>(self)->take(key, call);
}

//  void QWaylandViewporter::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QWaylandViewporter10initializeEv(
    QWaylandViewporter *self) {
  self->QWaylandViewporter::initialize();
}
