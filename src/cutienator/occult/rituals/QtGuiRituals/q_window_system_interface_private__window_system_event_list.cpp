//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QWindowSystemInterfacePrivate::WindowSystemEventList::WindowSystemEventLi
//      st()
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEventList *ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventListC1Ev() {
  return new QWindowSystemInterfacePrivate::WindowSystemEventList();
}

//  QWindowSystemInterfacePrivate::WindowSystemEventList::~WindowSystemEventL
//      ist()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventListD1Ev(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self) {
  delete self;
}

//  void QWindowSystemInterfacePrivate::WindowSystemEventList::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList5clearEv(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self) {
  self->clear();
}

//  void QWindowSystemInterfacePrivate::WindowSystemEventList::prepend(Window
//      SystemEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList7prependEPNS_17WindowSystemEventE(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self,
    QWindowSystemInterfacePrivate::WindowSystemEvent *e) {
  self->prepend(e);
}

//  WindowSystemEvent *QWindowSystemInterfacePrivate::WindowSystemEventList::
//      takeFirstOrReturnNull()
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList21takeFirstOrReturnNullEv(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self) {
  return self->takeFirstOrReturnNull();
}

//  WindowSystemEvent *QWindowSystemInterfacePrivate::WindowSystemEventList::
//      takeFirstNonUserInputOrReturnNull()
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList33takeFirstNonUserInputOrReturnNullEv(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self) {
  return self->takeFirstNonUserInputOrReturnNull();
}

//  bool QWindowSystemInterfacePrivate::WindowSystemEventList::nonUserInputEv
//      entsQueued()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList24nonUserInputEventsQueuedEv(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self) {
  return self->nonUserInputEventsQueued();
}

//  void QWindowSystemInterfacePrivate::WindowSystemEventList::append(WindowS
//      ystemEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList6appendEPNS_17WindowSystemEventE(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self,
    QWindowSystemInterfacePrivate::WindowSystemEvent *e) {
  self->append(e);
}

//  qsizetype QWindowSystemInterfacePrivate::WindowSystemEventList::count()
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK29QWindowSystemInterfacePrivate21WindowSystemEventList5countEv(
    const QWindowSystemInterfacePrivate::WindowSystemEventList *self) {
  return self->count();
}

//  WindowSystemEvent *QWindowSystemInterfacePrivate::WindowSystemEventList::
//      peekAtFirstOfType(EventType t) const
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::WindowSystemEvent *ritual_ZNK29QWindowSystemInterfacePrivate21WindowSystemEventList17peekAtFirstOfTypeENS_9EventTypeE(
    const QWindowSystemInterfacePrivate::WindowSystemEventList *self,
    QWindowSystemInterfacePrivate::EventType t) {
  return self->peekAtFirstOfType(t);
}

//  void QWindowSystemInterfacePrivate::WindowSystemEventList::remove(const
//      WindowSystemEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate21WindowSystemEventList6removeEPKNS_17WindowSystemEventE(
    QWindowSystemInterfacePrivate::WindowSystemEventList *self,
    const QWindowSystemInterfacePrivate::WindowSystemEvent *e) {
  self->remove(e);
}
