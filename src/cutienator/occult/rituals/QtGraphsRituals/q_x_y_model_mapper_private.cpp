//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qxymodelmapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qxymodelmapper.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qxymodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QAbstractItemModel>
#include <QtGraphs/QXYModelMapper>
#include <QtGraphs/QXYSeries>
#include <QtGraphs/private/qxymodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 637, as _ZN21QXYModelMapperPrivate16onModelRowsAddedE11QModelIndexxx
inline void QXYModelMapperPrivate::onModelRowsAdded(QModelIndex parent, qsizetype start, qsizetype end)
{
    Q_UNUSED(parent);
    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    if (m_orientation == Qt::Vertical) {
        insertData(start, end);
    } else if (start <= m_xSection || start <= m_ySection) {
        // if the changes affect the map - reinitialize the xy
        initializeXYFromModel();
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 653, as _ZN21QXYModelMapperPrivate18onModelRowsRemovedE11QModelIndexxx
inline void QXYModelMapperPrivate::onModelRowsRemoved(QModelIndex parent, qsizetype start, qsizetype end)
{
    Q_UNUSED(parent);
    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    if (m_orientation == Qt::Vertical) {
        removeData(start, end);
    } else if (start <= m_xSection || start <= m_ySection) {
        // if the changes affect the map - reinitialize the xy
        initializeXYFromModel();
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 669, as _ZN21QXYModelMapperPrivate19onModelColumnsAddedE11QModelIndexxx
inline void QXYModelMapperPrivate::onModelColumnsAdded(QModelIndex parent, qsizetype start, qsizetype end)
{
    Q_UNUSED(parent);
    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    if (m_orientation == Qt::Horizontal) {
        insertData(start, end);
    } else if (start <= m_xSection || start <= m_ySection) {
        // if the changes affect the map - reinitialize the xy
        initializeXYFromModel();
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 685, as _ZN21QXYModelMapperPrivate21onModelColumnsRemovedE11QModelIndexxx
inline void QXYModelMapperPrivate::onModelColumnsRemoved(QModelIndex parent, qsizetype start, qsizetype end)
{
    Q_UNUSED(parent);
    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    if (m_orientation == Qt::Horizontal) {
        removeData(start, end);
    } else if (start <= m_xSection || start <= m_ySection) {
        // if the changes affect the map - reinitialize the xy
        initializeXYFromModel();
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 701, as _ZN21QXYModelMapperPrivate20handleModelDestroyedEv
inline void QXYModelMapperPrivate::handleModelDestroyed()
{
    m_model = 0;
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 521, as _ZN21QXYModelMapperPrivate12onPointAddedEx
inline void QXYModelMapperPrivate::onPointAdded(qsizetype pointIndex)
{
    if (m_seriesSignalsBlock)
        return;

    if (m_count != -1)
        m_count += 1;

    blockModelSignals();
    if (m_orientation == Qt::Vertical)
        m_model->insertRows(int(pointIndex) + m_first, 1);
    else
        m_model->insertColumns(int(pointIndex) + m_first, 1);

    setValueToModel(xModelIndex(pointIndex), m_series->points().at(pointIndex).x());
    setValueToModel(yModelIndex(pointIndex), m_series->points().at(pointIndex).y());
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 540, as _ZN21QXYModelMapperPrivate14onPointRemovedEx
inline void QXYModelMapperPrivate::onPointRemoved(qsizetype pointIndex)
{
    if (m_seriesSignalsBlock)
        return;

    if (m_count != -1)
        m_count -= 1;

    blockModelSignals();
    if (m_orientation == Qt::Vertical)
        m_model->removeRow(int(pointIndex) + m_first);
    else
        m_model->removeColumn(int(pointIndex) + m_first);
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 556, as _ZN21QXYModelMapperPrivate15onPointsRemovedExx
inline void QXYModelMapperPrivate::onPointsRemoved(qsizetype pointIndex, qsizetype count)
{
    if (m_seriesSignalsBlock)
        return;

    m_count -= count;

    if (m_count < -1)
        m_count = -1;

    blockModelSignals();
    if (m_orientation == Qt::Vertical)
        m_model->removeRows(int(pointIndex) + m_first, int(count));
    else
        m_model->removeColumns(int(pointIndex) + m_first, int(count));
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 574, as _ZN21QXYModelMapperPrivate15onPointReplacedEx
inline void QXYModelMapperPrivate::onPointReplaced(qsizetype pointIndex)
{
    if (m_seriesSignalsBlock)
        return;

    blockModelSignals();
    setValueToModel(xModelIndex(pointIndex), m_series->points().at(pointIndex).x());
    setValueToModel(yModelIndex(pointIndex), m_series->points().at(pointIndex).y());
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 585, as _ZN21QXYModelMapperPrivate21handleSeriesDestroyedEv
inline void QXYModelMapperPrivate::handleSeriesDestroyed()
{
    m_series = 0;
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 473, as _ZN21QXYModelMapperPrivate11xModelIndexEx
inline QModelIndex QXYModelMapperPrivate::xModelIndex(qsizetype xIndex)
{
    if (m_count != -1 && xIndex >= m_count)
        return QModelIndex(); // invalid
    if (m_orientation == Qt::Vertical)
        return m_model->index(int(xIndex) + m_first, m_xSection);
    else
        return m_model->index(m_xSection, int(xIndex) + m_first);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 483, as _ZN21QXYModelMapperPrivate11yModelIndexEx
inline QModelIndex QXYModelMapperPrivate::yModelIndex(qsizetype yIndex)
{
    if (m_count != -1 && yIndex >= m_count)
        return QModelIndex(); // invalid
    if (m_orientation == Qt::Vertical)
        return m_model->index(int(yIndex) + m_first, m_ySection);
    else
        return m_model->index(m_ySection, int(yIndex) + m_first);
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 463, as _ZN21QXYModelMapperPrivate17blockModelSignalsEb
inline void QXYModelMapperPrivate::blockModelSignals(bool block)
{
    m_modelSignalsBlock = block;
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 468, as _ZN21QXYModelMapperPrivate18blockSeriesSignalsEb
inline void QXYModelMapperPrivate::blockSeriesSignals(bool block)
{
    m_seriesSignalsBlock = block;
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 493, as _ZN21QXYModelMapperPrivate14valueFromModelE11QModelIndex
inline qreal QXYModelMapperPrivate::valueFromModel(QModelIndex index)
{
    QVariant value = m_model->data(index, Qt::DisplayRole);
    switch (value.metaType().id()) {
    case QMetaType::QDateTime:
        return value.toDateTime().toMSecsSinceEpoch();
    case QMetaType::QDate:
        return value.toDate().startOfDay().toMSecsSinceEpoch();
    default:
        return value.toReal();
    }
}

//  from ../qtgraphs/src/graphs2d/xychart/qxymodelmapper.cpp, line 506, as _ZN21QXYModelMapperPrivate15setValueToModelE11QModelIndexd
inline void QXYModelMapperPrivate::setValueToModel(QModelIndex index, qreal value)
{
    QVariant oldValue = m_model->data(index, Qt::DisplayRole);
    switch (oldValue.metaType().id()) {
    case QMetaType::QDateTime:
        m_model->setData(index, QDateTime::fromMSecsSinceEpoch(value));
        break;
    case QMetaType::QDate:
        m_model->setData(index, QDateTime::fromMSecsSinceEpoch(value).date());
        break;
    default:
        m_model->setData(index, value);
    }
}
//  -----------------------------------------------------------------------

//  QXYModelMapper *QXYModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QXYModelMapper *ritual_ZN21QXYModelMapperPrivate6q_funcEv(
    QXYModelMapperPrivate *self) {
  return self->q_func();
}

//  const QXYModelMapper *QXYModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QXYModelMapper *ritual_ZNK21QXYModelMapperPrivate6q_funcEv(
    const QXYModelMapperPrivate *self) {
  return self->q_func();
}

//  void QXYModelMapperPrivate::onModelRowsAdded(QModelIndex parent,
//      qsizetype start, qsizetype end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate16onModelRowsAddedE11QModelIndexxx(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    qsizetype start,
    qsizetype end) {
  self->onModelRowsAdded(*parent, start, end);
}

//  void QXYModelMapperPrivate::onModelRowsRemoved(QModelIndex parent,
//      qsizetype start, qsizetype end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate18onModelRowsRemovedE11QModelIndexxx(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    qsizetype start,
    qsizetype end) {
  self->onModelRowsRemoved(*parent, start, end);
}

//  void QXYModelMapperPrivate::onModelColumnsAdded(QModelIndex parent,
//      qsizetype start, qsizetype end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate19onModelColumnsAddedE11QModelIndexxx(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    qsizetype start,
    qsizetype end) {
  self->onModelColumnsAdded(*parent, start, end);
}

//  void QXYModelMapperPrivate::onModelColumnsRemoved(QModelIndex parent,
//      qsizetype start, qsizetype end)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate21onModelColumnsRemovedE11QModelIndexxx(
    QXYModelMapperPrivate *self,
    const QModelIndex *parent,
    qsizetype start,
    qsizetype end) {
  self->onModelColumnsRemoved(*parent, start, end);
}

//  void QXYModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate20handleModelDestroyedEv(
    QXYModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QXYModelMapperPrivate::onPointAdded(qsizetype pointIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate12onPointAddedEx(
    QXYModelMapperPrivate *self,
    qsizetype pointIndex) {
  self->onPointAdded(pointIndex);
}

//  void QXYModelMapperPrivate::onPointRemoved(qsizetype pointIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate14onPointRemovedEx(
    QXYModelMapperPrivate *self,
    qsizetype pointIndex) {
  self->onPointRemoved(pointIndex);
}

//  void QXYModelMapperPrivate::onPointsRemoved(qsizetype pointIndex,
//      qsizetype count)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate15onPointsRemovedExx(
    QXYModelMapperPrivate *self,
    qsizetype pointIndex,
    qsizetype count) {
  self->onPointsRemoved(pointIndex, count);
}

//  void QXYModelMapperPrivate::onPointReplaced(qsizetype pointIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate15onPointReplacedEx(
    QXYModelMapperPrivate *self,
    qsizetype pointIndex) {
  self->onPointReplaced(pointIndex);
}

//  void QXYModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate21handleSeriesDestroyedEv(
    QXYModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

//  QModelIndex QXYModelMapperPrivate::xModelIndex(qsizetype xIndex)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN21QXYModelMapperPrivate11xModelIndexEx(
    QXYModelMapperPrivate *self,
    qsizetype xIndex) {
  return new QModelIndex(self->xModelIndex(xIndex));
}

//  QModelIndex QXYModelMapperPrivate::yModelIndex(qsizetype yIndex)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN21QXYModelMapperPrivate11yModelIndexEx(
    QXYModelMapperPrivate *self,
    qsizetype yIndex) {
  return new QModelIndex(self->yModelIndex(yIndex));
}

//  void QXYModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate17blockModelSignalsEb(
    QXYModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QXYModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate18blockSeriesSignalsEb(
    QXYModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  qreal QXYModelMapperPrivate::valueFromModel(QModelIndex index)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN21QXYModelMapperPrivate14valueFromModelE11QModelIndex(
    QXYModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->valueFromModel(*index);
}

//  void QXYModelMapperPrivate::setValueToModel(QModelIndex index, qreal
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QXYModelMapperPrivate15setValueToModelE11QModelIndexd(
    QXYModelMapperPrivate *self,
    const QModelIndex *index,
    qreal value) {
  self->setValueToModel(*index, value);
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_area) || QT_CONFIG(graphs_2d_line) || QT_CONFIG(graphs_2d_scatter) || QT_CONFIG(graphs_2d_spline))
