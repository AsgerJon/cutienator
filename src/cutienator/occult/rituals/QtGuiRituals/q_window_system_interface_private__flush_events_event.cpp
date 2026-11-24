//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::FlushEventsEvent::FlushEventsEvent(QEventL
//      oop::ProcessEventsFlags f)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::FlushEventsEvent *ritual_ZN29QWindowSystemInterfacePrivate16FlushEventsEventC1E6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    int f) {
  return new QWindowSystemInterfacePrivate::FlushEventsEvent(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(f));
}

//  QWindowSystemInterfacePrivate::FlushEventsEvent::~FlushEventsEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate16FlushEventsEventD1Ev(
    QWindowSystemInterfacePrivate::FlushEventsEvent *self) {
  delete self;
}
