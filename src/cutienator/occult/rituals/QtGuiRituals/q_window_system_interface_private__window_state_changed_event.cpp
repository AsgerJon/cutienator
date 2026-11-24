//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::WindowStateChangedEvent::WindowStateChange
//      dEvent(QWindow *_window, Qt::WindowStates _newState, Qt::WindowStates
//      _oldState)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowStateChangedEvent *ritual_ZN29QWindowSystemInterfacePrivate23WindowStateChangedEventC1EP7QWindow6QFlagsIN2Qt11WindowStateEES6_(
    QWindow *_window,
    int _newState,
    int _oldState) {
  return new QWindowSystemInterfacePrivate::WindowStateChangedEvent(
      _window,
      QFlags<Qt::WindowState>::fromInt(_newState),
      QFlags<Qt::WindowState>::fromInt(_oldState));
}

//  QWindowSystemInterfacePrivate::WindowStateChangedEvent::~WindowStateChang
//      edEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate23WindowStateChangedEventD1Ev(
    QWindowSystemInterfacePrivate::WindowStateChangedEvent *self) {
  delete self;
}
