//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>

//  QWindowSystemInterfacePrivate::PaintEvent::PaintEvent(QWindow *window,
//      const QRegion &region)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::PaintEvent *ritual_ZN29QWindowSystemInterfacePrivate10PaintEventC1EP7QWindowRK7QRegion(
    QWindow *window,
    const QRegion *region) {
  return new QWindowSystemInterfacePrivate::PaintEvent(window, *region);
}

//  QWindowSystemInterfacePrivate::PaintEvent::~PaintEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate10PaintEventD1Ev(
    QWindowSystemInterfacePrivate::PaintEvent *self) {
  delete self;
}
