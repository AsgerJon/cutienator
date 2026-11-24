//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSystemSemaphorePrivate::Backend::Backend()
extern "C" Q_DECL_EXPORT
QSystemSemaphorePrivate::Backend *ritual_ZN23QSystemSemaphorePrivate7BackendC1Ev() {
  return new QSystemSemaphorePrivate::Backend();
}

//  QSystemSemaphorePrivate::Backend::~Backend()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate7BackendD1Ev(
    QSystemSemaphorePrivate::Backend *self) {
  delete self;
}

#endif  // QT_CONFIG(systemsemaphore)
