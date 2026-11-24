//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeocoordinate.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QGeoCoordinate::QGeoCoordinate()
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN14QGeoCoordinateC1Ev() {
  return new QGeoCoordinate();
}

//  QGeoCoordinate::QGeoCoordinate(double latitude, double longitude)
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN14QGeoCoordinateC1Edd(
    double latitude,
    double longitude) {
  return new QGeoCoordinate(latitude, longitude);
}

//  QGeoCoordinate::QGeoCoordinate(double latitude, double longitude, double
//      altitude)
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN14QGeoCoordinateC1Eddd(
    double latitude,
    double longitude,
    double altitude) {
  return new QGeoCoordinate(latitude, longitude, altitude);
}

//  QGeoCoordinate::QGeoCoordinate(const QGeoCoordinate &other)
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZN14QGeoCoordinateC1ERKS_(
    const QGeoCoordinate *other) {
  return new QGeoCoordinate(*other);
}

//  QGeoCoordinate::~QGeoCoordinate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCoordinateD1Ev(QGeoCoordinate *self) {
  delete self;
}

//  bool operator==(const QGeoCoordinate &lhs, const QGeoCoordinate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QGeoCoordinateS1_(
    const QGeoCoordinate *lhs,
    const QGeoCoordinate *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoCoordinate &lhs, const QGeoCoordinate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QGeoCoordinateS1_(
    const QGeoCoordinate *lhs,
    const QGeoCoordinate *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QGeoCoordinate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGeoCoordinate7isValidEv(const QGeoCoordinate *self) {
  return self->isValid();
}

//  CoordinateType QGeoCoordinate::type() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate::CoordinateType ritual_ZNK14QGeoCoordinate4typeEv(
    const QGeoCoordinate *self) {
  return self->type();
}

//  void QGeoCoordinate::setLatitude(double latitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCoordinate11setLatitudeEd(
    QGeoCoordinate *self,
    double latitude) {
  self->setLatitude(latitude);
}

//  double QGeoCoordinate::latitude() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCoordinate8latitudeEv(const QGeoCoordinate *self) {
  return self->latitude();
}

//  void QGeoCoordinate::setLongitude(double longitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCoordinate12setLongitudeEd(
    QGeoCoordinate *self,
    double longitude) {
  self->setLongitude(longitude);
}

//  double QGeoCoordinate::longitude() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCoordinate9longitudeEv(const QGeoCoordinate *self) {
  return self->longitude();
}

//  void QGeoCoordinate::setAltitude(double altitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCoordinate11setAltitudeEd(
    QGeoCoordinate *self,
    double altitude) {
  self->setAltitude(altitude);
}

//  double QGeoCoordinate::altitude() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCoordinate8altitudeEv(const QGeoCoordinate *self) {
  return self->altitude();
}

//  qreal QGeoCoordinate::distanceTo(const QGeoCoordinate &other) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGeoCoordinate10distanceToERKS_(
    const QGeoCoordinate *self,
    const QGeoCoordinate *other) {
  return self->distanceTo(*other);
}

//  qreal QGeoCoordinate::azimuthTo(const QGeoCoordinate &other) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGeoCoordinate9azimuthToERKS_(
    const QGeoCoordinate *self,
    const QGeoCoordinate *other) {
  return self->azimuthTo(*other);
}

//  QGeoCoordinate QGeoCoordinate::atDistanceAndAzimuth(qreal distance, qreal
//      azimuth, qreal distanceUp) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK14QGeoCoordinate20atDistanceAndAzimuthEddd(
    const QGeoCoordinate *self,
    qreal distance,
    qreal azimuth,
    qreal distanceUp) {
  return new QGeoCoordinate(
      self->atDistanceAndAzimuth(
          distance,
          azimuth,
          distanceUp));
}

//  QString QGeoCoordinate::toString(CoordinateFormat format) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QGeoCoordinate8toStringENS_16CoordinateFormatE(
    const QGeoCoordinate *self,
    QGeoCoordinate::CoordinateFormat format) {
  return new QString(self->toString(format));
}

//  bool QGeoCoordinate::equals(const QGeoCoordinate &lhs, const
//      QGeoCoordinate &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGeoCoordinate6equalsERKS_S1_(
    const QGeoCoordinate *lhs,
    const QGeoCoordinate *rhs) {
  return QGeoCoordinate::equals(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QGeoCoordinate &coord)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK14QGeoCoordinate(
    const QDebug *dbg,
    const QGeoCoordinate *coord) {
  return new QDebug(operator<<(*dbg, *coord));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QGeoCoordinate::debugStreaming(QDebug dbg, const QGeoCoordinate
//      &coord)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN14QGeoCoordinate14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QGeoCoordinate *coord) {
  return new QDebug(QGeoCoordinate::debugStreaming(*dbg, *coord));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QGeoCoordinate>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_list_make_QGeoCoordinate() {
  return new QList<QGeoCoordinate>();
}

//  void QList<QGeoCoordinate>::append(const QGeoCoordinate &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoCoordinate(
    QList<QGeoCoordinate> *self,
    const QGeoCoordinate *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoCoordinate>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoCoordinate(
    const QList<QGeoCoordinate> *self) {
  return self->size();
}

//  const QGeoCoordinate &QList<QGeoCoordinate>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_list_at_QGeoCoordinate(
    const QList<QGeoCoordinate> *self,
    long long index) {
  return new QGeoCoordinate(self->at(index));
}

//  QList<QGeoCoordinate>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoCoordinate(QList<QGeoCoordinate> *self) {
  delete self;
}
