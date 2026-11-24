//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::FocusWindowEvent::FocusWindowEvent(QWindow
//      *focusedWindow, Qt::FocusReason r)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::FocusWindowEvent *ritual_ZN29QWindowSystemInterfacePrivate16FocusWindowEventC1EP7QWindowN2Qt11FocusReasonE(
    QWindow *focusedWindow,
    Qt::FocusReason r) {
  return new QWindowSystemInterfacePrivate::FocusWindowEvent(
      focusedWindow,
      r);
}

//  QWindowSystemInterfacePrivate::FocusWindowEvent::~FocusWindowEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate16FocusWindowEventD1Ev(
    QWindowSystemInterfacePrivate::FocusWindowEvent *self) {
  delete self;
}
