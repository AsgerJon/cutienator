//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameradata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>

//  QGeoCameraData::QGeoCameraData()
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_ZN14QGeoCameraDataC1Ev() {
  return new QGeoCameraData();
}

//  QGeoCameraData::QGeoCameraData(const QGeoCameraData &other)
extern "C" Q_DECL_EXPORT
QGeoCameraData *ritual_ZN14QGeoCameraDataC1ERKS_(
    const QGeoCameraData *other) {
  return new QGeoCameraData(*other);
}

//  QGeoCameraData::~QGeoCameraData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraDataD1Ev(QGeoCameraData *self) {
  delete self;
}

//  bool operator==(const QGeoCameraData &lhs, const QGeoCameraData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QGeoCameraDataS1_(
    const QGeoCameraData *lhs,
    const QGeoCameraData *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoCameraData &lhs, const QGeoCameraData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QGeoCameraDataS1_(
    const QGeoCameraData *lhs,
    const QGeoCameraData *rhs) {
  return operator!=(*lhs, *rhs);
}

//  void QGeoCameraData::setCenter(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraData9setCenterERK14QGeoCoordinate(
    QGeoCameraData *self,
    const QGeoCoordinate *coordinate) {
  self->setCenter(*coordinate);
}

//  QGeoCoordinate QGeoCameraData::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK14QGeoCameraData6centerEv(
    const QGeoCameraData *self) {
  return new QGeoCoordinate(self->center());
}

//  void QGeoCameraData::setBearing(double bearing)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraData10setBearingEd(
    QGeoCameraData *self,
    double bearing) {
  self->setBearing(bearing);
}

//  double QGeoCameraData::bearing() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCameraData7bearingEv(const QGeoCameraData *self) {
  return self->bearing();
}

//  void QGeoCameraData::setTilt(double tilt)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraData7setTiltEd(QGeoCameraData *self, double tilt) {
  self->setTilt(tilt);
}

//  double QGeoCameraData::tilt() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCameraData4tiltEv(const QGeoCameraData *self) {
  return self->tilt();
}

//  void QGeoCameraData::setRoll(double roll)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraData7setRollEd(QGeoCameraData *self, double roll) {
  self->setRoll(roll);
}

//  double QGeoCameraData::roll() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCameraData4rollEv(const QGeoCameraData *self) {
  return self->roll();
}

//  void QGeoCameraData::setFieldOfView(double fieldOfView)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraData14setFieldOfViewEd(
    QGeoCameraData *self,
    double fieldOfView) {
  self->setFieldOfView(fieldOfView);
}

//  double QGeoCameraData::fieldOfView() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCameraData11fieldOfViewEv(
    const QGeoCameraData *self) {
  return self->fieldOfView();
}

//  void QGeoCameraData::setZoomLevel(double zoomLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGeoCameraData12setZoomLevelEd(
    QGeoCameraData *self,
    double zoomLevel) {
  self->setZoomLevel(zoomLevel);
}

//  double QGeoCameraData::zoomLevel() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK14QGeoCameraData9zoomLevelEv(const QGeoCameraData *self) {
  return self->zoomLevel();
}

//  bool QGeoCameraData::isEqual(const QGeoCameraData &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGeoCameraData7isEqualERKS_(
    const QGeoCameraData *self,
    const QGeoCameraData *other) {
  return self->isEqual(*other);
}
