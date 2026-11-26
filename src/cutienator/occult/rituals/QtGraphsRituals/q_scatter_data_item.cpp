//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/qscatterdataitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtGraphs/qgraphsglobal.h>
#if (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
#include <QtGraphs/QtGraphs>
#include <QtGraphs/qscatterdataitem.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qlist.h>

//  QScatterDataItem::QScatterDataItem()
extern "C" Q_DECL_EXPORT
QScatterDataItem *ritual_ZN16QScatterDataItemC1Ev() {
  return new QScatterDataItem();
}

//  QScatterDataItem::QScatterDataItem(QVector3D position)
extern "C" Q_DECL_EXPORT
QScatterDataItem *ritual_ZN16QScatterDataItemC1E9QVector3D(
    const QVector3D *position) {
  return new QScatterDataItem(*position);
}

//  QScatterDataItem::QScatterDataItem(float x, float y, float z)
extern "C" Q_DECL_EXPORT
QScatterDataItem *ritual_ZN16QScatterDataItemC1Efff(
    float x,
    float y,
    float z) {
  return new QScatterDataItem(x, y, z);
}

//  QScatterDataItem::QScatterDataItem(QVector3D position, const QQuaternion
//      &rotation)
extern "C" Q_DECL_EXPORT
QScatterDataItem *ritual_ZN16QScatterDataItemC1E9QVector3DRK11QQuaternion(
    const QVector3D *position,
    const QQuaternion *rotation) {
  return new QScatterDataItem(*position, *rotation);
}

//  void QScatterDataItem::setPosition(QVector3D pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatterDataItem11setPositionE9QVector3D(
    QScatterDataItem *self,
    const QVector3D *pos) {
  self->setPosition(*pos);
}

//  QVector3D QScatterDataItem::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QScatterDataItem8positionEv(
    const QScatterDataItem *self) {
  return new QVector3D(self->position());
}

//  void QScatterDataItem::setRotation(const QQuaternion &rot)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatterDataItem11setRotationERK11QQuaternion(
    QScatterDataItem *self,
    const QQuaternion *rot) {
  self->setRotation(*rot);
}

//  QQuaternion QScatterDataItem::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK16QScatterDataItem8rotationEv(
    const QScatterDataItem *self) {
  return new QQuaternion(self->rotation());
}

//  void QScatterDataItem::setX(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatterDataItem4setXEf(
    QScatterDataItem *self,
    float value) {
  self->setX(value);
}

//  void QScatterDataItem::setY(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatterDataItem4setYEf(
    QScatterDataItem *self,
    float value) {
  self->setY(value);
}

//  void QScatterDataItem::setZ(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatterDataItem4setZEf(
    QScatterDataItem *self,
    float value) {
  self->setZ(value);
}

//  float QScatterDataItem::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QScatterDataItem1xEv(const QScatterDataItem *self) {
  return self->x();
}

//  float QScatterDataItem::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QScatterDataItem1yEv(const QScatterDataItem *self) {
  return self->y();
}

//  float QScatterDataItem::z() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK16QScatterDataItem1zEv(const QScatterDataItem *self) {
  return self->z();
}

//  QScatterDataItem::~QScatterDataItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QScatterDataItemD1Ev(QScatterDataItem *self) {
  delete self;
}

//  QList<QScatterDataItem>::QList()
extern "C" Q_DECL_EXPORT
QList<QScatterDataItem> *ritual_list_make_QScatterDataItem() {
  return new QList<QScatterDataItem>();
}

//  void QList<QScatterDataItem>::append(const QScatterDataItem &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QScatterDataItem(
    QList<QScatterDataItem> *self,
    const QScatterDataItem *element) {
  self->append(*element);
}

//  qsizetype QList<QScatterDataItem>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QScatterDataItem(
    const QList<QScatterDataItem> *self) {
  return self->size();
}

//  const QScatterDataItem &QList<QScatterDataItem>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QScatterDataItem *ritual_list_at_QScatterDataItem(
    const QList<QScatterDataItem> *self,
    long long index) {
  return new QScatterDataItem(self->at(index));
}

//  QList<QScatterDataItem>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QScatterDataItem(QList<QScatterDataItem> *self) {
  delete self;
}

#endif  // (QT_CONFIG(graphs_3d)) && (!(!QT_CONFIG(graphs_3d_bars3d) && !QT_CONFIG(graphs_3d_scatter3d) && !QT_CONFIG(graphs_3d_surface3d))) && (QT_CONFIG(graphs_3d_scatter3d))
