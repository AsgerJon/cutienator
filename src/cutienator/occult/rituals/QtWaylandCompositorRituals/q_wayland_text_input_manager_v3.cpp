//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandtextinputmanagerv3.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandtextinputmanagerv3.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QWaylandTextInputManagerV3 that Python can take functions over in. Every QWaylandTextInputManagerV3
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandTextInputManagerV3Call0)(const void *, int *);
class CuteQWaylandTextInputManagerV3 : public QWaylandTextInputManagerV3 {
public:
  using QWaylandTextInputManagerV3::QWaylandTextInputManagerV3;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QWaylandTextInputManagerV310initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandTextInputManagerV3::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandTextInputManagerV3Call0 call = reinterpret_cast<CuteQWaylandTextInputManagerV3Call0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandTextInputManagerV3::initialize();
  }
};

//  const QMetaObject *QWaylandTextInputManagerV3::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWaylandTextInputManagerV310metaObjectEv(
    const QWaylandTextInputManagerV3 *self) {
  return self->metaObject();
}

//  void *QWaylandTextInputManagerV3::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QWaylandTextInputManagerV311qt_metacastEPKc(
    QWaylandTextInputManagerV3 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandTextInputManagerV3::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QWaylandTextInputManagerV311qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandTextInputManagerV3 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandTextInputManagerV3::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWaylandTextInputManagerV32trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandTextInputManagerV3::tr(s, c, n));
}

//  QWaylandTextInputManagerV3Private *QWaylandTextInputManagerV3::d_func()
extern "C" Q_DECL_EXPORT
QWaylandTextInputManagerV3Private *ritual_ZN26QWaylandTextInputManagerV36d_funcEv(
    QWaylandTextInputManagerV3 *self) {
  return self->d_func();
}

//  const QWaylandTextInputManagerV3Private
//      *QWaylandTextInputManagerV3::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandTextInputManagerV3Private *ritual_ZNK26QWaylandTextInputManagerV36d_funcEv(
    const QWaylandTextInputManagerV3 *self) {
  return self->d_func();
}

//  QWaylandTextInputManagerV3::QWaylandTextInputManagerV3()
extern "C" Q_DECL_EXPORT
QWaylandTextInputManagerV3 *ritual_ZN26QWaylandTextInputManagerV3C1Ev() {
  return new CuteQWaylandTextInputManagerV3();
}

//  QWaylandTextInputManagerV3::QWaylandTextInputManagerV3(QWaylandCompositor
//      *compositor)
extern "C" Q_DECL_EXPORT
QWaylandTextInputManagerV3 *ritual_ZN26QWaylandTextInputManagerV3C1EP18QWaylandCompositor(
    QWaylandCompositor *compositor) {
  return new CuteQWaylandTextInputManagerV3(compositor);
}

//  QWaylandTextInputManagerV3::~QWaylandTextInputManagerV3()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandTextInputManagerV3D1Ev(
    QWaylandTextInputManagerV3 *self) {
  delete self;
}

//  void QWaylandTextInputManagerV3::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWaylandTextInputManagerV310initializeEv(
    QWaylandTextInputManagerV3 *self) {
  self->initialize();
}

//  const struct wl_interface *QWaylandTextInputManagerV3::interface()
extern "C" Q_DECL_EXPORT
const struct wl_interface *ritual_ZN26QWaylandTextInputManagerV39interfaceEv() {
  return QWaylandTextInputManagerV3::interface();
}

//  QByteArray QWaylandTextInputManagerV3::interfaceName()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN26QWaylandTextInputManagerV313interfaceNameEv() {
  return new QByteArray(QWaylandTextInputManagerV3::interfaceName());
}

//  a Python function taken by a CuteQWaylandTextInputManagerV3, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandTextInputManagerV3(
    QWaylandTextInputManagerV3 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandTextInputManagerV3 *>(self)->take(key, call);
}

//  void QWaylandTextInputManagerV3::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWaylandTextInputManagerV310initializeEv(
    QWaylandTextInputManagerV3 *self) {
  self->QWaylandTextInputManagerV3::initialize();
}
