//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qscatterdataproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatterdataproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qscatterdataproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/qabstract3daxis_p.h>
#include <QtGraphs/private/qscatter3dseries_p.h>
#include <QtGraphs/private/qscatterdataproxy_p.h>
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

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 488, as _ZN24QScatterDataProxyPrivate9setSeriesEP17QAbstract3DSeries
inline void QScatterDataProxyPrivate::setSeries(QAbstract3DSeries *series)
{
    Q_Q(QScatterDataProxy);
    QAbstractDataProxyPrivate::setSeries(series);
    QScatter3DSeries *scatterSeries = static_cast<QScatter3DSeries *>(series);
    emit q->seriesChanged(scatterSeries);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 333, as _ZN24QScatterDataProxyPrivateD2Ev
inline QScatterDataProxyPrivate::~QScatterDataProxyPrivate() {}

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

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 329, as _ZN24QScatterDataProxyPrivateC1Ev
inline QScatterDataProxyPrivate::QScatterDataProxyPrivate()
    : QAbstractDataProxyPrivate(QAbstractDataProxy::DataType::Scatter)
{}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 335, as _ZN24QScatterDataProxyPrivate10resetArrayEO5QListI16QScatterDataItemE
inline void QScatterDataProxyPrivate::resetArray(QScatterDataArray &&newArray)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    if (!newArray.isSharedWith(scatterSeries->dataArray()))
        scatterSeries->setDataArray(newArray);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 342, as _ZN24QScatterDataProxyPrivate15resetScaleArrayEO5QListI9QVector3DE
inline void QScatterDataProxyPrivate::resetScaleArray(QList<QVector3D> &&newArray)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    if (!newArray.isSharedWith(scatterSeries->scaleArray()))
        scatterSeries->setScaleArray(newArray);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 349, as _ZN24QScatterDataProxyPrivate7setItemExO16QScatterDataItem
inline void QScatterDataProxyPrivate::setItem(qsizetype index, QScatterDataItem &&item)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    Q_ASSERT(index >= 0 && index < scatterSeries->dataArray().size());
    QScatterDataArray array = scatterSeries->dataArray();
    array[index] = item;
    scatterSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 358, as _ZN24QScatterDataProxyPrivate8setItemsExO5QListI16QScatterDataItemE
inline void QScatterDataProxyPrivate::setItems(qsizetype index, QScatterDataArray &&items)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    Q_ASSERT(index >= 0 && (index + items.size()) <= scatterSeries->dataArray().size());
    QScatterDataArray array = scatterSeries->dataArray();
    for (int i = 0; i < items.size(); i++)
        array[index++] = items[i];
    scatterSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 368, as _ZN24QScatterDataProxyPrivate7addItemEO16QScatterDataItem
inline qsizetype QScatterDataProxyPrivate::addItem(QScatterDataItem &&item)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    qsizetype currentSize = scatterSeries->dataArray().size();
    QScatterDataArray array = scatterSeries->dataArray();
    array.append(item);
    scatterSeries->setDataArray(array);
    return currentSize;
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 378, as _ZN24QScatterDataProxyPrivate8addItemsEO5QListI16QScatterDataItemE
inline qsizetype QScatterDataProxyPrivate::addItems(QScatterDataArray &&items)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    qsizetype currentSize = 0;
    if (scatterSeries) {
        currentSize = scatterSeries->dataArray().size();
        QScatterDataArray array = scatterSeries->dataArray();
        array += items;
        scatterSeries->setDataArray(array);
    }
    return currentSize;
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 391, as _ZN24QScatterDataProxyPrivate10insertItemExO16QScatterDataItem
inline void QScatterDataProxyPrivate::insertItem(qsizetype index, QScatterDataItem &&item)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    Q_ASSERT(index >= 0 && index <= scatterSeries->dataArray().size());
    QScatterDataArray array = scatterSeries->dataArray();
    array.insert(index, item);
    scatterSeries->setDataArray(array);
}

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 400, as _ZN24QScatterDataProxyPrivate11insertItemsExO5QListI16QScatterDataItemE
inline void QScatterDataProxyPrivate::insertItems(qsizetype index, QScatterDataArray &&items)
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    Q_ASSERT(index >= 0 && index <= scatterSeries->dataArray().size());
    QScatterDataArray array = scatterSeries->dataArray();
    for (int i = 0; i < items.size(); i++)
        array.insert(index++, items.at(i));
    scatterSeries->setDataArray(array);
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

//  from ../qtgraphs/src/graphs3d/data/qscatterdataproxy.cpp, line 421, as _ZNK24QScatterDataProxyPrivate11limitValuesER9QVector3DS1_P15QAbstract3DAxisS3_S3_
inline void QScatterDataProxyPrivate::limitValues(QVector3D &minValues,
                                           QVector3D &maxValues,
                                           QAbstract3DAxis *axisX,
                                           QAbstract3DAxis *axisY,
                                           QAbstract3DAxis *axisZ) const
{
    auto *scatterSeries = static_cast<QScatter3DSeries *>(series());
    if (scatterSeries->dataArray().isEmpty())
        return;

    QVector3D firstPos = scatterSeries->dataArray().at(0).position();

    float minX = firstPos.x();
    float maxX = minX;
    float minY = firstPos.y();
    float maxY = minY;
    float minZ = firstPos.z();
    float maxZ = minZ;

    if (scatterSeries->dataArray().size() > 1) {
        for (int i = 1; i < scatterSeries->dataArray().size(); i++) {
            QVector3D pos = scatterSeries->dataArray().at(i).position();

            float value = pos.x();
            if (qIsNaN(value) || qIsInf(value))
                continue;
            if (isValidValue(minX, value, axisX))
                minX = value;
            if (maxX < value)
                maxX = value;

            value = pos.y();
            if (qIsNaN(value) || qIsInf(value))
                continue;
            if (isValidValue(minY, value, axisY))
                minY = value;
            if (maxY < value)
                maxY = value;

            value = pos.z();
            if (qIsNaN(value) || qIsInf(value))
                continue;
            if (isValidValue(minZ, value, axisZ))
                minZ = value;
            if (maxZ < value)
                maxZ = value;
        }
    }

    minValues.setX(minX);
    minValues.setY(minY);
    minValues.setZ(minZ);

    maxValues.setX(maxX);
    maxValues.setY(maxY);
    maxValues.setZ(maxZ);
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

//  QScatterDataProxyPrivate::QScatterDataProxyPrivate()
extern "C" Q_DECL_EXPORT
QScatterDataProxyPrivate *ritual_ZN24QScatterDataProxyPrivateC1Ev() {
  return new CuteQScatterDataProxyPrivate();
}

//  QScatterDataProxyPrivate::~QScatterDataProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivateD1Ev(
    QScatterDataProxyPrivate *self) {
  delete self;
}

//  void QScatterDataProxyPrivate::resetArray(QScatterDataArray &&newArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate10resetArrayEO5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    QScatterDataArray *newArray) {
  self->resetArray(std::move(*newArray));
}

//  void QScatterDataProxyPrivate::resetScaleArray(QList<QVector3D>
//      &&newArray)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate15resetScaleArrayEO5QListI9QVector3DE(
    QScatterDataProxyPrivate *self,
    QList<QVector3D> *newArray) {
  self->resetScaleArray(std::move(*newArray));
}

//  void QScatterDataProxyPrivate::setItem(qsizetype index, QScatterDataItem
//      &&item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate7setItemExO16QScatterDataItem(
    QScatterDataProxyPrivate *self,
    qsizetype index,
    QScatterDataItem *item) {
  self->setItem(index, std::move(*item));
}

//  void QScatterDataProxyPrivate::setItems(qsizetype index,
//      QScatterDataArray &&items)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate8setItemsExO5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    qsizetype index,
    QScatterDataArray *items) {
  self->setItems(index, std::move(*items));
}

//  qsizetype QScatterDataProxyPrivate::addItem(QScatterDataItem &&item)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QScatterDataProxyPrivate7addItemEO16QScatterDataItem(
    QScatterDataProxyPrivate *self,
    QScatterDataItem *item) {
  return self->addItem(std::move(*item));
}

//  qsizetype QScatterDataProxyPrivate::addItems(QScatterDataArray &&items)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN24QScatterDataProxyPrivate8addItemsEO5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    QScatterDataArray *items) {
  return self->addItems(std::move(*items));
}

//  void QScatterDataProxyPrivate::insertItem(qsizetype index,
//      QScatterDataItem &&item)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate10insertItemExO16QScatterDataItem(
    QScatterDataProxyPrivate *self,
    qsizetype index,
    QScatterDataItem *item) {
  self->insertItem(index, std::move(*item));
}

//  void QScatterDataProxyPrivate::insertItems(qsizetype index,
//      QScatterDataArray &&items)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QScatterDataProxyPrivate11insertItemsExO5QListI16QScatterDataItemE(
    QScatterDataProxyPrivate *self,
    qsizetype index,
    QScatterDataArray *items) {
  self->insertItems(index, std::move(*items));
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

//  void QScatterDataProxyPrivate::limitValues(QVector3D &minValues,
//      QVector3D &maxValues, QAbstract3DAxis *axisX, QAbstract3DAxis *axisY,
//      QAbstract3DAxis *axisZ) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QScatterDataProxyPrivate11limitValuesER9QVector3DS1_P15QAbstract3DAxisS3_S3_(
    const QScatterDataProxyPrivate *self,
    QVector3D *minValues,
    QVector3D *maxValues,
    QAbstract3DAxis *axisX,
    QAbstract3DAxis *axisY,
    QAbstract3DAxis *axisZ) {
  self->limitValues(*minValues, *maxValues, axisX, axisY, axisZ);
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

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
