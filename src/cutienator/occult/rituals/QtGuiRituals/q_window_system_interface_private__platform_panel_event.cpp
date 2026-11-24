//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::PlatformPanelEvent::PlatformPanelEvent(QWi
//      ndow *w)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::PlatformPanelEvent *ritual_ZN29QWindowSystemInterfacePrivate18PlatformPanelEventC1EP7QWindow(
    QWindow *w) {
  return new QWindowSystemInterfacePrivate::PlatformPanelEvent(w);
}

//  QWindowSystemInterfacePrivate::PlatformPanelEvent::~PlatformPanelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate18PlatformPanelEventD1Ev(
    QWindowSystemInterfacePrivate::PlatformPanelEvent *self) {
  delete self;
}
