//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandiviapplication.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandiviapplication.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
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

//  QString QWaylandIviApplication::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QWaylandIviApplication2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandIviApplication::tr(s, c, n));
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

//  QByteArray QWaylandIviApplication::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN22QWaylandIviApplication13interfaceNameEv() {
  return new QByteArray(QWaylandIviApplication::interfaceName());
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
