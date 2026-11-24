//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QWindowSystemInterfacePrivate::WheelEvent::WheelEvent(QWindow *w, ulong
//      time, const QPointF &local, const QPointF &global, QPoint pixelD,
//      QPoint angleD, int qt4D, Qt::Orientation qt4O, Qt::KeyboardModifiers
//      mods, Qt::ScrollPhase phase, Qt::MouseEventSource src, bool inverted,
//      const QPointingDevice *device)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WheelEvent *ritual_ZN29QWindowSystemInterfacePrivate10WheelEventC1EP7QWindowmRK7QPointFS5_6QPointS6_iN2Qt11OrientationE6QFlagsINS7_16KeyboardModifierEENS7_11ScrollPhaseENS7_16MouseEventSourceEbPK15QPointingDevice(
    QWindow *w,
    ulong time,
    const QPointF *local,
    const QPointF *global,
    const QPoint *pixelD,
    const QPoint *angleD,
    int qt4D,
    Qt::Orientation qt4O,
    int mods,
    Qt::ScrollPhase phase,
    Qt::MouseEventSource src,
    bool inverted,
    const QPointingDevice *device) {
  return new QWindowSystemInterfacePrivate::WheelEvent(
      w,
      time,
      *local,
      *global,
      *pixelD,
      *angleD,
      qt4D,
      qt4O,
      QFlags<Qt::KeyboardModifier>::fromInt(mods),
      phase,
      src,
      inverted,
      device);
}

//  QWindowSystemInterfacePrivate::WheelEvent::~WheelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10WheelEventD1Ev(
    QWindowSystemInterfacePrivate::WheelEvent *self) {
  delete self;
}
