//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_GESTURES)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QWindowSystemInterfacePrivate::GestureEvent::GestureEvent(QWindow
//      *window, ulong time, Qt::NativeGestureType type, const
//      QPointingDevice *dev, int fingerCount, QPointF pos, QPointF
//      globalPos, qreal realValue, QPointF delta)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::GestureEvent *ritual_ZN29QWindowSystemInterfacePrivate12GestureEventC1EP7QWindowmN2Qt17NativeGestureTypeEPK15QPointingDevicei7QPointFS8_dS8_(
    QWindow *window,
    ulong time,
    Qt::NativeGestureType type,
    const QPointingDevice *dev,
    int fingerCount,
    const QPointF *pos,
    const QPointF *globalPos,
    qreal realValue,
    const QPointF *delta) {
  return new QWindowSystemInterfacePrivate::GestureEvent(
      window,
      time,
      type,
      dev,
      fingerCount,
      *pos,
      *globalPos,
      realValue,
      *delta);
}

//  QWindowSystemInterfacePrivate::GestureEvent::~GestureEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate12GestureEventD1Ev(
    QWindowSystemInterfacePrivate::GestureEvent *self) {
  delete self;
}

#endif  // !defined(QT_NO_GESTURES)
