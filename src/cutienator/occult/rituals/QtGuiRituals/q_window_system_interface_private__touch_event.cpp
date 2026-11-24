//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qlist.h>

//  QWindowSystemInterfacePrivate::TouchEvent::TouchEvent(QWindow *w, ulong
//      time, QEvent::Type t, const QPointingDevice *device, const
//      QList<QEventPoint> &p, Qt::KeyboardModifiers mods)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::TouchEvent *ritual_ZN29QWindowSystemInterfacePrivate10TouchEventC1EP7QWindowmN6QEvent4TypeEPK15QPointingDeviceRK5QListI11QEventPointE6QFlagsIN2Qt16KeyboardModifierEE(
    QWindow *w,
    ulong time,
    QEvent::Type t,
    const QPointingDevice *device,
    const QList<QEventPoint> *p,
    int mods) {
  return new QWindowSystemInterfacePrivate::TouchEvent(
      w,
      time,
      t,
      device,
      *p,
      QFlags<Qt::KeyboardModifier>::fromInt(mods));
}

//  QWindowSystemInterfacePrivate::TouchEvent::~TouchEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10TouchEventD1Ev(
    QWindowSystemInterfacePrivate::TouchEvent *self) {
  delete self;
}
