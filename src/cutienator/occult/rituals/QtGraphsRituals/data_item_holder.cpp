//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/scatterinstancing_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/scatterinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  DataItemHolder::~DataItemHolder()
extern "C" Q_DECL_EXPORT
void ritual_ZN14DataItemHolderD1Ev(DataItemHolder *self) {
  delete self;
}

//  QList<DataItemHolder>::QList()
extern "C" Q_DECL_EXPORT
QList<DataItemHolder> *ritual_list_make_DataItemHolder() {
  return new QList<DataItemHolder>();
}

//  void QList<DataItemHolder>::append(const DataItemHolder &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_DataItemHolder(
    QList<DataItemHolder> *self,
    const DataItemHolder *element) {
  self->append(*element);
}

//  qsizetype QList<DataItemHolder>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_DataItemHolder(
    const QList<DataItemHolder> *self) {
  return self->size();
}

//  const DataItemHolder &QList<DataItemHolder>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
DataItemHolder *ritual_list_at_DataItemHolder(
    const QList<DataItemHolder> *self,
    long long index) {
  return new DataItemHolder(self->at(index));
}

//  QList<DataItemHolder>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_DataItemHolder(QList<DataItemHolder> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
