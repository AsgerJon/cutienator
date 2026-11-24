//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::LeaveEvent::LeaveEvent(QWindow *leave)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::LeaveEvent *ritual_ZN29QWindowSystemInterfacePrivate10LeaveEventC1EP7QWindow(
    QWindow *leave) {
  return new QWindowSystemInterfacePrivate::LeaveEvent(leave);
}

//  QWindowSystemInterfacePrivate::LeaveEvent::~LeaveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10LeaveEventD1Ev(
    QWindowSystemInterfacePrivate::LeaveEvent *self) {
  delete self;
}
