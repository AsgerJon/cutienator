//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qabstractseries.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qabstractseries.h>
#include <QtCore/qlist.h>

//  QLegendData::~QLegendData()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLegendDataD1Ev(QLegendData *self) {
  delete self;
}

//  QList<QLegendData>::QList()
extern "C" Q_DECL_EXPORT
QList<QLegendData> *ritual_list_make_QLegendData() {
  return new QList<QLegendData>();
}

//  void QList<QLegendData>::append(const QLegendData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLegendData(
    QList<QLegendData> *self,
    const QLegendData *element) {
  self->append(*element);
}

//  qsizetype QList<QLegendData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLegendData(const QList<QLegendData> *self) {
  return self->size();
}

//  const QLegendData &QList<QLegendData>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLegendData *ritual_list_at_QLegendData(
    const QList<QLegendData> *self,
    long long index) {
  return new QLegendData(self->at(index));
}

//  QList<QLegendData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLegendData(QList<QLegendData> *self) {
  delete self;
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
