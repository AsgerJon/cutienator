//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomaneuver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaneuver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qgeomaneuver.h>
#include <QtLocation/private/qgeomaneuver_p.h>
#include <QtCore/QVariant>
#include <QtPositioning/qgeocoordinate.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 370, as _ZNK19QGeoManeuverPrivate6equalsERKS_
inline bool QGeoManeuverPrivate::equals(const QGeoManeuverPrivate &other) const
{
    return ((valid() == other.valid())
            && (position() == other.position())
            && (text() == other.text())
            && (direction() == other.direction())
            && (timeToNextInstruction() == other.timeToNextInstruction())
            && (distanceToNextInstruction() == other.distanceToNextInstruction())
            && (waypoint() == other.waypoint()));
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 384, as _ZNK19QGeoManeuverPrivate5validEv
inline bool QGeoManeuverPrivate::valid() const
{
    return m_valid;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 389, as _ZN19QGeoManeuverPrivate8setValidEb
inline void QGeoManeuverPrivate::setValid(bool valid)
{
    m_valid = valid;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 394, as _ZNK19QGeoManeuverPrivate2idEv
inline QString QGeoManeuverPrivate::id() const
{
    return m_id;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 399, as _ZN19QGeoManeuverPrivate5setIdERK7QString
inline void QGeoManeuverPrivate::setId(const QString &id)
{
    m_id = id;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 404, as _ZNK19QGeoManeuverPrivate8positionEv
inline QGeoCoordinate QGeoManeuverPrivate::position() const
{
    return m_position;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 409, as _ZN19QGeoManeuverPrivate11setPositionERK14QGeoCoordinate
inline void QGeoManeuverPrivate::setPosition(const QGeoCoordinate &position)
{
    m_position = position;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 414, as _ZNK19QGeoManeuverPrivate4textEv
inline QString QGeoManeuverPrivate::text() const
{
    return m_text;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 419, as _ZN19QGeoManeuverPrivate7setTextERK7QString
inline void QGeoManeuverPrivate::setText(const QString &text)
{
    m_text = text;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 424, as _ZNK19QGeoManeuverPrivate9directionEv
inline QGeoManeuver::InstructionDirection QGeoManeuverPrivate::direction() const
{
    return m_direction;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 429, as _ZN19QGeoManeuverPrivate12setDirectionEN12QGeoManeuver20InstructionDirectionE
inline void QGeoManeuverPrivate::setDirection(QGeoManeuver::InstructionDirection direction)
{
    m_direction = direction;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 434, as _ZNK19QGeoManeuverPrivate21timeToNextInstructionEv
inline int QGeoManeuverPrivate::timeToNextInstruction() const
{
    return m_timeToNextInstruction;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 439, as _ZN19QGeoManeuverPrivate24setTimeToNextInstructionEi
inline void QGeoManeuverPrivate::setTimeToNextInstruction(int timeToNextInstruction)
{
    m_timeToNextInstruction = timeToNextInstruction;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 444, as _ZNK19QGeoManeuverPrivate25distanceToNextInstructionEv
inline qreal QGeoManeuverPrivate::distanceToNextInstruction() const
{
    return m_distanceToNextInstruction;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 449, as _ZN19QGeoManeuverPrivate28setDistanceToNextInstructionEd
inline void QGeoManeuverPrivate::setDistanceToNextInstruction(qreal distanceToNextInstruction)
{
    m_distanceToNextInstruction = distanceToNextInstruction;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 454, as _ZNK19QGeoManeuverPrivate8waypointEv
inline QGeoCoordinate QGeoManeuverPrivate::waypoint() const
{
    return m_waypoint;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 459, as _ZN19QGeoManeuverPrivate11setWaypointERK14QGeoCoordinate
inline void QGeoManeuverPrivate::setWaypoint(const QGeoCoordinate &waypoint)
{
    m_waypoint = waypoint;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 464, as _ZNK19QGeoManeuverPrivate18extendedAttributesEv
inline QVariantMap QGeoManeuverPrivate::extendedAttributes() const
{
    return m_extendedAttributes;
}

//  from ../qtlocation/src/location/maps/qgeomaneuver.cpp, line 469, as _ZN19QGeoManeuverPrivate21setExtendedAttributesERK4QMapI7QString8QVariantE
inline void QGeoManeuverPrivate::setExtendedAttributes(const QVariantMap &extendedAttributes)
{
    m_extendedAttributes = extendedAttributes;
}
//  -----------------------------------------------------------------------

//  bool QGeoManeuverPrivate::equals(const QGeoManeuverPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoManeuverPrivate6equalsERKS_(
    const QGeoManeuverPrivate *self,
    const QGeoManeuverPrivate *other) {
  return self->equals(*other);
}

//  bool QGeoManeuverPrivate::valid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoManeuverPrivate5validEv(
    const QGeoManeuverPrivate *self) {
  return self->valid();
}

//  void QGeoManeuverPrivate::setValid(bool valid)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate8setValidEb(
    QGeoManeuverPrivate *self,
    bool valid) {
  self->setValid(valid);
}

//  QString QGeoManeuverPrivate::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoManeuverPrivate2idEv(
    const QGeoManeuverPrivate *self) {
  return new QString(self->id());
}

//  void QGeoManeuverPrivate::setId(const QString &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate5setIdERK7QString(
    QGeoManeuverPrivate *self,
    const QString *id) {
  self->setId(*id);
}

//  QGeoCoordinate QGeoManeuverPrivate::position() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK19QGeoManeuverPrivate8positionEv(
    const QGeoManeuverPrivate *self) {
  return new QGeoCoordinate(self->position());
}

//  void QGeoManeuverPrivate::setPosition(const QGeoCoordinate &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate11setPositionERK14QGeoCoordinate(
    QGeoManeuverPrivate *self,
    const QGeoCoordinate *position) {
  self->setPosition(*position);
}

//  QString QGeoManeuverPrivate::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QGeoManeuverPrivate4textEv(
    const QGeoManeuverPrivate *self) {
  return new QString(self->text());
}

//  void QGeoManeuverPrivate::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate7setTextERK7QString(
    QGeoManeuverPrivate *self,
    const QString *text) {
  self->setText(*text);
}

//  QGeoManeuver::InstructionDirection QGeoManeuverPrivate::direction() const
extern "C" Q_DECL_EXPORT
QGeoManeuver::InstructionDirection ritual_ZNK19QGeoManeuverPrivate9directionEv(
    const QGeoManeuverPrivate *self) {
  return self->direction();
}

//  void QGeoManeuverPrivate::setDirection(QGeoManeuver::InstructionDirection
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate12setDirectionEN12QGeoManeuver20InstructionDirectionE(
    QGeoManeuverPrivate *self,
    QGeoManeuver::InstructionDirection direction) {
  self->setDirection(direction);
}

//  int QGeoManeuverPrivate::timeToNextInstruction() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QGeoManeuverPrivate21timeToNextInstructionEv(
    const QGeoManeuverPrivate *self) {
  return self->timeToNextInstruction();
}

//  void QGeoManeuverPrivate::setTimeToNextInstruction(int
//      timeToNextInstruction)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate24setTimeToNextInstructionEi(
    QGeoManeuverPrivate *self,
    int timeToNextInstruction) {
  self->setTimeToNextInstruction(timeToNextInstruction);
}

//  qreal QGeoManeuverPrivate::distanceToNextInstruction() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QGeoManeuverPrivate25distanceToNextInstructionEv(
    const QGeoManeuverPrivate *self) {
  return self->distanceToNextInstruction();
}

//  void QGeoManeuverPrivate::setDistanceToNextInstruction(qreal
//      distanceToNextInstruction)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate28setDistanceToNextInstructionEd(
    QGeoManeuverPrivate *self,
    qreal distanceToNextInstruction) {
  self->setDistanceToNextInstruction(distanceToNextInstruction);
}

//  QGeoCoordinate QGeoManeuverPrivate::waypoint() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK19QGeoManeuverPrivate8waypointEv(
    const QGeoManeuverPrivate *self) {
  return new QGeoCoordinate(self->waypoint());
}

//  void QGeoManeuverPrivate::setWaypoint(const QGeoCoordinate &waypoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate11setWaypointERK14QGeoCoordinate(
    QGeoManeuverPrivate *self,
    const QGeoCoordinate *waypoint) {
  self->setWaypoint(*waypoint);
}

//  QVariantMap QGeoManeuverPrivate::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK19QGeoManeuverPrivate18extendedAttributesEv(
    const QGeoManeuverPrivate *self) {
  return new QMap<QString, QVariant>(self->extendedAttributes());
}

//  void QGeoManeuverPrivate::setExtendedAttributes(const QVariantMap
//      &extendedAttributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivate21setExtendedAttributesERK4QMapI7QString8QVariantE(
    QGeoManeuverPrivate *self,
    const QMap<QString, QVariant> *extendedAttributes) {
  self->setExtendedAttributes(*extendedAttributes);
}

//  QGeoManeuverPrivate::~QGeoManeuverPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoManeuverPrivateD1Ev(QGeoManeuverPrivate *self) {
  delete self;
}
