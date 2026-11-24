//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::WindowSystemEvent::WindowSystemEvent(Event
//      Type t)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZN29QWindowSystemInterfacePrivate17WindowSystemEventC1ENS_9EventTypeE(
    QWindowSystemInterfacePrivate::EventType t) {
  return new QWindowSystemInterfacePrivate::WindowSystemEvent(t);
}

//  QWindowSystemInterfacePrivate::WindowSystemEvent::~WindowSystemEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate17WindowSystemEventD1Ev(
    QWindowSystemInterfacePrivate::WindowSystemEvent *self) {
  delete self;
}

//  bool QWindowSystemInterfacePrivate::WindowSystemEvent::synthetic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowSystemInterfacePrivate17WindowSystemEvent9syntheticEv(
    const QWindowSystemInterfacePrivate::WindowSystemEvent *self) {
  return self->synthetic();
}

//  bool QWindowSystemInterfacePrivate::WindowSystemEvent::nullWindow() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QWindowSystemInterfacePrivate17WindowSystemEvent10nullWindowEv(
    const QWindowSystemInterfacePrivate::WindowSystemEvent *self) {
  return self->nullWindow();
}
