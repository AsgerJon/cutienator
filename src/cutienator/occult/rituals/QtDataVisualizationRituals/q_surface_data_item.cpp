//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qsurfacedataitem.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qsurfacedataitem.h>
#include <QtGui/qvectornd.h>

//  QSurfaceDataItem::QSurfaceDataItem()
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemC1Ev() {
  return new QSurfaceDataItem();
}

//  QSurfaceDataItem::QSurfaceDataItem(const QVector3D &position)
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemC1ERK9QVector3D(
    const QVector3D *position) {
  return new QSurfaceDataItem(*position);
}

//  QSurfaceDataItem::QSurfaceDataItem(const QSurfaceDataItem &other)
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemC1ERKS_(
    const QSurfaceDataItem *other) {
  return new QSurfaceDataItem(*other);
}

//  QSurfaceDataItem::~QSurfaceDataItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItemD1Ev(QSurfaceDataItem *self) {
  delete self;
}

//  QSurfaceDataItem &QSurfaceDataItem::operator=(const QSurfaceDataItem
//      &other)
extern "C" Q_DECL_EXPORT
QSurfaceDataItem *ritual_ZN16QSurfaceDataItemaSERKS_(
    QSurfaceDataItem *self,
    const QSurfaceDataItem *other) {
  return &(self->operator=(*other));
}

//  void QSurfaceDataItem::setPosition(const QVector3D &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItem11setPositionERK9QVector3D(
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

//  void QSurfaceDataItem::createExtraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSurfaceDataItem15createExtraDataEv(QSurfaceDataItem *self) {
  self->createExtraData();
}
