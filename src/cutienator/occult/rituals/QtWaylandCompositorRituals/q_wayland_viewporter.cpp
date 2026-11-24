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

//  QString QWaylandViewporter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QWaylandViewporter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandViewporter::tr(s, c, n));
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
