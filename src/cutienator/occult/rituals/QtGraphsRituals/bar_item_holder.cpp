//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/barinstancing_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/barinstancing_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  BarItemHolder::~BarItemHolder()
extern "C" Q_DECL_EXPORT
void ritual_ZN13BarItemHolderD1Ev(BarItemHolder *self) {
  delete self;
}

//  QList<BarItemHolder *>::QList()
extern "C" Q_DECL_EXPORT
QList<BarItemHolder *> *ritual_list_make_BarItemHolder_ptr() {
  return new QList<BarItemHolder *>();
}

//  void QList<BarItemHolder *>::append(const BarItemHolder * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_BarItemHolder_ptr(
    QList<BarItemHolder *> *self,
    BarItemHolder *element) {
  self->append(element);
}

//  qsizetype QList<BarItemHolder *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_BarItemHolder_ptr(
    const QList<BarItemHolder *> *self) {
  return self->size();
}

//  const BarItemHolder * &QList<BarItemHolder *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
BarItemHolder *ritual_list_at_BarItemHolder_ptr(
    const QList<BarItemHolder *> *self,
    long long index) {
  return self->at(index);
}

//  QList<BarItemHolder *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_BarItemHolder_ptr(QList<BarItemHolder *> *self) {
  delete self;
}

#endif  // (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
