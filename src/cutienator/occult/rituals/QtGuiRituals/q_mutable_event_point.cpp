//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qeventpoint_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qeventpoint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qpointingdevice.h>
#include <QtCore/qsize.h>
#include <QtGui/qvectornd.h>

//  QEventPoint QMutableEventPoint::withTimeStamp(ulong timestamp, int
//      pointId, QEventPoint::State state, QPointF position, QPointF
//      scenePosition, QPointF globalPosition)
extern "C" Q_DECL_EXPORT
QEventPoint *ritual_ZN18QMutableEventPoint13withTimeStampEmiN11QEventPoint5StateE7QPointFS2_S2_(
    ulong timestamp,
    int pointId,
    QEventPoint::State state,
    const QPointF *position,
    const QPointF *scenePosition,
    const QPointF *globalPosition) {
  return new QEventPoint(
      QMutableEventPoint::withTimeStamp(
          timestamp,
          pointId,
          state,
          *position,
          *scenePosition,
          *globalPosition));
}

//  void QMutableEventPoint::update(const QEventPoint &from, QEventPoint &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint6updateERK11QEventPointRS0_(
    const QEventPoint *from,
    QEventPoint *to) {
  QMutableEventPoint::update(*from, *to);
}

//  void QMutableEventPoint::detach(QEventPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint6detachER11QEventPoint(QEventPoint *p) {
  QMutableEventPoint::detach(*p);
}

//  void QMutableEventPoint::setId(QEventPoint &p, int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint5setIdER11QEventPointi(
    QEventPoint *p,
    int arg) {
  QMutableEventPoint::setId(*p, arg);
}

//  void QMutableEventPoint::setDevice(QEventPoint &p, const QPointingDevice
//      *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint9setDeviceER11QEventPointPK15QPointingDevice(
    QEventPoint *p,
    const QPointingDevice *arg) {
  QMutableEventPoint::setDevice(*p, arg);
}

//  void QMutableEventPoint::setTimestamp(QEventPoint &p, ulong t)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint12setTimestampER11QEventPointm(
    QEventPoint *p,
    ulong t) {
  QMutableEventPoint::setTimestamp(*p, t);
}

//  void QMutableEventPoint::setPressTimestamp(QEventPoint &p, ulong arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint17setPressTimestampER11QEventPointm(
    QEventPoint *p,
    ulong arg) {
  QMutableEventPoint::setPressTimestamp(*p, arg);
}

//  void QMutableEventPoint::setState(QEventPoint &p, QEventPoint::State arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint8setStateER11QEventPointNS0_5StateE(
    QEventPoint *p,
    QEventPoint::State arg) {
  QMutableEventPoint::setState(*p, arg);
}

//  void QMutableEventPoint::setUniqueId(QEventPoint &p,
//      QPointingDeviceUniqueId arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint11setUniqueIdER11QEventPoint23QPointingDeviceUniqueId(
    QEventPoint *p,
    const QPointingDeviceUniqueId *arg) {
  QMutableEventPoint::setUniqueId(*p, *arg);
}

//  void QMutableEventPoint::setPosition(QEventPoint &p, QPointF arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint11setPositionER11QEventPoint7QPointF(
    QEventPoint *p,
    const QPointF *arg) {
  QMutableEventPoint::setPosition(*p, *arg);
}

//  void QMutableEventPoint::setScenePosition(QEventPoint &p, QPointF arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint16setScenePositionER11QEventPoint7QPointF(
    QEventPoint *p,
    const QPointF *arg) {
  QMutableEventPoint::setScenePosition(*p, *arg);
}

//  void QMutableEventPoint::setGlobalPosition(QEventPoint &p, QPointF arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint17setGlobalPositionER11QEventPoint7QPointF(
    QEventPoint *p,
    const QPointF *arg) {
  QMutableEventPoint::setGlobalPosition(*p, *arg);
}

//  void QMutableEventPoint::setGlobalPressPosition(QEventPoint &p, QPointF
//      arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint22setGlobalPressPositionER11QEventPoint7QPointF(
    QEventPoint *p,
    const QPointF *arg) {
  QMutableEventPoint::setGlobalPressPosition(*p, *arg);
}

//  void QMutableEventPoint::setGlobalGrabPosition(QEventPoint &p, QPointF
//      arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint21setGlobalGrabPositionER11QEventPoint7QPointF(
    QEventPoint *p,
    const QPointF *arg) {
  QMutableEventPoint::setGlobalGrabPosition(*p, *arg);
}

//  void QMutableEventPoint::setGlobalLastPosition(QEventPoint &p, QPointF
//      arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint21setGlobalLastPositionER11QEventPoint7QPointF(
    QEventPoint *p,
    const QPointF *arg) {
  QMutableEventPoint::setGlobalLastPosition(*p, *arg);
}

//  void QMutableEventPoint::setEllipseDiameters(QEventPoint &p, QSizeF arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint19setEllipseDiametersER11QEventPoint6QSizeF(
    QEventPoint *p,
    const QSizeF *arg) {
  QMutableEventPoint::setEllipseDiameters(*p, *arg);
}

//  void QMutableEventPoint::setPressure(QEventPoint &p, qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint11setPressureER11QEventPointd(
    QEventPoint *p,
    qreal arg) {
  QMutableEventPoint::setPressure(*p, arg);
}

//  void QMutableEventPoint::setRotation(QEventPoint &p, qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint11setRotationER11QEventPointd(
    QEventPoint *p,
    qreal arg) {
  QMutableEventPoint::setRotation(*p, arg);
}

//  void QMutableEventPoint::setVelocity(QEventPoint &p, QVector2D arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint11setVelocityER11QEventPoint9QVector2D(
    QEventPoint *p,
    const QVector2D *arg) {
  QMutableEventPoint::setVelocity(*p, *arg);
}

//  QWindow *QMutableEventPoint::window(const QEventPoint &p)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN18QMutableEventPoint6windowERK11QEventPoint(
    const QEventPoint *p) {
  return QMutableEventPoint::window(*p);
}

//  void QMutableEventPoint::setWindow(QEventPoint &p, QWindow *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint9setWindowER11QEventPointP7QWindow(
    QEventPoint *p,
    QWindow *arg) {
  QMutableEventPoint::setWindow(*p, arg);
}

//  QObject *QMutableEventPoint::target(const QEventPoint &p)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN18QMutableEventPoint6targetERK11QEventPoint(
    const QEventPoint *p) {
  return QMutableEventPoint::target(*p);
}

//  void QMutableEventPoint::setTarget(QEventPoint &p, QObject *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPoint9setTargetER11QEventPointP7QObject(
    QEventPoint *p,
    QObject *arg) {
  QMutableEventPoint::setTarget(*p, arg);
}

//  QMutableEventPoint::~QMutableEventPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPointD1Ev(QMutableEventPoint *self) {
  delete self;
}
