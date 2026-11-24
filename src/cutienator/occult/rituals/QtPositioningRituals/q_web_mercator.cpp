//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qwebmercator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qwebmercator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDoubleVector2D QWebMercator::coordToMercator(const QGeoCoordinate
//      &coord)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZN12QWebMercator15coordToMercatorERK14QGeoCoordinate(
    const QGeoCoordinate *coord) {
  return new QDoubleVector2D(QWebMercator::coordToMercator(*coord));
}

//  QGeoCoordinate QWebMercator::mercatorToCoord(const QDoubleVector2D
//      &mercator)
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN12QWebMercator15mercatorToCoordERK15QDoubleVector2D(
    const QDoubleVector2D *mercator) {
  return new QGeoCoordinate(QWebMercator::mercatorToCoord(*mercator));
}

//  QGeoCoordinate QWebMercator::coordinateInterpolation(const QGeoCoordinate
//      &from, const QGeoCoordinate &to, qreal progress)
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN12QWebMercator23coordinateInterpolationERK14QGeoCoordinateS2_d(
    const QGeoCoordinate *from,
    const QGeoCoordinate *to,
    qreal progress) {
  return new QGeoCoordinate(
      QWebMercator::coordinateInterpolation(
          *from,
          *to,
          progress));
}

//  double QWebMercator::realmod(const double a, const double b)
extern "C" Q_DECL_EXPORT
double ritual_ZN12QWebMercator7realmodEdd(double a, double b) {
  return QWebMercator::realmod(a, b);
}

//  QWebMercator::~QWebMercator()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWebMercatorD1Ev(QWebMercator *self) {
  delete self;
}
