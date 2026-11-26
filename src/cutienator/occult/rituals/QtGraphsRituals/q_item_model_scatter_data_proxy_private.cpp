//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qitemmodelscatterdataproxy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qitemmodelscatterdataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qitemmodelscatterdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qscatter3dseries_p.h>
#include <QtGraphs/private/scatteritemmodelhandler_p.h>
#include <QtGui/qquaternion.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qscatter3dseries_p.h>
#include <QtGraphs/private/qscatterdataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qitemmodelscatterdataproxy_p.h>
#include <QtGraphs/private/scatteritemmodelhandler_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/scatteritemmodelhandler.cpp, line 27, as _ZN23ScatterItemModelHandlerC1EP26QItemModelScatterDataProxyP7QObject
inline ScatterItemModelHandler::ScatterItemModelHandler(QItemModelScatterDataProxy *proxy, QObject *parent)
    : AbstractItemModelHandler(parent)
    , m_proxy(proxy)
    , m_proxyArray(0)
    , m_xPosRole(noRoleIndex)
    , m_yPosRole(noRoleIndex)
    , m_zPosRole(noRoleIndex)
    , m_rotationRole(noRoleIndex)
    , m_scaleRole(noRoleIndex)
    , m_haveXPosPattern(false)
    , m_haveYPosPattern(false)
    , m_haveZPosPattern(false)
    , m_haveRotationPattern(false)
    , m_haveScalePattern(false)
{}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 488, as _ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QScatterDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QScatter3DSeries *scatterSeries = static_cast<QScatter3DSeries *>(series);
    emit q->seriesChanged(scatterSeries);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 329, as _ZN24QScatterDataProxyPrivateC2Ev
inline QScatterDataProxyPrivate::QScatterDataProxyPrivate()
    : QAbstractDataProxyPrivate(QAbstractDataProxy::DataType::Scatter)
{}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 333, as _ZN24QScatterDataProxyPrivateD2Ev
inline QScatterDataProxyPrivate::~QScatterDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qitemmodelscatterdataproxy.cpp, line 879, as _ZN33QItemModelScatterDataProxyPrivateD2Ev
inline QItemModelScatterDataProxyPrivate::~QItemModelScatterDataProxyPrivate()
{
    delete m_itemModelHandler;
}
//  -----------------------------------------------------------------------

//  A QItemModelScatterDataProxyPrivate that Python can take functions over in. Every QItemModelScatterDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQItemModelScatterDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQItemModelScatterDataProxyPrivate : public QItemModelScatterDataProxyPrivate {
public:
  using QItemModelScatterDataProxyPrivate::QItemModelScatterDataProxyPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemModelScatterDataProxyPrivateCall0 call = reinterpret_cast<CuteQItemModelScatterDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QScatterDataProxyPrivate::setSeries(series);
  }
};

//  QItemModelScatterDataProxy *QItemModelScatterDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QItemModelScatterDataProxy *ritual_ZN33QItemModelScatterDataProxyPrivate6q_funcEv(
    QItemModelScatterDataProxyPrivate *self) {
  return self->q_func();
}

//  const QItemModelScatterDataProxy
//      *QItemModelScatterDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QItemModelScatterDataProxy *ritual_ZNK33QItemModelScatterDataProxyPrivate6q_funcEv(
    const QItemModelScatterDataProxyPrivate *self) {
  return self->q_func();
}

//  QItemModelScatterDataProxyPrivate::~QItemModelScatterDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QItemModelScatterDataProxyPrivateD1Ev(
    QItemModelScatterDataProxyPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQItemModelScatterDataProxyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemModelScatterDataProxyPrivate(
    QItemModelScatterDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemModelScatterDataProxyPrivate *>(self)->take(key, call);
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
