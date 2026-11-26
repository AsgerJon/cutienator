//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtCore/QPair>
#include <QtCore/QList>
#include <QtCore/QSet>

//  void QGeoCameraTilesPrivate::updateMetadata()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraTilesPrivate14updateMetadataEv(
    QGeoCameraTilesPrivate *self) {
  self->updateMetadata();
}

//  void QGeoCameraTilesPrivate::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraTilesPrivate14updateGeometryEv(
    QGeoCameraTilesPrivate *self) {
  self->updateGeometry();
}

//  Frustum QGeoCameraTilesPrivate::createFrustum(double viewExpansion) const
extern "C" Q_DECL_EXPORT
Frustum *ritual_ZNK22QGeoCameraTilesPrivate13createFrustumEd(
    const QGeoCameraTilesPrivate *self,
    double viewExpansion) {
  return new Frustum(self->createFrustum(viewExpansion));
}

//  PolygonVector QGeoCameraTilesPrivate::frustumFootprint(const Frustum
//      &frustum) const
extern "C" Q_DECL_EXPORT
QList<QDoubleVector3D> *ritual_ZNK22QGeoCameraTilesPrivate16frustumFootprintERK7Frustum(
    const QGeoCameraTilesPrivate *self,
    const Frustum *frustum) {
  return new QList<QDoubleVector3D>(self->frustumFootprint(*frustum));
}

//  QPair<PolygonVector, PolygonVector>
//      QGeoCameraTilesPrivate::splitPolygonAtAxisValue(const PolygonVector
//      &polygon, int axis, double value) const
extern "C" Q_DECL_EXPORT
QPair<PolygonVector, PolygonVector> *ritual_ZNK22QGeoCameraTilesPrivate23splitPolygonAtAxisValueERK5QListI15QDoubleVector3DEid(
    const QGeoCameraTilesPrivate *self,
    const QList<QDoubleVector3D> *polygon,
    int axis,
    double value) {
  return new QPair<PolygonVector, PolygonVector>(
      self->splitPolygonAtAxisValue(
          *polygon,
          axis,
          value));
}

//  ClippedFootprint QGeoCameraTilesPrivate::clipFootprintToMap(const
//      PolygonVector &footprint) const
extern "C" Q_DECL_EXPORT
QGeoCameraTilesPrivate::ClippedFootprint *ritual_ZNK22QGeoCameraTilesPrivate18clipFootprintToMapERK5QListI15QDoubleVector3DE(
    const QGeoCameraTilesPrivate *self,
    const QList<QDoubleVector3D> *footprint) {
  return new QGeoCameraTilesPrivate::ClippedFootprint(
      self->clipFootprintToMap(
          *footprint));
}

//  QList<QPair<double, int>>
//      QGeoCameraTilesPrivate::tileIntersections(double p1, int t1, double
//      p2, int t2) const
extern "C" Q_DECL_EXPORT
QList<QPair<double, int>> *ritual_ZNK22QGeoCameraTilesPrivate17tileIntersectionsEdidi(
    const QGeoCameraTilesPrivate *self,
    double p1,
    int t1,
    double p2,
    int t2) {
  return new QList<QPair<double, int>>(
      self->tileIntersections(
          p1,
          t1,
          p2,
          t2));
}

//  QSet<QGeoTileSpec> QGeoCameraTilesPrivate::tilesFromPolygon(const
//      PolygonVector &polygon) const
extern "C" Q_DECL_EXPORT
QSet<QGeoTileSpec> *ritual_ZNK22QGeoCameraTilesPrivate16tilesFromPolygonERK5QListI15QDoubleVector3DE(
    const QGeoCameraTilesPrivate *self,
    const QList<QDoubleVector3D> *polygon) {
  return new QSet<QGeoTileSpec>(self->tilesFromPolygon(*polygon));
}

//  QGeoCameraTilesPrivate *QGeoCameraTilesPrivate::get(QGeoCameraTiles *o)
extern "C" Q_DECL_EXPORT
QGeoCameraTilesPrivate *ritual_ZN22QGeoCameraTilesPrivate3getEP15QGeoCameraTiles(
    QGeoCameraTiles *o) {
  return QGeoCameraTilesPrivate::get(o);
}

//  QGeoCameraTilesPrivate::~QGeoCameraTilesPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraTilesPrivateD1Ev(QGeoCameraTilesPrivate *self) {
  delete self;
}

//  a QPair<PolygonVector, PolygonVector> a ritual of QGeoCameraTilesPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoCameraTilesPrivate__QPair_PolygonVector_PolygonVector(
    QPair<PolygonVector, PolygonVector> *self) {
  delete self;
}

//  a QList<QPair<double, int>> a ritual of QGeoCameraTilesPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoCameraTilesPrivate__QList_QPair_double_int(
    QList<QPair<double, int>> *self) {
  delete self;
}

//  a QSet<QGeoTileSpec> a ritual of QGeoCameraTilesPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QGeoCameraTilesPrivate__QSet_QGeoTileSpec(
    QSet<QGeoTileSpec> *self) {
  delete self;
}
