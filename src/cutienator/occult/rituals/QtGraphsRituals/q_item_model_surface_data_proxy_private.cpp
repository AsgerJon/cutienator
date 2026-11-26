//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qitemmodelsurfacedataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qitemmodelsurfacedataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qitemmodelsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qsurface3dseries_p.h>
#include <QtGraphs/private/surfaceitemmodelhandler_p.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qsurface3dseries_p.h>
#include <QtGraphs/private/qsurfacedataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qitemmodelsurfacedataproxy_p.h>
#include <QtGraphs/private/surfaceitemmodelhandler_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/surfaceitemmodelhandler.cpp, line 25, as _ZN23SurfaceItemModelHandlerC1EP26QItemModelSurfaceDataProxyP7QObject
inline SurfaceItemModelHandler::SurfaceItemModelHandler(QItemModelSurfaceDataProxy *proxy, QObject *parent)
    : AbstractItemModelHandler(parent)
    , m_proxy(proxy)
    , m_proxyArray(0)
    , m_xPosRole(noRoleIndex)
    , m_yPosRole(noRoleIndex)
    , m_zPosRole(noRoleIndex)
    , m_haveXPosPattern(false)
    , m_haveYPosPattern(false)
    , m_haveZPosPattern(false)
{}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 652, as _ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QSurfaceDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QSurface3DSeries *surfaceSeries = static_cast<QSurface3DSeries *>(series);
    emit q->seriesChanged(surfaceSeries);
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 414, as _ZN24QSurfaceDataProxyPrivateC2Ev
inline QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate()
    : QAbstractDataProxyPrivate(QAbstractDataProxy::DataType::Surface)
{}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 418, as _ZN24QSurfaceDataProxyPrivateD2Ev
inline QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qitemmodelsurfacedataproxy.cpp, line 1294, as _ZN33QItemModelSurfaceDataProxyPrivateD2Ev
inline QItemModelSurfaceDataProxyPrivate::~QItemModelSurfaceDataProxyPrivate()
{
    delete m_itemModelHandler;
}
//  -----------------------------------------------------------------------

//  A QItemModelSurfaceDataProxyPrivate that Python can take functions over in. Every QItemModelSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQItemModelSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQItemModelSurfaceDataProxyPrivate : public QItemModelSurfaceDataProxyPrivate {
public:
  using QItemModelSurfaceDataProxyPrivate::QItemModelSurfaceDataProxyPrivate;
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
      CuteQItemModelSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQItemModelSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }
};

//  QItemModelSurfaceDataProxy *QItemModelSurfaceDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QItemModelSurfaceDataProxy *ritual_ZN33QItemModelSurfaceDataProxyPrivate6q_funcEv(
    QItemModelSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  const QItemModelSurfaceDataProxy
//      *QItemModelSurfaceDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QItemModelSurfaceDataProxy *ritual_ZNK33QItemModelSurfaceDataProxyPrivate6q_funcEv(
    const QItemModelSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  QItemModelSurfaceDataProxyPrivate::~QItemModelSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QItemModelSurfaceDataProxyPrivateD1Ev(
    QItemModelSurfaceDataProxyPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQItemModelSurfaceDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelSurfaceDataProxyPrivate(
    QItemModelSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelSurfaceDataProxyPrivate *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
