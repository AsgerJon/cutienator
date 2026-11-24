//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qheightmapsurfacedataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qheightmapsurfacedataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qheightmapsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QHeightMapSurfaceDataProxyPrivate that Python can take functions over in. Every QHeightMapSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQHeightMapSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQHeightMapSurfaceDataProxyPrivate : public QHeightMapSurfaceDataProxyPrivate {
public:
  using QHeightMapSurfaceDataProxyPrivate::QHeightMapSurfaceDataProxyPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeightMapSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQHeightMapSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }
};

//  QHeightMapSurfaceDataProxy *QHeightMapSurfaceDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHeightMapSurfaceDataProxy *ritual_ZN33QHeightMapSurfaceDataProxyPrivate6q_funcEv(
    QHeightMapSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  const QHeightMapSurfaceDataProxy
//      *QHeightMapSurfaceDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHeightMapSurfaceDataProxy *ritual_ZNK33QHeightMapSurfaceDataProxyPrivate6q_funcEv(
    const QHeightMapSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQHeightMapSurfaceDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeightMapSurfaceDataProxyPrivate(
    QHeightMapSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeightMapSurfaceDataProxyPrivate *>(self)->take(key, call);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
