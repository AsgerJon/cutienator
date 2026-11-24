//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandxdgdecorationv1.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWaylandCompositor/qwaylandxdgdecorationv1.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWaylandXdgDecorationManagerV1 that Python can take functions over in. Every QWaylandXdgDecorationManagerV1
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandXdgDecorationManagerV1Call0)(const void *, int *);
class CuteQWaylandXdgDecorationManagerV1 : public QWaylandXdgDecorationManagerV1 {
public:
  using QWaylandXdgDecorationManagerV1::QWaylandXdgDecorationManagerV1;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QWaylandXdgDecorationManagerV110initializeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandXdgDecorationManagerV1::initialize()
  void initialize() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandXdgDecorationManagerV1Call0 call = reinterpret_cast<CuteQWaylandXdgDecorationManagerV1Call0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandXdgDecorationManagerV1::initialize();
  }
};

//  const QMetaObject *QWaylandXdgDecorationManagerV1::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QWaylandXdgDecorationManagerV110metaObjectEv(
    const QWaylandXdgDecorationManagerV1 *self) {
  return self->metaObject();
}

//  QString QWaylandXdgDecorationManagerV1::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QWaylandXdgDecorationManagerV12trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandXdgDecorationManagerV1::tr(s, c, n));
}

//  QWaylandXdgDecorationManagerV1::QWaylandXdgDecorationManagerV1()
extern "C" Q_DECL_EXPORT
QWaylandXdgDecorationManagerV1 *ritual_ZN30QWaylandXdgDecorationManagerV1C1Ev() {
  return new CuteQWaylandXdgDecorationManagerV1();
}

//  void QWaylandXdgDecorationManagerV1::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWaylandXdgDecorationManagerV110initializeEv(
    QWaylandXdgDecorationManagerV1 *self) {
  self->initialize();
}

//  QWaylandXdgToplevel::DecorationMode
//      QWaylandXdgDecorationManagerV1::preferredMode() const
extern "C" Q_DECL_EXPORT
QWaylandXdgToplevel::DecorationMode ritual_ZNK30QWaylandXdgDecorationManagerV113preferredModeEv(
    const QWaylandXdgDecorationManagerV1 *self) {
  return self->preferredMode();
}

//  void QWaylandXdgDecorationManagerV1::setPreferredMode(QWaylandXdgToplevel
//      ::DecorationMode preferredMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QWaylandXdgDecorationManagerV116setPreferredModeEN19QWaylandXdgToplevel14DecorationModeE(
    QWaylandXdgDecorationManagerV1 *self,
    QWaylandXdgToplevel::DecorationMode preferredMode) {
  self->setPreferredMode(preferredMode);
}

//  a Python function taken by a CuteQWaylandXdgDecorationManagerV1, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandXdgDecorationManagerV1(
    QWaylandXdgDecorationManagerV1 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandXdgDecorationManagerV1 *>(self)->take(key, call);
}

//  void QWaylandXdgDecorationManagerV1::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QWaylandXdgDecorationManagerV110initializeEv(
    QWaylandXdgDecorationManagerV1 *self) {
  self->QWaylandXdgDecorationManagerV1::initialize();
}
