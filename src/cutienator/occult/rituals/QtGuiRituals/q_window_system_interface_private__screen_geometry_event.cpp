//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QWindowSystemInterfacePrivate::ScreenGeometryEvent::ScreenGeometryEvent(Q
//      Screen *s, const QRect &g, const QRect &ag)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ScreenGeometryEvent *ritual_ZN29QWindowSystemInterfacePrivate19ScreenGeometryEventC1EP7QScreenRK5QRectS5_(
    QScreen *s,
    const QRect *g,
    const QRect *ag) {
  return new QWindowSystemInterfacePrivate::ScreenGeometryEvent(s, *g, *ag);
}

//  QWindowSystemInterfacePrivate::ScreenGeometryEvent::~ScreenGeometryEvent(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate19ScreenGeometryEventD1Ev(
    QWindowSystemInterfacePrivate::ScreenGeometryEvent *self) {
  delete self;
}
