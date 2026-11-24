//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qscatterdataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatterdataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qscatterdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qscatter3dseries_p.h>
#include <QtGraphs/private/qscatterdataproxy_p.h>
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

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 410, as _ZN24QScatterDataProxyPrivate11removeItemsExx
inline void QScatterDataProxyPrivate::removeItems(qsizetype index, qsizetype removeCount)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    Q_ASSERT(index >= 0);
    qsizetype maxRemoveCount = scatterSeries->dataArray().size() - index;
    removeCount = qMin(removeCount, maxRemoveCount);
    QScatterDataArray array = scatterSeries->dataArray();
    array.remove(index, removeCount);
    scatterSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 479, as _ZNK24QScatterDataProxyPrivate12isValidValueEffP15QAbstract3DAxis
inline bool QScatterDataProxyPrivate::isValidValue(float axisValue,
                                            float value,
                                            QAbstract3DAxis *axis) const
{
    return (axisValue > value
            && (value > 0.0f || (value == 0.0f && axis->d_func()->allowZero())
                || (value < 0.0f && axis->d_func()->allowNegatives())));
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 488, as _ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QScatterDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QScatter3DSeries *scatterSeries = static_cast<QScatter3DSeries *>(series);
    emit q->seriesChanged(scatterSeries);
}
//  -----------------------------------------------------------------------

//  A QScatterDataProxyPrivate that Python can take functions over in. Every QScatterDataProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQScatterDataProxyPrivateCall0)(const void *, QAbstract3DSeries *, int *);
class CuteQScatterDataProxyPrivate : public QScatterDataProxyPrivate {
public:
  using QScatterDataProxyPrivate::QScatterDataProxyPrivate;
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
      CuteQScatterDataProxyPrivateCall0 call = reinterpret_cast<CuteQScatterDataProxyPrivateCall0>(taken[0]);
      call(this, series, &handled);
      if (handled) return;
    }
    QScatterDataProxyPrivate::setSeries(series);
  }
};

//  QScatterDataProxy *QScatterDataProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QScatterDataProxy *ritual_ZN24QScatterDataProxyPrivate6q_funcEv(
    QScatterDataProxyPrivate *self) {
  return self->q_func();
}

//  const QScatterDataProxy *QScatterDataProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QScatterDataProxy *ritual_ZNK24QScatterDataProxyPrivate6q_funcEv(
    const QScatterDataProxyPrivate *self) {
  return self->q_func();
}

//  void QScatterDataProxyPrivate::removeItems(qsizetype index, qsizetype
//      removeCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate11removeItemsExx(
    QScatterDataProxyPrivate *self,
    qsizetype index,
    qsizetype removeCount) {
  self->removeItems(index, removeCount);
}

//  bool QScatterDataProxyPrivate::isValidValue(float axisValue, float value,
//      QAbstract3DAxis *axis) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QScatterDataProxyPrivate12isValidValueEffP15QAbstract3DAxis(
    const QScatterDataProxyPrivate *self,
    float axisValue,
    float value,
    QAbstract3DAxis *axis) {
  return self->isValidValue(axisValue, value, axis);
}

//  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QScatterDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->setSeries(series);
}

//  a Python function taken by a CuteQScatterDataProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScatterDataProxyPrivate(
    QScatterDataProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScatterDataProxyPrivate *>(self)->take(key, call);
}

//  void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries(
    QScatterDataProxyPrivate *self,
    QAbstract3DSeries *series) {
  self->QScatterDataProxyPrivate::setSeries(series);
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
