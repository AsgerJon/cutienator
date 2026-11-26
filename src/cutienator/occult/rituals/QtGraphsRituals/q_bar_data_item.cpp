//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qbardataitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qbardataitem.h>
#include <QtCore/qlist.h>

//  QBarDataItem::QBarDataItem()
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1Ev() {
  return new QBarDataItem();
}

//  QBarDataItem::QBarDataItem(float value)
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1Ef(float value) {
  return new QBarDataItem(value);
}

//  QBarDataItem::QBarDataItem(float value, float angle)
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_ZN12QBarDataItemC1Eff(float value, float angle) {
  return new QBarDataItem(value, angle);
}

//  void QBarDataItem::setValue(float val)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItem8setValueEf(QBarDataItem *self, float val) {
  self->setValue(val);
}

//  float QBarDataItem::value() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QBarDataItem5valueEv(const QBarDataItem *self) {
  return self->value();
}

//  void QBarDataItem::setRotation(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItem11setRotationEf(
    QBarDataItem *self,
    float angle) {
  self->setRotation(angle);
}

//  float QBarDataItem::rotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QBarDataItem8rotationEv(const QBarDataItem *self) {
  return self->rotation();
}

//  QBarDataItem::~QBarDataItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QBarDataItemD1Ev(QBarDataItem *self) {
  delete self;
}

//  QList<QBarDataItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QBarDataItem> *ritual_list_make_QBarDataItem() {
  return new QList<QBarDataItem>();
}

//  void QList<QBarDataItem>::append(const QBarDataItem &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBarDataItem(
    QList<QBarDataItem> *self,
    const QBarDataItem *element) {
  self->append(*element);
}

//  qsizetype QList<QBarDataItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBarDataItem(const QList<QBarDataItem> *self) {
  return self->size();
}

//  const QBarDataItem &QList<QBarDataItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QBarDataItem *ritual_list_at_QBarDataItem(
    const QList<QBarDataItem> *self,
    long long index) {
  return new QBarDataItem(self->at(index));
}

//  QList<QBarDataItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBarDataItem(QList<QBarDataItem> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_bars3d))
