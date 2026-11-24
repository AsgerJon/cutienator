//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qgeomaneuver.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qgeomaneuver.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QGeoManeuver::QGeoManeuver()
extern "C" Q_DECL_EXPORT
QGeoManeuver *ritual_ZN12QGeoManeuverC1Ev() {
  return new QGeoManeuver();
}

//  QGeoManeuver::QGeoManeuver(const QGeoManeuver &other)
extern "C" Q_DECL_EXPORT
QGeoManeuver *ritual_ZN12QGeoManeuverC1ERKS_(const QGeoManeuver *other) {
  return new QGeoManeuver(*other);
}

//  QGeoManeuver::~QGeoManeuver()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuverD1Ev(QGeoManeuver *self) {
  delete self;
}

//  bool operator==(const QGeoManeuver &lhs, const QGeoManeuver &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QGeoManeuverS1_(
    const QGeoManeuver *lhs,
    const QGeoManeuver *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoManeuver &lhs, const QGeoManeuver &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QGeoManeuverS1_(
    const QGeoManeuver *lhs,
    const QGeoManeuver *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QGeoManeuver::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGeoManeuver7isValidEv(const QGeoManeuver *self) {
  return self->isValid();
}

//  void QGeoManeuver::setPosition(const QGeoCoordinate &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver11setPositionERK14QGeoCoordinate(
    QGeoManeuver *self,
    const QGeoCoordinate *position) {
  self->setPosition(*position);
}

//  QGeoCoordinate QGeoManeuver::position() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK12QGeoManeuver8positionEv(
    const QGeoManeuver *self) {
  return new QGeoCoordinate(self->position());
}

//  void QGeoManeuver::setInstructionText(const QString &instructionText)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver18setInstructionTextERK7QString(
    QGeoManeuver *self,
    const QString *instructionText) {
  self->setInstructionText(*instructionText);
}

//  QString QGeoManeuver::instructionText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QGeoManeuver15instructionTextEv(
    const QGeoManeuver *self) {
  return new QString(self->instructionText());
}

//  void QGeoManeuver::setDirection(InstructionDirection direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver12setDirectionENS_20InstructionDirectionE(
    QGeoManeuver *self,
    QGeoManeuver::InstructionDirection direction) {
  self->setDirection(direction);
}

//  InstructionDirection QGeoManeuver::direction() const
extern "C" Q_DECL_EXPORT
QGeoManeuver::InstructionDirection ritual_ZNK12QGeoManeuver9directionEv(
    const QGeoManeuver *self) {
  return self->direction();
}

//  void QGeoManeuver::setTimeToNextInstruction(int secs)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver24setTimeToNextInstructionEi(
    QGeoManeuver *self,
    int secs) {
  self->setTimeToNextInstruction(secs);
}

//  int QGeoManeuver::timeToNextInstruction() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QGeoManeuver21timeToNextInstructionEv(
    const QGeoManeuver *self) {
  return self->timeToNextInstruction();
}

//  void QGeoManeuver::setDistanceToNextInstruction(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver28setDistanceToNextInstructionEd(
    QGeoManeuver *self,
    qreal distance) {
  self->setDistanceToNextInstruction(distance);
}

//  qreal QGeoManeuver::distanceToNextInstruction() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK12QGeoManeuver25distanceToNextInstructionEv(
    const QGeoManeuver *self) {
  return self->distanceToNextInstruction();
}

//  void QGeoManeuver::setWaypoint(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver11setWaypointERK14QGeoCoordinate(
    QGeoManeuver *self,
    const QGeoCoordinate *coordinate) {
  self->setWaypoint(*coordinate);
}

//  QGeoCoordinate QGeoManeuver::waypoint() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK12QGeoManeuver8waypointEv(
    const QGeoManeuver *self) {
  return new QGeoCoordinate(self->waypoint());
}

//  void QGeoManeuver::setExtendedAttributes(const QVariantMap
//      &extendedAttributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoManeuver21setExtendedAttributesERK4QMapI7QString8QVariantE(
    QGeoManeuver *self,
    const QMap<QString, QVariant> *extendedAttributes) {
  self->setExtendedAttributes(*extendedAttributes);
}

//  QVariantMap QGeoManeuver::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK12QGeoManeuver18extendedAttributesEv(
    const QGeoManeuver *self) {
  return new QMap<QString, QVariant>(self->extendedAttributes());
}

//  bool QGeoManeuver::isEqual(const QGeoManeuver &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGeoManeuver7isEqualERKS_(
    const QGeoManeuver *self,
    const QGeoManeuver *other) {
  return self->isEqual(*other);
}
