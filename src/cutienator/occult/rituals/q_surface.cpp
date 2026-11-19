//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qsurface.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qsurface.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>

//  QSurface::~QSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QSurfaceD1Ev(QSurface *self) {
  delete self;
}

//  SurfaceClass QSurface::surfaceClass() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceClass ritual_ZNK8QSurface12surfaceClassEv(
    const QSurface *self) {
  return self->surfaceClass();
}

//  QSurfaceFormat QSurface::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK8QSurface6formatEv(const QSurface *self) {
  return new QSurfaceFormat(self->format());
}

//  SurfaceType QSurface::surfaceType() const
extern "C" Q_DECL_EXPORT
QSurface::SurfaceType ritual_ZNK8QSurface11surfaceTypeEv(
    const QSurface *self) {
  return self->surfaceType();
}

//  bool QSurface::supportsOpenGL() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QSurface14supportsOpenGLEv(const QSurface *self) {
  return self->supportsOpenGL();
}

//  QSize QSurface::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK8QSurface4sizeEv(const QSurface *self) {
  return new QSize(self->size());
}
