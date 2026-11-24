//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsggeometry.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsggeometry.h>

//  void QSGGeometry::TexturedPoint2D::set(float nx, float ny, float ntx,
//      float nty)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry15TexturedPoint2D3setEffff(
    QSGGeometry::TexturedPoint2D *self,
    float nx,
    float ny,
    float ntx,
    float nty) {
  self->set(nx, ny, ntx, nty);
}

//  QSGGeometry::TexturedPoint2D::~TexturedPoint2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QSGGeometry15TexturedPoint2DD1Ev(
    QSGGeometry::TexturedPoint2D *self) {
  delete self;
}
