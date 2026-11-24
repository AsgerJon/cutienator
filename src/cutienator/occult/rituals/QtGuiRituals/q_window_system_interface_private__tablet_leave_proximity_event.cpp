//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QWindowSystemInterfacePrivate::TabletLeaveProximityEvent::TabletLeaveProx
//      imityEvent(QWindow *w, ulong time, const QPointF &local, const
//      QPointF &global, const QPointingDevice *device, Qt::MouseButtons b,
//      qreal xTilt, qreal yTilt, qreal tpressure, qreal rotation, qreal z,
//      Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::TabletLeaveProximityEvent *ritual_ZN29QWindowSystemInterfacePrivate25TabletLeaveProximityEventC1EP7QWindowmRK7QPointFS5_PK15QPointingDevice6QFlagsIN2Qt11MouseButtonEEdddddS9_INSA_16KeyboardModifierEE(
    QWindow *w,
    ulong time,
    const QPointF *local,
    const QPointF *global,
    const QPointingDevice *device,
    int b,
    qreal xTilt,
    qreal yTilt,
    qreal tpressure,
    qreal rotation,
    qreal z,
    int mods) {
  return new QWindowSystemInterfacePrivate::TabletLeaveProximityEvent(
      w,
      time,
      *local,
      *global,
      device,
      QFlags<Qt::MouseButton>::fromInt(b),
      xTilt,
      yTilt,
      tpressure,
      rotation,
      z,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  QWindowSystemInterfacePrivate::TabletLeaveProximityEvent::~TabletLeavePro
//      ximityEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate25TabletLeaveProximityEventD1Ev(
    QWindowSystemInterfacePrivate::TabletLeaveProximityEvent *self) {
  delete self;
}
