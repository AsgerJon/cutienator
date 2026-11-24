//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandsurface.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandsurface.h>
#include <QtCore/qbytearray.h>

//  QWaylandSurfaceRole::QWaylandSurfaceRole(const QByteArray &n)
extern "C" Q_DECL_EXPORT
QWaylandSurfaceRole *ritual_ZN19QWaylandSurfaceRoleC1ERK10QByteArray(
    const QByteArray *n) {
  return new QWaylandSurfaceRole(*n);
}

//  const QByteArray QWaylandSurfaceRole::name()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN19QWaylandSurfaceRole4nameEv(
    QWaylandSurfaceRole *self) {
  return new QByteArray(self->name());
}

//  QWaylandSurfaceRole::~QWaylandSurfaceRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandSurfaceRoleD1Ev(QWaylandSurfaceRole *self) {
  delete self;
}
