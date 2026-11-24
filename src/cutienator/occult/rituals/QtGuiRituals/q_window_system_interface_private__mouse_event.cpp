//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QWindowSystemInterfacePrivate::MouseEvent::MouseEvent(QWindow *w, ulong
//      time, const QPointF &local, const QPointF &global, Qt::MouseButtons
//      state, Qt::KeyboardModifiers mods, Qt::MouseButton b, QEvent::Type
//      type, Qt::MouseEventSource src, bool frame, const QPointingDevice
//      *device, int evPtId)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::MouseEvent *ritual_ZN29QWindowSystemInterfacePrivate10MouseEventC1EP7QWindowmRK7QPointFS5_6QFlagsIN2Qt11MouseButtonEES6_INS7_16KeyboardModifierEES8_N6QEvent4TypeENS7_16MouseEventSourceEbPK15QPointingDevicei(
    QWindow *w,
    ulong time,
    const QPointF *local,
    const QPointF *global,
    int state,
    int mods,
    Qt::MouseButton b,
    QEvent::Type type,
    Qt::MouseEventSource src,
    bool frame,
    const QPointingDevice *device,
    int evPtId) {
  return new QWindowSystemInterfacePrivate::MouseEvent(
      w,
      time,
      *local,
      *global,
      QFlags<Qt::MouseButton>::fromInt(state),
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      b,
      type,
      src,
      frame,
      device,
      evPtId);
}

//  QWindowSystemInterfacePrivate::MouseEvent::~MouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10MouseEventD1Ev(
    QWindowSystemInterfacePrivate::MouseEvent *self) {
  delete self;
}
