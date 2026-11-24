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
