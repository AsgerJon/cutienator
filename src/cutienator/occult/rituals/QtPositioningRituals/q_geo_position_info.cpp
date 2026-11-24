//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeopositioninfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/qgeopositioninfo.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>

//  QGeoPositionInfo::QGeoPositionInfo()
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_ZN16QGeoPositionInfoC1Ev() {
  return new QGeoPositionInfo();
}

//  QGeoPositionInfo::QGeoPositionInfo(const QGeoCoordinate &coordinate,
//      const QDateTime &updateTime)
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_ZN16QGeoPositionInfoC1ERK14QGeoCoordinateRK9QDateTime(
    const QGeoCoordinate *coordinate,
    const QDateTime *updateTime) {
  return new QGeoPositionInfo(*coordinate, *updateTime);
}

//  QGeoPositionInfo::QGeoPositionInfo(const QGeoPositionInfo &other)
extern "C" Q_DECL_EXPORT
QGeoPositionInfo *ritual_ZN16QGeoPositionInfoC1ERKS_(
    const QGeoPositionInfo *other) {
  return new QGeoPositionInfo(*other);
}

//  QGeoPositionInfo::~QGeoPositionInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPositionInfoD1Ev(QGeoPositionInfo *self) {
  delete self;
}

//  bool operator==(const QGeoPositionInfo &lhs, const QGeoPositionInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK16QGeoPositionInfoS1_(
    const QGeoPositionInfo *lhs,
    const QGeoPositionInfo *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoPositionInfo &lhs, const QGeoPositionInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK16QGeoPositionInfoS1_(
    const QGeoPositionInfo *lhs,
    const QGeoPositionInfo *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QGeoPositionInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoPositionInfo7isValidEv(const QGeoPositionInfo *self) {
  return self->isValid();
}

//  void QGeoPositionInfo::setTimestamp(const QDateTime &timestamp)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPositionInfo12setTimestampERK9QDateTime(
    QGeoPositionInfo *self,
    const QDateTime *timestamp) {
  self->setTimestamp(*timestamp);
}

//  QDateTime QGeoPositionInfo::timestamp() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QGeoPositionInfo9timestampEv(
    const QGeoPositionInfo *self) {
  return new QDateTime(self->timestamp());
}

//  void QGeoPositionInfo::setCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPositionInfo13setCoordinateERK14QGeoCoordinate(
    QGeoPositionInfo *self,
    const QGeoCoordinate *coordinate) {
  self->setCoordinate(*coordinate);
}

//  QGeoCoordinate QGeoPositionInfo::coordinate() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK16QGeoPositionInfo10coordinateEv(
    const QGeoPositionInfo *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  void QGeoPositionInfo::setAttribute(Attribute attribute, qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPositionInfo12setAttributeENS_9AttributeEd(
    QGeoPositionInfo *self,
    QGeoPositionInfo::Attribute attribute,
    qreal value) {
  self->setAttribute(attribute, value);
}

//  qreal QGeoPositionInfo::attribute(Attribute attribute) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK16QGeoPositionInfo9attributeENS_9AttributeE(
    const QGeoPositionInfo *self,
    QGeoPositionInfo::Attribute attribute) {
  return self->attribute(attribute);
}

//  void QGeoPositionInfo::removeAttribute(Attribute attribute)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPositionInfo15removeAttributeENS_9AttributeE(
    QGeoPositionInfo *self,
    QGeoPositionInfo::Attribute attribute) {
  self->removeAttribute(attribute);
}

//  bool QGeoPositionInfo::hasAttribute(Attribute attribute) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QGeoPositionInfo12hasAttributeENS_9AttributeE(
    const QGeoPositionInfo *self,
    QGeoPositionInfo::Attribute attribute) {
  return self->hasAttribute(attribute);
}

//  void QGeoPositionInfo::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QGeoPositionInfo6detachEv(QGeoPositionInfo *self) {
  self->detach();
}

//  bool QGeoPositionInfo::equals(const QGeoPositionInfo &lhs, const
//      QGeoPositionInfo &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QGeoPositionInfo6equalsERKS_S1_(
    const QGeoPositionInfo *lhs,
    const QGeoPositionInfo *rhs) {
  return QGeoPositionInfo::equals(*lhs, *rhs);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QGeoPositionInfo &info)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK16QGeoPositionInfo(
    const QDebug *dbg,
    const QGeoPositionInfo *info) {
  return new QDebug(operator<<(*dbg, *info));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QGeoPositionInfo::debugStreaming(QDebug dbg, const
//      QGeoPositionInfo &info)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN16QGeoPositionInfo14debugStreamingE6QDebugRKS_(
    const QDebug *dbg,
    const QGeoPositionInfo *info) {
  return new QDebug(QGeoPositionInfo::debugStreaming(*dbg, *info));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
