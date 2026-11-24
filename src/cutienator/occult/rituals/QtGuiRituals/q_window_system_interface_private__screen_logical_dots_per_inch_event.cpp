//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent::ScreenLogic
//      alDotsPerInchEvent(QScreen *s, qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent *ritual_ZN29QWindowSystemInterfacePrivate29ScreenLogicalDotsPerInchEventC1EP7QScreendd(
    QScreen *s,
    qreal dx,
    qreal dy) {
  return new QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent(
      s,
      dx,
      dy);
}

//  QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent::~ScreenLogi
//      calDotsPerInchEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate29ScreenLogicalDotsPerInchEventD1Ev(
    QWindowSystemInterfacePrivate::ScreenLogicalDotsPerInchEvent *self) {
  delete self;
}
