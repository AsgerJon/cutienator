//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeorouteparserosrmv5_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeorouteparserosrmv5_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>

//  QGeoRouteParserOsrmV5Extension::~QGeoRouteParserOsrmV5Extension()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGeoRouteParserOsrmV5ExtensionD1Ev(
    QGeoRouteParserOsrmV5Extension *self) {
  delete self;
}

//  void QGeoRouteParserOsrmV5Extension::updateQuery(QUrlQuery &query) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK30QGeoRouteParserOsrmV5Extension11updateQueryER9QUrlQuery(
    const QGeoRouteParserOsrmV5Extension *self,
    QUrlQuery *query) {
  self->updateQuery(*query);
}

//  void QGeoRouteParserOsrmV5Extension::updateSegment(QGeoRouteSegment
//      &segment, const QJsonObject &step, const QJsonObject &maneuver) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK30QGeoRouteParserOsrmV5Extension13updateSegmentER16QGeoRouteSegmentRK11QJsonObjectS4_(
    const QGeoRouteParserOsrmV5Extension *self,
    QGeoRouteSegment *segment,
    const QJsonObject *step,
    const QJsonObject *maneuver) {
  self->updateSegment(*segment, *step, *maneuver);
}
