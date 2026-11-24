//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::ScreenRefreshRateEvent::ScreenRefreshRateE
//      vent(QScreen *s, qreal r)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ScreenRefreshRateEvent *ritual_ZN29QWindowSystemInterfacePrivate22ScreenRefreshRateEventC1EP7QScreend(
    QScreen *s,
    qreal r) {
  return new QWindowSystemInterfacePrivate::ScreenRefreshRateEvent(s, r);
}

//  QWindowSystemInterfacePrivate::ScreenRefreshRateEvent::~ScreenRefreshRate
//      Event()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate22ScreenRefreshRateEventD1Ev(
    QWindowSystemInterfacePrivate::ScreenRefreshRateEvent *self) {
  delete self;
}
