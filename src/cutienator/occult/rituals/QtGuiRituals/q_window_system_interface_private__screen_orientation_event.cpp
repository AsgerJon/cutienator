//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::ScreenOrientationEvent::ScreenOrientationE
//      vent(QScreen *s, Qt::ScreenOrientation o)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ScreenOrientationEvent *ritual_ZN29QWindowSystemInterfacePrivate22ScreenOrientationEventC1EP7QScreenN2Qt17ScreenOrientationE(
    QScreen *s,
    Qt::ScreenOrientation o) {
  return new QWindowSystemInterfacePrivate::ScreenOrientationEvent(s, o);
}

//  QWindowSystemInterfacePrivate::ScreenOrientationEvent::~ScreenOrientation
//      Event()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate22ScreenOrientationEventD1Ev(
    QWindowSystemInterfacePrivate::ScreenOrientationEvent *self) {
  delete self;
}
