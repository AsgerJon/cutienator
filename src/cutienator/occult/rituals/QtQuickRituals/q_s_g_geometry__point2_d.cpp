//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsggeometry.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsggeometry.h>

//  void QSGGeometry::Point2D::set(float nx, float ny)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry7Point2D3setEff(
    QSGGeometry::Point2D *self,
    float nx,
    float ny) {
  self->set(nx, ny);
}

//  QSGGeometry::Point2D::~Point2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry7Point2DD1Ev(QSGGeometry::Point2D *self) {
  delete self;
}
