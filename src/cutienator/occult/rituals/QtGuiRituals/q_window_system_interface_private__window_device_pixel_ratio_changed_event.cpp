//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent::Window
//      DevicePixelRatioChangedEvent(QWindow *w)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent *ritual_ZN29QWindowSystemInterfacePrivate34WindowDevicePixelRatioChangedEventC1EP7QWindow(
    QWindow *w) {
  return new QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent(
      w);
}

//  QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent::~Windo
//      wDevicePixelRatioChangedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate34WindowDevicePixelRatioChangedEventD1Ev(
    QWindowSystemInterfacePrivate::WindowDevicePixelRatioChangedEvent *self) {
  delete self;
}
