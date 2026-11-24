//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/qquick3d.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3D/qquick3d.h>
#include <QtGui/qsurfaceformat.h>

//  QSurfaceFormat QQuick3D::idealSurfaceFormat(int samples)
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZN8QQuick3D18idealSurfaceFormatEi(int samples) {
  return new QSurfaceFormat(QQuick3D::idealSurfaceFormat(samples));
}

//  QQuick3D::~QQuick3D()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQuick3DD1Ev(QQuick3D *self) {
  delete self;
}
