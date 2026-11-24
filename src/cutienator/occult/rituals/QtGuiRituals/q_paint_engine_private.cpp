//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/qpaintengine.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QPaintEnginePrivate that Python can take functions over in. Every QPaintEnginePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPaintEnginePrivateCall0)(const void *, int *);
typedef void * (*CuteQPaintEnginePrivateCall1)(const void *, int *);
class CuteQPaintEnginePrivate : public QPaintEnginePrivate {
public:
  using QPaintEnginePrivate::QPaintEnginePrivate;
  CuteQPaintEnginePrivate(const QPaintEnginePrivate &other) : QPaintEnginePrivate(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QPaintEnginePrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintEnginePrivateCall0 call = reinterpret_cast<CuteQPaintEnginePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEnginePrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintEnginePrivateCall1 call = reinterpret_cast<CuteQPaintEnginePrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }
};

//  QPaintEngine *QPaintEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZN19QPaintEnginePrivate6q_funcEv(
    QPaintEnginePrivate *self) {
  return self->q_func();
}

//  const QPaintEngine *QPaintEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPaintEngine *ritual_ZNK19QPaintEnginePrivate6q_funcEv(
    const QPaintEnginePrivate *self) {
  return self->q_func();
}

//  QPaintEnginePrivate::QPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
QPaintEnginePrivate *ritual_ZN19QPaintEnginePrivateC1Ev() {
  return new CuteQPaintEnginePrivate();
}

//  QPaintEnginePrivate::~QPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivateD1Ev(QPaintEnginePrivate *self) {
  delete self;
}

//  void QPaintEnginePrivate::updateSystemClip()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivate16updateSystemClipEv(
    QPaintEnginePrivate *self) {
  self->updateSystemClip();
}

//  void QPaintEnginePrivate::setSystemTransform(const QTransform &xform)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivate18setSystemTransformERK10QTransform(
    QPaintEnginePrivate *self,
    const QTransform *xform) {
  self->setSystemTransform(*xform);
}

//  void QPaintEnginePrivate::setSystemViewport(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivate17setSystemViewportERK7QRegion(
    QPaintEnginePrivate *self,
    const QRegion *region) {
  self->setSystemViewport(*region);
}

//  void QPaintEnginePrivate::setSystemTransformAndViewport(const QTransform
//      &xform, const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivate29setSystemTransformAndViewportERK10QTransformRK7QRegion(
    QPaintEnginePrivate *self,
    const QTransform *xform,
    const QRegion *region) {
  self->setSystemTransformAndViewport(*xform, *region);
}

//  void QPaintEnginePrivate::systemStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivate18systemStateChangedEv(
    QPaintEnginePrivate *self) {
  self->systemStateChanged();
}

//  void QPaintEnginePrivate::drawBoxTextItem(const QPointF &p, const
//      QTextItemInt &ti)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QPaintEnginePrivate15drawBoxTextItemERK7QPointFRK12QTextItemInt(
    QPaintEnginePrivate *self,
    const QPointF *p,
    const QTextItemInt *ti) {
  self->drawBoxTextItem(*p, *ti);
}

//  QPaintEnginePrivate *QPaintEnginePrivate::get(QPaintEngine *paintEngine)
extern "C" Q_DECL_EXPORT
QPaintEnginePrivate *ritual_ZN19QPaintEnginePrivate3getEP12QPaintEngine(
    QPaintEngine *paintEngine) {
  return QPaintEnginePrivate::get(paintEngine);
}

//  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZN19QPaintEnginePrivate15aggregateEngineEv(
    QPaintEnginePrivate *self) {
  return self->aggregateEngine();
}

//  a Python function taken by a CuteQPaintEnginePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintEnginePrivate(
    QPaintEnginePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintEnginePrivate *>(self)->take(key, call);
}

//  void QPaintEnginePrivate::systemStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QPaintEnginePrivate18systemStateChangedEv(
    QPaintEnginePrivate *self) {
  self->QPaintEnginePrivate::systemStateChanged();
}

//  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZN19QPaintEnginePrivate15aggregateEngineEv(
    QPaintEnginePrivate *self) {
  return self->QPaintEnginePrivate::aggregateEngine();
}
