//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandidleinhibitv1.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qwaylandidleinhibitv1.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWaylandIdleInhibitManagerV1 that Python can take functions over in. Every QWaylandIdleInhibitManagerV1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandIdleInhibitManagerV1Call0)(const void *, int *);
class CuteQWaylandIdleInhibitManagerV1 : public QWaylandIdleInhibitManagerV1 {
public:
  using QWaylandIdleInhibitManagerV1::QWaylandIdleInhibitManagerV1;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QWaylandIdleInhibitManagerV110initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandIdleInhibitManagerV1::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandIdleInhibitManagerV1Call0 call = reinterpret_cast<CuteQWaylandIdleInhibitManagerV1Call0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandIdleInhibitManagerV1::initialize();
  }
};

//  const QMetaObject *QWaylandIdleInhibitManagerV1::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QWaylandIdleInhibitManagerV110metaObjectEv(
    const QWaylandIdleInhibitManagerV1 *self) {
  return self->metaObject();
}

//  void *QWaylandIdleInhibitManagerV1::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QWaylandIdleInhibitManagerV111qt_metacastEPKc(
    QWaylandIdleInhibitManagerV1 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandIdleInhibitManagerV1::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QWaylandIdleInhibitManagerV111qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandIdleInhibitManagerV1 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandIdleInhibitManagerV1::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QWaylandIdleInhibitManagerV12trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandIdleInhibitManagerV1::tr(s, c, n));
}

//  QWaylandIdleInhibitManagerV1Private
//      *QWaylandIdleInhibitManagerV1::d_func()
extern "C" Q_DECL_EXPORT
QWaylandIdleInhibitManagerV1Private *ritual_ZN28QWaylandIdleInhibitManagerV16d_funcEv(
    QWaylandIdleInhibitManagerV1 *self) {
  return self->d_func();
}

//  const QWaylandIdleInhibitManagerV1Private
//      *QWaylandIdleInhibitManagerV1::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandIdleInhibitManagerV1Private *ritual_ZNK28QWaylandIdleInhibitManagerV16d_funcEv(
    const QWaylandIdleInhibitManagerV1 *self) {
  return self->d_func();
}

//  QWaylandIdleInhibitManagerV1::QWaylandIdleInhibitManagerV1()
extern "C" Q_DECL_EXPORT
QWaylandIdleInhibitManagerV1 *ritual_ZN28QWaylandIdleInhibitManagerV1C1Ev() {
  return new CuteQWaylandIdleInhibitManagerV1();
}

//  QWaylandIdleInhibitManagerV1::QWaylandIdleInhibitManagerV1(QWaylandCompos
//      itor *compositor)
extern "C" Q_DECL_EXPORT
QWaylandIdleInhibitManagerV1 *ritual_ZN28QWaylandIdleInhibitManagerV1C1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandIdleInhibitManagerV1(compositor);
}

//  QWaylandIdleInhibitManagerV1::~QWaylandIdleInhibitManagerV1()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWaylandIdleInhibitManagerV1D1Ev(
    QWaylandIdleInhibitManagerV1 *self) {
  delete self;
}

//  void QWaylandIdleInhibitManagerV1::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWaylandIdleInhibitManagerV110initializeEv(
    QWaylandIdleInhibitManagerV1 *self) {
  self->initialize();
}

//  const struct wl_interface *QWaylandIdleInhibitManagerV1::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN28QWaylandIdleInhibitManagerV19interfaceEv() {
  return QWaylandIdleInhibitManagerV1::interface();
}

//  a Python function taken by a CuteQWaylandIdleInhibitManagerV1, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandIdleInhibitManagerV1(
    QWaylandIdleInhibitManagerV1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandIdleInhibitManagerV1 *>(self)->take(key, call);
}

//  void QWaylandIdleInhibitManagerV1::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QWaylandIdleInhibitManagerV110initializeEv(
    QWaylandIdleInhibitManagerV1 *self) {
  self->QWaylandIdleInhibitManagerV1::initialize();
}
