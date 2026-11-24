//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent::SafeAreaMargi
//      nsChangedEvent(QWindow *w)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent *ritual_ZN29QWindowSystemInterfacePrivate27SafeAreaMarginsChangedEventC1EP7QWindow(
    QWindow *w) {
  return new QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent(w);
}

//  QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent::~SafeAreaMarg
//      insChangedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate27SafeAreaMarginsChangedEventD1Ev(
    QWindowSystemInterfacePrivate::SafeAreaMarginsChangedEvent *self) {
  delete self;
}
