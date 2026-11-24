//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QWindowSystemInterfacePrivate::EnterEvent::EnterEvent(QWindow *enter,
//      const QPointF &local, const QPointF &global)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::EnterEvent *ritual_ZN29QWindowSystemInterfacePrivate10EnterEventC1EP7QWindowRK7QPointFS5_(
    QWindow *enter,
    const QPointF *local,
    const QPointF *global) {
  return new QWindowSystemInterfacePrivate::EnterEvent(
      enter,
      *local,
      *global);
}

//  QWindowSystemInterfacePrivate::EnterEvent::~EnterEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10EnterEventD1Ev(
    QWindowSystemInterfacePrivate::EnterEvent *self) {
  delete self;
}
