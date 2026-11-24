//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qbardataproxy_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbardataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qbardataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstract3dseries_p.h"
#include "qabstractdataproxy_p.h"
#include "qbar3dseries_p.h"
#include "qbardataproxy_p.h"
#include "qgraphs3dlogging_p.h"
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

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 652, as _ZN20QBarDataProxyPrivate10removeRowsExxb
inline void QBarDataProxyPrivate::removeRows(qsizetype rowIndex, qsizetype removeCount, bool removeLabels)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0);
    qsizetype maxRemoveCount = barSeries->dataArray().size() - rowIndex;
    removeCount = qMin(removeCount, maxRemoveCount);
    bool labelsChanged = false;
    QBarDataArray array = barSeries->dataArray();
    for (int i = 0; i < removeCount; i++) {
        barSeries->clearRow(rowIndex);
        array.removeAt(rowIndex);
        if (removeLabels && barSeries->rowLabels().size() > rowIndex) {
            auto rowLabels = barSeries->rowLabels();
            rowLabels.removeAt(rowIndex);
            barSeries->setRowLabels(rowLabels);
            labelsChanged = true;
        }
    }
    barSeries->setDataArray(array);
    if (labelsChanged)
        emit barSeries->rowLabelsChanged();
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 698, as _ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QBarDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QBar3DSeries *barSeries = static_cast<QBar3DSeries *>(series);
    emit q->seriesChanged(barSeries);
}
//  -----------------------------------------------------------------------

//  A QBarDataProxyPrivate that Python can take functions over in. Every QBarDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQBarDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQBarDataProxyPrivate : public QBarDataProxyPrivate {
public:
  using QBarDataProxyPrivate::QBarDataProxyPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
  void setSeries(QAbstract3DSeries *series) override {
    if (taken[0]) {
      int handled = 0;
      CuteQBarDataProxyPrivateCall0 call = reinterpret_cast<CuteQBarDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QBarDataProxyPrivate::setSeries(series);
  }
};

//  QBarDataProxy *QBarDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarDataProxy *ritual_ZN20QBarDataProxyPrivate6q_funcEv(
    QBarDataProxyPrivate *self) {
  return self->q_func();
}

//  const QBarDataProxy *QBarDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarDataProxy *ritual_ZNK20QBarDataProxyPrivate6q_funcEv(
    const QBarDataProxyPrivate *self) {
  return self->q_func();
}

//  void QBarDataProxyPrivate::removeRows(qsizetype rowIndex, qsizetype
//      removeCount, bool removeLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10removeRowsExxb(
    QBarDataProxyPrivate *self,
    qsizetype rowIndex,
    qsizetype removeCount,
    bool removeLabels) {
  self->removeRows(rowIndex, removeCount, removeLabels);
}

//  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QBarDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  a Python function taken by a CuteQBarDataProxyPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBarDataProxyPrivate(
    QBarDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBarDataProxyPrivate *>(self)->take(key, call);
}

//  void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QBarDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QBarDataProxyPrivate::setSeries(series);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
