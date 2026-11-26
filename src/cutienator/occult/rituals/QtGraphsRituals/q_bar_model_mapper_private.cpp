//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qbarmodelmapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbarmodelmapper.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qbarmodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QAbstractItemModel>
#include <QtGraphs/QBarModelMapper>
#include <QtGraphs/QBarSeries>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtGraphs/private/qbarmodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 467, as _ZN22QBarModelMapperPrivateD1Ev
inline QBarModelMapperPrivate::~QBarModelMapperPrivate() {}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 465, as _ZN22QBarModelMapperPrivateC1Ev
inline QBarModelMapperPrivate::QBarModelMapperPrivate() {}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 469, as _ZN22QBarModelMapperPrivate13barModelIndexExx
inline QModelIndex QBarModelMapperPrivate::barModelIndex(qsizetype barSection, qsizetype posInBar)
{
    if (m_count != -1 && posInBar >= m_count)
        return QModelIndex(); // invalid

    if (barSection < m_firstBarSetSection || barSection > m_lastBarSetSection)
        return QModelIndex(); // invalid

    if (m_orientation == Qt::Vertical)
        return m_model->index(int(posInBar) + m_first, int(barSection));
    else
        return m_model->index(int(barSection), int(posInBar) + m_first);
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 483, as _ZN22QBarModelMapperPrivate18blockSeriesSignalsEb
inline void QBarModelMapperPrivate::blockSeriesSignals(const bool block)
{
    m_seriesSignalsBlock = block;
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 488, as _ZN22QBarModelMapperPrivate17blockModelSignalsEb
inline void QBarModelMapperPrivate::blockModelSignals(const bool block)
{
    m_modelSignalsBlock = block;
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 493, as _ZN22QBarModelMapperPrivate6barSetE11QModelIndex
inline QBarSet *QBarModelMapperPrivate::barSet(QModelIndex index)
{
    if (!index.isValid())
        return 0;

    if (m_orientation == Qt::Vertical && index.column() >= m_firstBarSetSection
        && index.column() <= m_lastBarSetSection) {
        if (index.row() >= m_first && (m_count == -1 || index.row() < m_first + m_count))
            return m_series->barSets().at(index.column() - m_firstBarSetSection);

    } else if (m_orientation == Qt::Horizontal && index.row() >= m_firstBarSetSection
               && index.row() <= m_lastBarSetSection) {
        if (index.column() >= m_first && (m_count == -1 || index.column() < m_first + m_count))
            return m_series->barSets().at(index.row() - m_firstBarSetSection);
    }
    return 0; // This part of model has not been mapped to any slice
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 571, as _ZN22QBarModelMapperPrivate12modelUpdatedE11QModelIndexS0_
inline void QBarModelMapperPrivate::modelUpdated(QModelIndex topLeft, QModelIndex bottomRight)
{
    if (m_model == nullptr || m_series == nullptr)
        return;

    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    QModelIndex index;
    for (int row = topLeft.row(); row <= bottomRight.row(); row++) {
        for (int column = topLeft.column(); column <= bottomRight.column(); column++) {
            index = topLeft.sibling(row, column);
            QBarSet *bar = barSet(index);
            if (bar) {
                if (m_orientation == Qt::Vertical)
                    bar->replace(row - m_first, m_model->data(index).toReal());
                else
                    bar->replace(column - m_first, m_model->data(index).toReal());
            }
        }
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 596, as _ZN22QBarModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11OrientationExx
inline void QBarModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation orientation, qsizetype first, qsizetype last)
{
    if (m_model == nullptr || m_series == nullptr)
        return;

    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    if (orientation != m_orientation) {
        for (int section = first; section <= last; section++) {
            if (section >= m_firstBarSetSection && section <= m_lastBarSetSection) {
                QBarSet *bar = m_series->barSets().at(section - m_firstBarSetSection);
                if (bar)
                    bar->setLabel(m_model->headerData(section, orientation).toString());
            }
        }
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 681, as _ZN22QBarModelMapperPrivate20handleModelDestroyedEv
inline void QBarModelMapperPrivate::handleModelDestroyed()
{
    m_model = nullptr;
}

//  from ../qtgraphs/src/graphs2d/barchart/qbarmodelmapper.cpp, line 839, as _ZN22QBarModelMapperPrivate21handleSeriesDestroyedEv
inline void QBarModelMapperPrivate::handleSeriesDestroyed()
{
    m_series = nullptr;
}
//  -----------------------------------------------------------------------

//  QBarModelMapper *QBarModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBarModelMapper *ritual_ZN22QBarModelMapperPrivate6q_funcEv(
    QBarModelMapperPrivate *self) {
  return self->q_func();
}

//  const QBarModelMapper *QBarModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBarModelMapper *ritual_ZNK22QBarModelMapperPrivate6q_funcEv(
    const QBarModelMapperPrivate *self) {
  return self->q_func();
}

//  QBarModelMapperPrivate::QBarModelMapperPrivate()
extern "C" Q_DECL_EXPORT
QBarModelMapperPrivate *ritual_ZN22QBarModelMapperPrivateC1Ev() {
  return new QBarModelMapperPrivate();
}

//  QBarModelMapperPrivate::~QBarModelMapperPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivateD1Ev(QBarModelMapperPrivate *self) {
  delete self;
}

//  QModelIndex QBarModelMapperPrivate::barModelIndex(qsizetype barSection,
//      qsizetype posInBar)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN22QBarModelMapperPrivate13barModelIndexExx(
    QBarModelMapperPrivate *self,
    qsizetype barSection,
    qsizetype posInBar) {
  return new QModelIndex(self->barModelIndex(barSection, posInBar));
}

//  void QBarModelMapperPrivate::blockSeriesSignals(const bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate18blockSeriesSignalsEb(
    QBarModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

//  void QBarModelMapperPrivate::blockModelSignals(const bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate17blockModelSignalsEb(
    QBarModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  QBarSet *QBarModelMapperPrivate::barSet(QModelIndex index)
extern "C" Q_DECL_EXPORT
QBarSet *ritual_ZN22QBarModelMapperPrivate6barSetE11QModelIndex(
    QBarModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->barSet(*index);
}

//  void QBarModelMapperPrivate::modelUpdated(QModelIndex topLeft,
//      QModelIndex bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate12modelUpdatedE11QModelIndexS0_(
    QBarModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->modelUpdated(*topLeft, *bottomRight);
}

//  void QBarModelMapperPrivate::modelHeaderDataUpdated(Qt::Orientation
//      orientation, qsizetype first, qsizetype last)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate22modelHeaderDataUpdatedEN2Qt11OrientationExx(
    QBarModelMapperPrivate *self,
    Qt::Orientation orientation,
    qsizetype first,
    qsizetype last) {
  self->modelHeaderDataUpdated(orientation, first, last);
}

//  void QBarModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate20handleModelDestroyedEv(
    QBarModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QBarModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QBarModelMapperPrivate21handleSeriesDestroyedEv(
    QBarModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_bar))
