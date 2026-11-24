//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgoutputv1.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandxdgoutputv1.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWaylandXdgOutputManagerV1 that Python can take functions over in. Every QWaylandXdgOutputManagerV1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandXdgOutputManagerV1Call0)(const void *, int *);
class CuteQWaylandXdgOutputManagerV1 : public QWaylandXdgOutputManagerV1 {
public:
  using QWaylandXdgOutputManagerV1::QWaylandXdgOutputManagerV1;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QWaylandXdgOutputManagerV110initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandXdgOutputManagerV1::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandXdgOutputManagerV1Call0 call = reinterpret_cast<CuteQWaylandXdgOutputManagerV1Call0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandXdgOutputManagerV1::initialize();
  }
};

//  const QMetaObject *QWaylandXdgOutputManagerV1::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWaylandXdgOutputManagerV110metaObjectEv(
    const QWaylandXdgOutputManagerV1 *self) {
  return self->metaObject();
}

//  QString QWaylandXdgOutputManagerV1::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWaylandXdgOutputManagerV12trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgOutputManagerV1::tr(s, c, n));
}

//  QWaylandXdgOutputManagerV1::QWaylandXdgOutputManagerV1()
extern "C" Q_DECL_EXPORT
QWaylandXdgOutputManagerV1 *ritual_ZN26QWaylandXdgOutputManagerV1C1Ev() {
  return new CuteQWaylandXdgOutputManagerV1();
}

//  QWaylandXdgOutputManagerV1::QWaylandXdgOutputManagerV1(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
QWaylandXdgOutputManagerV1 *ritual_ZN26QWaylandXdgOutputManagerV1C1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandXdgOutputManagerV1(compositor);
}

//  void QWaylandXdgOutputManagerV1::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandXdgOutputManagerV110initializeEv(
    QWaylandXdgOutputManagerV1 *self) {
  self->initialize();
}

//  a Python function taken by a CuteQWaylandXdgOutputManagerV1, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandXdgOutputManagerV1(
    QWaylandXdgOutputManagerV1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandXdgOutputManagerV1 *>(self)->take(key, call);
}

//  void QWaylandXdgOutputManagerV1::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWaylandXdgOutputManagerV110initializeEv(
    QWaylandXdgOutputManagerV1 *self) {
  self->QWaylandXdgOutputManagerV1::initialize();
}
