//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qcustomseriescanvasrenderer.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_high_performance_backend))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qcustomseriescanvasrenderer.h>
#include <cstring>

//  A QCustomSeriesCanvasRenderer that Python can take functions over in. Every QCustomSeriesCanvasRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCustomSeriesCanvasRendererCall0)(const void *, QCustomSeries *, QCanvasPainter *, int *);
typedef void (*CuteQCustomSeriesCanvasRendererCall1)(const void *, QCustomSeries *, QCanvasPainterItem *, int *);
typedef void (*CuteQCustomSeriesCanvasRendererCall2)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCustomSeriesCanvasRendererCall3)(const void *, QCanvasPainter *, int *);
class CuteQCustomSeriesCanvasRenderer : public QCustomSeriesCanvasRenderer {
public:
  using QCustomSeriesCanvasRenderer::QCustomSeriesCanvasRenderer;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN27QCustomSeriesCanvasRenderer19initializeResourcesEP13QCustomSeriesP14QCanvasPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QCustomSeriesCanvasRenderer15synchronizeDataEP13QCustomSeriesP18QCanvasPainterItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QCustomSeriesCanvasRenderer14canvasPrePaintEP14QCanvasPainter")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN27QCustomSeriesCanvasRenderer11canvasPaintEP14QCanvasPainter")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QCustomSeriesCanvasRenderer::initializeResources(QCustomSeries
  //      *series, QCanvasPainter *p)
  void initializeResources(
      QCustomSeries *series,
      QCanvasPainter *p) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCustomSeriesCanvasRendererCall0 call = reinterpret_cast<CuteQCustomSeriesCanvasRendererCall0>(taken[0]);
      call(this, series, p, &handled);
      if (handled) return;
    }
    QCustomSeriesCanvasRenderer::initializeResources(series, p);
  }

  //  void QCustomSeriesCanvasRenderer::synchronizeData(QCustomSeries
  //      *series, QCanvasPainterItem *item)
  void synchronizeData(
      QCustomSeries *series,
      QCanvasPainterItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCustomSeriesCanvasRendererCall1 call = reinterpret_cast<CuteQCustomSeriesCanvasRendererCall1>(taken[1]);
      call(this, series, item, &handled);
      if (handled) return;
    }
    QCustomSeriesCanvasRenderer::synchronizeData(series, item);
  }

  //  void QCustomSeriesCanvasRenderer::canvasPrePaint(QCanvasPainter *p)
  void canvasPrePaint(QCanvasPainter *p) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCustomSeriesCanvasRendererCall2 call = reinterpret_cast<CuteQCustomSeriesCanvasRendererCall2>(taken[2]);
      call(this, p, &handled);
      if (handled) return;
    }
    QCustomSeriesCanvasRenderer::canvasPrePaint(p);
  }

  //  void QCustomSeriesCanvasRenderer::canvasPaint(QCanvasPainter *p)
  void canvasPaint(QCanvasPainter *p) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCustomSeriesCanvasRendererCall3 call = reinterpret_cast<CuteQCustomSeriesCanvasRendererCall3>(taken[3]);
      call(this, p, &handled);
      if (handled) return;
    }
  }
};

//  QCustomSeriesCanvasRenderer::QCustomSeriesCanvasRenderer()
extern "C" Q_DECL_EXPORT
QCustomSeriesCanvasRenderer *ritual_ZN27QCustomSeriesCanvasRendererC1Ev() {
  return new CuteQCustomSeriesCanvasRenderer();
}

//  QCustomSeriesCanvasRenderer::~QCustomSeriesCanvasRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCustomSeriesCanvasRendererD1Ev(
    QCustomSeriesCanvasRenderer *self) {
  delete self;
}

//  void QCustomSeriesCanvasRenderer::initializeResources(QCustomSeries
//      *series, QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCustomSeriesCanvasRenderer19initializeResourcesEP13QCustomSeriesP14QCanvasPainter(
    QCustomSeriesCanvasRenderer *self,
    QCustomSeries *series,
    QCanvasPainter *p) {
  self->initializeResources(series, p);
}

//  void QCustomSeriesCanvasRenderer::synchronizeData(QCustomSeries *series,
//      QCanvasPainterItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCustomSeriesCanvasRenderer15synchronizeDataEP13QCustomSeriesP18QCanvasPainterItem(
    QCustomSeriesCanvasRenderer *self,
    QCustomSeries *series,
    QCanvasPainterItem *item) {
  self->synchronizeData(series, item);
}

//  void QCustomSeriesCanvasRenderer::canvasPrePaint(QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCustomSeriesCanvasRenderer14canvasPrePaintEP14QCanvasPainter(
    QCustomSeriesCanvasRenderer *self,
    QCanvasPainter *p) {
  self->canvasPrePaint(p);
}

//  void QCustomSeriesCanvasRenderer::canvasPaint(QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCustomSeriesCanvasRenderer11canvasPaintEP14QCanvasPainter(
    QCustomSeriesCanvasRenderer *self,
    QCanvasPainter *p) {
  self->canvasPaint(p);
}

//  a Python function taken by a CuteQCustomSeriesCanvasRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustomSeriesCanvasRenderer(
    QCustomSeriesCanvasRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustomSeriesCanvasRenderer *>(self)->take(key, call);
}

//  void QCustomSeriesCanvasRenderer::initializeResources(QCustomSeries
//      *series, QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QCustomSeriesCanvasRenderer19initializeResourcesEP13QCustomSeriesP14QCanvasPainter(
    QCustomSeriesCanvasRenderer *self,
    QCustomSeries *series,
    QCanvasPainter *p) {
  self->QCustomSeriesCanvasRenderer::initializeResources(series, p);
}

//  void QCustomSeriesCanvasRenderer::synchronizeData(QCustomSeries *series,
//      QCanvasPainterItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QCustomSeriesCanvasRenderer15synchronizeDataEP13QCustomSeriesP18QCanvasPainterItem(
    QCustomSeriesCanvasRenderer *self,
    QCustomSeries *series,
    QCanvasPainterItem *item) {
  self->QCustomSeriesCanvasRenderer::synchronizeData(series, item);
}

//  void QCustomSeriesCanvasRenderer::canvasPrePaint(QCanvasPainter *p)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QCustomSeriesCanvasRenderer14canvasPrePaintEP14QCanvasPainter(
    QCustomSeriesCanvasRenderer *self,
    QCanvasPainter *p) {
  self->QCustomSeriesCanvasRenderer::canvasPrePaint(p);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_high_performance_backend))
