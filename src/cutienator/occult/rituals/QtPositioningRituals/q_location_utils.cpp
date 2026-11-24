//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qlocationutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qlocationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>

//  bool QLocationUtils::isValidLat(double lat)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QLocationUtils10isValidLatEd(double lat) {
  return QLocationUtils::isValidLat(lat);
}

//  bool QLocationUtils::isValidLong(double lng)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QLocationUtils11isValidLongEd(double lng) {
  return QLocationUtils::isValidLong(lng);
}

//  double QLocationUtils::clipLat(double lat, double clipValue)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils7clipLatEdd(double lat, double clipValue) {
  return QLocationUtils::clipLat(lat, clipValue);
}

//  double QLocationUtils::wrapLong(double lng)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils8wrapLongEd(double lng) {
  return QLocationUtils::wrapLong(lng);
}

//  CardinalDirection QLocationUtils::azimuthToCardinalDirection4(double
//      azimuth)
extern "C" Q_DECL_EXPORT
QLocationUtils::CardinalDirection ritual_ZN14QLocationUtils27azimuthToCardinalDirection4Ed(
    double azimuth) {
  return QLocationUtils::azimuthToCardinalDirection4(azimuth);
}

//  CardinalDirection QLocationUtils::azimuthToCardinalDirection8(double
//      azimuth)
extern "C" Q_DECL_EXPORT
QLocationUtils::CardinalDirection ritual_ZN14QLocationUtils27azimuthToCardinalDirection8Ed(
    double azimuth) {
  return QLocationUtils::azimuthToCardinalDirection8(azimuth);
}

//  CardinalDirection QLocationUtils::azimuthToCardinalDirection16(double
//      azimuth)
extern "C" Q_DECL_EXPORT
QLocationUtils::CardinalDirection ritual_ZN14QLocationUtils28azimuthToCardinalDirection16Ed(
    double azimuth) {
  return QLocationUtils::azimuthToCardinalDirection16(azimuth);
}

//  double QLocationUtils::wrapLongExt(double lng)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils11wrapLongExtEd(double lng) {
  return QLocationUtils::wrapLongExt(lng);
}

//  double QLocationUtils::mirrorAzimuthX(double azimuth)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils14mirrorAzimuthXEd(double azimuth) {
  return QLocationUtils::mirrorAzimuthX(azimuth);
}

//  double QLocationUtils::mirrorAzimuthY(double azimuth)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils14mirrorAzimuthYEd(double azimuth) {
  return QLocationUtils::mirrorAzimuthY(azimuth);
}

//  double QLocationUtils::radians(double degrees)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils7radiansEd(double degrees) {
  return QLocationUtils::radians(degrees);
}

//  double QLocationUtils::degrees(double radians)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils7degreesEd(double radians) {
  return QLocationUtils::degrees(radians);
}

//  double QLocationUtils::earthMeanRadius()
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils15earthMeanRadiusEv() {
  return QLocationUtils::earthMeanRadius();
}

//  double QLocationUtils::earthMeanCircumference()
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils22earthMeanCircumferenceEv() {
  return QLocationUtils::earthMeanCircumference();
}

//  double QLocationUtils::mercatorMaxLatitude()
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils19mercatorMaxLatitudeEv() {
  return QLocationUtils::mercatorMaxLatitude();
}

//  QGeoCoordinate QLocationUtils::antipodalPoint(const QGeoCoordinate &p)
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN14QLocationUtils14antipodalPointERK14QGeoCoordinate(
    const QGeoCoordinate *p) {
  return new QGeoCoordinate(QLocationUtils::antipodalPoint(*p));
}

//  double QLocationUtils::mapLeftLongitude(double centerLongitude)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils16mapLeftLongitudeEd(
    double centerLongitude) {
  return QLocationUtils::mapLeftLongitude(centerLongitude);
}

//  double QLocationUtils::mapRightLongitude(double centerLongitude)
extern "C" Q_DECL_EXPORT
double ritual_ZN14QLocationUtils17mapRightLongitudeEd(
    double centerLongitude) {
  return QLocationUtils::mapRightLongitude(centerLongitude);
}

//  void QLocationUtils::split_double(double input, float *hipart, float
//      *lopart)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLocationUtils12split_doubleEdPfS0_(
    double input,
    float *hipart,
    float *lopart) {
  QLocationUtils::split_double(input, hipart, lopart);
}

//  qreal QLocationUtils::metersPerPixel(qreal zoomLevel, const
//      QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN14QLocationUtils14metersPerPixelEdRK14QGeoCoordinate(
    qreal zoomLevel,
    const QGeoCoordinate *coordinate) {
  return QLocationUtils::metersPerPixel(zoomLevel, *coordinate);
}

//  NmeaSentence QLocationUtils::getNmeaSentenceType(QByteArrayView bv)
extern "C" Q_DECL_EXPORT
QLocationUtils::NmeaSentence ritual_ZN14QLocationUtils19getNmeaSentenceTypeE14QByteArrayView(
    const QByteArrayView *bv) {
  return QLocationUtils::getNmeaSentenceType(*bv);
}

//  QGeoSatelliteInfo::SatelliteSystem
//      QLocationUtils::getSatelliteSystem(QByteArrayView bv)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfo::SatelliteSystem ritual_ZN14QLocationUtils18getSatelliteSystemE14QByteArrayView(
    const QByteArrayView *bv) {
  return QLocationUtils::getSatelliteSystem(*bv);
}

//  QGeoSatelliteInfo::SatelliteSystem
//      QLocationUtils::getSatelliteSystemBySatelliteId(int satId)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfo::SatelliteSystem ritual_ZN14QLocationUtils31getSatelliteSystemBySatelliteIdEi(
    int satId) {
  return QLocationUtils::getSatelliteSystemBySatelliteId(satId);
}

//  bool QLocationUtils::getPosInfoFromNmea(QByteArrayView bv,
//      QGeoPositionInfo *info, double uere, bool *hasFix)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QLocationUtils18getPosInfoFromNmeaE14QByteArrayViewP16QGeoPositionInfodPb(
    const QByteArrayView *bv,
    QGeoPositionInfo *info,
    double uere,
    bool *hasFix) {
  return QLocationUtils::getPosInfoFromNmea(*bv, info, uere, hasFix);
}

//  bool QLocationUtils::hasValidNmeaChecksum(QByteArrayView bv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QLocationUtils20hasValidNmeaChecksumE14QByteArrayView(
    const QByteArrayView *bv) {
  return QLocationUtils::hasValidNmeaChecksum(*bv);
}

//  bool QLocationUtils::getNmeaTime(const QByteArray &bytes, QTime *time)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QLocationUtils11getNmeaTimeERK10QByteArrayP5QTime(
    const QByteArray *bytes,
    QTime *time) {
  return QLocationUtils::getNmeaTime(*bytes, time);
}

//  bool QLocationUtils::getNmeaLatLong(const QByteArray &latString, char
//      latDirection, const QByteArray &lngString, char lngDirection, double
//      *lat, double *lon)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QLocationUtils14getNmeaLatLongERK10QByteArraycS2_cPdS3_(
    const QByteArray *latString,
    char latDirection,
    const QByteArray *lngString,
    char lngDirection,
    double *lat,
    double *lon) {
  return QLocationUtils::getNmeaLatLong(
      *latString,
      latDirection,
      *lngString,
      lngDirection,
      lat,
      lon);
}

//  QLocationUtils::~QLocationUtils()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QLocationUtilsD1Ev(QLocationUtils *self) {
  delete self;
}
