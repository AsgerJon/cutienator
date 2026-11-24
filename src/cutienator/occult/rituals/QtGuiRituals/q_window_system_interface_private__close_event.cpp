//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::CloseEvent::CloseEvent(QWindow *w)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::CloseEvent *ritual_ZN29QWindowSystemInterfacePrivate10CloseEventC1EP7QWindow(
    QWindow *w) {
  return new QWindowSystemInterfacePrivate::CloseEvent(w);
}

//  QWindowSystemInterfacePrivate::CloseEvent::~CloseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10CloseEventD1Ev(
    QWindowSystemInterfacePrivate::CloseEvent *self) {
  delete self;
}
