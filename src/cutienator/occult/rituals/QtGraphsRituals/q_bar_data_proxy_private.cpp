//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qbardataproxy_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbardataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qbardataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QPair>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qbar3dseries_p.h>
#include <QtGraphs/private/qbardataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#include <QtCore/qmath.h>
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qbar3dseries_p.h>
#include <QtGraphs/private/qcategory3daxis_p.h>
#include <QtGraphs/private/qquickgraphsbars_p.h>
#include <QtGraphs/private/qvalue3daxis_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGui/qquaternion.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 698, as _ZN20QBarDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QBarDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QBarDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QBar3DSeries *barSeries = static_cast<QBar3DSeries *>(series);
    emit q->seriesChanged(barSeries);
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 549, as _ZN20QBarDataProxyPrivateD2Ev
inline QBarDataProxyPrivate::~QBarDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 82, as _ZN25QAbstractDataProxyPrivateC2EN18QAbstractDataProxy8DataTypeE
inline QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(QAbstractDataProxy::DataType type)
    : m_type(type)
    , m_series(0)
{}

//  from ../qtgraphs/src/graphs3d/data/qbar3dseries.cpp, line 759, as _ZN19QBar3DSeriesPrivate12fixRowLabelsExxRK5QListI7QStringEb
inline void QBar3DSeriesPrivate::fixRowLabels(qsizetype startIndex,
                                       qsizetype count,
                                       const QStringList &newLabels,
                                       bool isInsert)
{
    bool changed = false;
    qsizetype currentSize = m_rowLabels.size();

    qsizetype newSize = newLabels.size();
    if (startIndex >= currentSize) {
        // Adding labels past old label array, create empty strings to fill
        // intervening space
        if (newSize) {
            for (qsizetype i = currentSize; i < startIndex; i++)
                m_rowLabels << QString();
            // Doesn't matter if insert, append, or just change when there were no
            // existing strings, just append new strings.
            m_rowLabels << newLabels;
            changed = true;
        }
    } else {
        if (isInsert) {
            qsizetype insertIndex = startIndex;
            if (count)
                changed = true;
            for (qsizetype i = 0; i < count; i++) {
                if (i < newSize)
                    m_rowLabels.insert(insertIndex++, newLabels.at(i));
                else
                    m_rowLabels.insert(insertIndex++, QString());
            }
        } else {
            // Either append or change, replace labels up to array end and then add
            // new ones
            qsizetype lastChangeIndex = count + startIndex;
            qsizetype newIndex = 0;
            for (qsizetype i = startIndex; i < lastChangeIndex; i++) {
                if (i >= currentSize) {
                    // Label past the current size, so just append the new label
                    if (newSize < newIndex) {
                        changed = true;
                        m_rowLabels << newLabels.at(newIndex);
                    } else {
                        break; // No point appending empty strings, so just exit
                    }
                } else if (newSize > newIndex) {
                    // Replace existing label
                    if (m_rowLabels.at(i) != newLabels.at(newIndex)) {
                        changed = true;
                        m_rowLabels[i] = newLabels.at(newIndex);
                    }
                } else {
                    // No more new labels, so clear existing label
                    if (!m_rowLabels.at(i).isEmpty()) {
                        changed = true;
                        m_rowLabels[i] = QString();
                    }
                }
                newIndex++;
            }
        }
    }

    if (changed) {
        Q_Q(QBar3DSeries);
        emit q->rowLabelsChanged();
    }
}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 89, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QAbstractDataProxy);
    q->setParent(series);
    m_series = series;
}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 87, as _ZN25QAbstractDataProxyPrivateD2Ev
inline QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 545, as _ZN20QBarDataProxyPrivateC1Ev
inline QBarDataProxyPrivate::QBarDataProxyPrivate()
    : QAbstractDataProxyPrivate(QAbstractDataProxy::DataType::Bar)
{}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 551, as _ZN20QBarDataProxyPrivate10resetArrayEO5QListIS0_I12QBarDataItemEEOS0_I7QStringES7_
inline void QBarDataProxyPrivate::resetArray(QBarDataArray &&newArray,
                                      QStringList &&rowLabels,
                                      QStringList &&columnLabels)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    barSeries->setRowLabels(rowLabels);
    barSeries->setColumnLabels(columnLabels);

    if (newArray.data() != barSeries->dataArray().data()) {
        barSeries->clearArray();
        barSeries->setDataArray(newArray);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 565, as _ZN20QBarDataProxyPrivate6setRowExO5QListI12QBarDataItemEO7QString
inline void QBarDataProxyPrivate::setRow(qsizetype rowIndex, QBarDataRow &&row, QString &&label)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex < barSeries->dataArray().size());

    QBar3DSeriesPrivate::get(barSeries)->fixRowLabels(rowIndex, 1, QStringList(label), false);
    if (row.data() != barSeries->dataArray().at(rowIndex).data()) {
        barSeries->clearRow(rowIndex);
        QBarDataArray array = barSeries->dataArray();
        array[rowIndex] = row;
        barSeries->setDataArray(array);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 579, as _ZN20QBarDataProxyPrivate7setRowsExO5QListIS0_I12QBarDataItemEEOS0_I7QStringE
inline void QBarDataProxyPrivate::setRows(qsizetype rowIndex, QBarDataArray &&rows, QStringList &&labels)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && (rowIndex + rows.size()) <= barSeries->dataArray().size());

    QBar3DSeriesPrivate::get(barSeries)->fixRowLabels(rowIndex, rows.size(), labels, false);
    for (int i = 0; i < rows.size(); i++) {
        if (rows.at(i).data() != barSeries->dataArray().at(rowIndex).data()) {
            barSeries->clearRow(rowIndex);
            QBarDataArray array = barSeries->dataArray();
            array[rowIndex] = rows.at(i);
            barSeries->setDataArray(array);
        }
        rowIndex++;
    }
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 596, as _ZN20QBarDataProxyPrivate7setItemExxO12QBarDataItem
inline void QBarDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype columnIndex, QBarDataItem &&item)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex < barSeries->dataArray().size());
    QBarDataArray array = barSeries->dataArray();
    QBarDataRow &row = array[rowIndex];
    Q_ASSERT(columnIndex < row.size());
    row[columnIndex] = item;
    barSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 607, as _ZN20QBarDataProxyPrivate6addRowEO5QListI12QBarDataItemEO7QString
inline qsizetype QBarDataProxyPrivate::addRow(QBarDataRow &&row, QString &&label)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    qsizetype currentSize = barSeries->dataArray().size();
    QBar3DSeriesPrivate::get(barSeries)->fixRowLabels(currentSize, 1, QStringList(label), false);
    QBarDataArray array = barSeries->dataArray();
    array.append(row);
    barSeries->setDataArray(array);
    return currentSize;
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 618, as _ZN20QBarDataProxyPrivate7addRowsEO5QListIS0_I12QBarDataItemEEOS0_I7QStringE
inline qsizetype QBarDataProxyPrivate::addRows(QBarDataArray &&rows, QStringList &&labels)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    QBarDataArray array = barSeries->dataArray();
    qsizetype currentSize = array.size();
    QBar3DSeriesPrivate::get(barSeries)->fixRowLabels(currentSize, rows.size(), labels, false);
    for (int i = 0; i < rows.size(); i++)
        array.append(rows.at(i));
    barSeries->setDataArray(array);
    return currentSize;
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 630, as _ZN20QBarDataProxyPrivate9insertRowExO5QListI12QBarDataItemEO7QString
inline void QBarDataProxyPrivate::insertRow(qsizetype rowIndex, QBarDataRow &&row, QString &&label)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex <= barSeries->dataArray().size());
    QBar3DSeriesPrivate::get(barSeries)->fixRowLabels(rowIndex, 1, QStringList(label), true);
    QBarDataArray array = barSeries->dataArray();
    array.insert(rowIndex, row);
    barSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 640, as _ZN20QBarDataProxyPrivate10insertRowsExO5QListIS0_I12QBarDataItemEEOS0_I7QStringE
inline void QBarDataProxyPrivate::insertRows(qsizetype rowIndex, QBarDataArray &&rows, QStringList &&labels)
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex <= barSeries->dataArray().size());
    QBarDataArray array = barSeries->dataArray();

    QBar3DSeriesPrivate::get(barSeries)->fixRowLabels(rowIndex, rows.size(), labels, true);
    for (int i = 0; i < rows.size(); i++)
        array.insert(rowIndex++, rows.at(i));
    barSeries->setDataArray(array);
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

//  from ../qtgraphs/src/graphs3d/data/qbardataproxy.cpp, line 675, as _ZNK20QBarDataProxyPrivate11limitValuesExxxx
inline QPair<float, float> QBarDataProxyPrivate::limitValues(qsizetype startRow,
                                                      qsizetype endRow,
                                                      qsizetype startColumn,
                                                      qsizetype endColumn) const
{
    auto *barSeries = static_cast<QBar3DSeries *>(series());
    QPair<float, float> limits = qMakePair(0.0f, 0.0f);
    endRow = qMin(endRow, barSeries->dataArray().size() - 1);
    for (qsizetype i = startRow; i <= endRow; i++) {
        QBarDataRow row = barSeries->dataArray().at(i);
        qsizetype lastColumn = qMin(endColumn, row.size() - 1);
        for (qsizetype j = startColumn; j <= lastColumn; j++) {
            const QBarDataItem &item = row.at(j);
            float itemValue = item.value();
            if (limits.second < itemValue)
                limits.second = itemValue;
            if (limits.first > itemValue)
                limits.first = itemValue;
        }
    }
    return limits;
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

//  QBarDataProxyPrivate::QBarDataProxyPrivate()
extern "C" Q_DECL_EXPORT
QBarDataProxyPrivate *ritual_ZN20QBarDataProxyPrivateC1Ev() {
  return new CuteQBarDataProxyPrivate();
}

//  QBarDataProxyPrivate::~QBarDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivateD1Ev(QBarDataProxyPrivate *self) {
  delete self;
}

//  void QBarDataProxyPrivate::resetArray(QBarDataArray &&newArray,
//      QStringList &&rowLabels, QStringList &&columnLabels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10resetArrayEO5QListIS0_I12QBarDataItemEEOS0_I7QStringES7_(
    QBarDataProxyPrivate *self,
    QBarDataArray *newArray,
    QStringList *rowLabels,
    QStringList *columnLabels) {
  self->resetArray(
      std::move(*newArray),
      std::move(*rowLabels),
      std::move(*columnLabels));
}

//  void QBarDataProxyPrivate::setRow(qsizetype rowIndex, QBarDataRow &&row,
//      QString &&label)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate6setRowExO5QListI12QBarDataItemEO7QString(
    QBarDataProxyPrivate *self,
    qsizetype rowIndex,
    QBarDataRow *row,
    QString *label) {
  self->setRow(rowIndex, std::move(*row), std::move(*label));
}

//  void QBarDataProxyPrivate::setRows(qsizetype rowIndex, QBarDataArray
//      &&rows, QStringList &&labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate7setRowsExO5QListIS0_I12QBarDataItemEEOS0_I7QStringE(
    QBarDataProxyPrivate *self,
    qsizetype rowIndex,
    QBarDataArray *rows,
    QStringList *labels) {
  self->setRows(rowIndex, std::move(*rows), std::move(*labels));
}

//  void QBarDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype
//      columnIndex, QBarDataItem &&item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate7setItemExxO12QBarDataItem(
    QBarDataProxyPrivate *self,
    qsizetype rowIndex,
    qsizetype columnIndex,
    QBarDataItem *item) {
  self->setItem(rowIndex, columnIndex, std::move(*item));
}

//  qsizetype QBarDataProxyPrivate::addRow(QBarDataRow &&row, QString
//      &&label)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QBarDataProxyPrivate6addRowEO5QListI12QBarDataItemEO7QString(
    QBarDataProxyPrivate *self,
    QBarDataRow *row,
    QString *label) {
  return self->addRow(std::move(*row), std::move(*label));
}

//  qsizetype QBarDataProxyPrivate::addRows(QBarDataArray &&rows, QStringList
//      &&labels)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN20QBarDataProxyPrivate7addRowsEO5QListIS0_I12QBarDataItemEEOS0_I7QStringE(
    QBarDataProxyPrivate *self,
    QBarDataArray *rows,
    QStringList *labels) {
  return self->addRows(std::move(*rows), std::move(*labels));
}

//  void QBarDataProxyPrivate::insertRow(qsizetype rowIndex, QBarDataRow
//      &&row, QString &&label)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate9insertRowExO5QListI12QBarDataItemEO7QString(
    QBarDataProxyPrivate *self,
    qsizetype rowIndex,
    QBarDataRow *row,
    QString *label) {
  self->insertRow(rowIndex, std::move(*row), std::move(*label));
}

//  void QBarDataProxyPrivate::insertRows(qsizetype rowIndex, QBarDataArray
//      &&rows, QStringList &&labels)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBarDataProxyPrivate10insertRowsExO5QListIS0_I12QBarDataItemEEOS0_I7QStringE(
    QBarDataProxyPrivate *self,
    qsizetype rowIndex,
    QBarDataArray *rows,
    QStringList *labels) {
  self->insertRows(rowIndex, std::move(*rows), std::move(*labels));
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

//  QPair<float, float> QBarDataProxyPrivate::limitValues(qsizetype startRow,
//      qsizetype startColumn, qsizetype rowCount, qsizetype columnCount)
//      const
extern "C" Q_DECL_EXPORT
QPair<float, float> *ritual_ZNK20QBarDataProxyPrivate11limitValuesExxxx(
    const QBarDataProxyPrivate *self,
    qsizetype startRow,
    qsizetype startColumn,
    qsizetype rowCount,
    qsizetype columnCount) {
  return new QPair<float, float>(
      self->limitValues(
          startRow,
          startColumn,
          rowCount,
          columnCount));
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

//  a QPair<float, float> a ritual of QBarDataProxyPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBarDataProxyPrivate__QPair_float_float(
    QPair<float, float> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
