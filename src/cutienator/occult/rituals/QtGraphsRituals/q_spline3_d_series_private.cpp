//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qspline3dseries_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qspline3dseries.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qspline3dseries_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSpline3DSeriesPrivate that Python can take functions over in. Every QSpline3DSeriesPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSpline3DSeriesPrivateCall0)(const void *, QAbstractDataProxy *, int *);
typedef void (*CuteQSpline3DSeriesPrivateCall1)(const void *, QQuickGraphsItem *, int *);
typedef void (*CuteQSpline3DSeriesPrivateCall2)(const void *, int *);
typedef void (*CuteQSpline3DSeriesPrivateCall3)(const void *, QQuickGraphsItem *, int *);
class CuteQSpline3DSeriesPrivate : public QSpline3DSeriesPrivate {
public:
  using QSpline3DSeriesPrivate::QSpline3DSeriesPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate20connectGraphAndProxyEP16QQuickGraphsItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate15createItemLabelEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstract3DSeriesPrivate8setGraphEP16QQuickGraphsItem")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
  void setDataProxy(QAbstractDataProxy *proxy) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall0 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall0>(taken[0]);
      call(this, proxy, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::setDataProxy(proxy);
  }

  //  void QScatter3DSeriesPrivate::connectGraphAndProxy(QQuickGraphsItem
  //      *newGraph)
  void connectGraphAndProxy(QQuickGraphsItem *newGraph) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall1 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall1>(taken[1]);
      call(this, newGraph, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::connectGraphAndProxy(newGraph);
  }

  //  void QScatter3DSeriesPrivate::createItemLabel()
  void createItemLabel() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall2 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QScatter3DSeriesPrivate::createItemLabel();
  }

  //  void QAbstract3DSeriesPrivate::setGraph(QQuickGraphsItem *graph)
  void setGraph(QQuickGraphsItem *graph) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSpline3DSeriesPrivateCall3 call = reinterpret_cast<CuteQSpline3DSeriesPrivateCall3>(taken[3]);
      call(this, graph, &handled);
      if (handled) return;
    }
    QAbstract3DSeriesPrivate::setGraph(graph);
  }
};

//  QSpline3DSeries *QSpline3DSeriesPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSpline3DSeries *ritual_ZN22QSpline3DSeriesPrivate6q_funcEv(
    QSpline3DSeriesPrivate *self) {
  return self->q_func();
}

//  const QSpline3DSeries *QSpline3DSeriesPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSpline3DSeries *ritual_ZNK22QSpline3DSeriesPrivate6q_funcEv(
    const QSpline3DSeriesPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQSpline3DSeriesPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSpline3DSeriesPrivate(
    QSpline3DSeriesPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSpline3DSeriesPrivate *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
