//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsggeometry.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsggeometry.h>

//  void QSGGeometry::ColoredPoint2D::set(float nx, float ny, uchar nr, uchar
//      ng, uchar nb, uchar na)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry14ColoredPoint2D3setEffhhhh(
    QSGGeometry::ColoredPoint2D *self,
    float nx,
    float ny,
    uchar nr,
    uchar ng,
    uchar nb,
    uchar na) {
  self->set(nx, ny, nr, ng, nb, na);
}

//  QSGGeometry::ColoredPoint2D::~ColoredPoint2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry14ColoredPoint2DD1Ev(
    QSGGeometry::ColoredPoint2D *self) {
  delete self;
}
