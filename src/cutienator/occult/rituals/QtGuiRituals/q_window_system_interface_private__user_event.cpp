//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::UserEvent::UserEvent(QWindow *w, ulong
//      time, EventType t)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::UserEvent *ritual_ZN29QWindowSystemInterfacePrivate9UserEventC1EP7QWindowmNS_9EventTypeE(
    QWindow *w,
    ulong time,
    QWindowSystemInterfacePrivate::EventType t) {
  return new QWindowSystemInterfacePrivate::UserEvent(w, time, t);
}

//  QWindowSystemInterfacePrivate::UserEvent::~UserEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate9UserEventD1Ev(
    QWindowSystemInterfacePrivate::UserEvent *self) {
  delete self;
}
