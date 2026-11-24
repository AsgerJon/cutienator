//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::ApplicationStateChangedEvent::ApplicationS
//      tateChangedEvent(Qt::ApplicationState newState, bool forcePropagate)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ApplicationStateChangedEvent *ritual_ZN29QWindowSystemInterfacePrivate28ApplicationStateChangedEventC1EN2Qt16ApplicationStateEb(
    Qt::ApplicationState newState,
    bool forcePropagate) {
  return new QWindowSystemInterfacePrivate::ApplicationStateChangedEvent(
      newState,
      forcePropagate);
}

//  QWindowSystemInterfacePrivate::ApplicationStateChangedEvent::~Application
//      StateChangedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate28ApplicationStateChangedEventD1Ev(
    QWindowSystemInterfacePrivate::ApplicationStateChangedEvent *self) {
  delete self;
}
