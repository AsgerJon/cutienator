//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qpiemodelmapper_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qpiemodelmapper.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qpiemodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtGraphs/qpieslice.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtGraphs/qpiemodelmapper.h>
#include <QtGraphs/qpieseries.h>
#include <QtGraphs/private/qpiemodelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 430, as _ZN22QPieModelMapperPrivateD1Ev
inline QPieModelMapperPrivate::~QPieModelMapperPrivate() {}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 428, as _ZN22QPieModelMapperPrivateC1Ev
inline QPieModelMapperPrivate::QPieModelMapperPrivate() {}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 568, as _ZN22QPieModelMapperPrivate19onSliceLabelChangedEPK9QPieSlice
inline void QPieModelMapperPrivate::onSliceLabelChanged(const QPieSlice *slice) {
    if (m_seriesSignalsBlock)
        return;

    blockModelSignals();
    m_model->setData(labelModelIndex(m_series->slices().indexOf(slice)), slice->label());
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 577, as _ZN22QPieModelMapperPrivate19onSliceValueChangedEPK9QPieSlice
inline void QPieModelMapperPrivate::onSliceValueChanged(const QPieSlice *slice) {
    if (m_seriesSignalsBlock)
        return;

    blockModelSignals();
    m_model->setData(valueModelIndex(m_series->slices().indexOf(slice)), slice->value());
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 588, as _ZN22QPieModelMapperPrivate14onModelUpdatedE11QModelIndexS0_
inline void QPieModelMapperPrivate::onModelUpdated(QModelIndex topLeft, QModelIndex bottomRight)
{
    if (m_model == nullptr || m_series == nullptr)
        return;

    if (m_modelSignalsBlock)
        return;

    blockSeriesSignals();
    QModelIndex index;
    QPieSlice *slice;
    for (int row = topLeft.row(); row <= bottomRight.row(); row++) {
        for (int column = topLeft.column(); column <= bottomRight.column(); column++) {
            index = topLeft.sibling(row, column);
            slice = pieSlice(index);
            if (slice) {
                if (isValueIndex(index))
                    slice->setValue(m_model->data(index, Qt::DisplayRole).toReal());
                if (isLabelIndex(index))
                    slice->setLabel(m_model->data(index, Qt::DisplayRole).toString());
            }
        }
    }
    blockSeriesSignals(false);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 678, as _ZN22QPieModelMapperPrivate20handleModelDestroyedEv
inline void QPieModelMapperPrivate::handleModelDestroyed() { m_model = nullptr; }

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 504, as _ZN22QPieModelMapperPrivate13onSlicesAddedERK5QListIP9QPieSliceE
inline void QPieModelMapperPrivate::onSlicesAdded(const QList<QPieSlice *> &slices) {
    if (m_seriesSignalsBlock)
        return;

    if (slices.size() == 0)
        return;

    int firstIndex = int(m_series->slices().indexOf(slices.at(0)));
    if (firstIndex == -1)
        return;

    if (m_count != -1)
        m_count += slices.size();
    Q_Q(QPieModelMapper);
    for (int i = firstIndex; i < firstIndex + slices.size(); i++) {
        m_slices.insert(i, slices.at(i - firstIndex));
        QObject::connect(slices.at(i - firstIndex),
                         &QPieSlice::labelChanged,
                         q,
                         &QPieModelMapper::onSliceLabelChanged);
        QObject::connect(slices.at(i - firstIndex),
                         &QPieSlice::valueChanged,
                         q,
                         &QPieModelMapper::onSliceValueChanged);
    }

    blockModelSignals();
    if (m_orientation == Qt::Vertical)
        m_model->insertRows(firstIndex + m_first, int(slices.size()));
    else
        m_model->insertColumns(firstIndex + m_first, int(slices.size()));

    for (int i = firstIndex; i < firstIndex + slices.size(); i++) {
        m_model->setData(valueModelIndex(i), slices.at(i - firstIndex)->value());
        m_model->setData(labelModelIndex(i), slices.at(i - firstIndex)->label());
    }
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 543, as _ZN22QPieModelMapperPrivate15onSlicesRemovedERK5QListIP9QPieSliceE
inline void QPieModelMapperPrivate::onSlicesRemoved(const QList<QPieSlice *> &slices) {
    if (m_seriesSignalsBlock)
        return;

    if (slices.size() == 0)
        return;

    int firstIndex = int(m_slices.indexOf(slices.at(0)));
    if (firstIndex == -1)
        return;

    if (m_count != -1)
        m_count -= slices.size();

    for (int i = firstIndex + int(slices.size()) - 1; i >= firstIndex; i--)
        m_slices.removeAt(i);

    blockModelSignals();
    if (m_orientation == Qt::Vertical)
        m_model->removeRows(firstIndex + m_first, int(slices.size()));
    else
        m_model->removeColumns(firstIndex + m_first, int(slices.size()));
    blockModelSignals(false);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 586, as _ZN22QPieModelMapperPrivate21handleSeriesDestroyedEv
inline void QPieModelMapperPrivate::handleSeriesDestroyed() { m_series = nullptr; }

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 440, as _ZNK22QPieModelMapperPrivate8pieSliceE11QModelIndex
inline QPieSlice *QPieModelMapperPrivate::pieSlice(QModelIndex index) const {
    if (!index.isValid())
        return 0; // index is invalid

    if (m_orientation == Qt::Vertical
        && (index.column() == m_valuesSection || index.column() == m_labelsSection)) {
        if (index.row() >= m_first && (m_count == -1 || index.row() < m_first + m_count)) {
            if (m_model->index(index.row(), m_valuesSection).isValid()
                && m_model->index(index.row(), m_labelsSection).isValid())
                return m_series->slices().at(index.row() - m_first);
            else
                return 0;
        }
    } else if (m_orientation == Qt::Horizontal
               && (index.row() == m_valuesSection || index.row() == m_labelsSection)) {
        if (index.column() >= m_first && (m_count == -1 || index.column() < m_first + m_count)) {
            if (m_model->index(m_valuesSection, index.column()).isValid()
                && m_model->index(m_labelsSection, index.column()).isValid())
                return m_series->slices().at(index.column() - m_first);
            else
                return 0;
        }
    }
    return 0; // This part of model has not been mapped to any slice
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 486, as _ZNK22QPieModelMapperPrivate12isLabelIndexE11QModelIndex
inline bool QPieModelMapperPrivate::isLabelIndex(QModelIndex index) const {
    if (m_orientation == Qt::Vertical && index.column() == m_labelsSection)
        return true;
    else if (m_orientation == Qt::Horizontal && index.row() == m_labelsSection)
        return true;

    return false;
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 495, as _ZNK22QPieModelMapperPrivate12isValueIndexE11QModelIndex
inline bool QPieModelMapperPrivate::isValueIndex(QModelIndex index) const {
    if (m_orientation == Qt::Vertical && index.column() == m_valuesSection)
        return true;
    else if (m_orientation == Qt::Horizontal && index.row() == m_valuesSection)
        return true;

    return false;
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 466, as _ZN22QPieModelMapperPrivate15valueModelIndexEx
inline QModelIndex QPieModelMapperPrivate::valueModelIndex(qsizetype sliceIndex) {
    if (m_count != -1 && sliceIndex >= m_count)
        return QModelIndex(); // invalid

    if (m_orientation == Qt::Vertical)
        return m_model->index(int(sliceIndex) + m_first, m_valuesSection);
    else
        return m_model->index(m_valuesSection, int(sliceIndex) + m_first);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 476, as _ZN22QPieModelMapperPrivate15labelModelIndexEx
inline QModelIndex QPieModelMapperPrivate::labelModelIndex(qsizetype sliceIndex) {
    if (m_count != -1 && sliceIndex >= m_count)
        return QModelIndex(); // invalid

    if (m_orientation == Qt::Vertical)
        return m_model->index(int(sliceIndex) + m_first, m_labelsSection);
    else
        return m_model->index(m_labelsSection, int(sliceIndex) + m_first);
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 432, as _ZN22QPieModelMapperPrivate17blockModelSignalsEb
inline void QPieModelMapperPrivate::blockModelSignals(bool block) {
    m_modelSignalsBlock = block;
}

//  from ../qtgraphs/src/graphs2d/piechart/qpiemodelmapper.cpp, line 436, as _ZN22QPieModelMapperPrivate18blockSeriesSignalsEb
inline void QPieModelMapperPrivate::blockSeriesSignals(bool block) {
    m_seriesSignalsBlock = block;
}
//  -----------------------------------------------------------------------

//  QPieModelMapper *QPieModelMapperPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPieModelMapper *ritual_ZN22QPieModelMapperPrivate6q_funcEv(
    QPieModelMapperPrivate *self) {
  return self->q_func();
}

//  const QPieModelMapper *QPieModelMapperPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPieModelMapper *ritual_ZNK22QPieModelMapperPrivate6q_funcEv(
    const QPieModelMapperPrivate *self) {
  return self->q_func();
}

//  QPieModelMapperPrivate::QPieModelMapperPrivate()
extern "C" Q_DECL_EXPORT
QPieModelMapperPrivate *ritual_ZN22QPieModelMapperPrivateC1Ev() {
  return new QPieModelMapperPrivate();
}

//  QPieModelMapperPrivate::~QPieModelMapperPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivateD1Ev(QPieModelMapperPrivate *self) {
  delete self;
}

//  void QPieModelMapperPrivate::onSliceLabelChanged(const QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate19onSliceLabelChangedEPK9QPieSlice(
    QPieModelMapperPrivate *self,
    const QPieSlice *slice) {
  self->onSliceLabelChanged(slice);
}

//  void QPieModelMapperPrivate::onSliceValueChanged(const QPieSlice *slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate19onSliceValueChangedEPK9QPieSlice(
    QPieModelMapperPrivate *self,
    const QPieSlice *slice) {
  self->onSliceValueChanged(slice);
}

//  void QPieModelMapperPrivate::onModelUpdated(QModelIndex topLeft,
//      QModelIndex bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate14onModelUpdatedE11QModelIndexS0_(
    QPieModelMapperPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->onModelUpdated(*topLeft, *bottomRight);
}

//  void QPieModelMapperPrivate::handleModelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate20handleModelDestroyedEv(
    QPieModelMapperPrivate *self) {
  self->handleModelDestroyed();
}

//  void QPieModelMapperPrivate::onSlicesAdded(const QList<QPieSlice *>
//      &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate13onSlicesAddedERK5QListIP9QPieSliceE(
    QPieModelMapperPrivate *self,
    const QList<QPieSlice *> *slices) {
  self->onSlicesAdded(*slices);
}

//  void QPieModelMapperPrivate::onSlicesRemoved(const QList<QPieSlice *>
//      &slices)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate15onSlicesRemovedERK5QListIP9QPieSliceE(
    QPieModelMapperPrivate *self,
    const QList<QPieSlice *> *slices) {
  self->onSlicesRemoved(*slices);
}

//  void QPieModelMapperPrivate::handleSeriesDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate21handleSeriesDestroyedEv(
    QPieModelMapperPrivate *self) {
  self->handleSeriesDestroyed();
}

//  QPieSlice *QPieModelMapperPrivate::pieSlice(QModelIndex index) const
extern "C" Q_DECL_EXPORT
QPieSlice *ritual_ZNK22QPieModelMapperPrivate8pieSliceE11QModelIndex(
    const QPieModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->pieSlice(*index);
}

//  bool QPieModelMapperPrivate::isLabelIndex(QModelIndex index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPieModelMapperPrivate12isLabelIndexE11QModelIndex(
    const QPieModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->isLabelIndex(*index);
}

//  bool QPieModelMapperPrivate::isValueIndex(QModelIndex index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QPieModelMapperPrivate12isValueIndexE11QModelIndex(
    const QPieModelMapperPrivate *self,
    const QModelIndex *index) {
  return self->isValueIndex(*index);
}

//  QModelIndex QPieModelMapperPrivate::valueModelIndex(qsizetype sliceIndex)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN22QPieModelMapperPrivate15valueModelIndexEx(
    QPieModelMapperPrivate *self,
    qsizetype sliceIndex) {
  return new QModelIndex(self->valueModelIndex(sliceIndex));
}

//  QModelIndex QPieModelMapperPrivate::labelModelIndex(qsizetype sliceIndex)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN22QPieModelMapperPrivate15labelModelIndexEx(
    QPieModelMapperPrivate *self,
    qsizetype sliceIndex) {
  return new QModelIndex(self->labelModelIndex(sliceIndex));
}

//  void QPieModelMapperPrivate::blockModelSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate17blockModelSignalsEb(
    QPieModelMapperPrivate *self,
    bool block) {
  self->blockModelSignals(block);
}

//  void QPieModelMapperPrivate::blockSeriesSignals(bool block)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QPieModelMapperPrivate18blockSeriesSignalsEb(
    QPieModelMapperPrivate *self,
    bool block) {
  self->blockSeriesSignals(block);
}

#endif  // (QT_CONFIG(graphs_2d)) && (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_donut_pie))
