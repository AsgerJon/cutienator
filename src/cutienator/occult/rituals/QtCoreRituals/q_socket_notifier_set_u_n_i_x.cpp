//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSocketNotifierSetUNIX::QSocketNotifierSetUNIX()
extern "C" Q_DECL_EXPORT
QSocketNotifierSetUNIX *ritual_ZN22QSocketNotifierSetUNIXC1Ev() {
  return new QSocketNotifierSetUNIX();
}

//  bool QSocketNotifierSetUNIX::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QSocketNotifierSetUNIX7isEmptyEv(
    const QSocketNotifierSetUNIX *self) {
  return self->isEmpty();
}

//  short QSocketNotifierSetUNIX::events() const
extern "C" Q_DECL_EXPORT
short ritual_ZNK22QSocketNotifierSetUNIX6eventsEv(
    const QSocketNotifierSetUNIX *self) {
  return self->events();
}

//  QSocketNotifierSetUNIX::~QSocketNotifierSetUNIX()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSocketNotifierSetUNIXD1Ev(QSocketNotifierSetUNIX *self) {
  delete self;
}
