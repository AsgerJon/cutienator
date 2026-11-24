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

//  QWindow *QMutableEventPoint::window(const QEventPoint &p)
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZN18QMutableEventPoint6windowERK11QEventPoint(
    const QEventPoint *p) {
  return QMutableEventPoint::window(*p);
}

//  QObject *QMutableEventPoint::target(const QEventPoint &p)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN18QMutableEventPoint6targetERK11QEventPoint(
    const QEventPoint *p) {
  return QMutableEventPoint::target(*p);
}

//  QMutableEventPoint::~QMutableEventPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QMutableEventPointD1Ev(QMutableEventPoint *self) {
  delete self;
}
