//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpaintengineex_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpaintengineex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QPaintEngineExPrivate that Python can take functions over in. Every QPaintEngineExPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPaintEngineExPrivateCall0)(const void *, int *);
typedef void * (*CuteQPaintEngineExPrivateCall1)(const void *, int *);
typedef void * (*CuteQPaintEngineExPrivateCall2)(const void *, int *);
class CuteQPaintEngineExPrivate : public QPaintEngineExPrivate {
public:
  using QPaintEngineExPrivate::QPaintEngineExPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate18systemStateChangedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate15aggregateEngineEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QPaintEnginePrivate12nativeHandleEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QPaintEnginePrivate::systemStateChanged()
  void systemStateChanged() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPaintEngineExPrivateCall0 call = reinterpret_cast<CuteQPaintEngineExPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QPaintEnginePrivate::systemStateChanged();
  }

  //  QPaintEngine *QPaintEnginePrivate::aggregateEngine()
  QPaintEngine *aggregateEngine() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPaintEngineExPrivateCall1 call = reinterpret_cast<CuteQPaintEngineExPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPaintEnginePrivate::aggregateEngine();
  }

  //  Qt::HANDLE QPaintEnginePrivate::nativeHandle()
  Qt::HANDLE nativeHandle() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPaintEngineExPrivateCall2 call = reinterpret_cast<CuteQPaintEngineExPrivateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<Qt::HANDLE>(given);
    }
    return QPaintEnginePrivate::nativeHandle();
  }
};

//  QPaintEngineEx *QPaintEngineExPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPaintEngineEx *ritual_ZN21QPaintEngineExPrivate6q_funcEv(
    QPaintEngineExPrivate *self) {
  return self->q_func();
}

//  const QPaintEngineEx *QPaintEngineExPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPaintEngineEx *ritual_ZNK21QPaintEngineExPrivate6q_funcEv(
    const QPaintEngineExPrivate *self) {
  return self->q_func();
}

//  QPaintEngineExPrivate::QPaintEngineExPrivate()
extern "C" Q_DECL_EXPORT
QPaintEngineExPrivate *ritual_ZN21QPaintEngineExPrivateC1Ev() {
  return new CuteQPaintEngineExPrivate();
}

//  QPaintEngineExPrivate::~QPaintEngineExPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPaintEngineExPrivateD1Ev(QPaintEngineExPrivate *self) {
  delete self;
}

//  void QPaintEngineExPrivate::replayClipOperations()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPaintEngineExPrivate20replayClipOperationsEv(
    QPaintEngineExPrivate *self) {
  self->replayClipOperations();
}

//  bool QPaintEngineExPrivate::hasClipOperations() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPaintEngineExPrivate17hasClipOperationsEv(
    const QPaintEngineExPrivate *self) {
  return self->hasClipOperations();
}

//  a Python function taken by a CuteQPaintEngineExPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPaintEngineExPrivate(
    QPaintEngineExPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPaintEngineExPrivate *>(self)->take(key, call);
}
