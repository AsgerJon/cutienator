//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::PointerEvent::PointerEvent(QWindow *w,
//      ulong time, EventType t, Qt::KeyboardModifiers mods, const
//      QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::PointerEvent *ritual_ZN29QWindowSystemInterfacePrivate12PointerEventC1EP7QWindowmNS_9EventTypeE6QFlagsIN2Qt16KeyboardModifierEEPK15QPointingDevice(
    QWindow *w,
    ulong time,
    QWindowSystemInterfacePrivate::EventType t,
    int mods,
    const QPointingDevice *device) {
  return new QWindowSystemInterfacePrivate::PointerEvent(
      w,
      time,
      t,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      device);
}

//  QWindowSystemInterfacePrivate::PointerEvent::~PointerEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate12PointerEventD1Ev(
    QWindowSystemInterfacePrivate::PointerEvent *self) {
  delete self;
}
