//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::WindowScreenChangedEvent::WindowScreenChan
//      gedEvent(QWindow *w, QScreen *s)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowScreenChangedEvent *ritual_ZN29QWindowSystemInterfacePrivate24WindowScreenChangedEventC1EP7QWindowP7QScreen(
    QWindow *w,
    QScreen *s) {
  return new QWindowSystemInterfacePrivate::WindowScreenChangedEvent(w, s);
}

//  QWindowSystemInterfacePrivate::WindowScreenChangedEvent::~WindowScreenCha
//      ngedEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate24WindowScreenChangedEventD1Ev(
    QWindowSystemInterfacePrivate::WindowScreenChangedEvent *self) {
  delete self;
}
