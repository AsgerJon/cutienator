//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotilespec_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QGeoTileSpecPrivate::QGeoTileSpecPrivate(const QString &plugin, int
//      mapId, int zoom, int x, int y, int version)
extern "C" Q_DECL_EXPORT
QGeoTileSpecPrivate *ritual_ZN19QGeoTileSpecPrivateC1ERK7QStringiiiii(
    const QString *plugin,
    int mapId,
    int zoom,
    int x,
    int y,
    int version) {
  return new QGeoTileSpecPrivate(*plugin, mapId, zoom, x, y, version);
}

//  bool QGeoTileSpecPrivate::operator==(const QGeoTileSpecPrivate &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoTileSpecPrivateeqERKS_(
    const QGeoTileSpecPrivate *self,
    const QGeoTileSpecPrivate *rhs) {
  return self->operator==(*rhs);
}

//  QGeoTileSpecPrivate::~QGeoTileSpecPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTileSpecPrivateD1Ev(QGeoTileSpecPrivate *self) {
  delete self;
}
