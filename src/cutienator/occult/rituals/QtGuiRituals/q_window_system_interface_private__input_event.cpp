//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::InputEvent::InputEvent(QWindow *w, ulong
//      time, EventType t, Qt::KeyboardModifiers mods, const QInputDevice
//      *dev)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::InputEvent *ritual_ZN29QWindowSystemInterfacePrivate10InputEventC1EP7QWindowmNS_9EventTypeE6QFlagsIN2Qt16KeyboardModifierEEPK12QInputDevice(
    QWindow *w,
    ulong time,
    QWindowSystemInterfacePrivate::EventType t,
    int mods,
    const QInputDevice *dev) {
  return new QWindowSystemInterfacePrivate::InputEvent(
      w,
      time,
      t,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      dev);
}

//  QWindowSystemInterfacePrivate::InputEvent::~InputEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10InputEventD1Ev(
    QWindowSystemInterfacePrivate::InputEvent *self) {
  delete self;
}
