//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qsizetype QWindowSystemInterfacePrivate::windowSystemEventsQueued()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN29QWindowSystemInterfacePrivate24windowSystemEventsQueuedEv() {
  return QWindowSystemInterfacePrivate::windowSystemEventsQueued();
}

//  bool QWindowSystemInterfacePrivate::nonUserInputEventsQueued()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QWindowSystemInterfacePrivate24nonUserInputEventsQueuedEv() {
  return QWindowSystemInterfacePrivate::nonUserInputEventsQueued();
}

//  WindowSystemEvent *QWindowSystemInterfacePrivate::getWindowSystemEvent()
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZN29QWindowSystemInterfacePrivate20getWindowSystemEventEv() {
  return QWindowSystemInterfacePrivate::getWindowSystemEvent();
}

//  WindowSystemEvent
//      *QWindowSystemInterfacePrivate::getNonUserInputWindowSystemEvent()
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZN29QWindowSystemInterfacePrivate32getNonUserInputWindowSystemEventEv() {
  return QWindowSystemInterfacePrivate::getNonUserInputWindowSystemEvent();
}

//  WindowSystemEvent
//      *QWindowSystemInterfacePrivate::peekWindowSystemEvent(EventType t)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZN29QWindowSystemInterfacePrivate21peekWindowSystemEventENS_9EventTypeE(
    QWindowSystemInterfacePrivate::EventType t) {
  return QWindowSystemInterfacePrivate::peekWindowSystemEvent(t);
}

//  void
//      QWindowSystemInterfacePrivate::removeWindowSystemEvent(WindowSystemEv
//      ent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate23removeWindowSystemEventEPNS_17WindowSystemEventE(
    QWindowSystemInterfacePrivate::WindowSystemEvent *event) {
  QWindowSystemInterfacePrivate::removeWindowSystemEvent(event);
}

//  QWindowSystemInterface::TouchPoint
//      QWindowSystemInterfacePrivate::toNativeTouchPoint(const QEventPoint
//      &point, const QWindow *window)
extern "C" Q_DECL_EXPORT
QWindowSystemInterface::TouchPoint *ritual_ZN29QWindowSystemInterfacePrivate18toNativeTouchPointERK11QEventPointPK7QWindow(
    const QEventPoint *point,
    const QWindow *window) {
  return new QWindowSystemInterface::TouchPoint(
      QWindowSystemInterfacePrivate::toNativeTouchPoint(
          *point,
          window));
}

//  void QWindowSystemInterfacePrivate::installWindowSystemEventHandler(QWind
//      owSystemEventHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate31installWindowSystemEventHandlerEP25QWindowSystemEventHandler(
    QWindowSystemEventHandler *handler) {
  QWindowSystemInterfacePrivate::installWindowSystemEventHandler(handler);
}

//  void QWindowSystemInterfacePrivate::removeWindowSystemEventhandler(QWindo
//      wSystemEventHandler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate30removeWindowSystemEventhandlerEP25QWindowSystemEventHandler(
    QWindowSystemEventHandler *handler) {
  QWindowSystemInterfacePrivate::removeWindowSystemEventhandler(handler);
}

//  QWindowSystemInterfacePrivate::~QWindowSystemInterfacePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivateD1Ev(
    QWindowSystemInterfacePrivate *self) {
  delete self;
}
