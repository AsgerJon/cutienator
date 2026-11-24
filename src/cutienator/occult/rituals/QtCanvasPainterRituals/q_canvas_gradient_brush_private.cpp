//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/QtCanvasPainter>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcanvasgradient_p.h>
#include <QtCanvasPainter/6.12.0/QtCanvasPainter/private/qcpaint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QCanvasGradientBrushPrivate that Python can take functions over in. Every QCanvasGradientBrushPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQCanvasGradientBrushPrivateCall0)(const void *, int *);
typedef const QCPaint * (*CuteQCanvasGradientBrushPrivateCall1)(const void *, QCanvasPainter *, int *);
class CuteQCanvasGradientBrushPrivate : public QCanvasGradientBrushPrivate {
public:
  using QCanvasGradientBrushPrivate::QCanvasGradientBrushPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QCanvasBrushPrivate5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QCanvasBrushPrivate11createPaintEP14QCanvasPainter")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QCanvasBrushPrivate *QCanvasBrushPrivate::clone()
  QCanvasBrushPrivate *clone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasGradientBrushPrivateCall0 call = reinterpret_cast<CuteQCanvasGradientBrushPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QCanvasBrushPrivate *>(given);
    }
    return {};
  }

  //  QCPaint QCanvasBrushPrivate::createPaint(QCanvasPainter *painter)
  //      const
  QCPaint createPaint(QCanvasPainter *painter) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasGradientBrushPrivateCall1 call = reinterpret_cast<CuteQCanvasGradientBrushPrivateCall1>(taken[1]);
      const QCPaint * given = call(this, painter, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  a Python function taken by a CuteQCanvasGradientBrushPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasGradientBrushPrivate(
    QCanvasGradientBrushPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasGradientBrushPrivate *>(self)->take(key, call);
}
