//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/qcustomseriesdata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/qcustomseriesdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QDataStream>
#include <QtGraphs/private/qcustomseriesdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/customchart/qcustomseriesdata.cpp, line 15, as _ZNK17QCustomSeriesData4dataEv
inline QVariantMap QCustomSeriesData::data() const
{
    return m_data;
}

//  from ../qtgraphs/src/graphs2d/customchart/qcustomseriesdata.cpp, line 20, as _ZN17QCustomSeriesData7setDataERK4QMapI7QString8QVariantE
inline void QCustomSeriesData::setData(const QVariantMap &newData)
{
    m_data = newData;
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QCustomSeriesData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QCustomSeriesData10metaObjectEv(
    const QCustomSeriesData *self) {
  return self->metaObject();
}

//  QVariantMap QCustomSeriesData::data() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK17QCustomSeriesData4dataEv(
    const QCustomSeriesData *self) {
  return new QMap<QString, QVariant>(self->data());
}

//  void QCustomSeriesData::setData(const QVariantMap &newData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCustomSeriesData7setDataERK4QMapI7QString8QVariantE(
    QCustomSeriesData *self,
    const QMap<QString, QVariant> *newData) {
  self->setData(*newData);
}

//  QList<QCustomSeriesData *>::QList()
extern "C" Q_DECL_EXPORT
QList<QCustomSeriesData *> *ritual_list_make_QCustomSeriesData_ptr() {
  return new QList<QCustomSeriesData *>();
}

//  void QList<QCustomSeriesData *>::append(const QCustomSeriesData * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCustomSeriesData_ptr(
    QList<QCustomSeriesData *> *self,
    QCustomSeriesData *element) {
  self->append(element);
}

//  qsizetype QList<QCustomSeriesData *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCustomSeriesData_ptr(
    const QList<QCustomSeriesData *> *self) {
  return self->size();
}

//  const QCustomSeriesData * &QList<QCustomSeriesData *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QCustomSeriesData *ritual_list_at_QCustomSeriesData_ptr(
    const QList<QCustomSeriesData *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QCustomSeriesData *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCustomSeriesData_ptr(
    QList<QCustomSeriesData *> *self) {
  delete self;
}

#endif  // (!(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))) && (QT_CONFIG(graphs_2d_custom))
