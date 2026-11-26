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

//  void *QWaylandXdgOutputManagerV1::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWaylandXdgOutputManagerV111qt_metacastEPKc(
    QWaylandXdgOutputManagerV1 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandXdgOutputManagerV1::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWaylandXdgOutputManagerV111qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandXdgOutputManagerV1 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  QWaylandXdgOutputManagerV1Private *QWaylandXdgOutputManagerV1::d_func()
extern "C" Q_DECL_EXPORT
QWaylandXdgOutputManagerV1Private *ritual_ZN26QWaylandXdgOutputManagerV16d_funcEv(
    QWaylandXdgOutputManagerV1 *self) {
  return self->d_func();
}

//  const QWaylandXdgOutputManagerV1Private
//      *QWaylandXdgOutputManagerV1::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandXdgOutputManagerV1Private *ritual_ZNK26QWaylandXdgOutputManagerV16d_funcEv(
    const QWaylandXdgOutputManagerV1 *self) {
  return self->d_func();
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

//  const wl_interface *QWaylandXdgOutputManagerV1::interface()
extern "C" Q_DECL_EXPORT
const wl_interface *ritual_ZN26QWaylandXdgOutputManagerV19interfaceEv() {
  return QWaylandXdgOutputManagerV1::interface();
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
