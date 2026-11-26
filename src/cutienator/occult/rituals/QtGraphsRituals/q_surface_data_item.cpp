//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qsurfacedataitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qsurfacedataitem.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qlist.h>

//  QSurfaceDataItem::QSurfaceDataItem()
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemC1Ev() {
  return new QSurfaceDataItem();
}

//  QSurfaceDataItem::QSurfaceDataItem(QVector3D position)
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemC1E9QVector3D(
    const QVector3D *position) {
  return new QSurfaceDataItem(*position);
}

//  QSurfaceDataItem::QSurfaceDataItem(float x, float y, float z)
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemC1Efff(
    float x,
    float y,
    float z) {
  return new QSurfaceDataItem(x, y, z);
}

//  void QSurfaceDataItem::setPosition(QVector3D pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItem11setPositionE9QVector3D(
    QSurfaceDataItem *self,
    const QVector3D *pos) {
  self->setPosition(*pos);
}

//  QVector3D QSurfaceDataItem::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QSurfaceDataItem8positionEv(
    const QSurfaceDataItem *self) {
  return new QVector3D(self->position());
}

//  void QSurfaceDataItem::setX(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItem4setXEf(
    QSurfaceDataItem *self,
    float value) {
  self->setX(value);
}

//  void QSurfaceDataItem::setY(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItem4setYEf(
    QSurfaceDataItem *self,
    float value) {
  self->setY(value);
}

//  void QSurfaceDataItem::setZ(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItem4setZEf(
    QSurfaceDataItem *self,
    float value) {
  self->setZ(value);
}

//  float QSurfaceDataItem::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSurfaceDataItem1xEv(const QSurfaceDataItem *self) {
  return self->x();
}

//  float QSurfaceDataItem::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSurfaceDataItem1yEv(const QSurfaceDataItem *self) {
  return self->y();
}

//  float QSurfaceDataItem::z() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QSurfaceDataItem1zEv(const QSurfaceDataItem *self) {
  return self->z();
}

//  QSurfaceDataItem::~QSurfaceDataItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItemD1Ev(QSurfaceDataItem *self) {
  delete self;
}

//  QList<QSurfaceDataItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QSurfaceDataItem> *ritual_list_make_QSurfaceDataItem() {
  return new QList<QSurfaceDataItem>();
}

//  void QList<QSurfaceDataItem>::append(const QSurfaceDataItem &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QSurfaceDataItem(
    QList<QSurfaceDataItem> *self,
    const QSurfaceDataItem *element) {
  self->append(*element);
}

//  qsizetype QList<QSurfaceDataItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QSurfaceDataItem(
    const QList<QSurfaceDataItem> *self) {
  return self->size();
}

//  const QSurfaceDataItem &QList<QSurfaceDataItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_list_at_QSurfaceDataItem(
    const QList<QSurfaceDataItem> *self,
    long long index) {
  return new QSurfaceDataItem(self->at(index));
}

//  QList<QSurfaceDataItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QSurfaceDataItem(QList<QSurfaceDataItem> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_surface3d))
