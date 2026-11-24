//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qsurfacedataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsurfacedataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qsurface3dseries_p.h>
#include <QtGraphs/private/qsurfacedataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
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

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 522, as _ZN24QSurfaceDataProxyPrivate10removeRowsExx
inline void QSurfaceDataProxyPrivate::removeRows(qsizetype rowIndex, qsizetype removeCount)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0);
    qsizetype maxRemoveCount = surfaceSeries->dataArray().size() - rowIndex;
    removeCount = qMin(removeCount, maxRemoveCount);
    QSurfaceDataArray array = surfaceSeries->dataArray();
    for (int i = 0; i < removeCount; i++) {
        surfaceSeries->clearRow(rowIndex);
        array.removeAt(rowIndex);
    }
    surfaceSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 646, as _ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis
inline bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis *axis) const
{
    return (value > 0.0f || (value == 0.0f && axis->d_func()->allowZero())
            || (value < 0.0f && axis->d_func()->allowNegatives()));
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 652, as _ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QSurfaceDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QSurface3DSeries *surfaceSeries = static_cast<QSurface3DSeries *>(series);
    emit q->seriesChanged(surfaceSeries);
}
//  -----------------------------------------------------------------------

//  A QSurfaceDataProxyPrivate that Python can take functions over in. Every QSurfaceDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSurfaceDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQSurfaceDataProxyPrivate : public QSurfaceDataProxyPrivate {
public:
  using QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate;
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
      CuteQSurfaceDataProxyPrivateCall0 call = reinterpret_cast<CuteQSurfaceDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QSurfaceDataProxyPrivate::setSeries(series);
  }
};

//  QSurfaceDataProxy *QSurfaceDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSurfaceDataProxy *ritual_ZN24QSurfaceDataProxyPrivate6q_funcEv(
    QSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  const QSurfaceDataProxy *QSurfaceDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSurfaceDataProxy *ritual_ZNK24QSurfaceDataProxyPrivate6q_funcEv(
    const QSurfaceDataProxyPrivate *self) {
  return self->q_func();
}

//  void QSurfaceDataProxyPrivate::removeRows(qsizetype rowIndex, qsizetype
//      removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10removeRowsExx(
    QSurfaceDataProxyPrivate *self,
    qsizetype rowIndex,
    qsizetype removeCount) {
  self->removeRows(rowIndex, removeCount);
}

//  bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis
//      *axis) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis(
    const QSurfaceDataProxyPrivate *self,
    float value,
    QAbstract3DAxis *axis) {
  return self->isValidValue(value, axis);
}

//  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QSurfaceDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  a Python function taken by a CuteQSurfaceDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSurfaceDataProxyPrivate(
    QSurfaceDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSurfaceDataProxyPrivate *>(self)->take(key, call);
}

//  void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QSurfaceDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QSurfaceDataProxyPrivate::setSeries(series);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
