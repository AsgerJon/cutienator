//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qabstractdataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstractdataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qabstractdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 89, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QAbstractDataProxy);
    q->setParent(series);
    m_series = series;
}
//  -----------------------------------------------------------------------

//  A QAbstractDataProxyPrivate that Python can take functions over in. Every QAbstractDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQAbstractDataProxyPrivate : public QAbstractDataProxyPrivate {
public:
  using QAbstractDataProxyPrivate::QAbstractDataProxyPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractDataProxyPrivateCall0 call = reinterpret_cast<CuteQAbstractDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QAbstractDataProxyPrivate::setSeries(series);
  }
};

//  QAbstractDataProxy *QAbstractDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractDataProxy *ritual_ZN25QAbstractDataProxyPrivate6q_funcEv(
    QAbstractDataProxyPrivate *self) {
  return self->q_func();
}

//  const QAbstractDataProxy *QAbstractDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractDataProxy *ritual_ZNK25QAbstractDataProxyPrivate6q_funcEv(
    const QAbstractDataProxyPrivate *self) {
  return self->q_func();
}

//  QAbstract3DSeries *QAbstractDataProxyPrivate::series() const
extern "C" Q_DECL_EXPORT
QAbstract3DSeries *ritual_ZNK25QAbstractDataProxyPrivate6seriesEv(
    const QAbstractDataProxyPrivate *self) {
  return self->series();
}

//  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QAbstractDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  a Python function taken by a CuteQAbstractDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractDataProxyPrivate(
    QAbstractDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractDataProxyPrivate *>(self)->take(key, call);
}

//  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QAbstractDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QAbstractDataProxyPrivate::setSeries(series);
}

#endif  // !(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))
