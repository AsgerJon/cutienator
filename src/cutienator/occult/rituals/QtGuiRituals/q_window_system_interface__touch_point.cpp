//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterface::TouchPoint::TouchPoint()
extern "C" Q_DECL_EXPORT
QWindowSystemInterface::TouchPoint *ritual_ZN22QWindowSystemInterface10TouchPointC1Ev() {
  return new QWindowSystemInterface::TouchPoint();
}

//  QWindowSystemInterface::TouchPoint::~TouchPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QWindowSystemInterface10TouchPointD1Ev(
    QWindowSystemInterface::TouchPoint *self) {
  delete self;
}
