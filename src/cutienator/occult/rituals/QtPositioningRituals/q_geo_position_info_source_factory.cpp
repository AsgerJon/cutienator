//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeopositioninfosourcefactory.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtPositioning/qgeopositioninfosourcefactory.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QGeoPositionInfoSourceFactory::~QGeoPositionInfoSourceFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoPositionInfoSourceFactoryD1Ev(
    QGeoPositionInfoSourceFactory *self) {
  delete self;
}

//  QGeoPositionInfoSource
//      *QGeoPositionInfoSourceFactory::positionInfoSource(QObject *parent,
//      const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoSource *ritual_ZN29QGeoPositionInfoSourceFactory18positionInfoSourceEP7QObjectRK4QMapI7QString8QVariantE(
    QGeoPositionInfoSourceFactory *self,
    QObject *parent,
    const QMap<QString, QVariant> *parameters) {
  return self->positionInfoSource(parent, *parameters);
}

//  QGeoSatelliteInfoSource
//      *QGeoPositionInfoSourceFactory::satelliteInfoSource(QObject *parent,
//      const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoSource *ritual_ZN29QGeoPositionInfoSourceFactory19satelliteInfoSourceEP7QObjectRK4QMapI7QString8QVariantE(
    QGeoPositionInfoSourceFactory *self,
    QObject *parent,
    const QMap<QString, QVariant> *parameters) {
  return self->satelliteInfoSource(parent, *parameters);
}

//  QGeoAreaMonitorSource *QGeoPositionInfoSourceFactory::areaMonitor(QObject
//      *parent, const QVariantMap &parameters)
extern "C" Q_DECL_EXPORT
QGeoAreaMonitorSource *ritual_ZN29QGeoPositionInfoSourceFactory11areaMonitorEP7QObjectRK4QMapI7QString8QVariantE(
    QGeoPositionInfoSourceFactory *self,
    QObject *parent,
    const QMap<QString, QVariant> *parameters) {
  return self->areaMonitor(parent, *parameters);
}
