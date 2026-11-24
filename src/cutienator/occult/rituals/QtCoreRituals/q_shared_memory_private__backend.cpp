//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(sharedmemory)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsharedmemory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSharedMemoryPrivate::Backend::Backend()
extern "C" Q_DECL_EXPORT
QSharedMemoryPrivate::Backend *ritual_ZN20QSharedMemoryPrivate7BackendC1Ev() {
  return new QSharedMemoryPrivate::Backend();
}

//  QSharedMemoryPrivate::Backend::~Backend()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemoryPrivate7BackendD1Ev(
    QSharedMemoryPrivate::Backend *self) {
  delete self;
}

#endif  // QT_CONFIG(sharedmemory)
