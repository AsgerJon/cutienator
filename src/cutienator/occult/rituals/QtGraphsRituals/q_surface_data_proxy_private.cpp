//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qsurfacedataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsurfacedataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qsurfacedataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qsurface3dseries_p.h>
#include <QtGraphs/private/qsurfacedataproxy_p.h>
#include <QtGraphs/private/qgraphs3dlogging_p.h>
#include <QtGraphs/private/qabstract3dseries_p.h>
#include <QtGraphs/private/qabstractdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 652, as _ZN24QSurfaceDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QSurfaceDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QSurfaceDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QSurface3DSeries *surfaceSeries = static_cast<QSurface3DSeries *>(series);
    emit q->seriesChanged(surfaceSeries);
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 418, as _ZN24QSurfaceDataProxyPrivateD2Ev
inline QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 82, as _ZN25QAbstractDataProxyPrivateC2EN18QAbstractDataProxy8DataTypeE
inline QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(QAbstractDataProxy::DataType type)
    : m_type(type)
    , m_series(0)
{}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 89, as _ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QAbstractDataProxy);
    q->setParent(series);
    m_series = series;
}

//  from ../qtgraphs/src/graphs3d/data/qabstractdataproxy.cpp, line 87, as _ZN25QAbstractDataProxyPrivateD2Ev
inline QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate() {}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 414, as _ZN24QSurfaceDataProxyPrivateC1Ev
inline QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate()
    : QAbstractDataProxyPrivate(QAbstractDataProxy::DataType::Surface)
{}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 420, as _ZN24QSurfaceDataProxyPrivate10resetArrayEO5QListIS0_I16QSurfaceDataItemEE
inline void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray &&newArray)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    if (newArray.data() != surfaceSeries->dataArray().data()) {
        surfaceSeries->clearArray();
        surfaceSeries->setDataArray(newArray);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 429, as _ZN24QSurfaceDataProxyPrivate6setRowExO5QListI16QSurfaceDataItemE
inline void QSurfaceDataProxyPrivate::setRow(qsizetype rowIndex, QSurfaceDataRow &&row)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex < surfaceSeries->dataArray().size());
    Q_ASSERT(surfaceSeries->dataArray().at(rowIndex).size() == row.size());

    if (row.data() != surfaceSeries->dataArray().at(rowIndex).data()) {
        surfaceSeries->clearRow(rowIndex);
        QSurfaceDataArray array = surfaceSeries->dataArray();
        array[rowIndex] = row;
        surfaceSeries->setDataArray(array);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 443, as _ZN24QSurfaceDataProxyPrivate7setRowsExO5QListIS0_I16QSurfaceDataItemEE
inline void QSurfaceDataProxyPrivate::setRows(qsizetype rowIndex, QSurfaceDataArray &&rows)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    QSurfaceDataArray array = surfaceSeries->dataArray();
    Q_ASSERT(rowIndex >= 0 && (rowIndex + rows.size()) <= array.size());

    for (int i = 0; i < rows.size(); i++) {
        Q_ASSERT(surfaceSeries->dataArray().at(rowIndex).size() == rows.at(i).size());
        if (rows.at(i).data() != array.at(rowIndex).data()) {
            surfaceSeries->clearRow(rowIndex);
            array[rowIndex] = rows.at(i);
        }
        rowIndex++;
    }
    surfaceSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 460, as _ZN24QSurfaceDataProxyPrivate7setItemExxO16QSurfaceDataItem
inline void QSurfaceDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype columnIndex, QSurfaceDataItem &&item)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex < surfaceSeries->dataArray().size());
    QSurfaceDataArray array = surfaceSeries->dataArray();
    QSurfaceDataRow &row = array[rowIndex];
    Q_ASSERT(columnIndex < row.size());
    row[columnIndex] = item;
    surfaceSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 471, as _ZN24QSurfaceDataProxyPrivate6addRowEO5QListI16QSurfaceDataItemE
inline qsizetype QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow &&row)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    Q_ASSERT(surfaceSeries->dataArray().isEmpty()
             || surfaceSeries->dataArray().at(0).size() == row.size());
    qsizetype currentSize = surfaceSeries->dataArray().size();
    QSurfaceDataArray array = surfaceSeries->dataArray();
    array.append(row);
    surfaceSeries->setDataArray(array);
    return currentSize;
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 483, as _ZN24QSurfaceDataProxyPrivate7addRowsEO5QListIS0_I16QSurfaceDataItemEE
inline qsizetype QSurfaceDataProxyPrivate::addRows(QSurfaceDataArray &&rows)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    qsizetype currentSize = surfaceSeries->dataArray().size();
    QSurfaceDataArray array = surfaceSeries->dataArray();
    for (int i = 0; i < rows.size(); i++) {
        Q_ASSERT(surfaceSeries->dataArray().isEmpty()
                 || surfaceSeries->dataArray().at(0).size() == rows.at(i).size());
        array.append(rows.at(i));
    }
    surfaceSeries->setDataArray(array);
    return currentSize;
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 497, as _ZN24QSurfaceDataProxyPrivate9insertRowExO5QListI16QSurfaceDataItemE
inline void QSurfaceDataProxyPrivate::insertRow(qsizetype rowIndex, QSurfaceDataRow &&row)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex <= surfaceSeries->dataArray().size());
    Q_ASSERT(surfaceSeries->dataArray().isEmpty()
             || surfaceSeries->dataArray().at(0).size() == row.size());
    QSurfaceDataArray array = surfaceSeries->dataArray();
    array.insert(rowIndex, row);
    surfaceSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 508, as _ZN24QSurfaceDataProxyPrivate10insertRowsExO5QListIS0_I16QSurfaceDataItemEE
inline void QSurfaceDataProxyPrivate::insertRows(qsizetype rowIndex, QSurfaceDataArray &&rows)
{
    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    Q_ASSERT(rowIndex >= 0 && rowIndex <= surfaceSeries->dataArray().size());
    QSurfaceDataArray array = surfaceSeries->dataArray();

    for (int i = 0; i < rows.size(); i++) {
        Q_ASSERT(surfaceSeries->dataArray().isEmpty()
                 || surfaceSeries->dataArray().at(0).size() == rows.at(i).size());
        array.insert(rowIndex++, rows.at(i));
    }
    surfaceSeries->setDataArray(array);
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

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 536, as _ZNK24QSurfaceDataProxyPrivate11limitValuesER9QVector3DS1_P15QAbstract3DAxisS3_S3_
inline void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues,
                                           QVector3D &maxValues,
                                           QAbstract3DAxis *axisX,
                                           QAbstract3DAxis *axisY,
                                           QAbstract3DAxis *axisZ) const
{
    float min = 0.0f;
    float max = 0.0f;

    auto *surfaceSeries = static_cast<QSurface3DSeries *>(series());
    qsizetype rows = surfaceSeries->dataArray().size();
    qsizetype columns = 0;
    if (rows)
        columns = surfaceSeries->dataArray().at(0).size();

    if (rows && columns) {
        min = surfaceSeries->dataArray().at(0).at(0).y();
        max = surfaceSeries->dataArray().at(0).at(0).y();
    }

    for (int i = 0; i < rows; i++) {
        const QSurfaceDataRow &row = surfaceSeries->dataArray().at(i);
        if (!row.isEmpty()) {
            for (int j = 0; j < columns; j++) {
                float itemValue = surfaceSeries->dataArray().at(i).at(j).y();
                if (qIsNaN(itemValue) || qIsInf(itemValue))
                    continue;
                if ((min > itemValue || (qIsNaN(min) || qIsInf(min)))
                    && isValidValue(itemValue, axisY)) {
                    min = itemValue;
                }
                if (max < itemValue || (qIsNaN(max) || qIsInf(max)))
                    max = itemValue;
            }
        }
    }

    minValues.setY(min);
    maxValues.setY(max);

    if (columns) {
        // Have some defaults
        float xLow = surfaceSeries->dataArray().at(0).at(0).x();
        float xHigh = surfaceSeries->dataArray().at(0).last().x();
        float zLow = surfaceSeries->dataArray().at(0).at(0).z();
        float zHigh = surfaceSeries->dataArray().last().at(0).z();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                float zItemValue = surfaceSeries->dataArray().at(i).at(j).z();
                if (qIsNaN(zItemValue) || qIsInf(zItemValue))
                    continue;
                else if (isValidValue(zItemValue, axisZ))
                    zLow = qMin(zLow, zItemValue);
            }
            if (!qIsNaN(zLow) && !qIsInf(zLow))
                break;
        }
        for (qsizetype i = rows - 1; i >= 0; i--) {
            for (qsizetype j = 0; j < columns; j++) {
                float zItemValue = surfaceSeries->dataArray().at(i).at(j).z();
                if (qIsNaN(zItemValue) || qIsInf(zItemValue))
                    continue;
                else if (isValidValue(zItemValue, axisZ)) {
                    if (!qIsNaN(zHigh) && !qIsInf(zHigh))
                        zHigh = qMax(zHigh, zItemValue);
                    else
                        zHigh = zItemValue;
                }
            }
            if (!qIsNaN(zHigh) && !qIsInf(zHigh))
                break;
        }
        for (qsizetype j = 0; j < columns; j++) {
            for (qsizetype i = 0; i < rows; i++) {
                float xItemValue = surfaceSeries->dataArray().at(i).at(j).x();
                if (qIsNaN(xItemValue) || qIsInf(xItemValue))
                    continue;
                else if (isValidValue(xItemValue, axisX))
                    xLow = qMin(xLow, xItemValue);
            }
            if (!qIsNaN(xLow) && !qIsInf(xLow))
                break;
        }
        for (qsizetype j = columns - 1; j >= 0; j--) {
            for (qsizetype i = 0; i < rows; i++) {
                float xItemValue = surfaceSeries->dataArray().at(i).at(j).x();
                if (qIsNaN(xItemValue) || qIsInf(xItemValue)) {
                    continue;
                } else if (isValidValue(xItemValue, axisX)) {
                    if (!qIsNaN(xHigh) && !qIsInf(xHigh))
                        xHigh = qMax(xHigh, xItemValue);
                    else
                        xHigh = xItemValue;
                }
            }
            if (!qIsNaN(xHigh) && !qIsInf(xHigh))
                break;
        }
        minValues.setX(xLow);
        minValues.setZ(zLow);
        maxValues.setX(xHigh);
        maxValues.setZ(zHigh);
    } else {
        minValues.setX(axisX->d_func()->allowZero() ? 0.0f : 1.0f);
        minValues.setZ(axisZ->d_func()->allowZero() ? 0.0f : 1.0f);
        maxValues.setX(axisX->d_func()->allowZero() ? 0.0f : 1.0f);
        maxValues.setZ(axisZ->d_func()->allowZero() ? 0.0f : 1.0f);
    }
}

//  from ../qtgraphs/src/graphs3d/data/qsurfacedataproxy.cpp, line 646, as _ZNK24QSurfaceDataProxyPrivate12isValidValueEfP15QAbstract3DAxis
inline bool QSurfaceDataProxyPrivate::isValidValue(float value, QAbstract3DAxis *axis) const
{
    return (value > 0.0f || (value == 0.0f && axis->d_func()->allowZero())
            || (value < 0.0f && axis->d_func()->allowNegatives()));
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

//  QSurfaceDataProxyPrivate::QSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
QSurfaceDataProxyPrivate *ritual_ZN24QSurfaceDataProxyPrivateC1Ev() {
  return new CuteQSurfaceDataProxyPrivate();
}

//  QSurfaceDataProxyPrivate::~QSurfaceDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivateD1Ev(
    QSurfaceDataProxyPrivate *self) {
  delete self;
}

//  void QSurfaceDataProxyPrivate::resetArray(QSurfaceDataArray &&newArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10resetArrayEO5QListIS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    QSurfaceDataArray *newArray) {
  self->resetArray(std::move(*newArray));
}

//  void QSurfaceDataProxyPrivate::setRow(qsizetype rowIndex, QSurfaceDataRow
//      &&row)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate6setRowExO5QListI16QSurfaceDataItemE(
    QSurfaceDataProxyPrivate *self,
    qsizetype rowIndex,
    QSurfaceDataRow *row) {
  self->setRow(rowIndex, std::move(*row));
}

//  void QSurfaceDataProxyPrivate::setRows(qsizetype rowIndex,
//      QSurfaceDataArray &&rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate7setRowsExO5QListIS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    qsizetype rowIndex,
    QSurfaceDataArray *rows) {
  self->setRows(rowIndex, std::move(*rows));
}

//  void QSurfaceDataProxyPrivate::setItem(qsizetype rowIndex, qsizetype
//      columnIndex, QSurfaceDataItem &&item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate7setItemExxO16QSurfaceDataItem(
    QSurfaceDataProxyPrivate *self,
    qsizetype rowIndex,
    qsizetype columnIndex,
    QSurfaceDataItem *item) {
  self->setItem(rowIndex, columnIndex, std::move(*item));
}

//  qsizetype QSurfaceDataProxyPrivate::addRow(QSurfaceDataRow &&row)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QSurfaceDataProxyPrivate6addRowEO5QListI16QSurfaceDataItemE(
    QSurfaceDataProxyPrivate *self,
    QSurfaceDataRow *row) {
  return self->addRow(std::move(*row));
}

//  qsizetype QSurfaceDataProxyPrivate::addRows(QSurfaceDataArray &&rows)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QSurfaceDataProxyPrivate7addRowsEO5QListIS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    QSurfaceDataArray *rows) {
  return self->addRows(std::move(*rows));
}

//  void QSurfaceDataProxyPrivate::insertRow(qsizetype rowIndex,
//      QSurfaceDataRow &&row)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate9insertRowExO5QListI16QSurfaceDataItemE(
    QSurfaceDataProxyPrivate *self,
    qsizetype rowIndex,
    QSurfaceDataRow *row) {
  self->insertRow(rowIndex, std::move(*row));
}

//  void QSurfaceDataProxyPrivate::insertRows(qsizetype rowIndex,
//      QSurfaceDataArray &&rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSurfaceDataProxyPrivate10insertRowsExO5QListIS0_I16QSurfaceDataItemEE(
    QSurfaceDataProxyPrivate *self,
    qsizetype rowIndex,
    QSurfaceDataArray *rows) {
  self->insertRows(rowIndex, std::move(*rows));
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

//  void QSurfaceDataProxyPrivate::limitValues(QVector3D &minValues,
//      QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
//      QAbstract3DAxis *axisZ) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QSurfaceDataProxyPrivate11limitValuesER9QVector3DS1_P15QAbstract3DAxisS3_S3_(
    const QSurfaceDataProxyPrivate *self,
    QVector3D *minValues,
    QVector3D *maxValues,
    QAbstract3DAxis *axisX,
    QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) {
  self->limitValues(*minValues, *maxValues, axisX, axisY, axisZ);
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

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
